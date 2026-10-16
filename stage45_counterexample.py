"""Fixed full-valid counterexample to the local 311 multiplicity cap three.

One integer kernel embedding from a symbolic configuration, with three
free-digit extensions. This is not a modulus or parameter sweep.
"""
import gzip
import json
from collections import defaultdict
from pathlib import Path

from stage43_fourpair_inventory import words
from stage43_relation_growth import run


def audit(points, modulus):
    target = sum(points) % modulus
    all_words = list(words(8)) if len(points) == 8 else None
    if all_words is None:
        import itertools
        all_words = [tuple(indices.count(i) for i in range(5)) for indices in itertools.combinations_with_replacement(range(5), 5)]
    hits = [word for word in all_words if sum(word[i] * points[i] for i in range(len(points))) % modulus == target]
    assert hits == [(1,) * len(points)]
    result = {'N': modulus, 'A': points, 'target': target, 'full_word_checks': len(all_words), 'unique_original': True}
    if len(points) == 8:
        for degree in (3, 4, 5):
            repeated, ordinary, mixed311 = defaultdict(list), defaultdict(list), defaultdict(list)
            for word in words(degree):
                value = sum(word[i] * points[i] for i in range(8)) % modulus
                if max(word) > 1:
                    repeated[value].append(word)
                shape = tuple(sorted(x for x in word if x))
                if shape == tuple(sorted([2] + [1] * (degree - 2))):
                    ordinary[value].append(word)
                if degree == 5 and shape == (1, 1, 3):
                    mixed311[value].append(word)
            result[f'T{degree}'] = len(repeated)
            result[f'max_total_{degree}'] = max(map(len, repeated.values()))
            result[f'max_ordinary_{degree}'] = max(map(len, ordinary.values()))
            if degree == 5:
                result['mixed311_fiber_80'] = mixed311[80]
                result['all_quintic_words_at_80'] = repeated[80]
                result['max_mixed311'] = max(map(len, mixed311.values()))
    return result


def main():
    five = (0, 14, 15, 17, 21)
    eight = five + (1000, 10000, 100000)
    results = {'five_control': audit(five, 107), 'eight_control': audit(eight, 800001),
               'boundary': 'Actual large-odd full-valid counterexample to a local 311 cap. It does not satisfy the small quartic budget or contradict N>=248.'}
    results['complete_pattern'] = {
        'point_order': ['a', 'b', 'c', 'd', 'e'],
        'equal_words': '3a+b+c=3b+a+d=3c+b+d=3d+a+e',
        'rows': [[-2, 2, -1, 1, 0], [-3, 0, 2, 1, 0], [-2, -1, -1, 3, 1]],
        't_definition': 't=c-b', 'normalized_weights': [17, 14, 15, 21, 0],
        'parameterization_multipliers': [[8, -5, -1], [7, -4, -1], [7, -4, -1], [10, -6, -1]],
        'boundary': 'Integer identities prove a-e=17t,b-e=14t,c-e=15t,d-e=21t over every abelian group; no nonunit division or torsion branch omitted.'}
    model = {'id': 's45_four311', 'rows': [(x, 0, 0, 0) for x in five] + [(0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)],
             'torsion_rows': [0] * 8, 'torsion_order': 1, 'direction': [],
             'parameterization': '0,14t,15t,17t,21t,u,v,w; four mixed quintics equal 80t identically.'}
    results['model'] = model
    retained = Path('stage43_s45_four311_degree4_units2_certificate.json.gz')
    if retained.exists():
        certificate = json.loads(gzip.decompress(retained.read_bytes()))
        assert certificate['model'] == json.loads(json.dumps(model))
        results['growth'] = {'model': model['id'], 'positive_bound': len(certificate['words']),
                             'pair_records': len(certificate['pairs']), 'certificate': retained.name,
                             'degree': 4, 'units': [2], 'reused_positive_certificate': True}
    else:
        results['growth'] = run(model, 4, 89, [2])
    Path('stage45_counterexample_results.json').write_text(json.dumps(results, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(results, indent=2))


if __name__ == '__main__':
    main()
