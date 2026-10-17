"""Additional coverage audit using ordered physical labels, not checker helpers.

Run as ``python -m verification.independent``. This is another AI-written
implementation, not external mathematical review or a formal proof.
"""

from collections import Counter
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path
import gzip
import hashlib
import json

ROOT = Path(__file__).resolve().parent.parent
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
PERMS = {p + q for p in permutations(range(3)) for q in ((3, 4), (4, 3))}


def determinant(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    answer = Fraction(1)
    for j in range(len(a)):
        pivot = next((i for i in range(j, len(a)) if a[i][j]), None)
        if pivot is None:
            return 0
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            answer = -answer
        answer *= a[j][j]
        scale = a[j][j]
        a[j] = [x / scale for x in a[j]]
        for i in range(j + 1, len(a)):
            scale = a[i][j]
            a[i] = [x - scale * y for x, y in zip(a[i], a[j])]
    assert answer.denominator == 1
    return int(answer)


def evaluate(word, model):
    free = tuple(
        sum(n * r[j] for n, r in zip(word, model["rows"]))
        for j in range(len(model["rows"][0]))
    )
    torsion = tuple(
        sum(n * r[j] for n, r in zip(word, model["torsion_matrix"])) % g
        for j, g in enumerate(model["torsion_orders"])
    )
    return free, torsion


def direction(row):
    row = tuple(row)
    assert any(row)
    while not any(x % 2 for x in row):
        row = tuple(x // 2 for x in row)
    return row if next(x for x in row if x) > 0 else tuple(-x for x in row)


def private_directions(model):
    """Every ordinary collision has four distinct physical labels."""
    result = set()
    for x, b, y, a in permutations(range(8), 4):
        word = tuple(
            2 * (i == x) + (i == b) - 2 * (i == y) - (i == a) for i in range(8)
        )
        if any(evaluate(word, model)[0]) or any(evaluate(word, model)[1]):
            result.add(
                direction(sum(word[i] * BASE[i][j] for i in range(8)) for j in range(5))
            )
    return result


def reduction_constraints(reduction, modulus):
    """All transformed parameters, including every nonunit preimage."""
    rank = reduction["rank"]
    return product(
        *(
            (
                tuple(
                    x for x in range(modulus) if reduction["D"][i][i] * x % modulus == 0
                )
                if i < rank
                else range(modulus)
            )
            for i in range(5)
        )
    )


def check_cyclic_surjectivity(rows, reduction, modulus):
    direct = {
        z
        for z in product(range(modulus), repeat=5)
        if all(sum(x * y for x, y in zip(row, z)) % modulus == 0 for row in rows)
    }
    V = reduction["right"]
    recovered = {
        tuple(sum(V[i][j] * z[j] for j in range(5)) % modulus for i in range(5))
        for z in reduction_constraints(reduction, modulus)
    }
    assert direct == recovered, "Parameterization lost cyclic solutions"


def validate_branches(model, cases, nodes):
    expected = private_directions(model)
    actual = [tuple(c["direction"]) for c in cases]
    assert (
        len(actual) == len(set(actual)) and set(actual) == expected
    ), "Missing/duplicate branch"
    for c in cases:
        perm = tuple(c.get("permutation", range(5)))
        assert perm in PERMS, "Invalid physical symmetry"
        child = nodes[c["node"]]
        r = c["reduction"]
        assert all(
            type(x) is int for row in r["right"] for x in row
        ), "Matrix must be integral"
        assert all(type(x) is int for row in child["constraints"] for x in row)
        assert abs(determinant(r["right"])) == 1
        for row in child["constraints"]:
            transformed = [
                sum(row[perm[i]] * r["right"][i][j] for i in range(5)) for j in range(5)
            ]
            assert not any(transformed[r["rank"] :]), "Child loses free parameters"
            assert all(
                transformed[i] % g == 0 for i, g in enumerate(r["odd_diagonals"])
            ), "Odd torsion lost"


def main():
    counts = Counter()
    fixtures = {}
    for name in ("large-forests", "interactions", "two-triangle-class"):
        path = ROOT / "certificates/triangles" / (name + ".json.gz")
        data = json.loads(gzip.decompress(path.read_bytes()))
        groups = (
            [data]
            if name == "large-forests"
            else (
                [data["alternating"], data["coupling"]]
                if name == "interactions"
                else data["components"]
            )
        )
        for group in groups:
            nodes = group["nodes"]
            for node in nodes:
                r = node["reduction"]
                odd = tuple(r["odd_diagonals"])
                if any(g > 1 for g in odd):
                    fixtures.setdefault(odd, (node["constraints"], r))
                p = node["proof"]
                if p["kind"] == "forced_ordinary":
                    # Every current forcing node uses P<=8. Other conditional
                    # credit rules require a new, explicit review contract.
                    assert p.get("reason", "P9") == "P9"
                    validate_branches(node["model"], p["coverage"], nodes)
                    counts[name + "_forcing_nodes"] += 1
                    counts["refinement_branches"] += len(p["coverage"])
        counts[name + "_bytes"] = path.stat().st_size
    # Exercise actual retained reductions with 3-, 5-, and 9-torsion, using
    # exhaustive ambient cyclic solutions, independently of formal modules.
    selected = []
    for prime in (3, 5, 9):
        key = next(k for k in sorted(fixtures) if any(g % prime == 0 for g in k))
        rows, r = fixtures[key]
        check_cyclic_surjectivity(rows, r, prime)
        selected.append({"modulus": prime, "diagonals": list(key)})
    report = {
        "coverage": dict(counts),
        "cyclic_surjectivity": selected,
        "manifest_sha256": hashlib.sha256(
            (ROOT / "certificates/manifest.json").read_bytes()
        ).hexdigest(),
        "scope": "Ordered-label branch coverage and small cyclic parameter checks; not an independent human review.",
    }
    target = ROOT / ".verification/independent-report.json"
    target.parent.mkdir(exist_ok=True)
    target.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
