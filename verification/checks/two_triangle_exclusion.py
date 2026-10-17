"""Separate exact implementation of targeted single-class proof closure.

Standard library plus the existing Stage60 checker. No producer or search
imports. It independently reconstructs partitions, credits and coverage.
"""

from collections import Counter, defaultdict
from itertools import combinations, combinations_with_replacement, permutations
from pathlib import Path
import gzip, hashlib, json
import alignment_forests as C

ROOTS = {"3221": [[-4, 0, 0, 1, 0]], "4211": [[-4, 1, 0, 0, 0]], "22211": []}
PERMS = tuple((p + q for p in permutations(range(3)) for q in ((3, 4), (4, 3))))
WORDS = {
    d: tuple(
        (C.counts(labels) for labels in combinations_with_replacement(range(8), d))
    )
    for d in (3, 4, 5)
}
ORD = {
    d: tuple((w for w in WORDS[d] if w.count(2) == 1 and max(w) == 2))
    for d in (3, 4, 5)
}


def partitions(value, d, ordinary=False):
    G = defaultdict(list)
    for w in ORD[d] if ordinary else WORDS[d]:
        G[value(w)].append(w)
    return list(G.values())


def profile(W, d):
    centers = {w.index(2) for w in W}
    tails = [{i for i, n in enumerate(w) if n == 1} for w in W]
    if len(centers) != 3 or any((centers & T for T in tails)):
        return None
    edges = tails if d == 4 else [set(range(8)) - centers - T for T in tails]
    return sorted(Counter((i for E in edges for i in E)).values())


def inventory(value, prior_two=False):
    zero = value((0,) * 8)
    cubes = [G for G in partitions(value, 3) if max(G[0]) > 1]
    assert all((all((max(w) > 1 for w in G)) for G in cubes))
    assert all((len(G) <= 3 for G in cubes))
    P = sum(
        (
            sum((max(w) == 2 for w in G)) * (sum((max(w) == 2 for w in G)) - 1) // 2
            for G in cubes
        )
    )
    R = sum(((len(G) - 1) * (len(G) - 2) // 2 for G in cubes))
    c = sum((sum((max(w) == 2 for w in G)) == 3 for G in cubes))
    h = 28 - sum((len(G) * (len(G) - 1) // 2 for G in cubes))
    colors = defaultdict(list)
    for i in range(8):
        for j in range(8):
            if i != j:
                colors[
                    value(tuple((2 * int(k == i) - int(k == j) for k in range(8))))
                ].append((i, j))
    triangles = [
        E
        for edges in colors.values()
        for E in combinations(edges, 3)
        if len({i for e in E for i in e}) == 6
    ]
    F = {tuple(sorted(e)) for E in triangles for e in E}
    D = defaultdict(list)
    for ti, E in enumerate(triangles):
        for (i, a), (j, b) in combinations(E, 2):
            D[tuple(sorted((C.counts((i, i, b)), C.counts((j, j, a)))))].append(ti)
    quartic = partitions(value, 4, True)
    quintic = partitions(value, 5, True)
    assert all((len(G) <= 3 for G in quartic + quintic))
    E0 = []
    U0 = []
    w0 = []
    q0 = []
    bad = False
    inside = 0
    for G in quartic:
        if len(G) == 3 and profile(G, 4) == [1, 1, 1, 1, 2]:
            w0.append(G)
        if len(G) != 2:
            continue
        tails = [{i for i, n in enumerate(w) if n == 1} for w in G]
        centers = {w.index(2) for w in G}
        if (
            len(centers) == 2
            and (not tails[0] & tails[1])
            and (not any((T & centers for T in tails)))
        ):
            E0.append(G)
            if tuple(sorted(centers)) in F:
                U0.append(G)
    for G in quintic:
        if len(G) != 3 or profile(G, 5) != [1, 1, 1, 1, 2]:
            continue
        q0.append(G)
        tails = [{i for i, n in enumerate(w) if n == 1} for w in G]
        found = 0
        for i, j in combinations(range(3), 2):
            common = tails[i] & tails[j]
            if len(common) == 1 and tuple(sorted((G[i].index(2), G[j].index(2)))) in F:
                bad = True
            if len(common) == 2:
                found += 1
                pair = tuple(
                    sorted(
                        (
                            tuple((n - int(k in common) for k, n in enumerate(G[z])))
                            for z in (i, j)
                        )
                    )
                )
                if pair in D:
                    inside += 1
                if len(D.get(pair, [])) >= 2:
                    bad = True
        assert found == 1
    if inside >= 2:
        bad = True
    primary = colors[zero]
    succ = dict(primary)
    pred = {j: i for i, j in primary}
    assert len(succ) == len(pred) == len(primary)
    paths = []
    seen = set()
    for i in range(8):
        if i in pred:
            continue
        path = [i]
        while path[-1] in succ:
            path.append(succ[path[-1]])
            assert path[-1] not in path[:-1]
        paths.append(path)
        seen.update(path)
    assert seen == set(range(8))
    lengths = {i: len(path) for path in paths for i in path}
    differences = {
        value(tuple((int(k == i) - int(k == j) for k in range(8))))
        for i in range(8)
        for j in range(8)
        if i != j
    }
    directed = {e for E in triangles for e in E}
    assert directed <= set(primary)
    opened = [
        e
        for e in directed
        if value(tuple((2 * int(k == e[0]) - 2 * int(k == e[1]) for k in range(8))))
        not in differences
    ]
    assert all((j not in succ for i, j in opened))
    isolated = [path[0] for path in paths if len(path) == 1]
    available = [
        i for i in isolated if all((value(C.counts((i, j))) != zero for j in range(8)))
    ]
    ell = sum((lengths[i] >= 3 for i, j in opened))
    o = max(ell, len(opened) - len(available))
    t = len(triangles)
    assert 1 <= t <= 2 and len(primary) <= 4
    tmax = 1 if prior_two else t if len(primary) == 4 else 2
    qmax = min(h - len(opened), 4 * (P - len(D)) + 1, 4 * P - 11 * c)
    assert qmax >= 0
    robust = 288 - qmax + R + 2 * c + 2 * len(w0) - 2 * t - 2 * P
    lower = max(
        36 + R + len(q0),
        77 + 2 * R + 2 * c + 2 * o - 2 * t - 2 * P,
        (
            75
            + 4 * R
            + 2 * c
            - 5 * t
            + 4 * o
            + max(len(E0) + 5 * len(w0), 80 + t + 2 * c - 4 * P + 4 * len(w0))
        )
        // 2,
    )
    return {
        "P": P,
        "R": R,
        "c": c,
        "t": t,
        "triangles": triangles,
        "bad": bad,
        "q0": len(q0),
        "robust": robust,
        "conditional_target": 192 - lower,
        "unconditional_target": 156 - R - len(q0),
        "credit": 2 + 2 * (o + R + c) + 5 * len(w0) + len(U0) - 5 * t,
        "global_credit": 2 + 2 * (R + c) + 5 * len(w0) - 5 * tmax,
        "primary_edges": len(primary),
    }


def main():
    path = Path(__file__).with_name("two-triangle-class.json.gz")
    raw = path.read_bytes()
    d = json.loads(gzip.decompress(raw))
    stats = Counter()
    pairs = 0
    private = 0
    literal = 0
    completed = []
    sizes = []
    M = (
        (1, 0, 0, 0),
        (2, 0, 0, 0),
        (0, 1, 0, 0),
        (0, 2, 0, 0),
        (0, 0, 1, 0),
        (0, 0, 2, 0),
        (4, 0, 0, 0),
        (0, 0, 0, 1),
    )
    for j in (2, 4):
        other = 4 if j == 2 else 2
        R = C.counts((6, 6, other, other, other, 7, 7, 7))
        delta = C.val(C.sub(R, C.ONES), M)
        eq = tuple((3 * int(i == j) - int(i == 0) - 2 * int(i == 7) for i in range(8)))
        assert delta == tuple((-x for x in C.val(eq, M)))
        W = (
            C.counts((1, 1, 3 if j == 4 else 5, j, j + 1)),
            C.counts((2 if j == 4 else 4,) * 2 + (6, j, j + 1)),
            C.counts((0, 0, 6, 7, 3 if j == 4 else 5)),
        )
        for w in W:
            C.ordinary(w, 5)
        tails = [{i for i, n in enumerate(w) if n == 1} for w in W]
        assert len(tails[0] & tails[2]) == 1 and {W[0].index(2), W[2].index(2)} == {
            0,
            1,
        }
        eq = tuple((3 * int(i == j) - 2 * int(i == 0) - int(i == 7) for i in range(8)))
        assert C.val(C.sub(W[0], W[2]), M) == C.val(eq, M)

    def positive(p, value, orders, target):
        nonlocal pairs
        if p["kind"] == "rival":
            W = tuple(p["word"])
            C.word(W, 8)
            assert W != C.ONES and value(W) == value(C.ONES)
            return
        assert p["kind"] == "positive"
        degree = p["degree"]
        W = [tuple(w) for w in p["words"]]
        assert degree in (4, 5) and len(W) >= target and (len(set(W)) == len(W))
        for w in W:
            C.word(w, degree)
            assert max(w) > 1
        V = [value(w) for w in W]
        for i, j in combinations(range(len(W)), 2):
            delta = (
                tuple((x - y for x, y in zip(V[i][0], V[j][0]))),
                tuple(((x - y) % g for x, y, g in zip(V[i][1], V[j][1], orders))),
            )
            r, k, f = p["witnesses"][json.dumps(delta, separators=(",", ":"))]
            R = tuple(r)
            C.word(R, 8)
            assert R != C.ONES and isinstance(k, int) and C.unit2(f)
            rv = value(C.sub(R, C.ONES))
            assert tuple((f * x for x in rv[0])) == tuple((k * x for x in delta[0]))
            assert all(
                ((f * x - k * y) % g == 0 for x, y, g in zip(rv[1], delta[1], orders))
            )
            pairs += 1

    for comp in d["components"]:
        shape = comp["shape"]
        nodes = comp["nodes"]
        root = comp["root"]
        done = set()
        active = set()
        assert (
            shape in ROOTS
            and shape not in completed
            and (nodes[root]["constraints"] == ROOTS[shape])
        )
        prior = "3221" in completed

        def check(i):
            nonlocal private, literal
            if i in done:
                return
            assert i not in active
            active.add(i)
            n = nodes[i]
            K = n["constraints"]
            r = n["reduction"]
            m = n["model"]
            p = n["proof"]
            kind = p["kind"]
            stats[kind] += 1
            if K:
                C.reduction(K, r)
            else:
                assert (
                    r["rank"] == 0
                    and r["D"] == []
                    and (r["left"] == [])
                    and (
                        r["right"]
                        == [[int(i == j) for j in range(5)] for i in range(5)]
                    )
                )
            C.check_model(m, r)
            value = C.evaluator(m)
            if kind == "direct":
                e = p["exclusion"]
                if e["kind"] == "uniform_alignment_cap5":
                    E = [tuple(x) for x in e["edges"]]
                    assert len(E) == len(set(E)) == 5
                    assert (
                        len(
                            {
                                value(
                                    tuple(
                                        (
                                            2 * int(k == a) - int(k == b)
                                            for k in range(8)
                                        )
                                    )
                                )
                                for a, b in E
                            }
                        )
                        == 1
                    )
                else:
                    C.direct(e, value)
            elif kind == "interaction":
                T = p["exclusion"]["triangles"]
                assert len(T) == 2
                for E in T:
                    assert len(E) == 3 and len({i for e in E for i in e}) == 6
                    assert (
                        len(
                            {
                                value(
                                    tuple(
                                        (
                                            2 * int(k == a) - int(k == b)
                                            for k in range(8)
                                        )
                                    )
                                )
                                for a, b in E
                            }
                        )
                        == 1
                    )
                assert len({tuple(e) for E in T for e in E}) >= 5
            elif kind == "rival":
                positive(p, value, m["torsion_orders"], 0)
            elif kind == "positive":
                positive(
                    p,
                    value,
                    m["torsion_orders"],
                    (
                        89
                        if p["degree"] == 4
                        else inventory(value, prior)["unconditional_target"]
                    ),
                )
            else:
                Q = inventory(value, prior)
                if kind == "split_guard":
                    assert Q["bad"]
                elif kind == "global_credit":
                    assert Q["global_credit"] > 0
                elif kind == "prior_two_triangle":
                    assert prior and Q["t"] == 2
                elif kind == "prior_four_edge":
                    assert "4211" in completed and Q["primary_edges"] == 4
                elif kind == "forced_ordinary":
                    reason = p["reason"]
                    if reason == "P9":
                        assert Q["P"] <= 8
                    elif reason == "robust_count":
                        assert Q["robust"] >= 248
                    elif reason == "credit":
                        assert Q["credit"] > 0
                    else:
                        assert reason == "conditional_quintic"
                        positive(
                            p["quintic"],
                            value,
                            m["torsion_orders"],
                            Q["conditional_target"],
                        )
                    expected, lc = C.coverage(value)
                    literal += lc
                    seen = set()
                    for case in p["coverage"]:
                        row = tuple(case["direction"])
                        assert row in expected and row not in seen
                        seen.add(row)
                        private += 1
                        C.reduction(K + [list(row)], case["reduction"])
                        perm = tuple(case["permutation"])
                        assert perm in PERMS
                        j = case["node"]
                        assert 0 <= j < len(nodes) and j != i
                        assert all(
                            (
                                C.forced([z[a] for a in perm], case["reduction"])
                                for z in nodes[j]["constraints"]
                            )
                        )
                        check(j)
                    assert seen == expected
                else:
                    raise AssertionError(kind)
            active.remove(i)
            done.add(i)

        check(root)
        assert len(done) == len(nodes)
        completed.append(shape)
        sizes.append(len(done))
    result = {
        "checked_shapes": completed,
        "nodes": sizes,
        "proof_types": dict(stats),
        "private_directions": private,
        "literal_private_pairs": literal,
        "positive_mass8_identities": pairs,
        "archive_sha256": hashlib.sha256(raw).hexdigest(),
        "component_complete": set(completed) == {"3221"},
        "component_scope": "Two-triangle class only; the closing argument handles the other two small forests.",
        "checker": "Separate implementation by same assistant; not external or formal review.",
    }
    Path("two-triangle-report.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
