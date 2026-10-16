"""Small symbolic follow-up to the hand proof for quartic triangles.

Tests three accompanying 31 words, up to S3 x S2 symmetry, by positive
mass-eight identities. A surviving row space is not asserted realizable.
"""
import itertools
import json
from pathlib import Path

from stage45_five_label_311 import rival, words
from stage46_triangle_31 import permutation_image, symmetries


def main():
    permutations = tuple(symmetries())
    orbits = {}
    for centers in itertools.combinations(range(5), 3):
        options = [[j for j in range(5) if j != i and not (i < 3 and j < 3)]
                   for i in centers]
        for tails in itertools.product(*options):
            edges = tuple(zip(centers, tails))
            key = min(permutation_image(edges, p) for p in permutations)
            orbits.setdefault(key, []).append(edges)
    targets = tuple(word for word in words(8, 8) if word != (1,) * 8)
    ordinary = [tuple(2 * int(j == 5 + i) + int(j < 3 and j != i)
                      for j in range(8)) for i in range(3)]
    records = []
    for edges, members in sorted(orbits.items()):
        mixed = [tuple(3 * int(j == a) + int(j == b) for j in range(8))
                 for a, b in edges]
        representations = ordinary + mixed
        rows = [tuple(a - b for a, b in zip(word, representations[0]))
                for word in representations[1:]]
        witness, rank = rival(rows, targets)
        records.append({'edges': edges, 'orbit_size': len(members),
                        'rational_rank': rank, 'rival': witness})
    summary = {'assignments': sum(map(len, orbits.values())), 'orbits': len(orbits),
               'positive_rival_orbits': sum(bool(r['rival']) for r in records),
               'unexcluded_orbits': sum(not r['rival'] for r in records),
               'boundary': 'Unexcluded means no saved dyadic rival, not feasibility.'}
    Path('stage46_three_31_probe_results.json').write_text(
        json.dumps({'summary': summary, 'records': records}, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(summary, indent=2))
    print(json.dumps([r for r in records if not r['rival']], indent=2))


if __name__ == '__main__':
    main()
