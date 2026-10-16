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

start=monotonic();cap=180;reports=[];survivors=[];current=None;active=None
def run(m):
    global active
    full=(1<<m)-1; seen=set(); b_nodes=[0]*6
    counts={'blocks':0,'proper_saturated':0,'shapes_checked':0,'shapes_5odd_surviving':0,
            'even_triples':0,'sidon_eight':0,'rival_3odd':0,'rival_1odd':0}
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
        step=gcd(m,*b)
        if step>1:
            subgroup=sum(1<<r for r in range(0,m,step))
            if levels[5]==subgroup:
                # A competing three-term C multiset in M/J can be
                # corrected in J by five B terms. Index<=4 follows
                # from the elementary valid-five-point bound |J|>=30.
                assert m//step>=30 and step<=4
                counts['proper_saturated']+=1;return
        s=sum(b)%m
        f={(r-s+1)%m for r in range(m) if not member(levels[7],r)}
        allowed={(s-r)%m for r in range(m) if not member(levels[5],r)}
        unit_shape=sorted(a for a in allowed if (-a)%m in allowed)
        ubits=sum(1<<a for a in unit_shape)
        negative=sum(1<<((-a)%m) for a in allowed)
        pre2=sum(1<<a for a in range(m) if 2*a%m in allowed)
        pre2plus=sum(1<<a for a in range(m) if (2*a-1)%m in allowed)
        fbits=sum(1<<a for a in f)
        odd=[2*x+1 for x in b]; n=2*m
        diffs={(x-y)%n for x in odd for y in odd if x!=y}
        assert len(diffs)==20
        for index,u in enumerate(unit_shape):
            deadline();counts['shapes_checked']+=len(unit_shape)-index-1
            if m%2:
                double_condition=rotate(pre2,(pow(2,-1,m)*u)%m)
            else:
                double_condition=rotate(pre2 if u%2==0 else pre2plus,u//2)
            candidates=ubits & rotate(ubits,u) & rotate(negative,(-u)%m)
            candidates &= rotate(negative,2*u%m) & double_condition
            candidates &= full ^ ((1<<(u+1))-1)
            while candidates:
                low=candidates & -candidates;v=low.bit_length()-1;candidates^=low
                if len({a%m for a in (u,v,v-u,-u,-v,u-v)})!=6:continue
                counts['shapes_5odd_surviving']+=1
                bases=rotate(fbits,(-u-v)%m) & rotate(fbits,(-u)%m) & rotate(fbits,(-v)%m)
                while bases:
                    low=bases & -bases;rhs=low.bit_length()-1;bases^=low
                    if m%2:
                        roots=[rhs*pow(2,-1,m)%m]
                    elif rhs%2:continue
                    else:roots=[rhs//2,rhs//2+m//2]
                    for x in roots:
                        if x+v>=m:continue
                        c=[x,x+u,x+v]
                        check_even(c,b,levels,s,odd,diffs,n,m,member,counts)
    def check_even(c,b,levels,s,odd,diffs,n,m,member,counts):
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
                if bad:return
                assert len(newdiff)==56
                counts['sidon_eight']+=1
                sc=sum(c)%m; target=(s+sc)%m
                c3=[sum(p)%m for p in combinations_with_replacement(c,3)]
                assert c3.count(sc)==1 and not any(t!=sc and member(levels[5],target-t) for t in c3)
                if any(member(levels[3],target+1-sum(p))
                       for p in combinations_with_replacement(c,5)):
                    counts['rival_3odd']+=1;return
                if any(member(levels[1],target+2-sum(p))
                       for p in combinations_with_replacement(c,7)):
                    counts['rival_1odd']+=1;return
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
