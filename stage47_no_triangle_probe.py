"""Fixed symbolic path/split controls, not a cyclic-set or modulus search.

Enumerate words only in two declared free-abelian coefficient models.
No discovered absence is an arbitrary odd-group exclusion.
"""
import json
from collections import defaultdict
from itertools import combinations
from pathlib import Path


def words(n, degree, prefix=()):
    if n == 1:
        yield prefix + (degree,)
        return
    for x in range(degree + 1):
        yield from words(n - 1, degree - x, prefix + (x,))


def image(word, rows):
    return tuple(sum(c * r[j] for c, r in zip(word, rows)) for j in range(5))


def ordinary(word):
    return sorted(x for x in word if x) == [1, 1, 1, 2]


def ordinary4(word):
    return sorted(x for x in word if x) == [1, 1, 2]


def ordinary3(word):
    return sorted(x for x in word if x) == [1, 2]


def pair_counts(fibers, degree, predicate):
    intersections = defaultdict(int)
    triples = 0
    for ws in fibers.values():
        ow = [w for w in ws if predicate(w)]
        triples += len(ow) == 3
        for left, right in combinations(ow, 2):
            lc, rc = left.index(2), right.index(2)
            assert not right[lc] and not left[rc]
            common = sum(1 for i in range(8) if left[i] == right[i] == 1)
            intersections[common] += 1
    return {'pairs': sum(intersections.values()), 'by_tail_intersection': dict(intersections),
            'triple_fibers': triples}


def run(name, edges):
    rows = [(0, 0, 0, 0, 0), (2, 0, 0, 0, 0),
            (0, 2, 0, 0, 0), (0, 0, 2, 0, 0), (0, 0, 0, 2, 0)]
    halves = [(0, 0, 0, 0), (1, 0, 0, 0),
              (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]
    for a, b in edges:
        rows.append(tuple(halves[a][j] + halves[b][j] for j in range(4)) + (1,))
    fibers = {}
    for d in (3, 4, 5, 8):
        f = defaultdict(list)
        for w in words(8, d):
            f[image(w, rows)].append(w)
        fibers[d] = f
    original = (1,) * 8
    rivals = [w for w in fibers[8][image(original, rows)] if w != original]
    assert not rivals, (name, rivals)
    tris4 = []
    triples5 = []
    for val, ws in fibers[4].items():
        ordinary_ws = [w for w in ws if ordinary4(w)]
        if len(ordinary_ws) >= 3:
            tris4.append((val, ordinary_ws))
    for val, ws in fibers[5].items():
        ow = [w for w in ws if ordinary(w)]
        if len(ow) >= 3:
            triples5.append({'value': val, 'centers': [w.index(2) for w in ow],
                             'words': ow})
    parameters = [1, 17, 289, 4913, 83521]
    labels = [sum(a * b for a, b in zip(row, parameters)) for row in rows]
    modulus = 8 * max(labels) + 1
    assert len(set(labels)) == 8
    target = sum(labels) % modulus
    numerical_rivals = [w for w in words(8, 8)
                        if sum(c * a for c, a in zip(w, labels)) % modulus == target
                        and w != original]
    assert not numerical_rivals
    counts = {str(d): len([1 for val, ws in fibers[d].items()
                          if any(max(w) >= 2 for w in ws)]) for d in (3, 4, 5)}
    caps = {'cubic': max(len(ws) for val, ws in fibers[3].items()
                          if any(max(w) >= 2 for w in ws)),
            'ordinary_quartic': max(sum(ordinary4(w) for w in ws)
                                     for ws in fibers[4].values()),
            'ordinary_quintic': max(sum(ordinary(w) for w in ws)
                                     for ws in fibers[5].values())}
    pair_info = {str(d): pair_counts(fibers[d], d, pred)
                 for d, pred in [(3, ordinary3), (4, ordinary4), (5, ordinary)]}
    p3 = pair_info['3']['pairs']
    s4 = pair_info['4']['by_tail_intersection'].get(0, 0)
    s5 = pair_info['5']['by_tail_intersection'].get(0, 0)
    assert pair_info['4']['pairs'] == 4 * p3 + s4
    assert pair_info['5']['pairs'] == 6 * p3 + 2 * s4 + s5
    triangle4 = []
    for val, ws in tris4:
        tails = [{i for i, c in enumerate(w) if c == 1} for w in ws]
        if len(set().union(*tails)) == 3:
            triangle4.append((val, ws))
    ordinary5_values = sum(any(ordinary(w) for w in ws) for ws in fibers[5].values())
    mixed_only5_values = sum(any(max(w) >= 2 for w in ws) and not any(ordinary(w) for w in ws)
                            for ws in fibers[5].values())
    output = {'name': name, 'coefficient_rows': rows, 'declared_edges': edges,
              'formal_full_validity': True, 'formal_T_counts': counts,
              'formal_ordinary_quartic_triples': tris4,
              'formal_ordinary_quintic_triples': triples5,
              'formal_ordinary_quartic_triangle_cores': triangle4,
              'ordinary_pair_counts': pair_info,
              'ordinary_quintic_output_values': ordinary5_values,
              'mixed_only_quintic_output_values': mixed_only5_values,
              'formal_caps': caps, 'fixed_cyclic_control': {
                  'labels': labels, 'modulus': modulus,
                  'checked_mass_eight_words': 6435, 'rivals': numerical_rivals}}
    return output


if __name__ == '__main__':
    controls = [run('path', [(0, 1), (1, 2), (2, 3)]),
                run('split', [(0, 1), (1, 2), (3, 4)])]
    result = {'scope': 'Two fixed symbolic controls; no parameter or modulus sweep.',
              'controls': controls}
    Path('stage47_no_triangle_probe_results.json').write_text(
        json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps([{'model': x['name'], 'T': x['formal_T_counts'],
                       'quartic_triples': len(x['formal_ordinary_quartic_triples']),
                       'quintic_triples': len(x['formal_ordinary_quintic_triples']),
                       'caps': x['formal_caps']} for x in controls]))
