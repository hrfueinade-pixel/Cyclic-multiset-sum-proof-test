"""Targeted simultaneous pairs of added-label-avoiding star companions.

Tests the fixed 52 words, never a modulus or parameter space. An edge is a
positive mass-eight rival consequence using only dyadic cancellation. Missing
edges are inconclusive. The formal model from the first word covers every odd
group; the second relation is kept as an integer vector.
"""
import itertools
import json
import math
import random
from pathlib import Path

from stage47_star_avoid_probe import count_words, value


def ray(v):
    g=math.gcd(*v)
    if next(x for x in v if x)<0:
        g=-g
    return tuple(x//g for x in v),g


def main():
    data=json.loads(Path('stage47_star_avoid_results.json').read_text())
    models=[m for m in data['models'] if not m['direct_rivals']]
    assert len(models)==46
    edges=[]
    for i,m in enumerate(models):
        rows=m['rows']
        target=value((1,)*8,rows)
        rays={}
        for c in count_words(8,8):
            if c==(1,)*8: continue
            diff=tuple(x-y for x,y in zip(value(c,rows),target))
            if any(diff):
                r,g=ray(diff)
                rays.setdefault(r,[]).append((g,c))
        for j in range(i+1,len(models)):
            other=models[j]['word_abcv']
            diff=tuple(2*(a-b) for a,b in zip(other,m['word_abcv']))
            factor=1
            while all(x%2==0 for x in diff):
                factor*=2
                diff=tuple(x//2 for x in diff)
            r,g=ray(diff)
            for scale,c in rays.get(r,[]):
                if scale%g==0:
                    edges.append({'left':i,'right':j,'rival':c,
                                  'factor':factor,'multiplier':scale//g})
                    break
    forbidden={i:set()for i in range(46)}
    for e in edges:
        forbidden[e['left']].add(e['right']);forbidden[e['right']].add(e['left'])
    # Only a positive clique cover matters: no minimum or absence claim.
    rng=random.Random(4701)
    best=[list(range(i,i+1))for i in range(46)]
    for trial in range(500):
        remaining=set(range(46));cover=[]
        while remaining:
            candidate=set(remaining);clique=[]
            while candidate:
                scored=[(len(forbidden[i]&candidate)+rng.random()*3,i)for i in candidate]
                _,chosen=max(scored)
                clique.append(chosen);candidate&=forbidden[chosen]
            cover.append(sorted(clique));remaining-=set(clique)
        if len(cover)<len(best):best=cover
    summary={'vertices':46,'candidate_pairs':1035,'positive_rival_pairs':len(edges),
             'unexcluded_pairs':1035-len(edges),'positive_clique_cover_size':len(best)}
    Path('stage47_star_pairs_results.json').write_text(json.dumps({
        'scope':'Only the fixed same-star avoidance pairs. Missing witnesses are inconclusive.',
        'summary':summary,'words':[m['word_abcv'] for m in models],'edges':edges,
        'positive_clique_cover':best},indent=2)+'\n')
    print(json.dumps(summary,indent=2))


if __name__=='__main__':main()
