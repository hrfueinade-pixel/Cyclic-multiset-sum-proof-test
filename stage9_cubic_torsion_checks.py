"""Bounded exact bookkeeping for exclusion of order-three differences.

Standard library only. Eleven cycle partitions and their sign choices;
five relation-derived quotient groups <=105; 256 signed orientations;
exact cyclotomic ranks; three fixed eight-point fixtures. No modulus
sweep, random sampling, external algebra package, or proof by testing.
"""

from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations_with_replacement, product
from math import gcd, lcm
import json
from pathlib import Path


def partitions(total, least=1):
    if total == 0:
        yield ()
    for first in range(least, total + 1):
        for rest in partitions(total - first, first):
            yield (first,) + rest


def cycle_orders():
    records = []
    high = set()
    for sizes in partitions(6):
        for signs in product((-1, 1), repeat=len(sizes)):
            annihilator = 3 * lcm(*(abs(1 - s * 2 ** k) for s, k in zip(signs, sizes)))
            assert annihilator <= 315
            if annihilator >= 184:
                high.add(annihilator)
            records.append({"cycle_lengths": sizes, "cycle_sign_products": signs,
                            "cyclic_group_annihilator": annihilator})
    assert high == {189, 195, 255, 279, 315}
    return {"partitions": 11, "signed_partition_records": len(records),
            "possible_orders_at_least_184": sorted(high), "records": records}


def orbits(n):
    unseen = set(range(1, n))
    answer = []
    while unseen:
        a = min(unseen)
        doubled = set()
        x = a
        while x not in doubled:
            doubled.add(x)
            x = 2 * x % n
        orbit = doubled | {(-x) % n for x in doubled}
        unseen -= orbit
        answer.append(sorted(orbit))
    return answer


def quotient_structures():
    result = []
    for n in (63, 65, 85, 93, 105):
        groups = orbits(n)
        assert 1 << len(groups) <= 8192
        patterns = Counter()
        for selected in product((False, True), repeat=len(groups)):
            union = [x for group, take in zip(groups, selected) if take for x in group]
            if len(union) != 12 or gcd(n, *union) != 1:
                continue
            signature = tuple(sorted((n // gcd(n, group[0]), len(group))
                                     for group, take in zip(groups, selected) if take))
            patterns[signature] += 1
        result.append({"quotient_order": n, "orbit_count": len(groups),
                       "masks_examined": 1 << len(groups),
                       "generating_twelve_point_patterns": [
                           {"element_orders_and_orbit_sizes": pattern, "count": count}
                           for pattern, count in sorted(patterns.items())]})
    expected = {
        63: {((63, 12),): 3, ((7, 6), (9, 6)): 1},
        65: {((65, 12),): 4},
        85: {((5, 4), (17, 8)): 2},
        93: {((3, 2), (31, 10)): 3},
        105: {((3, 2), (5, 4), (7, 6)): 1},
    }
    for r in result:
        actual = {tuple(map(tuple, p["element_orders_and_orbit_sizes"])): p["count"]
                  for p in r["generating_twelve_point_patterns"]}
        assert actual == expected[r["quotient_order"]]
    return result


def convolution(a, b):
    n = len(a)
    answer = [0] * n
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            answer[(i + j) % n] += x * y
    return answer


def orientation_checks():
    templates = [(63, [1, 2, 4, 8, 16, 32]),
                 (63, [7, 14, 28, 9, 18, 36]),
                 (65, [1, 2, 4, 8, 16, 32]),
                 (85, [5, 10, 20, 40, 17, 34])]
    result = []
    for n, bases in templates:
        invariant = []
        bounded_multiplicity = 0
        for mask in range(64):
            c = [(-x if mask >> i & 1 else x) % n for i, x in enumerate(bases)]
            assert len(set(c + [(-x) % n for x in c])) == 12
            points = [0, 0] + c
            counts = [0] * n
            for i in range(8):
                for j in range(8):
                    if i != j:
                        counts[(points[i] - points[j]) % n] += 1
            bounded_multiplicity += all(k <= 3 for k in counts[1:])
            closed = all(counts[d] == counts[2 * d % n] for d in range(n))
            anti = [0] * n
            for x in c:
                anti[x] = 1
                anti[-x % n] = -1
            square = convolution(anti, anti)
            assert closed == all(square[d] == square[2 * d % n] for d in range(n))
            if closed:
                invariant.append(mask)
        result.append({"quotient_order": n, "bases": bases, "orientations_examined": 64,
                       "multiplicity_at_most_three": bounded_multiplicity,
                       "doubling_invariant_masks": invariant})
    assert result[0]["doubling_invariant_masks"] == [0, 21, 42, 63]
    assert all(not r["doubling_invariant_masks"] for r in result[1:])
    return result


def trim(a):
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def divide(a, b):
    a = a[:]
    assert b[-1] == 1
    q = [0] * max(1, len(a) - len(b) + 1)
    for k in range(len(a) - len(b), -1, -1):
        coefficient = a[k + len(b) - 1]
        q[k] = coefficient
        for j, v in enumerate(b):
            a[k + j] -= coefficient * v
    return trim(q), trim(a)


@lru_cache(None)
def cyclotomic(n):
    a = [-1] + [0] * (n - 1) + [1]
    for d in range(1, n):
        if n % d == 0:
            a, remainder = divide(a, list(cyclotomic(d)))
            assert remainder == [0]
    return tuple(a)


def power_vector(n, exponent):
    exponent %= n
    _, remainder = divide([0] * exponent + [1], list(cyclotomic(n)))
    degree = len(cyclotomic(n)) - 1
    return remainder + [0] * (degree - len(remainder))


def rank(vectors):
    a = [list(map(Fraction, v)) for v in vectors]
    r = 0
    for column in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][column]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        value = a[r][column]
        a[r] = [x / value for x in a[r]]
        for i in range(r + 1, len(a)):
            value = a[i][column]
            if value:
                a[i] = [x - value * y for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def cyclotomic_checks():
    unit65 = [i for i in range(65) if gcd(i, 65) == 1]
    support63 = sorted({s * 2 ** i % 63 for s in (-1, 1) for i in range(6)})
    assert len(support63) == len({x % 21 for x in support63}) == 12
    rank65 = rank([power_vector(65, i) for i in unit65])
    rank63 = rank([power_vector(63, i) for i in support63])
    assert rank65 == 48 and rank63 == 12
    relations = []
    for a in range(21):
        if gcd(a, 21) != 1:
            continue
        vectors = [power_vector(63, a + 21 * i) for i in range(3)]
        assert all(sum(v[j] for v in vectors) == 0 for j in range(36))
        relations.append([a, a + 21, a + 42])
    assert len(relations) == 12
    unit63 = [i for i in range(63) if gcd(i, 63) == 1]
    assert rank([power_vector(63, i) for i in unit63]) == 24
    return {"unit_65_conjugates": 48, "unit_65_rank": rank65,
            "unit_63_support": support63, "unit_63_support_rank": rank63,
            "full_unit_63_rank": 24, "unit_63_relations": relations,
            "method": "Exact reduction modulo recursively computed cyclotomic polynomials."}


def fixtures():
    data = [((0, 1, 3, 7, 15, 31, 63, 127), 255),
            ((0, 9487369, 18974739, 18974742, 33, 1089, 35937, 1185921), 28462107),
            ((0, 1, 17, 289, 4913, 4911, 4879, 4335), 39305)]
    answer = []
    for a, n in data:
        hits = [u for u in combinations_with_replacement(range(8), 8)
                if sum(a[i] for i in u) % n == sum(a) % n]
        assert hits == [tuple(range(8))]
        delta = {(x - y) % n for x in a for y in a if x != y}
        assert len(delta) == 56
        order3 = [d for d in sorted(delta) if n // gcd(n, d) == 3]
        cubes = defaultdict(list)
        for center in a:
            for singleton in a:
                cubes[(2 * center + singleton) % n].append((center, singleton))
        h = sum(2 * d % n not in delta for d in delta) // 2
        r3 = sum((len(f) - 1) * (len(f) - 2) // 2 for f in cubes.values())
        for f in cubes.values():
            centers, labels = {x for x, _ in f}, {y for _, y in f}
            pure = {x for x, y in f if x == y}
            assert len(centers) == len(labels) == len(f)
            assert centers & labels == pure
            if h == 0:
                assert len(pure) <= 1 and len(f) <= 4 and not order3
        answer.append({"N": n, "A": a, "multisets_checked": 6435,
                       "h": h, "R3": r3, "order_three_differences": order3,
                       "maximum_cubic_fiber": max(map(len, cubes.values())),
                       "multiway_fibers": [{"value": y, "representations": f}
                                           for y, f in cubes.items() if len(f) >= 3]})
    assert (answer[2]["h"], answer[2]["R3"], answer[2]["maximum_cubic_fiber"]) == (22, 3, 4)
    return answer


def main():
    result = {"six_point_cycle_arithmetic": cycle_orders(),
              "five_fixed_quotient_orbit_structures": quotient_structures(),
              "256_quotient_orientations": orientation_checks(),
              "exact_cyclotomic_checks": cyclotomic_checks(),
              "three_fixed_valid_fixtures": fixtures(),
              "scope": "Arithmetic bookkeeping and fixed controls; the theorem has an algebraic proof."}
    Path("stage9_cubic_torsion_results.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(json.dumps({"cycle_partitions": 11,
                      "signed_partition_records": result["six_point_cycle_arithmetic"]["signed_partition_records"],
                      "possible_orders": [189, 195, 255, 279, 315],
                      "orientation_checks": result["256_quotient_orientations"],
                      "cyclotomic_ranks": [48, 12, 24],
                      "valid_fixture_summaries": [{k: v for k, v in r.items() if k != "A"}
                                                  for r in result["three_fixed_valid_fixtures"]]}, indent=2))


if __name__ == "__main__":
    main()
