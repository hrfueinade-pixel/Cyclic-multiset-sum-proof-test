"""Standalone coordinate checks of complement duality and midpoint rivals.

These are identities on count words, not a search over cyclic sets or orders.
The universal deductions still require the hypotheses stated in the report.
"""
from itertools import combinations, combinations_with_replacement
import json
from pathlib import Path


def main():
    b = set(range(2, 8))
    tails = list(combinations(sorted(b), 3))
    pairs = fixed = 0
    for u in tails:
        for v in tails:
            # Orient the ordinary pair with private centers 0,1.
            row = tuple((2 if i == 0 else -2 if i == 1 else 0)
                        + int(i in u) - int(i in v) for i in range(8))
            du, dv = b - set(v), b - set(u)
            dual = tuple((2 if i == 0 else -2 if i == 1 else 0)
                         + int(i in du) - int(i in dv) for i in range(8))
            assert row == dual
            assert b - dv == set(u) and b - du == set(v)
            is_fixed = du == set(u) and dv == set(v)
            assert is_fixed == (not (set(u) & set(v)))
            fixed += is_fixed
            pairs += 1
    assert (pairs, fixed) == (400, 20)
    assert len(tails) == 20
    assert len(list(combinations(range(1, 8), 3))) == 35
    # Any fifth-degree word containing a pair produces the stated midpoint
    # rival if its VALUE equals the midpoint. Check mass/positivity/parity
    # with repetitions in the pair explicitly included.
    midpoint_cases = diagonal_cases = 0
    for labels in combinations_with_replacement(range(8), 5):
        p = tuple(labels.count(i) for i in range(8))
        for c in range(8):
            for d in range(c, 8):
                r = tuple(2*p[i] - int(i == c) - int(i == d) for i in range(8))
                contains = p[c] >= 1 and p[d] >= 1
                assert (min(r) >= 0) == contains
                if contains:
                    assert sum(r) == 8 and r != (1,)*8
                    assert sum(x % 2 for x in r) == (0 if c == d else 2)
                    midpoint_cases += 1
                    diagonal_cases += c == d
    # Packing arithmetic in the four near-saturated no-triple cases.
    cases = [(15, 247, 140, 4), (14, 247, 141, 3),
             (13, 245, 140, 4), (13, 247, 142, 2)]
    for k, n, upper, edges in cases:
        assert upper == n - 92 - k
        surplus = upper - 140
        assert edges == 4 - surplus
        assert n >= 232 + k and n % 2 == 1
    out = {'status': 'PASS', 'tail_pair_coordinate_checks': pairs,
           'complement_involution_fixed_points': fixed,
           'midpoint_rival_count_cases': midpoint_cases,
           'diagonal_midpoint_cases': diagonal_cases,
           'near_saturated_cases': cases,
           'boundary': 'Only universal word identities and packing arithmetic; '
                       'no assertion that the saturated systems exist or are excluded.'}
    Path(__file__).with_name('stage47_structural_check_results.json').write_text(
        json.dumps(out, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
