"""Standalone proof checker: coverage, group surjectivity, positive identities.

No discovery/producer imports. Every selected quartic pair is accompanied
by a positively reconstructed mass-eight rival identity, with powers of
two as the only canceled factors. Failure to find any identity is failure
of the proof, never a mathematical exclusion.
"""

from collections import Counter
from itertools import combinations, permutations
from math import gcd
from pathlib import Path
import copy
import gzip
import hashlib
import json

HERE = Path(__file__).parent
PAIR_IDENTITIES = 0
DIRECT_IDENTITIES = 0


def w(indices):
    return tuple((indices.count(i) for i in range(8)))


def sub(a, b):
    return tuple((x - y for x, y in zip(a, b)))


def decode(s):
    return tuple(map(int, s))


def dot(a, b):
    return sum((x * y for x, y in zip(a, b)))


def determinant(a):
    n = len(a)
    total = 0
    for p in permutations(range(n)):
        sign = (-1) ** sum((p[i] > p[j] for i in range(n) for j in range(i + 1, n)))
        product = sign
        for i in range(n):
            product *= a[i][p[i]]
        total += product
    return total


def unit2(n):
    return isinstance(n, int) and n > 0 and (n & n - 1 == 0)


def source_rows(tail, center=5):
    cw = (w((0, 0, 5, 6, 7)), w((1, 1, 3, 6, 7)), w((2, 2, 3, 4, 5)))
    base = (sub(cw[0], cw[1]), sub(cw[0], cw[2]))
    return base + (sub(w((0, 0, 6, 7)), w((center, center) + tuple(tail))),)


def check_parameterization(rows, parameter):
    M = parameter["rows"]
    free = parameter["free_labels"]
    pivots = parameter["pivots"]
    scale = parameter["scale"]
    assert len(M) == 8 and unit2(scale)
    assert sorted(free + pivots) == list(range(7)) and len(pivots) == len(rows)
    assert all((len(r) == len(free) for r in M)) and M[7] == [0] * len(free)
    assert all(
        (
            M[label] == [scale * int(i == j) for j in range(len(free))]
            for i, label in enumerate(free)
        )
    )
    assert unit2(abs(determinant([[r[c] for c in pivots] for r in rows])))
    assert all(
        (
            sum((r[i] * M[i][j] for i in range(8))) == 0
            for r in rows
            for j in range(len(free))
        )
    )
    return M


def coeff(word, M):
    return tuple((sum((word[i] * M[i][j] for i in range(8))) for j in range(len(M[0]))))


def normalize(v):
    factor = 1
    while all((n % 2 == 0 for n in v)):
        v = tuple((n // 2 for n in v))
        factor *= 2
    if next((n for n in v if n)) < 0:
        v = tuple((-n for n in v))
        factor = -factor
    return (v, factor)


def reduction(M, case):
    U = case["U"]
    n = len(M[0])
    direction = case["direction"]
    assert len(U) == n and all((len(r) == n for r in U)) and (abs(determinant(U)) == 1)
    actual = tuple((sum((direction[i] * U[i][j] for i in range(n))) for j in range(n)))
    g = case["gcd"]
    odd = case["odd_gcd"]
    assert g > 0 and actual == (g,) + (0,) * (n - 1)
    expected = g
    while expected % 2 == 0:
        expected //= 2
    assert odd == expected and odd % 2 == 1
    full = [[sum((r[i] * U[i][j] for i in range(n))) for j in range(n)] for r in M]
    return ([r[1:] for r in full], [r[0] % odd for r in full], odd)


def direct_identity(rows, target, identity):
    global DIRECT_IDENTITIES
    factor = identity["factor"]
    combo = identity["multipliers"]
    assert (
        unit2(factor)
        and len(combo) == len(rows)
        and all((isinstance(n, int) for n in combo))
    )
    assert tuple(
        (sum((combo[j] * rows[j][i] for j in range(len(rows)))) for i in range(8))
    ) == tuple((factor * n for n in target))
    DIRECT_IDENTITIES += 1


def check_exclusion(rows, certificate):
    kind = certificate["kind"]
    if kind == "label_collision":
        i, j = certificate["labels"]
        assert i != j and 0 <= i < 8 and (0 <= j < 8)
        target = sub(w((i,)), w((j,)))
    elif kind == "protected_collision":
        a = tuple(certificate["squarefree"])
        b = tuple(certificate["other"])
        degree = certificate["degree"]
        assert (
            len(a) == len(b) == 8
            and sum(a) == sum(b) == degree
            and (degree in (2, 3, 4))
        )
        assert set(a) <= {0, 1} and min(b) >= 0 and (a != b)
        target = sub(a, b)
    elif kind == "mass_eight_rival":
        rival = tuple(certificate["word"])
        assert (
            len(rival) == 8
            and min(rival) >= 0
            and (sum(rival) == 8)
            and (rival != (1,) * 8)
        )
        target = sub(rival, (1,) * 8)
    elif kind == "ordinary_cap_four":
        degree = certificate["degree"]
        words = [tuple(a) for a in certificate["words"]]
        assert degree in (4, 5) and len(words) == len(set(words)) == 4
        assert all(
            (sorted((n for n in a if n)) == [1] * (degree - 2) + [2] for a in words)
        )
        assert len(certificate["identities"]) == 3
        for a, c in zip(words[1:], certificate["identities"]):
            direct_identity(rows, sub(words[0], a), c)
        return
    else:
        raise AssertionError("Unrecognized exclusion")
    direct_identity(rows, target, certificate)


def all_eight_words():
    for bars in combinations(range(15), 7):
        cuts = (-1,) + bars + (15,)
        yield tuple((cuts[i + 1] - cuts[i] - 1 for i in range(8)))


EIGHT_WORDS = list(all_eight_words())
assert len(EIGHT_WORDS) == 6435 and (1,) * 8 in EIGHT_WORDS


def ray(v):
    common = gcd(*v)
    if next((n for n in v if n)) < 0:
        common = -common
    return (tuple((n // common for n in v)), common)


def check_positive(M, tor, order, proof):
    global PAIR_IDENTITIES

    def value(word):
        return (coeff(word, M), dot(word, tor) % order)

    target = value((1,) * 8)
    if proof["kind"] == "rival":
        rival = decode(proof["word"])
        assert (
            len(rival) == 8
            and min(rival) >= 0
            and (sum(rival) == 8)
            and (rival != (1,) * 8)
            and (value(rival) == target)
        )
        return 0
    assert proof["kind"] == "growth89"
    words = [decode(s) for s in proof["words"]]
    assert len(words) == len(set(words)) == 89
    assert all(
        (len(a) == 8 and min(a) >= 0 and (sum(a) == 4) and (max(a) > 1) for a in words)
    )
    values = [value(a) for a in words]
    assert len(set(values)) == 89
    rivals_by_ray = {}
    torsion_only = []
    for word in EIGHT_WORDS:
        if word == (1,) * 8:
            continue
        f, t = value(word)
        free = sub(f, target[0])
        torsion = (t - target[1]) % order
        if any(free):
            key, scale = ray(free)
            rivals_by_ray.setdefault(key, []).append((scale, torsion, word, free))
        elif torsion:
            torsion_only.append((torsion, word))
    for i, j in combinations(range(89), 2):
        free = sub(values[i][0], values[j][0])
        torsion = (values[i][1] - values[j][1]) % order
        found = False
        if any(free):
            key, scale = ray(free)
            for rscale, rtor, rword, rfree in rivals_by_ray.get(key, ()):
                numerator = rscale
                denominator = scale
                common = gcd(numerator, denominator)
                numerator //= common
                denominator //= common
                if denominator < 0:
                    numerator = -numerator
                    denominator = -denominator
                if not unit2(denominator):
                    continue
                if (denominator * rtor - numerator * torsion) % order:
                    continue
                assert tuple((denominator * v for v in rfree)) == tuple(
                    (numerator * v for v in free)
                )
                found = True
                break
        else:
            assert torsion
            for mult in range(1, order):
                for rtor, rword in torsion_only:
                    if (rtor - mult * torsion) % order == 0:
                        found = True
                        break
                if found:
                    break
        assert found, ("Missing positive separation identity", i, j)
        PAIR_IDENTITIES += 1
    return 3916


def check_inventory(cases, M, base_rows, residual_allowed=False):
    cube_words = sorted({w((c, c, b)) for c in range(8) for b in range(8)})
    assert len(cube_words) == 64
    expected = set()
    for a, b in combinations(cube_words, 2):
        d = sub(coeff(a, M), coeff(b, M))
        if any(d):
            expected.add(normalize(d)[0])
    assert {tuple(c["direction"]) for c in cases} == expected and len(cases) == len(
        expected
    )
    survivors = {}
    growth_count = 0
    for c in cases:
        a, b = map(decode, c["words"])
        assert a in cube_words and b in cube_words and (a != b)
        d = sub(coeff(a, M), coeff(b, M))
        assert any(d) and normalize(d)[0] == tuple(c["direction"])
        rows = base_rows + (sub(a, b),)
        if "exclusion" in c:
            check_exclusion(rows, c["exclusion"])
        else:
            free, tor, order = reduction(M, c)
            if "positive" in c:
                check_positive(free, tor, order, c["positive"])
                growth_count += 1
            else:
                assert residual_allowed and c["residual"] and (order == 1)
                survivors[c["index"]] = {"M": free, "rows": rows}
    return (survivors, growth_count)


def main():
    blob = (HERE / "split-sources.json.gz").read_bytes()
    data = json.loads(gzip.decompress(blob))
    source_cases = {tuple(c["tail"]): c for c in data["source_cases"]}
    assert set(source_cases) == set(combinations((1, 3, 4, 6, 7), 2))
    for tail, c in source_cases.items():
        rows = source_rows(tail)
        if "exclusion" in c:
            check_exclusion(rows, c["exclusion"])
        elif "positive" in c:
            M = check_parameterization(rows, c["parameterization"])
            check_positive(M, [0] * 8, 1, c["positive"])
        elif "mirror_of" in c:
            base_tail = tuple(c["mirror_of"])
            assert tail[0] == base_tail[0] and base_tail[1] == 6 and (tail[1] == 7)
            pi = (0, 1, 2, 3, 4, 5, 7, 6)
            assert (
                tuple(
                    (
                        tuple((r[pi[i]] for i in range(8)))
                        for r in source_rows(base_tail)
                    )
                )
                == rows
            )
        else:
            assert tail == (3, 6) and c["path_inventory"]
    base_rows = tuple(map(tuple, data["base_relations"]))
    assert base_rows == source_rows((3, 6))
    M = check_parameterization(base_rows, data["base_parameterization"])
    cube_words = sorted({w((c, c, b)) for c in range(8) for b in range(8)})
    sizes = Counter((coeff(a, M) for a in cube_words))
    assert len(sizes) == 60 and dict(Counter(sizes.values())) == {1: 56, 2: 4}
    survivors, growth_first = check_inventory(data["first"], M, base_rows, True)
    assert (
        set(survivors) == {389, 740, 764, 794, 800, 805} and len(data["first"]) == 901
    )
    assert {p["parent"] for p in data["second"]} == set(survivors) and len(
        data["second"]
    ) == 6
    growth_second = 0
    second_cases = 0
    torsion_orders = set()
    for parent in data["second"]:
        prior = survivors[parent["parent"]]
        sizes = Counter((coeff(a, prior["M"]) for a in cube_words))
        assert len(sizes) == 59 and dict(Counter(sizes.values())) == {1: 54, 2: 5}
        unresolved, growth = check_inventory(parent["cases"], prior["M"], prior["rows"])
        assert not unresolved
        growth_second += growth
        second_cases += len(parent["cases"])
        torsion_orders.update((c["odd_gcd"] for c in parent["cases"] if "odd_gcd" in c))
        print(
            json.dumps(
                {
                    "parent": parent["parent"],
                    "complete_positive_coverage": len(parent["cases"]),
                }
            ),
            flush=True,
        )
    assert second_cases == 4339
    for tail in combinations((3, 4, 5, 6, 7), 2):
        rows = source_rows(tail, center=1)
        protected = w((3, 6, 7))
        other = w((5,) + tail)
        assert protected != other and max(protected) == 1
        assert sub(protected, other) == sub(rows[2], rows[0])
    sample = next((c for c in data["first"] if "exclusion" in c))
    rows = base_rows + (sub(*map(decode, sample["words"])),)
    broken = copy.deepcopy(sample["exclusion"])
    if broken["kind"] == "ordinary_cap_four":
        broken = broken["identities"][0]
    broken["factor"] = 3
    failed = False
    try:
        direct_identity(rows, (0,) * 8, broken)
    except AssertionError:
        failed = True
    assert failed
    result = {
        "complete": True,
        "first_directions": 901,
        "first_growth_models": growth_first,
        "second_directions": second_cases,
        "second_growth_models": growth_second,
        "positive_quartic_pair_identities_reconstructed": PAIR_IDENTITIES,
        "direct_integer_identities_checked": DIRECT_IDENTITIES,
        "odd_torsion_orders_retained": sorted(torsion_orders),
        "bundle_sha256": hashlib.sha256(blob).hexdigest(),
        "proof_boundary": "General E>=2q follows only with the written source and global-count lemmas; this checker proves the source-budget component. Separate implementation is not external human review or formal certification.",
    }
    (HERE / "split-sources-report.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
