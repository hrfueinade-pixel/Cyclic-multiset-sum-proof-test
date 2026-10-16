"""Small exact checks of local quartic restrictions and their limitation.

All six fixed eight-point fixtures are checked through all 6435 multisets.
No project imports, random sampling, or modulus sweep. The counterexample
is valid but NOT h=0; it defeats a local doubling-closure shortcut only.
"""

from collections import Counter, defaultdict
from itertools import combinations, combinations_with_replacement
from math import gcd
import json
from pathlib import Path


class Components:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, i):
        while self.parent[i] != i:
            self.parent[i] = self.parent[self.parent[i]]
            i = self.parent[i]
        return i

    def join(self, i, j):
        self.parent[self.find(i)] = self.find(j)


def kind(u):
    multiplicities = sorted(Counter(u).values(), reverse=True)
    return {(4,): "4", (3, 1): "31", (2, 2): "22", (2, 1, 1): "211"}[tuple(multiplicities)]


def inspect(a, n):
    target = sum(a) % n
    hits = [u for u in combinations_with_replacement(range(8), 8)
            if sum(a[i] for i in u) % n == target]
    assert hits == [tuple(range(8))]
    delta = {(x - y) % n for x in a for y in a if x != y}
    assert len(delta) == 56
    assert len({(x + y) % n for x, y in combinations_with_replacement(a, 2)}) == 36
    triples = defaultdict(list)
    for u in combinations_with_replacement(range(8), 3):
        if len(set(u)) < 3:
            triples[sum(a[i] for i in u) % n].append(u)
    vertices = [u for u in combinations_with_replacement(range(8), 4) if len(set(u)) < 4]
    index = {u: i for i, u in enumerate(vertices)}
    graph = [set() for _ in vertices]
    ds = Components(len(vertices))
    for fiber in triples.values():
        for u, v in combinations(fiber, 2):
            for z in range(8):
                i, j = index[tuple(sorted(u + (z,)))], index[tuple(sorted(v + (z,)))]
                ds.join(i, j)
                graph[i].add(j)
                graph[j].add(i)
    quartics = defaultdict(list)
    for i, u in enumerate(vertices):
        quartics[sum(a[j] for j in u) % n].append(i)
    local31 = []
    disjoint_by_types = Counter()
    for value, fiber in quartics.items():
        for i, j in combinations(fiber, 2):
            u, v = vertices[i], vertices[j]
            if set(u).intersection(v):
                assert ds.find(i) == ds.find(j)
                continue
            ku, kv = kind(u), kind(v)
            disjoint_by_types["/".join(sorted((ku, kv)))] += 1
            if ku == kv == "31":
                cu = next(p for p, m in Counter(u).items() if m == 3)
                cv = next(p for p, m in Counter(v).items() if m == 3)
                d = (a[cu] - a[cv]) % n
                if 2 * d % n in delta:
                    assert n // gcd(n, d) == 5
                    sizes = sorted(Counter(x % (n // 5) for x in a).values())
                    assert sizes == [1, 1, 1, 1, 2, 2]
                    local31.append({"value": value, "left": tuple(a[k] for k in u),
                                    "right": tuple(a[k] for k in v),
                                    "degrees": [len(graph[i]), len(graph[j])],
                                    "different_components": ds.find(i) != ds.find(j)})
            if {ku, kv} == {"22", "31"}:
                double, triple = (u, v) if ku == "22" else (v, u)
                centers = list(set(double))
                c = next(p for p, m in Counter(triple).items() if m == 3)
                assert not all(2 * (a[p] - a[c]) % n in delta for p in centers)
            if n % 2 and ku in {"4", "22"} and kv in {"4", "22"}:
                raise AssertionError("Odd doubling injectivity forbids this collision")
    k = len({ds.find(i) for i in range(len(vertices))})
    h = sum(2 * d % n not in delta for d in delta) // 2
    r3 = sum((len(v) - 1) * (len(v) - 2) // 2 for v in triples.values())
    assert len(triples) == 36 + h + r3
    if n % 2 and h == 0 and r3 == 0:
        assert not any(v["different_components"] for v in local31)
    return {"N": n, "A": a, "multisets_checked": 6435,
            "h": h, "R3": r3,
            "T3": len(triples), "T4": len(quartics), "K": k, "D": k - len(quartics),
            "disjoint_vertex_pairs_by_type": dict(disjoint_by_types),
            "31_collision_with_present_doubled_center_difference": local31}


def crt_pair(c, d, q):
    return (d + q * ((c - d) * pow(q, -1, 5) % 5)) % (5 * q)


def low_block_table():
    points = [(0, 0), (1, 0), (0, 1), (2, 1)]

    def value(u):
        return sum(points[i][1] for i in u), sum(points[i][0] for i in u) % 5

    triples = defaultdict(list)
    for u in combinations_with_replacement(range(4), 3):
        if len(set(u)) < 3:
            triples[value(u)].append(u)
    vertices = [u for u in combinations_with_replacement(range(4), 4) if len(set(u)) < 4]
    index = {u: i for i, u in enumerate(vertices)}
    ds = Components(len(vertices))
    for fiber in triples.values():
        for u, v in combinations(fiber, 2):
            for z in range(4):
                ds.join(index[tuple(sorted(u + (z,)))], index[tuple(sorted(v + (z,)))])
    table = []
    expected = [(5, 5, 5), (8, 5, 6), (8, 4, 4), (8, 5, 6), (5, 5, 5)]
    for k in range(5):
        layer = [i for i, u in enumerate(vertices) if value(u)[0] == k]
        counts = len(layer), len({value(vertices[i]) for i in layer}), len({ds.find(i) for i in layer})
        assert counts == expected[k]
        table.append({"B_terms": k, "vertices": counts[0], "fibers": counts[1], "components": counts[2]})
    return table


def order_five_fixture():
    radix = 9
    q = 8 * radix ** 4 + 1
    points = [(0, 0), (1, 0), (0, 1), (2, 1)] + [(0, radix ** k) for k in range(1, 5)]
    a = tuple(crt_pair(c, d, q) for c, d in points)
    result = inspect(a, 5 * q)
    assert result["h"] > 0 and result["D"] == 2
    assert len(result["31_collision_with_present_doubled_center_difference"]) == 2
    assert all(r["degrees"] == [0, 0] and r["different_components"]
               for r in result["31_collision_with_present_doubled_center_difference"])
    result["CRT_coordinates"] = points
    result["radix"] = radix
    result["Q"] = q
    result["low_block_table"] = low_block_table()
    return result


def main():
    binary = tuple((1 << i) - 1 for i in range(8))
    fixtures = [(binary, 255), (binary, 256),
                ((0, 1, 129, 131, 135, 143, 159, 191), 254),
                ((0, 1, 13, 169, 2043, 2197, 28561, 28719), 229753),
                ((0, 4609, 4610, 4626, 4898, 9248, 9522, 9792), 78337)]
    result = {"local_order_five_counterexample": order_five_fixture(),
              "fixed_controls": [inspect(a, n) for a, n in fixtures],
              "scope": "Six fixed valid fixtures; not a global proof from testing."}
    Path("stage7_collision_mechanism_results.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
