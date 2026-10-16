"""Positive closure tests for the 15 shared-center residual configurations.

First a power-of-two pivot, then an explicitly recorded unimodular row
reduction retains all odd torsion. Each discovery has the unchanged two-second
cap. No group parameters or cyclic moduli are sampled.
"""
import json
import math
from pathlib import Path

from stage43_joint_relations import bezout
from stage43_relation_growth import run


def parameterize(record, index):
    equations = [row[1:] for row in record['rows']]
    first = next(row for row in equations if any(row))
    pivot = min((i for i, x in enumerate(first) if x and abs(x) & (abs(x) - 1) == 0), key=lambda i: abs(first[i]))
    scale = abs(first[pivot])
    remaining = [i for i in range(4) if i != pivot]
    base = [[0] * 3 for _ in range(4)]
    for j, i in enumerate(remaining):
        base[i][j] = scale
        base[pivot][j] = -first[i] * (1 if first[pivot] > 0 else -1)
    second = next((row for row in equations if any(sum(row[i] * base[i][j] for i in range(4)) for j in range(3))), None)
    transform = [[int(i == j) for j in range(3)] for i in range(3)]
    original = [0] * 3
    order = 1
    gcd = 0
    if second is not None:
        vector = [sum(second[i] * base[i][j] for i in range(4)) for j in range(3)]
        original = vector[:]
        for j in (1, 2):
            a, b = vector[0], vector[j]
            if a == b == 0:
                continue
            g, s, t = bezout(a, b)
            left = [row[0] for row in transform]
            right = [row[j] for row in transform]
            for i in range(3):
                transform[i][0] = s * left[i] + t * right[i]
                transform[i][j] = -(b // g) * left[i] + (a // g) * right[i]
            vector[0], vector[j] = g, 0
        gcd = vector[0]
        assert gcd == math.gcd(*original) and vector[1:] == [0, 0]
        order = gcd
        while order % 2 == 0:
            order //= 2
    merged = [[sum(base[i][k] * transform[k][j] for k in range(3)) for j in range(3)] for i in range(4)]
    parameter_rows = [tuple(row[1:]) if second is not None else tuple(row) for row in merged]
    parameter_torsion = [row[0] % order if second is not None else 0 for row in merged]
    width = len(parameter_rows[0])
    tails = [(0,) * (width + 1)] + [tuple(2 * x for x in row) + (0,) for row in parameter_rows]
    tail_torsion = [0] + [2 * x % order for x in parameter_torsion]
    halves = [(0,) * width] + parameter_rows
    half_torsion = [0] + parameter_torsion
    centers = [tuple(halves[i][k] + halves[j][k] for k in range(width)) + (1,) for i, j in record['first']]
    center_torsion = [(half_torsion[i] + half_torsion[j]) % order for i, j in record['first']]
    return {'id': f's44_{index:02}', 'rows': tails + centers,
            'torsion_rows': tail_torsion + center_torsion, 'torsion_order': order,
            'direction': first, 'configuration': record,
            'first_equation': first, 'first_pivot': pivot, 'first_scale': scale,
            'first_rows': base, 'second_equation': second, 'second_after_first': original,
            'unimodular_transform': transform, 'diagonal_gcd': gcd,
            'parameterization': 'Power-of-two pivot; a second independent row is reduced unimodularly, retaining its odd torsion.'}


def main():
    residual = [r for r in json.loads(Path('stage44_same_centers_results.json').read_text())['survivors'] if r['kind'] == 'unresolved']
    models = [parameterize(record, i) for i, record in enumerate(residual)]
    results = []
    for model in models:
        result = run(model, 4, 89, [2])
        results.append(result)
        print(json.dumps(result), flush=True)
    Path('stage44_shared_growth_results.json').write_text(json.dumps({
        'models': models, 'results': results,
        'boundary': 'Positive symbolic closure only; no failed clique or timeout certifies absence.'}, indent=2) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
