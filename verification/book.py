"""Typeset the maintained Markdown proof; Pandoc and XeLaTeX are build tools only."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
from urllib.parse import quote, unquote

ROOT = Path(__file__).resolve().parent.parent
SOURCES = (
    "PROOF.md",
    "proof/parity.md",
    "proof/multiplicity.md",
    "proof/counting.md",
    "proof/assignment.md",
    "proof/alignment.md",
    "proof/closing.md",
    "docs/certificates.md",
    "docs/references.md",
)
LEMMA_FILES = {
    1: "PROOF.md",
    2: "PROOF.md",
    3: "proof/parity.md",
    4: "proof/parity.md",
    5: "proof/multiplicity.md",
    6: "proof/counting.md",
    7: "proof/assignment.md",
    8: "proof/assignment.md",
    **{n: "proof/alignment.md" for n in range(9, 17)},
}
REPOSITORY = "https://github.com/hrfueinade-pixel/Cyclic-multiset-sum-proof-test"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def git(root, *args):
    return subprocess.check_output(["git", "-C", str(root), *args], text=True).strip()


def slug(text):
    return re.sub(r"[^\w\- ]", "", text.lower()).replace(" ", "-")


def manuscript(root, commit, manifest):
    """Give headings unique PDF targets and resolve source links before typesetting."""
    documents = {name: (root / name).read_text() for name in SOURCES}
    anchors, chapter_roots, canonical = {}, {}, {}
    for name, text in documents.items():
        fenced = False
        for line in text.splitlines():
            if line.startswith("```"):
                fenced = not fenced
            heading = re.match(r"^(#{1,6}) (.+)$", line)
            if fenced or not heading:
                continue
            label = heading[2]
            anchor = name.replace("/", "-").replace(".md", "") + "-" + slug(label)
            lemma = re.match(r"Lemma (\d+)\.", label)
            if lemma and LEMMA_FILES.get(int(lemma[1])) == name:
                number = int(lemma[1])
                if number in canonical:
                    raise ValueError(f"Duplicate lemma {number}")
                anchor = canonical[number] = f"lemma-{number}"
            anchors[name, slug(label)] = anchor
            chapter_roots.setdefault(name, anchor)
    if set(canonical) != set(LEMMA_FILES):
        raise ValueError("The PDF needs a unique target for every numbered lemma")

    def link(source, match):
        label, target = match[1], match[2]
        code_hash = re.fullmatch(r"`([0-9a-f]{40,64})`", label)
        if code_hash:
            label = "`" + code_hash[1][:12] + "`"
        if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", target):
            return f"[{label}]({target})"
        file, _, fragment = target.partition("#")
        destination = (root / source).parent / unquote(file) if file else root / source
        relative = destination.resolve().relative_to(root.resolve()).as_posix()
        if relative in documents:
            key = (
                anchors.get((relative, fragment))
                if fragment
                else chapter_roots[relative]
            )
            if key is None:
                raise ValueError(f"Unresolved PDF heading: {source}: {target}")
            return f"[{label}](#{key})"
        if not destination.exists():
            raise ValueError(f"Missing source link: {source}: {target}")
        return (
            f"[{label}]({REPOSITORY}/blob/{commit}/{quote(relative)}"
            + (f"#{fragment}" if fragment else "")
            + ")"
        )

    # Exclude existing links, code and math from automatic prose references.
    protected = re.compile(r"(\$\$.*?\$\$|\$[^$]*\$|\[[^\]]*\]\([^)]*\)|`[^`]*`)", re.S)
    reference = re.compile(r"\bLemmas?\s+(\d+)(?:\s*[–-]\s*(\d+))?")

    def lemma_links(text):
        pieces = protected.split(text)
        for i in range(0, len(pieces), 2):
            pieces[i] = reference.sub(
                lambda m: (
                    f"[{m[0]}](#lemma-{int(m[1])})" if int(m[1]) in canonical else m[0]
                ),
                pieces[i],
            )
        return "".join(pieces)

    output = [
        "This is an AI-assisted, computer-assisted proof proposal for mathematical review. "
        "It has not received independent external human review or proof-assistant certification.\n",
        f"Source: [{commit}]({REPOSITORY}/tree/{commit}).\n",
        f"Source manifest: `{manifest}`.\n",
    ]
    for name, original in documents.items():
        text = re.sub(
            r"(?<!!)\[([^\]]*)\]\(([^)]+)\)",
            lambda m: link(name, m),
            original,
            flags=re.S,
        )
        lines, prose, fenced, math = [], [], False, False

        def flush():
            if prose:
                lines.append(lemma_links("\n".join(prose)))
                prose.clear()

        for line in text.splitlines():
            if line.startswith("```"):
                flush()
                fenced = not fenced
                lines.append(line)
                continue
            heading = re.match(r"^(#{1,6}) (.+)$", line)
            if heading and not fenced and not math:
                flush()
                title = (
                    "Main argument"
                    if name == "PROOF.md" and heading[1] == "#"
                    else heading[2]
                )
                lines.append(
                    f"{heading[1]} {title} {{#{anchors[name, slug(heading[2])]}}}"
                )
            elif fenced or line.startswith("$$") or math:
                flush()
                lines.append(line)
            else:
                prose.append(line)
            if line.startswith("$$"):
                math = not math
        flush()
        output.append("\n".join(lines))
    return "\n\n".join(output) + "\n"


def build(output, root=ROOT, allow_dirty=False):
    output = Path(output).resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    dirty = bool(git(root, "status", "--porcelain"))
    if dirty and not allow_dirty:
        raise ValueError("Use a clean commit, or --allow-dirty for a local preview")
    for tool in ("pandoc", "xelatex", "pdftotext", "pdfinfo"):
        if not shutil.which(tool):
            raise ValueError(f"Missing PDF build tool: {tool}")
    commit = git(root, "rev-parse", "HEAD")
    manifest = sha(root / "certificates/manifest.json")
    build_dir = output.parent / "pdf-build"
    build_dir.mkdir(exist_ok=True)
    markdown = build_dir / "proof.md"
    markdown.write_text(manuscript(root, commit, manifest))
    shutil.copyfile(root / "docs/pdf/preamble.tex", build_dir / "preamble.tex")
    shutil.copyfile(root / "docs/pdf/layout.lua", build_dir / "layout.lua")
    env = os.environ.copy()
    env["SOURCE_DATE_EPOCH"] = git(root, "show", "-s", "--format=%ct", "HEAD")
    env["FORCE_SOURCE_DATE"] = "1"
    env["XDG_CACHE_HOME"] = str(build_dir / "cache")
    command = [
        "pandoc",
        "--from=markdown+tex_math_dollars+header_attributes-raw_tex",
        "--standalone",
        "--table-of-contents",
        "--toc-depth=2",
        "--top-level-division=chapter",
        "--variable=documentclass:report",
        "--variable=classoption:oneside",
        "--variable=fontsize:11pt",
        "--variable=geometry:margin=25mm",
        "--variable=papersize:a4",
        "--variable=colorlinks:true",
        "--metadata=title:Cyclic multiset sums: the eight-point minimum",
        "--metadata=subtitle:Computer-assisted proof proposal — review edition",
        "--metadata=date:",
        "--include-in-header=preamble.tex",
        "--lua-filter=layout.lua",
        "proof.md",
        "--output=proof.tex",
    ]
    log_path = output.with_suffix(".build.log")
    with log_path.open("w") as log:
        subprocess.run(
            command,
            cwd=build_dir,
            check=True,
            stdout=log,
            stderr=subprocess.STDOUT,
            env=env,
        )
        for _ in range(3):
            subprocess.run(
                [
                    "xelatex",
                    "-no-shell-escape",
                    "-halt-on-error",
                    "-interaction=nonstopmode",
                    "-output-directory=.",
                    "proof.tex",
                ],
                cwd=build_dir,
                check=True,
                stdout=log,
                stderr=subprocess.STDOUT,
                env=env,
            )
    latex_log = (build_dir / "proof.log").read_text(errors="replace")
    overshoots = [
        float(x)
        for x in re.findall(r"Overfull \\hbox \(([\d.]+)pt too wide\)", latex_log)
    ]
    if (
        "Missing character:" in latex_log
        or "There were undefined references" in latex_log
        or max(overshoots, default=0) > 5
    ):
        raise ValueError("PDF layout needs correction; inspect " + str(log_path))
    shutil.copyfile(build_dir / "proof.pdf", output)
    text = subprocess.check_output(["pdftotext", str(output), "-"], text=True)
    if "495" not in text or "248" not in text or "Contents" not in text:
        raise ValueError("PDF is missing expected proof or navigation content")
    report = {
        "format": 1,
        "kind": "typeset-proof",
        "source_commit": commit,
        "dirty_preview": dirty,
        "source_manifest_sha256": manifest,
        "sources": [{"path": name, "sha256": sha(root / name)} for name in SOURCES],
        "pdf_sha256": sha(output),
        "pdf_bytes": output.stat().st_size,
        "pandoc": subprocess.check_output(
            ["pandoc", "--version"], text=True
        ).splitlines()[0],
        "xelatex": subprocess.check_output(
            ["xelatex", "--version"], text=True
        ).splitlines()[0],
        "overfull_hboxes_pt": overshoots,
        "pdfinfo": subprocess.check_output(["pdfinfo", str(output)], text=True),
        "scope": "Typesetting and navigation; not mathematical or proof-assistant certification.",
    }
    output.with_suffix(".json").write_text(json.dumps(report, indent=2) + "\n")
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output", type=Path, default=ROOT / ".verification/publication/proof.pdf"
    )
    parser.add_argument("--allow-dirty", action="store_true")
    args = parser.parse_args()
    try:
        print(json.dumps(build(args.output, allow_dirty=args.allow_dirty), indent=2))
    except (ValueError, subprocess.CalledProcessError) as error:
        parser.exit(1, str(error) + "\n")


if __name__ == "__main__":
    main()
