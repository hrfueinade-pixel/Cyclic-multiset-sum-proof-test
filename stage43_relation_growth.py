"""Positive growth certificates for the finite four-pair cubic inventory.

The inventory has 16 permitted direction types. Each is parametrized
without dividing a nonunit; two require an explicit finite torsion
coordinate. Fixed two-second clique cap per model, with no group search.
"""
import argparse
import gzip
import itertools
import json
import math
import time
from pathlib import Path

from stage41_saturated_fiber_closure import find_clique
from stage43_fourpair_inventory import parameter_rows, words


def models():
    inventory = json.loads(Path('stage43_fourpair_inventory_results.json').read_text())
    result = []
    for index, direction in enumerate(inventory['permitted_classes']):
        d = tuple(direction)
        rows = parameter_rows(d)
        torsion = (0,)*8
        order = 1
        proof = 'unit-pivot'
        if d == (-6,0,0,3):
            centers = ((1,0,0,0), (0,1,0,0), (0,0,1,0), (2,0,0,0))
            rows = centers+tuple(tuple(2*x for x in row) for row in centers)
            torsion = (0,0,0,1,0,0,0,2)
            order = 3
            proof = 'delta=c3-2c0, 3delta=0'
        elif d == (-5,0,0,5):
            centers = ((1,0,0,0), (0,1,0,0), (0,0,1,0), (1,0,0,0))
            rows = centers+tuple(tuple(2*x for x in row) for row in centers)
            torsion = (0,0,0,1,0,0,0,2)
            order = 5
            proof = 'delta=c3-c0, 5delta=0'
        elif d == (-6,0,0,5):
            centers = ((5,0,0,0), (0,1,0,0), (0,0,1,0), (6,0,0,0))
            rows = centers+tuple(tuple(2*x for x in row) for row in centers)
            proof = 't=c3-c0 gives c0=5t and c3=6t'
        assert rows is not None
        result.append({'id':f'r{index:02}', 'direction':d, 'rows':rows,
                       'torsion_rows':torsion, 'torsion_order':order,
                       'parameterization':proof})
    return result


def coords(c, model):
    return tuple(sum(c[i]*model['rows'][i][j] for i in range(8)) for j in range(len(model['rows'][0]))), sum(c[i]*model['torsion_rows'][i] for i in range(8)) % model['torsion_order']


def subtract(a,b,order):
    return tuple(x-y for x,y in zip(a[0],b[0])), (a[1]-b[1]) % order


def ray(f):
    scale = math.gcd(*f)
    if next(x for x in f if x) < 0:
        scale = -scale
    return tuple(x//scale for x in f), scale


def run(model, degree, target, units):
    start = time.monotonic()
    order = model['torsion_order']
    stem = f"stage43_{model['id']}_degree{degree}_units{''.join(map(str,units))}"
    assert all(math.gcd(p,order) == 1 for p in units)
    base = coords((1,)*8,model)
    rays, pure = {}, []
    for c in words(8):
        if c == (1,)*8:
            continue
        f = subtract(coords(c,model),base,order)
        if not any(f[0]) and not f[1]:
            data = {'kind':'direct_rival', 'model':model, 'rival':''.join(map(str,c))}
            Path(stem+'_certificate.json.gz').write_bytes(gzip.compress(json.dumps(data,separators=(',',':')).encode(),mtime=0))
            return {'model':model['id'], 'direction':model['direction'], 'torsion_order':order,
                    'degree':degree, 'units':units, 'positive_bound':0,
                    'direct_rival':data['rival'], 'pair_records':0,
                    'elapsed_seconds':time.monotonic()-start,
                    'certificate':stem+'_certificate.json.gz'}
        if any(f[0]):
            direction, scale = ray(f[0])
            rays.setdefault(direction, []).append((scale,f[1],c))
        else:
            pure.append((f[1],c))
    cache = {}
    def witness(original):
        if original in cache:
            return cache[original]
        free, torsion = original
        factor = 1
        for p in units:
            while any(free) and all(x % p == 0 for x in free):
                free = tuple(x//p for x in free)
                torsion = torsion*pow(p,-1,order) % order if order > 1 else 0
                factor *= p
        answer = None
        if any(free):
            direction, scale = ray(free)
            for rival_scale,rival_torsion,c in rays.get(direction, ()):
                if rival_scale % scale == 0:
                    k = rival_scale//scale
                    if (k*torsion-rival_torsion) % order == 0:
                        answer = (c,k,factor)
                        break
        elif torsion:
            for k in range(1,order):
                for rival_torsion,c in pure:
                    if (k*torsion-rival_torsion) % order == 0:
                        answer = (c,k,factor)
                        break
                if answer:
                    break
        cache[original] = answer
        return answer
    representatives = {}
    for c in words(degree):
        if max(c)>1:
            representatives.setdefault(coords(c,model),c)
    vectors = list(representatives)
    adj = [0]*len(vectors)
    for i,left in enumerate(vectors):
        for j in range(i):
            if witness(subtract(left,vectors[j],order)):
                adj[i] |= 1 << j
                adj[j] |= 1 << i
    clique,complete,nodes = find_clique(adj,target,seconds=2)
    selected = [representatives[vectors[i]] for i in clique]
    pairs = []
    for i,j in itertools.combinations(clique,2):
        c,k,factor = witness(subtract(vectors[i],vectors[j],order))
        pairs.append({'rival':''.join(map(str,c)), 'multiplier':k, 'canceled_unit_factor':factor})
    data = {'model':model, 'degree':degree, 'units':units,
            'words':[''.join(map(str,c)) for c in selected], 'pairs':pairs}
    Path(stem+'_certificate.json.gz').write_bytes(gzip.compress(json.dumps(data,separators=(',',':')).encode(),mtime=0))
    return {'model':model['id'], 'direction':model['direction'], 'torsion_order':order,
            'degree':degree, 'units':units, 'formal_values':len(vectors), 'positive_bound':len(selected),
            'pair_records':len(pairs), 'target':target, 'discovery_complete':complete,
            'discovery_cap_seconds':2, 'discovery_nodes':nodes, 'elapsed_seconds':time.monotonic()-start,
            'certificate':stem+'_certificate.json.gz'}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model')
    parser.add_argument('--degree',type=int,default=4)
    parser.add_argument('--target',type=int,default=89)
    parser.add_argument('--units',default='2')
    args = parser.parse_args()
    units = [int(p) for p in args.units.split(',')]
    selected = [m for m in models() if args.model is None or m['id'] == args.model]
    assert selected
    results = []
    for model in selected:
        result = run(model,args.degree,args.target,units)
        results.append(result)
        print(json.dumps(result),flush=True)
    suffix = args.model or 'inventory'
    path = f"stage43_{suffix}_degree{args.degree}_units{''.join(map(str,units))}_results.json"
    Path(path).write_text(json.dumps({'results':results,'boundary':'Positive model certificates only; fixed symbolic inventory, no parameter or modulus sweep.'},indent=2)+'\n',encoding='utf-8')


if __name__ == '__main__':
    main()
