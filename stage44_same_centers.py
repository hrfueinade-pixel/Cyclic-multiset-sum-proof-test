"""Fixed shared-center experiment: two ordinary quintic triples on eight labels.

No numerical group, parameter, or modulus enumeration. Relations are checked
over Z with only a power of two canceled, so retained exclusions are uniform
in odd groups. Surviving symbolic patterns are not asserted realizable.
"""
import itertools
import json
from fractions import Fraction
from pathlib import Path


GRAPHS = {
    'triangle': ((0, 1), (0, 2), (1, 2)),
    'star': ((0, 1), (0, 2), (0, 3)),
    'path': ((0, 1), (1, 2), (2, 3)),
    'split': ((0, 1), (1, 2), (3, 4)),
}
EDGES = tuple(itertools.combinations(range(5), 2))


def word(edge):
    return tuple(int(i in edge) for i in range(5))


def minus(a, b):
    return tuple(x - y for x, y in zip(a, b))


def combinations_of_rows(rows, target):
    """Return a rational row combination, or None; zero rows are allowed."""
    a, b = rows
    for i, j in itertools.combinations(range(5), 2):
        det = a[i] * b[j] - a[j] * b[i]
        if det:
            u = Fraction(target[i] * b[j] - target[j] * b[i], det)
            v = Fraction(a[i] * target[j] - a[j] * target[i], det)
            return (u, v) if all(u * a[k] + v * b[k] == target[k] for k in range(5)) else None
    pivot = next((k for k in range(5) if a[k]), None)
    if pivot is not None:
        u = Fraction(target[pivot], a[pivot])
        return (u, Fraction(0)) if all(u * a[k] == target[k] for k in range(5)) else None
    pivot = next((k for k in range(5) if b[k]), None)
    if pivot is not None:
        v = Fraction(target[pivot], b[pivot])
        return (Fraction(0), v) if all(v * b[k] == target[k] for k in range(5)) else None
    return (Fraction(0), Fraction(0)) if not any(target) else None


def power_two(n):
    return n > 0 and n & (n - 1) == 0


def compositions(total, length):
    if length == 1:
        yield (total,)
    else:
        for first in range(total + 1):
            for rest in compositions(total - first, length - 1):
                yield (first,) + rest


def rival(rows):
    for count in compositions(5, 5):
        if count == (1,) * 5:
            continue
        f = tuple(x - 1 for x in count)
        coefficients = combinations_of_rows(rows, f)
        if coefficients is None or not all(power_two(x.denominator) for x in coefficients):
            continue
        scale = max(x.denominator for x in coefficients)
        return {'tail_counts': count, 'unit_factor': scale,
                'row_multipliers': [int(x * scale) for x in coefficients]}
    return None


def main():
    result = {'models': {}, 'survivors': [], 'witnesses': []}
    for name, first in GRAPHS.items():
        counts = {'patterns': 0, 'identical_fiber': 0, 'formal_lift': 0,
                  'explicit_rival': 0, 'unresolved': 0}
        for second in itertools.permutations(EDGES, 3):
            counts['patterns'] += 1
            differences = [minus(word(q), word(p)) for p, q in zip(first, second)]
            rows = [minus(differences[i], differences[0]) for i in (1, 2)]
            record = {'graph': name, 'first': first, 'second': second, 'rows': rows}
            if second == first:
                counts['identical_fiber'] += 1
            elif all(d == differences[0] for d in differences):
                counts['formal_lift'] += 1
                result['survivors'].append({**record, 'kind': 'formal_lift', 'common_difference': differences[0]})
            else:
                witness = rival(rows)
                if witness:
                    counts['explicit_rival'] += 1
                    result['witnesses'].append({**record, **witness})
                else:
                    counts['unresolved'] += 1
                    result['survivors'].append({**record, 'kind': 'unresolved'})
        result['models'][name] = counts
    result['boundary'] = 'Fixed shared-center symbolic inventory. Only explicit power-of-two rival identities exclude patterns; unresolved cases are not group realizations.'
    Path('stage44_same_centers_results.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result['models'], indent=2))
    print('Survivors:', len(result['survivors']))


if __name__ == '__main__':
    main()
