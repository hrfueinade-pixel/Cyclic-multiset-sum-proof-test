"""Small direct kernel audits and a star-template positive control."""

from collections import Counter, defaultdict
from itertools import combinations, combinations_with_replacement, permutations, product
from math import gcd, isqrt, prod
import json
from pathlib import Path
from time import monotonic

from stage6_path_quotients import cyclic_images, divisors, primitive_key, valid_with_witness
from stage6_tree_templates import determinant, relation_matrix


def audit_small_kernels():
    matrices = [
        [[3, 0], [0, 5]],
        [[3, 0], [0, 3]],
        [[9, 3], [0, 9]],
        [[5, 2], [2, 3]],
        [[1, 2, 0], [0, 3, 3], [2, 0, 5]],
        [[3, 3, 0], [0, 3, 3], [0, 0, 3]],
    ]
    checked_vectors = 0
    records = []
    for matrix in matrices:
        expected = set()
        for n in divisors(abs(determinant(matrix))):
            if n < 2:
                continue
            for b in product(range(n), repeat=len(matrix)):
                checked_vectors += 1
                if gcd(n, *b) != 1:
                    continue
                if all(sum(x * y for x, y in zip(row, b)) % n == 0 for row in matrix):
                    expected.add((n, primitive_key(b, n)))
        generated = {(n, primitive_key(a[1:], n))
                     for n, a in cyclic_images(matrix, verify=True, minimum_order=2)}
        assert generated == expected, (matrix, expected, generated)
        records.append({"matrix": matrix, "unit_orbits": len(expected),
                        "group_orders": sorted({n for n, _ in expected})})
    return {"integer_vectors_checked": checked_vectors, "matrices": records}


def prime_certificate():
    p = 15790321
    factors = (3, 5, 17, 29, 43, 113, 127)
    for q in factors + (7, 13, 241):
        assert all(q % d for d in range(2, isqrt(q) + 1))
    f = 3 * 7 * 13 * 241
    assert f * f > p and (p - 1) % f == 0
    assert prod(factors) * p == 2 ** 56 - 1
    assert pow(3, p - 1, p) == 1
    residues = {q: pow(3, (p - 1) // q, p) for q in (3, 7, 13, 241)}
    assert all(gcd(value - 1, p) == 1 for value in residues.values())
    return {"P": p, "F": f, "base": 3, "modular_residues": residues,
            "factorization_verified": True}


def overlap_check():
    n = 31
    candidates = sidon = pairs = 0
    groups = defaultdict(list)
    for tail in combinations(range(2, n), 3):
        candidates += 1
        a = (0, 1) + tail
        if len({(x + y) % n for x, y in combinations_with_replacement(a, 2)}) != 15:
            continue
        sidon += 1
        signature = tuple(sorted((x - y) % n for x in a for y in a if x != y))
        assert len(set(signature)) == 20
        groups[signature].append(frozenset(a))
    histogram = Counter()
    for fiber in groups.values():
        for x, y in combinations(fiber, 2):
            pairs += 1
            common = len(x.intersection(y))
            histogram[common] += 1
            assert common < 4
    return {"N": n, "set_size": 5, "normalization": "contains 0,1",
            "candidate_sets": candidates, "sidon_sets": sidon,
            "homometric_pairs": pairs, "overlap_histogram": dict(histogram),
            "scope": "One fixed modulus; no global computational claim."}


def star_control():
    start = monotonic()
    limit = 12
    counts = Counter()
    seen = set()
    valid = []
    invalid = []
    complete = True
    edges = [(i, 1) for i in range(8) if i != 1]
    for labels in permutations(range(1, 8)):
        if monotonic() - start > limit:
            complete = False
            break
        counts["label_permutations"] += 1
        if any(label == source for (source, _), label in zip(edges, labels)):
            continue
        counts["admissible_templates"] += 1
        matrix = relation_matrix(edges, labels)
        for n, a in cyclic_images(matrix, verify=True):
            counts["quotient_maps"] += 1
            if len(set(a)) != 8:
                continue
            key = n, tuple(sorted(a))
            if key in seen:
                continue
            seen.add(key)
            pairs = {(x + y) % n for x, y in combinations_with_replacement(a, 2)}
            if len(pairs) != 36:
                continue
            delta = {(x - y) % n for x in a for y in a if x != y}
            assert len(delta) == 56 and {2 * d % n for d in delta} == delta
            counts["sidon_h0_outputs"] += 1
            accepted, rival = valid_with_witness(a, n)
            record = {"N": n, "A": a}
            if accepted:
                counts["valid_h0_outputs"] += 1
                valid.append(record)
            else:
                counts["invalid_h0_outputs"] += 1
                if len(invalid) < 3:
                    invalid.append({**record, "rival": rival})
    assert valid and all(r["N"] == 255 for r in valid)
    return {"seconds_limit": limit, "elapsed_seconds": monotonic() - start,
            "complete_template_family": complete, "counts": dict(counts),
            "valid_examples": valid[:3], "invalid_examples": invalid}


def main():
    result = {"direct_kernel_audit": audit_small_kernels(),
              "prime_certificate": prime_certificate(),
              "one_point_overlap_check": overlap_check(),
              "star_control": star_control()}
    Path("stage6_presentation_audit.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
