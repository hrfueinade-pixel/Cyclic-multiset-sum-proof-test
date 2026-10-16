"""One declared cyclic control; no producer or historical imports.

Refutes a universal seven-predecessor cap for mixed-only quintic fibers.
Does not refute the conditional small-quartic-budget target.
"""
from collections import defaultdict
import json
from pathlib import Path


def words(degree, width=8):
    # Stars-and-bars positions, independent of the research generators.
    from itertools import combinations
    for bars in combinations(range(degree + width - 1), width - 1):
        boundaries = (-1,) + bars + (degree + width - 1,)
        yield tuple(boundaries[i + 1] - boundaries[i] - 1 for i in range(width))


def main():
    base = 53
    modulus = base ** 4
    signed = tuple(z * base ** i for i in range(4) for z in (2, -3))
    labels = tuple(x % modulus for x in signed)
    assert len(set(labels)) == 8
    target = sum(labels) % modulus
    fibers = {}
    for degree in (3, 4, 5, 8):
        fs = defaultdict(list)
        for p in words(degree):
            fs[sum(x * y for x, y in zip(labels, p)) % modulus].append(p)
        fibers[degree] = fs
    eight = fibers[8][target]
    assert eight == [(1,) * 8]
    assert sum(map(len, fibers[8].values())) == 6435
    assert all(len(fs) == 1 for fs in fibers[4].values())
    zero = fibers[5][0]
    expected = [tuple(3 if j == 2 * i else 2 if j == 2 * i + 1 else 0
                      for j in range(8)) for i in range(4)]
    assert set(zero) == set(expected)
    repeated4 = {q for q, ps in fibers[4].items() if max(ps[0]) >= 2}
    predecessors = [i for i, a in enumerate(labels) if (-a) % modulus in repeated4]
    assert predecessors == list(range(8))
    counts = {}
    ordinary_caps = {}
    for degree in (3, 4, 5):
        counts[str(degree)] = sum(any(max(p) >= 2 for p in ps)
                                  for ps in fibers[degree].values())
        ordinary_caps[str(degree)] = max(sum(sorted(p, reverse=True) ==
                                            [2] + [1] * (degree - 2) + [0] * (9 - degree)
                                            for p in ps)
                                        for ps in fibers[degree].values())
    assert counts == {"3": 64, "4": 260, "5": 733}
    assert ordinary_caps == {"3": 1, "4": 1, "5": 1}
    # Full cubic formula, computed directly rather than inferred from degree counts.
    delta = {a - b for a in labels for b in labels if a != b}
    delta = {d % modulus for d in delta}
    h = sum(2 * d % modulus not in delta for d in delta) // 2
    r3 = sum((len(ps) - 1) * (len(ps) - 2) // 2
             for ps in fibers[3].values() if any(max(p) >= 2 for p in ps))
    assert h == 28 and r3 == 0
    result = {"scope": "one fixed actual cyclic positive control, not a modulus search",
              "modulus": modulus, "signed_labels": signed, "residue_labels": labels,
              "mass_eight_words_checked": 6435, "full_valid": True,
              "repeated_value_counts": counts, "ordinary_multiplicity_caps": ordinary_caps,
              "h": h, "R3": r3, "zero_quintic_fiber": zero,
              "repeated_quartic_predecessor_labels": predecessors,
              "quartic_triangles": 0,
              "boundary": "T4=260>88 and large N; no sub-248 exclusion or counterexample"}
    Path(__file__).with_name("stage47_independent_control_results.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"full_valid": True, "counts": counts,
                      "predecessors": len(predecessors), "quartic_triangles": 0}))


if __name__ == "__main__":
    main()
