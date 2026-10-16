"""One fixed complementary-quintic matching slice; never a modulus sweep.

Test ONLY the proposed direct rival 1+sum(sign_i R_i), signs +/-1.
Failure means this restricted formula fails, not full validity or closure.
"""
import json
from itertools import combinations, product
from pathlib import Path


def relations(c, d):
    b = [i for i in range(8) if i not in (c, d)]
    for u in combinations(b, 3):
        row = [0] * 8
        row[c], row[d] = 2, -2
        for i in b:
            row[i] = 1 if i in u else -1
        yield tuple(row)


if __name__ == '__main__':
    first = (2, -2, 1, 1, 1, -1, -1, -1)
    choices = [list(relations(c, d)) for c, d in [(2, 3), (4, 5), (6, 7)]]
    signs = list(product((-1, 1), repeat=4))
    closed = 0
    failed = []
    first_witness = None
    for rest in product(*choices):
        rows = (first,) + rest
        found = None
        for sg in signs:
            rival = tuple(1 + sum(s * r[j] for s, r in zip(sg, rows)) for j in range(8))
            if min(rival) >= 0 and rival != (1,) * 8:
                assert sum(rival) == 8
                found = {'signs': sg, 'rival': rival}
                break
        if found:
            closed += 1
            if first_witness is None:
                first_witness = {'rows': rows, **found}
        else:
            if len(failed) < 3:
                failed.append(rows)
    total = 20**3
    result = {'scope': 'One fixed first edge relation and three disjoint-center pairs; '
                        'only signed sums of four relations tested.',
              'assignments': total, 'direct_signed_sum_rival': closed,
              'formula_failures': total - closed, 'failure_examples': failed,
              'first_positive_witness': first_witness,
              'boundary': 'A failed formula test is not a valid set or an unclosed group model.'}
    Path('stage47_no_triangle_matching_results.json').write_text(
        json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: result[k] for k in ('assignments', 'direct_signed_sum_rival', 'formula_failures')}))
