"""Full verification entry point; limited phases never certify the whole package."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
from time import monotonic

from verification.core import (
    CASES,
    ROOT,
    VerificationError,
    check_integrity,
    digest,
    parity_fingerprint,
    read_json,
    require,
    require_orders,
    stage_work,
    write_json,
)

SYMBOLIC = (
    (
        "multiplicity models",
        "multiplicity_models.py",
        "multiplicity-models-report.json",
    ),
    ("cubic exception", "cubic_exception.py", "cubic-exception-report.json"),
    ("quintic cap", "quintic_cap.py", "quintic-cap-report.json"),
    ("base assignment coverage", "assignment_base.py", "assignment-base-report.json"),
    ("split sources", "split_sources.py", "split-sources-report.json"),
    ("general split assignment", "split_assignment.py", "split-assignment-report.json"),
    ("triangle ownership", "triangle_ownership.py", "triangle-ownership-report.json"),
    ("triangle splits", "triangle_splits.py", "triangle-splits-report.json"),
    ("alignment forests", "alignment_forests.py", "alignment-forests-report.json"),
    (
        "triangle interactions",
        "triangle_interactions.py",
        "triangle-interactions-report.json",
    ),
    ("two-triangle exclusion", "two_triangle_exclusion.py", "two-triangle-report.json"),
)


def invoke(
    command: list[str], cwd: Path, name: str, timeout: float | None = None
) -> None:
    env = os.environ.copy()
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    env.pop("PYTHONOPTIMIZE", None)
    log = ROOT / ".verification/logs" / (name.replace(" ", "-") + ".log")
    log.parent.mkdir(parents=True, exist_ok=True)
    try:
        result = subprocess.run(
            command, cwd=cwd, env=env, capture_output=True, text=True, timeout=timeout
        )
    except subprocess.TimeoutExpired as error:

        def decoded(value):
            return (
                value.decode("utf-8", errors="replace")
                if isinstance(value, bytes)
                else value or ""
            )

        log.write_text(
            decoded(error.stdout)
            + decoded(error.stderr)
            + "\nPROCESS_TIMEOUT: verification is incomplete\n",
            encoding="utf-8",
        )
        raise VerificationError(
            name + " exceeded its process limit; verification is incomplete"
        ) from error
    log.write_text(result.stdout + result.stderr, encoding="utf-8")
    require(
        result.returncode == 0,
        name + " failed or was incomplete; inspect .verification/logs",
    )


def symbolic(work: Path) -> dict:
    outcomes = {}
    for name, script, report in SYMBOLIC:
        print("Checking " + name + "...", flush=True)
        invoke([sys.executable, "-B", script], work, name)
        require((work / report).is_file(), "Missing checker report: " + report)
        outcomes[name] = read_json(work / report)
    forests = outcomes["alignment forests"]
    require(
        set(forests["excluded_shapes"]) == {"53", "71", "332", "521", "431", "611"},
        "Large-forest root coverage is incomplete",
    )
    require(
        forests["proof_nodes"] == 2666
        and forests["positive_mass8_pair_identities"] == 1723040,
        "Unexpected forest certificate coverage",
    )
    interactions = outcomes["triangle interactions"]
    require(
        interactions["second_triangle_presentations"] == 3360
        and interactions["positive_mass8_pair_identities"] == 1570316,
        "Unexpected triangle interaction coverage",
    )
    two = outcomes["two-triangle exclusion"]
    require(
        two["checked_shapes"] == ["3221"]
        and two["nodes"] == [13333]
        and two["positive_mass8_identities"] == 7945564,
        "Two-triangle component coverage is incomplete",
    )
    return outcomes


def parity(work: Path, seconds: float, resume: bool) -> dict:
    all_records = {}
    reused = 0
    for case, (_, orders) in CASES.items():
        fingerprint = parity_fingerprint(case)
        records = []
        for index, order in enumerate(orders, 1):
            output = (
                ROOT / ".verification/parity" / fingerprint / case / f"{order}.json"
            )
            cached = read_json(output) if resume and output.is_file() else None
            if not (
                cached
                and cached.get("case") == case
                and cached.get("order") == order
                and cached.get("fingerprint") == fingerprint
                and cached.get("completion") == "COMPLETE"
            ):
                print(
                    f"Checking {case}: quotient {order} ({index}/{len(orders)})...",
                    flush=True,
                )
                invoke(
                    [
                        sys.executable,
                        "-B",
                        "-m",
                        "verification.worker",
                        case,
                        str(order),
                        "--seconds",
                        str(seconds),
                        "--output",
                        str(output),
                    ],
                    ROOT,
                    f"{case}-{order}",
                    timeout=seconds + 20,
                )
                cached = read_json(output)
            else:
                reused += 1
            records.append(cached)
        require_orders(records, case, fingerprint)
        all_records[case] = records
    # Reference counts are additional consistency controls, not substitutes
    # for the fresh exhaustive per-order enumeration above.
    reference = read_json(work / "three-five-reference.json")
    expected = {r["M"]: r["counts"] for r in reference["reports"]}
    require(
        set(expected) == set(CASES["three-five"][1]),
        "Missing three-five reference order",
    )
    for record in all_records["three-five"]:
        counts = record["report"]["counts"]
        other = expected[record["order"]]
        require(
            all(
                counts[a] == other[b]
                for a, b in [
                    ("blocks", "blocks"),
                    ("proper_saturated", "proper_saturated"),
                    ("shapes", "shapes_5odd_surviving"),
                    ("even_triples", "even_triples"),
                ]
            ),
            "Three-five consistency control failed",
        )
    reference = read_json(work / "four-four-reference.json")
    expected = {r["M"]: r["counts"] for r in reference["reports"]}
    require(
        set(expected) == set(CASES["four-four"][1]), "Missing four-four reference order"
    )
    for record in all_records["four-four"]:
        require(
            all(
                record["report"]["counts"][k] == expected[record["order"]][k]
                for k in ("B_blocks", "proper_saturated", "C_shapes")
            ),
            "Four-four consistency control failed",
        )
    shape_count = sum(len(r["shapes"]) for r in all_records["four-four"])
    require(shape_count == 51168, "Incorrect balanced-parity symbolic shape coverage")
    survivors = [s for r in all_records["seven-point"] for s in r["survivors"]]
    canonical = lambda rows, key: {(r["M"], tuple(r["B"])): tuple(r[key]) for r in rows}
    source = read_json(work / "seven-point-survivors.json")
    require(
        canonical(survivors, "missing") == canonical(source["survivors"], "missing_7B")
        and len(survivors) == 58,
        "Seven-point survivor coverage differs",
    )
    # The extension checker receives the completed enumeration from this run,
    # rather than treating a historical saved success as its proof input.
    write_json(
        work / "seven-point-reference.json",
        {
            "completion": "COMPLETE",
            "completed_orders": list(CASES["seven-point"][1]),
            "survivors": survivors,
            "reports": [r["report"] for r in all_records["seven-point"]],
        },
    )
    invoke(
        [sys.executable, "-B", "seven_point_extensions.py"],
        work,
        "seven-point extensions",
    )
    extensions = read_json(work / "seven-point-extensions-report.json")
    require(
        extensions["six_sets"] == 58 and extensions["valid_seven_survivors"] == 0,
        "An unexcluded seven-point extension remains",
    )
    invoke([sys.executable, "-B", "antipodal_lifts.py"], work, "antipodal lifts")
    lifts = read_json(work / "antipodal-lifts-report.json")
    require(
        lifts["six_lifts_checked"] == 480 and lifts["seven_lifts_checked"] == 192,
        "Incomplete antipodal lift domain",
    )
    return {
        "required_order_checks": sum(len(x) for _, x in CASES.values()),
        "completed_order_checks": sum(len(x) for x in all_records.values()),
        "reused_completed_orders": reused,
        "balanced_shapes": shape_count,
        "six_point_survivors": 58,
        "unexcluded_seven_point_extensions": 0,
        "six_lifts": 480,
        "seven_lifts": 192,
    }


def main(argv: list[str] | None = None) -> int:
    if not __debug__:
        print(
            "Verification requires assertions. Remove -O or PYTHONOPTIMIZE.",
            file=sys.stderr,
        )
        return 2
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--only",
        choices=("symbolic", "parity", "elementary"),
        help="Run a limited phase; its success does not certify the full package.",
    )
    parser.add_argument(
        "--resume",
        action="store_true",
        help="Reuse completed per-order runs of the same enumeration code, explicitly reported.",
    )
    parser.add_argument(
        "--seconds-per-order",
        type=float,
        default=120,
        help="Deadline for each finite parity order; incomplete runs fail (default: 120).",
    )
    options = parser.parse_args(argv)
    start = monotonic()
    summary = {"scope": options.only or "full", "status": "INCOMPLETE"}
    try:
        initial_manifest = digest(ROOT / "certificates/manifest.json")
        summary["manifest_sha256"] = initial_manifest
        summary["integrity"] = check_integrity()
        from verification.core import check_dependencies

        summary["dependencies"] = check_dependencies()
        work = stage_work()
        if options.only in (None, "symbolic"):
            summary["symbolic"] = symbolic(work)
        if options.only in (None, "parity"):
            summary["parity"] = parity(work, options.seconds_per_order, options.resume)
        if options.only in (None, "elementary"):
            print("Checking elementary identities and sharpness...", flush=True)
            invoke(
                [sys.executable, "-B", "elementary_identities.py"],
                work,
                "elementary identities",
            )
            invoke([sys.executable, "-B", "finishing.py"], work, "finishing")
            summary["elementary"] = read_json(
                work / "elementary-identities-report.json"
            )
            summary["finishing"] = read_json(work / "finishing-report.json")
        if options.only is None:
            print("Checking independent coverage controls...", flush=True)
            invoke(
                [sys.executable, "-B", "-m", "verification.independent"],
                ROOT,
                "independent coverage",
            )
            summary["independent"] = read_json(
                ROOT / ".verification/independent-report.json"
            )
            print("Checking failure controls and release privacy...", flush=True)
            invoke(
                [
                    sys.executable,
                    "-B",
                    "-m",
                    "unittest",
                    "discover",
                    "-s",
                    "tests",
                    "-v",
                ],
                ROOT,
                "failure controls",
            )
            invoke([sys.executable, "-B", "privacy_check.py"], ROOT, "release privacy")
            summary["privacy"] = "PASSED"
            summary["failure_controls"] = "PASSED"
            require(
                digest(ROOT / "certificates/manifest.json") == initial_manifest,
                "Release manifest changed during verification",
            )
            summary["integrity"] = check_integrity()
            summary["status"] = "FULL_CHECKS_PASSED"
        else:
            summary["status"] = "LIMITED_PHASE_PASSED"
        summary["elapsed_seconds"] = monotonic() - start
        write_json(ROOT / ".verification/summary.json", summary)
        print(
            json.dumps(
                {k: v for k, v in summary.items() if k not in ("symbolic",)}, indent=2
            )
        )
        print(
            "Full computational verification passed; the written reductions remain mathematical review obligations."
            if options.only is None
            else "Limited phase passed. Full verification has not been established by this command."
        )
        return 0
    except (VerificationError, OSError, ValueError, KeyError) as error:
        summary["error"] = str(error)
        summary["elapsed_seconds"] = monotonic() - start
        write_json(ROOT / ".verification/summary.json", summary)
        print("INCOMPLETE: " + str(error), file=sys.stderr)
        return 2
