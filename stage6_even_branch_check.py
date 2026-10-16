"""Independent finite checks of the h=0 even-subgroup classification.

No project imports. Five fixed fixtures, each checked through all 6435
eight-term multisets; both literal cubic propagation and support overlap
are constructed and compared. Tests do not prove the classification.
"""

from collections import Counter, defaultdict
from itertools import combinations, combinations_with_replacement
from math import gcd
import json
from pathlib import Path


def components(graph):
    remaining = set(range(len(graph)))
    result = []
    while remaining:
        pending = [remaining.pop()]
        visited = set(pending)
        while pending:
            for nxt in graph[pending.pop()]:
                if nxt in remaining:
                    remaining.remove(nxt)
                    visited.add(nxt)
                    pending.append(nxt)
        result.append(frozenset(visited))
    return frozenset(result)


def check(a, n):
    target = sum(a) % n
    hits = []
    checked = 0
    for u in combinations_with_replacement(range(8), 8):
        checked += 1
        if sum(a[i] for i in u) % n == target:
            hits.append(u)
    assert checked == 6435 and hits == [tuple(range(8))]
    divisor = gcd(n, *(x - a[0] for x in a))
    order = n // divisor
    b = tuple((x - a[0]) // divisor % order for x in a)
    delta = {(x - y) % order for x in b for y in b if x != y}
    assert len(delta) == 56
    h = sum(2 * d % order not in delta for d in delta) // 2
    pair_sums = {(b[i] + b[j]) % order: (i, j)
                 for i, j in combinations_with_replacement(range(8), 2)}
    assert len(pair_sums) == 36
    antipodal_types = Counter()
    difference_pairs = []
    if order % 2 == 0:
        t = order // 2
        for value, pair in pair_sums.items():
            opposite = (value + t) % order
            if opposite in pair_sums and value < opposite:
                double_count = (pair[0] == pair[1]) + (
                    pair_sums[opposite][0] == pair_sums[opposite][1])
                antipodal_types[("SS", "DS", "DD")[double_count]] += 1
        difference_pairs = [(d, (d + t) % order) for d in delta
                            if (d + t) % order in delta and d < (d + t) % order]
        loss = 2 * antipodal_types["DS"] + 4 * antipodal_types["SS"] + antipodal_types["DD"]
        assert loss == len(difference_pairs) == 56 - len({2 * d % order for d in delta})
        if h == 0:
            parity = Counter(x % 2 for x in b)
            assert sorted(parity.values()) == [1, 7]
            assert antipodal_types == {"DS": 7} and order == 254

    repeated_triples = defaultdict(list)
    for u in combinations_with_replacement(range(8), 3):
        if len(set(u)) < 3:
            repeated_triples[sum(b[i] for i in u) % order].append(u)
    vertices = [u for u in combinations_with_replacement(range(8), 4) if len(set(u)) < 4]
    assert len(vertices) == 260
    positions = {u: i for i, u in enumerate(vertices)}
    literal = [set() for _ in vertices]
    for fiber in repeated_triples.values():
        for u, v in combinations(fiber, 2):
            for z in range(8):
                i = positions[tuple(sorted(u + (z,)))]
                j = positions[tuple(sorted(v + (z,)))]
                literal[i].add(j)
                literal[j].add(i)
    quartics = defaultdict(list)
    for i, u in enumerate(vertices):
        quartics[sum(b[j] for j in u) % order].append(i)
    overlap = [set() for _ in vertices]
    for fiber in quartics.values():
        for i, j in combinations(fiber, 2):
            if set(vertices[i]).intersection(vertices[j]):
                overlap[i].add(j)
                overlap[j].add(i)
    assert literal == overlap
    k = len(components(literal))
    t3 = len(repeated_triples)
    t4 = len(quartics)
    if h == 0:
        assert k == t4
    return {"N": n, "A": a, "difference_subgroup_order": order,
            "multisets_checked": checked, "h": h, "T3": t3,
            "T4": t4, "E4": t4 - 29, "K": k, "D": k - t4,
            "antipodal_pair_sum_types": dict(antipodal_types),
            "doubling_difference_loss": len(difference_pairs),
            "literal_and_overlap_graphs_equal": True}


def main():
    even = (0, 1, 129, 131, 135, 143, 159, 191)
    binary = tuple((1 << i) - 1 for i in range(8))
    fixtures = [(even, 254), (tuple(2 * x for x in even), 508),
                (binary, 256), (tuple(2 * x for x in binary), 510),
                ((0, 1, 33, 1089, 20034, 37822, 39934, 39998), 40000)]
    result = [check(a, n) for a, n in fixtures]
    Path("stage6_even_branch_results.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
