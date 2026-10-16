"""Small quotient/lift discovery certificate for antipodal seven-sets.

All valid five-point cyclic sets at orders16..30, then all antipodal
six-lifts and seven-lifts. 30s cap. Antipodes are ALLOWED in this search;
do not impose the non-antipodal difference uniqueness filter.
"""
from pathlib import Path
from math import gcd
from itertools import product
from time import monotonic
import json

start=monotonic();cap=30;raw5=[];classes5=set();classes6=set();rows5=[]
six_records=[];seven_records=[];survivors=[]
def tick():
    if monotonic()-start>=cap:raise TimeoutError('Small lift family incomplete')
def canonical(m,a):
    return min(tuple(sorted(u*(x-z)%m for x in a))
               for u in range(1,m) if gcd(u,m)==1 for z in a)
def rival(m,a):
    tick();degree=len(a);target=sum(a)%m;full=2**m-1
    for omit in range(degree):
        available=[(i,x) for i,x in enumerate(a) if i!=omit]
        levels=[1]
        for k in range(degree):
            b=0
            for _,x in available:b|=((levels[-1]<<x)|(levels[-1]>>(m-x)))&full
            levels.append(b)
        if not(levels[degree]>>target)&1:continue
        counts=[0]*degree;r=target
        for k in range(degree,0,-1):
            for i,x in available:
                before=(r-x)%m
                if(levels[k-1]>>before)&1:counts[i]+=1;r=before;break
            else:raise AssertionError('Unreachable target')
        assert r==0 and sum(counts)==degree and counts!=[1]*degree
        assert sum((c-1)*x for c,x in zip(counts,a))%m==0
        return counts
    return None
def enumerate5(m):
    full=2**m-1;seen=set();nodes=[0]*6
    def shift(b,x):return ((b<<x)|(b>>(m-x)))&full
    def visit(p,levels,after,g):
        tick();nodes[len(p)]+=1
        if len(p)==5:
            a=tuple(sorted(p))
            if a not in seen:
                seen.add(a);assert gcd(m,*a)==1
                raw5.append({'N':m,'A':list(a)});classes5.add((m,canonical(m,a)))
            return
        degree=len(p)+1;target=sum(p)
        for x in range(after,m):
            if x==g:continue
            if g!=1 and any(gcd(x-z,m)==1 for z in p):continue
            if any((levels[degree-q]>>((target+(1-q)*x)%m))&1 for q in range(degree+1) if q!=1):continue
            new=[1]
            for k in range(1,6):new.append(levels[k]|shift(new[k-1],x))
            visit(p+[x],new,x+1,g)
    # Only30 has three prime factors in this range. Others have a unit pair.
    roots=[1] if m!=30 else [g for g in range(1,m) if m%g==0]
    for g in roots:
        levels=[sum(1<<r for r in {j*g%m for j in range(k+1)}) for k in range(6)]
        visit([0,g],levels,1,g)
    return {'N':m,'roots':roots,'prefixes':nodes,'valid_normalized':len(seen)}
for m in range(16,31):rows5.append(enumerate5(m))
def lifts(m,q):
    for duplicated in range(len(q)):
        others=[i for i in range(len(q)) if i!=duplicated]
        for bits in product((0,1),repeat=len(others)):
            a=[q[duplicated],q[duplicated]+m]
            a += [q[i]+bit*m for i,bit in zip(others,bits)]
            yield sorted(a)
for m,q in sorted(classes5):
    for a in lifts(m,q):
        counts=rival(2*m,a)
        six_records.append({'N':2*m,'A':a,'rival':counts})
        if counts is None:classes6.add((2*m,canonical(2*m,a)))
for m,q in sorted(classes6):
    for a in lifts(m,q):
        counts=rival(2*m,a)
        seven_records.append({'N':2*m,'A':a,'rival':counts})
        if counts is None:survivors.append({'N':2*m,'A':a})
out={'completion':'COMPLETE','cap_seconds':cap,'elapsed_seconds':monotonic()-start,
     'five_point_coverage':rows5,'valid_five_normalized':raw5,
     'five_affine_classes':[{'N':m,'A':list(q)} for m,q in sorted(classes5)],
     'six_lifts':six_records,'six_affine_classes':[{'N':m,'A':list(q)} for m,q in sorted(classes6)],
     'seven_lifts':seven_records,'seven_survivors':survivors}
Path('stage35_antipodal_seven_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'completion':'COMPLETE','seconds':out['elapsed_seconds'],
                  'five_normalized':len(raw5),'five_classes':len(classes5),
                  'six_lifts':len(six_records),'six_classes':len(classes6),
                  'seven_lifts':len(seven_records),'seven_survivors':len(survivors)}))
