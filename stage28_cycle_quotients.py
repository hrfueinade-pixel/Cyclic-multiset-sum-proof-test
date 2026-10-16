"""Complete four-cycle quotient replacement lemma; five-second cap.

Necessary arithmetic only, not enumeration of valid eight-point sets.
Each witness uses at most four points from x,2x,z,2z, and changes
the coefficient pair (3,3) while keeping its quotient sum.
"""
import json
from math import gcd
from pathlib import Path
from time import monotonic

start=monotonic()
choices=[(u,v) for u in range(9) for v in range(9)
         if (u+1)//2+(v+1)//2<=4 and (u,v)!=(3,3)]
records=[]; survivors=[]
for q in (13,15):
    for x in range(q):
        for z in range(q):
            if monotonic()-start>=5:
                raise TimeoutError('Incomplete four-cycle arithmetic')
            if gcd(q,x,z)!=1: continue
            matches=[(u,v) for u,v in choices
                     if ((u-3)*x+(v-3)*z)%q==0]
            if not matches:
                survivors.append([q,x,z]); continue
            u,v=matches[0]
            counts=[u%2,u//2,v%2,v//2]
            assert sum(counts)<=4 and counts!=[1,1,1,1]
            records.append({'q':q,'x':x,'z':z,'coefficients':[u,v],
                            'path_counts':counts})
out={'completion':'COMPLETE','scope':'All generating pairs modulo13 and15',
     'cap_seconds':5,'elapsed_seconds':monotonic()-start,
     'cases':len(records)+len(survivors),'witnesses':records,'survivors':survivors}
Path('stage28_cycle_quotient_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='witnesses'}))
