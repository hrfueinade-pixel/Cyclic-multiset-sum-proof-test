"""Exact cyclic sumsets and normalized roots used by the parity enumerations.

These shared routines are cross-checked against direct multiset enumeration
in tests/test_mathematics.py. They do not establish the reduction to a model.
"""

from math import gcd


def rotate(bits, offset, modulus):
    offset %= modulus
    return (bits << offset | bits >> (modulus - offset)) & ((1 << modulus) - 1)


def sumsets(points, degree, modulus):
    levels = [1]
    for _ in range(degree):
        reached = 0
        for point in points:
            reached |= rotate(levels[-1], point, modulus)
        levels.append(reached)
    return levels


def extend_sumsets(levels, point, modulus):
    return [
        _union(rotate(levels[d - k], k * point, modulus) for k in range(d + 1))
        for d in range(len(levels))
    ]


def _union(masks):
    result = 0
    for mask in masks:
        result |= mask
    return result


def valid_extension(prefix, levels, point, modulus):
    """Requires a valid prefix, a new distinct point, and levels through n+1.

    One copy reduces to validity of the prefix. All other multiplicities of
    the new point are tested, including zero copies.
    """
    degree = len(prefix) + 1
    target = sum(prefix)
    return not any(
        levels[degree - copies] >> ((target + (1 - copies) * point) % modulus) & 1
        for copies in range(degree + 1)
        if copies != 1
    )


def normalized_roots(modulus, primitive=False):
    if primitive:
        primes = [
            p
            for p in range(2, modulus + 1)
            if modulus % p == 0 and all(p % d for d in range(2, p))
        ]
        if len(primes) <= 2:
            return [1]
    # A root of order two is antipodal and is outside these four domains.
    return sorted(
        modulus // order for order in range(3, modulus + 1) if modulus % order == 0
    )


def affine_preimages(mask, modulus, coefficients=(-1, 1, 2, 3)):
    """Return the mask of all x with a*x+c in mask, retaining nonunit fibers."""
    transforms = {}
    for a in coefficients:
        divisor = gcd(a, modulus)
        inverse = pow(a // divisor, -1, modulus // divisor)
        transforms[a] = (
            divisor,
            inverse,
            [
                sum(
                    1 << x
                    for x in range(modulus)
                    if mask >> ((a * x - r) % modulus) & 1
                )
                for r in range(divisor)
            ],
        )

    def constraint(a, constant):
        divisor, inverse, masks = transforms[a]
        quotient, remainder = divmod(-constant % modulus, divisor)
        return rotate(masks[remainder], inverse * quotient, modulus)

    return constraint
