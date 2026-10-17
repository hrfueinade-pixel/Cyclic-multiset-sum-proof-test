"""Exact per-order enumeration for parity four four.

Coverage and pruning are inherited unchanged; verification.worker controls
the deadline and reports completeness for each required quotient order."""

from pathlib import Path
from itertools import product, combinations_with_replacement
from math import gcd
from time import monotonic
import json, gzip

start = monotonic()
cap = 480
reports = []
shape_records = []
survivors = []
active = None
vectors = [c for c in product(range(5), repeat=4) if sum(c) == 4 and c != (1, 1, 1, 1)]
assert len(vectors) == 34
nonconstant = sorted(
    [(c[3] - 1, c[1] - 1, c[2] - 1) for c in vectors if c[3] != 1],
    key=lambda x: (-abs(x[0]), -x[0], x[1], x[2]),
)
assert len(nonconstant) == 25


def run(m):
    global active
    full = 2**m - 1
    seen = set()
    counts = {
        "B_blocks": 0,
        "proper_saturated": 0,
        "C_shapes": 0,
        "candidate_bases": 0,
        "survivors": 0,
    }
    nodes = [0] * 5
    active = {"M": m, "completion": "RUNNING", "counts": counts, "prefixes": nodes}

    def tick():
        if monotonic() - start >= cap:
            raise TimeoutError()

    def shift(bits, x):
        x %= m
        return (bits << x | bits >> m - x) & full

    def members(bits):
        while bits:
            p = bits & -bits
            yield (p.bit_length() - 1)
            bits ^= p

    def sumsets(d):
        levels = [1]
        for degree in range(1, 9):
            reached = 0
            for x in d:
                reached |= shift(levels[-1], x)
            levels.append(reached)
        return levels

    def examine(points, levels):
        b = tuple(sorted(points))
        if b in seen:
            return
        seen.add(b)
        counts["B_blocks"] += 1
        subgroup_step = gcd(m, *b)
        if subgroup_step > 1 and levels[4] == sum(
            (1 << x for x in range(0, m, subgroup_step))
        ):
            assert m // subgroup_step >= 14 and subgroup_step <= 8
            counts["proper_saturated"] += 1
            return
        target = sum(b) % m
        g = {(target - r) % m for r in range(m) if not levels[4] >> r & 1}
        adjacency = sum((1 << r for r in g if -r % m in g))
        transforms = {}
        for a in (-1, 1, 2, 3):
            divisor = gcd(a, m)
            inv = pow(a // divisor, -1, m // divisor)
            if divisor == 1:
                masks = [sum((1 << inv * r % m for r in g))]
            else:
                masks = [
                    sum((1 << x for x in range(m) if (a * x - r) % m in g))
                    for r in range(divisor)
                ]
            transforms[a] = (divisor, inv, masks)

        def constraint(a, constant):
            divisor, inv, masks = transforms[a]
            q, r = divmod(-constant % m, divisor)
            return shift(masks[r], inv * q)

        for u in members(adjacency):
            tick()
            vmask = adjacency & shift(adjacency, u)
            vmask &= constraint(-1, -u) & constraint(-1, 2 * u) & constraint(2, -u)
            vmask &= full ^ (1 << u + 1) - 1
            for v in members(vmask):
                if (
                    len({(x - y) % m for x in (0, u, v) for y in (0, u, v) if x != y})
                    != 6
                ):
                    continue
                allowed = full ^ (1 << v + 1) - 1
                for a, bcoef, ccoef in nonconstant:
                    allowed &= constraint(a, bcoef * u + ccoef * v)
                    if not allowed:
                        break
                for w in members(allowed):
                    d = [0, u, v, w]
                    s = sum(d) % m
                    if len({(x - y) % m for x in d for y in d if x != y}) != 12:
                        continue
                    for c in vectors:
                        assert sum(((ci - 1) * di for ci, di in zip(c, d))) % m in g
                    counts["C_shapes"] += 1
                    ds = sumsets(d)
                    pair_sums = [
                        sum(p) % m for p in combinations_with_replacement(d, 2)
                    ]
                    six_mixed = 0
                    for r in members(ds[6]):
                        six_mixed |= shift(levels[2], r)
                    actual = []
                    passed_6_8 = []
                    for base in range(m - w):
                        if any(
                            (
                                levels[6] >> (target + 2 * base + s - 1 - r) % m & 1
                                for r in pair_sums
                            )
                        ):
                            continue
                        if levels[8] >> (target + 4 * base + s - 2) % m & 1:
                            continue
                        passed_6_8.append(base)
                        if six_mixed >> (target + s + 1 - 2 * base) % m & 1:
                            continue
                        if ds[8] >> (target + s + 2 - 4 * base) % m & 1:
                            continue
                        c = [base + x for x in d]
                        a = sorted([2 * x + 1 for x in b] + [2 * x for x in c])
                        if (
                            len({(x - y) % (2 * m) for x in a for y in a if x != y})
                            != 56
                        ):
                            continue
                        actual.append(c)
                        survivors.append({"N": 2 * m, "A": a, "B": list(b), "C": c})
                    counts["candidate_bases"] += len(passed_6_8)
                    counts["survivors"] += len(actual)
                    shape_records.append([m, list(b), d, passed_6_8, actual])

    def visit(points, levels, after, unitless):
        tick()
        size = len(points)
        nodes[size] += 1
        if levels[8] == full:
            return
        if size == 4:
            examine(points, levels)
            return
        degree = size + 1
        target = sum(points)
        for x in range(after, m):
            if x in points:
                continue
            if unitless and any((gcd(x - p, m) == 1 for p in points)):
                continue
            p = points + [x]
            if len({(a - b) % m for a in p for b in p if a != b}) != degree * (
                degree - 1
            ):
                continue
            if any(
                (
                    levels[degree - q] >> (target + (1 - q) * x) % m & 1
                    for q in range(degree + 1)
                    if q != 1
                )
            ):
                continue
            updated = []
            for k in range(9):
                reached = 0
                for j in range(k + 1):
                    reached |= shift(levels[k - j], j * x)
                updated.append(reached)
            visit(p, updated, x + 1, unitless)

    roots = sorted((m // order for order in range(3, m + 1) if m % order == 0))
    active["roots"] = roots
    for root in roots:
        levels = [
            sum((1 << r for r in {j * root % m for j in range(k + 1)}))
            for k in range(9)
        ]
        visit([0, root], levels, 1, root != 1)
    active["completion"] = "COMPLETE"
    return active
