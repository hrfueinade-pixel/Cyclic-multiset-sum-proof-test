"""Standalone positive abstract-partition audit and simultaneous rejection.

Imports no producers. Does not try to realize the partition in any group.
"""
from itertools import combinations
import json
from pathlib import Path


def all_words():
    for bars in combinations(range(12), 7):
        b = (-1,) + bars + (12,)
        p = tuple(b[i + 1] - b[i] - 1 for i in range(8))
        if max(p) >= 2:
            yield p


def ordinary(p):
    return p.count(2) == 1 and p.count(1) == 3 and p.count(0) == 4


def main():
    here = Path(__file__).parent
    data = json.loads((here / 'stage47_local_partition_results.json').read_text())
    fibers = [[tuple(p) for p in f] for f in data['fibers']]
    flat = [p for f in fibers for p in f]
    assert len(flat) == len(set(flat)) == 736
    assert set(flat) == set(all_words())
    relations = []
    centers_checked = parity_pairs = forbidden_pairs_checked = 0
    for fi, fiber in enumerate(fibers):
        os = [p for p in fiber if ordinary(p)]
        assert len(os) <= 2
        for p in os:
            center = p.index(2)
            for q in fiber:
                if p != q:
                    assert q[center] == 0
                    centers_checked += 1
        assert len({tuple(x % 2 for x in p) for p in fiber}) == len(fiber)
        for p, q in combinations(fiber, 2):
            d = tuple(a - b for a, b in zip(p, q))
            prim = d
            while all(x % 2 == 0 for x in prim):
                prim = tuple(x // 2 for x in prim)
            # Both potential rival orientations must have a negative count.
            assert min(prim) <= -2 and max(prim) >= 2
            forbidden_pairs_checked += 1
            parity_pairs += 1
            relations.append((d, fi, p, q))
    witness = None
    # A positive witness terminates this finite diagnostic immediately.
    # Raw rows only: the resulting identity cancels no prime at all.
    for i, (d, fi, p, q) in enumerate(relations):
        if witness:
            break
        for e, fj, a, b in relations[i + 1:]:
            if fi == fj:
                continue
            for sign in (1, -1):
                r = tuple(1 + x + sign * y for x, y in zip(d, e))
                if min(r) >= 0 and r != (1,) * 8:
                    assert sum(r) == 8
                    witness = {'fiber_indices': [fi, fj],
                               'first_equality': [p, q], 'second_equality': [a, b],
                               'second_relation_sign': sign, 'rival': r,
                               'identity': 'rival-allones=(first_left-first_right)+sign*(second_left-second_right)',
                               'units_canceled': []}
                    break
            if witness:
                break
    assert witness is not None
    result = {'fixed_partition_constraints_passed': True,
              'fiber_count': len(fibers), 'ordinary_centers_checked': centers_checked,
              'pair_checks': forbidden_pairs_checked,
              'simultaneous_equality_witness': witness,
              'conclusion': 'Partition obeys the stated local relaxation but is impossible under full validity in any group.',
              'boundary': 'No search of cyclic sets, no quartic budget certificate, no exclusion of an arbitrary modulus.'}
    (here / 'stage47_independent_partition_check_results.json').write_text(
        json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
