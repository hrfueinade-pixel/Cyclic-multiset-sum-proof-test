"""Independent bounded h=0 verifier at two fixed odd moduli.

No original search helpers are imported. Prefix validity is checked by
direct multiset enumeration, not extension bitsets.
"""

from collections import defaultdict
from itertools import combinations_with_replacement
from math import gcd
import json
from pathlib import Path
from time import monotonic


def orbit_masks(n):
    parent = list(range(n))

    def root(x):
        while parent[x] != x:
            x = parent[x]
        return x

    for x in range(1, n):
        for y in (2 * x % n, (-x) % n):
            parent[root(x)] = root(y)
    groups = defaultdict(list)
    for x in range(1, n):
        groups[root(x)].append(x)
    blocks = [(len(g), sum(1 << x for x in g)) for g in groups.values()]
    result = []

    def visit(i, size, mask):
        if size == 56:
            result.append(mask)
            return
        if size > 56 or i == len(blocks):
            return
        visit(i + 1, size, mask)
        visit(i + 1, size + blocks[i][0], mask | blocks[i][1])

    visit(0, 0, 0)
    return result


def valid(a, n):
    target = sum(a) % n
    for indices in combinations_with_replacement(range(len(a)), len(a)):
        if indices == tuple(range(len(a))):
            continue
        if sum(a[i] for i in indices) % n == target:
            return False
    return True


def key(a, n):
    return min(tuple(sorted(u * (x - base) % n for x in a))
               for base in a for u in range(1, n) if gcd(u, n) == 1)


def search(n, seconds=25):
    start = monotonic()
    delta_masks = orbit_masks(n)
    units = sum(1 << x for x in range(1, n) if gcd(x, n) == 1)
    normalized = [m for m in delta_masks if not m & units or m & 2]
    accepted = set()
    nodes = [0] * 9
    completed = 0

    class Deadline(Exception):
        pass

    def walk(a, available, differences, adjacency):
        nodes[len(a)] += 1
        if monotonic() - start >= seconds:
            raise Deadline
        if len(a) == 8:
            assert len(differences) == 56 and valid(a, n)
            accepted.add(key(a, n))
            return
        if available.bit_count() < 8 - len(a):
            return
        while available:
            bit = available & -available
            available -= bit
            x = bit.bit_length() - 1
            new = {(x - y) % n for y in a} | {(y - x) % n for y in a}
            if len(new) != 2 * len(a) or new.intersection(differences):
                continue
            grown = a + (x,)
            if not valid(grown, n):
                continue
            walk(grown, available & adjacency[x], differences | new, adjacency)

    try:
        for delta in normalized:
            seed = (0, 1) if delta & units else (0,)
            adjacency = []
            for x in range(n):
                adjacency.append(sum(1 << ((x + d) % n)
                                     for d in range(1, n) if delta >> d & 1))
            available = delta & ~((1 << (seed[-1] + 1)) - 1)
            for x in seed:
                available &= adjacency[x]
            differences = {(x - y) % n for x in seed for y in seed if x != y}
            walk(seed, available, differences, adjacency)
            completed += 1
        status = "COMPLETE"
    except Deadline:
        status = "TIMEOUT"
    return {"N": n, "status": status, "seconds_limit": seconds,
            "elapsed_seconds": monotonic() - start,
            "orbit_union_masks": len(delta_masks),
            "normalized_masks": len(normalized),
            "completed_masks": completed, "valid_prefix_counts": nodes,
            "accepted_affine_keys": sorted(accepted)}


def main():
    results = [search(n) for n in (273, 255)]
    Path("stage5_h0_independent_results.json").write_text(
        json.dumps(results, indent=2) + "\n", encoding="ascii")
    for r in results:
        print(json.dumps(r, indent=2))


if __name__ == "__main__":
    main()
