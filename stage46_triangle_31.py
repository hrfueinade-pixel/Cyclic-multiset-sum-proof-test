"""Fixed symbolic test: four 31 words beside an ordinary quartic triangle.

No cyclic sets, moduli, parameters, or historical searches are enumerated.
Every exclusion is a positive integer identity, canceling only powers of two.
"""
import itertools
import json
from pathlib import Path

from stage45_five_label_311 import echelon, words


def permutation_image(edges, permutation):
    return tuple(sorted((permutation[a], permutation[b]) for a, b in edges))


def symmetries():
    for first in itertools.permutations(range(3)):
        for last in itertools.permutations((3, 4)):
            yield first + last


def safe_witness(rows, base, targets):
    pivots, transform, kernels = echelon(rows)
    for counts in targets:
        vector = tuple(2 * counts[j] - 3 * base[j] - 2 * int(j >= 3)
                       for j in range(5))
        if any(sum(x * y for x, y in zip(vector, kernel)) for kernel in kernels):
            continue
        coefficients = [sum(vector[pivots[i]] * transform[i][j]
                            for i in range(len(pivots))) for j in range(len(rows))]
        if any(c.denominator & (c.denominator - 1) for c in coefficients):
            continue
        scale = max(c.denominator for c in coefficients)
        return {'counts': counts, 'unit_factor': scale,
                'multipliers': [int(c * scale) for c in coefficients]}
    return None


def main():
    targets = tuple(words(8, 5))
    records = []
    for missing in range(5):
        centers = [i for i in range(5) if i != missing]
        options = [[j for j in range(5) if j != i and not (i < 3 and j < 3)]
                   for i in centers]
        for tails in itertools.product(*options):
            edges = tuple(zip(centers, tails))
            representations = [tuple(3 * int(j == a) + int(j == b)
                                     for j in range(5)) for a, b in edges]
            rows = [tuple(a - b for a, b in zip(word, representations[0]))
                    for word in representations[1:]]
            reverse = next(((a, b) for a, b in edges if (b, a) in edges), None)
            witness = None if reverse else safe_witness(rows, representations[0], targets)
            records.append({'edges': edges, 'reverse_edge': reverse,
                            'rival': witness})
    permutations = tuple(symmetries())
    orbit_keys = {min(permutation_image(r['edges'], p) for p in permutations)
                  for r in records}
    residual = [r for r in records if not r['reverse_edge'] and not r['rival']]
    summary = {'assignments': len(records), 'symmetry_orbits': len(orbit_keys),
               'reverse_edge_exclusions': sum(bool(r['reverse_edge']) for r in records),
               'positive_rivals': sum(bool(r['rival']) for r in records),
               'unexcluded': len(residual),
               'scope': 'Four 31 words on B beside an ordinary quartic triangle; only positive dyadic identities exclude.'}
    Path('stage46_triangle_31_results.json').write_text(
        json.dumps({'summary': summary, 'records': records}, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(summary, indent=2))
    if residual:
        print(json.dumps(residual[:3], indent=2))


if __name__ == '__main__':
    main()
