"""Two fixed simultaneous-collision models; no residue or modulus sweep.

Ten seconds of clique discovery per requested model/degree. Positive pair
witnesses prove growth; incomplete discovery and small cliques prove no
absence. The inherited clique routine is used only as a search helper.
"""
import argparse
import gzip
import itertools
import json
import math
import time

from stage41_saturated_fiber_closure import find_clique


MODELS = {
    'doubling4': (((1,0,0,0), (0,1,0,0), (0,0,1,0), (0,0,0,1),
                  (2,0,0,0), (0,2,0,0), (0,0,2,0), (0,0,0,2)),
                 (0,)*8),
    'exception3': (((0,0,0,0), (0,0,0,0), (1,0,0,0), (-2,0,0,0),
                   (0,1,0,0), (0,-2,0,0), (0,0,1,0), (0,0,0,1)),
                  (0,1,0,0,0,0,0,0)),
}

for name, centers in {
    'pairchain': ((1,0,0,0), (4,0,0,0), (0,1,0,0), (0,0,1,0)),
    'twochains': ((1,0,0,0), (4,0,0,0), (0,1,0,0), (0,4,0,0)),
    'chain3': ((1,0,0,0), (4,0,0,0), (16,0,0,0), (64,0,0,0)),
}.items():
    MODELS[name] = (centers+tuple(tuple(2*x for x in c) for c in centers), (0,)*8)


def words(degree):
    for indices in itertools.combinations_with_replacement(range(8), degree):
        yield tuple(indices.count(i) for i in range(8))


def coordinates(word, model):
    rows, torsion = MODELS[model]
    return (tuple(sum(word[i]*rows[i][j] for i in range(8)) for j in range(4)),
            sum(word[i]*torsion[i] for i in range(8)) % 3)


def subtract(left, right):
    return tuple(x-y for x,y in zip(left[0], right[0])), (left[1]-right[1]) % 3


def ray(vector):
    divisor = math.gcd(*vector)
    first = next(x for x in vector if x)
    signed = divisor if first > 0 else -divisor
    return tuple(x//signed for x in vector), signed


def cancel_two(difference):
    free, torsion = difference
    power = 1
    while any(free) and all(x % 2 == 0 for x in free):
        free = tuple(x//2 for x in free)
        torsion = (2*torsion) % 3
        power *= 2
    return (free, torsion), power


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', choices=tuple(MODELS), required=True)
    parser.add_argument('--degree', type=int, choices=(3,4,5), default=4)
    parser.add_argument('--target', type=int, default=89)
    args = parser.parse_args()
    start = time.monotonic()
    base = coordinates((1,)*8, args.model)
    rays, torsion_only = {}, []
    for c in words(8):
        if c == (1,)*8:
            continue
        f = subtract(coordinates(c, args.model), base)
        assert f != ((0,)*4, 0), 'Unconditional rival in model'
        if any(f[0]):
            direction, scale = ray(f[0])
            rays.setdefault(direction, []).append((scale, f[1], c))
        else:
            torsion_only.append((f[1], c))

    cache = {}
    def witness(d):
        if d in cache:
            return cache[d]
        reduced, power = cancel_two(d)
        free, torsion = reduced
        result = None
        if any(free):
            direction, scale = ray(free)
            for rival_scale, rival_torsion, c in rays.get(direction, ()):
                if rival_scale % scale == 0:
                    multiplier = rival_scale//scale
                    if (multiplier*torsion-rival_torsion) % 3 == 0:
                        result = (c, multiplier, power)
                        break
        elif torsion:
            for rival_torsion, c in torsion_only:
                multiplier = rival_torsion*pow(torsion, -1, 3) % 3
                if multiplier:
                    result = (c, multiplier, power)
                    break
        cache[d] = result
        return result

    representatives = {}
    for c in words(args.degree):
        if max(c) > 1:
            representatives.setdefault(coordinates(c, args.model), c)
    vectors = list(representatives)
    adjacency = [0]*len(vectors)
    for i, left in enumerate(vectors):
        for j in range(i):
            if witness(subtract(left, vectors[j])):
                adjacency[i] |= 1 << j
                adjacency[j] |= 1 << i
    clique, complete, nodes = find_clique(adjacency, args.target, seconds=10)
    selected = [representatives[vectors[i]] for i in clique]
    pairs = []
    for i,j in itertools.combinations(range(len(selected)), 2):
        c, multiplier, power = witness(subtract(vectors[clique[i]], vectors[clique[j]]))
        pairs.append({'rival': ''.join(map(str,c)), 'multiplier': multiplier,
                      'canceled_power_two': power})
    data = {'model': args.model, 'degree': args.degree, 'units': [2],
            'torsion_order': 3 if args.model == 'exception3' else 1,
            'words': [''.join(map(str,c)) for c in selected], 'pairs': pairs}
    stem = f'stage42_{args.model}_degree{args.degree}'
    with open(stem+'_certificate.json.gz', 'wb') as stream:
        stream.write(gzip.compress(json.dumps(data, separators=(',',':')).encode(), mtime=0))
    summary = {'model': args.model, 'degree': args.degree,
               'symbolic_repeated_values': len(vectors), 'target': args.target,
               'positive_clique_size': len(selected), 'pair_witnesses': len(pairs),
               'discovery_complete': complete, 'search_nodes': nodes,
               'discovery_cap_seconds': 10, 'elapsed_seconds': time.monotonic()-start,
               'certificate': stem+'_certificate.json.gz',
               'boundary': 'Only the positive certificate proves growth for this model. No arbitrary cyclic sets, moduli, or parameter values were searched.'}
    with open(stem+'_results.json', 'w', encoding='utf-8') as stream:
        json.dump(summary, stream, indent=2)
        stream.write('\n')
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
