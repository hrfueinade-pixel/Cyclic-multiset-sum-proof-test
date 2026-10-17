"""Run exactly one required quotient order and preserve incomplete evidence."""

from __future__ import annotations

import argparse
import importlib.util
from pathlib import Path
import sys
from time import monotonic

from verification.core import CASES, ROOT, parity_fingerprint, write_json


def run_order(case: str, order: int, seconds: float, output: Path) -> int:
    if not __debug__:
        raise RuntimeError(
            "Proof verification requires assertions; remove -O/PYTHONOPTIMIZE."
        )
    if case not in CASES or order not in CASES[case][1]:
        raise ValueError("Order is outside the stated verification domain")
    path = ROOT / "verification/checks" / CASES[case][0]
    spec = importlib.util.spec_from_file_location("exact_order", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.start = monotonic()
    module.cap = seconds
    record = {"case": case, "order": order, "fingerprint": parity_fingerprint(case)}
    try:
        report = module.run(order)
        if report.get("M") != order or report.get("completion") != "COMPLETE":
            raise ValueError("Enumerator did not establish the requested order")
        record.update(
            completion="COMPLETE",
            report=report,
            survivors=module.survivors,
            shapes=getattr(module, "shape_records", []),
        )
        status = 0
    except TimeoutError:
        record.update(
            completion="INCOMPLETE",
            report=None,
            partial_order=getattr(module, "active", None),
            survivors=module.survivors,
        )
        status = 2
    record["elapsed_seconds"] = monotonic() - module.start
    write_json(output, record)
    print(f"{case} M={order}: {record['completion']}", flush=True)
    return status


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("case", choices=CASES)
    parser.add_argument("order", type=int)
    parser.add_argument("--seconds", type=float, required=True)
    parser.add_argument("--output", type=Path, required=True)
    options = parser.parse_args()
    return run_order(options.case, options.order, options.seconds, options.output)


if __name__ == "__main__":
    sys.exit(main())
