"""Separate arithmetic challenge to Stage 46; imports no discovery modules.

Checks supplied positive identities, fixed symbolic coverage and the hand
classification. It does not certify the unresolved global growth inequality.
"""
import itertools
import json
from collections import Counter
from pathlib import Path


def check_identity(record):
    counts = record['rival']['rival']
    factor = record['rival']['unit_factor']
    assert factor > 0 and factor & (factor - 1) == 0
    assert len(counts) == 8 and sum(counts) == 8
    assert all(isinstance(c, int) and c >= 0 for c in counts)
    assert counts != [1] * 8
    ordinary = []
    for excluded in range(3):
        word = [0] * 8
        word[5 + excluded] = 2
        for j in range(3):
            if j != excluded:
                word[j] = 1
        ordinary.append(word)
    mixed = []
    for center, tail in record['edges']:
        word = [0] * 8
        word[center] = 3
        word[tail] += 1
        mixed.append(word)
    rows = [[word[j] - ordinary[0][j] for j in range(8)]
            for word in ordinary[1:] + mixed]
    multipliers = record['rival']['multipliers']
    assert len(rows) == len(multipliers)
    for j in range(8):
        assert factor * (counts[j] - 1) == sum(k * row[j] for k, row in zip(multipliers, rows))


def classify(edges):
    outgoing = dict(edges)
    x_centers = sorted(i for i in outgoing if i < 3)
    if len(x_centers) >= 2:
        a, b = x_centers[:2]
        return 'two_X_centers_same_tail' if outgoing[a] == outgoing[b] else 'two_X_centers_distinct_tails'
    if any(outgoing.get(j) == i for i, j in edges):
        return 'opposite_edges'
    if any(i < 3 and j >= 3 and outgoing.get(j, 5) < 3 for i, j in edges):
        return 'X_U_X_path'
    assert len(x_centers) == 1 and 3 in outgoing and 4 in outgoing
    a = x_centers[0]
    u = outgoing[a]
    v = 7 - u
    assert outgoing[u] == v
    b = outgoing[v]
    if b == a:
        return 'directed_triangle'
    assert b < 3
    return 'final_X_U_U_X_chain'


def test_hand_formulas():
    # Formal q=0 coefficients, with independent a,b,c,u,v.
    a, b, c, u, v = [tuple(int(i == j) for j in range(5)) for i in range(5)]
    def add(*vectors):
        return tuple(sum(row[j] for row in vectors) for j in range(5))
    def mul(k, vector):
        return tuple(k * x for x in vector)
    two_x = mul(-1, add(b, c))
    two_y = mul(-1, add(a, c))
    two_z = mul(-1, add(a, b))
    # Two X centers pointing to different U labels: 2(r-s) is minus
    # twice the sum of the corresponding 31 equations.
    lhs = add(mul(2, c), two_x, two_y, mul(5, two_z), mul(-2, u), mul(-2, v))
    rhs = mul(-2, add(mul(3, a), u, mul(3, b), v))
    assert lhs == rhs
    # Two X centers with the same tail: doubled squarefree-pair difference.
    assert add(mul(2, a), two_x, mul(-2, b), mul(-1, two_y)) == mul(3, add(a, mul(-1, b)))
    # X->U->X: doubled value of 5a+z is 9a-b, obtained by subtracting
    # the second 31 equation from three copies of the first.
    assert add(mul(10, a), two_z) == add(mul(3, add(mul(3, a), u)), mul(-1, add(mul(3, u), b)))
    # Final chain a->u->v->b, coefficients in the one free a plus c.
    model = ((2, 0), (-54, 0), (0, 2), (-6, 0), (18, 0), (27, -1), (-1, -1), (26, 0))
    counts = (2, 1, 1, 0, 2, 1, 1, 0)
    assert tuple(sum(counts[i] * model[i][j] for i in range(8)) for j in range(2)) == (12, 0)
    assert tuple(sum(row[j] for row in model) for j in range(2)) == (12, 0)
    for d in range(4):
        for m in range(16):
            if (m - d) % 2 == 0:
                assert 2 + m - d >= 0


def positive_control():
    data = json.loads(Path('stage46_positive_control_results.json').read_text())
    a = data['set']
    modulus = data['modulus']
    hits = []
    # Counts rather than the producer's index-multiset implementation.
    def compositions(total, length, prefix=()):
        if length == 1:
            yield prefix + (total,)
        else:
            for first in range(total + 1):
                yield from compositions(total - first, length - 1, prefix + (first,))
    for counts in compositions(8, 8):
        if sum(x * y for x, y in zip(a, counts)) % modulus == sum(a) % modulus:
            hits.append(counts)
    assert hits == [(1,) * 8]
    assert modulus % 2 == 1 and 8 * max(a) < modulus
    q = data['quartic_value']
    fiber = [counts for counts in compositions(4, 8)
             if sum(x * y for x, y in zip(a, counts)) % modulus == q]
    assert sorted(sorted(x for x in counts if x) for counts in fiber) == [[1, 1, 2]] * 3 + [[1, 3]]
    assert {i for counts in fiber for i, n in enumerate(counts) if n} == set(range(8))
    return len(hits), len(fiber)


def main():
    test_hand_formulas()
    data = json.loads(Path('stage46_three_31_probe_results.json').read_text())
    permutations = [p + q for p in itertools.permutations(range(3)) for q in itertools.permutations((3, 4))]
    expanded = set()
    for record in data['records']:
        check_identity(record)
        images = {tuple(sorted((p[i], p[j]) for i, j in record['edges'])) for p in permutations}
        assert len(images) == record['orbit_size']
        assert expanded.isdisjoint(images)
        expanded.update(images)
    expected = set()
    classes = Counter()
    for centers in itertools.combinations(range(5), 3):
        for tails in itertools.product(range(5), repeat=3):
            if any(i == j or (i < 3 and j < 3) for i, j in zip(centers, tails)):
                continue
            edges = tuple(zip(centers, tails))
            expected.add(edges)
            classes[classify(edges)] += 1
    assert expanded == expected and len(expected) == 200
    rejected = []
    for kind in ('factor_three', 'wrong_mass', 'original_word'):
        corrupted = json.loads(json.dumps(data['records'][0]))
        if kind == 'factor_three':
            corrupted['rival']['unit_factor'] = 3
        elif kind == 'wrong_mass':
            corrupted['rival']['rival'][0] += 1
        else:
            corrupted['rival']['rival'] = [1] * 8
        try:
            check_identity(corrupted)
        except AssertionError:
            rejected.append(kind)
        else:
            raise AssertionError('Corruption was accepted: ' + kind)
    hits, fiber_size = positive_control()
    result = {'checked_orbits': len(data['records']), 'covered_assignments': len(expected),
              'hand_classes': dict(classes), 'positive_control_target_hits': hits,
              'positive_control_quartic_fiber': fiber_size,
              'rejected_corruptions': rejected,
              'boundary': 'Local elementary theorems checked; global N>=248 remains open.'}
    Path('stage46_proof_check_results.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
