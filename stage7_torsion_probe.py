"""Two fixed, bounded h=0 probes relevant to order-five collisions.

N=315 and N=585 are fixed three-prime-factor examples. All orbit-mask
and accepted-set counts are reported; no modulus sweep is performed.
Uses the previously audited hereditary-validity search.
"""

from collections import Counter
import json
from math import gcd
from pathlib import Path

from stage5_h0_probe import chunks, search


def plan(n):
    orbits = chunks(n)
    dp = [1] + [0] * 56
    for size, _ in orbits:
        for left in range(56, size - 1, -1):
            dp[left] += dp[left - size]
    assert dp[56] <= 2000
    return {"N": n, "orbit_sizes": dict(Counter(size for size, _ in orbits)),
            "planned_size56_masks": dp[56]}


def main():
    results = []
    for n in (315, 585):
        planned = plan(n)
        record = search(n, seconds=15)
        record["plan"] = planned
        assert record["all_orbit_union_masks"] == record["plan"]["planned_size56_masks"]
        for accepted in record["accepted"]:
            a = accepted["A"]
            accepted["difference_subgroup_order"] = n // gcd(n, *(x - a[0] for x in a))
        results.append(record)
        print(json.dumps({k: v for k, v in record.items()
                          if k not in ("accepted", "active_difference_mask")}, indent=2))
    Path("stage7_torsion_probe_results.json").write_text(
        json.dumps(results, indent=2) + "\n", encoding="ascii")


if __name__ == "__main__":
    main()
