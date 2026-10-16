"""Complete finite cubic-tail reconstruction for P3=18,19,20.

No residues, moduli, or group parameters are searched. Graphs are generated
with sorted complement degrees: every labeled graph is isomorphic to one
in this inventory. All pruning conditions are necessary under no ordinary
quartic fiber with three or more words. Only degree-five vertices impose
neighbor restrictions on tails. Lower-degree tails are unrestricted.
"""
from itertools import combinations, combinations_with_replacement
from pathlib import Path
import argparse
import hashlib
import gzip
import json
import time

VERTICES = tuple(range(8))
PAIRS = tuple(combinations(VERTICES, 2))
PAIRBIT = {p: 1 << i for i, p in enumerate(PAIRS)}


def degree_sequences(edge_count):
    for ds in combinations_with_replacement(range(2, 8), 8):
        if sum(ds) == 2 * edge_count:
            yield ds


def graphs(ds):
    """Every simple graph with this exact degree vector, once."""
    def visit(v, remaining, edges):
        if v == 8:
            if not any(remaining):
                yield tuple(edges)
            return
        k = remaining[v]
        eligible = tuple(w for w in range(v + 1, 8) if remaining[w])
        if k < 0 or k > len(eligible):
            return
        for targets in combinations(eligible, k):
            rem = list(remaining)
            rem[v] = 0
            for w in targets:
                rem[w] -= 1
            # All residual edges are within the remaining vertices.
            if any(rem[w] > 7 - v for w in range(v + 1, 8)):
                continue
            yield from visit(v + 1, tuple(rem), edges + [(v, w) for w in targets])
    yield from visit(0, tuple(ds), [])


def options_for(edges):
    neighbors = [set() for _ in VERTICES]
    for c, d in edges:
        neighbors[c].add(d)
        neighbors[d].add(c)
    options = []
    for c, d in edges:
        eligible = set(VERTICES) - {c, d}
        for v in (c, d):
            if len(neighbors[v]) == 5:
                eligible &= neighbors[v]
        opts = []
        for a in sorted(eligible):
            for b in sorted(eligible - {a}):
                free = set(VERTICES) - {a, b, c, d}
                left = sum(PAIRBIT[tuple(sorted((a, f)))] for f in free)
                right = sum(PAIRBIT[tuple(sorted((b, f)))] for f in free)
                opts.append((a, b, left, right))
        options.append(opts)
    return options


def assignments(edges):
    options = options_for(edges)
    used = [0] * 8
    chosen = {}
    def visit():
        if len(chosen) == len(edges):
            yield tuple((edges[i], chosen[i][:2]) for i in range(len(edges)))
            return
        best_i, best_opts = None, None
        for i, (c, d) in enumerate(edges):
            if i in chosen:
                continue
            available = [o for o in options[i] if not (used[c] & o[2] or used[d] & o[3])]
            if not available:
                return
            if best_opts is None or len(available) < len(best_opts):
                best_i, best_opts = i, available
        c, d = edges[best_i]
        for o in best_opts:
            chosen[best_i] = o
            used[c] |= o[2]
            used[d] |= o[3]
            yield from visit()
            used[c] ^= o[2]
            used[d] ^= o[3]
            del chosen[best_i]
    yield from visit()


def rows_for(assignment):
    rows = []
    for (c, d), (a, b) in assignment:
        row = [0] * 8
        row[c] += 2
        row[d] -= 2
        row[a] += 1
        row[b] -= 1
        assert sum(row) == 0
        rows.append(row[:7])
    return rows


def lattice_index(rows, certificates=False):
    """Exact integer row operations, returning index in Z^7, or 0 if rank<7."""
    mat = [list(r) for r in rows]
    coefficients = [[int(i == j) for j in range(len(rows))] for i in range(len(rows))] if certificates else None
    pivot = 0
    diag = []
    for col in range(7):
        nonzero = next((i for i in range(pivot, len(mat)) if mat[i][col]), None)
        if nonzero is None:
            continue
        mat[pivot], mat[nonzero] = mat[nonzero], mat[pivot]
        if certificates:
            coefficients[pivot], coefficients[nonzero] = coefficients[nonzero], coefficients[pivot]
        for i in range(pivot + 1, len(mat)):
            while mat[i][col]:
                quotient = mat[pivot][col] // mat[i][col]
                mat[pivot] = [x - quotient * y for x, y in zip(mat[pivot], mat[i])]
                if certificates:
                    coefficients[pivot] = [x - quotient * y for x, y in zip(coefficients[pivot], coefficients[i])]
                mat[pivot], mat[i] = mat[i], mat[pivot]
                if certificates:
                    coefficients[pivot], coefficients[i] = coefficients[i], coefficients[pivot]
        diag.append(abs(mat[pivot][col]))
        pivot += 1
    if pivot < 7:
        return (0, None) if certificates else 0
    index = 1
    for value in diag:
        index *= value
    if not certificates:
        return index
    if index != 1:
        return index, None
    # Convert the unimodular upper-triangular basis to the identity.
    for i in range(6, -1, -1):
        if mat[i][i] == -1:
            mat[i] = [-x for x in mat[i]]
            coefficients[i] = [-x for x in coefficients[i]]
        assert mat[i][i] == 1
        for j in range(i):
            factor = mat[j][i]
            mat[j] = [x - factor * y for x, y in zip(mat[j], mat[i])]
            coefficients[j] = [x - factor * y for x, y in zip(coefficients[j], coefficients[i])]
    assert mat[:7] == [[int(i == j) for j in range(7)] for i in range(7)]
    return index, coefficients[:7]


def save(result):
    survivors = result.pop('survivors')
    for survivor in survivors:
        index, cert = lattice_index(rows_for(survivor['assignment']), certificates=True)
        assert index == survivor['lattice_index']
        survivor['integer_combinations'] = cert
    bundle = Path(__file__).with_name('stage52_integer_certificates.json.gz')
    bundle.write_bytes(gzip.compress(json.dumps({'survivors': survivors}, separators=(',', ':')).encode(), mtime=0))
    result['certificate_bundle'] = bundle.name
    result['certificate_count'] = len(survivors)
    result['certificate_sha256'] = hashlib.sha256(bundle.read_bytes()).hexdigest()
    Path(__file__).with_name('stage52_center_graph_results.json').write_text(json.dumps(result, indent=2) + '\n')


def run(seconds):
    started = time.monotonic()
    records, survivors = [], []
    for p3 in (20, 19, 18):
        record = {'P3': p3, 'degree_sequences': [], 'graphs': 0, 'assignments': 0,
                  'index_histogram': {}, 'status': 'COMPLETE'}
        digest = hashlib.sha256()
        for ds in degree_sequences(28 - p3):
            count = 0
            for omitted in graphs(ds):
                if time.monotonic() - started > seconds:
                    raise TimeoutError('Incomplete inventory; no theorem inferred')
                count += 1
                edges = tuple(e for e in PAIRS if e not in omitted)
                digest.update(json.dumps(omitted, separators=(',', ':')).encode())
                for assignment in assignments(edges):
                    index = lattice_index(rows_for(assignment))
                    record['assignments'] += 1
                    key = str(index)
                    record['index_histogram'][key] = record['index_histogram'].get(key, 0) + 1
                    survivors.append({'P3': p3, 'omitted': omitted,
                                      'assignment': assignment, 'lattice_index': index})
            record['degree_sequences'].append({'degrees': ds, 'graphs': count})
            record['graphs'] += count
        record['graph_digest'] = digest.hexdigest()
        records.append(record)
        print(json.dumps(record), flush=True)
    result = {'scope': 'All sorted-degree complement graphs for P3=18,19,20 and every necessary tail assignment.',
              'records': records, 'runtime_seconds': time.monotonic() - started,
              'no_modulus_search': True,
              'all_survivors_have_index_one': all(s['lattice_index'] == 1 for s in survivors),
              'survivors': survivors}
    save(result)
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--seconds', type=float, default=120)
    args = parser.parse_args()
    run(args.seconds)
