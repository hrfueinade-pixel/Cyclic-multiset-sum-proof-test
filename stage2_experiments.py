"""Targeted structural checks; no search over ranges of moduli."""

from collections import Counter
from itertools import combinations, combinations_with_replacement
from math import comb

from research_experiments import collision, cube


def repeated_sumset(a, modulus, degree):
    tail = {sum(t) % modulus for t in combinations_with_replacement(a, degree - 2)}
    return {(2 * x + y) % modulus for x in a for y in tail}


def structure(a, modulus, base):
    normalized = tuple((x - base) % modulus for x in a)
    b = tuple(x for x in normalized if x)
    sums = cube(b, modulus)
    assert sums is not None
    m = len(b)
    n = m + 1
    total = sum(b) % modulus
    doubled = {2 * x % modulus for x in normalized}
    antipodal = n - len(doubled)
    assert antipodal in (0, 1)
    diff_counts = Counter((x - y) % modulus for x in normalized for y in normalized if x != y)
    for delta, count in diff_counts.items():
        assert count <= (2 if modulus % 2 == 0 and delta == modulus // 2 else 1)
    quarter = sum((u - v) % modulus == modulus // 2 for u, v in combinations(sorted(doubled), 2)) if modulus % 2 == 0 else 0
    assert quarter <= 1
    if modulus % 4 != 0:
        assert quarter == 0

    exterior = {}
    sumsets = {}
    for degree in (2, 3, 4):
        repeated = repeated_sumset(normalized, modulus, degree)
        low = {value for value, indices in sums.items() if len(indices) <= degree - 2}
        assert repeated & sums.keys() == low
        exterior[degree] = repeated - low
        sumsets[degree] = repeated
    for j in (2, 3, 4):
        for k in (2, 3, 4):
            if j + k <= n:
                reflected = {(total - x) % modulus for x in exterior[k]}
                assert exterior[j].isdisjoint(reflected)
                assert modulus >= len(sums) + len(exterior[j]) + len(exterior[k])

    r = len(doubled)
    triple_lower = n * r - comb(r, 2) - (2 * antipodal - 1) * quarter
    assert len(sumsets[3]) >= triple_lower
    assert len(exterior[3]) >= comb(n, 2) - antipodal - (2 * antipodal - 1) * quarter

    if n >= 4:
        d = exterior[2]
        reflected = {(total - x) % modulus for x in d}
        assert d.isdisjoint(reflected)
        if modulus % 2 == 0 and total % 2 == 0 and any(x % 2 for x in b):
            assert modulus >= len(sums) + 4 * len(d)

    if modulus % 2 == 0 and not antipodal:
        even_count = sum(x % 2 == 0 for x in normalized)
        odd_count = n - even_count
        assert len(exterior[3]) >= 2 * even_count * odd_count

    if n >= 7:
        assert modulus >= len(sums) + n * (n - 1)
        if n % 4 == 3:
            assert modulus >= len(sums) + n * (n - 1) + 1
    if n == 8:
        assert modulus >= 187
        if antipodal:
            assert modulus >= 218
    if n == 7:
        assert modulus >= 109

    if antipodal:
        projected = tuple(sorted({x % (modulus // 2) for x in normalized}))
        assert len(projected) == n - 1
        assert collision(projected, modulus // 2) is None

    return {"n": n, "N": modulus, "base": base, "s_parity": total % 2,
            "antipodal": antipodal, "quarter": quarter,
            "E2": len(exterior[2]), "E3": len(exterior[3]), "E4": len(exterior[4]),
            "triple_count_lower": triple_lower, "triple_count_actual": len(sumsets[3])}


def main():
    cases = []
    for n in range(4, 10):
        a = tuple((1 << i) - 1 for i in range(n))
        cases.append((a, (1 << n) - (1 << (n.bit_length() - 1))))
        cases.append((a, (1 << n) - 1))
        cases.append((a, 1 << n))
    cases.extend((((0, 1, 3, 10), 15), ((0, 1, 4, 6), 15), ((0, 2, 6, 14), 24)))
    cases.extend((((0, 1, 3, 7, 15), 30), ((0, 1, 3, 7, 15, 31), 62),
                  ((0, 1, 3, 7, 15, 31, 63, 127), 254)))
    cases.extend((((0, 1, 3, 7), 18), ((0, 1, 3, 7, 15), 82),
                  ((0, 1, 3, 7, 15, 31), 190),
                  ((0, 1, 3, 7, 15, 31, 63, 127), 1022)))
    checked_bases = 0
    known_quartic_failures = []
    for a, modulus in cases:
        assert collision(a, modulus) is None
        first = None
        for base in a:
            result = structure(a, modulus, base)
            checked_bases += 1
            proposed = comb(len(a), 3) + len(a) - 1 - 3 * result["antipodal"]
            if result["E4"] < proposed:
                known_quartic_failures.append({"A": a, "N": modulus, "base": base,
                                              "E4": result["E4"], "proposed": proposed})
            if first is None:
                first = result
        print(first)
    print({"valid_cases": len(cases), "translated_bases_checked": checked_bases,
           "unproved_quartic_hypothesis_failures": known_quartic_failures})

    print("Targeted perturbations; these only test the unproved quartic hypothesis:")
    tested = 0
    valid = 0
    quartic_failures = []
    candidates = []
    for modulus in (31, 37):
        for top in range(8, modulus):
            candidates.append(((0, 1, 3, 7, top), modulus))
    for modulus in (255, 257):
        for x in (63, 64, 65, 66, 67):
            for y in (127, 128, 129, 130, 131):
                candidates.append(((0, 1, 3, 7, 15, 31, x, y), modulus))
    for a, modulus in candidates:
        tested += 1
        if collision(a, modulus) is not None:
            continue
        valid += 1
        result = structure(a, modulus, a[0])
        proposed = comb(len(a), 3) + len(a) - 1 - 3 * result["antipodal"]
        if result["E4"] < proposed:
            quartic_failures.append({"A": a, "N": modulus, "E4": result["E4"],
                                     "proposed": proposed})
    print({"candidates_tested": tested, "valid": valid,
           "quartic_hypothesis_counterexamples": quartic_failures,
           "quartic_hypothesis_proved": False})

    print("Odd equality obstruction at N=185 (arithmetic, no set search):")
    unseen = set(range(1, 185))
    orbits = []
    while unseen:
        start = min(unseen)
        orbit = []
        value = start
        while value not in orbit:
            orbit.append(value)
            value = 2 * value % 185
        assert value == start
        unseen.difference_update(orbit)
        orbits.append(orbit)
    lengths = Counter(map(len, orbits))
    assert lengths == {4: 1, 36: 5}
    assert all(36 * a + 4 * b != 56 for a in range(6) for b in range(2))
    print({"doubling_orbit_lengths": dict(lengths),
           "invariant_56_element_nonzero_set_possible": False})
    for modulus, expected in ((107, 106), (27, 18)):
        value = 2 % modulus
        order = 1
        while value != 1:
            value = 2 * value % modulus
            order += 1
            assert order <= modulus
        assert order == expected
        print({"modulus": modulus, "multiplicative_order_of_2": order})

    print("Counterexamples to unconditional cubic exteriority:")
    for a, modulus, terms in (((0, 1, 3, 7), 12, (1, 1, 1)),
                              ((0, 1, 3, 7), 12, (3, 3, 1)),
                              ((0, 1, 3, 10), 15, (10, 10, 10))):
        sums = cube(a[1:], modulus)
        value = sum(terms) % modulus
        assert value in sums
        print({"A": a, "N": modulus, "terms": terms, "value": value,
               "subset_indices": sums[value]})

    print("Quartic collision despite disjoint marked supports:")
    a = (0, 1, 3, 7, 15, 31, 63, 127)
    sums = cube(a[1:], 248)
    left = (1, 1, 3, 63)
    right = (15, 15, 31, 7)
    assert sum(left) == sum(right) == 68
    assert 68 not in sums
    assert set(left).isdisjoint(right)
    print({"N": 248, "left": left, "right": right, "value": 68, "outside_S": True})

    print("Three antipodal reductions in the known n=8 construction:")
    modulus = 248
    reduced = a
    chain = []
    for _ in range(3):
        assert len({2 * x % modulus for x in reduced}) == len(reduced) - 1
        reduced = tuple(sorted({x % (modulus // 2) for x in reduced}))
        modulus //= 2
        assert collision(reduced, modulus) is None
        chain.append({"n": len(reduced), "N": modulus})
    assert len(reduced) == 5 and modulus == 31
    print(chain)


if __name__ == "__main__":
    main()
