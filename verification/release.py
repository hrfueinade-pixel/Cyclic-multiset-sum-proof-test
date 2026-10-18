"""Build and inspect a versioned review bundle; never substitutes for verify.py."""

from __future__ import annotations

import argparse
import gzip
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import tarfile

from verification.book import ROOT, git, sha
from verification.regeneration import output_directory


def digest(data):
    return hashlib.sha256(data).hexdigest()


def version_check(version):
    if not re.fullmatch(r"v\d+\.\d+\.\d+-review\.\d+", version):
        raise ValueError("Use a review version such as v0.1.0-review.1")
    return version


def evidence_check(record, manifest):
    summary = record.get("summary", {})
    parity = summary.get("parity", {})
    if (
        record.get("exit_code") != 0
        or summary.get("scope") != "full"
        or summary.get("status") != "FULL_CHECKS_PASSED"
        or record.get("manifest_sha256") != manifest
        or summary.get("manifest_sha256") != manifest
        or parity.get("required_order_checks") != 150
        or parity.get("completed_order_checks") != 150
        or parity.get("reused_completed_orders") != 0
        or summary.get("failure_controls") != "PASSED"
        or summary.get("privacy") != "PASSED"
    ):
        raise ValueError(
            "Release requires complete fresh verification of this source manifest"
        )


def pdf_check(pdf, report, commit, manifest):
    if (
        not pdf.startswith(b"%PDF-")
        or report.get("kind") != "typeset-proof"
        or report.get("source_commit") != commit
        or report.get("dirty_preview") is not False
        or report.get("source_manifest_sha256") != manifest
        or report.get("pdf_sha256") != digest(pdf)
    ):
        raise ValueError("PDF and its build report must belong to the release commit")


def generation_check(record, catalog, manifest):
    recipes = {r["id"]: r for r in catalog["recipes"]}
    rows = record.get("recipes", [])
    if (
        record.get("status") != "COMPLETE"
        or record.get("source_manifest_sha256") != manifest
        or record.get("archive_commit") != catalog["archive_commit"]
        or len(rows) != len(recipes)
        or {r.get("recipe") for r in rows} != set(recipes)
    ):
        raise ValueError(
            "Release needs all seven current discovery recipes, without duplicates"
        )
    for row in rows:
        recipe = recipes[row["recipe"]]
        count = row.get("validation", {}).get(
            "forced_distinct_repeated_values",
            row.get("validation", {}).get("distinct_repeated_values", 0),
        )
        if (
            row.get("status") != "POSITIVE_CERTIFICATE_VERIFIED"
            or count < recipe["required_values"]
            or row.get("certificate") != Path(recipe["certificate"]).name
            or not re.fullmatch(r"[a-z0-9_-]+", row.get("work_directory", ""))
            or row.get("scripts")
            != {p: catalog["program_sha256"][p] for p in recipe["scripts"]}
        ):
            raise ValueError("Incomplete or altered generation contract")


def read_tar(data):
    files = {}
    with tarfile.open(fileobj=io.BytesIO(data), mode="r:*") as archive:
        for member in archive:
            name = PurePosixPath(member.name)
            if name.is_absolute() or ".." in name.parts or "\\" in member.name:
                raise ValueError("Unsafe archive path")
            if member.isdir():
                continue
            if not member.isfile() or member.name in files:
                raise ValueError(
                    "Archive contains a link, special file, or duplicate name"
                )
            files[member.name] = archive.extractfile(member).read()
    return files


def tar_bytes(files, epoch):
    stream = io.BytesIO()
    with tarfile.open(fileobj=stream, mode="w", format=tarfile.PAX_FORMAT) as archive:
        for name, data in sorted(files.items()):
            info = tarfile.TarInfo(name)
            info.size, info.mode, info.mtime = len(data), 0o644, epoch
            archive.addfile(info, io.BytesIO(data))
    return gzip.compress(stream.getvalue(), mtime=0)


def checksum_text(files):
    return "".join(f"{digest(data)}  {name}\n" for name, data in sorted(files.items()))


def verify_bundle(path, expected_commit=None):
    packed = read_tar(Path(path).read_bytes())
    prefixes = {name.split("/", 1)[0] for name in packed}
    if len(prefixes) != 1:
        raise ValueError("Review bundle needs one top-level directory")
    prefix = prefixes.pop() + "/"
    files = {name[len(prefix) :]: data for name, data in packed.items()}
    metadata = json.loads(files["release.json"])
    version = version_check(metadata["version"])
    if metadata.get("format") != 1 or metadata.get("prerelease") is not True:
        raise ValueError("Unsupported review release format")
    if prefix != f"cyclic-multiset-sums-{version}/":
        raise ValueError("Bundle directory and version disagree")
    if expected_commit is not None and metadata["source_commit"] != expected_commit:
        raise ValueError("Unexpected release commit")
    listed = metadata["files"]
    if set(files) != set(listed) | {"release.json", "SHA256SUMS"}:
        raise ValueError("Missing or unlisted bundle file")
    for name, expected in listed.items():
        if (
            digest(files[name]) != expected["sha256"]
            or len(files[name]) != expected["bytes"]
        ):
            raise ValueError("Bundle content changed: " + name)
    if files["SHA256SUMS"].decode() != checksum_text(
        {k: v for k, v in files.items() if k != "SHA256SUMS"}
    ):
        raise ValueError("Bundle checksum inventory disagrees")
    manifest_bytes = files["source/certificates/manifest.json"]
    manifest_hash = digest(manifest_bytes)
    if manifest_hash != metadata["source_manifest_sha256"]:
        raise ValueError("Release source manifest mismatch")
    for item in json.loads(manifest_bytes)["files"]:
        data = files["source/" + item["path"]]
        if digest(data) != item["sha256"] or len(data) != item["bytes"]:
            raise ValueError("Source inventory mismatch: " + item["path"])
    for name, expected in metadata["certificate_sha256"].items():
        if digest(files["source/" + name]) != expected:
            raise ValueError("Certificate hash mismatch")
    evidence_check(
        json.loads(gzip.decompress(files["verification.json.gz"])), manifest_hash
    )
    pdf_check(
        files["proof.pdf"],
        json.loads(files["proof-build.json"]),
        metadata["source_commit"],
        manifest_hash,
    )
    generation = json.loads(files["regeneration/regeneration.json"])
    catalog = json.loads(files["source/docs/generation.json"])
    generation_check(generation, catalog, manifest_hash)
    for name, expected in catalog["program_sha256"].items():
        if digest(files["regeneration/programs/" + name]) != expected:
            raise ValueError("Recovered program mismatch")
    for row in generation["recipes"]:
        name = (
            "regeneration/generated/" + row["work_directory"] + "/" + row["certificate"]
        )
        if digest(files[name]) != row["sha256"]:
            raise ValueError("Regenerated certificate mismatch")
    return {
        "version": version,
        "source_commit": metadata["source_commit"],
        "source_manifest_sha256": manifest_hash,
        "files": len(files),
        "bundle_sha256": sha(path),
        "scope": "Artifact integrity and binding; run verify.py for mathematical certificate verification.",
    }


def build(version, output, pdf, evidence, regenerated, recovered, root=ROOT):
    version_check(version)
    configuration = json.loads((root / "docs/release.json").read_text())
    if (
        configuration["version"] != version
        or configuration.get("prerelease") is not True
    ):
        raise ValueError("Release configuration must select this review prerelease")
    if git(root, "status", "--porcelain"):
        raise ValueError("Review releases require a clean committed source tree")
    output = output_directory(root, output)
    if output.exists():
        raise ValueError("Release destination must not already exist")
    commit = git(root, "rev-parse", "HEAD")
    manifest = sha(root / "certificates/manifest.json")
    evidence_bytes, pdf_bytes = Path(evidence).read_bytes(), Path(pdf).read_bytes()
    evidence_check(json.loads(gzip.decompress(evidence_bytes)), manifest)
    pdf_report_bytes = Path(pdf).with_suffix(".json").read_bytes()
    pdf_check(pdf_bytes, json.loads(pdf_report_bytes), commit, manifest)
    generated_report = json.loads((Path(regenerated) / "regeneration.json").read_text())
    catalog = json.loads((root / "docs/generation.json").read_text())
    generation_check(generated_report, catalog, manifest)
    source = read_tar(
        subprocess.check_output(
            ["git", "-C", str(root), "archive", "--format=tar", commit]
        )
    )
    files = {"source/" + name: data for name, data in source.items()}
    files.update(
        {
            "proof.pdf": pdf_bytes,
            "proof-build.json": pdf_report_bytes,
            "proof-build.log": Path(pdf).with_suffix(".build.log").read_bytes(),
            "verification.json.gz": evidence_bytes,
            "regeneration/regeneration.json": (
                Path(regenerated) / "regeneration.json"
            ).read_bytes(),
            "regeneration/recovery.json": (
                Path(recovered) / "recovery.json"
            ).read_bytes(),
        }
    )
    catalog = json.loads((root / "docs/generation.json").read_text())
    for name, expected in catalog["program_sha256"].items():
        data = (Path(recovered) / "programs" / name).read_bytes()
        if digest(data) != expected:
            raise ValueError("Recovered program changed: " + name)
        files["regeneration/programs/" + name] = data
    for row in generated_report["recipes"]:
        if row["status"] != "POSITIVE_CERTIFICATE_VERIFIED":
            raise ValueError(
                "A discovery recipe did not produce a verified positive certificate"
            )
        work = Path(regenerated) / row["work_directory"]
        if digest((work / row["certificate"]).read_bytes()) != row["sha256"]:
            raise ValueError("Regenerated certificate changed")
        for path in sorted(work.iterdir()):
            if path.is_file() and path.suffix != ".py":
                files["regeneration/generated/" + work.name + "/" + path.name] = (
                    path.read_bytes()
                )
    notes = (
        f"# {configuration['name']}\n\n{configuration['status']}\n\n"
        f"Version: {version}\n\nSource commit: {commit}\n\n"
        "Read proof.pdf or source/PROOF.md. Re-run the proof from source with Python 3.12+: "
        "python verify.py --seconds-per-order 300.\n\n"
        "To rediscover the seven early positive certificates offline, run from source/: "
        "python -m verification.regeneration generate --recipe all --programs ../regeneration/programs. "
        "Complete later-family discovery is unavailable; see source/docs/generation.json.\n"
    )
    files["REVIEW.md"] = notes.encode()
    metadata = {
        "format": 1,
        "version": version,
        "prerelease": True,
        "source_commit": commit,
        "source_tree": git(root, "rev-parse", "HEAD^{tree}"),
        "source_manifest_sha256": manifest,
        "status": configuration["status"],
        "certificate_sha256": {
            k: digest(v) for k, v in source.items() if k.startswith("certificates/")
        },
        "files": {
            name: {"bytes": len(data), "sha256": digest(data)}
            for name, data in sorted(files.items())
        },
    }
    metadata_bytes = (json.dumps(metadata, indent=2) + "\n").encode()
    files["release.json"] = metadata_bytes
    files["SHA256SUMS"] = checksum_text(files).encode()
    output.mkdir(parents=True)
    prefix = f"cyclic-multiset-sums-{version}/"
    bundle = output / f"cyclic-multiset-sums-{version}.tar.gz"
    bundle.write_bytes(
        tar_bytes(
            {prefix + k: v for k, v in files.items()},
            int(git(root, "show", "-s", "--format=%ct", "HEAD")),
        )
    )
    (output / "cyclic-multiset-sums-proof.pdf").write_bytes(pdf_bytes)
    (output / "verification.json.gz").write_bytes(evidence_bytes)
    (output / "release.json").write_bytes(metadata_bytes)
    assets = {p.name: p.read_bytes() for p in output.iterdir()}
    (output / "SHA256SUMS").write_text(checksum_text(assets))
    result = verify_bundle(bundle, commit)
    # Scan public text and extracted PDF text; do not pretend binary PDF bytes are UTF-8.
    from privacy_check import payload_findings, text_findings

    findings = []
    for name, data in files.items():
        if name == "proof.pdf":
            text = subprocess.check_output(["pdftotext", str(pdf), "-"], text=True)
            findings += text_findings(name, text)
        else:
            findings += payload_findings(name, data, name.endswith(".gz"))
    if findings:
        raise ValueError(
            "Release privacy inspection found content requiring review: "
            + str(findings)
        )
    result["publication_privacy"] = "PASSED"
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="action", required=True)
    make = sub.add_parser("build")
    make.add_argument("--version", required=True)
    make.add_argument(
        "--output", type=Path, default=ROOT / ".verification/publication/release"
    )
    make.add_argument(
        "--pdf", type=Path, default=ROOT / ".verification/publication/proof.pdf"
    )
    make.add_argument(
        "--evidence",
        type=Path,
        default=ROOT / ".verification/publication/verification.json.gz",
    )
    make.add_argument(
        "--regenerated", type=Path, default=ROOT / ".verification/regenerated"
    )
    make.add_argument(
        "--recovered", type=Path, default=ROOT / ".verification/recovered"
    )
    inspect = sub.add_parser("verify")
    inspect.add_argument("bundle", type=Path)
    inspect.add_argument("--commit")
    args = parser.parse_args()
    try:
        result = (
            verify_bundle(args.bundle, args.commit)
            if args.action == "verify"
            else build(
                args.version,
                args.output,
                args.pdf,
                args.evidence,
                args.regenerated,
                args.recovered,
            )
        )
        print(json.dumps(result, indent=2))
    except (ValueError, KeyError, OSError, subprocess.CalledProcessError) as error:
        parser.exit(1, str(error) + "\n")


if __name__ == "__main__":
    main()
