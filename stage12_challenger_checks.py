"""One invalid selected-constraint fixture; not a search or certification."""

from itertools import combinations_with_replacement
import json
from pathlib import Path
from time import monotonic


def run():
    start = monotonic()
    cap = 2.0
    a = ((0, 0), (0, 1), (0, 51), (0, 119),
         (0, 117), (0, 17), (2, 2), (2, -1))

    def total(points):
        points = tuple(points)
        return (sum(x for x, y in points) % 3,
                sum(y for x, y in points) % 1009)

    def difference(p, q):
        return ((p[0] - q[0]) % 3, (p[1] - q[1]) % 1009)

    target = total(a)
    pairs = {total((a[i], a[j])) for i in range(8) for j in range(i, 8)}
    delta = {difference(p, q) for p in a for q in a if p != q}
    core_values = [total((a[i], a[i], a[i + 3])) for i in range(3)]
    assert len(set(core_values)) == 1
    assert total((a[0],) * 3) == total((a[7], a[7], a[6]))
    assert total((a[1],) * 3) == total((a[6], a[6], a[7]))
    assert total((a[2],) * 3) == total((a[5], a[5], a[3]))
    assert total((a[0], a[4], a[6])) == total((a[1], a[3], a[7]))

    rivals = []
    tested = 0
    complete = True
    for indices in combinations_with_replacement(range(8), 8):
        if monotonic() - start > cap:
            complete = False
            break
        tested += 1
        if indices != tuple(range(8)) and total(a[i] for i in indices) == target:
            rivals.append(indices)

    result = {
        'scope': 'One fixed selected-constraint fixture, not a modulus search',
        'runtime_cap_seconds': cap,
        'complete': complete,
        'elapsed_seconds': monotonic() - start,
        'candidate_count': 1,
        'group': 'Z/3 x Z/1009 (cyclic order 3027)',
        'points_in_C_B_F_order': a,
        'pair_sum_count': len(pairs),
        'ordered_difference_count': len(delta),
        'missing_doubled_differences': sum(
            (2*x % 3, 2*y % 1009) not in delta for x, y in delta),
        'order_three_difference_count': sum(x != 0 and y == 0 for x, y in delta),
        'multisets_checked': tested,
        'rivals': rivals,
        'valid_set_count': 0 if rivals else (1 if complete else None),
        'status': 'invalid diagnostic, not a counterexample' if rivals else 'unresolved',
    }
    if complete:
        assert tested == 6435
        assert (0, 0, 2, 4, 4, 5, 6, 6) in rivals
    return result


if __name__ == '__main__':
    result = run()
    Path(__file__).with_name('stage12_challenger_results.json').write_text(
        json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))
