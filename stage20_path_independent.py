"""Separate path coverage reconstruction and integer witness audit."""
from itertools import product
import json
from pathlib import Path
from time import monotonic

def identity(rows,c):
    if c is None: return False
    v,z,d=c['rival'],c['coefficients'],c['multiplier']
    if len(v)!=8 or sum(v)!=8 or v==[1]*8 or any(type(x)!=int or x<0 for x in v): return False
    if type(d)!=int or d<=0 or d&(d-1) or len(z)!=len(rows) or any(type(x)!=int for x in z): return False
    return all(d*(v[j]-1)==sum(a*r[j] for a,r in zip(z,rows)) for j in range(8))

def cases():
    for L in range(4,9):
        for letters in product(('O','P','Q','F'),repeat=L):
            w=''.join(letters)
            if w>w[::-1] or w.count('P')>2 or w.count('Q')>1 or w.count('F')>1: continue
            if 'F' in w:
                f=w.index('F')
                if f not in (0,L-1) or 'Q' in w or w[1 if f==0 else L-2]!='O': continue
            if 'Q' in w:
                q=w.index('Q')
                if any(abs(i-q)!=1 for i,t in enumerate(w) if t=='P'): continue
            size=L-1+w.count('O')+int(w[0]!='F')+int(w[-1]!='F')
            if size>8: continue
            p_indices=[i for i in range(1,L-1) if w[i]=='P']
            for bits in product((0,1),repeat=len(p_indices)):
                next_free=L-1; verts=[]; center={}
                for i,t in enumerate(w):
                    v=[0]*8
                    incident=([0] if i==0 else [L-2] if i==L-1 else [i-1,i])
                    if t=='F':
                        v[incident[0]]=4
                    elif t=='P' and i in (0,L-1):
                        center[i]=next_free; next_free+=1
                        v[center[i]]=3; v[incident[0]]=1
                    else:
                        if len(incident)==1:
                            incident.append(next_free); next_free+=1
                        if t=='Q':
                            for k in incident: v[k]=2
                        else:
                            if t=='O':
                                center[i]=next_free; next_free+=1
                            else:
                                center[i]=incident[bits[p_indices.index(i)]]
                            v[center[i]]+=2
                            for k in incident: v[k]+=1
                    verts.append(v)
                assert next_free==size
                supports=[{i for i,x in enumerate(v) if x} for v in verts]
                if any(supports[i]&supports[j] != ({j} if i==j+1 else set()) for i in range(L) for j in range(i)): continue
                if any(center[i] in supports[j] for i,t in enumerate(w) if t=='P' for j,s in enumerate(w) if s=='Q'): continue
                rows=[[v[j]-verts[0][j] for j in range(8)] for v in verts[1:]]
                domains=[]; pairs=[]
                for i in range(L):
                    for j in range(i):
                        if w[i] not in ('O','P') or w[j] not in ('O','P') or supports[i]&supports[j]: continue
                        a,c=center[i],center[j]
                        if w[i]==w[j]=='P':
                            row=[0]*8; row[a]=5; row[c]-=5; rows.append(row)
                        else:
                            choices=[]
                            for u in sorted(supports[i]-{a}):
                                for v in sorted(supports[j]-{c}):
                                    row=[0]*8; row[a]+=2; row[c]-=2; row[u]-=1; row[v]+=1
                                    choices.append(((u,v),row))
                            domains.append(choices); pairs.append([i,j])
                for choices in product(*domains):
                    yield (w,bits,tuple(r for r,_ in choices)),verts,rows+[r for _,r in choices],pairs,size

def main():
    start=monotonic()
    expected={k:(v,r,p,s) for k,v,r,p,s in cases()}
    data=json.loads(Path('stage20_path_results.json').read_text()); assert data['completion']=='COMPLETE'
    seen=set(); rejected=0
    for record in data['records']:
        if monotonic()-start>30: raise TimeoutError('Independent path audit incomplete')
        key=record['word'],tuple(record['orientation']),tuple(map(tuple,record['roles']))
        assert key not in seen and key in expected; seen.add(key)
        v,r,p,s=expected[key]
        assert record['vertices']==v and record['rows']==r and record['domain_pairs']==p and record['support_size']==s
        assert identity(r,record['certificate'])
        bad=dict(record['certificate']); bad['multiplier']*=2
        assert not identity(r,bad); rejected+=1
        bad=dict(record['certificate']); bad['coefficients']=[float(x) for x in bad['coefficients']]
        assert not identity(r,bad); rejected+=1
    assert seen==set(expected)
    result={'completion':'COMPLETE','seconds_limit':30,'elapsed_seconds':monotonic()-start,
            'branches_verified':len(seen),'corruptions_rejected':rejected,
            'word_counts':{w:sum(k[0]==w for k in seen) for w in sorted({k[0] for k in seen})}}
    Path('stage20_path_independent_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__': main()
