"""Bounded tests of a proposed local charge for new quartic collisions.

No random sampling, modulus sweep, or assumed symmetry completeness.
Every accepted fixture is checked by all 6435 degree-eight multisets.
"""

from collections import defaultdict
from itertools import combinations, combinations_with_replacement, product
import json
from pathlib import Path
from time import monotonic

from stage3_growth_probe import EXISTING_NONBINARY_4093
from stage3_search import direct_valid_count


class Components:
    def __init__(self, size):
        self.parent = list(range(size))

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def join(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return 0
        self.parent[y] = x
        return 1


def inspect(a, modulus):
    checked = direct_valid_count(a, modulus)
    assert checked["valid"] and checked["multisets_enumerated"] == 6435
    assert len({2 * x % modulus for x in a}) == 8
    triples = defaultdict(list)
    for i, x in enumerate(a):
        for j, y in enumerate(a):
            triples[(2 * x + y) % modulus].append((i, j))
    marks = [(i, j, k) for i in range(8)
             for j, k in combinations_with_replacement(range(8), 2)]
    indices = {mark: i for i, mark in enumerate(marks)}
    components = Components(len(marks))
    for fiber in triples.values():
        for (i, j), (k, l) in combinations(fiber, 2):
            for z in range(8):
                components.join(indices[(i, *sorted((j, z)))],
                                indices[(k, *sorted((l, z)))])
    for i, j in combinations(range(8), 2):
        components.join(indices[(i, j, j)], indices[(j, i, i)])
    initial_roots = [components.find(i) for i in range(len(marks))]
    component_count = len(set(initial_roots))
    differences = {(x - y) % modulus: (i, j)
                   for i, x in enumerate(a) for j, y in enumerate(a) if i != j}
    assert len(differences) == 56
    fibers = defaultdict(dict)
    for index, (i, j, k) in enumerate(marks):
        value = (2 * a[i] + a[j] + a[k]) % modulus
        assert i not in fibers[value]
        fibers[value][i] = index
    fresh_loss_by_ordinary_count = defaultdict(int)
    fiber_records = []
    for value, fiber in fibers.items():
        groups = defaultdict(set)
        ordinary_count = 0
        for index in fiber.values():
            mark = marks[index]
            groups[initial_roots[index]].update(mark)
            ordinary_count += len(set(mark)) == 3
        supports = list(groups.values())
        assert all(x.isdisjoint(y) for x, y in combinations(supports, 2))
        if ordinary_count == 4:
            assert len(groups) == 1 and len(supports[0]) == 8
        if len(groups) > 1:
            fresh_loss_by_ordinary_count[ordinary_count] += len(groups) - 1
            fiber_records.append({"value": value, "ordinary_count": ordinary_count,
                                  "component_support_sizes": sorted(map(len, supports)),
                                  "new_loss": len(groups) - 1})
    pair_ranks = []
    internal_ordinary_collisions = 0
    for i, j in combinations(range(8), 2):
        local = Components(len(marks))
        rank = 0
        witnesses = []
        ordinary_values = []
        for value, fiber in fibers.items():
            if i not in fiber or j not in fiber:
                continue
            left, right = fiber[i], fiber[j]
            if initial_roots[left] == initial_roots[right]:
                continue
            assert set(marks[left][1:]).isdisjoint(marks[right][1:])
            delta = (a[i] - a[j]) % modulus
            if (len(set(marks[left])) == len(set(marks[right])) == 3
                    and 2 * delta % modulus in differences):
                v, u = differences[2 * delta % modulus]
                assert v in marks[left][1:] and u in marks[right][1:]
                b = next(t for t in marks[left][1:] if t != v)
                e = next(t for t in marks[right][1:] if t != u)
                assert differences[4 * delta % modulus] == (e, b)
                assert len({i, j, u, v, b, e}) == 6
                ordinary_values.append(value)
                internal_ordinary_collisions += 1
            if local.join(initial_roots[left], initial_roots[right]):
                rank += 1
                witnesses.append({"value": value,
                                  "left": [a[t] for t in marks[left]],
                                  "right": [a[t] for t in marks[right]]})
        assert len(ordinary_values) <= 1
        if rank:
            pair_ranks.append({"centers": [a[i], a[j]], "rank": rank,
                               "witnesses": witnesses})
    loss = component_count - len(fibers)
    delta = {(x - y) % modulus for x in a for y in a if x != y}
    h = sum(2 * d % modulus not in delta for d in delta) // 2
    r3 = sum((len(f) - 1) * (len(f) - 2) // 2 for f in triples.values())
    assert len(triples) - 36 == h + r3
    cubic_dimension = 64 - len(triples)
    shadow_credit = 8 * cubic_dimension - (260 - component_count)
    assert shadow_credit >= 0
    return {"N": modulus, "A": a, "multisets_checked": 6435,
            "T3": len(triples), "T4": len(fibers),
            "growth_gap": len(fibers) - 2 * len(triples),
            "propagation_components": component_count,
            "new_collision_loss": loss,
            "missing_doubling_pairs": h, "R3": r3,
            "cubic_relation_dimension": cubic_dimension,
            "shadow_credit": shadow_credit,
            "internal_ordinary_collision_pairs": internal_ordinary_collisions,
            "naive_shadow_suffices_if_loss_h": 5 * h + 6 * r3 >= 53,
            "loss_at_most_h": loss <= h,
            "component_growth_17_plus_h": component_count >= 2 * len(triples) + h + 17,
            "fresh_loss_by_ordinary_count": dict(fresh_loss_by_ordinary_count),
            "fresh_fiber_records": fiber_records,
            "local_pair_ranks": pair_ranks,
            "max_local_rank": max((r["rank"] for r in pair_ranks), default=0)}


def fixtures():
    binary = tuple((1 << i) - 1 for i in range(8))
    for n in (255, 256, 1022):
        yield "existing binary", binary, n
    yield "ordinary-four integer", (0, 2, 38, 722, 6479, 6839, 6840, 6858), 54865
    yield "negative-three cycle", (0, 2, 20, 182, 1093, 1579, 1633, 1639), 1640
    for a in EXISTING_NONBINARY_4093:
        yield "existing nonbinary", a, 4093
    yield "even cubic exception", (0, 1, 33, 1089, 20034, 37822, 39934, 39998), 40000
    yield "order-three pair", (0, 1, 33, 1089, 20000, 57822, 59934, 59998), 60000
    yield "negative-three boundary", (0, 243, 351, 363, 365, 369, 405, 729), 5833
    yield "CRT 4+5", (0, 15, 31, 45, 93, 105, 217, 225), 465
    yield "CRT 2+7", (0, 3, 9, 21, 45, 93, 127, 189), 381
    yield "two collisions same centers", (0, 1, 13, 169, 2043, 2197, 28561, 28719), 229753
    yield "three collisions same centers", (0, 4609, 4610, 4626, 4898, 9248, 9522, 9792), 78337
    yield "four binary pairs", (0, 1, 65, 67, 4225, 4229, 274625, 274633), 2197065
    for alphabet in ((2, 3), (2, 4), (3, 4)):
        patterns = sorted({min(q[i:] + q[:i] for i in range(8))
                           for q in product(alphabet, repeat=8)})
        for q in patterns:
            prefix = 1
            a = []
            for radix in q:
                a.append(prefix - 1)
                prefix *= radix
            yield "mixed radix " + str(q), tuple(a), prefix - 1


def main():
    start = monotonic()
    seconds_limit = 30
    results = []
    seen = set()
    complete = True
    candidates = 0
    for label, a, n in fixtures():
        candidates += 1
        if monotonic() - start >= seconds_limit:
            complete = False
            break
        key = a, n
        if key in seen:
            continue
        seen.add(key)
        result = inspect(a, n)
        result["label"] = label
        results.append(result)
    report = {"seconds_limit": seconds_limit, "elapsed_seconds": monotonic() - start,
              "planned_fixture_records": 129, "candidate_records_seen": candidates,
              "distinct_pairs_tested": len(results), "valid_pairs": len(results),
              "distinct_collision_signatures": len({
                  (r["T3"], r["T4"], r["propagation_components"],
                   r["missing_doubling_pairs"], r["R3"], r["max_local_rank"])
                  for r in results}),
              "fixtures_outside_naive_shadow_range": sum(
                  not r["naive_shadow_suffices_if_loss_h"] for r in results),
              "complete_fixed_batch": complete, "complete_search_of_valid_sets": False,
              "local_rank_one_counterexamples": [r for r in results if r["max_local_rank"] > 1],
              "global_loss_28_counterexamples": [r for r in results if r["new_collision_loss"] > 28],
              "loss_h_counterexamples": [r for r in results if not r["loss_at_most_h"]],
              "component_growth_counterexamples": [r for r in results if not r["component_growth_17_plus_h"]],
              "growth_17_counterexamples": [r for r in results if r["growth_gap"] < 17],
              "results": results}
    Path("stage4_lemma_results.json").write_text(json.dumps(report, indent=2) + "\n", encoding="ascii")
    print(json.dumps({k: v for k, v in report.items() if k != "results"}, indent=2))


if __name__ == "__main__":
    main()
