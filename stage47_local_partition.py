"""A fixed quintic-word relaxation, not a cyclic set or exclusion search.

Question: do dyadic pairwise rival exclusions, center privacy and ordinary
cap TWO force 156 repeated quintic outputs? Positive partitions only.
No historical search helper is imported; no moduli or parameters varied.
"""
import itertools
import json
import random
from pathlib import Path


def words():
    return [tuple(t.count(i) for i in range(8))
            for t in itertools.combinations_with_replacement(range(8), 5)
            if len(set(t)) < 5]


def ordinary(w):
    return sorted(w) == [0, 0, 0, 0, 1, 1, 1, 2]


def forbidden(a, b):
    d = [x-y for x, y in zip(a, b)]
    while all(x % 2 == 0 for x in d):
        d = [x//2 for x in d]
    return min(d) >= -1 or max(d) <= 1


def main():
    w = words()
    adj = [set() for _ in w]
    for i in range(len(w)):
        for j in range(i):
            if forbidden(w[i], w[j]):
                adj[i].add(j)
                adj[j].add(i)
    oi = {i for i, a in enumerate(w) if ordinary(a)}
    best = None
    trials = []
    # Fixed finite diagnostic of word assignments, not a cyclic search.
    for seed in range(24):
        rng = random.Random(seed)
        # Ordinary words first so their necessary pairs are packed first.
        order = sorted(oi, key=lambda i: (-len(adj[i]), rng.random()))
        order += sorted(set(range(len(w)))-oi,
                        key=lambda i: (-len(adj[i]), rng.random()))
        fibers, counts = [], []
        for i in order:
            choices = [k for k, f in enumerate(fibers)
                       if not (adj[i] & f) and (i not in oi or counts[k] < 2)]
            if choices:
                # Prefer the occupied class to keep smaller classes available.
                k = max(choices, key=lambda k: (len(fibers[k]), -k))
            else:
                k = len(fibers)
                fibers.append(set())
                counts.append(0)
            fibers[k].add(i)
            counts[k] += int(i in oi)
        trials.append(len(fibers))
        if best is None or len(fibers) < len(best):
            best = fibers
    assert sum(map(len, best)) == 736
    assert all(len(f & oi) <= 2 for f in best)
    assert all(not forbidden(w[i], w[j]) for f in best
               for i, j in itertools.combinations(f, 2))
    # Distinguish pairwise permission from joint realizability. Seek a positive
    # rival implied by two saved equalities at different abstract outputs.
    differences = []
    for k, f in enumerate(best):
        for i, j in itertools.combinations(sorted(f), 2):
            differences.append((k, i, j, tuple(a-b for a, b in zip(w[i], w[j]))))
    closure = None
    for left, right in itertools.combinations(differences, 2):
        if left[0] == right[0]:
            continue
        for sign in (1, -1):
            delta = [a+sign*b for a, b in zip(left[3], right[3])]
            if not any(delta):
                continue
            factor = 1
            while all(x % 2 == 0 for x in delta):
                delta = [x//2 for x in delta]
                factor *= 2
            orientation = 1 if min(delta) >= -1 else (-1 if max(delta) <= 1 else 0)
            if orientation:
                rival = [1+orientation*x for x in delta]
                assert min(rival) >= 0 and sum(rival) == 8 and rival != [1]*8
                closure = {'fiber_indices': [left[0], right[0]],
                           'equalities': [[w[left[1]], w[left[2]]],
                                          [w[right[1]], w[right[2]]]],
                           'second_sign': sign, 'orientation': orientation,
                           'dyadic_factor': factor, 'rival': rival,
                           'identity': 'factor*(rival-allones)=orientation*(D1+second_sign*D2)'}
                break
        if closure:
            break
    out = {'scope': '736 fixed repeated degree-five words on eight labels',
           'constraints': ['dyadic pairwise rival exclusion',
                           'ordinary center privacy',
                           'at most two ordinary words per fiber',
                           'fixed-parity injectivity'],
           'not_enforced': ['simultaneous relation closure',
                            'cross-degree translates',
                            'quartic budget', 'cyclic realization'],
           'trial_fiber_counts': trials, 'fiber_count': len(best),
           'ordinary_word_count': len(oi),
           'cross_fiber_closure_rival': closure,
           'fibers': [[w[i] for i in sorted(f)] for f in best],
           'boundary': 'Positive abstract partition only. It is not a valid set, '
                       'not an odd-order exclusion and not an optimal partition.'}
    Path('stage47_local_partition_results.json').write_text(
        json.dumps(out, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in out.items() if k != 'fibers'}, indent=2))


if __name__ == '__main__':
    main()
