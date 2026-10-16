"""Fixed symbolic collision models: no group-parameter search.

A=(0,2u,2v,2w,z,z+u,z+2u-v,z+2u-w). Equalities between
coefficient vectors are challenged against ALL degree-eight rival vectors,
with only the declared unit factors canceled. Quartic and quintic cliques
are positive growth certificates. Absence/timeout excludes no model.
"""
import itertools
import argparse
import math
import json
import time


MODEL = ((0,0,0,0), (2,0,0,0), (0,2,0,0), (0,0,2,0),
         (0,0,0,1), (1,0,0,1), (2,-1,0,1), (2,0,-1,1))
MODELS = {
    'leaf22':MODEL,
    'hub22':((0,0,0,0),(2,0,0,0),(0,2,0,0),(0,0,2,0),
             (0,0,0,1),(-1,0,0,1),(0,-1,0,1),(0,0,-1,1)),
    'fourO':((0,0,0,0),(2,0,0,0),(0,2,0,0),(0,0,2,0),
             (-1,0,0,1),(0,-1,0,1),(-1,-1,0,1),(0,-1,-1,1)),
    'purehub':((0,0,0,0),(2,0,0,0),(0,2,0,0),(0,0,2,0),
                (-1,0,0,0),(0,-1,0,0),(0,0,-1,0),(0,0,0,1))}


def degree_words(degree):
    for w in itertools.combinations_with_replacement(range(8), degree):
        yield tuple(w.count(i) for i in range(8))


def coeff(c):
    return tuple(sum(c[i]*MODEL[i][j] for i in range(8)) for j in range(4))


def primitive_units(v, units):
    assert any(v)
    v = tuple(v)
    for p in units:
        while all(x % p == 0 for x in v):
            v = tuple(x//p for x in v)
    return v


def ray(v):
    g=math.gcd(*v)
    p=tuple(x//g for x in v)
    if next(x for x in p if x)<0:
        p=tuple(-x for x in p)
    return p,g


def find_clique(adj, target=89, seconds=10):
    deadline = time.monotonic()+seconds
    best = []
    nodes = 0
    complete = True

    def color_sort(p):
        order, bounds = [], []
        color = 0
        while p:
            color += 1
            q = p
            while q:
                bit = q & -q
                v = bit.bit_length()-1
                p ^= bit
                q ^= bit
                q &= ~adj[v]
                order.append(v)
                bounds.append(color)
        return order,bounds

    def expand(c,p):
        nonlocal best,nodes
        nodes += 1
        if len(best)>=target:
            raise StopIteration
        if nodes % 128==0 and time.monotonic()>deadline:
            raise TimeoutError
        order,bounds=color_sort(p)
        for i in range(len(order)-1,-1,-1):
            if len(c)+bounds[i]<=len(best):
                return
            v=order[i]
            nxt=p & adj[v]
            if nxt:
                expand(c+[v],nxt)
            elif len(c)+1>len(best):
                best=c+[v]
                if len(best)>=target:
                    raise StopIteration
            p &= ~(1<<v)

    try:
        expand([], (1<<len(adj))-1)
    except (StopIteration,TimeoutError):
        complete=False
    return best,complete,nodes


def main():
    global MODEL
    p=argparse.ArgumentParser()
    p.add_argument('--units',default='2')
    p.add_argument('--output',default='stage41_saturated_fiber_closure_results.json')
    p.add_argument('--integer-rays',action='store_true')
    p.add_argument('--modulus',type=int)
    p.add_argument('--degree',type=int,default=4)
    p.add_argument('--target',type=int,default=89)
    p.add_argument('--model',choices=tuple(MODELS),default='leaf22')
    args=p.parse_args()
    MODEL=MODELS[args.model]
    units=tuple(int(x) for x in args.units.split(','))
    start=time.monotonic()
    base=coeff((1,)*8)
    forbidden={}
    rays={}
    modular_forbidden={}
    for c in degree_words(8):
        if c==(1,)*8:
            continue
        f=tuple(x-y for x,y in zip(coeff(c),base))
        assert any(f), 'Model has an integer rival!'
        p=primitive_units(f,units)
        forbidden.setdefault(p,c)
        forbidden.setdefault(tuple(-x for x in p),c)
        rp,rg=ray(f)
        rays.setdefault(rp,[]).append((rg,c))
        if args.modulus:
            modular_forbidden.setdefault(tuple(x % args.modulus for x in f),c)

    difference_cache={}
    def rival_for_difference(d):
        if args.modulus:
            if d not in difference_cache:
                match=None
                for m in range(1,args.modulus):
                    c=modular_forbidden.get(tuple(m*x % args.modulus for x in d))
                    if c is not None:
                        match=c
                        break
                difference_cache[d]=match
            return difference_cache[d]
        d=primitive_units(d,units)
        if not args.integer_rays:
            return forbidden.get(d)
        rp,rg=ray(d)
        for scale,c in rays.get(rp,[]):
            if scale % rg==0:
                return c
        return None
    representatives={}
    for c in degree_words(args.degree):
        if max(c)>1:
            representatives.setdefault(coeff(c),c)
    vectors=list(representatives)
    adj=[0]*len(vectors)
    for i,v in enumerate(vectors):
        for j in range(i):
            d=tuple(x-y for x,y in zip(v,vectors[j]))
            if rival_for_difference(d) is not None:
                adj[i] |=1<<j
                adj[j] |=1<<i
    clique,complete,nodes=find_clique(adj,target=args.target)
    certificate=[]
    for i,j in itertools.combinations(clique,2):
        original_d=tuple(x-y for x,y in zip(vectors[i],vectors[j]))
        d=original_d if args.modulus else primitive_units(original_d,units)
        c=rival_for_difference(d)
        assert c is not None
        f=tuple(x-y for x,y in zip(coeff(c),base))
        if args.modulus:
            assert any(all((f[k]-m*d[k]) % args.modulus==0 for k in range(4))
                       for m in range(1,args.modulus))
        elif args.integer_rays:
            rd,gd=ray(d)
            rf,gf=ray(f)
            assert rd==rf and gf % gd==0
        else:
            f=primitive_units(f,units)
            assert f==d or tuple(-x for x in f)==d
        certificate.append([i,j,''.join(map(str,c))])
    result={
        'model_name':args.model,'model':MODEL,'base_coefficient':base,'invertible_primes_required':units,
        'integer_multiple_closure':args.integer_rays,
        'modulus_for_cyclic_closure':args.modulus,
        'degree':args.degree,'repeated_sum_coefficient_vectors':len(vectors),
        'forbidden_primitive_signed_vectors':len(forbidden),
        'target':args.target,'clique_size':len(clique),
        'search_complete':complete,'search_nodes':nodes,
        'selected':[{'index':i,'coefficient':vectors[i],
                     'quartic_word':representatives[vectors[i]]} for i in clique],
        'pair_certificates':certificate,
        'elapsed_seconds':time.monotonic()-start,
        'boundary':'Positive clique certificates concern this fixed symbolic model only; no arbitrary sets or cyclic moduli are enumerated.'}
    with open(args.output,'w',encoding='utf-8') as f:
        json.dump(result,f,separators=(',',':'))
        f.write('\n')
    print(json.dumps({k:v for k,v in result.items()
                      if k not in ('selected','pair_certificates')},indent=2))


if __name__=='__main__':
    main()
