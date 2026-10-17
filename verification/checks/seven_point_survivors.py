"""Exact per-order enumeration for seven point survivors.

Coverage and pruning are inherited unchanged; verification.worker controls
the deadline and reports completeness for each required quotient order."""

from pathlib import Path
from time import monotonic
from math import gcd
import json

start = monotonic()
cap = 180
results = []
survivors = []


def prime_count(n):
    return sum(
        (
            all((p % d for d in range(2, int(p**0.5) + 1))) and n % p == 0
            for p in range(2, n + 1)
        )
    )


def run(m):
    full = 2**m - 1
    nodes = [0] * 7
    found = []
    examined = set()
    roots = [1]
    if prime_count(m) >= 3:
        roots += [m // order for order in range(3, m) if m % order == 0]

    def shift(bits, x):
        x %= m
        return (bits << x | bits >> m - x) & full

    def recurse(prefix, levels, next_value, unitless):
        if monotonic() - start > cap:
            raise TimeoutError()
        nodes[len(prefix)] += 1
        if levels[7] == full:
            return
        if len(prefix) == 6:
            if gcd(m, *prefix) != 1:
                return
            key = tuple(sorted(prefix))
            if key not in examined:
                examined.add(key)
                row = {
                    "M": m,
                    "B": list(key),
                    "missing": [a for a in range(m) if not levels[7] >> a & 1],
                }
                found.append(row)
                survivors.append(row)
            return
        terms = len(prefix) + 1
        original = sum(prefix)
        for value in range(next_value, m):
            if value in prefix:
                continue
            if unitless and any((gcd(value - a, m) == 1 for a in prefix)):
                continue
            candidate = prefix + [value]
            differences = [(a - b) % m for a in candidate for b in candidate if a != b]
            if len(set(differences)) != terms * (terms - 1):
                continue
            if any(
                (
                    levels[terms - copies] >> (original + (1 - copies) * value) % m & 1
                    for copies in range(terms + 1)
                    if copies != 1
                )
            ):
                continue
            following = []
            for size in range(9):
                residue_set = 0
                for copies in range(size + 1):
                    residue_set |= shift(levels[size - copies], copies * value)
                following.append(residue_set)
            recurse(candidate, following, value + 1, unitless)

    for first in roots:
        if 2 * first == m:
            continue
        levels = []
        for k in range(9):
            levels.append(sum((1 << r for r in {first * j % m for j in range(k + 1)})))
        recurse([0, first], levels, 1, first != 1)
    return {
        "M": m,
        "completion": "COMPLETE",
        "roots": roots,
        "prefix_counts": nodes,
        "survivors": len(found),
    }
