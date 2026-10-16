"""Complete bounded quotient checks for the rooted-path template family.

Only group orders derived from an explicit relation matrix are considered.
Integer row/column operations diagonalize each presentation. Primitive
homomorphisms to cyclic groups are retained up to genuine unit scaling.
This is NOT a classification of all h=0 sets or of non-path trees.
"""

from collections import Counter
from itertools import combinations, combinations_with_replacement, permutations, product
from math import gcd, lcm, prod
import json
from pathlib import Path
from time import monotonic

from stage6_tree_templates import determinant, path_edges, relation_matrix


def multiply(a, b):
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def diagonalize(matrix, verify=False):
    size = len(matrix)
    a = [row[:] for row in matrix]
    left = [[int(i == j) for j in range(size)] for i in range(size)]
    right = [row[:] for row in left]
    for k in range(size):
        while True:
            if not a[k][k]:
                i, j = next((i, j) for i in range(k, size) for j in range(k, size)
                            if a[i][j])
                a[k], a[i] = a[i], a[k]
                left[k], left[i] = left[i], left[k]
                for rows in (a, right):
                    for row in rows:
                        row[k], row[j] = row[j], row[k]
            restarted = False
            for i in range(k + 1, size):
                if not a[i][k]:
                    continue
                q = a[i][k] // a[k][k]
                for rows in (a, left):
                    rows[i] = [x - q * y for x, y in zip(rows[i], rows[k])]
                if a[i][k]:
                    a[k], a[i] = a[i], a[k]
                    left[k], left[i] = left[i], left[k]
                    restarted = True
                    break
            if restarted:
                continue
            for j in range(k + 1, size):
                if not a[k][j]:
                    continue
                q = a[k][j] // a[k][k]
                for rows in (a, right):
                    for row in rows:
                        row[j] -= q * row[k]
                if a[k][j]:
                    for rows in (a, right):
                        for row in rows:
                            row[k], row[j] = row[j], row[k]
                    restarted = True
                    break
            if not restarted:
                break
    assert all(a[i][j] == 0 for i in range(size) for j in range(size) if i != j)
    diagonal = [abs(a[i][i]) for i in range(size)]
    assert all(diagonal)
    assert abs(determinant(matrix)) == prod(diagonal)
    if verify:
        assert multiply(multiply(left, matrix), right) == a
        assert abs(determinant(left)) == abs(determinant(right)) == 1
    return diagonal, right


def prime_powers(n):
    result = []
    p = 2
    while p * p <= n:
        power = 1
        while n % p == 0:
            power *= p
            n //= p
        if power != 1:
            result.append((p, power))
        p += 1
    if n > 1:
        result.append((n, n))
    return result


def divisors(n):
    result = [1]
    for p, power in prime_powers(n):
        terms = [1]
        while terms[-1] != power:
            terms.append(terms[-1] * p)
        result = [d * q for d in result for q in terms]
    return sorted(result)


def primitive_key(v, n):
    assert gcd(n, *v) == 1
    unit = 0
    for p, power in prime_powers(n):
        first = next(x % power for x in v if x % p)
        local = pow(first, -1, power)
        complementary = n // power
        unit += local * complementary * pow(complementary, -1, power)
    return tuple(unit * x % n for x in v)


def cyclic_images(matrix, verify=False, minimum_order=128):
    diagonal, right = diagonalize(matrix, verify)
    exponent = lcm(*diagonal)
    cyclic = prod(diagonal) == exponent
    for n in divisors(exponent):
        if n < minimum_order:
            continue
        kernels = [gcd(d, n) for d in diagonal]
        if cyclic:
            parameters = [tuple(n // g if g > 1 else 0 for g in kernels)]
        else:
            parameters = product(*(range(0, n, n // g) for g in kernels))
        seen = set()
        for y in parameters:
            if gcd(n, *y) != 1:
                continue
            key = primitive_key(y, n)
            if key in seen:
                continue
            seen.add(key)
            b = tuple(sum(c * v for c, v in zip(row, key)) % n for row in right)
            assert gcd(n, *b) == 1
            assert all(sum(c * v for c, v in zip(row, b)) % n == 0 for row in matrix)
            yield n, (0,) + b


def valid_with_witness(a, n):
    target = sum(a) % n
    for u in combinations_with_replacement(range(8), 8):
        if u == tuple(range(8)):
            continue
        if sum(a[i] for i in u) % n == target:
            return False, tuple(a[i] for i in u)
    return True, None


def main():
    start = monotonic()
    limit = 35
    counts = Counter()
    seen = set()
    retained = []
    invalid_h0_examples = []
    complete = True
    for root in range(1, 8):
        edges = path_edges(root)
        for labels in permutations(range(1, 8)):
            if monotonic() - start > limit:
                complete = False
                break
            counts["label_permutations"] += 1
            if any(label == source for (source, _), label in zip(edges, labels)):
                continue
            counts["admissible_templates"] += 1
            m = relation_matrix(edges, labels)
            if abs(determinant(m)) < 128:
                counts["small_determinant"] += 1
                continue
            verify = counts["admissible_templates"] % 100 == 0
            counts["integer_decomposition_audits"] += verify
            for n, a in cyclic_images(m, verify):
                counts["cyclic_quotient_maps_up_to_units"] += 1
                if len(set(a)) != 8:
                    counts["repeated_point"] += 1
                    continue
                # A sorted set is retained with a projectively normalized tuple.
                # This key only removes identical outputs, not all affine copies.
                key = n, tuple(sorted(a))
                if key in seen:
                    counts["duplicate_outputs"] += 1
                    continue
                seen.add(key)
                counts["distinct_eight_point_outputs"] += 1
                pair_sums = {(x + y) % n for x, y in combinations_with_replacement(a, 2)}
                if len(pair_sums) != 36:
                    counts["pair_sum_failure"] += 1
                    continue
                counts["sidon_outputs"] += 1
                delta = {(x - y) % n for x in a for y in a if x != y}
                assert len(delta) == 56
                if {2 * d % n for d in delta} != delta:
                    counts["doubling_closure_failure"] += 1
                    continue
                counts["h0_outputs"] += 1
                valid, witness = valid_with_witness(a, n)
                if not valid:
                    counts["full_validity_failure"] += 1
                    if len(invalid_h0_examples) < 5:
                        invalid_h0_examples.append({"N": n, "A": a, "rival": witness,
                                                    "root": root, "labels": labels})
                    continue
                counts["valid_h0_outputs"] += 1
                triples = Counter((2 * x + y) % n for x in a for y in a)
                r3 = sum((m - 1) * (m - 2) // 2 for m in triples.values())
                retained.append({"N": n, "A": a, "root": root,
                                 "labels": labels, "R3": r3})
        if not complete:
            break
    result = {"family": "rooted paths with marked endpoint, R3=0",
              "seconds_limit": limit, "elapsed_seconds": monotonic() - start,
              "complete_template_family": complete, "counts": dict(counts),
              "valid_retained": retained, "invalid_h0_examples": invalid_h0_examples,
              "scope": "Not all spanning trees; not all h0 sets; not all moduli."}
    Path("stage6_path_quotients.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
