"""Second cubic equality forced by the global count when the first is residual.

First residual models have T3=59, total cubic multiplicity at most two,
and at most five ordinary cubic pairs unless another equality occurs.
The hand bound q<=4P3 and 3t<=4P3 then excludes N<248. Thus all second
equalities are actual proof obligations, not parameter discovery samples.
"""
from itertools import combinations
from pathlib import Path
import argparse
import json
import time

from stage53_connected_split_probe import ALLWORDS, diff
from stage54_source_triple_probe import general_exclusion
from stage54_source_path_cubic_inventory import torsion_model, direction


def main(seconds,resume):
    from stage43_relation_growth import run
    started=time.monotonic()
    first=json.loads(Path('stage54_source_path_cubic_inventory_results.json').read_text())
    destination=Path('stage54_source_path_second_cubic_results.json')
    if resume:
        result=json.loads(destination.read_text())
        assert result['scope']=='Every second formally new cubic equality in the six first-cubic residual families.'
        assert not result['complete']
    else:
        result={'scope':'Every second formally new cubic equality in the six first-cubic residual families.',
                'parents':[],'complete':False,'all_closed':False}
    words=[w for w in ALLWORDS[3] if max(w)>1]
    for parent in [r for r in first['cases'] if not r['closed']]:
        assert parent['model']['torsion_order']==1
        base=parent['model']['rows']; cases={}; pairs=[]
        def val(w): return tuple(sum(w[i]*base[i][j] for i in range(8)) for j in range(len(base[0])))
        assert len({val(w) for w in words})==59
        for i,j in combinations(range(64),2):
            v=diff(val(words[i]),val(words[j]))
            if not any(v): continue
            key,factor=direction(v)
            cases.setdefault(key,{'words':(words[i],words[j]),'coefficient_direction':key,
                                  'source_scale':factor,'pair_indices':[]})
            cases[key]['pair_indices'].append((i,j))
            pairs.append({'indices':(i,j),'direction':key,'scale':factor})
        previous=next((r for r in result['parents'] if r['parent']==parent['index']),None)
        if previous:
            report=previous
            assert report['base_rows']==base and report['pair_coverage']==json.loads(json.dumps(pairs))
        else:
            report={'parent':parent['index'],'base_rows':base,'formal_cubic_values':59,
                    'pair_coverage':pairs,'cases':[],'complete':False}
            result['parents'].append(report)
        print(json.dumps({'parent':parent['index'],'directions':len(cases)}),flush=True)
        for index,(key,case) in enumerate(sorted(cases.items())):
            if index<len(report['cases']):
                saved=report['cases'][index]
                assert saved['index']==index and tuple(saved['coefficient_direction'])==key
                assert saved['words']==json.loads(json.dumps(case['words']))
                if saved.get('growth'):
                    assert Path(saved['growth']['certificate']).is_file()
                continue
            if time.monotonic()-started>seconds:
                destination.write_text(json.dumps(result)+'\n')
                raise TimeoutError('Second cubic coverage incomplete; no closure claimed.')
            rows=tuple(map(tuple,parent['relations']))+(diff(*case['words']),)
            exclusion=general_exclusion(rows)
            rec={'index':index,**case,'relations':rows,'exclusion':exclusion,'closed':bool(exclusion)}
            if exclusion is None:
                model,reduction=torsion_model(base,key,'s54_second_'+str(parent['index'])+'_'+str(index))
                rec['model']=model; rec['reduction']=reduction
                bound=run(model,4,89,[2])
                old=Path(bound['certificate']); new=Path(old.name.replace('stage43_s54_','stage54_'))
                old.rename(new); bound['certificate']=new.name
                rec['growth']=bound
                rec['closed']=bound.get('direct_rival') is not None or bound.get('positive_bound',0)>=89
            report['cases'].append(rec)
            if index%100==99:
                print(json.dumps({'parent':parent['index'],'processed':index+1,
                                  'open':[r['index'] for r in report['cases'] if not r['closed']]}),flush=True)
            if index%20==19:
                destination.write_text(json.dumps(result)+'\n')
        report['complete']=True
        destination.write_text(json.dumps(result)+'\n')
        print(json.dumps({'parent':parent['index'],'complete':True,
                          'closed':sum(r['closed'] for r in report['cases']),
                          'open':[r['index'] for r in report['cases'] if not r['closed']]}),flush=True)
    result['complete']=True
    result['all_closed']=all(r['closed'] for p in result['parents'] for r in p['cases'])
    result['elapsed']=time.monotonic()-started
    destination.write_text(json.dumps(result)+'\n')
    print(json.dumps({'complete':True,'all_closed':result['all_closed'],'elapsed':result['elapsed']}),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser(); p.add_argument('--seconds',type=float,default=180); p.add_argument('--resume',action='store_true')
    a=p.parse_args(); main(a.seconds,a.resume)
