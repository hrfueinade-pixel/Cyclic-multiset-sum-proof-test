"""Targeted tests of coexistence lemmas, with fixed finite template ranges.

This is not an exhaustive search over valid cyclic sets or over moduli.
Triangle-pendant templates fix p=1 and bound q,r; this is a restriction,
not an asserted symmetry reduction. All accepted sets are independently
checked by full eight-term multiset enumeration.
"""

from collections import Counter, defaultdict
from itertools import combinations, combinations_with_replacement
from math import gcd
from time import monotonic

from research_experiments import collision, cube


def pair_antipodes(a, modulus):
    pairs = {sum(pair) % modulus: pair
             for pair in combinations_with_replacement(a, 2)}
    assert len(pairs) == 36
    if modulus % 2:
        return []
    t = modulus // 2
    return [(pairs[x], pairs[(x + t) % modulus]) for x in pairs
            if (x + t) % modulus in pairs and x < (x + t) % modulus]


def fiber_data(a, modulus):
    triples = defaultdict(list)
    ordinary = defaultdict(list)
    for center in a:
        for singleton in a:
            triples[(2 * center + singleton) % modulus].append((center, singleton))
        for tail in combinations([x for x in a if x != center], 2):
            ordinary[(2 * center + sum(tail)) % modulus].append((center, tail))
    return triples, ordinary


def audit(a, modulus):
    assert len(a) == len(set(a)) == 8
    assert collision(a, modulus) is None
    assert len({2 * x % modulus for x in a}) == 8
    differences = Counter((x - y) % modulus for x in a for y in a if x != y)
    assert all(count == 1 for count in differences.values())
    antipodes = pair_antipodes(a, modulus)
    assert len(antipodes) <= 7
    kinds = Counter((left[0] == left[1], right[0] == right[1])
                    for left, right in antipodes)
    sf_sf = sum(left[0] != left[1] and right[0] != right[1]
                for left, right in antipodes)
    assert sf_sf <= 1
    triples, ordinary = fiber_data(a, modulus)
    lifts = defaultdict(list)
    cycle_values = []
    for value, reps in ordinary.items():
        assert len(reps) <= 4
        if len(reps) < 4:
            continue
        centers = {center for center, _ in reps}
        tails = [tail for _, tail in reps]
        assert centers.isdisjoint({x for tail in tails for x in tail})
        degree = Counter(x for tail in tails for x in tail)
        if set(degree.values()) == {2}:
            assert modulus % 2 == 0 and sf_sf == 1
            cycle_values.append(value)
        else:
            assert sorted(degree.values()) == [1, 2, 2, 3]
            hub = next(x for x, count in degree.items() if count == 3)
            triple_value = (value - hub) % modulus
            assert len(triples[triple_value]) >= 3
            if modulus % 2:
                assert len(triples[triple_value]) == 3
                assert all(center != tail for center, tail in triples[triple_value])
            lifts[triple_value].append(value)
    if modulus % 2:
        assert all(len(values) == 1 for values in lifts.values())
    return {"N": modulus, "A": a, "pair_antipodes": antipodes,
            "pair_antipode_kinds": dict(kinds),
            "triple_histogram": dict(sorted(Counter(map(len, triples.values())).items())),
            "ordinary_histogram": dict(sorted(Counter(map(len, ordinary.values())).items())),
            "triangle_pendant_lifts": dict(lifts), "cycle_values": cycle_values}


def main():
    binary = tuple((1 << i) - 1 for i in range(8))
    references = [(binary, 255), (binary, 256), (binary, 1022)]
    b = 19
    reference = tuple(sorted((0, 2, 2*b, 2*b*b,
                              b**3-1, b**3-b, b**3-1-b, b**3-b-b*b)))
    references.append((reference, 8 * max(reference) + 1))
    references.append((tuple(sorted(((-3)**i - 1)//4 % 1640 for i in range(8))), 1640))
    references.append(((0, 1, 33, 1089, 20034, 37822, 39934, 39998), 40000))
    print("Audited reference configurations:")
    for a, modulus in references:
        print(audit(a, modulus))

    print("Fixed triangle-pendant relation-template tests:")
    for modulus in (239, 247, 255):
        start = monotonic()
        tested = distinct_sets = sidon = cube_passing = 0
        valid = []
        seen = set()
        timed_out = False
        # Exactly 105*(modulus) parameter tuples unless the 20-second cap fires.
        for q in range(2, 9):
            for r in range(q + 1, 21):
                for h in range(modulus):
                    if monotonic() - start > 20:
                        timed_out = True
                        break
                    tested += 1
                    p = 1
                    a = tuple(sorted(x % modulus for x in
                                     (0, 2*p, 2*q, 2*r, h-p, h-q, h-p-q, h-r)))
                    if len(set(a)) != 8 or a in seen:
                        continue
                    seen.add(a)
                    distinct_sets += 1
                    differences = [(x-y) % modulus for x in a for y in a if x != y]
                    if len(set(differences)) != 56:
                        continue
                    sidon += 1
                    if cube(a[1:], modulus) is None:
                        continue
                    cube_passing += 1
                    if collision(a, modulus) is None:
                        result = audit(a, modulus)
                        assert (2*h) % modulus in result["triangle_pendant_lifts"].get((2*h) % modulus, [])
                        valid.append(result)
                if timed_out:
                    break
            if timed_out:
                break
        print({"N": modulus, "parameter_tuples": tested,
               "planned_parameter_tuples": 105 * modulus,
               "distinct_eight_element_sets": distinct_sets, "Sidon_sets": sidon,
               "cube_passing_sets": cube_passing, "valid_sets": len(valid),
               "time_seconds": round(monotonic() - start, 3),
               "template_complete": not timed_out, "search_globally_complete": False,
               "accepted": valid})

    print("Full non-type22 fiber determinant arithmetic:")
    determinant_cases = full_fiber_determinants()
    print(determinant_cases)
    print("Focused orbit completion tests for remaining full-fiber cases:")
    for modulus, ordinary_count, include_zero in ((189, 2, False), (189, 1, True), (243, 2, False)):
        print(full_fiber_orbits(modulus, ordinary_count, include_zero))
    print("Even full non-type22 fiber configuration enumeration:")
    print(even_full_fiber_search())


def partitions(total, minimum=1):
    if total == 0:
        yield ()
    for first in range(minimum, total + 1):
        for rest in partitions(total - first, first):
            yield (first,) + rest


def full_fiber_determinants():
    cases = []
    for ordinary_count in range(5):
        k = 8 - ordinary_count
        for cycle_count in range(1, k + 1):
            for cycles in partitions(cycle_count):
                if 2 in cycles or cycles.count(1) > 1:
                    continue
                tree_vertices = k - cycle_count
                determinant = (2 ** ordinary_count) * (3 ** tree_vertices)
                for length in cycles:
                    determinant *= 3 ** length - (-1) ** length
                assert determinant % 4 == 0
                reduced = determinant // 4
                moduli = [n for n in range(187, 248, 2) if reduced % n == 0]
                if moduli:
                    cases.append({"q": ordinary_count, "cycles": cycles, "trees": tree_vertices,
                                  "detM_over4": reduced, "odd_subthreshold_divisors": moduli})
    return cases


def full_fiber_orbits(modulus, ordinary_count, include_zero):
    inverse_two = pow(2, -1, modulus)
    nonordinary_sets = set()
    three_cycles = set()
    for start in range(modulus):
        if (-3) ** 3 * start % modulus == start and -3 * start % modulus != start:
            three_cycles.add(tuple(sorted({start, -3 * start % modulus, 9 * start % modulus})))
    for start in range(modulus):
        orbit = set()
        value = start
        while value not in orbit:
            orbit.add(value)
            value = -3 * value % modulus
        if include_zero:
            # A path may feed the zero loop or the three-cycle; include both.
            for cycle in three_cycles:
                expanded = orbit | set(cycle) | {0}
                if len(expanded) == 8 - ordinary_count:
                    nonordinary_sets.add(tuple(sorted(expanded)))
        elif len(orbit) == 8 - ordinary_count:
            nonordinary_sets.add(tuple(sorted(orbit)))
    tested = sidon = cube_passing = 0
    valid = []
    candidate_witnesses = Counter()
    for d in sorted(nonordinary_sets):
        possible_centers = sorted({-sum(tail) * inverse_two % modulus
                                   for tail in combinations(d, 2)} - set(d))
        for centers in combinations(possible_centers, ordinary_count):
            tested += 1
            a = tuple(sorted(d + centers))
            differences = [(x-y) % modulus for x in a for y in a if x != y]
            if len(set(differences)) != 56:
                candidate_witnesses["nonunique_difference"] += 1
                continue
            sidon += 1
            base = a[0]
            normalized = tuple((x-base) % modulus for x in a if x != base)
            if cube(normalized, modulus) is None:
                candidate_witnesses["subset_collision"] += 1
                continue
            cube_passing += 1
            rival = collision(a, modulus)
            if rival is not None:
                candidate_witnesses["eight_term_rival"] += 1
                continue
            result = audit(a, modulus)
            non22 = sum(1 for center in a
                        for tail in combinations_with_replacement(a, 2)
                        if not (tail[0] == tail[1] and tail[0] != center)
                        and (2 * center + sum(tail)) % modulus == 0)
            assert non22 == 8
            valid.append(result)
    return {"N": modulus, "q": ordinary_count, "include_zero": include_zero,
            "nonordinary_orbit_sets": len(nonordinary_sets), "candidate_completions": tested,
            "Sidon_completions": sidon, "cube_passing_completions": cube_passing,
            "valid_completions": len(valid), "rejection_counts": dict(candidate_witnesses),
            "accepted": valid, "scope_complete": True,
            "scope": "only the specified full non-type22 fiber orbit configuration"}


def affine_closed_sets(modulus, value):
    cycles, path_orbits = set(), set()
    for start in range(modulus):
        orbit = []
        current = start
        while current not in orbit:
            orbit.append(current)
            current = (value - 3 * current) % modulus
        position = orbit.index(current)
        cycle = frozenset(orbit[position:])
        if len(cycle) == 2 or len(cycle) > 8:
            continue
        cycles.add(cycle)
        if position and len(orbit) <= 8:
            path_orbits.add(frozenset(orbit))
    cycle_unions = {frozenset()}
    for cycle in sorted(cycles, key=lambda c: (len(c), sorted(c))):
        cycle_unions |= {u | cycle for u in tuple(cycle_unions) if len(u | cycle) <= 8}
    closed = {u for u in cycle_unions if 4 <= len(u) <= 8}
    for orbit in path_orbits:
        closed |= {u | orbit for u in cycle_unions if 4 <= len(u | orbit) <= 8}
    return closed


def even_full_fiber_search():
    # These ten moduli are derived from the determinant necessary condition.
    moduli = (192, 196, 200, 208, 210, 216, 224, 234, 240, 244)
    start = monotonic()
    records = []
    accepted = []
    for modulus in moduli:
        record = {"N": modulus, "value_classes": gcd(4, modulus), "closed_sets": 0,
                  "Sidon_nonordinary_sets": 0, "determinant_passing": 0,
                  "completions": 0, "Sidon_completions": 0, "cube_passing": 0,
                  "valid": 0}
        for value in range(gcd(4, modulus)):
            for d in sorted(affine_closed_sets(modulus, value), key=lambda d: (len(d), sorted(d))):
                if monotonic() - start > 30:
                    return {"complete": False, "time_seconds": round(monotonic()-start, 3),
                            "completed_records": records, "partial_record": record,
                            "accepted": accepted, "unfinished": {"N": modulus, "value": value}}
                record["closed_sets"] += 1
                q = 8 - len(d)
                if sum((value - 3*x) % modulus == x for x in d) > 2:
                    continue
                differences = [(x-y) % modulus for x in d for y in d if x != y]
                if len(set(differences)) != len(differences):
                    continue
                record["Sidon_nonordinary_sets"] += 1
                # Computing cycle factors from the actual functional graph.
                cycles = set()
                for vertex in d:
                    path = []
                    current = vertex
                    while current not in path:
                        path.append(current)
                        current = (value - 3*current) % modulus
                    cycles.add(frozenset(path[path.index(current):]))
                trees = len(d) - sum(map(len, cycles))
                determinant = 2 ** q * 3 ** trees
                for cycle in cycles:
                    determinant *= 3 ** len(cycle) - (-1) ** len(cycle)
                assert determinant % 4 == 0
                if (determinant // 4) % modulus:
                    continue
                record["determinant_passing"] += 1
                possible_centers = set()
                for tail in combinations(sorted(d), 2):
                    remainder = (value - sum(tail)) % modulus
                    if remainder % 2 == 0:
                        possible_centers.update((remainder // 2, remainder // 2 + modulus // 2))
                possible_centers -= d
                for centers in combinations(sorted(possible_centers), q):
                    record["completions"] += 1
                    a = tuple(sorted(set(d) | set(centers)))
                    assert len(a) == 8
                    differences = [(x-y) % modulus for x in a for y in a if x != y]
                    if len(set(differences)) != 56:
                        continue
                    record["Sidon_completions"] += 1
                    base = a[0]
                    if cube(tuple((x-base) % modulus for x in a if x != base), modulus) is None:
                        continue
                    record["cube_passing"] += 1
                    if collision(a, modulus) is None:
                        record["valid"] += 1
                        accepted.append({"N": modulus, "value": value, "A": a})
        records.append(record)
    return {"complete": True, "time_seconds": round(monotonic()-start, 3),
            "records": records, "accepted": accepted,
            "scope": "full non-type22 fibers only; no unrestricted valid-set search"}


if __name__ == "__main__":
    main()
