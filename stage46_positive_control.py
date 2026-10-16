"""One positive control, not a residue search.

Elementary proof: before translating, label coefficients are
(2a,2b,2c,u,-3u,-b-c,-a-c,-a-b), with a=1,b=17,c=289,u=4913.
All eight-term low coefficients lie in [-8,16]. Successive reduction
modulo 17 forces them to zero. The outside equation U-3V=-2 gives
(U,V)=(1,1) or (4,2). Triangle equations force their three center
counts to have the same parity, and triangle mass equals twice their
sum. Mass two is impossible; mass six forces all six triangle counts
one. This proves validity, with no modular wrap after translation.
"""
import itertools
import json
from pathlib import Path


def main():
    raw = (2, 34, 578, 4913, -14739, -306, -290, -18)
    shift = -min(raw)
    a = tuple(x + shift for x in raw)
    modulus = 8 * max(a) + 1
    target = sum(a) % modulus
    hits = [word for word in itertools.combinations_with_replacement(range(8), 8)
            if sum(a[i] for i in word) % modulus == target]
    assert hits == [tuple(range(8))]
    quartic = 4 * shift % modulus
    fiber = [word for word in itertools.combinations_with_replacement(range(8), 4)
             if sum(a[i] for i in word) % modulus == quartic]
    cubic = {sum(a[i] for i in word) % modulus
             for word in itertools.combinations_with_replacement(range(8), 3)}
    predecessors = [i for i in range(8) if (quartic - a[i]) % modulus in cubic]
    result = {'set': a, 'raw_set': raw, 'modulus': modulus,
              'target': target, 'checked_degree_eight_words': 6435,
              'target_representations': hits, 'quartic_value': quartic,
              'quartic_fiber': fiber, 'predecessor_labels': predecessors,
              'scope': 'Positive full-valid large-order counterexample to an unrestricted predecessor cap seven.'}
    Path('stage46_positive_control_results.json').write_text(
        json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
