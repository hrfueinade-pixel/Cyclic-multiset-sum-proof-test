"""Bounded checks for the cyclic unique-multiset-sum problem.

No search over ranges of moduli. All candidates and budgets are explicit.
"""

from itertools import combinations, combinations_with_replacement
from math import gcd


def collision(a, modulus):
    target = sum(a) % modulus
    baseline = tuple(range(len(a)))
    for indices in combinations_with_replacement(range(len(a)), len(a)):
        if indices != baseline and sum(a[i] for i in indices) % modulus == target:
            return tuple(a[i] for i in indices)
    return None


def cube(b, modulus):
    sums = {0: ()}
    for i, value in enumerate(b):
        new = {(s + value) % modulus: t + (i,) for s, t in sums.items()}
        if sums.keys() & new.keys():
            return None
        sums.update(new)
    return sums


def inspect(a, modulus):
    witness = collision(a, modulus)
    b = tuple((x - a[0]) % modulus for x in a[1:])
    sums = cube(b, modulus)
    if witness is not None:
        return {"a": a, "N": modulus, "valid": False,
                "dissociated": sums is not None, "collision": witness}
    assert sums is not None
    doubled_classes = {}
    for x in a:
        doubled_classes.setdefault((2 * x) % modulus, []).append(x)
    assert len(doubled_classes) >= len(a) - 1
    exterior_doubles = {(2 * x) % modulus for x in b if (2 * x) % modulus}
    assert exterior_doubles.isdisjoint(sums)
    assert modulus >= len(sums) + len(doubled_classes) - 1
    if modulus % 2 == 0:
        if any(x % 2 for x in b):
            assert sum(x % 2 == 0 for x in sums) == len(sums) // 2
            assert modulus >= len(sums) + 2 * (len(doubled_classes) - 1)
        else:
            assert modulus >= 2 * len(sums)
        assert modulus >= len(sums) + 2 * len(a) - 4
    else:
        assert len(doubled_classes) == len(a)
        if modulus == len(sums) + len(a) - 1:
            coefficient = (1 << (len(a) - 2)) + 2
            assert gcd(modulus, coefficient) != 1
    minimum_overlap = min(len(sums.keys() & {(x + shift) % modulus for x in sums})
                          for shift in range(1, modulus))
    return {"a": a, "N": modulus, "valid": True,
            "cube_size": len(sums), "exterior_doubles": sorted(exterior_doubles),
            "min_translate_overlap": minimum_overlap}


def main():
    print("Explicit binary construction checks (n=2,...,9):")
    for n in range(2, 10):
        a = tuple((1 << i) - 1 for i in range(n))
        modulus = (1 << n) - (1 << (n.bit_length() - 1))
        print(inspect(a, modulus))

    print("Dissociation alone is insufficient:")
    print(inspect((0, 1, 2), 5))

    print("Explicit additional valid cases:")
    for a, modulus in (((0, 2, 6), 12), ((0, 1, 3, 7, 15), 31)):
        print(inspect(a, modulus))

    print("Counterexample to the small translate-overlap lemma:")
    sums = cube((1, 3, 7, 15), 28)
    overlaps = [len(sums.keys() & {(x + shift) % 28 for x in sums})
                for shift in range(1, 15)]
    print({"N": 28, "S": sorted(sums), "shifts_1_to_14": overlaps})
    assert min(overlaps) == 5

    print("Moment exclusions (pure integer arithmetic, no candidate search):")
    for n in (4, 6, 8, 10, 12):
        lower = (1 << (n - 1)) + n - 1
        coefficient = (1 << (n - 2)) + 2
        print({"n": n, "odd_equality_N": lower,
               "moment_coefficient": coefficient,
               "gcd": gcd(lower, coefficient),
               "excluded": gcd(lower, coefficient) == 1})

    print("Selected odd-modulus tests, at most 350 normalized sets per pair:")
    for n, modulus in ((3, 5), (3, 7), (4, 13), (4, 15), (5, 29), (5, 31)):
        tested = 0
        valid = []
        for rest in combinations(range(1, modulus), n - 1):
            if tested == 350:
                break
            tested += 1
            a = (0,) + rest
            if collision(a, modulus) is None:
                valid.append(a)
                if len(valid) == 3:
                    break
        print({"n": n, "N": modulus, "tested": tested, "valid_examples": valid})
        for a in valid:
            print(inspect(a, modulus))


if __name__ == "__main__":
    main()
