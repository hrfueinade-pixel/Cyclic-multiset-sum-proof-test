"""Standalone checker for the triangle/paired-source ownership lemma.

Standard library only. Imports no producer, eliminator or prior checker.
Coverage uses all ordered canonical eight-label frames, rather than the
producer's shared-source construction. No search or timeout is a premise.
"""

from itertools import combinations, permutations
from pathlib import Path
import gzip, hashlib, json

BASE = (
    (1, 0, 0, 0, 0),
    (2, 0, 0, 0, 0),
    (0, 1, 0, 0, 0),
    (0, 2, 0, 0, 0),
    (0, 0, 1, 0, 0),
    (0, 0, 2, 0, 0),
    (0, 0, 0, 1, 0),
    (0, 0, 0, 0, 1),
)
PERMS = ((0, 1, 2, 3, 4), (0, 1, 2, 4, 3), (0, 2, 1, 3, 4), (0, 2, 1, 4, 3))
ONES = (1,) * 8


def counts(labels):
    return tuple((labels.count(i) for i in range(8)))


def sub(a, b):
    return tuple((x - y for x, y in zip(a, b)))


def relation(w):
    return tuple((sum((w[i] * BASE[i][j] for i in range(8))) for j in range(5)))


def mul(a, b):
    return [[sum((x * y for x, y in zip(r, c))) for c in zip(*b)] for r in a]


def determinant(a):
    n = len(a)
    a = [list(r) for r in a]
    sign = 1
    last = 1
    if n == 0:
        return 1
    for p in range(n - 1):
        if not a[p][p]:
            j = next((j for j in range(p + 1, n) if a[j][p]), None)
            if j is None:
                return 0
            a[p], a[j] = (a[j], a[p])
            sign = -sign
        pivot = a[p][p]
        for i in range(p + 1, n):
            for j in range(p + 1, n):
                numerator = a[i][j] * pivot - a[i][p] * a[p][j]
                assert numerator % last == 0
                a[i][j] = numerator // last
            a[i][p] = 0
        last = pivot
    return sign * a[-1][-1]


def unit2(x):
    return x > 0 and x & x - 1 == 0


def reduction(K, r):
    m = len(K)
    L = r["left"]
    V = r["right"]
    D = r["D"]
    rank = r["rank"]
    assert all((len(row) == 5 for row in K))
    assert len(L) == m and all((len(row) == m for row in L))
    assert len(V) == 5 and all((len(row) == 5 for row in V))
    assert abs(determinant(L)) == abs(determinant(V)) == 1
    assert mul(mul(L, K), V) == D
    assert 0 < rank <= min(m, 5)
    for i, row in enumerate(D):
        for j, x in enumerate(row):
            assert x == 0 if i != j or i >= rank else x > 0
    di = [D[i][i] for i in range(rank)]
    odd = []
    for x in di:
        while x % 2 == 0:
            x //= 2
        odd.append(x)
    assert di == r["diagonals"] and odd == r["odd_diagonals"]


def forced(row, r):
    x = [sum((row[i] * r["right"][i][j] for i in range(5))) for j in range(5)]
    return all((v == 0 for v in x[r["rank"] :])) and all(
        (x[i] % g == 0 for i, g in enumerate(r["odd_diagonals"]))
    )


def coordinates(w, m):
    return (
        tuple(
            (
                sum((w[i] * m["rows"][i][j] for i in range(8)))
                for j in range(len(m["rows"][0]))
            )
        ),
        tuple(
            (
                sum((w[i] * m["torsion_matrix"][i][j] for i in range(8))) % g
                for j, g in enumerate(m["torsion_orders"])
            )
        ),
    )


def model(m, r):
    T = mul(BASE, r["right"])
    rank = r["rank"]
    ti = [i for i, g in enumerate(r["odd_diagonals"]) if g > 1]
    assert m["rows"] == [row[rank:] for row in T]
    assert m["torsion_orders"] == [r["odd_diagonals"][i] for i in ti]
    assert m["torsion_matrix"] == [
        [row[i] % r["odd_diagonals"][i] for i in ti] for row in T
    ]


def coverage():
    answer = set()
    for x, y, z, a, b, c, d, e in permutations(range(8)):
        words = (
            counts((x, x, c, d, e)),
            counts((y, y, a, d, e)),
            counts((z, z, a, b, c)),
        )
        if {x, z} == {0, 1} or {y, z} == {0, 1}:
            answer.add(tuple(sorted(words)))
    assert len(answer) == 720
    return answer


def word(w, total):
    assert (
        len(w) == 8
        and all((isinstance(x, int) and x >= 0 for x in w))
        and (sum(w) == total)
    )


def check_proof(p):
    K = p["constraints"]
    r = p["reduction"]
    m = p["model"]
    reduction(K, r)
    model(m, r)
    val = lambda w: coordinates(w, m)
    zero = (tuple((0 for _ in m["rows"][0])), tuple((0 for _ in m["torsion_orders"])))
    e = p["exclusion"]
    owner = p["ownership"]
    if e:
        if e["kind"] == "model_label_collision":
            i, j = e["labels"]
            assert 0 <= i < 8 and 0 <= j < 8 and (i != j)
            assert val(tuple((int(k == i) - int(k == j) for k in range(8)))) == zero
        elif e["kind"] == "model_protected_collision":
            d = e["degree"]
            sf = e["squarefree"]
            other = e["other"]
            assert d in (2, 3, 4)
            word(sf, d)
            word(other, d)
            assert max(sf) == 1 and sf != other and (val(sf) == val(other))
        else:
            raise AssertionError("Unexpected unshipped exclusion type: " + e["kind"])
        return (0, "direct_exclusion")
    if owner:
        assert owner["kind"] == "declared_open_source_closed"
        f, g = owner["difference_labels"]
        assert 0 <= f < 8 and 0 <= g < 8 and (f != g)
        assert (
            val(
                tuple(
                    (
                        2 * int(i == 0) - 2 * int(i == 1) - int(i == f) + int(i == g)
                        for i in range(8)
                    )
                )
            )
            == zero
        )
        return (0, "source_closed")
    proof = p["positive"]
    if proof.get("kind") == "direct_rival":
        rival = proof["rival"]
        word(rival, 8)
        assert tuple(rival) != ONES and val(rival) == val(ONES)
        return (1, "mass_eight_rival")
    assert proof["degree"] == 4
    words = proof["words"]
    assert len(words) == 89
    for w in words:
        word(w, 4)
        assert max(w) > 1
    assert len(proof["pairs"]) == 89 * 88 // 2
    for (i, j), (rival, k, factor) in zip(combinations(range(89), 2), proof["pairs"]):
        word(rival, 8)
        assert tuple(rival) != ONES and isinstance(k, int) and unit2(factor)
        rv = val(sub(rival, ONES))
        difference = val(sub(words[i], words[j]))
        assert tuple((factor * x for x in rv[0])) == tuple(
            (k * x for x in difference[0])
        )
        assert all(
            (
                (factor * x - k * y) % g == 0
                for x, y, g in zip(rv[1], difference[1], m["torsion_orders"])
            )
        )
    return (len(proof["pairs"]), "quartic_growth89")


def main():
    path = Path(__file__).with_name("edge-ownership.json.gz")
    raw = path.read_bytes()
    data = json.loads(gzip.decompress(raw))
    cases = data["cases"]
    proofs = data["proofs"]
    got = {tuple((tuple(w) for w in c["words"])) for c in cases}
    assert len(cases) == len(got) == 720 and got == coverage()
    results = {}
    identities = 0
    for key, p in proofs.items():
        n, kind = check_proof(p)
        identities += n
        results[key] = kind
    assert all((kind != "source_closed" for kind in results.values()))
    for case in cases:
        words = case["words"]
        K = [relation(sub(words[0], words[i])) for i in (1, 2)]
        K = [list(row) for row in K if any(row)]
        assert K == case["constraints"]
        r = case["reduction"]
        reduction(K, r)
        p = proofs[case["proof_key"]]
        valid = False
        for perm in PERMS:
            inv = tuple((perm.index(i) for i in range(5)))
            transformed = [[row[j] for j in perm] for row in p["constraints"]]
            back = [[row[j] for j in inv] for row in K]
            if all((forced(row, r) for row in transformed)) and all(
                (forced(row, p["reduction"]) for row in back)
            ):
                valid = True
                break
        assert valid, "Wrong conditional source symmetry or odd row cancellation"
    from collections import Counter

    summary = {
        "complete": True,
        "split_source_presentations": 720,
        "proof_models": len(proofs),
        "proof_types": dict(Counter(results.values())),
        "positive_quartic_pair_identities": identities,
        "sha256": hashlib.sha256(raw).hexdigest(),
        "proof_boundary": "Every paired triangle edge is excluded as a genuine split source; general q<=h-o and P3ordinary>=9 follow with the written packing/forest argument. The remaining triangle families are separate proof components.",
    }
    Path(__file__).with_name("triangle-ownership-report.json").write_text(
        json.dumps(summary, indent=2) + "\n"
    )
    print(json.dumps(summary))


if __name__ == "__main__":
    main()
