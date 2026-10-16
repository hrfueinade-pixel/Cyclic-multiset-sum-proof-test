"""Audit three declared actual cyclic controls and new pair-lift identities.

No producer import; no parameter search or historical rerun.
"""
from collections import defaultdict, Counter
from itertools import combinations
import json
from pathlib import Path


def words(degree):
    for bars in combinations(range(degree + 7), 7):
        b = (-1,) + bars + (degree + 7,)
        yield tuple(b[i + 1] - b[i] - 1 for i in range(8))


def ordinary(p, degree):
    return p.count(2) == 1 and p.count(1) == degree - 2 and p.count(0) == 9 - degree


def audit_star_inventory(here):
    data = json.loads((here / 'stage47_star_avoid_results.json').read_text())
    models = data['models']
    assert len(models) == 52
    expected = set()
    for bars in combinations(range(8), 3):
        b = (-1,) + bars + (8,)
        w = tuple(b[i + 1] - b[i] - 1 for i in range(4))
        if sorted(w) != [1, 1, 1, 2]:
            expected.add(w)
    assert {tuple(m['word_abcv']) for m in models} == expected
    checked_rivals = 0
    for model in models:
        w = model['word_abcv']
        expected_rows = [(2,0,0,0), (0,2,0,0), (0,0,2,0),
                         tuple(2 * z for z in w), (0,0,0,2),
                         (0,-1,-1,0), (-1,0,-1,0), (-1,-1,0,0)]
        rows = [tuple(row) for row in model['rows']]
        assert rows == expected_rows
        target = tuple(sum(row[j] for row in rows) for j in range(4))
        for r in model['direct_rivals']:
            assert len(r) == 8 and min(r) >= 0 and sum(r) == 8 and r != [1] * 8
            assert tuple(sum(r[i] * rows[i][j] for i in range(8)) for j in range(4)) == target
            checked_rivals += 1
        excluded_hand = sorted(z for z in w if z) == [1, 2, 2] and sum(z == 2 for z in w[:3]) == 2
        assert bool(model['direct_rivals']) == excluded_hand
    assert checked_rivals > 0
    parity_same_v_pairs = parity_rivals = fixed_parity_pairs = 0
    for w, other in combinations(sorted(expected), 2):
        if w[3] % 2 != other[3] % 2:
            continue
        parity_same_v_pairs += 1
        differing = [i for i in range(3) if w[i] % 2 != other[i] % 2]
        if not differing:
            diff = [a - b for a, b in zip(w, other)]
            while all(x % 2 == 0 for x in diff):
                diff = [x // 2 for x in diff]
            assert min(diff) >= -1 or max(diff) <= 1
            fixed_parity_pairs += 1
            continue
        assert len(differing) == 2
        a, b = differing
        # Opposite triangle center: ab->z, ac->y, bc->x.
        center = {(0, 1): 7, (0, 2): 6, (1, 2): 5}[(a, b)]
        total = [0] * 8
        for i, label in enumerate((0, 1, 2, 4)):
            total[label] = w[i] + other[i]
        total[4] += 2
        total[a] += 1
        total[b] += 1
        total[center] += 2
        assert all(x % 2 == 0 for x in total)
        r = [x // 2 for x in total]
        assert min(r) >= 0 and sum(r) == 8 and r != [1] * 8
        rows = [(2,0,0,0), (0,2,0,0), (0,0,2,0),
                tuple(2 * z for z in w), (0,0,0,2),
                (0,-1,-1,0), (-1,0,-1,0), (-1,-1,0,0)]
        rival_delta = tuple(sum((r[i] - 1) * rows[i][k] for i in range(8)) for k in range(4))
        assert tuple(2 * z for z in rival_delta) == tuple(2 * (x - y) for x, y in zip(other, w))
        parity_rivals += 1
    pairs = json.loads((here / 'stage47_star_pairs_results.json').read_text())
    live_words = [m['word_abcv'] for m in models if not m['direct_rivals']]
    assert pairs['words'] == live_words and len(live_words) == 46
    def check_edge(edge):
        i, j = edge['left'], edge['right']
        assert 0 <= i < j < 46
        w = live_words[i]
        rows = [(2,0,0,0), (0,2,0,0), (0,0,2,0),
                tuple(2 * z for z in w), (0,0,0,2),
                (0,-1,-1,0), (-1,0,-1,0), (-1,-1,0,0)]
        r = edge['rival']
        factor, multiplier = edge['factor'], edge['multiplier']
        assert isinstance(factor, int) and factor > 0 and factor & (factor - 1) == 0
        assert isinstance(multiplier, int) and multiplier != 0
        assert len(r) == 8 and min(r) >= 0 and sum(r) == 8 and r != [1] * 8
        delta = tuple(sum((r[i] - 1) * rows[i][k] for i in range(8)) for k in range(4))
        challenged = tuple(2 * (a - b) for a, b in zip(live_words[j], w))
        assert tuple(factor * x for x in delta) == tuple(multiplier * x for x in challenged)
    assert len(pairs['edges']) == 726
    assert len({(e['left'], e['right']) for e in pairs['edges']}) == 726
    for edge in pairs['edges']:
        check_edge(edge)
    rejected = 0
    for kind in ('factor3', 'original', 'wrongmass', 'zeromultiplier'):
        bad = dict(pairs['edges'][0])
        if kind == 'factor3': bad['factor'] = 3
        elif kind == 'original': bad['rival'] = [1] * 8
        elif kind == 'wrongmass': bad['rival'] = [9] + [0] * 7
        else: bad['multiplier'] = 0
        try:
            check_edge(bad)
        except AssertionError:
            rejected += 1
        else:
            raise AssertionError('corruption accepted')
    return {'assignments': 52, 'positive_rivals_checked': checked_rivals,
            'hand_221_excluded_assignments': 6,
            'positive_star_pair_identities_checked': 726,
            'corruption_controls_rejected': rejected,
            'same_v_parity_hand_cases_checked': parity_same_v_pairs,
            'hand_positive_parity_rivals': parity_rivals,
            'fixed_parity_impossible_equalities': fixed_parity_pairs,
            'absence_boundary': 'No universal group exclusion follows for models without an identical formal rival.'}


def audit_matching_slice(here):
    data = json.loads((here / 'stage47_no_triangle_matching_results.json').read_text())
    def edge_rows(c, d):
        others = [i for i in range(8) if i != c and i != d]
        rows = []
        for mask in range(64):
            if mask.bit_count() != 3:
                continue
            r = [0] * 8
            r[c], r[d] = 2, -2
            for i, label in enumerate(others):
                r[label] = 1 if mask >> i & 1 else -1
            rows.append(tuple(r))
        return rows
    def viable(rows):
        for mask in range(16):
            r = tuple(1 + sum((1 if mask >> i & 1 else -1) * rows[i][j]
                              for i in range(4)) for j in range(8))
            if min(r) >= 0 and r != (1,) * 8:
                assert sum(r) == 8
                return True
        return False
    first = (2, -2, 1, 1, 1, -1, -1, -1)
    positive = total = 0
    for a in edge_rows(2, 3):
        for b in edge_rows(4, 5):
            for c in edge_rows(6, 7):
                total += 1
                positive += viable((first, a, b, c))
    assert total == data['assignments'] == 8000
    assert positive == data['direct_signed_sum_rival'] == 2340
    assert total - positive == data['formula_failures'] == 5660
    for example in data['failure_examples']:
        assert not viable(example)
    p = data['first_positive_witness']
    assert p['rival'] == [1 + sum(p['signs'][i] * p['rows'][i][j] for i in range(4))
                         for j in range(8)]
    assert min(p['rival']) >= 0 and sum(p['rival']) == 8 and p['rival'] != [1] * 8
    return {'fixed_assignments_independently_rebuilt': total,
            'positive_signed_sum_rivals': positive,
            'restricted_formula_failures': total - positive,
            'boundary': 'Formula failures are neither valid sets nor unclosed full group models.'}


def main():
    here = Path(__file__).parent
    controls = [
        ('path', (0, 2, 34, 578, 9826, 83522, 83539, 83827), 670617, (62, 244, 664)),
        ('split', (0, 2, 34, 578, 9826, 83522, 83539, 88723), 709785, (63, 250, 685)),
        ('star_avoiding', (10304, 10504, 30704, 10312, 9704, 0, 100, 10200),
         245633, (60, 228, 592)),
    ]
    results = []
    for name, A, N, expected in controls:
        fs = {}
        for d in (3, 4, 5, 8):
            fd = defaultdict(list)
            for p in words(d):
                fd[sum(a * z for a, z in zip(A, p)) % N].append(p)
            fs[d] = fd
        assert fs[8][sum(A) % N] == [(1,) * 8]
        assert sum(map(len, fs[8].values())) == 6435
        counts = tuple(sum(any(max(p) >= 2 for p in ps) for ps in fs[d].values())
                       for d in (3, 4, 5))
        assert counts == expected
        triangle_cores = 0
        caps = []
        P, S = {}, {}
        for d in (3, 4, 5):
            ordinary_fibers = [[p for p in ps if ordinary(p, d)]
                               for ps in fs[d].values()]
            caps.append(max(map(len, ordinary_fibers)))
            P[d] = sum(len(ps) * (len(ps) - 1) // 2 for ps in ordinary_fibers)
            S[d] = 0
            for ps in ordinary_fibers:
                for p, q in combinations(ps, 2):
                    tails_p = {i for i, z in enumerate(p) if z == 1}
                    tails_q = {i for i, z in enumerate(q) if z == 1}
                    S[d] += not (tails_p & tails_q)
                if d == 4 and len(ps) == 3:
                    edges = [{i for i, z in enumerate(p) if z == 1} for p in ps]
                    use = set().union(*edges)
                    if len(use) == 3 and all(sum(i in e for e in edges) == 2 for i in use):
                        triangle_cores += 1
        assert P[4] == 4 * P[3] + S[4]
        assert P[5] == 6 * P[3] + 2 * S[4] + S[5]
        assert S[5] <= 28
        assert max(len(ps) for ps in fs[3].values()) <= 3
        assert max(caps[1:]) <= 3
        if name in ('path', 'split'):
            assert triangle_cores == 0
        else:
            assert triangle_cores == 1
            raw_shift = 10302
            core_q = 4 * raw_shift % N
            star_q = (core_q + A[3]) % N
            ps = fs[5][star_q]
            ordinary_ps = [p for p in ps if ordinary(p, 5)]
            avoiding = [p for p in ps if not ordinary(p, 5) and p[3] == 0]
            assert len(ordinary_ps) == 3 and len(avoiding) == 2
            assert sorted(sorted(p, reverse=True)[:3] for p in avoiding) == [[3, 1, 1], [5, 0, 0]]
        results.append({'name': name, 'full_valid': True, 'T3_T4_T5': counts,
                        'ordinary_caps': caps, 'quartic_triangle_cores': triangle_cores,
                        'ordinary_pair_counts': P, 'disjoint_tail_pair_counts': S})
    star_audit = audit_star_inventory(here)
    matching_audit = audit_matching_slice(here)
    out = {'scope': 'Three fixed positive cyclic controls,52 symbolic companion assignments and positive pair-lift arithmetic.',
           'controls': results,
           'star_inventory_audit': star_audit,
           'restricted_matching_slice_audit': matching_audit,
           'boundary': 'All controls have T4>88; none resolves an odd order below248.'}
    here.joinpath('stage47_independent_newclaims_check_results.json').write_text(
        json.dumps(out, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
