"""Reconstruct incidence coverage and audit all identities, no producer imports."""
from itertools import product
import json
from pathlib import Path
from time import monotonic

WORDS=('QOOO','QPOO','PPOOO','POPOO','QPOOP','QPOOO')

def check(rows,c):
    if c is None:
        return False
    v=c['rival']; d=c['multiplier']; z=c['coefficients']
    if len(v)!=8 or any(type(x)!=int or x<0 for x in v) or sum(v)!=8 or v==[1]*8:
        return False
    if type(d)!=int or d<=0 or d&(d-1) or len(z)!=len(rows) or any(type(x)!=int for x in z):
        return False
    return all(d*(v[j]-1)==sum(a*r[j] for a,r in zip(z,rows)) for j in range(8))

def reconstruct(word):
    L=len(word)
    p=[i for i in range(L) if word[i]=='P']
    for orientation in product((0,1),repeat=len(p)):
        verts=[]; centers={}; private=L
        for i,kind in enumerate(word):
            v=[0]*8
            left=(i+L-1)%L; right=i
            if kind=='Q':
                v[left]=v[right]=2
            else:
                if kind=='O':
                    center=private; private+=1
                else:
                    center=(left,right)[orientation[p.index(i)]]
                centers[i]=center
                v[center]+=2; v[left]+=1; v[right]+=1
            verts.append(v)
        supports=[{i for i,k in enumerate(v) if k} for v in verts]
        if any((supports[i]&supports[j]) != ({j} if i==j+1 else {L-1} if i==L-1 and j==0 else set()) for i in range(L) for j in range(i)):
            continue
        if any(centers[i] in supports[j] for i in p for j in range(L) if word[j]=='Q'):
            continue
        rows=[[v[j]-verts[0][j] for j in range(8)] for v in verts[1:]]
        domains=[]; pairs=[]
        for i in range(L):
            for j in range(i):
                if word[i]=='Q' or word[j]=='Q' or supports[i]&supports[j]:
                    continue
                a,c=centers[i],centers[j]
                if word[i]==word[j]=='P':
                    r=[0]*8; r[a]+=5; r[c]-=5; rows.append(r)
                else:
                    options=[]
                    for u in sorted(supports[i]-{a}):
                        for v in sorted(supports[j]-{c}):
                            r=[0]*8; r[a]+=2; r[c]-=2; r[u]-=1; r[v]+=1
                            options.append(((u,v),r))
                    domains.append(options); pairs.append([i,j])
        for options in product(*domains):
            yield (word,orientation,tuple(x[0] for x in options)), verts,rows+[x[1] for x in options],pairs

def main():
    start=monotonic()
    data=json.loads(Path('stage19_cycle_results.json').read_text())
    assert data['completion']=='COMPLETE'
    expected={k:(v,r,p) for w in WORDS for k,v,r,p in reconstruct(w)}
    seen=set(); rejected=0
    for entry in data['records']:
        if monotonic()-start>30:
            raise TimeoutError('Audit incomplete')
        key=(entry['word'],tuple(entry['orientation']),tuple(map(tuple,entry['roles'])))
        assert key in expected and key not in seen
        seen.add(key)
        verts,rows,pairs=expected[key]
        assert entry['vertices']==verts and entry['rows']==rows and entry['domain_pairs']==pairs
        assert check(rows,entry['certificate'])
        damaged=dict(entry['certificate'])
        damaged['coefficients']=list(damaged['coefficients'])
        # Alter the multiplier instead of a potentially zero relation row.
        damaged['multiplier']*=2
        assert not check(rows,damaged); rejected+=1
        damaged=dict(entry['certificate']); damaged['coefficients']=[float(x) for x in damaged['coefficients']]
        assert not check(rows,damaged); rejected+=1
    assert seen==set(expected)
    result={'completion':'COMPLETE','seconds_limit':30,'elapsed_seconds':monotonic()-start,
            'coverage_reconstructed':len(expected),'identities_verified':len(seen),
            'corruptions_rejected':rejected,'per_word':{w:sum(k[0]==w for k in seen) for w in WORDS}}
    Path('stage19_cycle_independent_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    main()
