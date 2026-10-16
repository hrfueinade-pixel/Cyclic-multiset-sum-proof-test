"""Standalone exact checker for the six large-forest exclusions.

Standard library only. No producer, elimination or prior checker imports.
Private pair coverage is built from the 56 ordinary cubic words rather
than the producer's ordered four-label frames. No discovery is performed.
"""
from collections import Counter,defaultdict
from itertools import combinations
from pathlib import Path
import gzip,hashlib,json

BASE=((1,0,0,0,0),(2,0,0,0,0),(0,1,0,0,0),(0,2,0,0,0),
      (0,0,1,0,0),(0,0,2,0,0),(0,0,0,1,0),(0,0,0,0,1))
K0={'332':[[-4,0,0,1,0],[0,-4,0,0,1]],
    '521':[[-4,1,0,0,0],[-16,0,0,1,0]],
    '431':[[-4,1,0,0,0],[0,0,-4,0,1]],
    '611':[[-4,1,0,0,0],[-16,0,1,0,0]]}
FREE={'332':((1,0,0),(2,0,0),(0,1,0),(0,2,0),(0,0,1),(0,0,2),(4,0,0),(0,4,0)),
      '521':((1,0,0),(2,0,0),(4,0,0),(8,0,0),(0,1,0),(0,2,0),(16,0,0),(0,0,1)),
      '431':((1,0,0),(2,0,0),(4,0,0),(8,0,0),(0,1,0),(0,2,0),(0,0,1),(0,4,0)),
      '611':((1,0,0),(2,0,0),(4,0,0),(8,0,0),(16,0,0),(32,0,0),(0,1,0),(0,0,1))}
ONES=(1,)*8


def archive_bytes(path):
    if path.exists():return path.read_bytes()
    pieces=sorted(path.parent.glob(path.name+'.part*'))
    assert pieces and [p.name for p in pieces]==[path.name+'.part'+str(i).zfill(3)for i in range(len(pieces))]
    return b''.join(p.read_bytes()for p in pieces)


def counts(labels):return tuple(labels.count(i)for i in range(8))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def unit2(x):return isinstance(x,int)and x>0 and x&(x-1)==0
def val(w,M):return tuple(sum(w[i]*M[i][j]for i in range(8))for j in range(len(M[0])))
def word(w,d):assert len(w)==8 and all(isinstance(x,int)and x>=0 for x in w)and sum(w)==d
def ordinary(w,d):word(w,d);assert w.count(2)==1 and max(w)==2 and w.count(1)==d-2
def mul(a,b):return [[sum(x*y for x,y in zip(r,c))for c in zip(*b)]for r in a]


def determinant(M):
    A=[r[:]for r in M];n=len(A);sign=1;last=1
    if not n:return 1
    for p in range(n-1):
        if not A[p][p]:
            j=next((j for j in range(p+1,n)if A[j][p]),None)
            if j is None:return 0
            A[p],A[j]=A[j],A[p];sign=-sign
        z=A[p][p]
        for i in range(p+1,n):
            for j in range(p+1,n):
                q=A[i][j]*z-A[i][p]*A[p][j];assert q%last==0;A[i][j]=q//last
            A[i][p]=0
        last=z
    return sign*A[-1][-1]


def reduction(K,r):
    L=r['left'];V=r['right'];D=r['D'];rank=r['rank'];n=len(K)
    assert len(L)==n and all(len(row)==n for row in L)
    assert len(V)==5 and all(len(row)==5 for row in V)
    assert abs(determinant(L))==abs(determinant(V))==1
    assert mul(mul(L,K),V)==D and 0<rank<=min(n,5)
    for i,row in enumerate(D):
        for j,x in enumerate(row):assert x==0 if i!=j or i>=rank else x>0
    di=[D[i][i]for i in range(rank)];odd=[]
    for x in di:
        while x%2==0:x//=2
        odd.append(x)
    assert di==r['diagonals']and odd==r['odd_diagonals']


def forced(row,r):
    x=[sum(row[i]*r['right'][i][j]for i in range(5))for j in range(5)]
    return all(v==0 for v in x[r['rank']:])and all(x[i]%g==0 for i,g in enumerate(r['odd_diagonals']))


def check_model(m,r):
    T=mul(BASE,r['right']);rank=r['rank'];ti=[i for i,g in enumerate(r['odd_diagonals'])if g>1]
    assert m['rows']==[row[rank:]for row in T]
    assert m['torsion_orders']==[r['odd_diagonals'][i]for i in ti]
    assert m['torsion_matrix']==[[row[i]%r['odd_diagonals'][i]for i in ti]for row in T]


def evaluator(m):
    cache={}
    def value(w):
        w=tuple(w)
        if w not in cache:
            cache[w]=(val(w,m['rows']),tuple(sum(w[i]*m['torsion_matrix'][i][j]for i in range(8))%g
                                           for j,g in enumerate(m['torsion_orders'])))
        return cache[w]
    return value


def growth(proof,value,orders):
    W=[tuple(w)for w in proof['words']];assert len(W)==89 and len(set(W))==89 and len(proof['pairs'])==3916
    for w in W:word(w,4);assert max(w)>1
    for (i,j),(raw,k,f)in zip(combinations(range(89),2),proof['pairs']):
        R=tuple(raw);word(R,8);assert R!=ONES and isinstance(k,int)and unit2(f)
        rv=value(sub(R,ONES));a=value(W[i]);b=value(W[j])
        assert tuple(f*x for x in rv[0])==tuple(k*(x-y)for x,y in zip(a[0],b[0]))
        assert all((f*x-k*(y-z))%g==0 for x,y,z,g in zip(rv[1],a[1],b[1],orders))
    return 3916


def direct(e,value):
    kind=e['kind']
    zero=value((0,)*8)
    if kind=='model_label_collision':
        i,j=e['labels'];assert 0<=i<8 and 0<=j<8 and i!=j
        assert value(sub(counts((i,)),counts((j,))))==zero
    elif kind=='model_protected_collision':
        d=e['degree'];a=tuple(e['squarefree']);b=tuple(e['other']);assert d in (2,3,4)
        word(a,d);word(b,d);assert max(a)==1 and a!=b and value(a)==value(b)
    elif kind in ('model_cubic_cap4','model_ordinary_cap4'):
        d=3 if kind=='model_cubic_cap4'else e['degree'];assert d in (3,4,5)
        W=[tuple(w)for w in e['words']];assert len(W)==4 and len(set(W))==4
        for w in W:
            if kind=='model_cubic_cap4':word(w,3);assert max(w)>1
            else:ordinary(w,d)
        assert len({value(w)for w in W})==1
    elif kind=='model_split_source3':
        W=[tuple(w)for w in e['quintic_words']];assert len(W)==3 and len(set(W))==3
        for w in W:ordinary(w,5)
        assert len({value(w)for w in W})==1
        centers={w.index(2)for w in W};assert len(centers)==3
        tails=[{i for i,n in enumerate(w)if n==1}for w in W];assert all(not t&centers for t in tails)
        omitted=[set(range(8))-centers-t for t in tails]
        assert sorted(Counter(i for E in omitted for i in E).values())==[1,1,1,1,2]
        S=[tuple(w)for w in e['source_words']];third=tuple(e['third_word'])
        for w in S+[third]:ordinary(w,4)
        assert S[0]!=S[1]and third not in S and len({value(w)for w in S+[third]})==1
        assert not {i for i,n in enumerate(S[0])if n==1}&{i for i,n in enumerate(S[1])if n==1}
        found=False
        for i,j in combinations(range(3),2):
            common=tails[i]&tails[j]
            if len(common)==1:
                c=next(iter(common));U=[tuple(n-int(k==c)for k,n in enumerate(W[z]))for z in (i,j)]
                if set(U)==set(S):found=True
        assert found
        # Stage54: a genuine split source has exactly two ordinary words.
    elif kind=='cyclic_three_coset':
        a,b,c=e['labels'];assert len({a,b,c})==3
        for j in (b,c):assert value(tuple(3*(int(i==j)-int(i==a))for i in range(8)))==zero
        # Three distinct labels in one cyclic order-three coset sum to3a.
    elif kind=='alignment_cycle_bound':
        C=e['cycle'];assert 3<=len(C)<=8 and len(set(C))==len(C)
        colors=[value(tuple(2*int(k==C[i])-int(k==C[(i+1)%len(C)])for k in range(8)))for i in range(len(C))]
        assert len(set(colors))==1
        # Published Stage56 cycle/block saturation theorem excludes N<248.
    elif kind=='alignment_two_cycle_triangle':
        a,b=e['cycle'];E=e['extra_edges'];assert len(E)==2 and len({a,b}|set(E[0])|set(E[1]))==6
        edges=[(a,b),(b,a)]+E
        colors=[value(tuple(2*int(k==i)-int(k==j)for k in range(8)))for i,j in edges]
        assert len(set(colors))==1
        other=set(range(8))-{a,b,*E[0],*E[1]};assert len(other)==2
        R=counts((E[0][0],)*3+(E[1][0],)*3+tuple(other));word(R,8)
        assert R!=ONES and value(R)==value(ONES)
    else:raise AssertionError('Unsupported exclusion '+kind)


ORD=tuple(counts((i,i,j))for i in range(8)for j in range(8)if i!=j)


def direction(row):
    assert any(row);r=list(row)
    while all(x%2==0 for x in r):r=[x//2 for x in r]
    if next(x for x in r if x)<0:r=[-x for x in r]
    return tuple(r)


def coverage(value):
    answer=set();literal=0
    for a,b in combinations(ORD,2):
        labels={a.index(2),a.index(1),b.index(2),b.index(1)}
        if len(labels)!=4 or value(a)==value(b):continue
        literal+=1;answer.add(direction(val(sub(a,b),BASE)))
    return answer,literal


def long_path(data):
    M=tuple((1<<i,0)for i in range(7))+((0,1),);types=set();literal=0
    for a,b in combinations(ORD,2):
        if len({a.index(2),a.index(1),b.index(2),b.index(1)})!=4:continue
        A,B=val(sub(a,b),M)
        if not(A or B):continue
        literal+=1
        while A%2==B%2==0:A//=2;B//=2
        if B<0 or (B==0 and A<0):A=-A;B=-B
        types.add((A,B))
    assert literal==830 and len(types)==261
    seen=set();stats=Counter();pairs=0
    for rec in data:
        A,B=rec['relation'];assert(A,B)in types and(A,B)not in seen;seen.add((A,B));p=rec['proof'];kind=p['kind'];stats[kind]+=1
        if B==0:assert kind=='root_order'and 0<A<=156
        else:
            assert B in (1,2)
            rows=tuple((B*(1<<i),)for i in range(7))+((-A,),)
            value=lambda w:(val(w,rows),())
            if kind=='direct':direct(p['exclusion'],value)
            elif kind=='rival':
                R=tuple(p['word']);word(R,8);assert R!=ONES and value(R)==value(ONES)
            else:assert kind=='growth89';pairs+=growth(p,value,())
    assert seen==types
    # Explicit exceptional seven-coin rivals in the root-order hand lemma.
    for d,W in ((121,(0,0,2,0,1,1,3)),(123,(0,1,0,1,1,1,3)),(125,(0,0,1,1,1,1,3))):
        assert sum(W)==7 and sum(x*(1<<i)for i,x in enumerate(W))==127+d
    return stats,pairs


def main():
    path=Path(__file__).with_name('stage60_forest_certificates.json.gz');raw=archive_bytes(path);data=json.loads(gzip.decompress(raw))
    pairs=0;stats=Counter();coverage_cases=0;literal_cases=0;nodes=data['nodes'];done=set();visiting=set()
    M53=((1,0),(2,0),(4,0),(8,0),(16,0),(0,1),(0,2),(0,4))
    pairs+=growth(data['forest53'],lambda w:(val(w,M53),()),())
    ls,lp=long_path(data['long_path']);pairs+=lp
    def check_coverage(parentK,value,cases):
        nonlocal coverage_cases,literal_cases
        expected,literal=coverage(value);literal_cases+=literal;seen=set()
        for c in cases:
            d=tuple(c['direction']);assert d in expected and d not in seen;seen.add(d)
            K=parentK+[list(d)];r=c['reduction'];reduction(K,r)
            n=c['node'];assert isinstance(n,int)and 0<=n<len(nodes)
            assert all(forced(row,r)for row in nodes[n]['constraints'])
            check_node(n);coverage_cases+=1
        assert seen==expected
    def check_node(i):
        nonlocal pairs
        if i in done:return
        assert i not in visiting;visiting.add(i)
        node=nodes[i];K=node['constraints'];r=node['reduction'];m=node['model']
        reduction(K,r);check_model(m,r);value=evaluator(m);proof=node['proof'];kind=proof['kind'];stats[kind]+=1
        if kind=='direct':direct(proof['exclusion'],value)
        elif kind=='rival':
            R=tuple(proof['word']);word(R,8);assert R!=ONES and value(R)==value(ONES)
        elif kind=='growth89':pairs+=growth(proof,value,m['torsion_orders'])
        elif kind=='forced_ordinary':
            P=sum(value(a)==value(b)for a,b in combinations(ORD,2));assert P<=8
            # Stage58 proves every counterexample has P>=9, so a new ordinary pair is compulsory.
            check_coverage(K,value,proof['coverage'])
        else:raise AssertionError(kind)
        visiting.remove(i);done.add(i)
    assert set(data['forests'])==set(K0)
    counts={}
    for shape,forest in data['forests'].items():
        assert forest['base_constraints']==K0[shape]
        expected,literal=coverage(lambda w:val(w,FREE[shape]));counts[shape]={'private_cases':literal,'directions':len(expected)}
        check_coverage(K0[shape],lambda w:val(w,FREE[shape]),forest['coverage'])
    assert len(done)==len(nodes)
    result={'excluded_shapes':['53','71','332','521','431','611'],
            'remaining_shapes':['22211','4211','3221'],'archive_sha256':hashlib.sha256(raw).hexdigest(),
            'proof_nodes':len(done),'node_types':dict(stats),'long_path_types':dict(ls),
            'coverage_cases':coverage_cases,'literal_private_cases':literal_cases+830,
            'positive_mass8_pair_identities':pairs,'first_forest_coverage':counts,
            'full_N_ge_248':'OPEN','boundary':'Same-assistant separate implementation; depends on published caps, cycle theorem, source theorem and P>=9 theorem.'}
    dest=Path(__file__).with_name('stage60_check_results.json');dest.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))


if __name__=='__main__':main()
