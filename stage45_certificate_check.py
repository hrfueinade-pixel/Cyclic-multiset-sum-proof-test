"""Independent checks of Stage 45's local counterexample and positive evidence.

No discovery, row-reduction, embedding, or earlier research modules imported.
An unresolved symbolic configuration is never counted as an exclusion.
"""
import gzip
import itertools
import json
import math
from collections import defaultdict
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def power_two(n):
    return isinstance(n, int) and n > 0 and n & (n - 1) == 0


def compositions(total, length):
    if length == 1:
        yield (total,)
    else:
        for first in range(total + 1):
            for rest in compositions(total - first, length - 1):
                yield (first,) + rest


def rows_from_tails(tails):
    words = [tuple(3 * int(j == i) + int(j in pair) for j in range(5)) for i, pair in enumerate(tails)]
    return [tuple(x - y for x, y in zip(word, words[0])) for word in words[1:]]


def minor(matrix, columns):
    return sum((-1 if sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3)) % 2 else 1)
               * math.prod(matrix[i][columns[p[i]]] for i in range(3)) for p in itertools.permutations(range(3)))


def check_inventory_rival(record):
    rows = rows_from_tails(record['tails'])
    require(rows == [tuple(row) for row in record['rows']], 'Wrong collision equations')
    c = record['rival']
    require(len(c) == 5 and all(isinstance(x, int) and x >= 0 for x in c) and sum(c) == 5 and c != [1] * 5, 'Wrong five-term rival')
    r = record['unit_factor']
    multipliers = record['multipliers']
    require(power_two(r) and len(multipliers) == 3 and all(isinstance(x, int) for x in multipliers), 'Unsafe cancellation or multipliers')
    require(all(r * (c[i] - 1) == sum(multipliers[j] * rows[j][i] for j in range(3)) for i in range(5)), 'Wrong multiplied rival')


def full_audit(points, modulus):
    n = len(points)
    all_original_degree = list(compositions(n, n))
    target = sum(points) % modulus
    hits = [word for word in all_original_degree if sum(x * y for x, y in zip(word, points)) % modulus == target]
    require(hits == [(1,) * n], 'Invalid declared set')
    result = {'N': modulus, 'A': points, 'target': target, 'full_word_checks': len(all_original_degree), 'unique_original': True}
    for degree in (3, 4, 5):
        repeated, ordinary, mixed = defaultdict(list), defaultdict(list), defaultdict(list)
        for word in compositions(degree, n):
            y = sum(x * a for x, a in zip(word, points)) % modulus
            shape = tuple(sorted(x for x in word if x))
            if max(word) > 1:
                repeated[y].append(word)
            if shape == tuple(sorted([2] + [1] * (degree - 2))):
                ordinary[y].append(word)
            if degree == 5 and shape == (1, 1, 3):
                mixed[y].append(word)
        if n == 8:
            result[f'T{degree}'] = len(repeated)
            result[f'max_total_{degree}'] = max(map(len, repeated.values()))
            result[f'max_ordinary_{degree}'] = max(map(len, ordinary.values()))
        if degree == 5:
            result['max_mixed311'] = max(map(len, mixed.values()))
            result['fiber_80'] = repeated.get(80, [])
            result['mixed311_at_80'] = mixed.get(80, [])
    return result


def check_growth(data):
    model = {'id': 's45_four311', 'rows': [[x, 0, 0, 0] for x in (0, 14, 15, 17, 21)] + [[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]],
             'torsion_rows': [0] * 8, 'torsion_order': 1, 'direction': [],
             'parameterization': '0,14t,15t,17t,21t,u,v,w; four mixed quintics equal 80t identically.'}
    require(data['model'] == model and data['degree'] == 4 and data['units'] == [2], 'Wrong or unbound growth model')
    def parse(text, degree):
        require(len(text) == 8 and text.isdigit(), 'Malformed word')
        word = tuple(map(int, text))
        require(sum(word) == degree, 'Wrong word mass')
        return word
    def value(word):
        return tuple(sum(word[i] * model['rows'][i][j] for i in range(8)) for j in range(4))
    target = value((1,) * 8)
    words = [parse(text, 4) for text in data['words']]
    require(len(words) == 92 and len(set(words)) == 92 and all(max(word) > 1 for word in words), 'Wrong selected quartics')
    require(len(data['pairs']) == math.comb(len(words), 2), 'Missing pair witnesses')
    for (left, right), witness in zip(itertools.combinations(words, 2), data['pairs']):
        rival = parse(witness['rival'], 8)
        require(rival != (1,) * 8, 'Original word as rival')
        r, k = witness['canceled_unit_factor'], witness['multiplier']
        require(power_two(r) and isinstance(k, int) and k != 0, 'Unsafe growth multiplier')
        require(all(r * (a - b) == k * (x - y) for a, b, x, y in zip(value(rival), target, value(left), value(right))), 'Wrong growth pair equation')
    return len(data['pairs'])


def main():
    packed = json.loads(gzip.decompress(Path('stage45_certificates.json.gz').read_bytes()))
    inventory = packed['inventory']
    allowed = [tuple(itertools.combinations([j for j in range(5) if i != j], 2)) for i in range(4)]
    expected = set(itertools.product(*allowed))
    for record in inventory['excluded'] + inventory['residual']:
        key = tuple(tuple(pair) for pair in record['tails'])
        require(key in expected, 'Invalid or duplicate symbolic assignment')
        expected.remove(key)
        rows = rows_from_tails(key)
        require(rows == [tuple(row) for row in record['rows']], 'Wrong inventory row')
        rank_three = any(minor(rows, columns) for columns in itertools.combinations(range(5), 3))
        if record in inventory['residual']:
            require(record['rational_rank'] == 3 and rank_three, 'Wrong residual rational rank')
        else:
            check_inventory_rival(record)
    require(not expected and len(inventory['excluded']) == 714 and len(inventory['residual']) == 582, 'Incomplete inventory')
    five = full_audit((0, 14, 15, 17, 21), 107)
    binary_five = full_audit((1, 2, 4, 8, 16), 31)
    require(binary_five['max_mixed311'] == 3, 'Invalid first cap-two counterexample')
    eight = full_audit((0, 14, 15, 17, 21, 1000, 10000, 100000), 800001)
    require(len(eight['mixed311_at_80']) == len(eight['fiber_80']) == 4, 'Missing fourfold mixed counterexample')
    require(eight['max_total_3'] == 2 and eight['max_ordinary_4'] == eight['max_ordinary_5'] == 2, 'Local-cap counterexample premise fails')
    require(eight['T4'] == 229 and eight['T3'] == 60 and eight['T5'] == 601, 'Wrong output counts')
    counter = packed['counterexample']
    require(counter['five_control']['A'] == list(five['A']) and counter['five_control']['N'] == five['N'], 'Wrong five control')
    for key in ('A', 'N', 'target', 'full_word_checks', 'unique_original', 'T3', 'T4', 'T5', 'max_total_3', 'max_ordinary_4', 'max_ordinary_5', 'max_mixed311'):
        require(counter['eight_control'][key] == (list(eight[key]) if key == 'A' else eight[key]), 'Wrong reported control: ' + key)
    pair_count = check_growth(packed['growth_certificate'])
    complete = counter['complete_pattern']
    rows = [[-2, 2, -1, 1, 0], [-3, 0, 2, 1, 0], [-2, -1, -1, 3, 1]]
    require(complete['rows'] == rows and complete['normalized_weights'] == [17, 14, 15, 21, 0], 'Wrong complete pattern')
    for i, w in enumerate((17, 14, 15, 21)):
        target = [int(j == i) - int(j == 4) + w * int(j == 1) - w * int(j == 2) for j in range(5)]
        multipliers = complete['parameterization_multipliers'][i]
        require(all(isinstance(x, int) for x in multipliers) and len(multipliers) == 3, 'Noninteger coverage proof')
        require(all(target[j] == sum(multipliers[k] * rows[k][j] for k in range(3)) for j in range(5)), 'Incomplete group parametrization')
    diagnostic = packed['embedding_diagnostic']
    require(diagnostic['examined'] == 3 and diagnostic['counterexample']['weights'] == [17, 14, 15, 21, 0], 'Wrong fixed kernel diagnostic')
    require([tuple(e) for e in diagnostic['counterexample']['tails']] == [tuple(e) for e in inventory['residual'][2]['tails']], 'Diagnostic not bound to its configuration')
    for row in inventory['residual'][2]['rows']:
        require(sum(x * y for x, y in zip(row, (17, 14, 15, 21, 0))) == 0, 'Wrong kernel embedding')
    orbit = set()
    original = ((1, 2), (0, 3), (1, 3), (0, 4))
    for permutation in itertools.permutations(range(4)):
        p = permutation + (4,)
        image = [None] * 4
        for i, tail in enumerate(original):
            image[p[i]] = tuple(sorted(p[j] for j in tail))
        orbit.add(tuple(image))
    residual_keys = {tuple(tuple(tail) for tail in record['tails']) for record in inventory['residual']}
    require(orbit <= residual_keys, 'Pattern orbit not in residual inventory')
    for alteration in ('mass', 'original', 'unit'):
        broken = dict(inventory['excluded'][0])
        if alteration == 'mass':
            broken['rival'] = [0] * 5
        elif alteration == 'original':
            broken['rival'] = [1] * 5
        else:
            broken['unit_factor'] = 3
        try:
            check_inventory_rival(broken)
        except ValueError:
            pass
        else:
            raise ValueError('Corrupt witness accepted: ' + alteration)
    result = {'symbolic_assignments_checked': 1296, 'safe_rivals_checked': 714,
              'unexcluded_symbolic_assignments': 582, 'five_full_word_checks': five['full_word_checks'],
              'binary_five_full_word_checks': binary_five['full_word_checks'],
              'eight_full_word_checks': eight['full_word_checks'], 'mixed311_fiber_80': eight['fiber_80'],
              'local_cap_three_refuted': True, 'existing_multiplicity_caps_satisfied': True,
              'counterexample_T4': eight['T4'], 'family_T4_positive_bound': 92,
              'growth_pair_witnesses_checked': pair_count,
              'complete_mixed_pattern_excluded': True, 'symmetry_equivalent_patterns_closed': len(orbit),
              'still_unexcluded_symbolic_assignments': 582 - len(orbit),
              'boundary': 'Large-odd counterexample to a local mixed-fiber lemma; one complete mixed collision pattern excluded below248 by integer coverage and quartic growth. Global N>=248 remains open; other residual patterns are not excluded.'}
    Path('stage45_certificate_check_results.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
