"""Bounded local role check, not a search for valid sets or moduli.

Four doubled-difference equations for the isolated-22 endpoint shape.
Exclusions require an exact integer certificate forcing an eight-term
rival after multiplication by a power of two. Odd torsion is NOT divided
away. A survivor is only a local necessary-constraint presentation.
"""

import argparse
from collections import Counter
from fractions import Fraction
from itertools import product
from math import gcd, lcm
from time import monotonic


NAMES = ("s", "r", "a", "c", "b", "p", "q", "f")
POINTS = (
    (0, 0, 0, 0, 0), (1, 0, 0, 0, 0),
    (0, 1, 0, 0, 0), (0, 0, 1, 0, 0),
    (0, 0, 0, 1, 0), (2, -2, 0, -1, 0),
    (2, 0, -2, -1, 0), (0, 0, 0, 0, 1),
)
S, R, A, C, B, P, Q, F = range(8)
COMPARISONS = ((A, R, P), (A, S, P), (C, R, Q), (C, S, Q))


def role_options(center, core, tail):
    other_center = C if center == A else A
    other_core = S if core == R else R
    return tuple((positive, negative)
                 for positive in (B, tail)
                 for negative in (center, other_center, other_core, F)
                 if negative != other_center or positive == B)


def relation(center, core, positive, negative):
    return tuple(2 * (POINTS[center][j] - POINTS[core][j])
                 - POINTS[positive][j] + POINTS[negative][j]
                 for j in range(5))


def compositions(total, length):
    if length == 1:
        yield (total,)
    else:
        for first in range(total + 1):
            for rest in compositions(total - first, length - 1):
                yield (first,) + rest


def rivals():
    target = tuple(sum(point[j] for point in POINTS) for j in range(5))
    for counts in compositions(8, 8):
        if counts == (1,) * 8:
            continue
        vector = tuple(sum(counts[i] * POINTS[i][j] for i in range(8))
                       - target[j] for j in range(5))
        yield counts, vector


def elimination(rows):
    # Row-reduce the transposed presentation, retaining exact row operations.
    matrix = [[Fraction(rows[j][i]) for j in range(4)]
              + [Fraction(int(i == j)) for j in range(5)] for i in range(5)]
    pivots = []
    for col in range(4):
        rank = len(pivots)
        pivot = next((i for i in range(rank, 5) if matrix[i][col]), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        divisor = matrix[rank][col]
        matrix[rank] = [entry / divisor for entry in matrix[rank]]
        for i in range(5):
            if i != rank and matrix[i][col]:
                factor = matrix[i][col]
                matrix[i] = [x - factor * y for x, y in zip(matrix[i], matrix[rank])]
        pivots.append(col)
    transforms = []
    for row in matrix:
        denominator = lcm(*(entry.denominator for entry in row[4:]))
        transforms.append((tuple(int(entry * denominator) for entry in row[4:]),
                           denominator))
    return pivots, transforms


def certificate(rows, pivots, transforms, vector):
    products = [sum(x * y for x, y in zip(row, vector))
                for row, _ in transforms]
    rank = len(pivots)
    if any(products[rank:]):
        return None
    coefficients = [Fraction(0)] * 4
    for i, pivot in enumerate(pivots):
        numerator, denominator = products[i], transforms[i][1]
        reduced = denominator // gcd(numerator, denominator)
        if reduced & (reduced - 1):
            return None
        coefficients[pivot] = Fraction(numerator, denominator)
    multiplier = lcm(*(entry.denominator for entry in coefficients))
    integers = tuple(int(entry * multiplier) for entry in coefficients)
    assert multiplier > 0 and not multiplier & (multiplier - 1)
    assert all(sum(integers[i] * rows[i][j] for i in range(4))
               == multiplier * vector[j] for j in range(5))
    return multiplier, integers


def main(seconds):
    start = monotonic()
    options = [role_options(*comparison) for comparison in COMPARISONS]
    forbidden = tuple(rivals())
    counts = Counter()
    survivors = []
    ranks = Counter()
    completed = True
    for roles in product(*options):
        if monotonic() - start >= seconds:
            completed = False
            break
        counts["raw"] += 1
        negatives = tuple(role[1] for role in roles)
        if len(set(negatives)) != 4:
            counts["negative_reuse"] += 1
            continue
        if any(roles[i][0] == roles[j][0] == B for i, j in ((0, 2), (1, 3))):
            counts["same_core_common_positive"] += 1
            continue
        counts["eligible"] += 1
        rows = tuple(relation(center, core, *role)
                     for (center, core, _), role in zip(COMPARISONS, roles))
        pivots, transforms = elimination(rows)
        ranks[len(pivots)] += 1
        witness = None
        for rival, vector in forbidden:
            witness = certificate(rows, pivots, transforms, vector)
            if witness is not None:
                break
        if witness is not None:
            counts["certified_rival"] += 1
        else:
            counts["survivor"] += 1
            if len(survivors) < 4:
                survivors.append((tuple((NAMES[e], NAMES[v]) for e, v in roles), rows))
    print("scope: four local equations; at most 2401 assignments; 6434 eight-term rivals")
    print("completion:", "COMPLETE" if completed else "TIMEOUT (incomplete)")
    print("runtime_cap_seconds:", seconds)
    print("elapsed_seconds:", round(monotonic() - start, 3))
    print("counts:", dict(counts))
    print("ranks:", dict(ranks))
    print("surviving local presentations (NOT valid counterexamples):", survivors)
    print("Rank-deficient free coefficients are set to zero; this can MISS certificates,")
    print("but every reported exclusion is checked by an exact integer identity.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--seconds", type=float, default=90.0)
    main(parser.parse_args().seconds)
