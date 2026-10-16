"""Independent reconstruction and direct integer audit of bounded pure roles."""
import json
from pathlib import Path
from time import monotonic

def main():
    start=monotonic()
    data=json.loads(Path('stage21_pure_path_results.json').read_text()); assert data['completion']=='COMPLETE'
    expected={('FOO',(a,b)) for a in range(8) for b in range(8) if a!=b}|{('FOP',(a,)) for a in range(8)}
    seen=set(); count=0; survivors=[]
    for entry in data['records']:
        if monotonic()-start>30: raise TimeoutError('Pure role audit incomplete')
        shape,roles=entry['shape'],entry['roles']; key=shape,tuple(roles)
        assert key in expected and key not in seen; seen.add(key)
        rows=[[-3,1,2,0,0,0,0,0],[-4,1,0,2,1,0,0,0] if shape=='FOO' else [-4,1,0,3,0,0,0,0]]
        row=[0]*8
        if shape=='FOO':
            row[1]=2; row[0]=-2; row[roles[0]]-=1; row[roles[1]]+=1
        else:
            row[0]=6; row[3]=-5; row[roles[0]]-=1
        rows.append(row); assert rows==entry['rows']
        c=entry['certificate']
        if c is None:
            survivors.append({'shape':shape,'roles':roles,'rows':rows}); continue
        v,z,d=c['rival'],c['coefficients'],c['multiplier']
        assert len(v)==8 and sum(v)==8 and min(v)>=0 and v!=[1]*8
        assert type(d)==int and d>0 and not d&(d-1) and all(type(x)==int for x in z)
        assert all(d*(v[j]-1)==sum(a*r[j] for a,r in zip(z,rows)) for j in range(8))
        assert any(2*d*(v[j]-1)!=sum(a*r[j] for a,r in zip(z,rows)) for j in range(8))
        count+=1
    assert seen==expected
    result={'completion':'COMPLETE','seconds_limit':30,'elapsed_seconds':monotonic()-start,
            'coverage':len(seen),'certificates_verified':count,'altered_multipliers_rejected':count,
            'uncertified_presentations':survivors,
            'limit':'Only saved exclusions audited. Survivor realizability and absence of other certificates are not asserted.'}
    Path('stage21_pure_independent_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print('COMPLETE:',count,'identities;',len(survivors),'uncertified roles preserved')

if __name__=='__main__': main()
