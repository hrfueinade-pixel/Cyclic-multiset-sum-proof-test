"""Independent Stage17 role, witness, rank-forcing, and torsion audit.

The base quartic equalities are encoded with u=0.  Every accepted exclusion
has an integer identity with a power-of-two multiplier.  Necessary role
survivors are not asserted realizable. This separately checks the initial
16-role cross-check and audits all saved producer witnesses and coverage,
including the final 504 branches and elementary signed-orbit calculations.
No local-proof or historical checker is imported.
"""
from fractions import Fraction
from itertools import product
from pathlib import Path
import json
import time
from math import gcd

LABELS = ('u', 'a', 'c', 'b', 'v', 'w', 'p', 'q')
POINTS = ((0,0,0,0,0), (1,0,0,0,0), (0,1,0,0,0),
          (0,0,1,0,0), (0,0,0,1,0), (0,0,0,0,1),
          (-2,0,-1,1,1), (0,-2,-1,1,1))
P = dict(zip(LABELS, POINTS))

def vector_sum(counts):
    return tuple(sum(k*p[j] for k,p in zip(counts,POINTS)) for j in range(5))

TARGET = vector_sum((1,)*8)

def compositions(total, places):
    if places == 1:
        yield (total,)
        return
    for n in range(total+1):
        for rest in compositions(total-n, places-1):
            yield (n,)+rest

def row(center, positive, negative):
    return tuple(2*P[center][j]-P[positive][j]+P[negative][j]
                 for j in range(5))

def solve_two_rows(rows, desired):
    """Solve by a 2x2 minor, then validate all five coordinates."""
    first, second = rows
    for i in range(5):
        for j in range(i+1,5):
            det = first[i]*second[j]-first[j]*second[i]
            if det:
                x=Fraction(desired[i]*second[j]-desired[j]*second[i],det)
                y=Fraction(first[i]*desired[j]-first[j]*desired[i],det)
                if any(x*first[k]+y*second[k]!=desired[k] for k in range(5)):
                    return None
                denominator=max(x.denominator,y.denominator)
                if denominator & (denominator-1):
                    return None
                return denominator, (int(x*denominator),int(y*denominator))
    raise ValueError('Unexpected dependent two-row presentation')

def verify(rows, counts, scale, coefficients):
    if (len(counts)!=8 or any(type(n) is not int or n<0 for n in counts)
            or sum(counts)!=8 or tuple(counts)==(1,)*8):
        return False
    if type(scale) is not int or scale<=0 or scale & (scale-1) or len(coefficients)!=2:
        return False
    if not all(type(z) is int for z in coefficients):
        return False
    actual=vector_sum(counts)
    return all(scale*(actual[j]-TARGET[j]) ==
               sum(z*r[j] for z,r in zip(coefficients,rows)) for j in range(5))

def audit_local_results(path):
    """Reconstruct every relation and verify witnesses without its producer."""
    data=json.loads(path.read_text(encoding='utf-8'))
    names=('w','u','a','c','b','p','q','v')
    points=((0,0,0),(1,0,0),(1,1,0),(1,1,1),
            (0,-4,0),(0,2,4),(0,2,2),(0,0,4))
    by_name=dict(zip(names,points))
    directions={'double_v_minus_w':(0,0,8),
                'double_b_minus_w':(0,-8,0)}
    assert tuple(data['point_names'])==names
    assert tuple(map(tuple,data['point_vectors']))==points
    assert data['completion']=='COMPLETE'
    target=tuple(sum(p[j] for p in points) for j in range(3))
    def relation(name,pair):
        positive,negative=pair
        assert positive!=negative and positive in names and negative in names
        return tuple(directions[name][j]-by_name[positive][j]+by_name[negative][j]
                     for j in range(3))
    def check(rows,counts,scale,coefficients):
        if (len(counts)!=8 or any(type(n) is not int or n<0 for n in counts)
                or sum(counts)!=8 or tuple(counts)==(1,)*8): return False
        if type(scale) is not int or scale<=0 or scale & (scale-1): return False
        if len(coefficients)!=len(rows) or any(type(z) is not int for z in coefficients):
            return False
        rival=tuple(sum(n*p[j] for n,p in zip(counts,points))-target[j] for j in range(3))
        return all(scale*rival[j]==sum(z*r[j] for z,r in zip(coefficients,rows))
                   for j in range(3))
    singles={name:set() for name in directions}
    combined=set()
    audited=negative_tests=0
    for entry in data['exclusions']:
        rows=tuple(relation(name,pair) for name,pair in zip(entry['directions'],entry['roles']))
        assert rows==tuple(map(tuple,entry['rows']))
        cert=entry['certificate']
        counts=cert['rival_counts']; scale=cert['multiplier']; coeff=cert['coefficients']
        assert check(rows,counts,scale,coeff)
        assert cert['vector']==[sum(n*p[j] for n,p in zip(counts,points))-target[j]
                                for j in range(3)]
        changed=list(coeff); index=next(i for i,r in enumerate(rows) if any(r)); changed[index]+=1
        assert not check(rows,counts,scale,changed)
        assert not check(rows,counts,3,coeff)
        assert not check(rows,[1]*8,scale,coeff)
        assert not check(rows,[8]*8,scale,coeff)
        audited+=1; negative_tests+=4
        if len(rows)==1:
            pair=tuple(entry['roles'][0]); domain=singles[entry['directions'][0]]
            assert pair not in domain; domain.add(pair)
        else:
            key=tuple(map(tuple,entry['roles'])); assert key not in combined; combined.add(key)
    retained={entry['direction']:set(map(tuple,entry['retained_roles']))
              for entry in data['single_domains']}
    all_roles=set(product(names,names))-{(n,n) for n in names}
    for name in directions:
        assert not singles[name]&retained[name]
        assert singles[name]|retained[name]==all_roles
    for entry in data['survivors']:
        rows=tuple(relation(name,pair) for name,pair in zip(entry['directions'],entry['roles']))
        assert rows==tuple(map(tuple,entry['rows']))
        key=tuple(map(tuple,entry['roles'])); assert key not in combined; combined.add(key)
    assert combined==set(product(retained['double_v_minus_w'],retained['double_b_minus_w']))
    final_coverage={}
    initial_survivor_keys={tuple(map(tuple,entry['roles'])) for entry in data['survivors']}
    assert not data.get('extra_quartic_exclusions',[])
    assert {tuple(map(tuple,entry['roles'])) for entry in data['extra_quartic_survivors']}==initial_survivor_keys
    for entry in data.get('rank_forcing_coverage',[]):
        parents=tuple(map(tuple,entry['parent_roles']))
        rows=tuple(relation(name,pair) for name,pair in zip(directions,parents))
        x,y=rows
        cross=(x[1]*y[2]-x[2]*y[1],x[2]*y[0]-x[0]*y[2],x[0]*y[1]-x[1]*y[0])
        divisor=gcd(*cross); functional=tuple(z//divisor for z in cross)
        assert functional==tuple(entry['functional']) and any(functional)
        assert all(sum(f*r for f,r in zip(functional,row))==0 for row in rows)
        def height(pair):
            return sum(f*(by_name[pair[0]][j]-by_name[pair[1]][j]) for j,f in enumerate(functional))
        ordered_roles=[pair for pair in product(names,names) if pair[0]!=pair[1]]
        source=max(ordered_roles,key=height)
        assert source==tuple(entry['source_difference'])
        maximum=height(source); assert maximum>0 and maximum==entry['maximum']
        doubled=tuple(2*(by_name[source[0]][j]-by_name[source[1]][j]) for j in range(3))
        assert doubled==tuple(entry['doubled_direction'])
        assert entry['complete'] and entry['partners_examined']==56
        final_coverage[parents]={'seen':set(),'rows':rows,'functional':functional,
                                'source':source,'doubled':doubled,'maximum':maximum}
    determinants=[]
    final_survivors=[]
    for entry in data.get('rank_forcing_exclusions',[])+data.get('rank_forcing_survivors',[]):
        parents=tuple(map(tuple,entry['parent_roles'])); covered=final_coverage[parents]
        partner=tuple(entry['partner_role']); assert partner in all_roles
        assert partner not in covered['seen']; covered['seen'].add(partner)
        assert tuple(entry['source_difference'])==covered['source']
        assert tuple(entry['functional'])==covered['functional']
        last=tuple(covered['doubled'][j]-by_name[partner[0]][j]+by_name[partner[1]][j] for j in range(3))
        rows=covered['rows']+(last,)
        assert rows==tuple(map(tuple,entry['rows']))
        assert sum(f*r for f,r in zip(covered['functional'],last))>=covered['maximum']>0
        x,y,z=rows
        det=(x[0]*(y[1]*z[2]-y[2]*z[1])-x[1]*(y[0]*z[2]-y[2]*z[0])
             +x[2]*(y[0]*z[1]-y[1]*z[0]))
        assert det
        if 'certificate' in entry:
            cert=entry['certificate']; counts=cert['rival_counts']; scale=cert['multiplier']; coeff=cert['coefficients']
            assert check(rows,counts,scale,coeff)
            changed=list(coeff); changed[0]+=1
            assert not check(rows,counts,scale,changed)
            assert not check(rows,counts,3,coeff)
            assert not check(rows,[1]*8,scale,coeff)
            assert not check(rows,[8]*8,scale,coeff)
            audited+=1; negative_tests+=4
        else:
            determinants.append(abs(det))
            final_survivors.append({'parent_roles':parents,'partner_role':partner,'determinant':abs(det)})
    if final_coverage:
        assert len(final_coverage)==len(data['extra_quartic_survivors'])==9
        assert set(final_coverage)==initial_survivor_keys
        assert all(covered['seen']==all_roles for covered in final_coverage.values())
    signed_orbits={}
    for modulus in (503,163,167,61,59,161):
        powers=set(); value=1
        while value not in powers:
            powers.add(value); value=(2*value)%modulus
        assert value==1
        signed=powers|{(-value)%modulus for value in powers}
        signed_orbits[str(modulus)]={'doubling_order':len(powers),'signed_orbit':len(signed)}
    return {'source':path.name,'completion':'COMPLETE','independent_integer_certificates':audited,
            'deliberate_corruption_rejections':negative_tests,
            'single_role_coverage':{name:len(singles[name])+len(retained[name]) for name in directions},
            'combined_retained_domain_coverage':len(combined),
            'remaining_two_direction_presentations':len(data['survivors']),
            'rank_forcing_domain_coverage':sum(len(c['seen']) for c in final_coverage.values()),
            'rank_forcing_survivors':final_survivors,'determinants':determinants,
            'signed_doubling_orbits':signed_orbits,
            'verdict':'All saved integer identities and complete necessary role coverage accepted.'}

def main():
    start=time.monotonic()
    rivals=[(n,tuple(x-y for x,y in zip(vector_sum(n),TARGET)))
            for n in compositions(8,8) if n!=(1,)*8]
    outcomes=[]
    tests={'accepted_good':0,'rejected_corrupt_coefficient':0,
           'rejected_odd_scale':0,'rejected_all_ones':0,'rejected_bad_counts':0}
    choices_a=tuple(product(('b','p'),('v','w')))
    choices_c=tuple(product(('b','q'),('v','w')))
    for a_choice,c_choice in product(choices_a,choices_c):
        rows=(row('a',*a_choice),row('c',*c_choice))
        certificate=None
        for counts,desired in rivals:
            solution=solve_two_rows(rows,desired)
            if solution is None:
                continue
            scale,coefficients=solution
            assert verify(rows,counts,scale,coefficients)
            assert not verify(rows,counts,scale,(coefficients[0]+1,coefficients[1]))
            assert not verify(rows,counts,3,coefficients)
            assert not verify(rows,(1,)*8,scale,coefficients)
            assert not verify(rows,(8,)*8,scale,coefficients)
            for test in tests: tests[test]+=1
            certificate={'counts':counts,'scale':scale,'coefficients':coefficients}
            break
        outcomes.append({'a_choice':a_choice,'c_choice':c_choice,
                         'rows':rows,'certificate':certificate})
    result={'scope':'Initial 16-role cross-check; independent producer certificate, full coverage, rank-forcing, and signed-orbit audit',
            'completion':'COMPLETE','elapsed_seconds':round(time.monotonic()-start,4),
            'coordinate_labels':('a','c','b','v','w'),'point_labels':LABELS,
            'point_vectors':POINTS,'target':TARGET,'rivals':len(rivals),
            'cases':len(outcomes),'certified':sum(o['certificate'] is not None for o in outcomes),
            'survivors':[o for o in outcomes if o['certificate'] is None],
            'negative_tests':tests,'outcomes':outcomes}
    local_path=Path(__file__).with_name('stage17_local_results.json')
    if local_path.exists():
        result['local_certificate_audit']=audit_local_results(local_path)
    output=Path(__file__).with_name('stage17_independent_results.json')
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('outcomes','point_vectors')},indent=2))

if __name__=='__main__': main()
