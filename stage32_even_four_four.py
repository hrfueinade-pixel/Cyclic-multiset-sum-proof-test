"""Discovery of even4+4 below248, 180s cap; no primitive block assumption.

All B4 normalized by a unit pair or unitless divisor root. For C=c+D,
four/four uniqueness forces every repeated quartic deviation of D into
G=sum B-complement(4B). Build D from the triple restriction, then exact
linear residue preimages for its fourth point. Test all even odd-counts.
"""
from itertools import combinations_with_replacement
from pathlib import Path
from math import gcd
from time import monotonic
import json
import argparse

parser=argparse.ArgumentParser()
parser.add_argument('--upper',type=int,default=123)
parser.add_argument('--lower',type=int,default=94)
parser.add_argument('--seconds',type=float,default=180)
parser.add_argument('--output',default='stage32_even_four_four_results.json')
args=parser.parse_args()
assert 94<=args.lower<=args.upper<=123
start=monotonic();cap=args.seconds;reports=[];survivors=[];symbolic=[];active=None
def run(m):
    global active
    full=2**m-1;seen=set();nodes=[0]*5
    counts={'B_blocks':0,'proper_saturated':0,'C_triples':0,'C_shapes':0,
            'bases_6_8':0,'sidon_eight':0,'rival_2':0,'rival_0':0}
    active={'M':m,'completion':'RUNNING','counts':counts,'prefixes':nodes}
    def tick():
        if monotonic()-start>cap:raise TimeoutError()
    def shift(bits,x):
        x%=m;return ((bits<<x)|(bits>>(m-x)))&full
    def elements(bits):
        while bits:
            one=bits & -bits;yield one.bit_length()-1;bits^=one
    def sums(points,degree):
        levels=[1]
        for k in range(degree):
            bits=0
            for p in points:bits|=shift(levels[-1],p)
            levels.append(bits)
        return levels
    def inspect(b,levels):
        key=tuple(sorted(b))
        if key in seen:return
        seen.add(key);counts['B_blocks']+=1
        step=gcd(m,*b)
        if step>1 and levels[4]==sum(1<<r for r in range(0,m,step)):
            assert m//step>=14 and step<=8
            counts['proper_saturated']+=1;return
        sb=sum(b)%m
        g={ (sb-r)%m for r in range(m) if not (levels[4]>>r)&1 }
        gbits=sum(1<<a for a in g)
        negative=sum(1<<((-a)%m) for a in g)
        uvals=sorted(a for a in g if (-a)%m in g)
        ubits=sum(1<<a for a in uvals)
        seeds={}
        for coefficient in (2,3):
            divisor=gcd(coefficient,m)
            seeds[coefficient]=[sum(1<<x for x in range(m)
                                    if (coefficient*x-r)%m in g) for r in range(divisor)]
        def preimage(coefficient,offset):
            offset%=m;divisor=gcd(coefficient,m);q,r=divmod(offset,divisor)
            translation=q*pow(coefficient//divisor,-1,m//divisor)
            return shift(seeds[coefficient][r],translation)
        for u in uvals:
            tick()
            vb=ubits & shift(ubits,u) & shift(negative,-u) & shift(negative,2*u)
            vb &= preimage(2,u)
            vb &= full ^ ((1<<(u+1))-1)
            for v in elements(vb):
                if len({d%m for d in (u,v,v-u,-u,-v,u-v)})!=6:continue
                counts['C_triples']+=1
                triple=[0,u,v];ts=u+v
                fourth=full ^ ((1<<(v+1))-1)
                for p in combinations_with_replacement(triple,4):
                    fourth &= shift(negative,sum(p)-ts)
                    if not fourth:break
                if not fourth:continue
                for p in combinations_with_replacement(triple,2):
                    fourth &= shift(gbits,ts-sum(p))
                    if not fourth:break
                if not fourth:continue
                for p in triple:
                    fourth &= preimage(2,ts-p)
                    if not fourth:break
                fourth &= preimage(3,ts)
                for w in elements(fourth):
                    d=triple+[w];sd=sum(d)%m
                    if len({(a-z)%m for a in d for z in d if a!=z})!=12:continue
                    # Direct check of the complete four/four condition.
                    for p in combinations_with_replacement(d,4):
                        if tuple(d)!=p:assert (sum(p)-sd)%m in g
                    counts['C_shapes']+=1
                    dlevels=sums(d,8)
                    if dlevels[8]==full:continue
                    convolution=0
                    for t in elements(dlevels[6]):convolution |= shift(levels[2],t)
                    if convolution==full:continue
                    allowed2=full
                    for t in elements(dlevels[2]):
                        allowed2 &= shift(full ^ levels[6],-sb-sd+1+t)
                    allowed4=shift(full ^ levels[8],-sb-sd+2)
                    possible=[]
                    for c0 in range(m-w):
                        tick()
                        if not (allowed2>>(2*c0%m))&1 or not (allowed4>>(4*c0%m))&1:continue
                        counts['bases_6_8']+=1
                        c=[c0+a for a in d]
                        a=sorted([2*z+1 for z in b]+[2*z for z in c]);n=2*m
                        if len({(x-y)%n for x in a for y in a if x!=y})!=56:continue
                        counts['sidon_eight']+=1
                        if (convolution>>((sb+sd+1-2*c0)%m))&1:
                            counts['rival_2']+=1;continue
                        if (dlevels[8]>>((sb+sd+2-4*c0)%m))&1:
                            counts['rival_0']+=1;continue
                        possible.append(c)
                        survivors.append({'N':n,'B':sorted(b),'C':c,'A':a})
                    if possible:symbolic.append({'M':m,'B':sorted(b),'C_shape':d,'bases':possible})
    def visit(p,levels,delta,after,g):
        tick();nodes[len(p)]+=1
        if levels[8]==full:return
        if len(p)==4:inspect(p,levels);return
        degree=len(p)+1;target=sum(p)
        for x in range(after,m):
            if x==g:continue
            if g!=1 and any(gcd(x-a,m)==1 for a in p):continue
            ds=[];bad=False
            for a in p:
                v=(x-a)%m;w=(a-x)%m
                if v==w or v in delta or w in delta or v in ds or w in ds:
                    bad=True;break
                ds.extend((v,w))
            if bad:continue
            if any((levels[degree-q]>>((target+(1-q)*x)%m))&1 for q in range(degree+1) if q!=1):continue
            nxt=[1]
            for k in range(1,9):nxt.append(levels[k]|shift(nxt[k-1],x))
            visit(p+[x],nxt,delta|set(ds),x+1,g)
    roots=[g for g in range(1,m) if m%g==0 and 2*g!=m]
    active['roots']=roots
    for g in roots:
        levels=[sum(1<<r for r in {j*g%m for j in range(k+1)}) for k in range(9)]
        visit([0,g],levels,{g,m-g},1,g)
    active['completion']='COMPLETE';return active

complete=True
for m in range(args.upper,args.lower-1,-1):
    try:
        r=run(m);reports.append(r)
        print(json.dumps({'M':m,'counts':r['counts'],'seconds':monotonic()-start}),flush=True)
    except TimeoutError:
        complete=False;break
out={'completion':'COMPLETE' if complete else 'TIMEOUT/incomplete',
     'cap_seconds':cap,'elapsed_seconds':monotonic()-start,
     'requested_orders':list(range(args.upper,args.lower-1,-1)),
     'completed_orders':[r['M'] for r in reports],
     'partial_order':active if not complete else None,'reports':reports,
     'survivors':survivors,'symbolic_survivors':symbolic,
     'scope':'Even4+4 only; all normalized valid non-antipodal four-blocks'}
Path(args.output).write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('reports','partial_order','symbolic_survivors','survivors')}),flush=True)
