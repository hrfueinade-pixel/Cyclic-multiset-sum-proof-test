"""Complete necessary-condition relaxation, not cyclic-set enumeration."""
import argparse
from collections import Counter
from functools import lru_cache
from itertools import product
import json
from pathlib import Path
from time import monotonic


def pack(items):
    @lru_cache(None)
    def visit(rest, bins):
        if not rest:
            return () if bins == (0,) * 8 else None
        x, tail = rest[0], rest[1:]
        for capacity in sorted(set(bins), reverse=True):
            if capacity < x:
                continue
            i = bins.index(capacity)
            new = list(bins)
            new[i] -= x
            result = visit(tail, tuple(sorted(new)))
            if result is not None:
                return (capacity,) + result
        return None
    return visit(tuple(sorted(items, reverse=True)), (7,) * 8)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--seconds', type=float, default=30)
    args = ap.parse_args()
    start = monotonic()
    survivors, exclusions = [], []
    complete = True
    # a_m counts shifts t with |2A intersect (A+t)|=m, m=2,...,6.
    # Pair budget is 28. m copies of the indegree m-1 must fill 8 rows of 7.
    for high in product(range(10), range(5), range(3), range(2)):
        a3, a4, a5, a6 = high
        a2 = 28 - 3*a3 - 6*a4 - 10*a5 - 15*a6
        if a2 < 0:
            continue
        if monotonic() - start > args.seconds:
            complete = False
            break
        spectrum = (a2, a3, a4, a5, a6)
        items = tuple(w for m, a in enumerate(spectrum, 2) for w in [m-1]*(m*a))
        assert sum(items) == 56
        witness = pack(items)
        entry = {'spectrum_a2_to_a6': spectrum,
                 'triangles_without_22': sum(a*m*(m-1)*(m-2)//6 for m,a in enumerate(spectrum,2)),
                 'items': dict(Counter(items))}
        if witness is None:
            exclusions.append(entry)
        else:
            bins = [7]*8
            rows = [[] for _ in bins]
            for x, capacity in zip(sorted(items, reverse=True), witness):
                i = bins.index(capacity)
                bins[i] -= x
                rows[i].append(x)
            assert bins == [0]*8
            survivors.append(dict(entry, row_witness=rows))
    result = {'completion': 'COMPLETE' if complete else 'TIMEOUT',
              'seconds_limit':args.seconds, 'elapsed_seconds':monotonic()-start,
              'scope':'8 row capacities and overlap spectrum only; row/column labels and group realizability relaxed',
              'survivors':survivors, 'exclusions':exclusions,
              'maximum_triangles_without_22':max((r['triangles_without_22'] for r in survivors),default=None) if complete else None}
    Path('stage18_tree_spectra_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('survivors','exclusions')},indent=2))
    print('spectra:',len(survivors),'survivors;',len(exclusions),'excluded')


if __name__ == '__main__':
    main()
