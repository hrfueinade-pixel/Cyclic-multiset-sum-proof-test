"""Discovery of odd counterexamples via primitive five-block plus triple.

Coverage: every valid generated odd eight-set has a primitive5subset,
because <=3 prime factors need <=4 selected generators including0.
Unit-pair or unitless divisor roots cover that subset. Necessary q=5,
6,7,8 constraints precede pair-Sidon and exact remaining count checks.
180s global cap; completed orders only give exclusion claims.
"""
from pathlib import Path
from itertools import combinations_with_replacement
from math import gcd
from time import monotonic
import json,gzip

start=monotonic();cap=180;reports=[];survivors=[];identities=[];active=None
def prime_count(n):
    return sum(n%p==0 and all(p%d for d in range(2,int(p**0.5)+1)) for p in range(2,n+1))
def run(n):
    global active
    full=2**n-1;seen=set();nodes=[0]*6
    counts={'primitive_B':0,'C_shapes':0,'bases_6_7_8':0,'sidon_eight':0,
            'rivals':0,'valid_survivors':0}
    active={'N':n,'completion':'RUNNING','counts':counts,'prefixes':nodes}
    def tick():
        if monotonic()-start>=cap:raise TimeoutError()
    def shift(bits,x):
        x%=n;return ((bits<<x)|(bits>>(n-x)))&full
    def elements(bits):
        while bits:
            p=bits & -bits;yield p.bit_length()-1;bits^=p
    def sumsets(points):
        levels=[1]
        for k in range(8):
            out=0
            for x in points:out|=shift(levels[-1],x)
            levels.append(out)
        return levels
    def realize(points,levels,degree,target):
        mult=[0]*len(points)
        for k in range(degree,0,-1):
            for i,x in enumerate(points):
                r=(target-x)%n
                if (levels[k-1]>>r)&1:mult[i]+=1;target=r;break
            else:raise AssertionError('No representation')
        assert target==0;return mult
    def inspect(b,levels):
        b=sorted(b)
        if gcd(n,*b)!=1:return
        key=tuple(b)
        if key in seen:return
        seen.add(key);counts['primitive_B']+=1
        sb=sum(b)%n
        g={ (sb-r)%n for r in range(n) if not(levels[5]>>r)&1 }
        uvals=sorted(a for a in g if (-a)%n in g)
        ubits=sum(1<<a for a in uvals);negative=sum(1<<((-a)%n) for a in g)
        half=sum(1<<x for x in range(n) if 2*x%n in g)
        inv2=pow(2,-1,n)
        for u in uvals:
            tick()
            vm=ubits & shift(ubits,u) & shift(negative,-u) & shift(negative,2*u) & shift(half,inv2*u)
            vm &= full ^ ((1<<(u+1))-1)
            for v in elements(vm):
                if len({d%n for d in (u,v,v-u,-u,-v,u-v)})!=6:continue
                counts['C_shapes']+=1;d=[0,u,v];sd=(u+v)%n
                base1=full
                for pair in combinations_with_replacement(d,2):
                    base1 &= shift(full ^ levels[6],-sb-sd+sum(pair))
                    if not base1:break
                if not base1:continue
                base2=full
                for point in d:base2 &= shift(full ^ levels[7],-sb-sd+point)
                base3=shift(full ^ levels[8],-sb-sd)
                ds=None
                for base in elements(base1):
                    if base+v>=n:continue
                    if not(base2>>(2*base%n))&1 or not(base3>>(3*base%n))&1:continue
                    c=[base+a for a in d];a=sorted(b+c)
                    if len(set(a))!=8:continue
                    counts['bases_6_7_8']+=1
                    if len({(x-y)%n for x in a for y in a if x!=y})!=56:continue
                    counts['sidon_eight']+=1
                    if ds is None:ds=sumsets(d)
                    rival=None
                    for q in (4,3,2,1,0):
                        target=(sb+sd+(q-5)*base)%n
                        for r in elements(ds[8-q]):
                            if (levels[q]>>((target-r)%n))&1:
                                cb=realize(b,levels,q,(target-r)%n)
                                cc=realize(d,ds,8-q,r)
                                vector=[0]*8
                                for x,k in zip(b,cb):vector[a.index(x)]+=k
                                for x,k in zip(c,cc):vector[a.index(x)]+=k
                                assert sum(vector)==8 and vector!=[1]*8
                                assert sum((k-1)*x for k,x in zip(vector,a))%n==0
                                rival=vector;break
                        if rival is not None:break
                    if rival is None:
                        counts['valid_survivors']+=1;survivors.append({'N':n,'A':a,'B':b,'C':c})
                    else:
                        counts['rivals']+=1;identities.append([n,a,rival])
    def visit(p,levels,delta,after,g):
        tick();nodes[len(p)]+=1
        if levels[6]==full:return
        if len(p)==5:inspect(p,levels);return
        degree=len(p)+1;target=sum(p)
        for x in range(after,n):
            if x==g:continue
            if g!=1 and any(gcd(x-a,n)==1 for a in p):continue
            dif=[];bad=False
            for a in p:
                v=(x-a)%n;w=(a-x)%n
                if v==w or v in delta or w in delta or v in dif or w in dif:
                    bad=True;break
                dif.extend((v,w))
            if bad:continue
            if any((levels[degree-q]>>((target+(1-q)*x)%n))&1 for q in range(degree+1) if q!=1):continue
            new=[1]
            for k in range(1,9):new.append(levels[k]|shift(new[k-1],x))
            visit(p+[x],new,delta|set(dif),x+1,g)
    roots=[1] if prime_count(n)<=2 else [g for g in range(1,n) if n%g==0]
    active['roots']=roots
    for g in roots:
        levels=[sum(1<<r for r in {j*g%n for j in range(k+1)}) for k in range(9)]
        visit([0,g],levels,{g,n-g},1,g)
    active['completion']='COMPLETE';return active

complete=True
for n in range(189,248,2):
    try:
        r=run(n);reports.append(r)
        print(json.dumps({'N':n,'counts':r['counts'],'seconds':monotonic()-start}),flush=True)
    except TimeoutError:
        complete=False;break
out={'completion':'COMPLETE' if complete else 'TIMEOUT/incomplete',
     'cap_seconds':cap,'elapsed_seconds':monotonic()-start,
     'completed_orders':[r['N'] for r in reports],'reports':reports,
     'partial_order':active if not complete else None,'survivors':survivors,
     'identity_count':len(identities),'identity_file':'stage33_rivals.json.gz'}
Path('stage33_odd_five_three_results.json').write_text(json.dumps(out,indent=2)+'\n')
Path('stage33_rivals.json.gz').write_bytes(gzip.compress(json.dumps(identities,separators=(',',':')).encode(),mtime=0))
print(json.dumps({k:v for k,v in out.items() if k not in ('reports','partial_order','survivors')}),flush=True)
