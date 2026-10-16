"""Five-second consistency check of new completed odd exclusions only."""
from pathlib import Path
from time import monotonic
import json

start=monotonic();cap=5
p=json.loads(Path('stage36_odd_canonical_results.json').read_text())
a=json.loads(Path('stage37_odd_independent_results.json').read_text())
pd={r['N']:r for r in p['reports']};ad={r['N']:r for r in a['reports']}
shared=sorted(set(pd)&set(ad))
assert shared and shared==list(range(189,max(shared)+1,2))
rows=[]
for n in shared:
    if monotonic()-start>=cap:raise TimeoutError('Cross-check incomplete')
    assert pd[n]['completion']==ad[n]['completion']=='COMPLETE'
    for key in ('primitive_B','bases_6_7_8','sidon_eight','rivals','valid_survivors'):
        assert pd[n]['counts'][key]==ad[n]['counts'][key]
    assert pd[n]['counts']['bases_6_7_8']==pd[n]['counts']['valid_survivors']==0
    rows.append({'N':n,'primitive_blocks':pd[n]['counts']['primitive_B'],
                 'discovery_triple_shapes':pd[n]['counts']['C_shapes'],
                 'independent_triple_shapes_after_safe_saturation_prune':ad[n]['counts']['C_shapes'],
                 'necessary_base_survivors':0})
assert not p['survivors'] and not a['survivors']
out={'completion':'COMPLETE','cap_seconds':cap,'elapsed_seconds':monotonic()-start,
     'independently_excluded_odd_orders':shared,'rows':rows,
     'new_general_lower_bound':max(shared)+2,
     'dependencies':['Audited elementary eight-point N>=187',
                     'Stage3 independent187 exclusion','Stages30-35 all even N<248 excluded'],
     'universal_248':'OPEN','aperiodicity':'Elementary Stage37 theorem; no computation'}
Path('stage37_final_crosscheck_results.json').write_text(json.dumps(out,indent=2)+'\n')
pending=list(range(max(shared)+2,248,2))
symbolic={'unexcluded_odd_orders':pending,
          'discovery_only_completed_orders':sorted(set(pd)-set(ad)),
          'discovery_interrupted_order':p['partial_order']['N'],
          'independent_interrupted_order':a['partial_order']['N'],
          'no_actual_valid_eight_set_survivor_found':True,
          'family':{'B':'Primitive valid five-set; canonical normalized unit pair or all unitless divisor roots',
                    'C':'c+{0,u,v}, 0<u<v, 0<=c<N-v, B and C disjoint',
                    'G':'sum(B)-complement(5B)',
                    'opposing_shapes':['u','-u','v','-v','v-u','u-v','-u-v','2u-v','2v-u'],
                    'constraints':'All nine deviations in G; q6/q7/q8 holes as Stage33; whole-set Sidon and remaining q0..4',
                    'structural_requirements':['h>0 by Stage26','doubling overlap<=5 by Stage29',
                                               '4A aperiodic by new Stage37 elementary proof']},
          'status':'Symbolic necessary families, not counterexamples or complete exclusions'}
Path('stage37_symbolic_survivors.json').write_text(json.dumps(symbolic,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
