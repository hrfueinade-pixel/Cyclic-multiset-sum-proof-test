"""Separate construction of all 88 endpoint-opponent roles; no producer imports."""
from itertools import product
import json
from pathlib import Path
from time import monotonic

def build():
    # Explicit coefficient rows avoid the producer's incidence generator.
    families={
      'isolatedO':([[-1,0,2,1,0,0,0,0],[0,0,0,0,2,1,1,0]],None),
      'FO':([[-1,0,2,1,0,0,0,0],[0,0,0,0,4,0,0,0],[0,0,0,0,1,2,1,0]],None),
      'PO':([[-1,0,2,1,0,0,0,0],[0,0,0,0,3,1,0,0],[0,0,0,0,0,1,2,1]],None)}
    first=[3,1,0,0,0,0,0,0]
    def delta(a,c,u,v):
        r=[0]*8; r[a]+=2; r[c]-=2; r[u]-=1; r[v]+=1
        return r
    for shape,(raw,_) in families.items():
        # First row above is already coreO-coreP; others are vertices.
        base=[raw[0]]+[[v[j]-first[j] for j in range(8)] for v in raw[1:]]
        # Correct literal core row: 2c+b+q - (3a+b).
        base[0]=[-3,0,2,1,0,0,0,0]
        domains=[]; names=[]
        if shape=='isolatedO':
            domains=[[(r,delta(4,0,r[0],r[1])) for r in product((5,6),(1,))],
                     [(r,delta(4,2,r[0],r[1])) for r in product((5,6),(1,3))]]
            names=[['double_centers',2,0],['double_centers',2,1]]
        elif shape=='FO':
            # Iteration order is the increasing vertex-pair order.
            forced=[]
            for k in range(8):
                r=[0]*8; r[4]=6; r[0]=-5; r[k]-=1
                forced.append(((k,),r))
            domains=[forced,[(r,delta(5,0,r[0],r[1])) for r in product((4,6),(1,))],
                     [(r,delta(5,2,r[0],r[1])) for r in product((4,6),(1,3))]]
            names=[['forced_point',2,0],['double_centers',3,0],['double_centers',3,1]]
        else:
            base.append([-5,0,0,0,5,0,0,0])
            domains=[[(r,delta(4,2,r[0],r[1])) for r in product((5,),(1,3))],
                     [(r,delta(6,0,r[0],r[1])) for r in product((5,7),(1,))],
                     [(r,delta(6,2,r[0],r[1])) for r in product((5,7),(1,3))]]
            names=[['double_centers',2,1],['double_centers',3,0],['double_centers',3,1]]
        for choices in product(*domains):
            yield (shape,tuple(r for r,_ in choices)),base+[r for _,r in choices],names

def valid(rows,c):
    if c is None: return False
    v,z,d=c['rival'],c['coefficients'],c['multiplier']
    if len(v)!=8 or sum(v)!=8 or v==[1]*8 or any(type(x)!=int or x<0 for x in v): return False
    if type(d)!=int or d<=0 or d&(d-1) or len(z)!=len(rows) or any(type(x)!=int for x in z): return False
    return all(d*(v[j]-1)==sum(a*r[j] for a,r in zip(z,rows)) for j in range(8))

def main():
    start=monotonic()
    expected={k:(r,n) for k,r,n in build()}
    data=json.loads(Path('stage23_endpoint_results.json').read_text()); assert data['completion']=='COMPLETE'
    seen=set(); rejected=0
    for entry in data['records']:
        if monotonic()-start>30: raise TimeoutError('Endpoint audit incomplete')
        key=entry['shape'],tuple(map(tuple,entry['roles']))
        assert key in expected and key not in seen; seen.add(key)
        rows,names=expected[key]
        assert entry['rows']==rows and entry['domain_names']==names
        assert valid(rows,entry['certificate'])
        bad=dict(entry['certificate']); bad['multiplier']*=2
        assert not valid(rows,bad); rejected+=1
        bad=dict(entry['certificate']); bad['coefficients']=[float(x) for x in bad['coefficients']]
        assert not valid(rows,bad); rejected+=1
    assert seen==set(expected)
    result={'completion':'COMPLETE','seconds_limit':30,'elapsed_seconds':monotonic()-start,
            'branches_verified':len(seen),'corruptions_rejected':rejected,
            'per_shape':{s:sum(k[0]==s for k in seen) for s in ('isolatedO','FO','PO')}}
    Path('stage23_endpoint_independent_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__': main()
