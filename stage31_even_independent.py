"""Independent five-block/triple necessary-family check, global240s cap.

No producer imports. Explicit coin-count sumset union, graph-triangle
enumeration of triple differences, scalar cube deviations, and direct
translation loop (no doubled-base intersection or modular division).
Every symbolic five-odd survivor shape is preserved.
"""
from pathlib import Path
from itertools import combinations_with_replacement
from math import gcd
from time import monotonic
import json

start=monotonic();cap=240;reports=[];shape_records=[];survivors=[];active=None
def run(m):
    global active
    full=2**m-1;blocks=set();count={'blocks':0,'proper_saturated':0,
                                  'shapes':0,'even_triples':0};prefixes=[0]*6
    active={'M':m,'completion':'RUNNING','counts':count,'prefixes':prefixes}
    def tick():
        if monotonic()-start>cap:raise TimeoutError()
    def shift(bits,x):
        x%=m;return ((bits<<x)|(bits>>(m-x)))&full
    def inspect(points,levels):
        b=tuple(sorted(points))
        if b in blocks:return
        blocks.add(b);count['blocks']+=1
        divisor=gcd(m,*b)
        if divisor>1 and levels[5]==sum(1<<r for r in range(0,m,divisor)):
            assert m//divisor>=30 and divisor<=4
            count['proper_saturated']+=1;return
        target=sum(b)%m
        g={ (target-r)%m for r in range(m) if not (levels[5]>>r)&1 }
        f={ (r-target+1)%m for r in range(m) if not (levels[7]>>r)&1 }
        neighbors={d for d in g if (-d)%m in g}
        bits=sum(1<<d for d in neighbors)
        for u in sorted(neighbors):
            tick()
            possibilities=bits & shift(bits,u)
            possibilities &= full ^ ((1<<(u+1))-1)
            while possibilities:
                one=possibilities & -possibilities
                v=one.bit_length()-1;possibilities^=one
                delta={(p-q)%m for p in (0,u,v) for q in (0,u,v) if p!=q}
                if len(delta)!=6:continue
                if any((3*a-u-v)%m not in g for a in (0,u,v)):continue
                # Confirm the entire nine-multiset condition directly.
                for triple in combinations_with_replacement((0,u,v),3):
                    if triple!=(0,u,v):assert (sum(triple)-u-v)%m in g
                count['shapes']+=1;possible=[]
                for base in range(m-v):
                    c=[base,base+u,base+v]
                    pairs=[(c[0]+c[1])%m,(c[0]+c[2])%m,(c[1]+c[2])%m]
                    if all(s in f for s in pairs):possible.append(c)
                shape_records.append({'M':m,'B':list(b),'C_shape':[0,u,v],
                                      'compatible_even_triples':possible})
                count['even_triples']+=len(possible)
                for c in possible:survivors.append({'M':m,'B':list(b),'C':c})
    def walk(points,levels,after,unitless):
        tick();size=len(points);prefixes[size]+=1
        if levels[7]==full:return
        if size==5:inspect(points,levels);return
        degree=size+1;target=sum(points)
        for new in range(after,m):
            if new in points:continue
            if unitless and any(gcd(new-a,m)==1 for a in points):continue
            extended=points+[new]
            differences=[(a-b)%m for a in extended for b in extended if a!=b]
            if len(set(differences))!=degree*(degree-1):continue
            if any((levels[degree-q]>>((target+(1-q)*new)%m))&1
                   for q in range(degree+1) if q!=1):continue
            updated=[]
            for terms in range(8):
                reached=0
                for copies in range(terms+1):reached|=shift(levels[terms-copies],copies*new)
                updated.append(reached)
            walk(extended,updated,new+1,unitless)
    roots=sorted(m//order for order in range(3,m+1) if m%order==0)
    active['roots']=roots
    for first in roots:
        levels=[sum(1<<r for r in {k*first%m for k in range(terms+1)}) for terms in range(8)]
        walk([0,first],levels,1,first!=1)
    active['completion']='COMPLETE';return active

complete=True
for m in range(123,93,-1):
    try:
        row=run(m);reports.append(row)
        print(json.dumps({'M':m,'counts':row['counts'],'seconds':monotonic()-start}),flush=True)
    except TimeoutError:
        complete=False;break
source=json.loads(Path('stage31_even_three_five_results.json').read_text())
if complete:
    assert source['completion']=='COMPLETE' and not source['survivors'] and not survivors
    expected={r['M']:r['counts'] for r in source['reports']}
    for r in reports:
        a=r['counts'];b=expected[r['M']]
        assert a['blocks']==b['blocks'] and a['proper_saturated']==b['proper_saturated']
        assert a['shapes']==b['shapes_5odd_surviving'] and a['even_triples']==b['even_triples']
out={'completion':'COMPLETE' if complete else 'TIMEOUT/incomplete',
     'cap_seconds':cap,'elapsed_seconds':monotonic()-start,
     'completed_orders':[r['M'] for r in reports],'reports':reports,
     'partial_order':active if not complete else None,'survivors':survivors,
     'symbolic_shapes':shape_records,'imports_producer':False}
Path('stage31_even_independent_results.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
print(json.dumps({'completion':out['completion'],'seconds':out['elapsed_seconds'],
                  'orders':len(reports),'symbolic_shapes':len(shape_records),'survivors':len(survivors)}),flush=True)
