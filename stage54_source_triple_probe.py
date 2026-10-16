"""Can a genuine quintic split use a three-ordinary quartic source?

This is a fixed symbolic question tied to the full weighted inequality.
No residues, moduli, or group parameters are searched. Positive witnesses
only; a small growth bound or a discovery timeout is inconclusive.
"""
from fractions import Fraction
from itertools import combinations
from math import lcm
from pathlib import Path
import json
import time

from stage53_connected_split_probe import CENTRAL, V, word, diff, normal, ALLWORDS, SQUAREFREE


def dyadic_parameterization(rows):
    """Surjective model over any odd group, using only unit pivots."""
    mat=[list(map(Fraction,r[:7])) for r in rows]
    remaining=set(range(7)); pivots=[]; k=0
    while k<len(mat):
        choices=[]
        for i in range(k,len(mat)):
            for c in remaining:
                v=mat[i][c]
                if v and abs(v.numerator)&(abs(v.numerator)-1)==0 and v.denominator&(v.denominator-1)==0:
                    choices.append((abs(v),c,i))
        if not choices:
            break
        _,c,i=min(choices)
        mat[k],mat[i]=mat[i],mat[k]
        pivot=mat[k][c]
        mat[k]=[v/pivot for v in mat[k]]
        for i in range(len(mat)):
            if i!=k and mat[i][c]:
                factor=mat[i][c]
                mat[i]=[v-factor*w for v,w in zip(mat[i],mat[k])]
        remaining.remove(c); pivots.append(c); k+=1
    if any(any(r) for r in mat[k:]):
        return None
    free=sorted(remaining)
    coords=[[Fraction(int(i==f)) for f in free] for i in range(7)]
    for row,c in enumerate(pivots):
        coords[c]=[-mat[row][f] for f in free]
    coords.append([Fraction(0) for _ in free])
    scale=lcm(*(v.denominator for r in coords for v in r))
    assert scale>0 and scale&(scale-1)==0
    return {'rows':tuple(tuple(int(v*scale) for v in r) for r in coords),
            'free_labels':free,'scale':scale,'pivots':pivots,
            'rref':[[[v.numerator,v.denominator] for v in r] for r in mat[:k]]}


def general_exclusion(rows):
    value,certificate,rank,_=normal(rows)
    for i,j in combinations(V,2):
        target=tuple(int(v==i)-int(v==j) for v in V)
        cert=certificate(target)
        if cert:
            return {'kind':'label_collision','labels':(i,j),**cert}
    for degree in (2,3,4):
        groups={}
        for w in ALLWORDS[degree]:
            groups.setdefault(value(w),[]).append(w)
        for sf in SQUAREFREE[degree]:
            for w in groups[value(sf)]:
                if sf!=w:
                    cert=certificate(diff(sf,w))
                    if cert:
                        return {'kind':'protected_collision','degree':degree,'squarefree':sf,'other':w,**cert}
    original=(1,)*8; target=value(original)
    for w in ALLWORDS[8]:
        if w!=original and value(w)==target:
            cert=certificate(diff(w,original))
            if cert:
                return {'kind':'mass_eight_rival','word':w,**cert}
    for degree in (4,5):
        groups={}
        for c in V:
            for tail in combinations(set(V)-{c},degree-2):
                w=word(c,tail)
                groups.setdefault(value(w),[]).append(w)
        for group in groups.values():
            if len(group)<4:
                continue
            for words in combinations(group,4):
                certs=[certificate(diff(words[0],w)) for w in words[1:]]
                if all(certs):
                    return {'kind':'ordinary_cap_four','degree':degree,'words':words,'identities':certs}
    return None


def main():
    from stage43_relation_growth import run
    started=time.monotonic(); records=[]
    source=CENTRAL['sources'][0][0]
    for tail in combinations((1,3,4,6,7),2):
        third=word(5,tail)
        rows=CENTRAL['rows']+(diff(source,third),)
        exclusion=general_exclusion(rows)
        item={'tail':tail,'relations':rows,'exclusion':exclusion}
        if exclusion is None:
            parameter=dyadic_parameterization(rows)
            item['parameterization']=parameter
            if parameter:
                model={'id':'s54_source_'+''.join(map(str,tail)), 'direction':[],
                       'rows':parameter['rows'],'torsion_rows':(0,)*8,'torsion_order':1,
                       'parameterization':'Dyadic unit pivots, free labels and scale recorded; complete odd-group coverage.'}
                result=run(model,4,89,[2])
                old=Path(result['certificate']); dest=Path(old.name.replace('stage43_s54_','stage54_'))
                old.rename(dest); result['certificate']=dest.name
                item['growth']=result
        records.append(item)
        print(json.dumps({k:v for k,v in item.items() if k not in ('relations','parameterization')}),flush=True)
    result={'scope':'All ten possible third ordinary words centered at the added label of a genuine split source.',
            'records':records,'elapsed':time.monotonic()-started,
            'boundary':'Only displayed positive bounds/exclusions are proved; no modulus search or timeout premise.'}
    Path('stage54_source_triple_results.json').write_text(json.dumps(result,indent=2)+'\n')


if __name__=='__main__':
    main()
