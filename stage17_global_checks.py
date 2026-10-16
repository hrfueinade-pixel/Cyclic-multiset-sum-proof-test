"""Exact bookkeeping for Stage 17's global cycle restrictions.

No search of sets or moduli. Certificates use integer rows and powers of
two only. The incidence enumeration is complete only for its stated
abstract cycle models, not a classification of valid cyclic sets.
"""
from collections import Counter, defaultdict
from itertools import combinations_with_replacement, product
import json
from pathlib import Path


def add(*vs):
    return tuple(sum(xs) for xs in zip(*vs))


def scale(k, v):
    return tuple(k * x for x in v)


def unit(i, n=8):
    return tuple(int(j == i) for j in range(n))


def verify_certificate(record):
    rows, z = record['rows'], record['integer_coefficients']
    rival = record['rival']
    k = record['power_of_two']
    if not isinstance(k, int) or k < 0:
        return False
    if len(rows) != len(z) or not all(isinstance(x, int) for x in z):
        return False
    if len(rival) != 8 or sum(rival) != 8 or min(rival) < 0:
        return False
    if rival == [1] * 8 or any(sum(r) != 0 for r in rows):
        return False
    lhs = tuple((2 ** k) * (x - 1) for x in rival)
    rhs = tuple(sum(c * row[j] for c, row in zip(z, rows)) for j in range(8))
    return lhs == rhs


def certificate(name, rows, z, c, k):
    record = {'name': name, 'rows': [list(r) for r in rows],
              'integer_coefficients': z, 'power_of_two': k,
              'rival': [1 + x for x in c]}
    assert verify_certificate(record)
    return record


def even_non22_certificates():
    records = []
    # L/R denote a 31 centered on the previous/next shared edge point;
    # O has a private ordinary center. All 8-point even cycle roles fit.
    for length in (4, 6, 8):
        for types in product('OLR', repeat=length):
            if length + types.count('O') > 8:
                continue
            centers, vertices, private = [], [], length
            for i, kind in enumerate(types):
                if kind == 'O':
                    center = private
                    private += 1
                else:
                    center = (i - 1) % length if kind == 'L' else i
                centers.append(center)
                vertices.append(add(scale(2, unit(center)), unit((i-1) % length), unit(i)))
            if len(set(centers)) != length:
                continue
            # A valid cycle has exactly the displayed support intersections.
            supports = [{j for j, x in enumerate(v) if x} for v in vertices]
            if any(bool(supports[i] & supports[j]) !=
                   ((i-j) % length in (1, length-1))
                   for i in range(length) for j in range(i)):
                continue
            c = tuple(sum((-1) ** i for i, a in enumerate(centers) if a == j)
                      for j in range(8))
            rows = [add(v, scale(-1, vertices[0])) for v in vertices[1:]]
            records.append(certificate(f'even-{length}-' + ''.join(types),
                                       rows, [(-1) ** i for i in range(1, length)], c, 1))
    assert records
    return records


def local_certificates():
    # T is supplied by Stage 8 Lemma 2.1 and doubled-difference closure.
    # Three coherently oriented consecutive 31s on points x0,x1,x2,x3.
    r1 = (3, -2, -1, 0, 0, 0, 0, 0)
    r2 = (0, 3, -2, -1, 0, 0, 0, 0)
    torsion = (5, 0, -5, 0, 0, 0, 0, 0)
    chain = certificate('three-31-chain', [r1, r2, torsion], [2, 1, -1],
                        (1, -1, 1, -1, 0, 0, 0, 0), 0)
    # Q P O P, coordinate order a,b,p,q,d, then three unused points.
    rows = [(3, -3, 1, -1, 0, 0, 0, 0),
            (0, -3, 2, 1, 0, 0, 0, 0),
            (1, -2, 0, -1, 2, 0, 0, 0),
            (5, -5, 0, 0, 0, 0, 0, 0)]
    quadrilateral = certificate('22-31-ordinary-31', rows, [-2, 1, -1, 1],
                                (-1, 0, 0, 2, -1, 0, 0, 0), 1)
    return [chain, quadrilateral]


def canonical(word):
    versions = [word[i:] + word[:i] for i in range(len(word))]
    reverse = word[::-1]
    versions += [reverse[i:] + reverse[:i] for i in range(len(word))]
    return min(versions)


def long_type_words():
    remaining = defaultdict(set)
    examined = 0
    for length in range(4, 9):
        for kinds in product('OPQ', repeat=length):
            examined += 1
            word = ''.join(kinds)
            n_q, n_o, n_p = word.count('Q'), word.count('O'), word.count('P')
            if n_q > 1 or length + n_o > 8:
                continue
            if not n_q and length % 2 == 0:
                continue
            if any(all(word[(i+j) % length] == 'P' for j in range(3))
                   for i in range(length)):
                continue
            if n_q:
                q = word.index('Q')
                if any(word[i] == 'P' and (i-q) % length not in (1, length-1)
                       for i in range(length)):
                    continue
                if length == 4 and n_p == 2:
                    continue
            elif length == 5 and n_p >= 3:
                continue
            remaining[str(length)].add(canonical(word))
    result = {k: sorted(v) for k, v in remaining.items()}
    assert set(result) == {'4', '5'}
    assert len(result['4']) == 2 and len(result['5']) == 4
    return {'ordered_words_examined': examined, 'remaining_dihedral_type_words': result,
            'scope': 'Necessary type words only; no realization or exclusion of the surviving words.'}


def binary_control():
    a, modulus = [1 << i for i in range(8)], 255
    fibers = defaultdict(list)
    for v in combinations_with_replacement(range(8), 4):
        if len(set(v)) < 4:
            fibers[sum(a[i] for i in v) % modulus].append(v)
    paths, cycles = [], Counter()
    for vs in fibers.values():
        adjacency = [{j for j, other in enumerate(vs) if i != j and set(v) & set(other)}
                     for i, v in enumerate(vs)]
        assert all(len(ns) <= 2 for ns in adjacency)
        unseen = set(range(len(vs)))
        while unseen:
            reached, pending = {unseen.pop()}, []
            pending.extend(reached)
            while pending:
                for j in adjacency[pending.pop()] & unseen:
                    unseen.remove(j)
                    reached.add(j)
                    pending.append(j)
            if all(len(adjacency[i]) == 2 for i in reached):
                cycles[len(reached)] += 1
            else:
                paths.append(len(reached))
    assert len(paths) == 36 and cycles == {3: 56}
    internal = sum(max(0, length-2) for length in paths)
    isolated = sum(length == 1 for length in paths)
    assert 3 * sum(cycles.values()) == 188 + isolated - internal - cycles[4] - 2 * cycles[5]
    return {'N': modulus, 'path_lengths': dict(Counter(paths)), 'cycle_lengths': dict(cycles),
            'internal_path_vertices': internal, 'isolated_22': isolated,
            'budget_for_53_cycles': internal + cycles[4] + 2 * cycles[5],
            'required_upper_budget': 29 + isolated,
            'scope': 'One proved binary control, not evidence for a universal bound.'}


def main():
    records = even_non22_certificates() + local_certificates()
    damaged = dict(records[0])
    damaged['integer_coefficients'] = list(records[0]['integer_coefficients'])
    damaged['integer_coefficients'][0] += 1
    assert not verify_certificate(damaged)
    odd_denominator = dict(records[0])
    odd_denominator['integer_coefficients'] = [x / 3 for x in records[0]['integer_coefficients']]
    assert not verify_certificate(odd_denominator)
    result = {'completed': True, 'timed_out': False,
              'scope': 'Proof bookkeeping, bounded cycle-role words, and one binary control; no set or modulus search.',
              'certificates': records, 'certificate_count': len(records),
              'negative_controls_rejected': ['incorrect identity', 'noninteger odd-denominator coefficients'],
              'long_cycle_types': long_type_words(), 'binary_control': binary_control()}
    Path(__file__).with_name('stage17_global_results.json').write_text(
        json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items() if k != 'certificates'}, indent=2))


if __name__ == '__main__':
    main()
