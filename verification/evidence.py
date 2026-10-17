"""Export complete verification evidence, bound to the verified source manifest.

Evidence is outside the source manifest to avoid hashing itself. Exporting
an incomplete run preserves that status and never changes it to a success.
"""

import argparse
import gzip
import hashlib
import json
from pathlib import Path
import platform


def export(source, console, exit_code, destination):
    run = source / ".verification"
    manifest = source / "certificates/manifest.json"
    summary = json.loads((run / "summary.json").read_text())
    fingerprint = hashlib.sha256(manifest.read_bytes()).hexdigest()
    if "manifest_sha256" in summary:
        assert (
            summary["manifest_sha256"] == fingerprint
        ), "Sources changed after this run"
    artifacts = {}
    paths = sorted((run / "logs").glob("*.log"))
    paths += sorted((run / "parity").rglob("*.json"))
    paths += sorted((run / "work").glob("*-report.json"))
    if (run / "independent-report.json").exists():
        paths.append(run / "independent-report.json")
    for path in paths:
        artifacts[path.relative_to(run).as_posix()] = path.read_text()
    record = {
        "format": 1,
        "command": ["python", "verify.py", "--seconds-per-order", "300"],
        "python": platform.python_version(),
        "exit_code": exit_code,
        "manifest_sha256": fingerprint,
        "summary": summary,
        "console": console.read_text(),
        "artifacts": artifacts,
        "scope": "Complete captured logs, reports and per-order records; source certificate inputs are in the repository.",
    }
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(
        gzip.compress(json.dumps(record, separators=(",", ":")).encode(), mtime=0)
    )
    print(
        json.dumps(
            {
                "evidence": str(destination),
                "bytes": destination.stat().st_size,
                "manifest_sha256": fingerprint,
                "status": summary["status"],
                "exit_code": exit_code,
            },
            indent=2,
        )
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source", type=Path, default=Path(__file__).resolve().parent.parent
    )
    parser.add_argument("--console", type=Path, required=True)
    parser.add_argument("--exit-code", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    options = parser.parse_args()
    export(options.source, options.console, options.exit_code, options.output)


if __name__ == "__main__":
    main()
