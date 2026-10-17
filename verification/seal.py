"""Regenerate release integrity metadata after an intentional reviewed edit."""

from pathlib import Path
import hashlib
import json


def main():
    root = Path(__file__).resolve().parent.parent
    paths = [
        p
        for folder in (
            "certificates",
            "verification",
            "proof",
            "tests",
            "docs",
            ".github",
        )
        for p in (root / folder).rglob("*")
        if p.is_file()
        and "__pycache__" not in p.parts
        and p != root / "certificates/manifest.json"
    ]
    paths.extend(
        root / name
        for name in (
            "README.md",
            "PROOF.md",
            "verify.py",
            "privacy_check.py",
            ".gitignore",
            ".gitattributes",
        )
    )
    records = [
        {
            "path": p.relative_to(root).as_posix(),
            "bytes": p.stat().st_size,
            "sha256": hashlib.sha256(p.read_bytes()).hexdigest(),
        }
        for p in sorted(paths)
    ]
    value = {
        "format": 1,
        "scope": "Release integrity only; mathematical verification is separate.",
        "files": records,
    }
    (root / "certificates/manifest.json").write_text(
        json.dumps(value, indent=2) + "\n", encoding="utf-8", newline="\n"
    )
    print(f"Sealed {len(records)} release inputs. Run python verify.py next.")


if __name__ == "__main__":
    main()
