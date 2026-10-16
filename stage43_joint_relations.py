"""Complete two-relation atlas for the three unclosed cubic direction types.

This enumerates symbolic directions, not cyclic moduli or parameters.
Unimodular transformations retain all torsion; oddness cancels only two.
"""
import itertools
import gzip
import json
import math
from pathlib import Path

from stage43_relation_growth import run


TYPES = ((-4,0,0,1), (-5,0,1,4), (-4,-1,1,4))


def sign_normal(v):
    return tuple(-x for x in v) if next(x for x in v if x) < 0 else tuple(v)


def canonical_pair(left,right):
    return min(tuple(sorted((sign_normal(tuple(left[i] for i in p)),
                             sign_normal(tuple(right[i] for i in p)))))
               for p in itertools.permutations(range(4)))


def bezout(a,b):
    old_r,r = a,b
    old_s,s = 1,0
    old_t,t = 0,1
    while r:
        q = old_r//r
        old_r,r = r,old_r-q*r
        old_s,s = s,old_s-q*s
        old_t,t = t,old_t-q*t
    if old_r < 0:
        return -old_r,-old_s,-old_t
    return old_r,old_s,old_t


def first_rows(d):
    pivot = min((i for i,x in enumerate(d) if x and abs(x) & (abs(x)-1) == 0),key=lambda i:abs(d[i]))
    others = [i for i in range(4) if i != pivot]
    scale = abs(d[pivot])
    rows = [[0]*3 for _ in range(4)]
    for j,i in enumerate(others):
        rows[i][j] = scale
        rows[pivot][j] = -d[i]*(1 if d[pivot] > 0 else -1)
    return rows,pivot,scale


def quotient_model(left,right,index):
    rows,pivot,scale = first_rows(left)
    vector = [sum(right[i]*rows[i][j] for i in range(4)) for j in range(3)]
    original = vector[:]
    assert any(vector)
    transform = [[int(i == j) for j in range(3)] for i in range(3)]
    for j in (1,2):
        a,b = vector[0],vector[j]
        if a == b == 0:
            continue
        g,s,t = bezout(a,b)
        col0 = [row[0] for row in transform]
        colj = [row[j] for row in transform]
        for i in range(3):
            transform[i][0] = s*col0[i]+t*colj[i]
            transform[i][j] = -(b//g)*col0[i]+(a//g)*colj[i]
        vector[0],vector[j] = g,0
    g = vector[0]
    assert g > 0 and vector[1:] == [0,0]
    order = g
    while order % 2 == 0:
        order //= 2
    merged = [[sum(rows[i][k]*transform[k][j] for k in range(3)) for j in range(3)] for i in range(4)]
    centers = tuple((row[1],row[2],0,0) for row in merged)
    torsion = tuple(row[0] % order for row in merged)
    return {'id':f'j{index:02}', 'relations':[left,right], 'direction':list(left),
            'rows':centers+tuple(tuple(2*x for x in row) for row in centers),
            'torsion_rows':torsion+tuple(2*x % order for x in torsion),
            'torsion_order':order, 'first_unit_pivot':pivot, 'first_unit_scale':scale,
            'first_rows':rows, 'second_after_first':original,
            'unimodular_transform':transform, 'diagonal_gcd':g,
            'parameterization':'First unit pivot then unimodular single-row reduction; odd part of gcd retained as torsion.'}


def atlas():
    directions = sorted({sign_normal(tuple(v[i] for i in p)) for v in TYPES for p in itertools.permutations(range(4))})
    pairs = sorted({canonical_pair(a,b) for a,b in itertools.combinations(directions,2)})
    return directions,[quotient_model(*pair,index) for index,pair in enumerate(pairs)]


def main():
    directions,models = atlas()
    results = []
    for model in models:
        retained = Path(f"stage43_{model['id']}_degree4_units2_certificate.json.gz")
        if retained.exists():
            data = json.loads(gzip.decompress(retained.read_bytes()))
            assert data['model'] == json.loads(json.dumps(model))
            result = {'model':model['id'], 'direction':model['direction'],
                      'torsion_order':model['torsion_order'], 'degree':4, 'units':[2],
                      'positive_bound':len(data.get('words',[])),
                      'pair_records':len(data.get('pairs',[])),
                      'certificate':retained.name, 'reused_positive_certificate':True}
            if data.get('kind') == 'direct_rival':
                result['direct_rival'] = data['rival']
        else:
            result = run(model,4,89,[2])
        results.append(result)
        print(json.dumps(result),flush=True)
    output = {'directions':directions, 'direction_count':len(directions),
              'raw_unordered_pairs':math.comb(len(directions),2),
              'models':models, 'results':results,
              'boundary':'Complete fixed symbolic two-relation atlas under S4/sign/swap. Positive growth bounds do not imply a general theorem until the independent checker verifies coverage and every certificate.'}
    Path('stage43_joint_relations_results.json').write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8')


if __name__ == '__main__':
    main()
