"""All orientations of six long-cycle words; dyadic certificates only."""
import argparse
from fractions import Fraction
from itertools import product
import json
from math import lcm
from pathlib import Path
from time import monotonic

WORDS=('QOOO','QPOO','PPOOO','POPOO','QPOOP','QPOOO')

def e(i):
    return tuple(int(j==i) for j in range(8))

def lin(*terms):
    return tuple(sum(c*v[j] for c,v in terms) for j in range(8))

def compositions(n,k):
    if k==1:
        yield (n,)
    else:
        for x in range(n+1):
            for tail in compositions(n-x,k-1):
                yield (x,)+tail

def find(rows,candidates):
    # RREF rows augmented by their combination coefficients.
    m=len(rows)
    matrix=[[Fraction(x) for x in row]+[Fraction(int(i==j)) for j in range(m)] for i,row in enumerate(rows)]
    pivots=[]
    for j in range(8):
        r=len(pivots)
        p=next((k for k in range(r,m) if matrix[k][j]),None)
        if p is None:
            continue
        matrix[r],matrix[p]=matrix[p],matrix[r]
        a=matrix[r][j]
        matrix[r]=[x/a for x in matrix[r]]
        for k in range(m):
            if k!=r and matrix[k][j]:
                a=matrix[k][j]
                matrix[k]=[x-a*y for x,y in zip(matrix[k],matrix[r])]
        pivots.append(j)
        if len(pivots)==m:
            break
    # Scale each transformation once for fast integer candidate tests.
    transforms=[]
    for row in matrix[:len(pivots)]:
        den=lcm(*(x.denominator for x in row))
        transforms.append((tuple(int(x*den) for x in row),den))
    for counts in candidates:
        v=tuple(x-1 for x in counts)
        den=lcm(*(d for _,d in transforms))
        residual=[den*x for x in v]
        coeff=[0]*m
        for pivot,(row,d) in zip(pivots,transforms):
            a=residual[pivot]
            # residual is kept over denominator den; pivot row normalized.
            if a:
                if a%d:
                    # Rational fallback for this candidate.
                    break
                residual=[x-(a//d)*y for x,y in zip(residual,row[:8])]
                coeff=[x+(a//d)*y for x,y in zip(coeff,row[8:])]
        else:
            if any(residual):
                continue
            g=den
            from math import gcd
            for z in coeff:
                g=gcd(g,z)
            multiplier=den//g
            coeff=[z//g for z in coeff]
            if multiplier & (multiplier-1):
                continue
            assert all(multiplier*v[j]==sum(z*r[j] for z,r in zip(coeff,rows)) for j in range(8))
            return {'rival':counts,'multiplier':multiplier,'coefficients':coeff}
        # General exact solve if integer-scaled elimination was not enough.
        residual=[Fraction(x) for x in v]
        coeff=[Fraction(0)]*m
        for p,row in zip(pivots,matrix):
            a=residual[p]
            residual=[x-a*y for x,y in zip(residual,row[:8])]
            coeff=[x+a*y for x,y in zip(coeff,row[8:])]
        if any(residual):
            continue
        den=lcm(*(x.denominator for x in coeff))
        if den & (den-1):
            continue
        ints=[int(x*den) for x in coeff]
        assert all(den*v[j]==sum(z*r[j] for z,r in zip(ints,rows)) for j in range(8))
        return {'rival':counts,'multiplier':den,'coefficients':ints}
    return None

def models(word):
    L=len(word)
    ps=[i for i,t in enumerate(word) if t=='P']
    for orient in product((0,1),repeat=len(ps)):
        centers={}
        private=L
        vertices=[]
        for i,t in enumerate(word):
            prev=(i-1)%L
            if t=='Q':
                vertices.append(lin((2,e(prev)),(2,e(i))))
                continue
            if t=='O':
                centers[i]=private
                private+=1
            else:
                centers[i]=prev if orient[ps.index(i)]==0 else i
            vertices.append(lin((2,e(centers[i])),(1,e(prev)),(1,e(i))))
        supports=[{j for j,x in enumerate(v) if x} for v in vertices]
        if any(bool(supports[i]&supports[j]) != ((i-j)%L in (1,L-1)) for i in range(L) for j in range(i)):
            continue
        # A P adjacent to Q must meet it at its singleton, not its center.
        if any(word[j]=='Q' and centers[i] in supports[j] for i in ps for j in range(L)):
            continue
        base=[lin((1,v),(-1,vertices[0])) for v in vertices[1:]]
        domains=[]
        names=[]
        for i in range(L):
            for j in range(i):
                if word[i]=='Q' or word[j]=='Q' or supports[i]&supports[j]:
                    continue
                a,c=centers[i],centers[j]
                diff=lin((2,e(a)),(-2,e(c)))
                if word[i]==word[j]=='P':
                    base.append(lin((5,e(a)),(-5,e(c))))
                    continue
                if word[i]==word[j]=='O':
                    tails_i=sorted(supports[i]-{a})
                    tails_j=sorted(supports[j]-{c})
                else:
                    # Positive endpoint on the P side must be its singleton;
                    # the center choice gives a forbidden squarefree pair.
                    if word[i]=='P':
                        tails_i=sorted(supports[i]-{a})
                        tails_j=sorted(supports[j]-{c})
                    else:
                        tails_i=sorted(supports[i]-{a})
                        tails_j=sorted(supports[j]-{c})
                roles=[(u,v) for u in tails_i for v in tails_j]
                domains.append([(role,lin((1,diff),(-1,e(role[0])),(1,e(role[1])))) for role in roles])
                names.append([i,j])
        yield {'word':word,'orientation':orient,'vertices':vertices,'support_size':private,
               'centers':centers,'base_rows':base,'domains':domains,'domain_pairs':names}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--seconds',type=float,default=60)
    args=ap.parse_args()
    start=monotonic()
    candidates=tuple(c for c in compositions(8,8) if c!=(1,)*8)
    records=[]
    complete=True
    for word in WORDS:
        for model in models(word):
            for roles in product(*model['domains']):
                if monotonic()-start>args.seconds:
                    complete=False
                    break
                rows=model['base_rows']+[row for _,row in roles]
                witness=find(rows,candidates)
                records.append({'word':word,'orientation':model['orientation'],
                                'roles':[r for r,_ in roles], 'domain_pairs':model['domain_pairs'],
                                'vertices':model['vertices'],'support_size':model['support_size'],
                                'rows':rows,'certificate':witness})
            if not complete:
                break
        if not complete:
            break
    result={'completion':'COMPLETE' if complete else 'TIMEOUT','seconds_limit':args.seconds,
            'elapsed_seconds':monotonic()-start,'records':records}
    Path('stage19_cycle_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(result['completion'],result['elapsed_seconds'])
    for word in WORDS:
        local=[r for r in records if r['word']==word]
        print(word,len(local),'branches;',sum(r['certificate'] is None for r in local),'symbolic survivors')

if __name__=='__main__':
    main()
