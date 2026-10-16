"""Standalone coverage and positive-certificate audit; no producer imports.

Uses reverse vertex order for graph generation, sets for quartic tails,
and direct integer multiplication to verify certificates. It performs no
integer elimination and no search over group parameters or moduli.
"""
from collections import Counter, defaultdict
from itertools import combinations, combinations_with_replacement
from pathlib import Path
import gzip
import hashlib
import json
import time

HERE = Path(__file__).parent
VERTICES = frozenset(range(8))
ALL_EDGES = tuple(combinations(range(8), 2))


def generate(degrees):
    def descend(v, residual, edges):
        if v < 0:
            if all(x == 0 for x in residual):
                yield tuple(sorted(edges))
            return
        candidates = [i for i in range(v) if residual[i] > 0]
        if residual[v] < 0 or residual[v] > len(candidates):
            return
        for group in combinations(candidates, residual[v]):
            following = list(residual)
            following[v] = 0
            for w in group:
                following[w] -= 1
            if any(x > v - 1 for x in following[:v]):
                continue
            yield from descend(v - 1, following, edges + [(w, v) for w in group])
    yield from descend(7, list(degrees), [])


def solve(edges):
    adjacency = defaultdict(set)
    for c, d in edges:
        adjacency[c].add(d)
        adjacency[d].add(c)
    possibilities = {}
    for c, d in edges:
        opts = []
        # Independently form all 30 private, distinct-tail cubic options.
        for a in VERTICES - {c, d}:
            for b in VERTICES - {c, d, a}:
                if any(len(adjacency[v]) == 5 and not {a, b} <= adjacency[v] for v in (c, d)):
                    continue
                free = VERTICES - {c, d, a, b}
                opts.append((a, b, frozenset(frozenset((a, f)) for f in free),
                             frozenset(frozenset((b, f)) for f in free)))
        possibilities[c, d] = opts
    def visit(remaining, used, chosen):
        if not remaining:
            yield tuple((edge, chosen[edge]) for edge in sorted(chosen))
            return
        viable = {}
        for edge in remaining:
            c, d = edge
            viable[edge] = [o for o in possibilities[edge] if not(o[2] & used[c] or o[3] & used[d])]
            if not viable[edge]:
                return
        edge = min(remaining, key=lambda e: (len(viable[e]), -e[0], -e[1]))
        c, d = edge
        for a, b, left, right in viable[edge]:
            next_used = list(used)
            next_used[c] = used[c] | left
            next_used[d] = used[d] | right
            yield from visit(remaining - {edge}, next_used, {**chosen, edge: (a, b)})
    yield from visit(frozenset(edges), [frozenset()] * 8, {})


def key(assignment):
    return tuple(tuple(c + a) for c, a in assignment)


def certificate_valid(survivor):
    rows = []
    for centers, tails in survivor['assignment']:
        c, d = centers
        a, b = tails
        rows.append([2 * int(i == c) - 2 * int(i == d) + int(i == a) - int(i == b) for i in range(8)])
    coefficients = survivor['integer_combinations']
    if coefficients is None or len(coefficients) != 7:
        return False
    for i, combination in enumerate(coefficients):
        if len(combination) != len(rows) or any(type(n) is not int for n in combination):
            return False
        actual = [sum(n * row[j] for n, row in zip(combination, rows)) for j in range(8)]
        if actual != [int(j == i) - int(j == 7) for j in range(8)]:
            return False
    return True


def fixed_control():
    A = (0, 136, 518, 556, 640, 700, 912, 944)
    modulus = 7553
    target = sum(A) % modulus
    original = tuple(range(8))
    mass_eight = list(combinations_with_replacement(range(8), 8))
    rivals = [w for w in mass_eight if sum(A[i] for i in w) % modulus == target and w != original]
    fibers = {}
    totals = {}
    for degree in (3, 4, 5):
        all_values, repeated_values = set(), set()
        ordinary = defaultdict(list)
        for word in combinations_with_replacement(range(8), degree):
            value = sum(A[i] for i in word) % modulus
            all_values.add(value)
            counts = Counter(word)
            if len(counts) != degree:
                repeated_values.add(value)
            if sorted(counts.values()) == [1] * (degree - 2) + [2]:
                center = next(i for i in counts if counts[i] == 2)
                ordinary[value].append((center, frozenset(i for i in counts if i != center)))
        totals[degree] = {'all_values': len(all_values), 'repeated_values': len(repeated_values)}
        fibers[degree] = ordinary
    disjoint = []
    cubic_edges = []
    for value, words in fibers[3].items():
        for first, second in combinations(words, 2):
            cubic_edges.append(tuple(sorted((first[0], second[0]))))
    for value, words in fibers[4].items():
        for first, second in combinations(words, 2):
            if first[1].isdisjoint(second[1]):
                disjoint.append((value, first, second))
    splits = []
    for value, words in fibers[5].items():
        if len(words) != 3:
            continue
        noncenters = VERTICES - {w[0] for w in words}
        omitted = [noncenters - tail for _, tail in words]
        degrees = sorted(Counter(i for edge in omitted for i in edge).values())
        if degrees == [1, 1, 1, 1, 2]:
            source_edges = [tuple(sorted((x[0], y[0]))) for x, y in combinations(words, 2)
                            if len(x[1] & y[1]) == 1]
            splits.append({'value': value, 'centers': sorted(w[0] for w in words),
                           'source_center_edges': sorted(source_edges)})
    assert len(mass_eight) == 6435 and not rivals
    assert len(disjoint) == 4 and len(splits) == 2
    assert max(map(len, fibers[4].values())) == 2
    assert totals[4] == {'all_values': 297, 'repeated_values': 227}
    shared = set(map(tuple, splits[0]['source_center_edges'])) & set(map(tuple, splits[1]['source_center_edges']))
    delta = {(x - y) % modulus for x in A for y in A if x != y}
    assert shared and all(2 * (A[c] - A[d]) % modulus not in delta for c, d in shared)
    return {'A': A, 'modulus': modulus, 'mass_eight_words_checked': len(mass_eight),
            'valid': not rivals, 'q': len(splits), 'E': len(disjoint),
            'ordinary_quartic_triples': 0, 'T4_repeated': 227, 'size_4A': 297,
            'split_outputs': splits, 'shared_open_source_edges': sorted(shared),
            'cubic_edges': cubic_edges}


def main():
    started = time.monotonic()
    reference = json.loads((HERE / 'stage52_center_graph_results.json').read_text())
    raw = (HERE / reference['certificate_bundle']).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == reference['certificate_sha256']
    survivors = json.loads(gzip.decompress(raw))['survivors']
    assert len(survivors) == 1536 and all(certificate_valid(s) for s in survivors)
    # Positive controls reject a broken coefficient and a torsion-only identity.
    broken = json.loads(json.dumps(survivors[0]))
    broken['integer_combinations'][0][0] += 1
    assert not certificate_valid(broken)
    doubled = json.loads(json.dumps(survivors[0]))
    doubled['integer_combinations'] = [[2 * x for x in row] for row in doubled['integer_combinations']]
    assert not certificate_valid(doubled)
    expected_keys = {key(s['assignment']) for s in survivors}
    assert len(expected_keys) == len(survivors)
    observed_keys = set()
    records = []
    for prior in reference['records']:
        p3 = prior['P3']
        record = {'P3': p3, 'degree_sequences': [], 'graphs': 0, 'assignments': 0}
        # Generate the degree partitions independently of the saved list.
        for ds in combinations_with_replacement(range(2, 8), 8):
            if sum(ds) != 2 * (28 - p3):
                continue
            count = 0
            for omitted in generate(ds):
                if time.monotonic() - started > 120:
                    raise TimeoutError('Incomplete independent coverage')
                count += 1
                edges = tuple(e for e in ALL_EDGES if e not in omitted)
                for assignment in solve(edges):
                    k = key(assignment)
                    assert k not in observed_keys
                    observed_keys.add(k)
                    record['assignments'] += 1
            record['degree_sequences'].append({'degrees': list(ds), 'graphs': count})
            record['graphs'] += count
        assert record['degree_sequences'] == prior['degree_sequences']
        assert record['graphs'] == prior['graphs'] and record['assignments'] == prior['assignments']
        records.append(record)
        print(json.dumps(record), flush=True)
    assert observed_keys == expected_keys
    control = fixed_control()
    result = {'status': 'PASS', 'records': records, 'positive_certificates_checked': len(survivors),
              'corruptions_rejected': 2, 'fixed_control': control,
              'runtime_seconds': time.monotonic() - started,
              'boundary': 'Separate implementation by the same assistant, not independent human or formal verification.'}
    (HERE / 'stage52_independent_results.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'status': 'PASS', 'certificates': len(survivors), 'fixed_control': control}), flush=True)


if __name__ == '__main__':
    main()
