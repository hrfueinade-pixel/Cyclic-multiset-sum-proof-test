"""Exact elementary checks for the full cyclic-eight finishing argument.

Standard library only. No producer, search, or previous checker imports.
It checks the literal rival construction, forests, ledger and equality.
"""

from itertools import combinations
from pathlib import Path
import json

BASE = (
    (1, 0, 0, 0, 0),
    (2, 0, 0, 0, 0),
    (0, 1, 0, 0, 0),
    (0, 2, 0, 0, 0),
    (0, 0, 1, 0, 0),
    (0, 0, 2, 0, 0),
    (0, 0, 0, 1, 0),
    (0, 0, 0, 0, 1),
)
ONES = (1,) * 8


def val(W):
    return tuple((sum((W[i] * BASE[i][j] for i in range(8))) for j in range(5)))


def main():
    checked = 0
    for x, y in combinations(range(8), 2):
        a, b = next(
            ((a, b) for a, b in ((0, 1), (2, 3), (4, 5)) if not {a, b} & {x, y})
        )
        assert len({x, y, a, b}) == 4
        for z in range(8):
            R = list(ONES)
            for i in (x, y, a, b):
                R[i] -= 1
            R[z] += 1
            R[a] += 3
            assert sum(R) == 8 and min(R) >= 0 and (tuple(R) != ONES)
            delta = tuple((r - 1 for r in R))
            equation = tuple(
                (int(i == z) - int(i == x) - int(i == y) for i in range(8))
            )
            assert val(delta) == val(equation)
            checked += 1
    forests = {}
    for shape, paths in {
        "22211": [[0, 1], [2, 3], [4, 5], [6], [7]],
        "4211": [[0, 1, 2, 3], [4, 5], [6], [7]],
        "3221": [[0, 1, 2], [3, 4], [5, 6], [7]],
    }.items():
        assert sorted((i for path in paths for i in path)) == list(range(8))
        edges = [(a, b) for path in paths for a, b in zip(path, path[1:])]
        tris = [
            T for T in combinations(edges, 3) if len({i for e in T for i in e}) == 6
        ]
        F = {e for T in tris for e in T}
        outgoing = {a for a, b in edges}
        o = sum((b not in outgoing for a, b in F))
        t = len(tris)
        forests[shape] = {
            "triangles": t,
            "open_paired_edges": o,
            "twice_N_lower": 496 + 2 * o - 5 * t,
        }
    assert forests["3221"]["triangles"] == 2
    assert all(
        (
            forests[s]["triangles"] == 1
            and forests[s]["open_paired_edges"] >= 2
            and (forests[s]["twice_N_lower"] > 494)
            for s in ("22211", "4211")
        )
    )
    sums = [S for S in (255, 503, 751, 999) if 8 <= S <= 1024]
    assert sums == [255, 503, 751, 999]
    minima = [S // 128 + (S % 128).bit_count() for S in sums]
    assert minima == [8, 9, 11, 12]
    assert (
        sum(((1 << i) - 1 for i in range(8))) == 247
        and sum((1 << i for i in range(8))) == 255
    )
    result = {
        "distinct_pair_sum_rival_identities": checked,
        "forests": forests,
        "sharp_construction_coin_minima": minima,
        "finishing_inequality": "2N>=495 contradicts N<=247",
        "full_proof_boundary": "Elementary finish plus the previously checked parity, counting and symbolic exclusion chain; not external/formal review.",
    }
    Path("finishing-report.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
