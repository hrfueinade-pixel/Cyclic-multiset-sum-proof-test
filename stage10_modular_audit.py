"""Independent prime-power kernel audit of the four-way template checks.

No diagonalization or integer normal-form routine is used here. Shared
structural generators are audited by a mathematical coverage proof in
stage10_fourway_findings.md; the matrices, determinant, cyclic quotient
solutions and final rejections are independently reconstructed.
"""

import argparse
from collections import Counter
from itertools import combinations_with_replacement, product
from math import gcd
import json
from pathlib import Path
from time import monotonic

from stage10_fourway_templates import structural_templates, pure_structural_templates


def det3(a):
    return (a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
            - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
            + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0]))


def adjugate(a):
    cols = [tuple((-1) ** (i + j) * det3([[a[r][s] for s in range(4) if s != i]
                                         for r in range(4) if r != j])
                  for i in range(4)) for j in range(4)]
    det = sum(a[0][i] * cols[0][i] for i in range(4))
    assert all(sum(a[r][i] * col[i] for i in range(4)) == det * (r == j)
               for j, col in enumerate(cols) for r in range(4))
    return det, cols


def factors(n):
    answer = []
    p = 2
    while p * p <= n:
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        if e:
            answer.append((p, e))
        p += 1
    if n > 1:
        answer.append((n, 1))
    return answer


def affine_solutions(matrix, rhs, p, restrictions):
    a = [[x % p for x in row] + [v % p] for row, v in zip(matrix, rhs)]
    a += [[int(j == i) for j in range(4)] + [value] for i, value in restrictions]
    r, pivots = 0, []
    for c in range(4):
        pivot = next((i for i in range(r, len(a)) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        unit = pow(a[r][c], -1, p)
        a[r] = [x * unit % p for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c]:
                factor = a[i][c]
                a[i] = [(x - factor * y) % p for x, y in zip(a[i], a[r])]
        pivots.append(c)
        r += 1
    if any(not any(row[:4]) and row[4] for row in a):
        return []
    free = [c for c in range(4) if c not in pivots]
    assert p ** len(free) <= 4096
    answer = []
    for values in product(range(p), repeat=len(free)):
        x = [0] * 4
        for c, value in zip(free, values):
            x[c] = value
        for i, c in enumerate(pivots):
            x[c] = (a[i][4] - sum(a[i][j] * x[j] for j in free)) % p
        answer.append(tuple(x))
    return answer


def local_projective_kernel(matrix, cols, p, exponent):
    modulus = p ** exponent
    det = sum(matrix[0][i] * cols[0][i] for i in range(4))
    assert det % modulus == 0  # The caller only requests determinant divisors.
    col = next((v for v in cols if any(x % p for x in v)), None)
    if col is not None:
        # A nonzero cofactor gives rank three modulo p, hence one
        # primitive unit orbit at every divisor p^e of the determinant.
        first = next(i for i, x in enumerate(col) if x % p)
        unit = pow(col[first], -1, modulus)
        answer = [tuple(unit * x % modulus for x in col)]
    else:
        answer = []
        for first in range(4):
            restrictions = [(i, 0) for i in range(first)] + [(first, 1)]
            answer += affine_solutions(matrix, [0] * 4, p, restrictions)
        for e in range(1, exponent):
            old_modulus = p ** e
            lifted = []
            for x in answer:
                first = next(i for i, value in enumerate(x) if value % p)
                products = [sum(c * v for c, v in zip(row, x)) for row in matrix]
                assert all(value % old_modulus == 0 for value in products)
                rhs = [-(value // old_modulus) % p for value in products]
                for z in affine_solutions(matrix, rhs, p, [(first, 0)]):
                    lifted.append(tuple(x[i] + old_modulus * z[i] for i in range(4)))
            answer = lifted
            assert len(answer) <= 4096 and len(set(answer)) == len(answer)
    for x in answer:
        first = next(i for i, value in enumerate(x) if value % p)
        assert x[first] == 1 and all(value % p == 0 for value in x[:first])
        assert all(sum(c * v for c, v in zip(row, x)) % modulus == 0 for row in matrix)
    return answer, col is None


def quotient_images(matrix, det, cols, counts):
    fs = factors(abs(det))
    cache = {}
    for exponents in product(*(range(e + 1) for _, e in fs)):
        selected = [(p, e) for (p, _), e in zip(fs, exponents) if e]
        n = 1
        for p, e in selected:
            n *= p ** e
        if n < 184:
            continue
        counts["determinant_divisor_orders_checked"] += 1
        local = []
        for p, e in selected:
            if (p, e) not in cache:
                cache[p, e], difficult = local_projective_kernel(matrix, cols, p, e)
                counts["rank_at_most_two_local_audits"] += difficult
            local.append(cache[p, e])
        for vectors in product(*local):
            x = [0] * 4
            for (p, e), v in zip(selected, vectors):
                modulus = p ** e
                cofactor = n // modulus
                multiplier = cofactor * pow(cofactor, -1, modulus)
                x = [a + multiplier * b for a, b in zip(x, v)]
            x = tuple(value % n for value in x)
            assert gcd(n, *x) == 1
            assert all(sum(c * v for c, v in zip(row, x)) % n == 0 for row in matrix)
            yield n, x


def matrix_and_filter(edges, labels, selected, pure):
    if not pure and any(labels[i] == 0 for i in range(len(selected))):
        return None
    marked = 0 if pure else 4
    for source in {a for a, _ in edges}:
        partners = [(b, label) for (a, b), label in zip(edges, labels) if a == source]
        marks = [(source, marked)] + partners
        if len(marks) > 4 or sum(a == b for a, b in marks) > 1:
            return None
        if any(label == center and center != own
               for own, label in marks for center, _ in marks):
            return None
    if pure:
        points = [(0, 0, 0, 0)] + [tuple(int(i == j) for i in range(4)) for j in range(3)]
        points += [tuple(-2 * x for x in points[i]) for i in range(1, 4)]
        points += [(0, 0, 0, 1)]
        label_order = (1, 2, 3, 7)
    else:
        points = [(0, 0, 0, 0)] + [tuple(int(i == j) for i in range(4)) for j in range(1, 4)]
        points += [tuple(int(i == 0) - 2 * x for i, x in enumerate(c)) for c in points[:4]]
        label_order = (0, 1, 2, 3)
    rows = {}
    for (a, b), label in zip(edges, labels):
        rows[label] = tuple(2 * points[a][i] + points[marked][i]
                            - 2 * points[b][i] - points[label][i] for i in range(4))
    return tuple(rows[label] for label in label_order)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pure", action="store_true")
    pure = parser.parse_args().pure
    start = monotonic()
    limit = 30 if pure else 20
    counts = Counter()
    seen = set()
    complete = True
    accepted = []
    templates = pure_structural_templates() if pure else structural_templates()
    for selected, edges, labels in templates:
        if monotonic() - start > limit:
            complete = False
            break
        counts["labeled_structural_templates"] += 1
        matrix = matrix_and_filter(edges, labels, selected, pure)
        if matrix is None:
            continue
        counts["locally_admissible_templates"] += 1
        if matrix in seen:
            continue
        seen.add(matrix)
        counts["distinct_matrices"] += 1
        det, cols = adjugate(matrix)
        assert abs(det) % 2 and abs(det) <= 2187
        if abs(det) < 184:
            continue
        counts["large_matrices"] += 1
        for n, vector in quotient_images(matrix, det, cols, counts):
            counts["cyclic_quotient_maps_up_to_units"] += 1
            if pure:
                c1, c2, c3, x = vector
                c = (c1, c2, c3)
                a = (0,) + c + tuple(-2 * z % n for z in c) + (x,)
            else:
                y, c1, c2, c3 = vector
                c = (0, c1, c2, c3)
                a = c + tuple((y - 2 * z) % n for z in c)
            if len(set(a)) != 8:
                counts["repeated_point_maps"] += 1
                continue
            if len({(x + y) % n for x, y in combinations_with_replacement(a, 2)}) != 36:
                counts["pair_sum_failure_maps"] += 1
                continue
            counts["sidon_maps"] += 1
            delta = {(x - y) % n for x in a for y in a if x != y}
            if any(2 * d % n not in delta for d in delta):
                counts["doubling_closure_failure_maps"] += 1
            else:
                accepted.append({"N": n, "A": a, "matrix": matrix})
    primary_path = "stage10_fourway_pure_results.json" if pure else "stage10_fourway_template_results.json"
    primary = json.loads(Path(primary_path).read_text(encoding="ascii"))
    if complete:
        assert primary["complete_template_family"]
        for key in ("labeled_structural_templates", "locally_admissible_templates",
                    "distinct_matrices", "large_matrices", "cyclic_quotient_maps_up_to_units"):
            assert counts[key] == primary["counts"][key], (key, counts[key], primary["counts"][key])
        assert not accepted
    result = {"branch": "one pure" if pure else "disjoint",
              "complete_audit": complete, "seconds_limit": limit,
              "elapsed_seconds": monotonic() - start, "counts": dict(counts),
              "accepted_h0": accepted,
              "scope": "Shared structural generators; independently reconstructed modular kernels and rejections."}
    output = "stage10_modular_pure_audit.json" if pure else "stage10_modular_disjoint_audit.json"
    Path(output).write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
