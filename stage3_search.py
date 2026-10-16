"""Deadline-bounded exact hereditary-validity search, standard library only.

No absence result is exhaustive unless the returned status is COMPLETE.
Every accepted candidate is independently checked by full multiset enumeration.
"""

import argparse
import json
from functools import lru_cache
from itertools import combinations, combinations_with_replacement
from math import gcd
from pathlib import Path
from time import monotonic

from research_experiments import collision


def bits(mask):
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask -= bit


def rotate(mask, shift, modulus):
    shift %= modulus
    if not shift:
        return mask
    full = (1 << modulus) - 1
    return ((mask << shift) | (mask >> (modulus - shift))) & full


def append_sumsets(sumsets, value, modulus):
    # Unbounded use of the new point, truncated at the requested degree.
    result = list(sumsets)
    for degree in range(1, len(result)):
        result[degree] |= rotate(result[degree - 1], value, modulus)
    return result


@lru_cache(maxsize=128)
def dilation_tables(coefficient, modulus):
    tables = []
    for start in range(0, modulus, 8):
        table = [0] * 256
        images = [1 << (coefficient * (start + i) % modulus) for i in range(8)]
        for pattern in range(1, 256):
            low = pattern & -pattern
            table[pattern] = table[pattern - low] | images[low.bit_length() - 1]
        tables.append(table)
    return tables


def dilate(mask, coefficient, modulus):
    result = 0
    for table in dilation_tables(coefficient % modulus, modulus):
        result |= table[mask & 255]
        mask >>= 8
        if not mask:
            break
    return result


def forbidden_extensions(prefix, sumsets, modulus):
    """Exact forbidden values, assuming prefix is already valid.

    A rival at the next degree uses q copies of the new element x.
    For q=0, x is an old (p+1)-term sum minus the old target.
    For q>=2, (q-1)x equals the old target minus an old (p+1-q)-term sum.
    The q=1 case is excluded by validity of the prefix.
    """
    degree = len(prefix) + 1
    target = sum(prefix) % modulus
    forbidden = rotate(sumsets[degree], -target, modulus)
    full = (1 << modulus) - 1
    if forbidden == full:
        return forbidden
    for q in range(2, degree + 1):
        coefficient = q - 1
        divisor = gcd(coefficient, modulus)
        reduced_modulus = modulus // divisor
        inverse = pow(coefficient // divisor, -1, reduced_modulus)
        if divisor == 1:
            forbidden |= rotate(dilate(sumsets[degree - q], -inverse, modulus),
                                inverse * target, modulus)
            if forbidden == full:
                return forbidden
            continue
        for old_sum in bits(sumsets[degree - q]):
            rhs = (target - old_sum) % modulus
            if rhs % divisor:
                continue
            first = inverse * (rhs // divisor) % reduced_modulus
            for lift in range(divisor):
                forbidden |= 1 << (first + lift * reduced_modulus)
            if forbidden == full:
                return forbidden
    return forbidden


def prefix_state(prefix, modulus, degree=8):
    state = [1] + [0] * degree
    for value in prefix:
        state = append_sumsets(state, value, modulus)
    return state


def direct_valid_count(a, modulus):
    target = sum(a) % modulus
    candidates = 0
    hits = []
    for indices in combinations_with_replacement(range(len(a)), len(a)):
        candidates += 1
        if sum(a[i] for i in indices) % modulus == target:
            hits.append(tuple(a[i] for i in indices))
    return {"multisets_enumerated": candidates, "target_representations": hits,
            "valid": len(hits) == 1}


def accepted_growth(a, modulus):
    t3 = {(2*x+y) % modulus for x in a for y in a}
    t4 = {(2*x+y+z) % modulus for x in a
          for y,z in combinations_with_replacement(a,2)}
    key = min(tuple(sorted(u*(x-base) % modulus for x in a))
              for u in range(1,modulus) if gcd(u,modulus)==1 for base in a)
    return {"T3":len(t3),"T4":len(t4),"growth_gap":len(t4)-2*len(t3),
            "affine_key":key}


def validate_encoding():
    comparisons = 0
    for modulus, size in ((5, 3), (6, 3), (7, 3), (11, 4), (12, 4), (15, 4)):
        for p in range(1, size):
            for rest in combinations(range(1, modulus), p - 1):
                prefix = (0,) + rest
                if collision(prefix, modulus) is not None:
                    continue
                state = prefix_state(prefix, modulus, size)
                forbidden = forbidden_extensions(prefix, state, modulus)
                for x in range(prefix[-1] + 1, modulus):
                    predicted = not (forbidden >> x) & 1
                    actual = collision(prefix + (x,), modulus) is None
                    assert predicted == actual, (prefix, x, modulus, predicted)
                    comparisons += 1
    reference_checks = []
    for modulus in (248, 255, 256):
        a = tuple((1 << i) - 1 for i in range(8))
        prefix = (0,)
        state = prefix_state(prefix, modulus)
        for x in a[1:]:
            assert not (forbidden_extensions(prefix, state, modulus) >> x) & 1
            state = append_sumsets(state, x, modulus)
            prefix += (x,)
        verified = direct_valid_count(a, modulus)
        assert verified["valid"] and verified["multisets_enumerated"] == 6435
        reference_checks.append({"N": modulus, "A": a, **verified})
    return {"small_extension_comparisons": comparisons,
            "independent_known_eight_element_checks": reference_checks}


class Deadline(Exception):
    pass


def search(modulus, size, seconds, initial=(0,), checkpoint=None, stop_on_valid=False,
           first_min=None, first_max=None):
    """Enumerate all sorted extensions of initial, subject to exact pruning.

    initial=(0,) covers every translated set. Any stronger initial tuple
    covers only that conditional class unless justified separately.
    """
    start = monotonic()
    deadline = start + seconds
    prefix_counts = [0] * (size + 1)
    extension_counts = [0] * (size + 1)
    valid = []
    completed_branches = []
    active_prefix = initial
    initial_state = prefix_state(initial, modulus, size)
    assert collision(initial, modulus) is None

    def record(status):
        result = {"status": status, "N": modulus, "n": size,
                  "initial": initial, "seconds_limit": seconds,
                  "first_extension_min": first_min,
                  "first_extension_max": first_max,
                  "elapsed_seconds": monotonic() - start,
                  "visited_valid_prefixes_by_size": prefix_counts,
                  "legal_extensions_by_new_size": extension_counts,
                  "fully_completed_first_extension_branches": completed_branches,
                  "active_prefix_at_checkpoint": active_prefix,
                  "accepted_sets": valid, "complete_search": status == "COMPLETE"}
        if size==8:
            result["accepted_affine_classes"] = len({tuple(v["affine_key"]) for v in valid})
            result["growth_plus17_counterexamples"] = [v for v in valid if v["growth_gap"]<17]
        if checkpoint:
            Path(checkpoint).write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
        return result

    def dfs(prefix, state):
        nonlocal active_prefix
        active_prefix = prefix
        prefix_counts[len(prefix)] += 1
        if monotonic() >= deadline:
            raise Deadline
        if len(prefix) == size:
            verified = direct_valid_count(prefix, modulus)
            assert verified["valid"]
            valid.append({"A": prefix, **verified,
                          **(accepted_growth(prefix,modulus) if size==8 else {})})
            if stop_on_valid:
                raise StopIteration
            return
        forbidden = forbidden_extensions(prefix, state, modulus)
        last = modulus - (size - len(prefix))
        available = (((1 << (last + 1)) - 1) ^ ((1 << (prefix[-1] + 1)) - 1)) & ~forbidden
        if len(prefix) == len(initial):
            if first_min is not None:
                available &= ~((1 << first_min) - 1)
            if first_max is not None:
                available &= (1 << (first_max + 1)) - 1
        for value in bits(available):
            extension_counts[len(prefix) + 1] += 1
            dfs(prefix + (value,), append_sumsets(state, value, modulus))
            if len(prefix) == len(initial):
                completed_branches.append(value)
                record("RUNNING")

    try:
        dfs(initial, initial_state)
        status = "COMPLETE"
    except Deadline:
        status = "TIMEOUT"
    except StopIteration:
        status = "VALID_FOUND"
    return record(status)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", type=int, default=187)
    parser.add_argument("--n", type=int, default=8)
    parser.add_argument("--seconds", type=float, default=120)
    parser.add_argument("--initial", type=int, nargs="+", default=[0, 1])
    parser.add_argument("--checkpoint", default="stage3_search_checkpoint.json")
    parser.add_argument("--validate", action="store_true")
    parser.add_argument("--stop-on-valid", action="store_true")
    parser.add_argument("--first-min", type=int)
    parser.add_argument("--first-max", type=int)
    args = parser.parse_args()
    if args.validate:
        print(json.dumps(validate_encoding(), indent=2))
    print(json.dumps(search(args.N, args.n, args.seconds, tuple(args.initial),
                            args.checkpoint, args.stop_on_valid,
                            args.first_min, args.first_max), indent=2))


if __name__ == "__main__":
    main()
