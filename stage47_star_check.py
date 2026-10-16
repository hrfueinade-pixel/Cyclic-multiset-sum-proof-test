"""Independent checks for new star avoidance evidence; no producer imports.

The inventory absence remains diagnostic. Only supplied nonnegative rival
identities and the fixed full-valid counterexample support conclusions.
"""
import itertools
import json
from collections import Counter,defaultdict
from pathlib import Path


def compositions(total,width):
    if width==1:
        yield (total,)
    else:
        for first in range(total+1):
            for rest in compositions(total-first,width-1):
                yield (first,)+rest


def coeff(c,rows):
    return tuple(sum(c[i]*rows[i][j] for i in range(8)) for j in range(4))


def check():
    # Independently exhaust the short hand construction, including ordinary
    # 2111 words: all 56 degree-five words on four labels.
    hand_pairs=0;hand_injective=0
    four=list(compositions(5,4))
    assert len(four)==56
    for left,right in itertools.combinations(four,2):
        if (left[3]-right[3])%2:continue
        paritydiff=[i for i in range(3)if(left[i]-right[i])%2]
        assert len(paritydiff)in(0,2)
        if not paritydiff:
            epsilon=tuple(x%2 for x in left)
            reduced_left=tuple((x-e)//2 for x,e in zip(left,epsilon))
            reduced_right=tuple((x-e)//2 for x,e in zip(right,epsilon))
            assert reduced_left!=reduced_right and sum(reduced_left)==sum(reduced_right)<=2
            hand_injective+=1;continue
        embedded_left=(left[0],left[1],left[2],0,left[3],0,0,0)
        embedded_right=(right[0],right[1],right[2],0,right[3],0,0,0)
        numerator=[a+b for a,b in zip(embedded_left,embedded_right)]
        numerator[4]+=2
        for i in paritydiff:numerator[i]+=1
        missing=next(i for i in range(3)if i not in paritydiff)
        center=5+missing
        numerator[center]+=2
        assert all(x%2==0 for x in numerator)
        rival=tuple(x//2 for x in numerator)
        assert sum(rival)==8 and min(rival)>=0 and rival!=(1,)*8
        rows=[(2,0,0,0),(0,2,0,0),(0,0,2,0),tuple(2*x for x in left),
              (0,0,0,2),(0,-1,-1,0),(-1,0,-1,0),(-1,-1,0,0)]
        delta=tuple(a-b for a,b in zip(coeff(rival,rows),coeff((1,)*8,rows)))
        assert tuple(2*x for x in delta)==tuple(2*(b-a)for a,b in zip(left,right))
        hand_pairs+=1
    d=json.loads(Path('stage47_star_avoid_results.json').read_text())
    seen=set()
    for m in d['models']:
        w=tuple(m['word_abcv']);seen.add(w)
        assert sum(w)==5 and tuple(sorted(x for x in w if x))!=(1,1,1,2)
        expected=[(2,0,0,0),(0,2,0,0),(0,0,2,0),tuple(2*x for x in w),
                  (0,0,0,2),(0,-1,-1,0),(-1,0,-1,0),(-1,-1,0,0)]
        rows=[tuple(x)for x in m['rows']]
        assert rows==expected
        target=coeff((1,)*8,rows)
        for rival in m['direct_rivals']:
            assert sum(rival)==8 and min(rival)>=0 and rival!=[1]*8
            assert coeff(rival,rows)==target
    wanted={w for w in compositions(5,4)if sorted(x for x in w if x)!=[1,1,1,2]}
    assert seen==wanted and len(seen)==52
    p=json.loads(Path('stage47_star_pairs_results.json').read_text())
    assert len(p['words'])==46 and len(p['edges'])==726
    edgekeys=set()
    for e in p['edges']:
        key=(e['left'],e['right']);assert key not in edgekeys;edgekeys.add(key)
        left=p['words'][e['left']];right=p['words'][e['right']]
        rows=[(2,0,0,0),(0,2,0,0),(0,0,2,0),tuple(2*x for x in left),
              (0,0,0,2),(0,-1,-1,0),(-1,0,-1,0),(-1,-1,0,0)]
        r=e['rival'];assert sum(r)==8 and min(r)>=0 and r!=[1]*8
        factor=e['factor'];assert factor>0 and factor&(factor-1)==0
        k=e['multiplier'];assert k!=0
        delta=tuple(a-b for a,b in zip(coeff(r,rows),coeff((1,)*8,rows)))
        assert tuple(factor*x for x in delta)==tuple(k*2*(a-b)for a,b in zip(right,left))
    cover=p['positive_clique_cover']
    assert sorted(i for block in cover for i in block)==list(range(46))
    for block in cover:
        for i,j in itertools.combinations(block,2):
            assert (min(i,j),max(i,j))in edgekeys
    raw=(2,202,20402,10,-598,-10302,-10202,-102)
    a=tuple(x+10302 for x in raw);n=245633;target=sum(a)%n
    assert len(set(a))==8 and n==8*max(a)+1
    hits=[c for c in compositions(8,8)if sum(x*y for x,y in zip(a,c))%n==target]
    assert hits==[(1,)*8]
    fibers={};counts={};caps={};r3=0
    for degree in (3,4,5):
        repeated=defaultdict(list)
        for c in compositions(degree,8):
            if max(c)>1:repeated[sum(x*y for x,y in zip(a,c))%n].append(c)
        counts[degree]=len(repeated)
        ordinary=lambda c:sorted(x for x in c if x)==[1]*(degree-2)+[2]
        caps[degree]={'total':max(map(len,repeated.values())),
                      'ordinary':max(sum(ordinary(c)for c in words)for words in repeated.values())}
        if degree==3:r3=sum((len(words)-1)*(len(words)-2)//2 for words in repeated.values())
        if degree==4:fibers['quartic']=[c for c in compositions(4,8)if sum(x*y for x,y in zip(raw,c))==0]
        if degree==5:fibers['star_u']=[c for c in compositions(5,8)if sum(x*y for x,y in zip(raw,c))==10]
    difference={(x-y)%n for x in a for y in a if x!=y}
    h=sum((2*x)%n not in difference for x in difference)//2
    assert counts=={3:60,4:228,5:592} and h==24 and r3==0
    assert caps[3]['total']==2 and caps[4]['ordinary']==3 and caps[5]['ordinary']==3
    assert len(fibers['quartic'])==3 and len(fibers['star_u'])==5
    result={'status':'PASS','positive_rival_pair_records':len(p['edges']),
            'positive_clique_cover_bound':len(cover),
            'short_hand_rival_pairs':hand_pairs,'fixed_parity_pairs':hand_injective,
            'inventory_assignments':52,'surviving_assignments_diagnostic':46,
            'fixed_control':{'set':a,'raw_set':raw,'modulus':n,'T':counts,
                             'h':h,'R3':r3,'caps':caps,'fibers':fibers,
                             'eight_term_words_checked':6435,'full_valid':True},
            'boundary':'Counterexample to unrestricted avoidance cap one, outside sub-248 target.'}
    Path('stage47_star_check_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':check()
