"""Targeted 6+2 coset family; no arbitrary-eight-set exclusion is claimed.

Enumerate Sidon six-subsets containing 0,1 in Z/j for j=33,35,45,49.
Use each missing signed difference d to place two points in a second coset
of Z/(q*j). Stop only at a stated global cap; preserve the partial counters.
This tests the gap between Sidon/aperiodicity and protected cubic/quartic sums.
"""
import argparse
import json
from collections import Counter
from pathlib import Path
from time import monotonic

from stage38_growth_experiment import describe, enrich


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seconds", type=float, default=30)
    args = parser.parse_args()
    start = monotonic()
    counter = Counter()
    best = {}
    partial = None
    completion = "COMPLETE_FIXED_COSET_FAMILY"

    def tick(j, b):
        nonlocal partial
        if monotonic() - start >= args.seconds:
            partial = {"kernel_order": j, "prefix": list(b)}
            raise TimeoutError

    def sixes(j, b=(0, 1), pairs=frozenset((0, 1, 2))):
        tick(j, b)
        counter["prefixes"] += 1
        if len(b) == 6:
            yield b
            return
        for x in range(b[-1] + 1, j):
            added = {(x + y) % j for y in b} | {2 * x % j}
            if len(added) != len(b) + 1 or pairs & added:
                continue
            yield from sixes(j, b + (x,), pairs | added)

    try:
        for j, q in ((33, 7), (35, 7), (45, 5), (49, 5)):
            for b in sixes(j):
                counter[f"six_sets_{j}"] += 1
                delta = {(x - y) % j for x in b for y in b if x != y}
                for d in range(1, (j + 1) // 2):
                    if d in delta:
                        continue
                    a = tuple(sorted([q * x for x in b] + [1, 1 + q * d]))
                    row = describe(a, j * q)
                    assert row["sumset2"] == 36
                    row["kernel_six"] = list(b)
                    row["kernel_order"] = j
                    row["quotient_order"] = q
                    row["missing_step"] = d
                    counter["eight_candidates"] += 1
                    levels = {"Sidon_overlap5": row["maximum_dilation_overlap"] <= 5,
                              "Sidon_Q70": row["squarefree4_distinct"] == 70,
                              "Sidon_cubic": row["cubic_protected"],
                              "quartic_protected": row["quartic_protected"]}
                    for level, yes in levels.items():
                        if not yes:
                            continue
                        counter[level] += 1
                        order = (row["sumset4"], row["N"], row["A"])
                        if level not in best or order < (best[level]["sumset4"], best[level]["N"], best[level]["A"]):
                            best[level] = row.copy()
    except TimeoutError:
        completion = "INCOMPLETE_FIXED_COSET_FAMILY"
    best = {key: enrich(row) for key, row in best.items()}
    # Keep this positive witness reproducible even if a faster host explores
    # more of the partial family and obtains a different best diagnostic.
    controls = [enrich(describe((0, 1, 7, 21, 49, 84, 99, 140), 245))]
    out = {"completion": completion, "seconds_limit": args.seconds,
           "elapsed_seconds": monotonic() - start, "counters": dict(counter),
           "partial_state": partial, "best": best, "controls": controls, "covers_all_sets": False,
           "new_modulus_exclusion": False, "universal_growth_proved": False}
    Path("stage38_coset_experiment_results.json").write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps({k: v for k, v in out.items() if k != "best"}, indent=2))
    print(json.dumps({key: {k: row[k] for k in ("N", "A", "sumset3", "sumset4", "squarefree4_distinct", "cubic_protected", "maximum_dilation_overlap", "periods4", "valid8")} for key, row in best.items()}, indent=2))


if __name__ == "__main__":
    main()
