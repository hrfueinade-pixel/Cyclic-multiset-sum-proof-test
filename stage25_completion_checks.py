"""Bounded final inventory/parity/status audit, not another research search."""
from itertools import product
import json
from pathlib import Path
import subprocess
import sys
from time import monotonic

def canonical_cycle(w):
    return min(v[i:]+v[:i] for v in (w,w[::-1]) for i in range(len(w)))

def inventory(cap):
    paths=set(); cycles=set(); isolated={'O','Q'}
    for L in (2,3):
        for letters in product('FOPQ',repeat=L):
            w=''.join(letters)
            if w>w[::-1] or w.count('F')>1 or w.count('Q')>1 or w.count('P')>2: continue
            if 'F' in w:
                f=w.index('F')
                if f not in (0,L-1) or 'Q' in w or w[1 if f==0 else L-2]!='O': continue
            if w=='PP' or w in ('FOP','POF'): continue
            if 'Q' in w and any(abs(i-w.index('Q'))!=1 for i,t in enumerate(w) if t=='P'): continue
            size=L-1+w.count('O')+int(w[0]!='F')+int(w[-1]!='F')
            if size<=cap: paths.add(w)
    # Triangle geometry: three edge-points, private O centers. Every P
    # has two center choices. It must meet any Q at its singleton.
    for letters in product('OPQ',repeat=3):
        w=''.join(letters)
        if w.count('Q')>1 or w.count('P')>2 or 3+w.count('O')>cap: continue
        p=[i for i,t in enumerate(w) if t=='P']
        for bits in product((0,1),repeat=len(p)):
            centers={i:((i-1)%3,i)[bit] for i,bit in zip(p,bits)}
            if len(set(centers.values()))!=len(centers): continue
            if any(centers[i] in {(j-1)%3,j} for i in p for j,t in enumerate(w) if t=='Q'): continue
            # Two Ps with the same singleton would give order three.
            singleton=[i if centers[i]==(i-1)%3 else (i-1)%3 for i in p]
            if len(set(singleton))!=len(singleton): continue
            cycles.add(canonical_cycle(w))
    return {'isolated':sorted(isolated),'paths':sorted(paths),'triangles':sorted(cycles)}

def main():
    start=monotonic()
    four=inventory(4); five=inventory(5)
    assert four=={'isolated':['O','Q'],'paths':['FO','OP','OQ','PQ','PQP'],'triangles':['OPP','OPQ']}
    assert five=={'isolated':['O','Q'],
                  'paths':['FO','FOO','OO','OP','OPP','OPQ','OQ','OQP','POP','PQ','PQP'],
                  'triangles':['OOP','OOQ','OPP','OPQ']}
    # All necessary DS/SS/DD numerical cases, no realizability assertion.
    losses=[]
    for d,e,j in product(range(8),range(2),range(2)):
        if e and d>2 or j and d>6: continue
        losses.append({'d':d,'e':e,'j':j,'L':2*d+4*e+j})
    assert max(r['L'] for r in losses)==14
    parity=[{'p':p,'q':8-p,'minimum_h':p*(8-p)-7} for p in range(1,8)]
    assert [r['p'] for r in parity if r['minimum_h']<=4]==[1,7]
    files=('stage18_tree_spectra_results.json','stage18_tree_spectra_independent_results.json',
           'stage19_cycle_results.json','stage19_cycle_independent_results.json',
           'stage20_path_results.json','stage20_path_independent_results.json',
           'stage21_pure_path_results.json','stage21_pure_independent_results.json',
           'stage23_endpoint_results.json','stage23_endpoint_independent_results.json',
           'stage24_arithmetic_results.json')
    assert all(json.loads(Path(f).read_text())['completion']=='COMPLETE' for f in files)
    records=[r for f in ('stage19_cycle_results.json','stage20_path_results.json',
                        'stage21_pure_path_results.json','stage23_endpoint_results.json')
             for r in json.loads(Path(f).read_text())['records']]
    assert sum(r['certificate'] is not None for r in records)==1183
    # Timeout controls run in a separate workspace directory and preserve
    # their entire small JSONs in this report, without touching evidence.
    controls=[]
    producers=(('stage18_tree_spectra.py','stage18_tree_spectra_results.json'),
               ('stage19_cycle_roles.py','stage19_cycle_results.json'),
               ('stage20_path_roles.py','stage20_path_results.json'),
               ('stage21_pure_paths.py','stage21_pure_path_results.json'),
               ('stage23_endpoint_roles.py','stage23_endpoint_results.json'))
    root=Path(__file__).resolve().parent
    control_dir=root/'.stage25_timeout_controls'
    control_dir.mkdir(exist_ok=True)
    for script,output in producers:
        remaining=30-(monotonic()-start)
        if remaining<=0: raise TimeoutError('Final audit incomplete')
        run=subprocess.run([sys.executable,str(root/script),'--seconds','0'],cwd=control_dir,
                           capture_output=True,text=True,timeout=min(10,remaining),check=True)
        data=json.loads((control_dir/output).read_text())
        assert data['completion']=='TIMEOUT'
        # A cooperative deadline may retain partial branches on coarse clocks.
        # Their status is incomplete; passing partial records prove no family.
        if 'maximum_triangles_without_22' in data: assert data['maximum_triangles_without_22'] is None
        controls.append({'script':script,'output':data})
    assert monotonic()-start<30
    result={'completion':'COMPLETE','seconds_limit':30,'elapsed_seconds':monotonic()-start,
            'support4_inventory':four,'support5_inventory':five,
            'DS_SS_DD_relaxation':losses,'parity_restrictions':parity,
            'completed_result_files':list(files),'saved_certificate_count':1183,
            'zero_budget_controls':controls,
            'scope':'Symbolic short type words, integer bounds, saved statuses and timeout semantics only.'}
    Path('stage25_completion_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print('COMPLETE:',len(losses),'loss cases; 5 zero-budget controls; inventories checked')

if __name__=='__main__': main()
