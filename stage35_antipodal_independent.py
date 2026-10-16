"""All-zero-normalized five-set enumeration plus exact antipodal lift audit.

No producer imports. Unlike unit-root search, all139503 five-subsets
containing0 at16..30 are considered, including antipodes. Independent
full-multiset validity and complete lift-domain checks;60s global cap.
"""
from pathlib import Path
from itertools import combinations,combinations_with_replacement,product
from math import gcd
from time import monotonic
import json

start=monotonic();cap=60;raw=[];classes=set();reports=[]
def tick():
    if monotonic()-start>=cap:raise TimeoutError('Antipodal audit incomplete')
def key(m,a):
    return min(tuple(sorted((v*(x-o))%m for x in a))
               for v in range(1,m) if gcd(v,m)==1 for o in a)
def valid(m,a):
    target=sum(a)%m;matches=0
    for t in combinations_with_replacement(a,len(a)):
        if sum(t)%m==target:
            matches+=1
            if matches>1:return False
    return matches==1
for m in range(16,31):
    considered=0;pair_surv=0;accepted=0
    for t in combinations(range(1,m),4):
        tick();considered+=1;a=(0,*t)
        square=[sum(p)%m for p in combinations(a,2)]
        doubles={2*x%m for x in a}
        if len(set(square))!=10 or set(square)&doubles:continue
        pair_surv+=1
        if not valid(m,a):continue
        assert gcd(m,*a)==1
        raw.append({'N':m,'A':list(a)});classes.add((m,key(m,a)));accepted+=1
    reports.append({'N':m,'five_subsets':considered,'pair_survivors':pair_surv,'valid':accepted})
assert sum(r['five_subsets'] for r in reports)==139503
producer=json.loads(Path('stage35_antipodal_seven_results.json').read_text())
assert producer['completion']=='COMPLETE'
expected={(r['N'],tuple(r['A'])) for r in producer['five_affine_classes']}
assert classes==expected
assert {(r['N'],tuple(r['A'])) for r in producer['valid_five_normalized']} <= {(r['N'],tuple(r['A'])) for r in raw}
def all_lifts(m,a):
    family=[]
    for i in range(len(a)):
        free=[x for j,x in enumerate(a) if j!=i]
        for choices in product((0,m),repeat=len(free)):
            family.append((2*m,tuple(sorted([a[i],a[i]+m]+[x+y for x,y in zip(free,choices)]))))
    return family
six_expected=[p for m,a in sorted(classes) for p in all_lifts(m,a)]
assert len(six_expected)==480
six_source={(r['N'],tuple(r['A'])):r for r in producer['six_lifts']}
assert len(six_source)==480 and set(six_source)==set(six_expected)
six_classes=set();identities=0
for m,a in six_expected:
    tick();truth=valid(m,a);row=six_source[(m,a)]
    assert truth==(row['rival'] is None)
    if truth:six_classes.add((m,key(m,a)))
    else:
        c=row['rival']
        assert len(c)==6 and all(type(x)==int and x>=0 for x in c)
        assert sum(c)==6 and c!=[1]*6
        assert sum((x-1)*v for x,v in zip(c,a))%m==0
        identities+=1
assert six_classes=={(r['N'],tuple(r['A'])) for r in producer['six_affine_classes']}
seven_expected=[p for m,a in sorted(six_classes) for p in all_lifts(m,a)]
seven_source={(r['N'],tuple(r['A'])):r for r in producer['seven_lifts']}
assert len(seven_expected)==len(seven_source)==192 and set(seven_source)==set(seven_expected)
for m,a in seven_expected:
    tick();assert not valid(m,a)
    c=seven_source[(m,a)]['rival']
    assert len(c)==7 and all(type(x)==int and x>=0 for x in c)
    assert sum(c)==7 and c!=[1]*7
    assert sum((x-1)*v for x,v in zip(c,a))%m==0
    identities+=1
assert not producer['seven_survivors']
out={'completion':'COMPLETE','cap_seconds':cap,'elapsed_seconds':monotonic()-start,
     'all_five_coverage':reports,'valid_five_with_zero':raw,
     'five_affine_classes':[{'N':m,'A':list(a)} for m,a in sorted(classes)],
     'six_lifts_checked':len(six_expected),'seven_lifts_checked':len(seven_expected),
     'integer_identities_checked':identities,'imports_producer':False}
Path('stage35_antipodal_independent_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('all_five_coverage','valid_five_with_zero','five_affine_classes')}))
