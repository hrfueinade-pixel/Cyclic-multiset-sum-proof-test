"""Independent positive-witness audit using count compositions, not word lists.

Imports no producer, historical verifier, numpy, or research kernel. Checks
all saved diagnostic witnesses through all 6435 degree-eight multisets.
It does not certify negative discovery searches or the interrupted coset run.
"""
import json
from collections import defaultdict
from itertools import combinations
from math import comb
from pathlib import Path
from time import monotonic


def counts(degree, slots=8, prefix=()):
    if slots == 1:
        yield prefix + (degree,)
    else:
        for c in range(degree + 1):
            yield from counts(degree - c, slots - 1, prefix + (c,))


def residue(c, a, n):
    return sum(x * y for x, y in zip(c, a)) % n


def audit(n, a):
    assert n % 2 and len(a) == len(set(a)) == 8
    f = {}
    for degree in (2, 3, 4):
        table = defaultdict(list)
        for c in counts(degree):
            table[residue(c, a, n)].append(c)
        assert sum(map(len, table.values())) == comb(degree + 7, 7)
        f[degree] = table
    q = {}
    for degree in (3, 4):
        records = []
        for support in combinations(range(8), degree):
            c = tuple(int(i in support) for i in range(8))
            records.append((residue(c, a, n), c))
        q[degree] = records
    protected = {k: all(f[k][x] == [c] for x, c in q[k]) for k in (3, 4)}
    q4 = {x for x, _ in q[4]}
    target = sum(a) % n
    inter = set(f[4]) & {(target - x) % n for x in f[4]}
    delta = {(a[i] - a[j]) % n for i in range(8) for j in range(8) if i != j}
    h = sum(2 * d % n not in delta for d in delta) // 2
    overlap = []
    for t in range(n):
        pairs = [(i, j) for i in range(8) for j in range(8) if (2 * a[i] - a[j]) % n == t]
        overlap.append(len(pairs))
    periods = [d for d in range(n) if all((x + d) % n in f[4] for x in f[4])]
    rivals = []
    checked = 0
    for c in counts(8):
        checked += 1
        if residue(c, a, n) == target and c != (1,) * 8:
            rivals.append(c)
    assert checked == 6435
    valid = not rivals
    assert valid == (protected[4] and inter == q4)
    marks = defaultdict(list)
    for i in range(8):
        for j in range(8):
            marks[(2 * a[i] + a[j]) % n].append((i, j))
    r3 = sum(comb(len(v) - 1, 2) for v in marks.values() if len(v) >= 3)
    if len(delta) == 56:
        assert len(marks) == 36 + h + r3
    if protected[3]:
        assert len(f[3]) == 56 + len(marks) == 92 + h + r3
    # Rank of the coordinate pairing is the number of available complements.
    # Every row has at most one 1, in a different column from all other rows.
    pairing_rank = len(inter)
    if valid:
        assert pairing_rank == 70
        assert all((2 * x - target) % n for x in q4)
        assert n >= 2 * len(f[4]) - 69
        incidences = {x: sum((x - v) % n in f[3] for v in a) for x in f[4]}
        assert sum(incidences.values()) == 8 * len(f[3])
        assert all(incidences[x] == 4 for x in q4)
        assert len(f[4]) >= len(f[3]) + 35
    first_bad = None
    for x, c in q[4]:
        for d in f[4][x]:
            if d != c:
                first_bad = {"residue": x, "squarefree_counts": list(c), "opponent_counts": list(d)}
                break
        if first_bad:
            break
    return {"N": n, "A": list(a), "sumset2": len(f[2]), "sumset3": len(f[3]),
            "sumset4": len(f[4]), "difference_count": len(delta), "T3": len(marks),
            "h": h, "R3": r3, "cubic_protected": protected[3],
            "quartic_protected": protected[4], "squarefree3_distinct": len({x for x, _ in q[3]}),
            "squarefree4_distinct": len(q4),
            "quartics_protected_count": sum(f[4][x] == [c] for x, c in q[4]),
            "maximum_dilation_overlap": max(overlap),
            "overlap_shifts": [t for t, value in enumerate(overlap) if value == max(overlap)],
            "periods4": periods, "intersection_size": len(inter),
            "intersection_exact_Q": inter == q4, "pairing_rank": pairing_rank,
            "valid8": valid, "eight_multisets_checked": checked,
            "rival_count": len(rivals), "first_rival": list(rivals[0]) if rivals else None,
            "first_quartic_failure": first_bad}


def check_rival(n, a, c):
    return (len(c) == 8 and all(type(x) is int and x >= 0 for x in c)
            and sum(c) == 8 and c != [1] * 8 and residue(c, a, n) == sum(a) % n)


def main():
    start = monotonic()
    pending = {}
    for filename in ("stage38_growth_experiment_results.json", "stage38_coset_experiment_results.json"):
        source = json.loads(Path(filename).read_text())
        for row in [*source["best"].values(), *source.get("controls", [])]:
            pending.setdefault((row["N"], tuple(row["A"])), []).append(row)
    cubic = json.loads(Path("stage38_cubic_probe_results.json").read_text())
    for row in cubic["zero_score_witnesses"]:
        pending.setdefault((row["N"], tuple(row["A"])), []).append({**row, "cubic_protected": True})
    results = []
    corruptions = 0
    for (n, a), saved in sorted(pending.items()):
        if monotonic() - start >= 30:
            raise TimeoutError("Witness audit incomplete; no completed output written")
        truth = audit(n, a)
        for row in saved:
            for k in truth:
                if k in row and k != "first_quartic_failure":
                    assert row[k] == truth[k], (n, k, row[k], truth[k])
            bad = row.get("first_quartic_failure")
            if bad:
                u = [bad["squarefree"].count(i) for i in range(8)]
                v = [bad["opponent"].count(i) for i in range(8)]
                assert len(set(bad["squarefree"])) == 4 and u != v
                assert sum(u) == sum(v) == 4
                assert residue(u, a, n) == residue(v, a, n) == bad["residue"]
            if row.get("rival"):
                c = row["rival"]
                assert check_rival(n, a, c)
                wrong = c.copy()
                wrong[0] += 1
                assert not check_rival(n, a, wrong)
                corruptions += 1
                wrong = c.copy()
                j = next(j for j in range(1, 8) if wrong[j] and a[j] != a[0])
                wrong[j] -= 1
                wrong[0] += 1
                assert sum(wrong) == 8 and not check_rival(n, a, wrong)
                corruptions += 1
        results.append(truth)
    by_key = {(r["N"], tuple(r["A"])): r for r in results}
    low = by_key[(245, (0, 1, 7, 21, 49, 84, 99, 140))]
    assert low["difference_count"] == 56 and low["periods4"] == [0]
    assert low["maximum_dilation_overlap"] == 3 and low["sumset4"] == 130
    c3 = by_key[(247, (0, 1, 3, 7, 15, 31, 63, 165))]
    assert c3["cubic_protected"] and c3["sumset3"] == 104 and c3["sumset4"] == 199
    assert c3["h"] == 12 and c3["R3"] == 0 and c3["maximum_dilation_overlap"] == 6
    warning = by_key[(251, tuple((1 << i) - 1 for i in range(8)))]
    assert warning["intersection_exact_Q"] and warning["squarefree4_distinct"] == 70 and not warning["valid8"]
    # Abstract reflection countermodel: no claim that it is an A-generated sumset.
    q0 = set(range(1, 36)) | set(range(212, 247))
    v0 = q0 | set(range(36, 124))
    assert len(q0) == 70 and len(v0) == 158
    assert v0 & {(-x) % 247 for x in v0} == q0
    assert v0 | {(-x) % 247 for x in v0} == set(range(1, 247))
    assert all({(x + d) % 247 for x in v0} != v0 for d in range(1, 247))
    # Sharpness of the validity-only incidence increment in an exponent-two group.
    def xor_sum(c):
        return sum((1 << (i - 1)) for i in range(1, 8) if c[i] % 2)
    xor3 = {xor_sum(c) for c in counts(3)}
    xor4 = {xor_sum(c) for c in counts(4)}
    xor8_matches = [c for c in counts(8) if xor_sum(c) == 127]
    assert xor8_matches == [(1,) * 8]
    assert len(xor3) == 64 and len(xor4) == 99
    out = {"completion": "COMPLETE_POSITIVE_WITNESS_AUDIT", "seconds_limit": 30,
           "elapsed_seconds": monotonic() - start, "distinct_witnesses_checked": len(results),
           "eight_multisets_checked": 6435 * len(results), "corrupted_rivals_rejected": corruptions,
           "producer_imported": False, "negative_search_certified": False,
           "new_modulus_exclusion": False,
           "abstract_reflection_model": {"N": 247, "V_size": 158, "intersection_size": 70, "periods": [0]},
           "exponent_two_sharpness_model": {"group": "(Z/2)^7", "valid8": True,
                "sumset3": 64, "sumset4": 99, "increment": 35, "eight_multisets_checked": 6435},
           "results": results}
    Path("stage38_independent_results.json").write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps({k: v for k, v in out.items() if k != "results"}, indent=2))
    print(json.dumps({"low_growth": low, "cubic_counterexample": c3}, indent=2))


if __name__ == "__main__":
    main()
