"""Fixed arithmetic certificates and invalid negative-doubling controls.

The prime powers come from the already-proved bound |H|<=2187 and the
smallest exponent with p^e>=128, not an exhaustive modulus search.
"""

from itertools import combinations_with_replacement
from math import gcd, lcm
import json
from pathlib import Path


def partitions(total, least=1):
    if total == 0:
        yield ()
    for first in range(least, total + 1):
        for rest in partitions(total - first, first):
            yield (first,) + rest


def signed_doubling_orbit(n):
    orbit = set()
    x = 1
    while x not in orbit:
        orbit.add(x)
        x = 2 * x % n
    assert x == 1
    return orbit | {(-x) % n for x in orbit}


def prime_power_table():
    result = []
    for p in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43):
        exponent, n = 2, p ** 2
        while n < 128:
            exponent += 1
            n *= p
        assert n <= 2187
        orbit = signed_doubling_orbit(n)
        assert len(orbit) > 56
        k = next(k for k in range(1, p) if pow(2, k, p) == 1)
        lifting_witness = pow(2, k, p ** 2)
        assert lifting_witness != 1
        expected_size = k * p ** (exponent - 1) * (1 if k % 2 == 0 else 2)
        assert len(orbit) == expected_size
        result.append({"p": p, "minimum_exponent": exponent,
                       "minimum_power": n, "joint_orbit_size": len(orbit),
                       "order_of_two_mod_p": k,
                       "two_power_k_mod_p_squared": lifting_witness})
    return result


def negative_control(a, n):
    assert len(set(a)) == 8
    assert {2 * x % n for x in a} == {(-x) % n for x in a}
    order = n // gcd(n, *(x - a[0] for x in a))
    target = sum(a) % n
    rivals = []
    checked = 0
    for indices in combinations_with_replacement(range(8), 8):
        checked += 1
        if indices != tuple(range(8)) and sum(a[i] for i in indices) % n == target:
            if len(rivals) < 2:
                rivals.append(tuple(a[i] for i in indices))
    assert rivals and checked == 6435
    return {"N": n, "A": a, "difference_subgroup_order": order,
            "negative_doubling_stable": True, "valid": False,
            "multisets_checked": checked, "rivals": rivals}


def main():
    partition_bounds = []
    for partition in partitions(8):
        if len(partition) == 1:
            continue
        q = [abs((1 - (-2) ** k) // 3) for k in partition]
        bound = 3 * lcm(*q)
        assert bound <= 129
        partition_bounds.append({"partition": partition, "lcm": lcm(*q),
                                 "subgroup_order_upper_bound": bound})
    assert max(r["lcm"] for r in partition_bounds) == 43
    eight = tuple((-2) ** k % 255 for k in range(8))
    seven_and_fixed = (0,) + tuple((-2) ** k % 129 for k in range(7))
    three_and_five = tuple(11 * (-2) ** k % 99 for k in range(3)) + tuple(
        3 * (-2) ** k % 99 for k in range(5))
    result = {"prime_power_table": prime_power_table(),
              "negative_doubling_partition_bounds": partition_bounds,
              "invalid_negative_doubling_controls": [negative_control(a, n) for a, n in (
                  (eight, 255), (seven_and_fixed, 129), (three_and_five, 99))],
              "scope": "13 fixed orbit certificates, 21 partitions, 3 invalid fixtures."}
    Path("stage7_arithmetic_results.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
