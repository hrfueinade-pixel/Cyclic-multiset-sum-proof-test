"""Exact bounded checks of two symbolic high-cubic-multiplicity families."""

from collections import Counter, defaultdict
from itertools import combinations, combinations_with_replacement
import json
from pathlib import Path

from research_experiments import collision


def statistics(a, n, inspected_quartic=0):
    triples = defaultdict(list)
    quartics = defaultdict(list)
    ordinary = defaultdict(list)
    pairs = list(combinations_with_replacement(a, 2))
    for c in a:
        for d in a:
            triples[(2 * c + d) % n].append((c, d))
        for d, e in pairs:
            quartics[(2 * c + d + e) % n].append((c, d, e))
        for d, e in combinations([v for v in a if v != c], 2):
            ordinary[(2 * c + d + e) % n].append((c, d, e))
    bases = []
    for base in a:
        b = [v for v in a if v != base]
        low = {sum((v - base) % n for v in chosen) % n
               for r in range(3) for chosen in combinations(b, r)}
        value = (inspected_quartic - 4 * base) % n
        bases.append({"base": base, "inspected_quartic_translated": value,
                      "inspected_fiber_exterior": value not in low})
    assert collision(a, n) is None
    return {"N": n, "A": a, "all_multisets_checked": 6435,
            "valid": True, "T3": len(triples), "T4": len(quartics),
            "E4": len(quartics) - 29,
            "growth_gap": len(quartics) - 2 * len(triples),
            "triple_histogram": dict(Counter(map(len, triples.values()))),
            "marked_quartic_histogram": dict(Counter(map(len, quartics.values()))),
            "triple_zero_fiber": triples[0],
            "inspected_quartic": inspected_quartic,
            "inspected_marked_fiber": quartics[inspected_quartic],
            "inspected_ordinary_fiber": ordinary[inspected_quartic],
            "translated_fiber_tests": bases}


def main():
    even_model = (0, 1, 33, 1089, 20034, 37822, 39934, 39998)
    order3_model = (0, 1, 33, 1089, 20000, 57822, 59934, 59998)
    boundary_model = (0, 243, 351, 363, 365, 369, 405, 729)
    records = [statistics(even_model, 40000), statistics(order3_model, 60000),
               statistics(boundary_model, 5833, 1458)]
    for record in records:
        print(json.dumps(record))
    Path("stage3_root_model_results.json").write_text(
        json.dumps(records, indent=2) + "\n", encoding="ascii")


if __name__ == "__main__":
    main()
