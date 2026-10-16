"""Targeted hole-placement experiment on the discovered cubic cohort.

Inspect every 5+3 split of saved positive witnesses, plus N=255 valid control.
This is a finite cohort, not a census or exclusion of any modulus.
"""
import json
from collections import Counter, defaultdict
from itertools import combinations, combinations_with_replacement
from math import gcd
from pathlib import Path


def table(a, n, degree):
    out = defaultdict(list)
    for w in combinations_with_replacement(range(len(a)), degree):
        out[sum(a[i] for i in w) % n].append(w)
    return out


def inspect(n, a):
    cubic = table(a, n, 3)
    assert all(len(cubic[sum(a[i] for i in w) % n]) == 1 for w in combinations(range(8), 3))
    f4 = table(a, n, 4)
    protected4 = sum(len(f4[sum(a[i] for i in w) % n]) == 1 for w in combinations(range(8), 4))
    q4 = {sum(a[i] for i in w) % n for w in combinations(range(8), 4)}
    assert len(q4) in (69, 70)
    overlaps = Counter((2 * x - y) % n for x in a for y in a)
    target = sum(a) % n
    rivals = [w for w in combinations_with_replacement(range(8), 8)
              if w != tuple(range(8)) and sum(a[i] for i in w) % n == target]
    assert all(len(set(w)) <= 4 for w in rivals)
    if protected4 == 70:
        assert all(len(set(w)) <= 3 for w in rivals)
    split_rows = []
    for inds in combinations(range(8), 5):
        b = [a[i] for i in inds]
        c = [a[i] for i in range(8) if i not in inds]
        sb, sc = sum(b) % n, sum(c) % n
        levels = {k: set(table(b, n, k)) for k in range(5, 9)}
        holes = {k: {(sb - x) % n for x in range(n) if x not in levels[k]} for k in range(5, 9)}
        for k in (5, 6, 7):
            eroded = {x for x in holes[k] if all((x + y) % n in holes[k] for y in b)}
            # b need not contain zero: do not restrict the erosion center to H_k.
            if 0 not in b:
                eroded = {x for x in range(n) if all((x + y) % n in holes[k] for y in b)}
            assert eroded == holes[k + 1]
        deviations = {(sum(c[i] for i in w) - sc) % n
                      for w in combinations_with_replacement(range(3), 3) if w != (0, 1, 2)}
        q5 = deviations <= holes[5]
        q6 = all((r - sc) % n in holes[6] for r in table(c, n, 2))
        q7 = all((r - sc) % n in holes[7] for r in c)
        q8 = (-sc) % n in holes[8]
        joint = q5 and q6 and q7 and q8
        shadow = {(x - sc) % n for x in cubic if x != sc}
        assert joint == (shadow <= holes[5])
        intersection = levels[5] & {(target - x) % n for x in cubic}
        assert joint == (intersection == {sb})
        five_words = table(b, n, 5)[sb]
        valid5 = five_words == [tuple(range(5))]
        # Cubic protection cancels every five-term rival with support >=2.
        assert all(w == tuple(range(5)) or len(set(w)) == 1 for w in five_words)
        primitive = gcd(n, *(x - b[0] for x in b)) == 1
        split_rows.append({'B': b, 'C': c, 'primitive': primitive, 'valid5': valid5,
                           'sumset5': len(levels[5]), 'holes5': len(holes[5]),
                           'intersection_5B_s_minus_3A': len(intersection),
                           'q5': q5, 'q6': q6, 'q7': q7, 'q8': q8, 'joint': joint})
    eligible = [r for r in split_rows if r['primitive'] and r['valid5']]
    joint_rows = [r for r in eligible if r['joint']]
    return {'N': n, 'A': a, 'cubic_protected': True,
            'maximum_dilation_overlap': max(overlaps.values()), 'sumset3': len(cubic),
            'squarefree4_distinct': len(q4), 'protected_quartics': protected4,
            'eight_term_rival_count': len(rivals),
            'rival_support_histogram': dict(Counter(len(set(w)) for w in rivals)),
            'first_rival': [rivals[0].count(i) for i in range(8)] if rivals else None,
            'all_splits': 56, 'primitive_valid5_splits': len(eligible),
            'split_pass_counts': {key: sum(r[key] for r in eligible) for key in ('q5', 'q6', 'q7', 'q8', 'joint')},
            'joint_pass_splits': joint_rows,
            'minimum_hole_shadow_deficit': min((r['intersection_5B_s_minus_3A'] - 1 for r in eligible), default=None)}


def main():
    source = json.loads(Path('stage39_cubic_cohort_results.json').read_text())
    keys = {(w['N'], tuple(w['A'])) for w in source['witnesses']}
    rows = [inspect(n, list(a)) for n, a in sorted(keys)]
    control = inspect(255, [0, 1, 3, 7, 15, 31, 63, 127])
    assert control['eight_term_rival_count'] == 0 and control['split_pass_counts']['joint'] == 56
    out = {'status': 'COMPLETE_SAVED_COHORT', 'cohort_size': len(rows), 'rows': rows,
           'valid255_control': control, 'primitive_valid5_joint_witnesses':
           sum(bool(r['joint_pass_splits']) for r in rows),
           'Q70_low_overlap_witnesses': sum(r['squarefree4_distinct'] == 70 and r['maximum_dilation_overlap'] <= 5 for r in rows),
           'new_modulus_exclusion': False, 'general_hole_lemma_proved': False}
    Path('stage39_fiveblock_results.json').write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps({k: v for k, v in out.items() if k not in ('rows', 'valid255_control')}, indent=2))
    for r in rows:
        if r['joint_pass_splits'] or r['squarefree4_distinct'] == 70:
            print(json.dumps(r))


if __name__ == '__main__':
    main()
