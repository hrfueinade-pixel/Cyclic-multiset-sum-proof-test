"""Discovery of the full even3+5 family below248; global90s cap.

0,1 roots cover unit differences; all other divisor roots retain only
unitless differences. No primitivity assumption on the odd five-block.
All C pair sums must lie outside7B, after target translation. Inverting
the three pair sums enumerates all candidate even triples. Exact parity
counts1,3,5,7 decide eight-term validity. Partial survivors are preserved.
"""
from itertools import combinations,combinations_with_replacement
from math import gcd
from pathlib import Path
from time import monotonic
import json

start=monotonic();cap=90;reports=[];survivors=[];current=None;active=None
def run(m):
    global active
    full=(1<<m)-1; seen=set(); b_nodes=[0]*6
    counts={'blocks':0,'pair_sum_triples':0,'even_triples':0,'sidon_eight':0,
            'rival_5odd':0,'rival_3odd':0,'rival_1odd':0}
    active={'M':m,'completion':'RUNNING','B_prefix_counts':b_nodes,'counts':counts}
    def deadline():
        if monotonic()-start>=cap:raise TimeoutError()
    def rotate(bits,x):
        return ((bits<<x)|(bits>>(m-x)))&full
    def member(bits,x):return (bits>>(x%m))&1
    def check_block(b,levels):
        key=tuple(sorted(b))
        if key in seen:return
        seen.add(key);counts['blocks']+=1
        s=sum(b)%m
        f=sorted((r-s+1)%m for r in range(m) if not member(levels[7],r))
        odd=[2*x+1 for x in b]; n=2*m
        diffs={(x-y)%n for x in odd for y in odd if x!=y}
        assert len(diffs)==20
        for r1,r2,r3 in combinations(f,3):
            deadline();counts['pair_sum_triples']+=1
            rhs=(r2+r3-r1)%m
            if m%2:
                roots=[rhs*pow(2,-1,m)%m]
            elif rhs%2:continue
            else:roots=[rhs//2,rhs//2+m//2]
            for x in roots:
                c=sorted([x,(r3-x)%m,(r2-x)%m])
                if len(set(c))!=3:continue
                counts['even_triples']+=1
                even=[2*a for a in c]
                newdiff=list(diffs);bad=False
                for i,a in enumerate(even):
                    for z in odd+even[:i]:
                        v=(a-z)%n;w=(z-a)%n
                        if v==w or v in newdiff or w in newdiff:
                            bad=True;break
                        newdiff.extend((v,w))
                    if bad:break
                if bad:continue
                assert len(newdiff)==56
                counts['sidon_eight']+=1
                sc=sum(c)%m; target=(s+sc)%m
                c3=[sum(p)%m for p in combinations_with_replacement(c,3)]
                if c3.count(sc)!=1 or any(t!=sc and member(levels[5],target-t) for t in c3):
                    counts['rival_5odd']+=1;continue
                if any(member(levels[3],target+1-sum(p))
                       for p in combinations_with_replacement(c,5)):
                    counts['rival_3odd']+=1;continue
                if any(member(levels[1],target+2-sum(p))
                       for p in combinations_with_replacement(c,7)):
                    counts['rival_1odd']+=1;continue
                # q=7 excluded by all three pair sums being in F.
                assert all(not member(levels[7],target-1-a) for a in c)
                survivors.append({'N':n,'B':sorted(b),'C':c,'A':sorted(odd+even),
                                  'difference_gcd':gcd(n,*(a-(odd+even)[0] for a in odd+even))})
    def visit(p,g,levels,difference,after):
        deadline();k=len(p);b_nodes[k]+=1
        if levels[7]==full:return
        if k==5:
            check_block(p,levels);return
        t=sum(p)%m;degree=k+1
        for x in range(after,m):
            if x==g:continue
            if g!=1 and any(gcd(x-a,m)==1 for a in p):continue
            ds=[];bad=False
            for a in p:
                v=(x-a)%m;w=(a-x)%m
                if v==w or v in difference or w in difference or v in ds or w in ds:
                    bad=True;break
                ds.extend((v,w))
            if bad:continue
            if any(member(levels[degree-q],t+(1-q)*x) for q in range(degree+1) if q!=1):continue
            nxt=[1]
            for j in range(1,8):nxt.append(levels[j]|rotate(nxt[j-1],x))
            visit(p+[x],g,nxt,difference|set(ds),x+1)
    roots=[g for g in range(1,m) if m%g==0 and 2*g!=m]
    active['roots']=roots
    for g in roots:
        levels=[]
        for k in range(8):
            bits=0
            for j in range(k+1):bits|=1<<(j*g%m)
            levels.append(bits)
        visit([0,g],g,levels,{g,m-g},1)
    active['completion']='COMPLETE'
    return active

complete=True
for m in range(123,93,-1):
    current=m
    try:
        r=run(m);reports.append(r)
        print(json.dumps({'M':m,'counts':r['counts'],'seconds':monotonic()-start}),flush=True)
    except TimeoutError:
        complete=False;break
out={'completion':'COMPLETE' if complete else 'TIMEOUT/incomplete',
     'cap_seconds':cap,'elapsed_seconds':monotonic()-start,
     'completed_orders':[r['M'] for r in reports],
     'partial_order':active if not complete else None,
     'reports':reports,'survivors':survivors,
     'scope':'All odd five-blocks and compatible even triples;even3+5 only'}
Path('stage31_even_three_five_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('reports','partial_order','survivors')}),flush=True)
