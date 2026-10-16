"""Use the proved general source theorem on the remaining graph exceptions.

All inputs are fixed simultaneous word relations. No group parameters or
cyclic moduli are searched. Positive discovery only; incomplete bounds
remain open and do not prove a general assignment theorem.
"""
from itertools import combinations
from pathlib import Path
from collections import Counter
import json
import gzip
from fractions import Fraction
from math import gcd,lcm

from stage53_connected_split_probe import CENTRAL, V, word, diff, normal, roots, attachments, split
from stage54_source_triple_probe import general_exclusion, dyadic_parameterization
from stage54_source_path_cubic_inventory import torsion_model


ORD4=[word(c,t) for c in V for t in combinations(set(V)-{c},2)]


def one_torsion_parameterization(rows,name):
    """Complete intermediate unit model plus one retained torsion constraint."""
    mat=[list(map(Fraction,r[:7])) for r in rows]; indices=list(range(len(rows)))
    columns=set(range(7)); pivots=[]; k=0
    while k<len(mat):
        choices=[]
        for i in range(k,len(mat)):
            for c in columns:
                v=mat[i][c]
                if v and abs(v.numerator)&(abs(v.numerator)-1)==0 and v.denominator&(v.denominator-1)==0:
                    choices.append((abs(v),c,i))
        if not choices: break
        _,c,i=min(choices); mat[k],mat[i]=mat[i],mat[k]; indices[k],indices[i]=indices[i],indices[k]
        factor=mat[k][c]; mat[k]=[v/factor for v in mat[k]]
        for i in range(len(mat)):
            if i!=k and mat[i][c]:
                f=mat[i][c]; mat[i]=[v-f*w for v,w in zip(mat[i],mat[k])]
        columns.remove(c); pivots.append(c); k+=1
    free=sorted(columns)
    coords=[[Fraction(int(i==f)) for f in free] for i in range(7)]
    for row,c in enumerate(pivots): coords[c]=[-mat[row][f] for f in free]
    coords.append([Fraction(0) for _ in free])
    scale=lcm(*(v.denominator for r in coords for v in r)); assert scale&(scale-1)==0
    M=[[int(v*scale) for v in r] for r in coords]
    unit={'rows':M,'scale':scale,'free_labels':free,'pivots':pivots,'selected_rows':indices[:k]}
    constraints=[[sum(r[i]*M[i][j] for i in range(8)) for j in range(len(free))] for r in rows]
    first=next((r for r in constraints if any(r)),None)
    if first is None:
        return {'model':{'id':name,'direction':[],'rows':M,'torsion_rows':[0]*8,'torsion_order':1,
                         'parameterization':'Only dyadic pivots.'},'unit':unit,'constraints':constraints,'U':None}
    model,reduction=torsion_model(M,tuple(first),name)
    U=reduction['U']
    transformed=[[sum(r[i]*U[i][j] for i in range(len(free))) for j in range(len(free))] for r in constraints]
    if any(any(r[1:]) for r in transformed): return None
    g=gcd(*(r[0] for r in transformed)); odd=g
    while odd%2==0: odd//=2
    full=[[sum(r[i]*U[i][j] for i in range(len(free))) for j in range(len(free))] for r in M]
    model['torsion_order']=odd; model['torsion_rows']=[r[0]%odd for r in full]
    return {'model':model,'unit':unit,'constraints':constraints,'U':U,'gcd':g,'odd_gcd':odd}


def source_exclusion(rows,models):
    value,cert,rank,coords=normal(rows)
    for model in models:
        for source_index,source in enumerate(model['sources']):
            for other in ORD4:
                if other in source or value(other)!=value(source[0]):
                    continue
                equality=cert(diff(source[0],other))
                source_equality=cert(diff(*source))
                if equality and source_equality:
                    return {'kind':'split_source_triple','split_labels':model['labels'],
                            'source_index':source_index,'third_word':other,
                            'source_identity':source_equality,'third_identity':equality}
    return None


def positive_case(rows,models,name):
    from stage43_relation_growth import run
    record={'rows':rows,'splits':[m['labels'] for m in models]}
    exclusion=general_exclusion(rows)
    if exclusion is None: exclusion=source_exclusion(rows,models)
    record['exclusion']=exclusion
    if exclusion is None:
        parameter=one_torsion_parameterization(rows,name)
        record['complete_parameterization']=parameter
        if parameter:
            growth=run(parameter['model'],4,89,[2])
            old=Path(growth['certificate']); dest=Path(old.name.replace('stage43_s55_','stage55_'))
            old.rename(dest); growth['certificate']=dest.name
            record['growth']=growth
    record['closed']=bool(exclusion) or record.get('growth',{}).get('positive_bound',0)>=89 or record.get('growth',{}).get('direct_rival') is not None
    return record


def cubic_splits():
    answer=[]
    for i,j in combinations((0,1,2),2):
        x,y=i,j; c,a=i+3,j+3
        free=set(V)-{x,y,a,c}
        for z in sorted(free):
            for b in sorted(free-{z}):
                d,e=sorted(free-{z,b})
                answer.append(split(x,y,z,a,b,c,d,e))
    assert len(answer)==36
    return answer


def extend():
    data=json.loads(Path('stage55_split_exception_results.json').read_text())
    records=data['records']
    for r in records:
        if r['closed'] or r['scope']=='cubic_triple': continue
        models=[split(*a) for a in r['splits']]
        result=positive_case(tuple(map(tuple,r['rows'])),models,'s55_torsion_'+r['scope']+'_'+str(r['index']))
        r.update(result)
        print(json.dumps({'scope':r['scope'],'index':r['index'],'closed':r['closed'],
                          'tor':r.get('complete_parameterization',{}).get('model',{}).get('torsion_order'),
                          'bound':r.get('growth',{}).get('positive_bound')}),flush=True)
    base=(diff(word(0,(3,)),word(1,(4,))),diff(word(0,(3,)),word(2,(5,))))
    all_models=cubic_splits(); first=[]
    for i,model in enumerate(all_models):
        r=positive_case(base+(model['rows'][1],),(model,),'s55_c3_one_'+str(i))
        r['index']=i; first.append(r)
        print(json.dumps({'c3_first':i,'closed':r['closed'],'bound':r.get('growth',{}).get('positive_bound'),
                          'kind':r['exclusion']['kind'] if r['exclusion'] else None}),flush=True)
    survivors=[i for i,r in enumerate(first) if not r['closed']]
    pairs=[]
    for i,j in combinations(survivors,2):
        a,b=all_models[i],all_models[j]
        rows=base+(a['rows'][1],b['rows'][1])
        r=positive_case(rows,(a,b),'s55_c3_pair_'+str(i)+'_'+str(j))
        r.update(left=i,right=j); pairs.append(r)
        print(json.dumps({'c3_pair':(i,j),'closed':r['closed'],'bound':r.get('growth',{}).get('positive_bound'),
                          'tor':r.get('complete_parameterization',{}).get('model',{}).get('torsion_order'),
                          'kind':r['exclusion']['kind'] if r['exclusion'] else None}),flush=True)
    data['cubic_first']=first; data['cubic_survivors']=survivors; data['cubic_pairs']=pairs
    Path('stage55_split_exception_results.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({'path_open':[(r['scope'],r.get('index')) for r in records if r['scope']!='cubic_triple' and not r['closed']],
                      'cubic_survivors':survivors,'pair_open':[(r['left'],r['right']) for r in pairs if not r['closed']]}))


def triangle_marks():
    data=json.loads(Path('stage55_split_exception_results.json').read_text())
    previous=json.loads(gzip.decompress(Path('stage53_split_graph_certificates.json.gz').read_bytes()))['two_marks']
    left=list(roots((0,2))); answer=[]
    for r in previous['records']:
        witness=r['witness']
        if not witness or witness['kind']!='ordinary_quartic_triple': continue
        degrees=Counter(i for w in witness['words'] for i,n in enumerate(w) if n==1)
        if tuple(sorted(degrees.values(),reverse=True))!=(2,2,2): continue
        y,z,f,g=r['first_closure']; closing=[0]*8
        closing[y]+=2; closing[z]-=2; closing[f]-=1; closing[g]+=1
        rows=CENTRAL['rows']+(tuple(closing),)+left[r['root']]['rows']
        result=positive_case(rows,(CENTRAL,left[r['root']]['split']),
                             's55_triangle_marks_'+str(r['root'])+'_'+str(f)+str(g))
        result.update(root=r['root'],first_closure=r['first_closure'])
        answer.append(result)
        print(json.dumps({'root':r['root'],'closure':r['first_closure'],'closed':result['closed'],
                          'kind':result['exclusion']['kind'] if result['exclusion'] else None,
                          'bound':result.get('growth',{}).get('positive_bound'),
                          'tor':result.get('complete_parameterization',{}).get('model',{}).get('torsion_order')}),flush=True)
    assert len(answer)==2
    data['triangle_marks']=answer
    Path('stage55_split_exception_results.json').write_text(json.dumps(data,indent=2)+'\n')


def main():
    left=list(roots((0,2))); edges=list(attachments((0,2)))
    records=[]
    prior=json.loads(gzip.decompress(Path('stage53_split_graph_certificates.json.gz').read_bytes()))
    inputs=[('root',prior['marked_edge']['half_records']),
            ('edge',prior['degree_three']['half_records']),
            ('marks',prior['two_marks']['records'])]
    for scope,data in inputs:
        for r in data:
            witness=r['witness']
            if not witness or witness['kind']!='ordinary_quartic_triple': continue
            ws=witness['words']; deg=Counter(i for w in ws for i,n in enumerate(w) if n==1)
            signature=tuple(sorted(deg.values(),reverse=True))
            if signature!=(2,2,1,1): continue
            if scope=='root':
                index=r['index']; models=(CENTRAL,left[index]['split']); rows=CENTRAL['rows']+left[index]['rows']
            elif scope=='edge':
                index=r['attachment']; models=(CENTRAL,edges[index]); rows=CENTRAL['rows']+edges[index]['rows']
            else:
                index=r['root']; models=(CENTRAL,left[index]['split'])
                y,z,f,g=r['first_closure']; closure=[0]*8
                closure[y]+=2; closure[z]-=2; closure[f]-=1; closure[g]+=1
                rows=CENTRAL['rows']+(tuple(closure),)+left[index]['rows']
            result=positive_case(rows,models,'s55_'+scope+'_'+str(index))
            result.update(scope=scope,index=index)
            records.append(result)
            print(json.dumps({'scope':scope,'index':index,'closed':result['closed'],
                              'kind':result['exclusion']['kind'] if result['exclusion'] else None,
                              'bound':result.get('growth',{}).get('positive_bound'),
                              'dyadic_model':result.get('parameterization') is not None}),flush=True)
    # A regular ordinary cubic triple; the four nontrivial first-split
    # orbits cover thirds/middle labels among {2,5,6,7}, up to free swap.
    base=(diff(word(0,(3,)),word(1,(4,))),diff(word(0,(3,)),word(2,(5,))))
    all_splits=cubic_splits()
    for z,b in ((5,6),(6,2),(6,5),(6,7)):
        model=next(m for m in all_splits if m['labels'][0:3]==(0,1,z) and m['labels'][4]==b)
        # Its first row is the existing cubic equality; only second row new.
        rows=base+(model['rows'][1],)
        result=positive_case(rows,(model,),'s55_cubic_'+str(z)+str(b))
        result.update(scope='cubic_triple',third=z,middle=b)
        records.append(result)
        print(json.dumps({'scope':'cubic_triple','third':z,'middle':b,'closed':result['closed'],
                          'kind':result['exclusion']['kind'] if result['exclusion'] else None,
                          'bound':result.get('growth',{}).get('positive_bound')}),flush=True)
    Path('stage55_split_exception_results.json').write_text(json.dumps({'records':records,
        'boundary':'Fixed graph exceptions and four cubic-triple/split coupling models only; no full N claim.'},indent=2)+'\n')


if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser(); p.add_argument('--extend',action='store_true'); p.add_argument('--triangle-marks',action='store_true'); a=p.parse_args()
    if a.triangle_marks: triangle_marks()
    elif a.extend: extend()
    else: main()
