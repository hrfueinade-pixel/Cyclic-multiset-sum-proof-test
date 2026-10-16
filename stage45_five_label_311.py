"""Fixed symbolic test of four 311 quintics on five fully protected labels.

The four tripled centers are normalized to 0,1,2,3. Each tail is one of
six pairs on the other four labels: exactly 6**4 symbolic assignments.
No group, modulus, or parameter search; only explicit multiplied rivals.
"""
import gzip
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path


def words(total, length):
    for indices in itertools.combinations_with_replacement(range(length), total):
        yield tuple(indices.count(i) for i in range(length))


def echelon(rows):
    width = len(rows[0])
    a = [[Fraction(x) for x in row] for row in rows]
    transform = [[Fraction(int(i == j)) for j in range(len(rows))] for i in range(len(rows))]
    pivots = []
    for column in range(width):
        pivot = next((i for i in range(len(pivots), len(a)) if a[i][column]), None)
        if pivot is None:
            continue
        i = len(pivots)
        a[i], a[pivot] = a[pivot], a[i]
        transform[i], transform[pivot] = transform[pivot], transform[i]
        scale = a[i][column]
        a[i] = [x / scale for x in a[i]]
        transform[i] = [x / scale for x in transform[i]]
        for j in range(len(a)):
            if j != i and a[j][column]:
                scale = a[j][column]
                a[j] = [x - scale * y for x, y in zip(a[j], a[i])]
                transform[j] = [x - scale * y for x, y in zip(transform[j], transform[i])]
        pivots.append(column)
    kernels = []
    for column in range(width):
        if column not in pivots:
            vector = [Fraction(0)] * width
            vector[column] = Fraction(1)
            for i, pivot in enumerate(pivots):
                vector[pivot] = -a[i][column]
            scale = math.lcm(*(x.denominator for x in vector))
            kernels.append(tuple(int(x * scale) for x in vector))
    return pivots, transform[:len(pivots)], kernels


def rival(rows, targets):
    pivots, transform, kernels = echelon(rows)
    for counts in targets:
        f = tuple(x - 1 for x in counts)
        if any(sum(x * y for x, y in zip(f, vector)) for vector in kernels):
            continue
        coefficients = [sum(Fraction(f[pivots[i]]) * transform[i][j] for i in range(len(pivots))) for j in range(len(rows))]
        if any(x.denominator & (x.denominator - 1) for x in coefficients):
            continue
        scale = max(x.denominator for x in coefficients)
        return {'rival': counts, 'unit_factor': scale, 'multipliers': [int(x * scale) for x in coefficients]}, len(pivots)
    return None, len(pivots)


def main():
    targets = [word for word in words(5, 5) if word != (1,) * 5]
    tails = [tuple(itertools.combinations([j for j in range(5) if i != j], 2)) for i in range(4)]
    excluded, residual = [], []
    for pairs in itertools.product(*tails):
        representations = [tuple(3 * int(j == i) + int(j in pair) for j in range(5)) for i, pair in enumerate(pairs)]
        rows = [tuple(x - y for x, y in zip(word, representations[0])) for word in representations[1:]]
        witness, rank = rival(rows, targets)
        record = {'tails': pairs, 'rows': rows, 'rational_rank': rank}
        if witness:
            excluded.append({**record, **witness})
        else:
            residual.append(record)
    data = {'excluded': excluded, 'residual': residual,
            'boundary': 'Only explicit power-of-two rival identities exclude patterns. Residual row spaces need not be realized in any cyclic group.'}
    Path('stage45_five_label_311_inventory.json.gz').write_bytes(gzip.compress(json.dumps(data, separators=(',', ':')).encode(), mtime=0))
    summary = {'patterns': len(excluded) + len(residual), 'explicit_rivals': len(excluded),
               'unresolved': len(residual), 'residual_ranks': {str(r): sum(x['rational_rank'] == r for x in residual) for r in range(4)},
               'boundary': data['boundary']}
    Path('stage45_five_label_311_results.json').write_text(json.dumps(summary, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
