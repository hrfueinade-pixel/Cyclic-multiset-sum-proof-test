"""New odd exclusion audit: explicit coin counts and scalar cubic shapes.

No discovery imports. Affine canonical unit-pair blocks and all unitless
divisor roots. Only selected completed discovery orders are compared.
Opposing triple deviations derive from every non-original multiset.
"""
from pathlib import Path
from itertools import combinations_with_replacement
from math import gcd
from time import monotonic
import argparse,json,gzip

parser=argparse.ArgumentParser()
parser.add_argument('--lower',type=int,default=189)
parser.add_argument('--upper',type=int,required=True)
parser.add_argument('--seconds',type=float,default=600)
args=parser.parse_args()
assert 189<=args.lower<=args.upper<248 and args.lower%2==args.upper%2==1
start=monotonic();reports=[];shapes=[];survivors=[];active=None

def run(n):
    global active
    full=(1<<n)-1;seen=set();unit={d:pow(d,-1,n) for d in range(1,n) if gcd(d,n)==1}
    nodes=[0]*6;counts={'primitive_B':0,'eight_sum_saturated':0,'C_shapes':0,
                       'bases_6_7_8':0,'sidon_eight':0,'rivals':0,'valid_survivors':0}
    active={'N':n,'completion':'RUNNING','counts':counts,'prefixes':nodes}
    def tick():
        if monotonic()-start>=args.seconds:raise TimeoutError()
    def shift(bits,x):
        x%=n;return ((bits<<x)|(bits>>(n-x)))&full
    def members(bits):
        while bits:
            one=bits & -bits;yield one.bit_length()-1;bits^=one
    def all_sums(points,degree):
        return {sum(t)%n for t in combinations_with_replacement(points,degree)}
    def inspect(points,levels):
        b=tuple(sorted(points))
        if gcd(n,*b)!=1:return
        images=[]
        for p in b:
            for q in b:
                inv=unit.get((q-p)%n)
                if inv is not None:images.append(tuple(sorted(inv*(x-p)%n for x in b)))
        if images and b!=min(images):return
        if b in seen:return
        seen.add(b);counts['primitive_B']+=1
        # All eight terms from B give a rival for every possible triple.
        if levels[8]==full:counts['eight_sum_saturated']+=1;return
        s=sum(b)%n
        g={(s-r)%n for r in range(n) if not(levels[5]>>r)&1}
        edges=sum(1<<d for d in g if (-d)%n in g)
        q8missing={r for r in range(n) if not(levels[8]>>r)&1}
        q7missing={r for r in range(n) if not(levels[7]>>r)&1}
        for u in members(edges):
            tick()
            vmask=edges & shift(edges,u) & (full ^ ((1<<(u+1))-1))
            for v in members(vmask):
                d=(0,u,v);sd=u+v
                if len({(x-y)%n for x in d for y in d if x!=y})!=6:continue
                if any((3*x-sd)%n not in g for x in d):continue
                assert all((sum(t)-sd)%n in g for t in combinations_with_replacement(d,3) if t!=d)
                counts['C_shapes']+=1
                possible=[]
                for c in range(n-v):
                    if (s+sd+3*c)%n not in q8missing:continue
                    if any((s+sd+2*c-x)%n not in q7missing for x in d):continue
                    if any((levels[6]>>((s+sd+c-sum(pair))%n))&1
                           for pair in combinations_with_replacement(d,2)):continue
                    cpoints=tuple(c+x for x in d);a=tuple(sorted(b+cpoints))
                    if len(set(a))!=8:continue
                    counts['bases_6_7_8']+=1;possible.append(c)
                    if len({(x-y)%n for x in a for y in a if x!=y})!=56:continue
                    counts['sidon_eight']+=1
                    # Full independent 6435-multiset certification only
                    # for actual candidate sets surviving the reductions.
                    target=sum(a)%n
                    rival=next((t for t in combinations_with_replacement(a,8)
                                if t!=a and sum(t)%n==target),None)
                    if rival is None:
                        counts['valid_survivors']+=1;survivors.append({'N':n,'A':list(a)})
                    else:counts['rivals']+=1
                if possible:shapes.append([n,list(b),list(d),possible])
    def visit(p,levels,after,unitless):
        tick();nodes[len(p)]+=1
        if levels[6]==full:return
        if len(p)==5:inspect(p,levels);return
        degree=len(p)+1;total=sum(p)
        for x in range(after,n):
            if x in p:continue
            if unitless and any(gcd(x-z,n)==1 for z in p):continue
            a=p+[x]
            if len({(z-w)%n for z in a for w in a if z!=w})!=degree*(degree-1):continue
            if any((levels[degree-q]>>((total+(1-q)*x)%n))&1
                   for q in range(degree+1) if q!=1):continue
            updated=[]
            for k in range(9):
                out=0
                for copies in range(k+1):out|=shift(levels[k-copies],copies*x)
                updated.append(out)
            visit(a,updated,x+1,unitless)
    # Include every unitless divisor root even when the two-prime lemma
    # could rule it out. This is a different coverage partition.
    roots=[d for d in range(1,n) if n%d==0]
    active['roots']=roots
    for first in roots:
        levels=[sum(1<<r for r in {copies*first%n for copies in range(k+1)}) for k in range(9)]
        visit([0,first],levels,1,first!=1)
    active['completion']='COMPLETE';return active

complete=True
for n in range(args.lower,args.upper+1,2):
    try:
        r=run(n);reports.append(r)
        print(json.dumps({'N':n,'counts':r['counts'],'seconds':monotonic()-start}),flush=True)
    except TimeoutError:complete=False;break
comparison='Pending discovery checkpoint; independently completed orders retained'
if Path('stage36_odd_canonical_results.json').exists():
    source=json.loads(Path('stage36_odd_canonical_results.json').read_text())
    expected={r['N']:r for r in source['reports']}
    for r in reports:
        if r['N'] not in expected:continue
        assert r['counts']['primitive_B']==expected[r['N']]['counts']['primitive_B']
        assert r['counts']['bases_6_7_8']==expected[r['N']]['counts']['bases_6_7_8']
        assert r['counts']['valid_survivors']==expected[r['N']]['counts']['valid_survivors']
    comparison='Compared available completed discovery orders; final cross-check required'
out={'completion':'COMPLETE' if complete else 'TIMEOUT/incomplete','cap_seconds':args.seconds,
     'elapsed_seconds':monotonic()-start,'completed_orders':[r['N'] for r in reports],
     'reports':reports,'partial_order':active if not complete else None,
     'survivors':survivors,'imports_producer':False,'symbolic_base_survivors':shapes,
     'comparison':comparison}
Path('stage37_odd_independent_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('reports','partial_order','survivors','symbolic_base_survivors')}),flush=True)
