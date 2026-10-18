"""Release integrity, isolated checker staging, and exact coverage gates."""

from __future__ import annotations

import ast
import hashlib
import json
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent.parent
CASES = {
    "two-six": ("parity_two_six.py", tuple(range(94, 124))),
    "three-five": ("parity_three_five.py", tuple(range(94, 124))),
    "four-four": ("parity_four_four.py", tuple(range(94, 124))),
    "seven-point": ("seven_point_survivors.py", tuple(range(64, 124))),
}


class VerificationError(RuntimeError):
    """A required claim is invalid, incomplete, or unsupported by its evidence."""


def check_dependencies(root: Path = ROOT) -> dict:
    """Reject missing claims, circular premises, and unaccounted proof inputs."""
    ledger = read_json(root / "certificates/dependencies.json")
    claims = ledger["claims"]
    indexed = {row["id"]: row for row in claims}
    require(len(indexed) == len(claims), "Duplicate mathematical claim")
    visited, active = set(), set()

    def visit(key):
        require(key in indexed, "Missing mathematical premise: " + key)
        require(key not in active, "Circular mathematical premises: " + key)
        if key in visited:
            return
        active.add(key)
        for premise in indexed[key]["depends_on"]:
            visit(premise)
        active.remove(key)
        visited.add(key)

    visit(ledger["theorem"])
    require(visited == set(indexed), "Unconnected claims in the proof ledger")
    checks, inputs = set(), set()
    for row in claims:
        require(row["kind"] in ("hand", "finite"), "Unknown claim kind")
        require((root / row["exposition"]).is_file(), "Missing claim exposition")
        if row["kind"] == "finite":
            require(bool(row["checks"]), "Finite claim without a checker")
        checks.update(row["checks"])
        inputs.update(row["inputs"])
    actual_checks = {p.name for p in (root / "verification/checks").glob("*.py")}
    require(checks == actual_checks, "Unaccounted or missing proof checker")
    actual_inputs = {
        p.relative_to(root).as_posix()
        for p in (root / "certificates").rglob("*")
        if p.is_file() and p.name not in ("manifest.json", "dependencies.json")
    }
    require(inputs == actual_inputs, "Unaccounted or missing certificate input")
    return {
        "claims": len(claims),
        "checkers": len(checks),
        "certificate_inputs": len(inputs),
        "scope": "Acyclic dependency and file coverage; hand reductions require mathematical review.",
    }


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationError(message)


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def check_integrity(root: Path = ROOT) -> dict:
    manifest = read_json(root / "certificates/manifest.json")
    recorded = manifest["files"]
    require(
        len({item["path"] for item in recorded}) == len(recorded),
        "Duplicate manifest path",
    )
    for item in recorded:
        path = root / item["path"]
        require(path.is_file(), "Missing release input: " + item["path"])
        require(
            path.stat().st_size == item["bytes"] and digest(path) == item["sha256"],
            "Changed release input: " + item["path"],
        )
    expected = {item["path"] for item in recorded}
    actual = {
        p.relative_to(root).as_posix()
        for folder in ("certificates", "verification", "proof", "tests", "docs")
        for p in (root / folder).rglob("*")
        if p.is_file()
        and "__pycache__" not in p.parts
        and p != root / "certificates/manifest.json"
    }
    actual.update(
        name
        for name in (
            "README.md",
            "PROOF.md",
            "verify.py",
            "privacy_check.py",
            ".gitignore",
            ".gitattributes",
        )
        if (root / name).is_file()
    )
    if (root / ".github").exists():
        actual.update(
            p.relative_to(root).as_posix()
            for p in (root / ".github").rglob("*")
            if p.is_file()
        )
    require(actual == expected, "Release file set differs from manifest")
    return {
        "files": len(recorded),
        "scope": "Package integrity only; mathematical checks are separate.",
    }


def parity_fingerprint(case: str, root: Path = ROOT) -> str:
    module = root / "verification/checks" / CASES[case][0]
    hasher = hashlib.sha256()
    # Formatting and prose do not invalidate a completed enumeration; changes
    # to the algorithm or worker do. Coverage is checked afresh by the parent.
    for path in (
        module,
        root / "verification/worker.py",
        root / "verification/parity.py",
        root / "verification/core.py",
    ):
        tree = ast.parse(path.read_text(encoding="utf-8"))
        hasher.update(ast.dump(tree, include_attributes=False).encode())
    return hasher.hexdigest()


def require_orders(records: list[dict], case: str, fingerprint: str) -> None:
    expected = set(CASES[case][1])
    require(len(records) == len(expected), "Missing or duplicate " + case + " orders")
    require(
        {r.get("order") for r in records} == expected,
        "Incorrect " + case + " order coverage",
    )
    for record in records:
        require(
            record.get("case") == case and record.get("fingerprint") == fingerprint,
            "Wrong algorithm or case in order record",
        )
        require(
            record.get("completion") == "COMPLETE",
            "Incomplete " + case + " enumeration",
        )
        report = record.get("report") or {}
        require(
            report.get("M") == record["order"]
            and report.get("completion") == "COMPLETE",
            "Order record does not establish completion",
        )
        if case != "seven-point":
            require(
                not record.get("survivors"), "An unexcluded parity survivor remains"
            )


def stage_work(root: Path = ROOT) -> Path:
    work = root / ".verification/work"
    work.mkdir(parents=True, exist_ok=True)
    inputs = list((root / "certificates").rglob("*.json")) + list(
        (root / "certificates").rglob("*.json.gz")
    )
    inputs = [p for p in inputs if p.name not in ("manifest.json", "dependencies.json")]
    inputs += list((root / "verification/checks").glob("*.py"))
    require(
        len({p.name for p in inputs}) == len(inputs),
        "Staged input basenames must be unique",
    )
    expected = {p.name for p in inputs}
    # Only flat files in this dedicated generated workspace are replaced.
    for old in work.iterdir():
        if old.is_file():
            old.unlink()
    for source in inputs:
        shutil.copyfile(source, work / source.name)
    return work
