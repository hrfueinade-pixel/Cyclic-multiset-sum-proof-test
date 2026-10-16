"""Rebuild normalized-family coverage and check every eight-term identity.

No producer imports or reachability search. A separate enumeration uses
divisors as point orders, lists ordered differences, and reconstructs
the set from saved starts rather than trusting saved A data. 30s cap.
"""
from pathlib import Path
from time import monotonic
from math import gcd
import json

start=monotonic(); cap=30
def check_time():
    if monotonic()-start>=cap: raise TimeoutError('Independent coverage incomplete')
data=json.loads(Path('stage29_two_path_results.json').read_text())
assert data['completion']=='COMPLETE' and not data['survivors']
verified={}; per_order={}
for n,length,x,y,text in data['exclusions']:
    check_time()
    assert n in range(185,248,2) and length in (1,2,3,4)
    assert 0<x<n and n%x==0 and 0<=y<n and gcd(n,x,y)==1
    points=sorted({pow(2,k,n)*x%n for k in range(length)}|
                  {pow(2,k,n)*y%n for k in range(8-length)})
    assert len(points)==8
    counts=[int(c) for c in text]
    assert len(counts)==8 and sum(counts)==8 and 0 in counts
    assert sum((c-1)*a for c,a in zip(counts,points))%n==0
    differences=[(points[i]-points[j])%n for i in range(8) for j in range(8) if i!=j]
    assert len(set(differences))==len(differences)==56
    key=(n,tuple(points)); assert key not in verified
    verified[key]=text; per_order[n]=per_order.get(n,0)+1

expected=set(); parameters=0; rows=[]
for modulus in range(185,248,2):
    local=0; row_params=0
    orders=[order for order in range(2,modulus+1) if modulus%order==0]
    for order in orders:
        first=modulus//order
        for second in range(modulus):
            if gcd(modulus,first,second)!=1: continue
            for size in range(1,5):
                check_time(); parameters+=1; row_params+=1
                # Iterative doubling, independent of producer power expressions.
                sequence=[]
                for seed,terms in ((first,size),(second,8-size)):
                    v=seed
                    for _ in range(terms):
                        sequence.append(v); v=(v+v)%modulus
                if len(set(sequence))!=8: continue
                ordered=[]
                for p in sequence:
                    for q in sequence:
                        if p!=q: ordered.append((p-q)%modulus)
                if len(set(ordered))!=56: continue
                key=(modulus,tuple(sorted(sequence)))
                assert key in verified, key
                if key not in expected: local+=1
                expected.add(key)
    rows.append({'n':modulus,'parameters':row_params,'sidon_sets':local})
assert expected==set(verified)
assert parameters==sum(r['parameters'] for r in data['statistics'])==71512
assert len(verified)==30204
assert {r['n']:r['parameters'] for r in rows}=={r['n']:r['parameters'] for r in data['statistics']}
assert {r['n']:r['sidon_sets'] for r in rows}=={r['n']:r['distinct_sidon_sets'] for r in data['statistics']}
result={'completion':'COMPLETE','cap_seconds':cap,
        'elapsed_seconds':monotonic()-start,'parameters_checked':parameters,
        'identities_checked':len(verified),'coverage':rows,'imports_producer':False,
        'scope':'Two-path family at odd185..247 only; no general set search'}
Path('stage29_two_path_independent_results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='coverage'}))
