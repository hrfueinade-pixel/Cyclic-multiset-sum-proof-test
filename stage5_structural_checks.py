"""Small direct checks of the proved tree and quartic-component formulas."""

from collections import Counter, defaultdict
from itertools import combinations_with_replacement
import json
from pathlib import Path


def check(a, n):
    target = sum(a) % n
    hits = [u for u in combinations_with_replacement(range(8), 8)
            if sum(a[i] for i in u) % n == target]
    assert hits == [tuple(range(8))]
    delta = {(x - y) % n for x in a for y in a if x != y}
    assert len(delta) == 56 and {2 * d % n for d in delta} == delta
    triples = defaultdict(list)
    for i in range(8):
        for j in range(8):
            triples[(2 * a[i] + a[j]) % n].append((i, j))
    assert Counter(map(len, triples.values())) == {1: 8, 2: 28}
    f = {v[0][0]: v[0][1] for v in triples.values() if len(v) == 1}
    assert set(f) == set(f.values()) == set(range(8))
    assert all(i != j for i, j in f.items())
    stars = 0
    for base in range(8):
        edges = {}
        labels = set()
        for fiber in triples.values():
            if len(fiber) != 2:
                continue
            for (d, b), (e, r) in (fiber, fiber[::-1]):
                if b == base:
                    assert d not in edges and e != base and r != base
                    edges[d] = e
                    labels.add(r)
        root = next(i for i, j in f.items() if j == base)
        assert set(edges) == set(range(8)) - {root}
        assert labels == set(range(8)) - {base}
        for d in range(8):
            visited = set()
            while d != root:
                assert d not in visited
                visited.add(d)
                d = edges[d]
        stars += set(edges.values()) == {root}
    quartics = defaultdict(list)
    for u in combinations_with_replacement(range(8), 4):
        if len(set(u)) < 4:
            quartics[sum(a[i] for i in u) % n].append(u)
    paths = cycles = components = 0
    for fiber in quartics.values():
        graph = [{j for j, v in enumerate(fiber)
                  if j != i and set(u).intersection(v)}
                 for i, u in enumerate(fiber)]
        assert all(len(neighbors) <= 2 for neighbors in graph)
        unseen = set(range(len(fiber)))
        fiber_components = 0
        while unseen:
            pending = [unseen.pop()]
            visited = set(pending)
            while pending:
                for j in graph[pending.pop()]:
                    if j in unseen:
                        unseen.remove(j)
                        visited.add(j)
                        pending.append(j)
            is_cycle = all(len(graph[i]) == 2 for i in visited)
            cycles += is_cycle
            paths += not is_cycle
            components += 1
            fiber_components += 1
        assert fiber_components == 1
    assert paths == 36 and components == 36 + cycles
    return {"N": n, "A": a, "singleton_permutation": f,
            "rooted_trees": 8, "star_trees": stars,
            "quartic_paths_or_isolated": paths, "quartic_cycles": cycles,
            "K": components, "T4": len(quartics), "D": 0,
            "multisets_checked": 6435}


def main():
    binary = tuple((1 << i) - 1 for i in range(8))
    results = [check(binary, 255),
               check((0, 1, 9, 73, 75, 91, 219, 223), 255),
               check(tuple(2 * x for x in binary), 510)]
    Path("stage5_structural_results.json").write_text(
        json.dumps(results, indent=2) + "\n", encoding="ascii")
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
