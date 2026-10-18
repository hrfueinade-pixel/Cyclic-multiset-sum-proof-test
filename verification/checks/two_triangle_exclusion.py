"""Verify the two-triangle component with only its active leaf contracts.

Uses alignment_forests arithmetic helpers. Every refinement is forced by
P<=8 and covers all new private ordinary cubic equalities. No conditional
quintic-credit leaf is accepted.
"""

from collections import Counter, defaultdict
from itertools import combinations, combinations_with_replacement, permutations
from pathlib import Path
import gzip, hashlib, json
import alignment_forests as C

ROOTS = {"3221": [[-4, 0, 0, 1, 0]]}
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


def unconditional_credit(value):
    """Persistent R3, cubic triples and quartic splits; actual t<=2."""
    cubes = [G for G in partitions(value, 3) if max(G[0]) > 1]
    assert all(all(max(w) > 1 for w in G) and len(G) <= 3 for G in cubes)
    R = sum((len(G) - 1) * (len(G) - 2) // 2 for G in cubes)
    c = sum(sum(max(w) == 2 for w in G) == 3 for G in cubes)
    quartic = partitions(value, 4, True)
    assert all(len(G) <= 3 for G in quartic)
    w = sum(len(G) == 3 and profile(G, 4) == [1, 1, 1, 1, 2] for G in quartic)
    return 2 + 2 * (R + c) + 5 * w - 10


def shared_triangle_split(value):
    """A descent in two triangles cannot support a genuine split."""
    colors = defaultdict(list)
    for i in range(8):
        for j in range(8):
            if i != j:
                colors[value(tuple(2 * (k == i) - (k == j) for k in range(8)))].append(
                    (i, j)
                )
    descents = Counter()
    for edges in colors.values():
        for triangle in combinations(edges, 3):
            if len({i for edge in triangle for i in edge}) != 6:
                continue
            for (i, a), (j, b) in combinations(triangle, 2):
                descents[tuple(sorted((C.counts((i, i, b)), C.counts((j, j, a)))))] += 1
    for G in partitions(value, 5, True):
        if len(G) != 3 or profile(G, 5) != [1, 1, 1, 1, 2]:
            continue
        for a, b in combinations(G, 2):
            common = {i for i in range(8) if a[i] == b[i] == 1}
            if len(common) == 2:
                pair = tuple(
                    sorted(
                        tuple(n - (i in common) for i, n in enumerate(word))
                        for word in (a, b)
                    )
                )
                if descents[pair] >= 2:
                    return True
    return False


def require_ordinary_refinement(proof, value):
    assert proof.get("reason") == "P9", "Unreviewed conditional leaf"
    assert sum(value(a) == value(b) for a, b in combinations(ORD[3], 2)) <= 8


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
                assert (
                    p["degree"] == 4
                ), "Only unconditional quartic separation is shipped"
                positive(p, value, m["torsion_orders"], 89)
            elif kind == "split_guard":
                assert shared_triangle_split(value)
            elif kind == "global_credit":
                assert unconditional_credit(value) > 0
            elif kind == "forced_ordinary":
                require_ordinary_refinement(p, value)
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
