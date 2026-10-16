"""One targeted rank-three singleton-cone presentation, not a modulus sweep.

Reuses the Stage13 max-functional closure generator and prime-power kernels.
No Stage13 I/II enumeration or historical search runs on import.
The cooperative deadline is not preemptive inside one factor/kernel call.
"""

import argparse
import json
from pathlib import Path
from time import monotonic

import stage13_pure_cone_closure as closure


POINTS = ((0, 0, 0), (1, 0, 0), (-2, 0, 0), (0, 1, 0),
          (0, -2, 0), (0, 0, 1), (-2, 0, 2), (0, 0, -4))


def run(cap):
    start = monotonic()
    closure.POINTS["III"] = POINTS
    record = closure.check_family("III", start, start + cap)
    complete = record["completion_status"] == "complete"
    return {
        "scope": "Only singleton-cone III; full-rank closure matrices and their derived odd divisor orders 188..2187",
        "runtime_cap_seconds": cap,
        "elapsed_seconds": monotonic() - start,
        "completion_status": "complete" if complete else "INCOMPLETE",
        "complete_singleton_presentation_exclusion": complete and not record["valid_survivors"],
        "family": record,
        "dependencies": [
            "Stage12 fresh singleton core-five/ordinary-three residual and R3>=2",
            "Stage13 elementary reduction to singleton presentation III",
            "Elementary cubic packing H>=188 and tree determinant H<=2187",
            "Stage13 max-functional closure generator and Stage10 prime-power kernel implementation"],
        "limitations": [
            "Any timeout is an incomplete prefix, not a shape exclusion.",
            "Deadline is cooperative; individual factor/kernel calls are not preempted; serialization is outside it.",
            "Fresh quartic fibers coning no cubic triple are not covered.",
            "No novelty claim or elementary replacement for the finite calculation is asserted."]}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--cap", type=float, default=30)
    parser.add_argument("--output", default="stage14_singleton_cone_results.json")
    args = parser.parse_args()
    result = run(args.cap)
    Path(args.output).write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
