"""Bounded, reproducible n=8 collision audit. No exhaustive modulus search.

Run with Python 3. Uses only the standard library and the two earlier scripts.
The generator uses fixed seeds and fixed candidate counts, with no early stop.
"""

from collections import Counter, defaultdict
from itertools import combinations, combinations_with_replacement, product
from math import gcd
from random import Random

from research_experiments import collision, cube
from stage2_experiments import repeated_sumset


def independent_valid(a, modulus):
    # Coefficient of the target in the degree-eight complete homogeneous sum.
    dp = [[0] * modulus for _ in range(9)]
    dp[0][0] = 1
    for value in a:
        for degree in range(1, 9):
            previous, current = dp[degree - 1], dp[degree]
            for residue, count in enumerate(previous):
                if count:
                    target = (residue + value) % modulus
                    current[target] = min(2, current[target] + count)
    return dp[8][sum(a) % modulus] == 1


def affine_key(a, modulus):
    return min(tuple(sorted(u * (x - base) % modulus for x in a))
               for u in range(1, modulus) if gcd(u, modulus) == 1 for base in a)


def analyze(a, modulus):
    assert len(a) == len(set(a)) == 8
    assert collision(a, modulus) is None
    assert independent_valid(a, modulus)
    p = 8 - len({2 * x % modulus for x in a})
    counts = Counter((x - y) % modulus for x in a for y in a if x != y)
    assert all(v <= (2 if modulus % 2 == 0 and k == modulus // 2 else 1)
               for k, v in counts.items())
    results = []
    ordinary_max = 0
    overlap_example = None
    all_fibers = defaultdict(list)
    for indices in combinations_with_replacement(range(8), 4):
        vector = tuple(indices.count(i) for i in range(8))
        if max(vector) < 2:
            continue
        all_fibers[sum(a[i] for i in indices) % modulus].append(vector)
    for value, vectors in all_fibers.items():
        ordinary = [v for v in vectors if sorted(c for c in v if c) == [1, 1, 2]]
        if not p:
            assert len(ordinary) <= 4
        ordinary_max = max(ordinary_max, len(ordinary))
        for u, v in combinations(vectors, 2):
            diff = [x - y for x, y in zip(u, v)]
            assert max(diff) >= 2 and min(diff) <= -2
            shared = [a[i] for i in range(8) if u[i] and v[i]]
            if shared and overlap_example is None:
                overlap_example = {"value": value, "u": u, "v": v, "shared": shared}
    marked = defaultdict(list)
    for i in range(8):
        for j, k in combinations_with_replacement(range(8), 2):
            marked[(2 * a[i] + a[j] + a[k]) % modulus].append((i, j, k))
    if not p:
        assert max(map(len, marked.values())) <= 8
        assert len(marked) >= 57  # E3 is contained in E4 and has at least 28 points.
    for base in a:
        normalized = tuple((x - base) % modulus for x in a)
        b = tuple(x for x in normalized if x)
        sums = cube(b, modulus)
        assert sums is not None and len(sums) == 128
        low = {value for value, indices in sums.items() if len(indices) <= 2}
        t4 = repeated_sumset(normalized, modulus, 4)
        assert t4 & sums.keys() == low
        assert len(low) == 29 and len(t4) == len(marked)
        exterior = t4 - low
        reflected = {(sum(b) - x) % modulus for x in exterior}
        assert t4.isdisjoint({(sum(b) - x) % modulus for x in t4})
        assert exterior.isdisjoint(sums) and exterior.isdisjoint(reflected)
        assert reflected.isdisjoint(sums)
        results.append(len(exterior))
        if base == a[0]:
            exterior_histogram = Counter(len(marked[(x + 4 * base) % modulus]) for x in exterior)
            low_marked_mass = sum(len(marked[(x + 4 * base) % modulus]) for x in low)
    assert len(set(results)) == 1
    sizes = Counter(map(len, marked.values()))
    excess = 288 - len(marked)
    pair_energy = sum(k * (k - 1) // 2 * v for k, v in sizes.items())
    assert excess == sum((k - 1) * v for k, v in sizes.items())
    if p:
        quotient = tuple(sorted({x % (modulus // 2) for x in a}))
        assert len(quotient) == 7 and collision(quotient, modulus // 2) is None
    return {"N": modulus, "A": a, "antipodal": p, "E4": results[0],
            "T4": len(marked), "marked_histogram": dict(sorted(sizes.items())),
            "exterior_marked_histogram_at_first_base": dict(sorted(exterior_histogram.items())),
            "low_marked_mass_at_first_base": low_marked_mass,
            "excess": excess, "pair_energy": pair_energy,
            "cauchy_lower_T4": (288 * 288 + 288 + 2 * pair_energy - 1) // (288 + 2 * pair_energy),
            "ordinary_max": ordinary_max, "overlap_example": overlap_example}


def main():
    binary = tuple((1 << i) - 1 for i in range(8))
    explicit_results = []
    print("Explicit reference cases:")
    for modulus in (248, 254, 255, 256, 1022):
        explicit_results.append(analyze(binary, modulus))
        print(explicit_results[-1])

    print("Two nonbinary constructions with proofs in the report:")
    b = 19
    four_fiber = tuple(sorted((0, 2, 2 * b, 2 * b * b, b**3 - 1,
                              b**3 - 1 - b, b**3 - b, b**3 - b - b * b)))
    explicit_results.append(analyze(four_fiber, 8 * max(four_fiber) + 1))
    print(explicit_results[-1])
    orbit = tuple(((-3)**i - 1) // 4 % 1640 for i in range(8))
    eight_fiber = tuple(sorted(orbit))
    explicit_results.append(analyze(eight_fiber, 1640))
    print(explicit_results[-1])
    assert all((3 * orbit[i] + orbit[(i + 1) % 8]) % 1640 == 1639 for i in range(8))
    assert sum((3 * x + y) % 1640 == 1639 for x in eight_fiber for y in eight_fiber) == 8
    for modulus in (248, 255):
        sums = cube(binary[1:], modulus)
        assert (2 * 1 + 3 + 63) % modulus == (2 * 15 + 31 + 7) % modulus == 68
        assert 68 not in sums
    assert (2 * 3 + 0 + 0) % 255 == (2 * 1 + 1 + 3) % 255 == 6
    assert 6 not in cube(binary[1:], 255)

    print("Audit the previous perturbations by dimension:")
    for n, moduli in ((5, (31, 37)), (8, (255, 257))):
        valid = []
        candidates = 0
        for modulus in moduli:
            rests = ((top,) for top in range(8, modulus)) if n == 5 else product(range(63, 68), range(127, 132))
            prefix = (0, 1, 3, 7) if n == 5 else (0, 1, 3, 7, 15, 31)
            for rest in rests:
                candidates += 1
                a = prefix + tuple(rest)
                if collision(a, modulus) is None:
                    valid.append({"N": modulus, "A": a})
        print({"n": n, "candidates": candidates, "valid": valid})

    batches = []
    for modulus in (239, 247, 255, 257, 509, 1021):
        rng = Random(20261008 + modulus)
        candidates = [tuple(sorted((0, 1, 3, 7, 15,
                                     31 + rng.randrange(-3, 4),
                                     63 + rng.randrange(-5, 6),
                                     127 + rng.randrange(-9, 10)))) for _ in range(64)]
        batches.append(("local", modulus, candidates))
    for modulus in (257, 509, 1021, 4093):
        rng = Random(20261009 + modulus)
        candidates = [tuple(sorted((0,) + tuple(rng.sample(range(1, modulus), 7))))
                      for _ in range(64)]
        batches.append(("random", modulus, candidates))

    failures_60, failures_63 = [], []
    audited = []
    for name, modulus, candidates in batches:
        survivors = [a for a in candidates if cube(a[1:], modulus) is not None]
        valid = sorted({a for a in survivors if collision(a, modulus) is None})
        keys = {affine_key(a, modulus) for a in valid}
        binary_key = affine_key(binary, modulus)
        analyses = [analyze(a, modulus) for a in valid]
        audited.extend(analyses)
        failures_60.extend(r for r in analyses if not r["antipodal"] and r["E4"] < 60)
        failures_63.extend(r for r in analyses if not r["antipodal"] and r["E4"] < 63)
        print({"batch": name, "N": modulus, "candidate_draws": len(candidates),
               "distinct_candidates": len(set(candidates)), "dissociated_draws": len(survivors),
               "distinct_valid": len(valid), "affine_classes": len(keys),
               "nonbinary_affine_classes": len(keys - {binary_key}),
               "E4_range": (min(r["E4"] for r in analyses), max(r["E4"] for r in analyses)) if analyses else None})
        for result in analyses[:2]:
            print(result)
    print({"total_candidate_draws": sum(len(c) for _, _, c in batches),
           "audited_distinct_pairs": len({(r["N"], r["A"]) for r in audited}),
           "all_distinct_valid_pairs": len({(r["N"], r["A"]) for r in audited + explicit_results}),
           "all_distinct_base_checks": 8 * len({(r["N"], r["A"]) for r in audited + explicit_results}),
           "tested_claim_60_failures": failures_60,
           "tested_stronger_63_failures": failures_63,
           "sampled_largest_ordinary_fiber": max((r["ordinary_max"] for r in audited), default=0),
           "sampled_largest_marked_fiber": max((max(r["marked_histogram"]) for r in audited), default=0),
           "complete_search": False, "bound_proved_by_tests": False})


if __name__ == "__main__":
    main()
