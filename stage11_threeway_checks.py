"""Fixed arithmetic and fixture checks for the stage11 checkpoint proof."""

from collections import Counter, defaultdict
from itertools import combinations_with_replacement, product
from math import gcd
import json
from pathlib import Path


def orbit(n, start=1):
    answer = set()
    x = start % n
    while x not in answer:
        answer.add(x)
        answer.add(-x % n)
        x = 2 * x % n
    return answer


def main():
    expected = {5: 4, 7: 6, 15: 8, 25: 20, 35: 24, 75: 40,
                105: 24, 87: 56, 29: 28, 69: 44, 23: 22,
                117: 24, 39: 24}
    assert all(len(orbit(n)) == size for n, size in expected.items())
    assert 67 not in orbit(117)
    graph_counts = Counter()
    annihilators = {0: 63, 1: 69, 2: 87, 3: 117}
    patterns = 0
    for targets in product(*[tuple(j for j in range(3) if j != i) for i in range(3)]):
        pair = next(((i, j) for i in range(3) for j in range(i + 1, 3)
                     if targets[i] == j and targets[j] == i), None)
        for types in product(("U", "V"), repeat=3):
            patterns += 1
            if pair is None:
                key = "three_cycle_" + str(types.count("U")) + "U"
                a = [7 if t == "U" else 5 for t in types]
                b = [9 - value for value in a]
                d = (a[0] * a[1] * a[2] + b[0] * b[1] * b[2]) // 3
                assert d == annihilators[types.count("U")]
            else:
                i, j = pair
                k = next(v for v in range(3) if v not in pair)
                if types[i] == types[j] == "U":
                    key = "two_cycle_UU_tail_" + types[k]
                elif types[i] == types[j] == "V":
                    key = "two_cycle_VV"
                else:
                    key = "two_cycle_UV"
            graph_counts[key] += 1
    assert patterns == 64
    assert graph_counts == {"three_cycle_3U": 2, "three_cycle_2U": 6,
                           "three_cycle_1U": 6, "three_cycle_0U": 2,
                           "two_cycle_UU_tail_U": 6, "two_cycle_UU_tail_V": 6,
                           "two_cycle_UV": 24, "two_cycle_VV": 12}
    for n, core in ((117, (0, 60, 84, 1, 115, 67)),
                    (63, (0, 48, 51, 1, 31, 25))):
        assert all((2 * core[i] + core[i + 3]) % n == 1 for i in range(3))
        for i in range(3):
            j = (i + 1) % 3
            partner = 2 * core[i + 3] + core[j + 3] if n == 117 else 2 * core[j + 3] + core[i + 3]
            assert 3 * core[i] % n == partner % n
        if n == 63:
            assert sum(core) % n == 3 * core[4] % n
    n = 8000625
    lifts = (0, 3, 41, 4, -2, -78, 1000, 1000000)
    a = tuple(value % n for value in lifts)
    target = sum(a) % n
    checked = 0
    for multiset in combinations_with_replacement(range(8), 8):
        checked += 1
        if sum(a[i] for i in multiset) % n == target:
            assert multiset == tuple(range(8)), multiset
    assert checked == 6435
    delta = {(x - y) % n for x in a for y in a if x != y}
    assert len(delta) == 56 and all(3 * d % n for d in delta)
    h = sum(2 * d % n not in delta for d in delta) // 2
    assert h == 23
    cubics = defaultdict(list)
    for i, x in enumerate(a):
        for j, y in enumerate(a):
            cubics[(2 * x + y) % n].append((i, j))
    multiway = {value: marks for value, marks in cubics.items() if len(marks) >= 3}
    assert multiway == {4: [(0, 3), (1, 4), (2, 5)]}
    assert 3 * a[0] % n == (2 * a[4] + a[3]) % n
    result = {"complete_fixed_checks": True, "arrow_type_patterns": patterns,
              "graph_counts": dict(graph_counts), "fixed_order_orbit_sizes": expected,
              "fixture_candidates": 1, "valid_fixtures": 1,
              "fixture": {"N": n, "integer_lifts": lifts, "h": h,
                          "validity_multisets_checked": checked,
                          "threeway_fibers": multiway},
              "scope": "Proof arithmetic and one non-h0 control; no three-way exclusion."}
    Path("stage11_threeway_results.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
