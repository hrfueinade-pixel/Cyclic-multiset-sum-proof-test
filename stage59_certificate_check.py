"""Standalone exact checker for the triangle split lemma and forest corollary.

Standard library only; imports no producer or earlier checker. Coverage
uses ordered physical frames. The growth prototype solves a coefficient-
one equation directly, so no integer normal-form reduction or odd cancellation is used.
The program performs no witness search, parameter scan or modulus scan.
"""
from collections import Counter
from itertools import combinations,permutations
from pathlib import Path
import gzip,hashlib,json

BASE=((1,0,0,0,0),(2,0,0,0,0),(0,1,0,0,0),(0,2,0,0,0),
      (0,0,1,0,0),(0,0,2,0,0),(0,0,0,1,0),(0,0,0,0,1))
# p=w+2r is an exact surjective parameterization over every abelian group.
GROWTH=((1,0,0,0),(2,0,0,0),(0,1,0,0),(0,2,0,0),
        (0,0,1,0),(0,0,2,0),(0,0,1,2),(0,0,0,1))
ONES=(1,)*8


def word(w,d):
    assert len(w)==8 and all(isinstance(x,int) and x>=0 for x in w) and sum(w)==d


def counts(labels):return tuple(labels.count(i) for i in range(8))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def val(w,rows=BASE):return tuple(sum(w[i]*rows[i][j] for i in range(8)) for j in range(len(rows[0])))
def unit2(x):return isinstance(x,int) and x>0 and x&(x-1)==0


def multiple(a,b):
    j=next(i for i,x in enumerate(b) if x)
    assert a[j]%b[j]==0
    k=a[j]//b[j]
    assert a==tuple(k*x for x in b)


def coverage():
    # Four positions left after the fixed cubic descent. Tail order is irrelevant.
    result={}
    for z,b,d,e in permutations((4,5,6,7)):
        W=(counts((0,0,3,d,e)),counts((2,2,1,d,e)),counts((z,z,1,b,3)))
        key=(z,b)
        if key in result:assert result[key]==W
        result[key]=W
    assert len(result)==12
    return result


def check_local(data):
    expected=coverage();seen=set();kinds=Counter()
    for rec in data['cases']:
        key=(rec['third'],rec['middle']);assert key in expected and key not in seen;seen.add(key)
        W=tuple(tuple(w) for w in rec['words']);assert W==expected[key]
        for w in W:word(w,5)
        assert val(sub(W[0],W[1]))==(0,)*5
        K=val(sub(W[0],W[2]));assert any(K)
        proof=rec['proof'];kind=proof['kind'];kinds[kind]+=1
        if kind=='label':
            i,j=proof['labels'];assert 0<=i<8 and 0<=j<8 and i!=j
            multiple(val(tuple(int(a==i)-int(a==j) for a in range(8))),K)
        elif kind=='protected':
            d=proof['degree'];a=tuple(proof['squarefree']);b=tuple(proof['other'])
            assert d in (2,3,4);word(a,d);word(b,d);assert max(a)==1 and a!=b
            multiple(val(sub(a,b)),K)
        elif kind=='rival':
            r=tuple(proof['word']);word(r,8);assert r!=ONES
            multiple(val(sub(r,ONES)),K)
        elif kind=='growth89':
            assert key in ((6,5),(7,5)) and proof['swap_free_labels']==(key==(6,5))
            swap=proof['swap_free_labels']
            target=(0,0,-1,-2,1) if swap else (0,0,-1,1,-2)
            multiple(target,K)
        elif kind=='residual':
            assert key in ((6,7),(7,6))
            target=(0,0,3,-2,-1) if key==(6,7) else (0,0,3,-1,-2)
            multiple(target,K)
        else:raise AssertionError(kind)
    assert seen==set(expected)
    assert kinds=={'protected':4,'label':2,'rival':2,'growth89':2,'residual':2}
    return kinds


def check_growth(data):
    assert data['prototype']=='p=w+2r'
    Q=data['positive'];W=[tuple(w) for w in Q['words']]
    assert len(W)==89 and len(set(W))==89 and len(Q['pairs'])==3916
    for w in W:word(w,4);assert max(w)>1
    for (i,j),(r,k,factor) in zip(combinations(range(89),2),Q['pairs']):
        r=tuple(r);word(r,8);assert r!=ONES and isinstance(k,int) and unit2(factor)
        R=val(sub(r,ONES),GROWTH);D=val(sub(W[i],W[j]),GROWTH)
        assert tuple(factor*x for x in R)==tuple(k*x for x in D)
    return 3916


def residual_pairs():
    candidates=[(i,s) for i in (0,2,4) for s in (0,1)]
    K={(i,s):val(tuple(3*int(j==i)-(2-s)*int(j==6)-(1+s)*int(j==7) for j in range(8)))
       for i,s in candidates}
    checked=Counter()
    for (i,s),(j,t) in combinations(candidates,2):
        if s==t:
            a=counts((i,i+1));b=counts((j,j+1))
            assert i!=j and max(a)==max(b)==1
            assert val(sub(a,b))==sub(K[i,s],K[j,t])
            checked['protected_pair']+=1
        elif i==j:
            a=counts((6,));b=counts((7,))
            delta=sub(K[i,s],K[j,t]);multiple(val(sub(a,b)),delta)
            checked['label']+=1
        else:
            # Choose i as the center with equation 3xi=2p+r.
            if s==1:i,j=j,i
            k=next(a for a in (0,2,4) if a not in (i,j))
            rival=counts((k,k+1,i,i,i+1,i+1,7,7))
            word(rival,8);assert rival!=ONES
            assert val(sub(rival,ONES))==sub(K[i,0],K[j,1])
            checked['mass8_rival']+=1
    assert checked=={'protected_pair':6,'label':3,'mass8_rival':6}
    return checked


def partitions(n,maximum=None):
    if n==0:
        yield ()
        return
    for first in range(min(n,maximum or n),0,-1):
        for rest in partitions(n-first,first):yield (first,)+rest


def forest_table():
    rows=[]
    for shape in partitions(8):
        edges=[];start=0
        for size in shape:
            edges.extend((i,i+1) for i in range(start,start+size-1));start+=size
        def matching(indices):return len({v for i in indices for v in edges[i]})==2*len(indices)
        matchings={r:[I for I in combinations(range(len(edges)),r) if matching(I)] for r in (2,3,4)}
        if not matchings[3] or matchings[4]:continue
        P=len(matchings[2]);t=len(matchings[3]);J=sum(max(size-2,0) for size in shape)
        D={pair for tri in matchings[3] for pair in combinations(tri,2)}
        Q=4*(P-len(D))+t
        lower=288-Q-2*P-2*t
        assert lower>=248
        rows.append({'shape':shape,'ordinary_pairs':P,'pure_pairs':J,'triangles':t,
                     'triangle_incident_pairs':len(D),'split_upper':Q,'N_lower':lower,
                     'external_deficit_rhs':lower-247,
                     'minimum_external_ordinary_pairs':(lower-247+5)//6})
    expected={(2,2,2,1,1),(4,2,1,1),(3,2,2,1),(6,1,1),(5,2,1),(4,3,1),(3,3,2),(7,1),(5,3)}
    assert {r['shape'] for r in rows}==expected and len(rows)==9
    return rows


def main():
    path=Path(__file__).with_name('stage59_one_split_certificates.json.gz')
    raw=path.read_bytes();data=json.loads(gzip.decompress(raw))
    result={'scope':'One split per triangle and all nine ordinary-collision-exhausted forest families.',
            'archive_sha256':hashlib.sha256(raw).hexdigest(),
            'local_cases':dict(check_local(data)),'positive_quartic_values':89,
            'positive_mass8_identities':check_growth(data),
            'residual_pairs':dict(residual_pairs()),'forest_table':forest_table(),
            'full_N_ge_248':'OPEN','certification':'Separate implementation by the same assistant; not formal or external review.'}
    dest=Path(__file__).with_name('stage59_check_results.json')
    dest.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))


if __name__=='__main__':main()
