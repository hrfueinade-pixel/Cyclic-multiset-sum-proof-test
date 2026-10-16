"""Independent coverage, parameter and arithmetic check of Stage 44.

No discovery or model-building modules are imported. Counts are not treated
as evidence until all graph patterns and every individual witness are checked.
"""
import gzip
import itertools
import json
import math
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def two_power(n):
    return isinstance(n, int) and n > 0 and n & (n - 1) == 0


def edge_vector(edge):
    return tuple(int(i in edge) for i in range(5))


def cross_rows(first, second):
    differences = [tuple(q - p for p, q in zip(edge_vector(a), edge_vector(b))) for a, b in zip(first, second)]
    return [tuple(x - y for x, y in zip(differences[i], differences[0])) for i in (1, 2)]


def check_tail_rival(record):
    rows = cross_rows(record['first'], record['second'])
    require(rows == [tuple(x) for x in record['rows']], 'Wrong cross rows')
    counts = record['tail_counts']
    require(len(counts) == 5 and all(isinstance(x, int) and x >= 0 for x in counts) and sum(counts) == 5, 'Wrong rival degree')
    require(counts != [1] * 5, 'Original word used as rival')
    r = record['unit_factor']
    require(two_power(r), 'Nonunit cancellation')
    multipliers = record['row_multipliers']
    require(len(multipliers) == 2 and all(isinstance(x, int) for x in multipliers), 'Wrong multipliers')
    require(all(r * (counts[k] - 1) == sum(multipliers[j] * rows[j][k] for j in range(2)) for k in range(5)), 'Wrong multiplied rival equation')


def determinant(matrix):
    return sum((-1 if (p[0] > p[1]) + (p[0] > p[2]) + (p[1] > p[2]) & 1 else 1) * math.prod(matrix[i][p[i]] for i in range(3)) for p in itertools.permutations(range(3)))


def check_model(model, residual):
    require(model['configuration'] == residual, 'Wrong coverage configuration')
    equations = [list(row[1:]) for row in cross_rows(residual['first'], residual['second'])]
    first = model['first_equation']
    require(first in equations and any(first), 'Missing first equation')
    pivot = model['first_pivot']
    scale = model['first_scale']
    require(scale == abs(first[pivot]) and two_power(scale), 'Unsafe first pivot')
    others = [i for i in range(4) if i != pivot]
    base = [[0] * 3 for _ in range(4)]
    for j, i in enumerate(others):
        base[i][j] = scale
        base[pivot][j] = -first[i] * (1 if first[pivot] > 0 else -1)
    require(model['first_rows'] == base, 'Wrong surjective first model')
    substituted = [[sum(row[i] * base[i][j] for i in range(4)) for j in range(3)] for row in equations]
    second = model['second_equation']
    transform = model['unimodular_transform']
    require(abs(determinant(transform)) == 1, 'Non-unimodular reduction')
    order = model['torsion_order']
    if second is None:
        require(not any(any(row) for row in substituted), 'Lost independent second equation')
        require(transform == [[int(i == j) for j in range(3)] for i in range(3)], 'Unexpected rank-one transform')
        require(order == 1 and model['diagonal_gcd'] == 0, 'Wrong rank-one torsion')
        require(model['second_after_first'] == [0, 0, 0], 'Wrong second metadata')
    else:
        require(second in equations, 'Wrong second equation')
        vector = [sum(second[i] * base[i][j] for i in range(4)) for j in range(3)]
        require(vector == model['second_after_first'] and any(vector), 'Wrong substituted row')
        g = math.gcd(*vector)
        require(model['diagonal_gcd'] == g, 'Wrong gcd')
        require([sum(vector[i] * transform[i][j] for i in range(3)) for j in range(3)] == [g, 0, 0], 'Wrong diagonal equation')
        odd = g
        while odd % 2 == 0:
            odd //= 2
        require(order == odd, 'Lost odd torsion')
    merged = [[sum(base[i][k] * transform[k][j] for k in range(3)) for j in range(3)] for i in range(4)]
    free = [row[1:] if second is not None else row[:] for row in merged]
    torsion = [row[0] % order if second is not None else 0 for row in merged]
    width = len(free[0])
    halves = [[0] * width] + free
    half_torsion = [0] + torsion
    rows = [[2 * x for x in row] + [0] for row in halves]
    tor = [2 * x % order for x in half_torsion]
    for i, j in residual['first']:
        rows.append([halves[i][k] + halves[j][k] for k in range(width)] + [1])
        tor.append((half_torsion[i] + half_torsion[j]) % order)
    require(model['rows'] == rows and model['torsion_rows'] == tor, 'Certificate model not the full coverage model')
    for equation in equations:
        require(all(sum(equation[i] * free[i][j] for i in range(4)) == 0 for j in range(width)), 'Free part fails relation')
        require(sum(equation[i] * torsion[i] for i in range(4)) % order == 0, 'Torsion part fails relation')


def counts(text, degree, repeated=False):
    require(len(text) == 8 and text.isdigit(), 'Malformed word')
    c = tuple(map(int, text))
    require(sum(c) == degree, 'Wrong word degree')
    if repeated:
        require(max(c) > 1, 'Squarefree word counted as repeated')
    return c


def value(c, model):
    return tuple(sum(c[i] * model['rows'][i][j] for i in range(8)) for j in range(len(model['rows'][0]))), sum(c[i] * model['torsion_rows'][i] for i in range(8)) % model['torsion_order']


def difference(a, b, order):
    return tuple(x - y for x, y in zip(a[0], b[0])), (a[1] - b[1]) % order


def check_certificate(data, model):
    require(data['model'] == model, 'Unbound certificate')
    order = model['torsion_order']
    target = value((1,) * 8, model)
    if data.get('kind') == 'direct_rival':
        rival = counts(data['rival'], 8)
        require(rival != (1,) * 8 and value(rival, model) == target, 'Wrong direct rival')
        return 0, 0
    require(data['degree'] == 4 and data['units'] == [2], 'Wrong growth degree or units')
    selected = [counts(word, 4, True) for word in data['words']]
    require(len(set(selected)) == len(selected) and len(selected) >= 89, 'Too few distinct repeated words')
    require(len(data['pairs']) == math.comb(len(selected), 2), 'Missing pair witnesses')
    for (left, right), witness in zip(itertools.combinations(selected, 2), data['pairs']):
        c = counts(witness['rival'], 8)
        require(c != (1,) * 8, 'Original word as collision witness')
        r, k = witness['canceled_unit_factor'], witness['multiplier']
        require(two_power(r) and isinstance(k, int) and k != 0, 'Unsafe multiplied equation')
        f = difference(value(c, model), target, order)
        d = difference(value(left, model), value(right, model), order)
        require(all(r * x == k * y for x, y in zip(f[0], d[0])) and (r * f[1] - k * d[1]) % order == 0, 'Wrong growth pair equation')
    return len(selected), len(data['pairs'])


def weak_words(degree):
    for indices in itertools.combinations_with_replacement(range(8), degree):
        yield tuple(indices.count(i) for i in range(8))


def ordinary_fibers(points, modulus, degree):
    shape = tuple(sorted([2] + [1] * (degree - 2)))
    fibers = {}
    for word in weak_words(degree):
        if tuple(sorted(x for x in word if x)) == shape:
            y = sum(word[i] * points[i] for i in range(8)) % modulus
            fibers.setdefault(y, []).append(word)
    return fibers


def classify_triples(fibers, degree):
    triples = {}
    for value_, words in fibers.items():
        require(len(words) <= 3, 'Control violates ordinary-cap premise')
        if len(words) != 3:
            continue
        centers = {word.index(2) for word in words}
        require(len(centers) == 3, 'Control has reused center')
        other = set(range(8)) - centers
        tails = [{i for i, x in enumerate(word) if x == 1} for word in words]
        if degree == 3:
            kind = 'cubic'
        elif degree == 4:
            vertices = set.union(*tails)
            kind = 'triangle' if len(vertices) == 3 else 'other'
        else:
            edges = [other - tail for tail in tails]
            signature = tuple(sorted(sum(i in edge for edge in edges) for i in other))
            kind = {(0, 0, 2, 2, 2): 'triangle', (0, 1, 1, 1, 3): 'star',
                    (0, 1, 1, 2, 2): 'path', (1, 1, 1, 1, 2): 'split'}[signature]
        triples[value_] = {'words': words, 'centers': centers, 'tails': tails, 'kind': kind}
    return triples


def check_controls():
    controls = []
    for name, points in (
            ('star', (0, 2, 34, 578, 9826, 83522, 83538, 83810)),
            ('triangle', (0, 2, 34, 578, 9826, 83522, 83538, 83539))):
        modulus = 670481
        target = sum(points) % modulus
        all_eight = list(weak_words(8))
        hits = [word for word in all_eight if sum(points[i] * word[i] for i in range(8)) % modulus == target]
        require(hits == [(1,) * 8], 'Invalid declared control')
        cubics = classify_triples(ordinary_fibers(points, modulus, 3), 3)
        quartics = classify_triples(ordinary_fibers(points, modulus, 4), 4)
        quintics = classify_triples(ordinary_fibers(points, modulus, 5), 5)
        cubic_outputs = set()
        for y, cubic in cubics.items():
            used = cubic['centers'] | set.union(*cubic['tails'])
            free = set(range(8)) - used
            require(len(free) == 2, 'Wrong cubic free labels')
            output = (y + sum(points[i] for i in free)) % modulus
            require(output in quintics and quintics[output]['kind'] == 'triangle', 'Cubic lift not a triangle quintic')
            require(output not in cubic_outputs, 'Noninjective cubic lift')
            cubic_outputs.add(output)
        require(cubic_outputs == {y for y, q in quintics.items() if q['kind'] == 'triangle'}, 'Incomplete triangle inverse')
        quartic_outputs = set()
        for y, quartic in quartics.items():
            if quartic['kind'] != 'triangle':
                continue
            used = quartic['centers'] | set.union(*quartic['tails'])
            free = set(range(8)) - used
            require(len(free) == 2, 'Wrong quartic free labels')
            for i in free:
                output = (y + points[i]) % modulus
                require(output in quintics and quintics[output]['kind'] == 'star', 'Quartic lift not a star quintic')
                require(output not in quartic_outputs, 'Noninjective quartic lift')
                quartic_outputs.add(output)
        require(quartic_outputs == {y for y, q in quintics.items() if q['kind'] == 'star'}, 'Incomplete star inverse')
        for centers in {tuple(sorted(q['centers'])) for q in quintics.values()}:
            group = [q for q in quintics.values() if tuple(sorted(q['centers'])) == centers]
            require(len(group) <= 2 and (len(group) < 2 or all(q['kind'] == 'star' for q in group)), 'Control contradicts shared-center rigidity')
        controls.append({'name': name, 'N': modulus, 'A': points,
                         'eight_term_multisets_checked': len(all_eight),
                         'cubic_triples': len(cubics),
                         'quartic_triangle_triples': sum(q['kind'] == 'triangle' for q in quartics.values()),
                         'quintic_triangle_triples': len(cubic_outputs), 'quintic_star_triples': len(quartic_outputs),
                         'quintic_path_triples': sum(q['kind'] == 'path' for q in quintics.values()),
                         'quintic_split_triples': sum(q['kind'] == 'split' for q in quintics.values())})
    return controls


def main():
    packed = json.loads(gzip.decompress(Path('stage44_certificates.json.gz').read_bytes()))
    inventory = packed['inventory']
    graphs = {'triangle': ((0, 1), (0, 2), (1, 2)), 'star': ((0, 1), (0, 2), (0, 3)),
              'path': ((0, 1), (1, 2), (2, 3)), 'split': ((0, 1), (1, 2), (3, 4))}
    edges = tuple(itertools.combinations(range(5), 2))
    signatures = {tuple(sorted(sum(i in e for e in graph) for i in range(5))) for graph in itertools.combinations(edges, 3)}
    require(signatures == {(0, 0, 2, 2, 2), (0, 1, 1, 1, 3), (0, 1, 1, 2, 2), (1, 1, 1, 1, 2)}, 'Incomplete graph inventory')
    def graph_orbit(graph):
        return min(tuple(sorted(tuple(sorted((p[i], p[j]))) for i, j in graph)) for p in itertools.permutations(range(5)))
    require({graph_orbit(graph) for graph in itertools.combinations(edges, 3)} == {graph_orbit(graph) for graph in graphs.values()}, 'Missing first-graph orbit')
    supplied = {}
    for record in inventory['witnesses'] + inventory['survivors']:
        key = (record['graph'], tuple(tuple(e) for e in record['second']))
        require(key not in supplied, 'Duplicate pattern')
        supplied[key] = record
    checked = 0
    residual = []
    lifts = []
    for name, first in graphs.items():
        for second in itertools.permutations(edges, 3):
            checked += 1
            key = (name, second)
            if second == first:
                require(key not in supplied, 'Original fiber declared excluded')
                continue
            require(key in supplied, 'Uncovered symbolic pattern')
            record = supplied.pop(key)
            require(record['first'] == [list(e) for e in first], 'Wrong fixed first graph')
            require(record['rows'] == [list(row) for row in cross_rows(first, second)], 'Wrong recorded equations')
            if 'tail_counts' in record:
                check_tail_rival(record)
            elif record['kind'] == 'unresolved':
                residual.append(record)
            else:
                require(record['kind'] == 'formal_lift' and name == 'star', 'Unexpected formal lift')
                require(second == ((1, 4), (2, 4), (3, 4)), 'Wrong star pairing')
                require(record['rows'] == [[0] * 5, [0] * 5] and record['common_difference'] == [-1, 0, 0, 0, 1], 'Wrong star difference')
                lifts.append(record)
    require(not supplied and len(residual) == 15 and len(lifts) == 1, 'Coverage mismatch')
    growth = packed['growth']
    require(len(growth['models']) == len(growth['results']) == 15, 'Incomplete residual closure')
    require(set(packed['certificates']) == {r['certificate'] for r in growth['results']}, 'Unmatched certificate files')
    models = {model['id']: model for model in growth['models']}
    remaining = {(r['graph'], tuple(tuple(e) for e in r['second'])): r for r in residual}
    pair_count = 0
    direct = 0
    bounds = []
    for result in growth['results']:
        model = models.pop(result['model'])
        config = model['configuration']
        key = (config['graph'], tuple(tuple(e) for e in config['second']))
        require(key in remaining, 'Duplicate residual model')
        check_model(model, remaining.pop(key))
        bound, pairs = check_certificate(packed['certificates'][result['certificate']], model)
        pair_count += pairs
        if bound:
            require(result['positive_bound'] == bound, 'Wrong reported growth')
            bounds.append(bound)
        else:
            require(result['direct_rival'] == packed['certificates'][result['certificate']]['rival'], 'Wrong reported direct rival')
            direct += 1
    require(not models and not remaining and direct == 2 and len(bounds) == 13, 'Incomplete closure')
    for change in ('degree', 'unit', 'original'):
        broken = dict(inventory['witnesses'][0])
        if change == 'degree':
            broken['tail_counts'] = [0] * 5
        elif change == 'unit':
            broken['unit_factor'] = 3
        else:
            broken['tail_counts'] = [1] * 5
        try:
            check_tail_rival(broken)
        except ValueError:
            pass
        else:
            raise ValueError('Corruption accepted: ' + change)
    result = {'symbolic_patterns_checked': checked, 'tail_rival_witnesses_checked': len(inventory['witnesses']),
              'identical_fibers': 4, 'formal_star_lifts': len(lifts), 'residual_cases_closed': 15,
              'residual_direct_rivals': direct, 'residual_growth_cases': len(bounds),
              'quartic_positive_bounds': bounds, 'growth_pair_records_checked': pair_count,
              'shared_center_rigidity_verified': True,
              'fixed_valid_controls': check_controls(),
              'boundary': 'Complete computer-assisted shared-center rigidity only; full N>=248 remains open. Same-author separate implementation.'}
    Path('stage44_certificate_check_results.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
