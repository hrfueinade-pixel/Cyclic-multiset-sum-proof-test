"""Finite arithmetic controls supporting the written elementary arguments.

These checks accompany, rather than replace, the quantified proofs in PROOF.md.
"""

from collections import Counter
from itertools import combinations, combinations_with_replacement
import json
from math import comb
from pathlib import Path


def main():
    assert 32 + 2 * (36 - comb(6, 2) - 6) == 62
    assert 128 + 2 * (64 - comb(8, 2) - 8) == 184
    remaining = set(range(1, 185))
    orbit_sizes = []
    while remaining:
        first = min(remaining)
        orbit = set()
        value = first
        while value not in orbit:
            orbit.add(value)
            value = 2 * value % 185
        assert value == first
        remaining -= orbit
        orbit_sizes.append(len(orbit))
    assert sorted(orbit_sizes) == [4, 36, 36, 36, 36, 36]
    assert all(36 * a + 4 * b != 56 for a in range(6) for b in range(2))
    # All simple three-edge graphs on five possible tail labels.
    types = Counter()
    for edges in combinations(list(combinations(range(5), 2)), 3):
        degrees = tuple(sorted(sum(i in edge for edge in edges) for i in range(5)))
        types[degrees] += 1
    assert sum(types.values()) == 120
    assert set(types) == {
        (0, 0, 2, 2, 2),
        (0, 1, 1, 1, 3),
        (0, 1, 1, 2, 2),
        (1, 1, 1, 1, 2),
    }
    # Coefficients of (c,t,p,w,q,E) in -4*n3+3*C4+S4.
    assert tuple(
        -4 * a + 3 * b + d
        for a, b, d in zip((1, 2, 1, 0, 1, 0), (2, 1, 1, 1, 0, 0), (0, 0, 1, 2, 0, 1))
    ) == (2, -5, 0, 5, -4, 1)
    # Independent enumeration of every degree-eight word in the equality set.
    points = (0, 1, 3, 7, 15, 31, 63, 127)
    words = list(combinations_with_replacement(range(8), 8))
    rivals = [w for w in words if sum(points[i] for i in w) % 248 == sum(points) % 248]
    assert len(words) == comb(15, 7) == 6435
    assert rivals == [tuple(range(8))]
    report = {
        "six_point_bound": 62,
        "initial_eight_point_packing": 184,
        "doubling_orbits_modulo_185": sorted(orbit_sizes),
        "tail_graphs_checked": 120,
        "weighted_coefficients": [2, -5, 0, 5, -4, 1],
        "equality_words_checked": 6435,
        "equality_representations": 1,
        "scope": "Arithmetic controls; written proofs supply the general implications.",
    }
    Path("elementary-identities-report.json").write_text(
        json.dumps(report, indent=2) + "\n"
    )
    print(json.dumps(report))


if __name__ == "__main__":
    main()
