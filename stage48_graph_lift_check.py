"""Standalone finite combinatorial check of the new recoverable graph lifts.

No research discovery imports or numerical group parameters.
"""
from itertools import combinations
from collections import Counter
from pathlib import Path
import json


def graph_type(edges):
    degrees = Counter(v for e in edges for v in e)
    shape = sorted(degrees.values())
    return {[2, 2, 2].__repr__(): 'triangle',
            [1, 1, 1, 3].__repr__(): 'star',
            [1, 1, 2, 2].__repr__(): 'path',
            [1, 1, 1, 1, 2].__repr__(): 'split'}[repr(shape)]


def main():
    labels = set(range(5))
    all_edges = list(combinations(labels, 2))
    tally = Counter()
    records = []
    for omitted in combinations(all_edges, 3):
        shape = graph_type(omitted)
        tails = [labels-set(e) for e in omitted]
        common = set.intersection(*tails)
        if shape == 'triangle':
            assert len(common) == 2
            reduced = [t-common for t in tails]
            assert all(len(t) == 1 for t in reduced)
            assert len(set().union(*reduced)) == 3
        elif shape in ('star', 'path'):
            assert len(common) == 1
            reduced = [t-common for t in tails]
            assert graph_type(reduced) == ('triangle' if shape == 'star' else 'path')
            assert set.intersection(*reduced) == set()
            assert all((r|common) == t for r, t in zip(reduced, tails))
        else:
            assert len(common) == 0
            reduced = None
        tally[shape] += 1
        records.append({'omitted_edges': omitted, 'shape': shape,
                        'tail_intersection': sorted(common),
                        'reduced_tails': [sorted(x) for x in reduced] if reduced else None})
    assert dict(tally) == {'triangle': 10, 'star': 20, 'path': 60, 'split': 30}
    quartic_tally = Counter()
    for tails in combinations(all_edges, 3):
        shape = graph_type(tails)
        disjoint_pairs = sum(set(a).isdisjoint(b) for a, b in combinations(tails, 2))
        assert disjoint_pairs == {'triangle': 0, 'star': 0, 'path': 1, 'split': 2}[shape]
        if shape == 'star':
            common = set.intersection(*(set(e) for e in tails))
            assert len(common) == 1
            reduced = [set(e)-common for e in tails]
            assert all(len(x) == 1 for x in reduced)
            assert len(set().union(*reduced)) == 3
        quartic_tally[shape] += 1
    result = {'scope': 'All120 three-edge subsets on five abstract vertices.',
              'quintic_omitted_edge_shapes': dict(tally),
              'quartic_tail_shapes': dict(quartic_tally),
              'checked_inverse_removals': records,
              'boundary': 'Finite combinatorial shape verification; fullvalidity and ordinary caps '
                          'remain separate mathematical premises for fiber bijections.'}
    Path('stage48_graph_lift_check_results.json').write_text(
        json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(dict(tally)))


if __name__ == '__main__':
    main()
