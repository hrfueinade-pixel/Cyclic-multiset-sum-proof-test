"""Recover archived inputs and rediscover seven positive certificates in isolation."""

from __future__ import annotations

import argparse
import gzip
import hashlib
import importlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent.parent


def digest(data):
    return hashlib.sha256(data).hexdigest()


def archive_blob(root, commit, name):
    if Path(name).name != name or not name.startswith("stage"):
        raise ValueError("Unsafe historical input name")
    result = subprocess.run(
        ["git", "-C", str(root), "show", commit + ":" + name], capture_output=True
    )
    if result.returncode:
        raise ValueError(
            f"Historical input unavailable: {commit}:{name}; use a full Git clone"
        )
    return result.stdout


def output_directory(root, output):
    output = Path(output).resolve()
    try:
        relative = output.relative_to(root.resolve())
    except ValueError:
        return output
    if not relative.parts or relative.parts[0] != ".verification":
        raise ValueError(
            "Generated material inside the repository must go under .verification/"
        )
    return output


def completed_reference(parts):
    rows = {}
    for raw in parts:
        for row in json.loads(raw)["reports"]:
            if row.get("completion") != "COMPLETE":
                continue
            order = row["M"]
            if order in rows:
                raise ValueError("Duplicate completed reference order")
            rows[order] = row
    if set(rows) != set(range(94, 124)):
        raise ValueError("Historical references do not complete all 30 required orders")
    return (
        json.dumps(
            {
                "completion": "COMPLETE",
                "completed_orders": sorted(rows),
                "reports": [rows[n] for n in sorted(rows)],
                "scope": "Only fully completed per-order reference records; partial search states excluded.",
            },
            indent=2,
        )
        + "\n"
    ).encode()


def recover_payload(entry, load):
    names = entry["source_files"]
    parts = [load(name) for name in names]
    if entry["transformation"] == "byte-identical copy":
        if len(parts) != 1:
            raise ValueError("A copied input must have exactly one source")
        data = parts[0]
    elif entry["transformation"] == "exact concatenation":
        base = names[0].split(".part")[0]
        if names != [base + ".part" + str(i).zfill(3) for i in range(len(names))]:
            raise ValueError("Missing or reordered archive part")
        data = b"".join(parts)
    elif entry["path"] == "certificates/parity/four-four-reference.json":
        data = completed_reference(parts)
    else:
        raise ValueError("Unsupported historical transformation")
    if digest(data) != entry["sha256"]:
        raise ValueError("Recovered input hash mismatch: " + entry["path"])
    return data


def recover(root, output, programs=False):
    output = output_directory(root, output)
    if output.exists():
        raise ValueError("Recovery destination must not already exist")
    catalog = json.loads((root / "docs/generation.json").read_text())
    source = json.loads((root / "docs/source-map.json").read_text())
    if source["archive_commit"] != catalog["archive_commit"]:
        raise ValueError("Archive revisions disagree")
    load = lambda name: archive_blob(root, catalog["archive_commit"], name)
    files = {}
    for entry in source["retained_files"]:
        if entry["path"].startswith("certificates/"):
            files[entry["path"]] = recover_payload(entry, load)
    if programs:
        for name, expected in catalog["program_sha256"].items():
            data = load(name)
            if digest(data) != expected:
                raise ValueError("Historical program hash mismatch")
            files["programs/" + name] = data
    output.mkdir(parents=True)
    for name, data in files.items():
        destination = output / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(data)
    report = {
        "format": 1,
        "kind": "archive-recovery",
        "archive_commit": catalog["archive_commit"],
        "files": [
            {"path": k, "bytes": len(v), "sha256": digest(v)} for k, v in files.items()
        ],
        "scope": "Restores historical bytes; does not rerun discovery or establish mathematical exclusions.",
    }
    (output / "recovery.json").write_text(json.dumps(report, indent=2) + "\n")
    return report


def validate(path, recipe):
    if sys.flags.optimize:
        raise ValueError(
            "Certificate validation requires assertions; do not use Python -O"
        )
    name = "multiplicity_models" if recipe["schema"] == "stage41" else "cubic_exception"
    checker = importlib.import_module("verification.checks." + name)
    result = checker.check_file(Path(path))
    if isinstance(result.get("file"), Path):
        result["file"] = result["file"].name
    data = json.loads(gzip.decompress(Path(path).read_bytes()))
    if len(data["words"]) < recipe["required_values"]:
        raise ValueError("Discovery did not reach the required positive growth bound")
    return result


def generate_one(root, output, catalog, recipe, seconds, programs=None):
    record = {
        "recipe": recipe["id"],
        "archive_commit": catalog["archive_commit"],
        "status": "INCOMPLETE",
        "scripts": {},
        "required_values": recipe["required_values"],
    }
    output.mkdir(parents=True, exist_ok=True)
    # A new isolated directory prevents a missing result from reusing an old certificate.
    work = Path(tempfile.mkdtemp(prefix=recipe["id"] + "-", dir=output))
    record["work_directory"] = work.name
    try:
        for name in recipe["scripts"]:
            data = (
                (Path(programs) / name).read_bytes()
                if programs
                else archive_blob(root, catalog["archive_commit"], name)
            )
            expected = catalog["program_sha256"][name]
            if digest(data) != expected:
                raise ValueError("Historical generator hash mismatch")
            (work / name).write_bytes(data)
            record["scripts"][name] = expected
        command = [
            sys.executable,
            "-B",
            recipe["program"],
            "--model",
            recipe["model"],
            "--degree",
            str(recipe["degree"]),
            "--target",
            str(recipe["required_values"]),
        ]
        if recipe["schema"] == "stage41":
            command += [
                "--integer-rays",
                "--units",
                ",".join(map(str, recipe["units"])),
                "--output",
                "discovery.json",
            ]
        record["command"] = ["python", *command[1:]]
        env = os.environ.copy()
        env.pop("PYTHONOPTIMIZE", None)
        env["PYTHONHASHSEED"] = "0"
        with (work / "discovery.log").open("w") as log:
            process = subprocess.run(
                command,
                cwd=work,
                env=env,
                stdout=log,
                stderr=subprocess.STDOUT,
                timeout=seconds,
            )
        record["exit_code"] = process.returncode
        if process.returncode:
            raise ValueError("Historical discovery failed; inspect discovery.log")
        destination = work / Path(recipe["certificate"]).name
        if recipe["schema"] == "stage41":
            raw = json.loads((work / "discovery.json").read_text())
            data = {
                "model": recipe["model"],
                "degree": recipe["degree"],
                "units": recipe["units"],
                "words": [
                    "".join(map(str, x["quartic_word"])) for x in raw["selected"]
                ],
                "rivals": [
                    x[2] if isinstance(x, list) else "".join(map(str, x["rival"]))
                    for x in raw["pair_certificates"]
                ],
            }
            destination.write_bytes(
                gzip.compress(json.dumps(data, separators=(",", ":")).encode(), mtime=0)
            )
            record["packaging"] = (
                "Single-case projection of the archived stage41 packager; no saved discovery result used"
            )
        else:
            generated = (
                work
                / f"stage42_{recipe['model']}_degree{recipe['degree']}_certificate.json.gz"
            )
            destination.write_bytes(generated.read_bytes())
        # The current verifier is imported only after the archived producer process exits.
        record["validation"] = validate(destination, recipe)
        published = root / recipe["certificate"]
        record.update(
            {
                "status": "POSITIVE_CERTIFICATE_VERIFIED",
                "certificate": destination.name,
                "sha256": digest(destination.read_bytes()),
                "byte_identical_to_published": destination.read_bytes()
                == published.read_bytes(),
                "same_json_as_published": json.loads(
                    gzip.decompress(destination.read_bytes())
                )
                == json.loads(gzip.decompress(published.read_bytes())),
            }
        )
    except (
        ValueError,
        AssertionError,
        KeyError,
        OSError,
        subprocess.TimeoutExpired,
    ) as error:
        record["error"] = str(error)
    (work / "result.json").write_text(json.dumps(record, indent=2) + "\n")
    return record


def generate(root, output, selected, seconds=180, programs=None):
    if sys.flags.optimize:
        raise ValueError("Certificate validation requires assertions")
    output = output_directory(root, output)
    catalog = json.loads((root / "docs/generation.json").read_text())
    recipes = (
        catalog["recipes"]
        if selected == "all"
        else [r for r in catalog["recipes"] if r["id"] == selected]
    )
    if not recipes:
        raise ValueError("Unknown discovery recipe")
    records = [
        generate_one(root, output, catalog, recipe, seconds, programs)
        for recipe in recipes
    ]
    report = {
        "format": 1,
        "kind": "fresh-positive-discovery",
        "archive_commit": catalog["archive_commit"],
        "source_manifest_sha256": digest(
            (root / "certificates/manifest.json").read_bytes()
        ),
        "status": (
            "COMPLETE"
            if all(x["status"] == "POSITIVE_CERTIFICATE_VERIFIED" for x in records)
            else "INCOMPLETE"
        ),
        "recipes": records,
        "scope": "Seven named positive growth models only. This is not full proof regeneration, clique optimality, or a negative search exclusion.",
    }
    (output / "regeneration.json").write_text(json.dumps(report, indent=2) + "\n")
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="action", required=True)
    recover_parser = sub.add_parser(
        "recover", help="Restore certificate bytes from the pinned Git archive"
    )
    recover_parser.add_argument(
        "--output", type=Path, default=ROOT / ".verification/recovered"
    )
    recover_parser.add_argument(
        "--programs",
        action="store_true",
        help="Also restore the hashed historical programs",
    )
    discover = sub.add_parser(
        "generate",
        help="Run fresh discovery, then independently check its positive witness",
    )
    discover.add_argument("--recipe", default="all")
    discover.add_argument(
        "--output", type=Path, default=ROOT / ".verification/regenerated"
    )
    discover.add_argument("--seconds", type=float, default=180)
    discover.add_argument(
        "--programs",
        type=Path,
        help="Use hash-checked recovered programs without Git/network",
    )
    args = parser.parse_args()
    try:
        if args.action == "recover":
            report = recover(ROOT, args.output, args.programs)
            print(json.dumps({"kind": report["kind"], "files": len(report["files"])}))
        else:
            report = generate(
                ROOT, args.output, args.recipe, args.seconds, args.programs
            )
            print(json.dumps(report, indent=2))
            if report["status"] != "COMPLETE":
                parser.exit(
                    1, "Discovery incomplete; no mathematical exclusion follows.\n"
                )
    except (ValueError, OSError) as error:
        parser.exit(1, str(error) + "\n")


if __name__ == "__main__":
    main()
