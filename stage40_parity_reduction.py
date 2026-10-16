"""Finite word identities and one historical binary control; no exclusion search.

The mathematical equivalence is proved in stage40_findings.md. This script
records its support/parity arithmetic and why a naive two-cube packing fails.
It does not enumerate eight-term residues or re-certify any old exclusions.
"""
import itertools
import json
from collections import Counter


def count_vectors(degree, length=8):
    for word in itertools.combinations_with_replacement(range(length), degree):
        yield tuple(word.count(i) for i in range(length))


def main():
    parity = Counter()
    types = Counter()
    for c in count_vectors(8):
        if sum(x > 0 for x in c) > 3:
            continue
        odd = tuple(i for i, x in enumerate(c) if x % 2)
        assert len(odd) in (0, 2)
        if odd:
            v = tuple((x - (i in odd)) // 2 for i, x in enumerate(c))
            assert sum(v) == 3
            p, q = odd
        else:
            w = [x // 2 for x in c]
            p = q = next(i for i, x in enumerate(w) if x)
            w[p] -= 1
            v = tuple(w)
            assert sum(v) == 3
        reconstructed = [2*x for x in v]
        reconstructed[p] += 1
        reconstructed[q] += 1
        assert tuple(reconstructed) == c
        parity[str(len(odd))] += 1
        types[''.join(map(str, sorted((x for x in c if x), reverse=True)))] += 1

    n = 255
    a = (0, 1, 3, 7, 15, 31, 63, 127)
    s = sum(a) % n
    subset = {sum(a[i+1] for i in range(7) if mask >> i & 1) % n
              for mask in range(128)}
    doubled = {2*x % n for x in subset}
    triple = {sum(x*y for x, y in zip(c, a)) % n for c in count_vectors(3)}
    pair = {sum(x*y for x, y in zip(c, a)) % n for c in count_vectors(2)}
    quartic = {sum(x*y for x, y in zip(c, a)) % n for c in count_vectors(4)}
    parity_sumset = {(2*x+y) % n for x in triple for y in pair}
    assert len(subset) == 128
    assert s not in parity_sumset
    result = {
        'scope': 'support<=3 degree-eight words and one historical N=255 control',
        'support_at_most_three_words': sum(parity.values()),
        'odd_support_histogram': dict(parity),
        'multiplicity_types': dict(types),
        'binary_control': {
            'N': n, 'A': a, 's': s, 'subset_cube_size': len(subset),
            'cube_dilation_intersection_size': len(subset & doubled),
            'cube_dilation_intersection': sorted(subset & doubled),
            'sizes_2A_3A_4A': [len(pair), len(triple), len(quartic)],
            's_in_2dot3A_plus_2A': s in parity_sumset,
            'parity_sumset_size': len(parity_sumset),
            'validity_boundary': 'Validity is historical and has an elementary binary-carry proof; this script does not re-enumerate degree-eight residues.'
        },
        'boundary': 'No modulus below 248 is searched or excluded. Word enumeration validates a reduction, not the unproved covering lemma.'
    }
    with open('stage40_parity_reduction_results.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2)
        f.write('\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
