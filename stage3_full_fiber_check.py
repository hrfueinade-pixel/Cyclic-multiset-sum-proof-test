"""Independent finite arithmetic checks for odd full non-type22 fibers.

Does not import any earlier research or search modules. Canonical orbit
coverage is justified separately in stage3_audit_notes.md.
"""

from itertools import combinations, combinations_with_replacement
import json
from math import prod
from pathlib import Path


def determinants():
    rows = []
    for q in range(5):
        k = 8 - q
        for count in range(1, k + 1):
            for cycles in combinations_with_replacement(range(1, k + 1), count):
                used = sum(cycles)
                if used > k or 2 in cycles or cycles.count(1) > 1:
                    continue
                trees = k - used
                determinant = 2**q * 3**trees * prod(3**ell - (-1)**ell for ell in cycles)
                assert determinant % 4 == 0
                divisors = [n for n in range(187, 248, 2) if determinant // 4 % n == 0]
                if divisors:
                    rows.append({"q": q, "cycles": cycles, "trees": trees,
                                 "detM_over4": determinant // 4,
                                 "odd_subthreshold_divisors": divisors})
    return rows


def canonical_orbit(modulus):
    values = []
    x = 1
    while x not in values:
        values.append(x)
        x = -3 * x % modulus
    assert len(values) == 6
    return tuple(sorted(values))


def completion_check(modulus):
    h = canonical_orbit(modulus)
    inverse2 = (modulus + 1) // 2
    centers = sorted({-inverse2 * (d + e) % modulus for d, e in combinations(h, 2)} - set(h))
    rows = []
    sidon = cube = valid = 0
    for added in combinations(centers, 2):
        a = tuple(sorted(h + added))
        differences = [(x - y) % modulus for x in a for y in a if x != y]
        unique_differences = len(set(differences)) == 56
        normalized = tuple((x - a[0]) % modulus for x in a[1:])
        subsets = {sum(normalized[i] for i in range(7) if mask & (1 << i)) % modulus
                   for mask in range(128)}
        unique_subsets = len(subsets) == 128
        sidon += unique_differences
        cube += unique_differences and unique_subsets
        target = sum(a) % modulus
        hits = 0
        rival = None
        scanned = 0
        baseline = tuple(range(8))
        for indices in combinations_with_replacement(range(8), 8):
            scanned += 1
            if sum(a[i] for i in indices) % modulus == target:
                hits += 1
                if indices != baseline and rival is None:
                    rival = tuple(a[i] for i in indices)
        assert scanned == 6435
        valid += hits == 1
        assert hits > 1 and rival is not None
        rows.append({"centers": added, "unique_differences": unique_differences,
                     "unique_subsets": unique_subsets, "target_multisets": hits,
                     "first_rival": rival})
    return {"N": modulus, "canonical_nonordinary_points": h,
            "possible_ordinary_centers": centers, "candidate_completions": len(rows),
            "Sidon_completions": sidon, "Sidon_and_cube_completions": cube,
            "valid_completions": valid, "all_multisets_scanned": 6435 * len(rows),
            "candidate_records": rows}


def main():
    result = {"determinant_cases": determinants(),
              "canonical_completion_checks": [completion_check(189), completion_check(243)]}
    print(json.dumps(result, indent=2))
    Path("stage3_independent_full_fiber_result.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="ascii")


if __name__ == "__main__":
    main()
