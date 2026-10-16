"""Finite cubic-relation inventory for four doubled pairs, not group search.

Classify formal cubic equalities up to permuting the four pairs and changing
the equality's sign. Only powers of two are canceled in the group proof.
"""
import itertools
import json
import math
from pathlib import Path


def words(degree):
    for indices in itertools.combinations_with_replacement(range(8), degree):
        yield tuple(indices.count(i) for i in range(8))


def paired(c):
    return tuple(c[i]+2*c[i+4] for i in range(4))


def cancel_two(d):
    d = tuple(d)
    while any(d) and all(x % 2 == 0 for x in d):
        d = tuple(x//2 for x in d)
    return d


def canonical(d):
    d = cancel_two(d)
    return min(tuple(sorted(d)), tuple(sorted(-x for x in d)))


def parameter_rows(d):
    pivot = next((i for i,x in enumerate(d) if x and abs(x) & (abs(x)-1) == 0), None)
    if pivot is None:
        return None
    scale = abs(d[pivot])
    other = [i for i in range(4) if i != pivot]
    rows = [[0]*4 for _ in range(4)]
    for j,i in enumerate(other):
        rows[i][j] = scale
        rows[pivot][j] = -d[i]*(1 if d[pivot] > 0 else -1)
    centers = tuple(map(tuple,rows))
    return centers+tuple(tuple(2*x for x in row) for row in centers)


def main():
    base = (3,)*4
    forbidden = {}
    for c in words(8):
        if c == (1,)*8:
            continue
        f = tuple(x-y for x,y in zip(paired(c),base))
        assert any(f)
        forbidden.setdefault(f,c)
    cubic = {}
    for c in words(3):
        if max(c) > 1:
            cubic.setdefault(paired(c),c)
    classes = {}
    for left,right in itertools.combinations(cubic,2):
        raw = tuple(x-y for x,y in zip(left,right))
        d = canonical(raw)
        classes.setdefault(d, {'direction':d,'pairs_in_class':0})['pairs_in_class'] += 1
    output = []
    for d,entry in sorted(classes.items()):
        witness = None
        for scale in range(-16,17):
            if scale:
                f = tuple(scale*x for x in d)
                if f in forbidden:
                    witness = {'rival':forbidden[f], 'multiplier':scale}
                    break
        rows = parameter_rows(d)
        entry.update({'direct_rival':witness, 'unit_pivot_available':rows is not None})
        if witness is None and rows is not None:
            entry['model_rows'] = rows
            entry['formal_cubic_values'] = len({tuple(sum(c[i]*rows[i][j] for i in range(8)) for j in range(4)) for c in words(3) if max(c)>1})
        output.append(entry)
    result = {'formal_cubic_values':len(cubic), 'unordered_formal_pairs':math.comb(len(cubic),2),
              'classes':output, 'permitted_classes':[e['direction'] for e in output if e['direct_rival'] is None],
              'boundary':'Complete fixed cubic-word inventory under pair permutations, sign, and safe doubling cancellation. No parameter or modulus values enumerated. No growth exclusion follows from inventory alone.'}
    Path('stage43_fourpair_inventory_results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k != 'classes'},indent=2))


if __name__ == '__main__':
    main()
