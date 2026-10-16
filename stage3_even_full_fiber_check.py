"""Independent exact enumeration of even full non-type22 fiber cases.

No imports from earlier modules. Only the determinant-derived moduli and
the proved one-path functional graph configurations are enumerated.
"""

from itertools import combinations, combinations_with_replacement
import json
from math import gcd, prod
from pathlib import Path
from time import monotonic


def candidate_moduli():
    moduli = set()
    for q in range(5):
        k = 8 - q
        for count in range(1, k + 1):
            for cycles in combinations_with_replacement(range(1, k + 1), count):
                if sum(cycles) > k or 2 in cycles or cycles.count(1) > 2:
                    continue
                determinant = 2**q * 3**(k - sum(cycles))
                determinant *= prod(3**ell - (-1)**ell for ell in cycles)
                assert determinant % 4 == 0
                moduli.update(n for n in range(188, 248, 2) if determinant // 4 % n == 0)
    return sorted(moduli)


def closed_configurations(n, value):
    successor = [(value - 3*x) % n for x in range(n)]
    cycles = set()
    tails = set()
    for start in range(n):
        position = {}
        sequence = []
        current = start
        while current not in position:
            position[current] = len(sequence)
            sequence.append(current)
            current = successor[current]
        boundary = position[current]
        cycle = frozenset(sequence[boundary:])
        if len(cycle) != 2 and len(cycle) <= 8:
            cycles.add(cycle)
            if boundary and len(sequence) <= 8:
                tails.add(frozenset(sequence))
    cycle_list = sorted(cycles, key=lambda c: (len(c), sorted(c)))
    unions = set()

    def choose(index, current):
        if index == len(cycle_list):
            unions.add(current)
            return
        choose(index + 1, current)
        merged = current | cycle_list[index]
        if len(merged) <= 8:
            choose(index + 1, merged)

    choose(0, frozenset())
    configurations = {u for u in unions if 4 <= len(u) <= 8}
    for tail in tails:
        configurations.update(u | tail for u in unions if 4 <= len(u | tail) <= 8)
    return configurations, successor


def unique_differences(a, n):
    return len({(x-y) % n for x in a for y in a if x != y}) == len(a)*(len(a)-1)


def direct_valid(a, n):
    target = sum(a) % n
    hits = 0
    for indices in combinations_with_replacement(range(8), 8):
        if sum(a[i] for i in indices) % n == target:
            hits += 1
    return hits == 1


def run(seconds=90):
    start = monotonic()
    records = []
    for n in candidate_moduli():
        counts = {"N": n, "closed_sets": 0, "Sidon_nonordinary_sets": 0,
                  "determinant_passing": 0, "completions": 0,
                  "Sidon_completions": 0, "cube_passing": 0, "valid": 0}
        for value in range(gcd(4, n)):
            configurations, successor = closed_configurations(n, value)
            for h in configurations:
                if monotonic() - start > seconds:
                    return {"complete": False, "records": records, "partial_record": counts,
                            "seconds_limit": seconds, "elapsed_seconds": monotonic()-start}
                counts["closed_sets"] += 1
                if sum(successor[x] == x for x in h) > 2 or not unique_differences(h, n):
                    continue
                counts["Sidon_nonordinary_sets"] += 1
                cycles = set()
                for x in h:
                    sequence = []
                    current = x
                    while current not in sequence:
                        sequence.append(current)
                        current = successor[current]
                    cycles.add(frozenset(sequence[sequence.index(current):]))
                q = 8 - len(h)
                trees = len(h) - sum(map(len, cycles))
                determinant = 2**q * 3**trees * prod(3**len(c)-(-1)**len(c) for c in cycles)
                assert determinant % 4 == 0
                if determinant // 4 % n:
                    continue
                counts["determinant_passing"] += 1
                wanted = {(value-d-e) % n for d,e in combinations(h, 2)}
                centers = [c for c in range(n) if c not in h and 2*c % n in wanted]
                for added in combinations(centers, q):
                    counts["completions"] += 1
                    a = tuple(sorted(h | set(added)))
                    assert len(a) == 8
                    if not unique_differences(a, n):
                        continue
                    counts["Sidon_completions"] += 1
                    b = tuple((x-a[0]) % n for x in a[1:])
                    sums = {sum(b[i] for i in range(7) if mask & (1 << i)) % n
                            for mask in range(128)}
                    if len(sums) != 128:
                        continue
                    counts["cube_passing"] += 1
                    counts["valid"] += direct_valid(a, n)
        records.append(counts)
    return {"complete": True, "records": records, "seconds_limit": seconds,
            "elapsed_seconds": monotonic()-start,
            "scope": "full non-type22 fiber configurations only"}


if __name__ == "__main__":
    result = run()
    print(json.dumps(result, indent=2))
    Path("stage3_independent_even_full_fiber_result.json").write_text(
        json.dumps(result, indent=2)+"\n", encoding="ascii")
