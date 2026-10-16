"""A fixed local experiment, not a search of all eight-point sets.

Compare Sidon/cubic protection with squarefree quartic protection and the
complementary intersection. All parameter coverage is specified by family().
No historical research kernel is imported. Standard library only.
"""
import argparse
import json
from collections import Counter, defaultdict
from itertools import combinations, combinations_with_replacement, product
from pathlib import Path
from time import monotonic

BASE = tuple((1 << i) - 1 for i in range(8))
WORDS = {k: list(combinations_with_replacement(range(8), k)) for k in (2, 3, 4, 8)}
SQUARE = {k: list(combinations(range(8), k)) for k in (3, 4)}


def family():
    # 3264 single-coordinate presentations and 9801 two-coordinate ones.
    for n in (*range(207, 248, 2), 251, 253, 255):
        for i in range(8):
            for d in range(-8, 9):
                a = list(BASE)
                a[i] += d
                yield "single", n, tuple(sorted(x % n for x in a)), [i, d]
    for n in (239, 247, 255):
        for i, j in ((5, 6), (5, 7), (6, 7)):
            for d, e in product(range(-16, 17), repeat=2):
                a = list(BASE)
                a[i] += d
                a[j] += e
                yield "pair", n, tuple(sorted(x % n for x in a)), [i, j, d, e]


def sums(a, n, k):
    f = defaultdict(list)
    for word in WORDS[k]:
        f[sum(a[i] for i in word) % n].append(word)
    return f


def describe(a, n):
    f2, f3, f4 = (sums(a, n, k) for k in (2, 3, 4))
    q3 = [sum(a[i] for i in w) % n for w in SQUARE[3]]
    q4 = [sum(a[i] for i in w) % n for w in SQUARE[4]]
    q = set(q4)
    cubic_protected = all(len(f3[x]) == 1 for x in q3)
    quartic_protected = all(len(f4[x]) == 1 for x in q4)
    target = sum(a) % n
    inter = set(f4) & {(target - x) % n for x in f4}
    delta = {(x - y) % n for x in a for y in a if x != y}
    h = len({x for x in delta if 2 * x % n not in delta}) // 2
    doubled = {2 * x % n for x in a}
    overlap = max(len(doubled & {(x + t) % n for x in a}) for t in range(n))
    return {"N": n, "A": list(a), "sumset2": len(f2), "sumset3": len(f3),
            "sumset4": len(f4), "squarefree3_distinct": len(set(q3)),
            "squarefree4_distinct": len(q), "cubic_protected": cubic_protected,
            "quartic_protected": quartic_protected,
            "quartics_protected_count": sum(len(f4[x]) == 1 for x in q4),
            "intersection_size": len(inter), "intersection_exact_Q": inter == q,
            "h": h, "maximum_dilation_overlap": overlap}


def enrich(row):
    n, a = row["N"], row["A"]
    f4 = sums(a, n, 4)
    row["periods4"] = [t for t in range(n) if {(x + t) % n for x in f4} == set(f4)]
    target = sum(a) % n
    rivals = [w for w in WORDS[8]
              if w != tuple(range(8)) and sum(a[i] for i in w) % n == target]
    row["valid8"] = not rivals
    row["eight_multisets_checked"] = len(WORDS[8])
    row["rival_count"] = len(rivals)
    row["rival"] = None if not rivals else [rivals[0].count(i) for i in range(8)]
    bad = []
    for w in SQUARE[4]:
        x = sum(a[i] for i in w) % n
        for v in f4[x]:
            if v != w:
                bad.append({"squarefree": list(w), "opponent": list(v), "residue": x})
    row["first_quartic_failure"] = bad[0] if bad else None
    assert row["valid8"] == (row["quartic_protected"] and row["intersection_exact_Q"])
    return row


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seconds", type=float, default=45)
    args = parser.parse_args()
    start = monotonic()
    counters = Counter()
    best = {}
    seen = set()
    completion = "COMPLETE_FIXED_FAMILY"
    for label, n, a, parameters in family():
        if monotonic() - start >= args.seconds:
            completion = "INCOMPLETE_FIXED_FAMILY"
            break
        counters["presentations"] += 1
        if len(set(a)) != 8:
            counters["not_distinct"] += 1
            continue
        key = n, a
        if key in seen:
            counters["duplicates"] += 1
            continue
        seen.add(key)
        # Fast prefilter; every discarded set violates a proved prerequisite.
        pair = {sum(a[i] for i in w) % n for w in WORDS[2]}
        if len(pair) != 36:
            counters["not_Sidon"] += 1
            continue
        row = describe(a, n)
        row["family"] = label
        row["parameters"] = parameters
        levels = {"Sidon": True,
                  "Sidon_cubic": row["cubic_protected"],
                  "Sidon_cubic_Q70": row["cubic_protected"] and row["squarefree4_distinct"] == 70,
                  "Sidon_cubic_Q70_overlap5": row["cubic_protected"] and row["squarefree4_distinct"] == 70 and row["maximum_dilation_overlap"] <= 5,
                  "quartic_protected": row["quartic_protected"],
                  "intersection_only": row["intersection_exact_Q"] and row["squarefree4_distinct"] == 70,
                  "valid_by_quartic_split": row["quartic_protected"] and row["intersection_exact_Q"]}
        for level, yes in levels.items():
            if yes:
                counters[level] += 1
                order = (row["sumset4"], row["N"], row["A"])
                if level not in best or order < (best[level]["sumset4"], best[level]["N"], best[level]["A"]):
                    best[level] = row.copy()
    best = {level: enrich(row) for level, row in best.items()}
    # Positive control, and a selected non-Sidon warning about the bare identity.
    controls = [enrich(describe(BASE, n)) for n in (251, 255)]
    out = {"completion": completion, "seconds_limit": args.seconds,
           "elapsed_seconds": monotonic() - start, "planned_presentations": 13065,
           "counters": dict(counters), "best": best, "controls": controls,
           "covers_all_sets": False, "new_modulus_exclusion": False,
           "universal_growth_proved": False}
    Path("stage38_growth_experiment_results.json").write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps({k: v for k, v in out.items() if k not in ("best", "controls")}, indent=2))
    print(json.dumps({level: {k: row[k] for k in ("N", "A", "sumset3", "sumset4", "quartics_protected_count", "intersection_exact_Q", "valid8")} for level, row in best.items()}, indent=2))


if __name__ == "__main__":
    main()
