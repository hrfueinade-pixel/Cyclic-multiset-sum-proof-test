"""Two bounded h=0 configuration searches, not a modulus sweep.

Enumerate symmetric doubling-orbit unions of size 56 at N=255 and 273.
Unit-difference cases normalize to (0,1); unit-free cases retain (0,).
No claim of completeness is made after a deadline is reached.
"""

from functools import lru_cache
from math import gcd
import json
from pathlib import Path
from time import monotonic

from stage3_search import (append_sumsets, bits, direct_valid_count,
                           forbidden_extensions, prefix_state, rotate)
from stage4_lemma_experiments import inspect


def chunks(n):
    unseen = set(range(1, n))
    result = []
    while unseen:
        x = min(unseen)
        orbit = set()
        while x not in orbit:
            orbit.add(x)
            x = 2 * x % n
        group = orbit | {(-x) % n for x in orbit}
        unseen.difference_update(group)
        result.append((len(group), sum(1 << x for x in group)))
    return result


def masks(n):
    groups = chunks(n)

    @lru_cache(None)
    def possible(i, left):
        if left == 0:
            return True
        if i == len(groups) or left < 0:
            return False
        return (possible(i + 1, left)
                or possible(i + 1, left - groups[i][0]))

    def generate(i, left, mask):
        if left == 0:
            yield mask
            return
        if possible(i + 1, left):
            yield from generate(i + 1, left, mask)
        if possible(i + 1, left - groups[i][0]):
            yield from generate(i + 1, left - groups[i][0], mask | groups[i][1])

    yield from generate(0, 56, 0)


def affine_key(a, n):
    return min(tuple(sorted(u * (x - base) % n for x in a))
               for base in a for u in range(1, n) if gcd(u, n) == 1)


def search(n, seconds=20):
    start = monotonic()
    deadline = start + seconds
    candidate_masks = list(masks(n))
    unit_mask = sum(1 << x for x in range(1, n) if gcd(x, n) == 1)
    counts = [0] * 9
    completed = 0
    searched = 0
    accepted = {}
    active_mask = None

    class Deadline(Exception):
        pass

    def dfs(prefix, state, available, used_differences, adjacency):
        counts[len(prefix)] += 1
        if monotonic() >= deadline:
            raise Deadline
        if len(prefix) == 8:
            checked = direct_valid_count(prefix, n)
            assert checked["valid"] and used_differences.bit_count() == 56
            key = affine_key(prefix, n)
            if key not in accepted:
                accepted[key] = inspect(prefix, n)
            return
        available &= ~forbidden_extensions(prefix, state, n)
        if available.bit_count() < 8 - len(prefix):
            return
        for x in bits(available):
            added = 0
            legal = True
            for y in prefix:
                forward, reverse = (x - y) % n, (y - x) % n
                pair = (1 << forward) | (1 << reverse)
                if added & pair or used_differences & pair:
                    legal = False
                    break
                added |= pair
            if not legal:
                continue
            after = available & ~((1 << (x + 1)) - 1) & adjacency[x]
            dfs(prefix + (x,), append_sumsets(state, x, n), after,
                used_differences | added, adjacency)

    try:
        for delta in candidate_masks:
            if delta & unit_mask:
                if not delta & 2:
                    continue
                prefix = (0, 1)
                used = (1 << 1) | (1 << (n - 1))
            else:
                prefix = (0,)
                used = 0
            active_mask = delta
            searched += 1
            adjacency = [rotate(delta, x, n) for x in range(n)]
            available = delta & ~((1 << (prefix[-1] + 1)) - 1)
            for x in prefix:
                available &= adjacency[x]
            dfs(prefix, prefix_state(prefix, n), available, used, adjacency)
            completed += 1
        status = "COMPLETE"
    except Deadline:
        status = "TIMEOUT"
    return {"N": n, "status": status, "seconds_limit": seconds,
            "elapsed_seconds": monotonic() - start,
            "all_orbit_union_masks": len(candidate_masks),
            "normalized_masks_started": searched,
            "normalized_masks_completed": completed,
            "valid_prefix_counts": counts,
            "accepted_affine_classes": len(accepted),
            "accepted": list(accepted.values()),
            "active_difference_mask": active_mask,
            "scope": "valid non-antipodal eight-sets with h=0 at this N only"}


def main():
    results = [search(n) for n in (273, 255)]
    Path("stage5_h0_probe_results.json").write_text(
        json.dumps(results, indent=2) + "\n", encoding="ascii")
    for r in results:
        print(json.dumps({k: v for k, v in r.items()
                          if k not in ("accepted", "active_difference_mask")}, indent=2))


if __name__ == "__main__":
    main()
