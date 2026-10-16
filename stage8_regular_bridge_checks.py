"""Bounded algebra and support checks for the h=R3=0 quartic bridge.

The sixteen certificates use exact rational arithmetic with ONLY powers
of two as denominators. The support check considers at most 4096 masks
per fixed support size. Seven fixed valid fixtures are independently
enumerated through all 6435 degree-eight multisets. No modulus sweep,
random sampling, external packages, or inference of a theorem from tests.
"""

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, combinations_with_replacement
import json
from pathlib import Path


def add(*vectors):
    return tuple(sum(v[i] for v in vectors) for i in range(len(vectors[0])))


def scale(k, v):
    return tuple(k * x for x in v)


def pure_chain_certificates():
    # Coefficients of (z,a,b,c,E); all rows represent zero relations.
    r1 = (4, -3, -1, 0, 0)
    r2 = (4, 0, -3, -1, 0)
    r3 = (-6, 5, 0, 0, 1)
    e_is_b = (0, 0, -1, 0, 1)
    e_is_c = (0, 0, 0, -1, 1)
    assert add(r3, scale(2, r1), scale(-1, r2)) == (-2, -1, 1, 1, 1)
    assert add(e_is_b, scale(-1, r1), scale(-1, r3)) == (2, -2, 0, 0, 0)
    assert add(scale(Fraction(3, 2), r1), scale(Fraction(-1, 2), r2),
               scale(Fraction(1, 2), r3), scale(Fraction(-1, 2), e_is_c)) == (1, -2, 0, 1, 0)
    return {"identities_checked": 3,
            "conclusions": ["E+b+c=2z+a", "E=b implies 2z=2a", "E=c implies c+z=2a"]}


def sixteen_cases():
    # Coordinates are coefficients of (B,Q,P), in that order.
    points = {"b": (1, 0, 0), "p": (0, 0, 1), "c": (3, 0, -2),
              "u": (0, 0, 0), "v": (0, 2, 0), "w": (4, 0, 0),
              "r": (2, -1, 0), "s": (0, -1, 0)}
    rows_r = [(-5, 2, 2), (-5, 4, 2), (-7, 2, 4), (-7, 4, 4)]
    rows_s = [(-1, 4, 2), (3, 2, 2), (-3, 4, 4), (1, 2, 4)]
    witnesses = [
        [("r", "w"), ("b", "u"), ("ww", "ub"), ("pw", "bu")],
        [("b", "u"), ("bb", "rw"), ("pb", "uu"), ("rpb", "uuu")],
        [("bw", "pr"), ("pu", "bw"), ("r", "w"), ("b", "u")],
        [("pb", "uw"), ("rw", "pb"), ("b", "u"), ("bb", "rw")],
    ]
    records = []
    for i, row_r in enumerate(rows_r):
        for j, row_s in enumerate(rows_s):
            left, right = witnesses[i][j]
            assert len(left) == len(right)
            assert left != right
            if len(left) >= 3:
                assert len(set(left)) == len(left)
            difference = add(*(points[k] for k in left),
                             *(scale(-1, points[k]) for k in right))
            certificate = None
            for a, b in combinations(range(3), 2):
                det = row_r[a] * row_s[b] - row_r[b] * row_s[a]
                if not det:
                    continue
                lam = Fraction(difference[a] * row_s[b] - difference[b] * row_s[a], det)
                mu = Fraction(row_r[a] * difference[b] - row_r[b] * difference[a], det)
                if add(scale(lam, row_r), scale(mu, row_s)) == difference:
                    certificate = lam, mu
                    break
            assert certificate is not None
            assert all(x.denominator & (x.denominator - 1) == 0 for x in certificate)
            records.append({"R_case": i + 1, "S_case": j + 1,
                            "R_row": row_r, "S_row": row_s,
                            "left": list(left), "right": list(right),
                            "difference": difference,
                            "row_coefficients": list(map(str, certificate))})
    assert len(records) == 16
    return records


def one_ordinary_supports():
    counts = Counter()
    examples = {}
    for k in (3, 4, 5):
        ordinary = (0, 0, 1, 2)
        vertices = [tuple(sorted((a, a, a, b)))
                    for a in range(1, k) for b in range(1, k) if a != b]
        assert len(vertices) <= 12
        for mask in range(1 << len(vertices)):
            counts["masks_examined"] += 1
            chosen = [ordinary] + [v for i, v in enumerate(vertices) if mask >> i & 1]
            support = [set(v) for v in chosen]
            if set.union(*support) != set(range(k)):
                continue
            # A 31 on the ordinary tail pair forces equality of doubled centers.
            if any(s == {1, 2} for s in support[1:]):
                continue
            centers = [next(x for x, m in Counter(v).items() if m == 3)
                       for v in chosen[1:]]
            if len(set(centers)) != len(centers):
                continue
            if len({tuple(sorted(s)) for s in support[1:]}) != len(support) - 1:
                continue
            graph = [{j for j, t in enumerate(support) if i != j and s & t}
                     for i, s in enumerate(support)]
            if any(not n or len(n) > 2 for n in graph):
                continue
            seen, pending = {0}, [0]
            while pending:
                i = pending.pop()
                for j in graph[i] - seen:
                    seen.add(j)
                    pending.append(j)
            if len(seen) != len(chosen):
                continue
            if any(set.intersection(*(support[i] for i in indices))
                   for indices in combinations(range(len(chosen)), 3)):
                continue
            unpaired = []
            legal = True
            for i, neighbors in enumerate(graph):
                if len(neighbors) != 1:
                    continue
                j = next(iter(neighbors))
                common = support[i] & support[j]
                assert len(common) == 1
                label = next(iter(common))
                if i:
                    c = centers[i - 1]
                    singleton = next(x for x, m in Counter(chosen[i]).items() if m == 1)
                    if label != singleton:
                        legal = False
                        break
                else:
                    c = 0
                unpaired.append((c, label))
            if not legal or len({label for _, label in unpaired}) != len(unpaired):
                continue
            m = len(chosen) - 1
            if m == 2 and not support[1] & support[2]:
                category = "five-point disjoint-31 path"
                assert k == 5
            elif m == 2 and all(len(n) == 2 for n in graph):
                category = "four-point triangle"
                assert k == 4
            elif m == 2:
                category = "five-point adjacent-31 path"
                assert k == 5
            elif m == 3:
                category = "five-point four-cycle"
                assert k == 5 and all(len(n) == 2 for n in graph)
            else:
                raise AssertionError((k, chosen, graph))
            counts[category] += 1
            examples.setdefault(category, chosen)
    assert set(examples) == {"five-point disjoint-31 path", "four-point triangle",
                             "five-point adjacent-31 path", "five-point four-cycle"}
    return {"counts": dict(counts), "representative_patterns": examples,
            "scope": "Support incidence only, not realizable cyclic sets or affine classes."}


def fixed_fixtures():
    binary = tuple((1 << i) - 1 for i in range(8))
    fixtures = [(binary, 255), (binary, 256),
                ((0, 1, 129, 131, 135, 143, 159, 191), 254),
                ((0, 1, 13, 169, 2043, 2197, 28561, 28719), 229753),
                ((0, 4609, 4610, 4626, 4898, 9248, 9522, 9792), 78337),
                ((0, 209956, 52490, 209957, 209965, 52570, 210685, 59050), 262445),
                ((0, 9487369, 18974739, 18974742, 33, 1089, 35937, 1185921), 28462107)]
    results = []
    for a, n in fixtures:
        hits = [u for u in combinations_with_replacement(range(8), 8)
                if sum(a[i] for i in u) % n == sum(a) % n]
        assert hits == [tuple(range(8))]
        delta = {(x - y) % n for x in a for y in a if x != y}
        assert len(delta) == 56
        assert len({(x + y) % n for x, y in combinations_with_replacement(a, 2)}) == 36
        h = sum(2 * d % n not in delta for d in delta) // 2
        cubes = defaultdict(list)
        for u in combinations_with_replacement(range(8), 3):
            if len(set(u)) < 3:
                cubes[sum(a[i] for i in u) % n].append(u)
        r3 = sum((len(f) - 1) * (len(f) - 2) // 2 for f in cubes.values())
        quartics = [u for u in combinations_with_replacement(range(8), 4)
                    if len(set(u)) < 4]
        assert len(quartics) == 260
        index = {v: i for i, v in enumerate(quartics)}
        graph = [set() for _ in quartics]
        for fiber in cubes.values():
            for u, v in combinations(fiber, 2):
                for z in range(8):
                    i = index[tuple(sorted(u + (z,)))]
                    j = index[tuple(sorted(v + (z,)))]
                    graph[i].add(j)
                    graph[j].add(i)
        component, supports = {}, []
        for root in range(260):
            if root in component:
                continue
            identifier = len(supports)
            used, pending = set(), [root]
            component[root] = identifier
            while pending:
                i = pending.pop()
                used.update(quartics[i])
                for j in graph[i]:
                    if j not in component:
                        component[j] = identifier
                        pending.append(j)
            supports.append(used)
        fibers = defaultdict(list)
        for i, u in enumerate(quartics):
            fibers[sum(a[j] for j in u) % n].append(i)
        local_pure_checks = 0
        for f in fibers.values():
            pure = [quartics[i][0] for i in f if len(set(quartics[i])) == 1]
            triples = [quartics[i] for i in f if sorted(Counter(quartics[i]).values()) == [1, 3]]
            for z in pure:
                for left, right in combinations(triples, 2):
                    if z in set(left) | set(right) or not set(left) & set(right):
                        continue
                    center_l = next(i for i, m in Counter(left).items() if m == 3)
                    center_r = next(i for i, m in Counter(right).items() if m == 3)
                    single_l = next(i for i, m in Counter(left).items() if m == 1)
                    single_r = next(i for i, m in Counter(right).items() if m == 1)
                    if single_l == single_r:
                        closed = all(2 * (a[z] - a[c]) % n in delta
                                     for c in (center_l, center_r))
                    elif single_l == center_r:
                        closed = 2 * (a[z] - a[center_l]) % n in delta
                    elif single_r == center_l:
                        closed = 2 * (a[z] - a[center_r]) % n in delta
                    else:
                        raise AssertionError("Overlapping distinct 31s have a shared singleton or form a chain")
                    local_pure_checks += 1
                    assert not (n % 2 and closed)
        for f in fibers.values():
            ids = {component[i] for i in f}
            for i, j in combinations(ids, 2):
                assert not supports[i] & supports[j]
        ordinary_fresh = sum(
            len({component[i] for i in f if len(set(quartics[i])) == 3}) > 1
            for f in fibers.values())
        d = len(supports) - len(fibers)
        if n % 2 and h == r3 == 0:
            assert d == ordinary_fresh == 0
        results.append({"N": n, "A": a, "valid_multisets_checked": 6435,
                        "h": h, "R3": r3, "D": d,
                        "ordinary_fresh_fibers": ordinary_fresh,
                        "pure_overlapping_31_local_controls": local_pure_checks,
                        "regular_odd_hypotheses": bool(n % 2 and h == r3 == 0)})
    return results


def main():
    result = {"sixteen_exact_algebra_certificates": sixteen_cases(),
              "pure_chain_exact_certificates": pure_chain_certificates(),
              "one_ordinary_component_patterns": one_ordinary_supports(),
              "fixed_valid_fixtures": fixed_fixtures(),
              "scope": "Proof bookkeeping; six reused fixtures and one non-h0 CRT control; no search."}
    Path("stage8_regular_bridge_results.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(json.dumps({"algebra_cases": 16,
                      "support_patterns": result["one_ordinary_component_patterns"],
                      "fixed_valid_fixtures": result["fixed_valid_fixtures"],
                      "scope": result["scope"]}, indent=2))


if __name__ == "__main__":
    main()
