"""Every seventh-point extension of the complete six-point survivor list.

5s cap. Exact degree-seven multiset witnesses, not saturation inference.
"""
from pathlib import Path
from itertools import combinations_with_replacement
from time import monotonic
import json

start=monotonic();cap=5
source=json.loads(Path('stage34_combined_results.json').read_text())
assert source['completion']=='COMPLETE'
rows=[];survivors=[]
for record in source['survivors']:
    m=record['M'];b=record['B'];s=sum(b)%m
    for missing in record['missing_7B']:
        if monotonic()-start>=cap:raise TimeoutError('Seventh extensions incomplete')
        x=(missing-s)%m
        row={'M':m,'B':b,'missing_7B':missing,'seventh_point':x}
        if x in b:
            row['outcome']='REPEATED POINT';rows.append(row);continue
        a=sorted(b+[x]);target=sum(a)%m
        rival=None
        for multiset in combinations_with_replacement(a,7):
            if list(multiset)!=a and sum(multiset)%m==target:
                rival=[multiset.count(v) for v in a];break
        row['A']=a;row['rival_counts']=rival
        if rival is None:
            row['outcome']='UNCERTIFIED SURVIVOR';survivors.append(row)
        else:
            row['outcome']='EXPLICIT SEVEN-TERM RIVAL'
            assert sum(rival)==7 and rival!=[1]*7
            assert sum((c-1)*v for c,v in zip(rival,a))%m==0
        rows.append(row)
out={'completion':'COMPLETE','cap_seconds':cap,'elapsed_seconds':monotonic()-start,
     'six_point_survivors':len(source['survivors']),'extensions':rows,'survivors':survivors}
Path('stage34_seventh_extension_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'completion':'COMPLETE','six_survivors':len(source['survivors']),
                  'extensions':len(rows),'seven_survivors':len(survivors),
                  'seconds':out['elapsed_seconds']}))
