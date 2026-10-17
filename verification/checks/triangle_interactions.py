"""Separate implementation checking the complete triangle interaction.

Imports only standard-library code and the existing Stage60 checker,
never a producer or elimination helper. Coverage of second triangles
uses all ordered eight-label frames. No search is performed.
"""

from collections import Counter
from itertools import combinations, permutations
from pathlib import Path
import gzip, hashlib, json
import alignment_forests as C

ALT = [[1, 4, -5, 0, 0], [0, 20, -21, 0, 1]]
PERMS = tuple((p + q for p in permutations(range(3)) for q in ((3, 4), (4, 3))))


def main():
    path = Path(__file__).with_name("interactions.json.gz")
    raw = C.archive_bytes(path)
    data = json.loads(gzip.decompress(raw))
    stats = Counter()
    pairids = 0
    private_cases = 0
    literal_private = 0
    active = []

    def component(comp, root=None):
        nonlocal pairids, private_cases, literal_private
        nodes = comp["nodes"]
        done = set()
        visiting = set()

        def check_forward(case, K):
            C.reduction(K, case["reduction"])
            p = tuple(case["permutation"])
            assert p in PERMS
            n = case["node"]
            assert 0 <= n < len(nodes)
            assert all(
                (
                    C.forced([row[j] for j in p], case["reduction"])
                    for row in nodes[n]["constraints"]
                )
            )
            check_node(n)

        def check_affine(e, value, K):
            frame = e["frame"]
            assert sorted(frame) == list(range(8))
            x, a = e["alignment_edge"]
            assert (x, a) == tuple(frame[:2])
            gamma = tuple((2 * int(i == x) - int(i == a) for i in range(8)))
            zero = value((0,) * 8)
            for j in (0, 2, 4):
                edge = tuple(
                    (
                        2 * int(i == frame[j]) - int(i == frame[j + 1]) - gamma[i]
                        for i in range(8)
                    )
                )
                assert value(edge) == zero
            Y = [
                tuple((int(i == frame[j]) - gamma[i] for i in range(8)))
                for j in (0, 2, 4, 6, 7)
            ]
            assert all(
                (
                    value(
                        tuple(
                            (
                                sum((row[j] * Y[j][i] for j in range(5)))
                                for i in range(8)
                            )
                        )
                    )
                    == zero
                    for row in K
                )
            )

        def positive(p, value, orders):
            nonlocal pairids
            W = [tuple(w) for w in p["words"]]
            assert len(W) == 89 and len(set(W)) == 89
            for w in W:
                C.word(w, 4)
                assert max(w) > 1
            V = [value(w) for w in W]
            for i, j in combinations(range(89), 2):
                d = (
                    tuple((x - y for x, y in zip(V[i][0], V[j][0]))),
                    tuple(((x - y) % g for x, y, g in zip(V[i][1], V[j][1], orders))),
                )
                raw, k, f = p["witnesses"][json.dumps(d, separators=(",", ":"))]
                R = tuple(raw)
                C.word(R, 8)
                assert R != C.ONES and isinstance(k, int) and C.unit2(f)
                rv = value(C.sub(R, C.ONES))
                assert tuple((f * x for x in rv[0])) == tuple((k * y for y in d[0]))
                assert all(
                    ((f * x - k * y) % g == 0 for x, y, g in zip(rv[1], d[1], orders))
                )
                pairids += 1

        def check_node(i):
            nonlocal private_cases, literal_private
            if i in done:
                return
            assert i not in visiting
            visiting.add(i)
            n = nodes[i]
            K = n["constraints"]
            r = n["reduction"]
            m = n["model"]
            C.reduction(K, r)
            C.check_model(m, r)
            value = C.evaluator(m)
            p = n["proof"]
            kind = p["kind"]
            stats[kind] += 1
            if kind == "direct":
                e = p["exclusion"]
                t = e["kind"]
                if t == "uniform_alignment_cap5":
                    E = [tuple(edge) for edge in e["edges"]]
                    assert len(E) == 5 and len(set(E)) == 5
                    assert all((0 <= i < 8 and 0 <= j < 8 and (i != j) for i, j in E))
                    assert (
                        len(
                            {
                                value(
                                    tuple(
                                        (
                                            2 * int(k == i) - int(k == j)
                                            for k in range(8)
                                        )
                                    )
                                )
                                for i, j in E
                            }
                        )
                        == 1
                    )
                elif t == "affine_alternating_family":
                    check_affine(e, value, ALT)
                else:
                    C.direct(e, value)
            elif kind == "rival":
                R = tuple(p["word"])
                C.word(R, 8)
                assert R != C.ONES and value(R) == value(C.ONES)
            elif kind == "positive89":
                positive(p, value, m["torsion_orders"])
            elif kind == "forced_ordinary":
                P = sum((value(a) == value(b) for a, b in combinations(C.ORD, 2)))
                assert P <= 8
                expected, literal = C.coverage(value)
                literal_private += literal
                seen = set()
                for case in p["coverage"]:
                    d = tuple(case["direction"])
                    assert d in expected and d not in seen
                    seen.add(d)
                    check_forward(case, K + [list(d)])
                    private_cases += 1
                assert seen == expected
            elif kind == "affine_target":
                target = p["target"]
                if target == "alternating":
                    check_affine(p, value, ALT)
                else:
                    assert 0 <= target < len(nodes) and target != i
                    check_affine(p, value, nodes[target]["constraints"])
                    check_node(target)
            else:
                raise AssertionError(kind)
            visiting.remove(i)
            done.add(i)

        if root is not None:
            check_node(root)
        else:
            expected = {
                tuple(sorted(((x, a), (y, b), (z, c))))
                for x, a, y, b, z, c, p, q in permutations(range(8))
            }
            assert len(expected) == 3360
            seen = set()
            for case in comp["triangle_cases"]:
                E = tuple((tuple(e) for e in case["edges"]))
                signature = tuple(sorted(E))
                assert signature in expected and signature not in seen
                seen.add(signature)
                rows = [
                    tuple((2 * int(k == i) - int(k == j) for k in range(8)))
                    for i, j in E
                ]
                gamma = C.val(rows[0], C.BASE)
                K = [list(C.val(C.sub(rows[0], row), C.BASE)) for row in rows[1:]]
                K = [row for row in K if any(row)]
                kind = case["kind"]
                stats[kind] += 1
                if kind == "same_class_formal":
                    assert not K and (not any(gamma))
                elif kind == "same_class_forced":
                    C.reduction(K, case["reduction"])
                    assert C.forced(gamma, case["reduction"])
                else:
                    assert kind == "distinct_class"
                    check_forward(case, K)
            assert seen == expected
        active.append(len(done))

    A = data["alternating"]
    assert A["nodes"][A["root"]]["constraints"] == ALT
    component(A, A["root"])
    component(data["coupling"])
    result = {
        "scope": "At most one quartic-triangle alignment class in a hypothetical odd N<248 counterexample.",
        "archive_sha256": hashlib.sha256(raw).hexdigest(),
        "checked_nodes": active,
        "proof_types": dict(stats),
        "second_triangle_presentations": 3360,
        "private_direction_cases": private_cases,
        "literal_private_cases": literal_private,
        "positive_mass8_pair_identities": pairids,
        "boundary": "Separate implementation using the existing Stage60 checker helpers and its four-edge theorem; no producer/elimination imports.",
    }
    Path(__file__).with_name("triangle-interactions-report.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    print(json.dumps(result))


if __name__ == "__main__":
    main()
