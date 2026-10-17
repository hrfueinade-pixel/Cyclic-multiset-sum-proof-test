"""Exact per-order enumeration for parity two six.

Coverage and pruning are inherited unchanged; verification.worker controls
the deadline and reports completeness for each required quotient order."""

from pathlib import Path
from time import monotonic
from math import gcd
import json

from verification.parity import (
    extend_sumsets,
    normalized_roots,
    rotate,
    sumsets,
    valid_extension,
)

start = monotonic()
cap = 120
results = []
survivors = []


def run(m):
    full = 2**m - 1
    nodes = [0] * 7
    found = []
    examined = set()
    roots = normalized_roots(m, primitive=True)

    def shift(bits, x):
        return rotate(bits, x, m)

    def recurse(prefix, levels, next_value, unitless):
        if monotonic() - start > cap:
            raise TimeoutError()
        nodes[len(prefix)] += 1
        if levels[8] == full:
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
                    "missing": [a for a in range(m) if not levels[8] >> a & 1],
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
            if not valid_extension(prefix, levels, value, m):
                continue
            following = extend_sumsets(levels, value, m)
            recurse(candidate, following, value + 1, unitless)

    for first in roots:
        if 2 * first == m:
            continue
        levels = sumsets([0, first], 8, m)
        recurse([0, first], levels, 1, first != 1)
    return {
        "M": m,
        "completion": "COMPLETE",
        "roots": roots,
        "prefix_counts": nodes,
        "survivors": len(found),
    }
