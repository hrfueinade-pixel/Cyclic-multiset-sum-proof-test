"""Three fully classified opponents to the remaining PO endpoint."""
import argparse
from itertools import product
import json
from pathlib import Path
from time import monotonic
from stage19_cycle_roles import e,lin,compositions,find

def models():
    coreP=lin((3,e(0)),(1,e(1)))
    coreO=lin((2,e(2)),(1,e(1)),(1,e(3)))
    for shape in ('isolatedO','FO','PO'):
        if shape=='isolatedO':
            vertices=[coreP,coreO,lin((2,e(4)),(1,e(5)),(1,e(6)))]
            types='POO'; centers={0:0,1:2,2:4}
        elif shape=='FO':
            vertices=[coreP,coreO,lin((4,e(4))),lin((2,e(5)),(1,e(4)),(1,e(6)))]
            types='POFO'; centers={0:0,1:2,3:5}
        else:
            vertices=[coreP,coreO,lin((3,e(4)),(1,e(5))),lin((2,e(6)),(1,e(5)),(1,e(7)))]
            types='POPO'; centers={0:0,1:2,2:4,3:6}
        supports=[{j for j,x in enumerate(v) if x} for v in vertices]
        base=[lin((1,v),(-1,vertices[0])) for v in vertices[1:]]
        domains=[]; names=[]
        for i in range(len(vertices)):
            for j in range(i):
                if supports[i]&supports[j]: continue
                if types[i] in 'OP' and types[j] in 'OP':
                    a,c=centers[i],centers[j]
                    if types[i]==types[j]=='P':
                        base.append(lin((5,e(a)),(-5,e(c))))
                    else:
                        roles=product(sorted(supports[i]-{a}),sorted(supports[j]-{c}))
                        domains.append([(r,lin((2,e(a)),(-2,e(c)),(-1,e(r[0])),(1,e(r[1])))) for r in roles])
                        names.append(['double_centers',i,j])
                elif {types[i],types[j]}=={'F','P'}:
                    f=i if types[i]=='F' else j
                    p=j if f==i else i
                    z=next(iter(supports[f])); a=centers[p]
                    domains.append([((k,),lin((6,e(z)),(-5,e(a)),(-1,e(k)))) for k in range(8)])
                    names.append(['forced_point',f,p])
        yield shape,vertices,base,domains,names

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--seconds',type=float,default=60)
    args=ap.parse_args(); start=monotonic()
    candidates=tuple(c for c in compositions(8,8) if c!=(1,)*8)
    records=[]; complete=True
    for shape,vertices,base,domains,names in models():
        for options in product(*domains):
            if monotonic()-start>args.seconds: complete=False; break
            rows=base+[r for _,r in options]
            records.append({'shape':shape,'vertices':vertices,'domain_names':names,
                            'roles':[r for r,_ in options],'rows':rows,'certificate':find(rows,candidates)})
        if not complete: break
    data={'completion':'COMPLETE' if complete else 'TIMEOUT','seconds_limit':args.seconds,
          'elapsed_seconds':monotonic()-start,'records':records}
    Path('stage23_endpoint_results.json').write_text(json.dumps(data,indent=2)+'\n')
    print(data['completion'],data['elapsed_seconds'])
    for shape in ('isolatedO','FO','PO'):
        local=[r for r in records if r['shape']==shape]
        print(shape,len(local),'branches;',sum(r['certificate'] is None for r in local),'uncertified')

if __name__=='__main__': main()
