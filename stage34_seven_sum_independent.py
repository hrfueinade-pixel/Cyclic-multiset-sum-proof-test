"""New seven-sum necessary six-point family; independent180s cap.

No producer imports. Sets with a unit difference normalize to0,1;
remaining sets have only nonunit differences and normalize to0,g for
some proper divisor g. Sumsets use explicit count-of-new-point union,
not the producer's unbounded-coin recurrence. Validity is derived by
the number of copies of the new point; q=1 uses prefix validity.
"""
from pathlib import Path
from time import monotonic
from math import gcd
import json

start=monotonic(); cap=180; results=[]; survivors=[]
def prime_count(n):
    return sum(all(p%d for d in range(2,int(p**0.5)+1)) and n%p==0
               for p in range(2,n+1))

def run(m):
    full=2**m-1; nodes=[0]*7; found=[]; examined=set()
    roots=[1]
    if prime_count(m)>=3:
        roots += [m//order for order in range(3,m) if m%order==0]
    def shift(bits,x):
        x%=m
        return ((bits<<x)|(bits>>(m-x)))&full
    def recurse(prefix,levels,next_value,unitless):
        if monotonic()-start>cap:raise TimeoutError()
        nodes[len(prefix)]+=1
        if levels[7]==full:return
        if len(prefix)==6:
            if gcd(m,*prefix)!=1:return
            key=tuple(sorted(prefix))
            if key not in examined:
                examined.add(key)
                row={'M':m,'B':list(key),
                     'missing':[a for a in range(m) if not (levels[7]>>a)&1]}
                found.append(row); survivors.append(row)
            return
        terms=len(prefix)+1
        original=sum(prefix)
        for value in range(next_value,m):
            if value in prefix:continue
            if unitless and any(gcd(value-a,m)==1 for a in prefix):continue
            candidate=prefix+[value]
            differences=[(a-b)%m for a in candidate for b in candidate if a!=b]
            if len(set(differences))!=terms*(terms-1):continue
            if any((levels[terms-copies]>>((original+(1-copies)*value)%m))&1
                   for copies in range(terms+1) if copies!=1):continue
            # Explicit union by copy count is independent of coin recurrence.
            following=[]
            for size in range(9):
                residue_set=0
                for copies in range(size+1):
                    residue_set |= shift(levels[size-copies],copies*value)
                following.append(residue_set)
            recurse(candidate,following,value+1,unitless)
    for first in roots:
        if 2*first==m:continue
        levels=[]
        for k in range(9):
            levels.append(sum(1<<r for r in {first*j%m for j in range(k+1)}))
        recurse([0,first],levels,1,first!=1)
    return {'M':m,'completion':'COMPLETE','roots':roots,
            'prefix_counts':nodes,'survivors':len(found)}

complete=True; current=None
for m in range(64,124):
    current=m
    try:
        r=run(m); results.append(r)
        print(json.dumps({'M':m,'nodes':sum(r['prefix_counts']),
                          'survivors':r['survivors'],'seconds':monotonic()-start}),flush=True)
    except TimeoutError:
        complete=False;break
producer=json.loads(Path('stage34_combined_results.json').read_text())
if complete:
    assert producer['completion']=='COMPLETE'
    expected={(r['M'],tuple(r['B'])):set(r['missing_7B']) for r in producer['survivors']}
    found={(r['M'],tuple(r['B'])):set(r['missing']) for r in survivors}
    assert found==expected and len(found)==len(survivors)
    assert [r['M'] for r in results]==list(range(64,124))
out={'completion':'COMPLETE' if complete else 'TIMEOUT/incomplete',
     'cap_seconds':cap,'elapsed_seconds':monotonic()-start,
     'coverage':'Unit-difference normalization plus unitless normalized roots',
     'completed_orders':[r['M'] for r in results],
     'interrupted_order':None if complete else current,
     'reports':results,'survivors':survivors,'imports_producer':False}
Path('stage34_seven_sum_independent_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('reports','survivors')}),flush=True)
if not complete:
    raise SystemExit(2)
