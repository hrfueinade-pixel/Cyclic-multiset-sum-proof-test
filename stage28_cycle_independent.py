"""Separate actual-multiset enumeration for the new quotient lemma.

No producer imports. All multisets of <=4 terms from four labeled path
points, all generating quotient pairs; a five-second cooperative cap.
"""
from itertools import combinations_with_replacement
from math import gcd
from pathlib import Path
from time import monotonic
import json

start=monotonic()
saved=json.loads(Path('stage28_cycle_quotient_results.json').read_text())
assert saved['completion']=='COMPLETE' and not saved['survivors']
witnesses={(r['q'],r['x'],r['z']):r for r in saved['witnesses']}
assert len(witnesses)==len(saved['witnesses'])
actual=[s for k in range(5) for s in combinations_with_replacement(range(4),k)
        if s!=(0,1,2,3)]
expected=set(); records=[]
for q in (13,15):
    for a in range(q):
        for b in range(q):
            if gcd(q,a,b)!=1: continue
            if monotonic()-start>=5: raise TimeoutError('Independent check incomplete')
            key=(q,a,b); expected.add(key)
            points=[a,2*a,b,2*b]
            target=sum(points)%q
            alternatives=[s for s in actual if sum(points[i] for i in s)%q==target]
            assert alternatives, key
            w=witnesses[key]; c=w['path_counts']
            assert len(c)==4 and all(type(n)==int and n>=0 for n in c)
            assert sum(c)<=4 and c!=[1,1,1,1]
            assert sum(n*t for n,t in zip(c,points))%q==target
            assert [c[0]+2*c[1],c[2]+2*c[3]]==w['coefficients']
            records.append({'q':q,'x':a,'z':b,'alternative_terms':list(alternatives[0]),
                            'alternative_count':len(alternatives)})
assert set(witnesses)==expected and len(expected)==360
out={'completion':'COMPLETE','cap_seconds':5,
     'elapsed_seconds':monotonic()-start,'verified_cases':len(expected),
     'independent_witnesses':records,'imports_producer':False}
Path('stage28_cycle_independent_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='independent_witnesses'}))
