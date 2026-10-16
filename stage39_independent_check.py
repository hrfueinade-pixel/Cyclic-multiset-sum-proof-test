"""Positive-witness audit: weak compositions, no discovery imports/numpy.

Rebuilds cubic fibers, dilation intersections, quartic fibers and all 6435
eight-term representations. Also inspects every 5+3 split of the witness.
Negative search coverage is not audited or certified by this program.
"""
import json
from collections import defaultdict
from itertools import combinations
from math import gcd
from pathlib import Path


def compositions(total, slots, prefix=()):
    if slots == 1:
        yield prefix + (total,)
    else:
        for c in range(total + 1):
            yield from compositions(total - c, slots - 1, prefix + (c,))


def fibers(a, n, degree):
    out = defaultdict(list)
    for c in compositions(degree, len(a)):
        out[sum(x * y for x, y in zip(a, c)) % n].append(c)
    return out


def main():
    source = json.loads(Path('stage39_cubic_overlap_results.json').read_text())
    w = source['witness']
    assert w is not None
    n, a = w['N'], tuple(w['A'])
    assert n % 2 and 207 <= n < 248 and len(a) == len(set(a)) == 8
    f3, f4, f8 = (fibers(a, n, k) for k in (3, 4, 8))
    cubics = []
    for inds in combinations(range(8), 3):
        c = tuple(int(i in inds) for i in range(8))
        r = sum(a[i] for i in inds) % n
        assert f3[r] == [c]
        cubics.append({'indices': list(inds), 'residue': r})
    assert len(cubics) == 56 and sum(map(len, f3.values())) == 120
    overlap = []
    for t in range(n):
        pairs = [(i, j) for i in range(8) for j in range(8) if (2 * a[i] - a[j]) % n == t]
        if pairs:
            assert len({i for i, j in pairs}) == len(pairs)
            assert len({j for i, j in pairs}) == len(pairs)
            overlap.append({'shift': t, 'pairs': [list(p) for p in pairs], 'size': len(pairs)})
    assert sum(r['size'] for r in overlap) == 64
    maximum = max(r['size'] for r in overlap)
    assert maximum == w['maximum_overlap'] <= 5
    rivals = [c for c in f8[sum(a) % n] if c != (1,) * 8]
    assert sum(map(len, f8.values())) == 6435 and rivals
    q = {sum(a[i] for i in inds) % n for inds in combinations(range(8), 4)}
    failures = []
    for inds in combinations(range(8), 4):
        c = tuple(int(i in inds) for i in range(8))
        r = sum(a[i] for i in inds) % n
        for alt in f4[r]:
            if c != alt:
                failures.append({'squarefree': list(c), 'alternative': list(alt), 'residue': r})
    split_rows = []
    for inds in combinations(range(8), 5):
        b = [a[i] for i in inds]
        c = [a[i] for i in range(8) if i not in inds]
        sb = sum(b) % n
        sc = sum(c) % n
        fb = {k: set(fibers(b, n, k)) for k in range(5, 9)}
        deviations = { (sum(x * y for x, y in zip(c, v)) - sc) % n
                       for v in compositions(3, 3) if v != (1, 1, 1) }
        holes5 = {(sb - r) % n for r in range(n) if r not in fb[5]}
        q5 = deviations <= holes5
        q6 = all((sb + sc - r) % n not in fb[6] for r in fibers(c, n, 2))
        q7 = all((sb + sc - r) % n not in fb[7] for r in c)
        q8 = (sb + sc) % n not in fb[8]
        split_rows.append({'B_indices': list(inds), 'B': b, 'C': c,
                           'holes5': len(holes5), 'deviations_distinct': len(deviations),
                           'q5': q5, 'q6': q6, 'q7': q7, 'q8': q8})
    assert len(split_rows) == 56
    # Deliberate corruptions: wrong mass, and equal mass but changed residue.
    alt = list(rivals[0])
    alt[0] += 1
    assert sum(alt) != 8
    alt = list(rivals[0])
    j = next(j for j in range(1, 8) if alt[j])
    alt[j] -= 1
    alt[0] += 1
    assert sum(alt) == 8 and sum(x * y for x, y in zip(a, alt)) % n != sum(a) % n
    cohort_source = json.loads(Path('stage39_cubic_cohort_results.json').read_text())
    saved_blocks = json.loads(Path('stage39_fiveblock_results.json').read_text())
    by_key = {(r['N'], tuple(r['A'])): r for r in saved_blocks['rows']}
    cohort_audits = []
    classes = defaultdict(list)
    for row in cohort_source['witnesses']:
        cn, ca = row['N'], tuple(row['A'])
        c3, c4, c8 = (fibers(ca, cn, k) for k in (3, 4, 8))
        assert all(c3[sum(ca[i] for i in inds) % cn] == [tuple(int(i in inds) for i in range(8))]
                   for inds in combinations(range(8), 3))
        mq = max(len({2 * x % cn for x in ca} & {(x + t) % cn for x in ca}) for t in range(cn))
        assert mq == row['maximum_overlap'] <= 5
        quartics = [(sum(ca[i] for i in inds) % cn,
                     tuple(int(i in inds) for i in range(8))) for inds in combinations(range(8), 4)]
        qsize = len({r for r, _ in quartics})
        assert qsize in (69, 70)
        # Cubic protection forces every alternative quartic to have disjoint support.
        for r, qcounts in quartics:
            for alt in c4[r]:
                if alt != qcounts:
                    assert all(not (x and y) for x, y in zip(alt, qcounts))
        crivals = [v for v in c8[sum(ca) % cn] if v != (1,) * 8]
        assert all(sum(x > 0 for x in v) <= 4 for v in crivals)
        protected4 = sum(c4[r] == [v] for r, v in quartics)
        canonical = min(tuple(sorted((x - u) * pow(v - u, -1, cn) % cn for x in ca))
                        for u in ca for v in ca if gcd(v - u, cn) == 1)
        classes[(cn, canonical)].append(list(ca))
        saved = by_key[(cn, ca)]
        assert (saved['sumset3'], saved['squarefree4_distinct'], saved['protected_quartics'],
                saved['eight_term_rival_count']) == (len(c3), qsize, protected4, len(crivals))
        eligible, joint, mindeficit = 0, 0, None
        pass_counts = dict.fromkeys(('q5', 'q6', 'q7', 'q8', 'joint'), 0)
        for inds in combinations(range(8), 5):
            cb = [ca[i] for i in inds]
            cc = [ca[i] for i in range(8) if i not in inds]
            csb, csc = sum(cb) % cn, sum(cc) % cn
            b5 = fibers(cb, cn, 5)
            # Exact quintic validity, and the separate support-cancellation challenge.
            bvalid = b5[csb] == [(1,) * 5]
            assert all(v == (1,) * 5 or sum(x > 0 for x in v) == 1 for v in b5[csb])
            if not bvalid or gcd(cn, *(x - cb[0] for x in cb)) != 1:
                continue
            eligible += 1
            sets = {k: set(fibers(cb, cn, k)) for k in (5, 6, 7, 8)}
            vals = [(csb + csc - sum(x * y for x, y in zip(cc, v))) % cn
                    for v in compositions(3, 3) if v != (1, 1, 1)]
            flags = [all(r not in sets[5] for r in vals),
                     all((csb + csc - r) % cn not in sets[6] for r in fibers(cc, cn, 2)),
                     all((csb + csc - r) % cn not in sets[7] for r in cc),
                     (csb + csc) % cn not in sets[8]]
            for key, value in zip(('q5', 'q6', 'q7', 'q8'), flags):
                pass_counts[key] += value
            pass_counts['joint'] += all(flags)
            shadow_deficit = len(sets[5] & {(sum(ca) - r) % cn for r in c3}) - 1
            assert all(flags) == (shadow_deficit == 0)
            mindeficit = shadow_deficit if mindeficit is None else min(mindeficit, shadow_deficit)
        assert eligible == saved['primitive_valid5_splits']
        assert pass_counts == saved['split_pass_counts']
        assert mindeficit == saved['minimum_hole_shadow_deficit']
        cohort_audits.append({'N': cn, 'A': list(ca), 'cubic_protected': True,
                              'maximum_overlap': mq, 'Q4_distinct': qsize,
                              'rivals_checked': len(crivals), 'eight_multisets_checked': 6435,
                              'all_splits_checked': 56, 'hole_counts_verified': True})
    assert len(cohort_audits) == len(by_key)
    midpoint_probe = json.loads(Path('stage39_midpoint_probe_results.json').read_text())
    near_audits = []
    for cn, row in midpoint_probe['best'].items():
        cn, ca = int(cn), row['A']
        cf = fibers(ca, cn, 3)
        loss = sum(len(cf[sum(ca[i] for i in inds) % cn]) - 1 for inds in combinations(range(8), 3))
        mq = max(len({2 * x % cn for x in ca} & {(x + t) % cn for x in ca}) for t in range(cn))
        midpoint = any((2 * sum(ca[i] for i in inds) - sum(ca)) % cn == 0 for inds in combinations(range(8), 4))
        assert (loss, mq, midpoint) == (row['cubic_loss'], row['maximum_overlap'], row['midpoint_quartic_collision'])
        near_audits.append({'N': cn, 'A': ca, 'cubic_loss': loss, 'maximum_overlap': mq,
                            'midpoint_quartic_collision': midpoint})
    control_a, control_n = tuple((1 << i) - 1 for i in range(8)), 255
    control3 = fibers(control_a, control_n, 3)
    control8 = fibers(control_a, control_n, 8)
    assert control8[sum(control_a) % control_n] == [(1,) * 8]
    for inds in combinations(range(8), 5):
        cb = [control_a[i] for i in inds]
        b5 = fibers(cb, control_n, 5)
        assert b5[sum(cb) % control_n] == [(1,) * 5]
        assert set(b5) & {(sum(control_a) - r) % control_n for r in control3} == {sum(cb) % control_n}
    assert saved_blocks['valid255_control']['split_pass_counts']['joint'] == 56
    out = {'status': 'POSITIVE_WITNESS_VERIFIED', 'N': n, 'A': list(a),
           'cubic_protected': True, 'cubic_multisets_checked': 120,
           'cubic_singletons': cubics, 'maximum_dilation_overlap': maximum,
           'nonempty_overlap_fibers': overlap, 'sumset3': len(f3), 'sumset4': len(f4),
           'squarefree4_distinct': len(q), 'quartic_failures': failures,
           'eight_multisets_checked': 6435, 'valid8': False,
           'eight_term_rivals': [list(c) for c in rivals],
           'all_five_three_splits': split_rows,
           'split_pass_counts': {key: sum(r[key] for r in split_rows) for key in ('q5', 'q6', 'q7', 'q8')},
           'split_joint_pass': sum(all(r[k] for k in ('q5', 'q6', 'q7', 'q8')) for r in split_rows),
           'corrupted_rivals_rejected': 2,
           'cohort_audits': cohort_audits, 'cohort_affine_classes': len(classes),
           'affine_class_representatives': [{'N': k[0], 'normalized': list(k[1]), 'members': v}
                                          for k, v in sorted(classes.items())],
           'near_witness_audits': near_audits,
           'valid255_control_independently_checked': True,
           'total_eight_multisets_checked': 6435 * (2 + len(cohort_audits)),
           'original_problem_counterexample': False, 'new_modulus_exclusion': False}
    Path('stage39_independent_results.json').write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps({k: v for k, v in out.items() if k not in ('cubic_singletons',
         'nonempty_overlap_fibers', 'quartic_failures', 'all_five_three_splits', 'cohort_audits',
         'affine_class_representatives', 'eight_term_rivals')}, indent=2))


if __name__ == '__main__':
    main()
