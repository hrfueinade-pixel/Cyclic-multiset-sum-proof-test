"""Five fixed positive controls and an overlap witness, not a set search.

Weak compositions reconstruct all fibers independently of the symbolic
producer. Eight-term uniqueness is checked directly, not inferred from
cubic or quartic protection. No historical exclusion is rerun.
"""
import itertools
import json
import math
from collections import defaultdict
from pathlib import Path


def compositions(total, width=8):
    if width == 1:
        yield (total,)
        return
    for first in range(total+1):
        for tail in compositions(total-first, width-1):
            yield (first,)+tail


def fibers(points, modulus, degree):
    result = defaultdict(list)
    for c in compositions(degree):
        result[sum(x*y for x,y in zip(c,points)) % modulus].append(c)
    return result


def ordinary(word, degree):
    return sorted(x for x in word if x) == [1]*(degree-2)+[2]


def check_control(name, points, modulus):
    assert len(set(points)) == 8 and modulus % 2 == 1
    s = sum(points) % modulus
    original = (1,)*8
    eighth = fibers(points,modulus,8)
    assert eighth[s] == [original]
    sizes, protections, multiplicities, repeated = {}, {}, {}, {}
    all_fibers = {}
    for degree in (3,4,5):
        current = fibers(points,modulus,degree)
        all_fibers[degree] = current
        squarefree = {y for y,words in current.items() if any(max(c)==1 for c in words)}
        repeated[degree] = {y for y,words in current.items() if any(max(c)>1 for c in words)}
        protections[str(degree)] = all(len(current[y]) == 1 for y in squarefree)
        assert protections[str(degree)] and len(squarefree) == math.comb(8,degree)
        sizes[str(degree)] = len(repeated[degree])
        multiplicities[str(degree)] = max(sum(ordinary(c,degree) for c in words) for words in current.values())
    cubes = all_fibers[3]
    marks = {y:len(words) for y,words in cubes.items() if any(max(c)>1 for c in words)}
    delta = {(a-b) % modulus for a in points for b in points if a != b}
    assert len(delta) == 56
    h = sum((2*d) % modulus not in delta for d in delta)//2
    r3 = sum(math.comb(m-1,2) for m in marks.values())
    assert sizes['3'] == 36+h+r3
    # Challenge the two exact packing identities independently.
    q3 = {y for y,words in cubes.items() if max(words[0]) == 1}
    q4 = {y for y,words in all_fibers[4].items() if max(words[0]) == 1}
    assert set(cubes) & {(s-y) % modulus for y in all_fibers[5]} == q3
    assert set(all_fibers[4]) & {(s-y) % modulus for y in all_fibers[4]} == q4
    assert (s*pow(2,-1,modulus)) % modulus not in all_fibers[4]
    centers_private = True
    for degree in (4,5):
        for words in all_fibers[degree].values():
            for word in words:
                if not ordinary(word,degree):
                    continue
                center = word.index(2)
                if any(other != word and other[center] for other in words):
                    centers_private = False
    assert centers_private
    result = {'name':name, 'N':modulus, 'A':points, 'full_validity':True,
              'eight_term_words_checked':sum(map(len,eighth.values())),
              'repeated_value_counts':sizes, 'h':h, 'R3':r3,
              'max_ordinary_representations':multiplicities,
              'max_total_repeated_cubic_representations':max(marks.values()),
              'cubic_plus_quintic':sizes['3']+sizes['5'],
              'quartic_protection':protections['4'], 'private_center_check':centers_private}
    if name == 'binary':
        target = (2*sum(points[:4])) % modulus
        four_words = all_fibers[5][target]
        assert len(four_words) == 4 and all(ordinary(c,5) for c in four_words)
        lifts = []
        for i,j in itertools.combinations(range(4),2):
            rest = [k for k in range(4) if k not in (i,j)]
            left = [0]*8
            left[i] = 2
            left[4+j] = 1
            right = [0]*8
            right[j] = 2
            right[4+i] = 1
            pair = [0]*8
            for k in rest:
                pair[4+k] = 1
            value_left = sum(x*y for x,y in zip(left,points)) % modulus
            value_right = sum(x*y for x,y in zip(right,points)) % modulus
            pair_value = sum(x*y for x,y in zip(pair,points)) % modulus
            assert value_left == value_right
            assert (value_left+pair_value) % modulus == target
            lifts.append({'cubic_value':value_left, 'pair_value':pair_value,
                          'cubic_words':[left,right], 'pair_word':pair})
        assert len({row['cubic_value'] for row in lifts}) == 6
        result['reused_output'] = {'quintic_value':target, 'ordinary_words':four_words,
                                    'six_distinct_cubic_fibers_same_output':lifts}
        assert sizes['3'] < 57
    if name == 'exception':
        assert marks[0] == 4 and sum(ordinary(c,3) for c in cubes[0]) == 2
        result['exceptional_cubic_words'] = cubes[0]
    return result


def main():
    controls = [
        ('binary', [1,4,16,64,2,8,32,128], 255),
        ('doubling4', [1,17,289,4913,2,34,578,9826], 1000003),
        ('pairchain', [1,4,289,4913,2,8,578,9826], 1000003),
        ('twochains', [1,4,289,1156,2,8,578,2312], 1000003),
        ('exception', [0,100003,1,300007,17,299975,289,4913], 300009),
    ]
    output = {'controls':[check_control(*row) for row in controls],
              'boundary':'Only five declared controls; no parameter or residue-set search. Full validity outside the target interval does not refute the conditional sub-248 theorem.'}
    Path('stage42_fixed_controls_results.json').write_text(json.dumps(output,indent=2)+'\n', encoding='utf-8')
    print(json.dumps({**output, 'controls':[{k:v for k,v in row.items() if k not in ('reused_output','exceptional_cubic_words')} for row in output['controls']]},indent=2))


if __name__ == '__main__':
    main()
