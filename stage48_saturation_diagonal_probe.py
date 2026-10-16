"""All 90 labelled ordinary-pair presentations at one diagonal midpoint.

Only test explicit dyadic/triadic row-span mass-eight rivals. Lack of a
witness is not an exclusion, group model, or complete proof search.
"""
from itertools import combinations
from math import gcd
from pathlib import Path
import json


def words(n, degree, prefix=()):
    if n == 1:
        yield prefix + (degree,)
    else:
        for x in range(degree + 1):
            yield from words(n - 1, degree - x, prefix + (x,))


def units23(x):
    x = abs(x)
    for p in (2, 3):
        while x and x % p == 0:
            x //= p
    return x == 1


def main():
    tails = list(combinations(range(3, 8), 3))
    candidates = [w for w in words(8, 8) if w != (1,) * 8]
    successes, residual = [], []
    for u in tails:
        for v in tails:
            if u == v:
                continue
            left, right = [0] * 8, [0] * 8
            left[1], right[2] = 2, 2
            for i in u:
                left[i] = 1
            for i in v:
                right[i] = 1
            row1 = tuple(a - b for a, b in zip(left, right))
            row2 = tuple(2 * a - 1 - (2 if i == 0 else 0) for i, a in enumerate(left))
            pivot = next((i, j, row1[i]*row2[j] - row1[j]*row2[i])
                         for i, j in combinations(range(8), 2)
                         if row1[i]*row2[j] - row1[j]*row2[i])
            i, j, determinant = pivot
            found = None
            for rival in candidates:
                d = tuple(x - 1 for x in rival)
                alpha = d[i]*row2[j] - d[j]*row2[i]
                beta = row1[i]*d[j] - row1[j]*d[i]
                if any(determinant * d[k] != alpha*row1[k] + beta*row2[k]
                       for k in range(8)):
                    continue
                common = gcd(gcd(abs(determinant), abs(alpha)), abs(beta))
                den = abs(determinant) // common
                if not units23(den):
                    continue
                sign = 1 if determinant > 0 else -1
                found = {'rival': rival, 'unit_multiplier': den,
                         'relation_multipliers': [sign*alpha//common, sign*beta//common]}
                break
            record = {'tails': [u, v], 'tail_intersection': len(set(u) & set(v)),
                      'rows': [row1, row2]}
            if found:
                successes.append({**record, **found})
            else:
                residual.append(record)
    result = {'scope': 'One diagonal midpoint labelled0, ordinary centers1,2, '
                        'tails on labels3..7; all90 ordered distincttail assignments.',
              'hypotheses': 'The two saturated branches N245 or247; only2,3cancelled.',
              'positive_rivals': successes, 'row_span_test_residual': residual,
              'boundary': 'Residual means only no mass-eight rival in tested dyadic/triadic row span.'}
    Path('stage48_saturation_diagonal_probe_results.json').write_text(
        json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'assignments': 90, 'positive_rivals': len(successes),
                      'residual': len(residual),
                      'residual_intersections': sorted(set(x['tail_intersection'] for x in residual))}))


if __name__ == '__main__':
    main()
