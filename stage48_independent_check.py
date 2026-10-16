"""Standalone count-vector audit of midpoint complement rivals.

No producers or prior-stage engines imported. No cyclic set search.
"""
from itertools import combinations
from collections import defaultdict
import json
from pathlib import Path


def main():
    here = Path(__file__).parent
    data = json.loads((here / 'stage48_saturation_diagonal_probe_results.json').read_text())
    expected = {(u, v) for u in combinations(range(3, 8), 3)
                for v in combinations(range(3, 8), 3) if u != v}
    got = set()
    for record in data['positive_rivals']:
        u, v = map(tuple, record['tails'])
        got.add((u, v))
        O, Op = [0] * 8, [0] * 8
        O[1], Op[2] = 2, 2
        for i in u: O[i] = 1
        for i in v: Op[i] = 1
        rows = [tuple(O[i] - Op[i] for i in range(8)),
                tuple(2 * O[i] - 1 - 2 * (i == 0) for i in range(8))]
        assert record['rows'] == [list(r) for r in rows]
        r = tuple(2 + 2 * (i == 0) - O[i] - Op[i] for i in range(8))
        assert tuple(record['rival']) == r
        assert min(r) >= 0 and sum(r) == 8 and r != (1,) * 8
        assert r[0] == 4
        assert tuple(r[i] - 1 for i in range(8)) == tuple(rows[0][i] - rows[1][i] for i in range(8))
        assert record['unit_multiplier'] == 1
        assert record['relation_multipliers'] == [1, -1]
    assert got == expected and len(got) == 90 and not data['row_span_test_residual']
    # Exhaust the finite overlap presentations, including midpoint labels
    # overlapping ordinary centers and tails. No group values are assigned.
    cases = diagonal = original_exceptions = 0
    midpoint_pairs = list(combinations(range(8), 2)) + [(i, i) for i in range(8)]
    for a, b in combinations(range(8), 2):
        others = [i for i in range(8) if i not in (a, b)]
        tails = list(combinations(others, 3))
        for U in tails:
            for V in tails:
                O, Op = [0] * 8, [0] * 8
                O[a], Op[b] = 2, 2
                for i in U: O[i] = 1
                for i in V: Op[i] = 1
                assert max(x + y for x, y in zip(O, Op)) <= 2
                for c, d in midpoint_pairs:
                    r = tuple(2 + (i == c) + (i == d) - O[i] - Op[i] for i in range(8))
                    assert min(r) >= 0 and sum(r) == 8
                    exception = c != d and {c, d} == {a, b} and not (set(U) & set(V))
                    assert (r == (1,) * 8) == exception
                    cases += 1
                    original_exceptions += exception
                    if c == d:
                        diagonal += 1
                        assert r[c] >= 2 and r != (1,) * 8
    assert cases == 403200 and diagonal == 89600 and original_exceptions == 560
    injection_cases = injection_direct_rivals = 0
    for center in range(8):
        for i, j in combinations([x for x in range(8) if x != center], 2):
            for U in combinations([x for x in range(8) if x not in (center, i)], 3):
                for V in combinations([x for x in range(8) if x not in (center, j)], 3):
                    left, right = [0] * 8, [0] * 8
                    for x in U: left[x] += 1
                    for x in V: right[x] += 1
                    left[j] += 1
                    right[i] += 1
                    assert left[i] == 0 and right[i] >= 1
                    assert left != right
                    both_repeated = max(left) >= 2 and max(right) >= 2
                    assert both_repeated == (j in U and i in V)
                    injection_cases += 1
                    if both_repeated:
                        r = [0] * 8
                        r[center] = 4
                        for x in U: r[x] += 1
                        for x in V: r[x] += 1
                        r[i] -= 1
                        r[j] -= 1
                        assert min(r) >= 0 and sum(r) == 8 and r[i] == r[j] == 0
                        injection_direct_rivals += 1
    assert injection_cases == 67200 and injection_direct_rivals == 16800
    graph_counts = {'triangle': 0, 'star': 0, 'path': 0, 'split': 0}
    vertices = set(range(5))
    for edges in combinations(list(combinations(range(5), 2)), 3):
        E = [set(e) for e in edges]
        degrees = sorted((sum(i in e for e in E) for i in vertices), reverse=True)
        kind = {(2,2,2,0,0): 'triangle', (3,1,1,1,0): 'star',
                (2,2,1,1,0): 'path', (2,1,1,1,1): 'split'}[tuple(degrees)]
        graph_counts[kind] += 1
        disjoint = sum(not(a & b) for a, b in combinations(E, 2))
        assert disjoint == {'triangle': 0, 'star': 0, 'path': 1, 'split': 2}[kind]
        quintic_tails = [vertices - e for e in E]
        common = set.intersection(*quintic_tails)
        assert len(common) == {'triangle': 2, 'star': 1, 'path': 1, 'split': 0}[kind]
        if kind in ('star', 'path'):
            lifted_edges = [tail - common for tail in quintic_tails]
            use = set.union(*lifted_edges)
            target_kind = 'triangle' if kind == 'star' else 'path'
            assert len(use) == (3 if target_kind == 'triangle' else 4)
            if target_kind == 'triangle':
                assert all(sum(i in e for e in lifted_edges) == 2 for i in use)
            else:
                assert sorted(sum(i in e for e in lifted_edges) for i in use) == [1,1,2,2]
            reconstructed = [e | common for e in lifted_edges]
            assert reconstructed == quintic_tails
    assert graph_counts == {'triangle': 10, 'star': 20, 'path': 60, 'split': 30}
    A = (0,101,303,707,1515,3131,6363,1)
    modulus = 12827
    def words(degree):
        for bars in combinations(range(degree + 7), 7):
            b = (-1,) + bars + (degree + 7,)
            yield tuple(b[i + 1] - b[i] - 1 for i in range(8))
    fs = {}
    for degree in (3,4,5,8):
        fd = defaultdict(list)
        for p in words(degree):
            fd[sum(a * z for a, z in zip(A, p)) % modulus].append(p)
        fs[degree] = fd
    assert fs[8][sum(A) % modulus] == [(1,) * 8]
    counts = {str(d): sum(any(max(p) >= 2 for p in ps) for ps in fs[d].values()) for d in (3,4,5)}
    assert counts == {'3': 43, '4': 127, '5': 260}
    def ordinary(p,d):
        return p.count(2) == 1 and p.count(1) == d-2 and p.count(0) == 9-d
    caps = {str(d): max(sum(ordinary(p,d) for p in ps) for ps in fs[d].values()) for d in (3,4,5)}
    assert caps == {'3': 2, '4': 3, '5': 3}
    assert max(map(len,fs[3].values())) == 2
    classes = {str(d): {'triangle':0,'star':0,'path':0,'split':0} for d in (4,5)}
    cubic_triples = disjoint_double = 0
    for ps in fs[3].values():
        cubic_triples += sum(ordinary(p,3) for p in ps) == 3
    for degree in (4,5):
        for ps in fs[degree].values():
            os = [p for p in ps if ordinary(p,degree)]
            if degree == 4 and len(os) == 2:
                disjoint_double += not ({i for i,z in enumerate(os[0]) if z == 1} &
                                        {i for i,z in enumerate(os[1]) if z == 1})
            if len(os) != 3: continue
            centers = {p.index(2) for p in os}
            remaining = set(range(8)) - centers
            edges = [{i for i,z in enumerate(p) if z == 1} for p in os]
            if degree == 5: edges = [remaining - e for e in edges]
            ds = sorted((sum(i in e for e in edges) for i in remaining), reverse=True)
            kind = {(2,2,2,0,0):'triangle',(3,1,1,1,0):'star',
                    (2,2,1,1,0):'path',(2,1,1,1,1):'split'}[tuple(ds)]
            classes[str(degree)][kind] += 1
    delta_set = {(a-b) % modulus for a in A for b in A if a != b}
    h = sum(2*d % modulus not in delta_set for d in delta_set)//2
    r3 = sum((len(ps)-1)*(len(ps)-2)//2 for ps in fs[3].values() if any(max(p)>=2 for p in ps))
    assert h == 7 and r3 == 0 and cubic_triples == 0 and disjoint_double == 7
    assert classes['4']['triangle'] == 7 and classes['4']['split'] == 0 and classes['5']['split'] == 0
    lhs = 5*classes['4']['triangle'] + 4*classes['5']['split']
    rhs = 2*(h+r3)+2*cubic_triples+5*classes['4']['split']+disjoint_double
    assert (lhs,rhs) == (35,21)
    control = {'actual_cyclic_labels':A,'modulus':modulus,'full_valid':True,'T_counts':counts,
               'ordinary_caps':caps,'h':h,'R3':r3,'triple_graph_counts':classes,
               'C3ordinary':cubic_triples,'S4double':disjoint_double,
               'weighted_left':lhs,'weighted_right':rhs,
               'boundary':'Refutes an unconditional weighted lemma; T4=127>88 and large N.'}
    # Integer accounting for the endpoint example, not a residue search.
    N, k, t = 247, 11, 144
    assert N == 92 + k + t and 2 * (t - 140) == 8
    result = {'scope': 'Fixed midpoint count-vector identities and exact overlap classification.',
              'positive_diagonal_models_checked': 90, 'units_canceled': [],
              'midpoint_overlap_presentations': cases, 'diagonal_presentations': diagonal,
              'only_original_exceptions': original_exceptions,
              'exception_class': 'offdiagonal midpoint labels equal the two ordinary centers, with disjoint complementary tails',
              'diagonal_center_injection_presentations': injection_cases,
              'diagonal_center_injection_positive_rival_presentations': injection_direct_rivals,
              'three_edge_classification_checked': graph_counts,
              'path_lift_correction': 'A quintic omitted-edge path has one common tail label, recovering a quartic path.',
              'unconditional_weighted_lemma_counterexample': control,
              'global_necessary_relation': '3*(N-236-h-R3+n3)>=4+M+delta',
              'coordinator_global_coupling_accepted_deductively': '2N>=496+2(h+R3)-4n3+3C4+S4',
              'global_no_triple_consequence': 'N>=248+h+R3+3C4/2+S4/2',
              'refined_global_necessity_accepted_deductively':
                  '5C4triangle+4C5split>=2+2(h+R3)+2C3ordinary+5C4split+S4double under N<=247',
              'boundary': 'Does not establish the full N>=248 theorem; quartic-triangle or genuine quintic-split systems still require closure.'}
    (here / 'stage48_independent_check_results.json').write_text(
        json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
