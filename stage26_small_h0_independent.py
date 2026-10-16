"""Independent BFS orbit inventory and complete necessary-union/centroid checks.

No producer or historical imports. This verifies new finite premises only,
not actual cyclic-set enumeration or the historical order-seven theorem.
"""
from itertools import combinations,product
from math import gcd
import json
from pathlib import Path
from time import monotonic

def main():
    start=monotonic(); records=[]; surviving=[]
    producer=json.loads(Path('stage26_small_h0_orbit_results.json').read_text())
    assert producer['completion']=='COMPLETE'
    original={r['H']:r for r in producer['records']}
    assert set(original)==set(range(187,248,2))
    for n in range(187,248,2):
        if monotonic()-start>=10: raise TimeoutError('Independent arithmetic incomplete')
        seen=set(); blocks=[]
        for seed in range(1,n):
            if seed in seen: continue
            found={seed}; queue=[seed]
            while queue:
                x=queue.pop()
                for y in ((-x)%n,(x+x)%n):
                    if y not in found:
                        found.add(y); queue.append(y)
            assert 0 not in found and not seen&found
            seen|=found; blocks.append(sorted(found))
        assert seen==set(range(1,n))
        assert {tuple(b) for b in blocks}=={tuple(b['residues']) for b in original[n]['blocks']}
        allowed=[b for b in blocks if len(b)<=56 and all(3*x%n for x in b)]
        unions=[]
        for mask in range(1<<len(allowed)):
            chosen=[b for i,b in enumerate(allowed) if mask>>i&1]
            if sum(map(len,chosen))!=56: continue
            delta=sorted(x for b in chosen for x in b)
            if gcd(n,*delta)!=1: continue
            assert len(delta)==56 and set(delta)=={2*x%n for x in delta}=={(-x)%n for x in delta}
            entry={'representatives':[b[0] for b in chosen],
                   'block_sizes':[len(b) for b in chosen]}
            if n in (195,217,221):
                quotient={195:13,217:31,221:13}[n]
                weights=[sum(x%quotient==q for x in delta) for q in range(quotient)]
                entry['projected_difference_weights']=weights
                if n==195:
                    assert weights==[8]+[4]*12
                    assert {x for x in delta if x%13==0}=={13*k for k in range(1,15) if gcd(k,15)==1}
                elif n==217:
                    # Order-31 blocks can overlap the projected unit orbit;
                    # only the six kernel differences are needed below.
                    assert weights[0]==6 and sum(weights[1:])==50
                else:
                    assert weights==[8]+[4]*12
                    inside=[x//13 for x in delta if x%13==0]
                    assert len(inside)==8 and set(inside)=={2*x%17 for x in inside}
            if n==215: assert all(gcd(x,215)==1 for x in delta)
            if n==225: assert all(gcd(x,225)>1 for x in delta)
            unions.append(entry)
        assert bool(unions)==original[n]['necessary_orbit_union_exists']
        if unions: surviving.append(n)
        records.append({'H':n,'orbit_count':len(blocks),'eligible_orbits':len(allowed),
                        'subsets_examined':1<<len(allowed),'necessary_unions':unions})
    assert surviving==[195,215,217,221,225]
    perfect=[]; normalized=[]
    for a in combinations(range(13),4):
        differences=[(x-y)%13 for x in a for y in a if x!=y]
        if len(set(differences))!=12: continue
        # 10 is the inverse of 4 modulo 13; this is a unit inverse.
        centroid=sum(a)*10%13
        assert centroid in a
        perfect.append({'set':a,'centroid':centroid})
        if 0 in a and 1 in a: normalized.append({'set':a,'centroid':centroid})
    assert len(perfect)==52 and len(normalized)==4
    signed17={pow(2,k,17) for k in range(8)}|{(-pow(2,k,17))%17 for k in range(8)}
    assert len(signed17)==8 and signed17=={1,2,4,8,9,13,15,16}
    witnesses={}
    # The centroid pair is normalized to step 1; changing a pair's sign
    # translates its possible sums, so orientation does not affect coverage.
    for k,b,c,d in product(range(6),(0,1),(0,1),(0,1)):
        witnesses.setdefault((k+2*b+4*c+8*d)%17,[k,b,c,d])
    assert set(witnesses)==set(range(17))
    assert monotonic()-start<10
    result={'completion':'COMPLETE','seconds_limit':10,'elapsed_seconds':monotonic()-start,
            'surviving_orders':surviving,'records':records,
            'four_subsets_checked':715,'perfect_difference_sets':perfect,
            'normalized_perfect_sets':normalized,'mod17_replacement_witnesses':witnesses,
            'scope':'Independent necessary orbit unions and finite projection/replacement arithmetic; not set validity enumeration.'}
    Path('stage26_small_h0_independent_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print('COMPLETE in',result['elapsed_seconds'],'seconds')
    print('surviving unions:',[(r['H'],len(r['necessary_unions'])) for r in records if r['necessary_unions']])
    print('52 perfect sets checked; all 17 replacement residues witnessed')

if __name__=='__main__': main()
