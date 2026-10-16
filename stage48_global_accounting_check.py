"""Fixed scalar/graph diagnostic and the declared equality control.

No cyclic-set or modulus search. The scalar record is NOT a realization.
It checks which simultaneous information is lost by aggregate equations.
"""
from itertools import combinations, combinations_with_replacement
from pathlib import Path
import json


def edge(a, b):
    return tuple(sorted((a, b)))


def degrees(edges):
    out = [0] * 8
    for a, b in edges:
        out[a] += 1
        out[b] += 1
    return out


def main():
    complete = set(combinations(range(8), 2))
    cycle = {edge(i, (i + 1) % 8) for i in range(8)}
    cubic_graph = complete - cycle
    midpoint_graph = (cycle | {edge(i, (i + 2) % 8) for i in range(8)}) - {(0, 1)}
    triple_centers = [(0, 1, 2), (3, 4, 5), (0, 1, 6), (2, 3, 7)]
    v = [sum(i in triple for triple in triple_centers) for i in range(8)]
    dc, ds = degrees(cubic_graph), degrees(midpoint_graph)
    singles = [35 + v[i] - 6 * dc[i] - ds[i] for i in range(8)]
    N, h, R3 = 247, 6, 0
    k = h + R3
    P3, P4, P5, S4, S5 = 20, 80, 135, 0, 15
    n1, n2, n3, C4, M, delta = 22, 123, 4, 0, 0, 0
    T3, T4, T5 = 42, 88, 149
    assert len(cubic_graph) == P3 and dc == [5] * 8
    assert len(midpoint_graph) == S5 and ds == [3, 3, 4, 4, 4, 4, 4, 4]
    assert v == [2, 2, 2, 2, 1, 1, 1, 1]
    assert singles == [4, 4, 3, 3, 2, 2, 2, 2] and sum(singles) == n1
    assert 280 == n1 + 2 * n2 + 3 * n3
    assert P5 == n2 + 3 * n3
    assert P4 == 4 * P3 + S4
    assert P5 == 6 * P3 + 2 * S4 + S5
    assert T4 == 168 - P4 + C4
    assert T5 == 140 + (n1 - n3) // 2 + M
    assert T3 == 36 + k and N == 56 + T3 + T5 + delta
    assert N >= 71 + 2 * T4
    assert 36 <= S5 + n1 + M + delta
    assert 8 <= n1 + M + delta
    assert all(singles[i] >= 1 for i in range(8))
    assert all((ds[i] - (35 - singles[i] + v[i])) % 2 == 0 for i in range(8))
    assert all(35 - singles[i] - v[i] >= 0 for i in range(8))
    assert 2 * N >= 496 + 2 * k - 4 * n3 + 3 * C4 + S4
    # Cubic multiplicity cap: 20 ordinary pairs, 2 ordinary/pure pairs,
    # 14 ordinary singles and 6 pure singles. This is only a count record.
    assert 20 * 2 + 2 + 14 == 56 and 2 + 6 == 8
    assert 20 + 2 + 14 + 6 == T3
    assert 28 - h == 20 + 2 and 28 - k == 20 + 2

    # The lower-bound target is weak, and equality really is attainable.
    A = (0, 1, 3, 7, 15, 31, 63, 127)
    target = sum(A) % 248
    matches = [w for w in combinations_with_replacement(range(8), 8)
               if sum(A[i] for i in w) % 248 == target]
    assert matches == [tuple(range(8))]
    bit_targets = [255 + 248 * j for j in range(4)]
    assert bit_targets == [255, 503, 751, 999]
    assert all(x.bit_count() == 8 for x in bit_targets)
    assert all(x > 255 for x in bit_targets[1:])
    result = {
        'scope': 'One fixed scalar/center-graph record, not a cyclic realization; one declared positive equality control.',
        'scalar_record': {'N': N, 'h': h, 'R3': R3, 'k': k, 'T3': T3,
                          'T4': T4, 'T5': T5, 'P3ordinary': P3,
                          'P4ordinary': P4, 'P5ordinary': P5,
                          'S4': S4, 'S5': S5, 'n1': n1, 'n2': n2,
                          'n3': n3, 'C4': C4, 'M5': M, 'delta': delta},
        'cubic_pair_center_edges': sorted(cubic_graph),
        'S5_center_edges': sorted(midpoint_graph),
        'putative_split_triple_centers': triple_centers,
        'ordinary_single_center_counts': singles,
        'boundary': 'This record is feasible only for aggregate equations. The separate three-class tail/lift check rejects its P3ordinary=20,C4=0 pattern. No tails or group labels are supplied here; this is not a cyclic realization or a refutation of the target.',
        'equality_control': {'N': 248, 'A': A, 'mass_eight_words_checked': 6435,
                             'target_residue': target, 'representations': matches,
                             'translated_integer_targets': bit_targets},
        'complete_N_ge_248_proof': False,
    }
    (Path(__file__).parent / 'stage48_global_accounting_check_results.json').write_text(
        json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
