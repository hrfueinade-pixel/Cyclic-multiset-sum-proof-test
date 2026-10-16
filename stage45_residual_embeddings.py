"""Fixed formal kernel diagnostic, not a search over cyclic parameters.

Choose a nonconstant integer kernel basis vector for each residual symbolic
row matrix. Testing its 126 degree-five words distinguishes a genuine
torsion-free local counterexample from missing odd-torsion exclusions.
Stop after the first counterexample if found.
"""
import gzip
import json
from pathlib import Path

from stage45_five_label_311 import echelon, words


def main():
    inventory = json.loads(gzip.decompress(Path('stage45_five_label_311_inventory.json.gz').read_bytes()))
    degree_five = list(words(5, 5))
    result = {'examined': 0, 'distinct_models': 0, 'counterexample': None, 'formal_rivals': []}
    for index, record in enumerate(inventory['residual']):
        result['examined'] += 1
        _, _, kernels = echelon(record['rows'])
        weights = next(k for k in kernels if len(set(k)) > 1)
        weights = tuple(x - min(weights) for x in weights)
        if len(set(weights)) != 5:
            result['formal_rivals'].append({'index': index, 'weights': weights, 'coincident_labels': True})
            continue
        result['distinct_models'] += 1
        hits = [word for word in degree_five if sum(word[i] * weights[i] for i in range(5)) == sum(weights)]
        if hits == [(1,) * 5]:
            result['counterexample'] = {'index': index, 'weights': weights, 'tails': record['tails'], 'hits': hits}
            break
        result['formal_rivals'].append({'index': index, 'weights': weights, 'rival': next(word for word in hits if word != (1,) * 5)})
    result['boundary'] = 'One formal kernel embedding per residual configuration; no odd-torsion branch excluded by a torsion-free diagnostic.'
    Path('stage45_residual_embeddings_results.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items() if k != 'formal_rivals'}, indent=2))


if __name__ == '__main__':
    main()
