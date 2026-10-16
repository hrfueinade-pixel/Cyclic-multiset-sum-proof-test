"""Complete small-order two-path necessary family, 30-second cap.

Unit scaling normalizes first start x to gcd(x,n), a proper divisor n.
The other start ranges over all residues, gcd(n,x,y)=1. No closure
assumption, MC or historical search kernel. Saved witnesses are actual
eight-term rivals on the constructed set, with at least one point absent.
"""
from pathlib import Path
from math import gcd
from time import monotonic
import json

start=monotonic(); cap=30
records=[]; survivors=[]; seen=set(); stats=[]
def rival(n,a):
    target=sum(a)%n; mask=(1<<n)-1
    for omit in range(8):
        terms=[(i,x) for i,x in enumerate(a) if i!=omit]
        levels=[1]
        for k in range(8):
            bits=levels[-1]; nxt=0
            for _,x in terms:
                nxt|=((bits<<x)|(bits>>(n-x)))&mask
            levels.append(nxt)
        if not (levels[8]>>target)&1: continue
        counts=[0]*8; residue=target
        for k in range(8,0,-1):
            for i,x in terms:
                prev=(residue-x)%n
                if (levels[k-1]>>prev)&1:
                    counts[i]+=1; residue=prev; break
            else: raise AssertionError('Backtracking failed')
        assert residue==0 and sum(counts)==8 and counts[omit]==0
        assert sum(c*x for c,x in zip(counts,a))%n==target
        return counts
    return None

complete=True
for n in range(185,248,2):
    row={'n':n,'parameters':0,'distinct_sidon_sets':0,'rivals':0,'survivors':0}
    for length in (1,2,3,4):
        other=8-length
        for x in range(1,n):
            if n%x: continue
            for y in range(n):
                if monotonic()-start>=cap:
                    complete=False; break
                if gcd(n,x,y)!=1: continue
                row['parameters']+=1
                a=sorted({(x*2**i)%n for i in range(length)}|
                         {(y*2**j)%n for j in range(other)})
                if len(a)!=8: continue
                diff={ (u-v)%n for u in a for v in a if u!=v }
                if len(diff)!=56: continue
                key=(n,tuple(a))
                if key in seen: continue
                seen.add(key); row['distinct_sidon_sets']+=1
                entry={'n':n,'lengths':[length,other],'starts':[x,y],'A':a}
                counts=rival(n,a)
                if counts is None:
                    row['survivors']+=1; survivors.append(entry)
                else:
                    row['rivals']+=1
                    records.append([n,length,x,y,''.join(map(str,counts))])
            if not complete: break
        if not complete: break
    stats.append(row)
    if not complete: break
out={'completion':'COMPLETE' if complete else 'TIMEOUT/incomplete',
     'cap_seconds':cap,'elapsed_seconds':monotonic()-start,
     'coverage':'All odd185..247; normalized starts; four unordered path lengths',
     'exclusion_format':['n','first_path_length','first_start','second_start',
                         'rival_counts_in_sorted_A_order'],
     'statistics':stats,'exclusions':records,'survivors':survivors}
Path('stage29_two_path_results.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
print(json.dumps({'completion':out['completion'],'elapsed_seconds':out['elapsed_seconds'],
                  'parameters':sum(r['parameters'] for r in stats),
                  'sidon_sets':len(seen),'excluded':len(records),'survivors':len(survivors)}))
