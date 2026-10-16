"""Discovery: necessary six-point quotient with 7B not full, M=64..123.

120s default global cap. Enumerate every necessary six-point survivor;
the separate seventh-extension check is required to exclude seven-sets.
Prefixes are hereditary valid, pair-Sidon,
non-antipodal. 0,g unit-normalization covers all primitive six-point sets;
for at most two prime factors the elementary unit-difference lemma gives
g=1. Any full 7-fold prefix sumset prunes all extensions since0 remains
in the prefix. The historical output field 'full8' counts this 7-fold prune.
"""
from math import gcd
from pathlib import Path
from time import monotonic
import json
import argparse

parser=argparse.ArgumentParser()
parser.add_argument('--lower',type=int,default=64)
parser.add_argument('--upper',type=int,default=123)
parser.add_argument('--seconds',type=float,default=120)
parser.add_argument('--output',default='stage34_seven_sum_results.json')
args=parser.parse_args()
assert 64<=args.lower<=args.upper<=123
start=monotonic(); cap=args.seconds; reports=[]; survivors=[]; total_nodes=0;partial_state=None
def primes(n):
    out=[]; p=2
    while p*p<=n:
        if n%p==0:
            out.append(p)
            while n%p==0:n//=p
        p+=1
    if n>1:out.append(n)
    return out

def run(m):
    global total_nodes,partial_state
    mask=(1<<m)-1; nodes=[0]*7; prune={'sidon':0,'validity':0,'full8':0}
    checked=set(); found=[]
    partial_state={'M':m,'nodes_by_size':nodes,'pruning':prune,'survivors':found}
    def rotate(bits,x):
        return ((bits<<x)|(bits>>(m-x)))&mask
    def visit(prefix,first,old,delta,after):
        global total_nodes
        if monotonic()-start>=cap: raise TimeoutError()
        k=len(prefix)
        nodes[k]+=1; total_nodes+=1
        if old[7]==mask:
            prune['full8']+=1; return
        if k==6:
            b=tuple(sorted(prefix))
            if gcd(m,*b)!=1:return
            if b not in checked:
                checked.add(b)
                missing=[x for x in range(m) if not(old[7]>>x)&1]
                found.append({'M':m,'B':list(b),'missing_7B':missing})
            return
        degree=k+1; target=sum(prefix)%m
        for x in range(after,m):
            if x==first:continue
            newdiff=[]; bad=False
            for a in prefix:
                v=(x-a)%m; w=(a-x)%m
                if v==w or v in delta or w in delta or v in newdiff or w in newdiff:
                    bad=True;break
                newdiff.extend((v,w))
            if bad:prune['sidon']+=1;continue
            if (old[degree]>>((target+x)%m))&1:
                prune['validity']+=1;continue
            if any((old[degree-q]>>((target-(q-1)*x)%m))&1
                   for q in range(2,degree+1)):
                prune['validity']+=1;continue
            new=[old[0]]
            for d in range(1,9):new.append(old[d]|rotate(new[d-1],x))
            visit(prefix+[x],first,new,delta|set(newdiff),x+1)
    ps=primes(m)
    roots=[1] if len(ps)<=2 else [g for g in range(1,m) if m%g==0 and 2*g!=m]
    for g in roots:
        sums=[sum(1<<(j*g%m) for j in range(k+1)) for k in range(9)]
        # Repeated residues can occur for small point order: use OR, not sum.
        sums=[]
        for k in range(9):
            bits=0
            for j in range(k+1):bits|=1<<(j*g%m)
            sums.append(bits)
        visit([0,g],g,sums,{g,m-g},1)
    return {'M':m,'completion':'COMPLETE','prime_factors':ps,'roots':roots,
            'nodes_by_size':nodes,'pruning':prune,'survivor_count':len(found)},found

complete=True; current=None
for m in range(args.lower,args.upper+1):
    current=m
    try:
        report,found=run(m); reports.append(report); survivors.extend(found)
        print(json.dumps({'M':m,'nodes':sum(report['nodes_by_size']),
                          'survivors':len(found),'seconds':monotonic()-start}),flush=True)
    except TimeoutError:
        complete=False; break
out={'completion':'COMPLETE' if complete else 'TIMEOUT/incomplete',
     'cap_seconds':cap,'elapsed_seconds':monotonic()-start,
     'completed_orders':[r['M'] for r in reports],
     'interrupted_order':None if complete else current,'total_nodes':total_nodes,
     'requested_orders':list(range(args.lower,args.upper+1)),
     'partial_state':partial_state if not complete else None,
     'scope':'Primitive hereditary-valid non-antipodal six-point B;7B not full',
     'reports':reports,'survivors':survivors}
Path(args.output).write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('reports','survivors')}),flush=True)
