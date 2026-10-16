"""Extra cubic equality forced by the exact source-path model.

The base has sixty formal repeated cubic values and only four collision
pairs. The hand global count forces at least six pairs below248, so a valid
realization must identify two DIFFERENT formal cubic classes.
Inventory is symbolic only. Odd gcd factors are retained as torsion.
"""
from itertools import combinations
from math import gcd
from pathlib import Path
import argparse
import json
import time

from stage53_connected_split_probe import ALLWORDS, diff
from stage54_source_triple_probe import general_exclusion


def egcd(a,b):
    old_r,r=a,b; old_s,s=1,0; old_t,t=0,1
    while r:
        q=old_r//r
        old_r,r=r,old_r-q*r
        old_s,s=s,old_s-q*s
        old_t,t=t,old_t-q*t
    if old_r<0:
        old_r,old_s,old_t=-old_r,-old_s,-old_t
    assert a*old_s+b*old_t==old_r
    return old_r,old_s,old_t


def torsion_model(base,v,name):
    n=len(v); U=[[int(i==j) for j in range(n)] for i in range(n)]
    row=list(v)
    first=next(i for i,x in enumerate(row) if x)
    if first:
        row[0],row[first]=row[first],row[0]
        for i in range(n): U[i][0],U[i][first]=U[i][first],U[i][0]
    for j in range(1,n):
        if not row[j]: continue
        a,b=row[0],row[j]; g,p,q=egcd(a,b)
        old0=[U[i][0] for i in range(n)]; oldj=[U[i][j] for i in range(n)]
        for i in range(n):
            U[i][0]=p*old0[i]+q*oldj[i]
            U[i][j]=-(b//g)*old0[i]+(a//g)*oldj[i]
        row[0],row[j]=g,0
    if row[0]<0:
        row[0]=-row[0]
        for i in range(n): U[i][0]=-U[i][0]
    assert [sum(v[i]*U[i][j] for i in range(n)) for j in range(n)]==row
    g=row[0]; odd=g
    while odd%2==0: odd//=2
    transformed=[[sum(a[i]*U[i][j] for i in range(n)) for j in range(n)] for a in base]
    model={'id':name,'direction':v,'rows':[a[1:] for a in transformed],
           'torsion_rows':[a[0]%odd for a in transformed],'torsion_order':odd,
           'parameterization':'Unimodular column reduction; odd gcd retained, only powers of two removed.'}
    return model,{'U':U,'gcd':g,'odd_gcd':odd,'transformed':transformed}


def direction(v):
    d=list(v); factor=1
    while all(x%2==0 for x in d):
        d=[x//2 for x in d]; factor*=2
    if next(x for x in d if x)<0:
        d=[-x for x in d]; factor=-factor
    return tuple(d),factor


def main(growth,seconds):
    started=time.monotonic()
    basefile=json.loads(Path('stage54_source_triple_results.json').read_text())
    source=next(r for r in basefile['records'] if r['tail']==[3,6])
    base=source['parameterization']['rows']
    def val(w): return tuple(sum(w[i]*base[i][j] for i in range(8)) for j in range(len(base[0])))
    words=[w for w in ALLWORDS[3] if max(w)>1]
    assert len(words)==64 and len({val(w) for w in words})==60
    cases={}; pairs=[]
    for i,j in combinations(range(64),2):
        v=diff(val(words[i]),val(words[j]))
        if not any(v): continue
        key,factor=direction(v)
        cases.setdefault(key,{'words':(words[i],words[j]),'coefficient_direction':key,
                              'source_scale':factor,'pair_indices':[]})
        cases[key]['pair_indices'].append((i,j))
        pairs.append({'indices':(i,j),'direction':key,'scale':factor})
    result={'scope':'All additional repeated cubic equalities for the complete source-path family.',
            'base_rows':base,'base_relations':source['relations'],'words':words,
            'formal_cubic_values':60,'pair_coverage':pairs,'cases':[],
            'inventory_complete':False,'all_cases_closed':False}
    print(json.dumps({'directions':len(cases),'covered_pairs':len(pairs)}),flush=True)
    if growth: from stage43_relation_growth import run
    for index,(key,case) in enumerate(sorted(cases.items())):
        if time.monotonic()-started>seconds:
            Path('stage54_source_path_cubic_inventory_results.json').write_text(json.dumps(result)+'\n')
            raise TimeoutError('New symbolic inventory incomplete; no global exclusion conclusion.')
        extra=diff(*case['words'])
        rows=tuple(map(tuple,source['relations']))+(extra,)
        exclusion=general_exclusion(rows)
        rec={'index':index,**case,'relations':rows,'exclusion':exclusion,'closed':bool(exclusion)}
        if exclusion is None:
            model,reduction=torsion_model(base,key,'s54_path_extra_'+str(index))
            rec['model']=model; rec['reduction']=reduction
            if growth:
                bound=run(model,4,89,[2])
                old=Path(bound['certificate']); new=Path(old.name.replace('stage43_s54_','stage54_'))
                old.rename(new); bound['certificate']=new.name
                rec['growth']=bound
                rec['closed']=bound.get('direct_rival') is not None or bound.get('positive_bound',0)>=89
        result['cases'].append(rec)
        print(json.dumps({'index':index,'exclusion':exclusion['kind'] if exclusion else None,
                          'closed':rec['closed'],'bound':rec.get('growth',{}).get('positive_bound'),
                          'torsion':rec.get('model',{}).get('torsion_order')}),flush=True)
        Path('stage54_source_path_cubic_inventory_results.json').write_text(json.dumps(result)+'\n')
    result['inventory_complete']=True
    result['all_cases_closed']=all(r['closed'] for r in result['cases'])
    result['elapsed']=time.monotonic()-started
    Path('stage54_source_path_cubic_inventory_results.json').write_text(json.dumps(result)+'\n')
    print(json.dumps({'complete':True,'cases':len(cases),'direct':sum(bool(r['exclusion']) for r in result['cases']),
                      'closed':sum(r['closed'] for r in result['cases']),
                      'open':[r['index'] for r in result['cases'] if not r['closed']],'elapsed':result['elapsed']}),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser(); p.add_argument('--growth',action='store_true'); p.add_argument('--seconds',type=float,default=180)
    a=p.parse_args(); main(a.growth,a.seconds)
