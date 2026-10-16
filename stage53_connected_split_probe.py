"""New symbolic question: a two-open split and adjacent one-open splits.

No group elements or moduli are enumerated. Negative witness discovery is
inconclusive. Positive exclusions retain integer identities with only a
power of two canceled. This diagnostic is not a global compensation proof.
"""
from fractions import Fraction
from itertools import combinations
from math import lcm
from pathlib import Path
import argparse
import json
import time

V = tuple(range(8))


def word(center, tails):
    ans = [0] * 8
    ans[center] = 2
    for x in tails:
        ans[x] += 1
    return tuple(ans)


def diff(left, right):
    return tuple(x-y for x, y in zip(left, right))


def split(x, y, z, a, b, c, d, e):
    words = (word(x, (c,d,e)), word(y, (a,d,e)), word(z, (a,b,c)))
    sources = ((word(x,(d,e)), word(z,(a,b))),
               (word(y,(d,e)), word(z,(b,c))))
    return {'labels':(x,y,z,a,b,c,d,e), 'words':words, 'sources':sources,
            'rows':(diff(words[0], words[1]), diff(words[0], words[2]))}


CENTRAL = split(0,1,2,3,4,5,6,7)


def attachments(edge):
    for r in sorted(set(V)-set(edge)):
        for z in edge:
            x = next(v for v in edge if v != z)
            y = r
            tail = sorted(set(V)-{x,y,z})
            for a in tail:
                for c in tail:
                    if a == c:
                        continue
                    for b in tail:
                        if b in (a,c):
                            continue
                        d,e = sorted(set(tail)-{a,b,c})
                        model = split(x,y,z,a,b,c,d,e)
                        yield model


def roots(edge):
    for model in attachments(edge):
        x,y,z,a,b,c,d,e = model['labels']
        for f in (d,e):
            for g in (b,c):
                row = [0]*8
                row[y] += 2
                row[z] -= 2
                row[f] -= 1
                row[g] += 1
                yield {'split': model, 'closure':(y,z,f,g),
                       'rows': model['rows']+(tuple(row),)}


def normal(rows):
    """Rational elimination is discovery only; certificates enforce dyadic use."""
    mat = [list(map(Fraction, r[:7])) for r in rows]
    coeff = [[Fraction(int(i==j)) for j in range(len(rows))]
             for i in range(len(rows))]
    pivots = []
    k = 0
    for c in range(7):
        found = next((i for i in range(k,len(mat)) if mat[i][c]), None)
        if found is None:
            continue
        mat[k], mat[found] = mat[found], mat[k]
        coeff[k], coeff[found] = coeff[found], coeff[k]
        factor = mat[k][c]
        mat[k] = [v/factor for v in mat[k]]
        coeff[k] = [v/factor for v in coeff[k]]
        for i in range(len(mat)):
            if i != k and mat[i][c]:
                factor = mat[i][c]
                mat[i] = [v-factor*w for v,w in zip(mat[i],mat[k])]
                coeff[i] = [v-factor*w for v,w in zip(coeff[i],coeff[k])]
        pivots.append(c)
        k += 1
    free = sorted(set(range(7))-set(pivots))
    label_coords = [[Fraction(int(i==f)) for f in free] for i in range(7)]
    for row,c in enumerate(pivots):
        label_coords[c] = [-mat[row][f] for f in free]
    label_coords.append([Fraction(0) for _ in free])
    scale = lcm(*(v.denominator for row in label_coords for v in row))
    label_coords = tuple(tuple(int(v*scale) for v in row) for row in label_coords)
    short = None
    def value(w):
        return tuple(sum(w[i]*label_coords[i][j] for i in V) for j in range(len(free)))
    def certificate(target):
        nonlocal short
        # Target is homogeneous, and coordinate seven follows from row sums.
        if value(target) != (0,)*len(free):
            return None
        combo = [sum(Fraction(target[c])*coeff[i][j] for i,c in enumerate(pivots))
                 for j in range(len(rows))]
        factor = lcm(*(v.denominator for v in combo))
        if factor & (factor-1):
            # A rational basis can miss an integral combination involving a
            # dependent original row. Try explicit one/two-row identities;
            # never interpret rational row membership as a group identity.
            if short is None:
                short = {}
                for i,row in enumerate(rows):
                    for sign in (-1,1):
                        co=[0]*len(rows)
                        co[i]=sign
                        short[tuple(sign*v for v in row)]=co
                for i,j in combinations(range(len(rows)),2):
                    for si in (-1,1):
                        for sj in (-1,1):
                            co=[0]*len(rows)
                            co[i],co[j]=si,sj
                            short[tuple(si*rows[i][v]+sj*rows[j][v] for v in V)]=co
            for scale in (1,2,4,8,16,32):
                key=tuple(scale*v for v in target)
                if key in short:
                    return {'factor':scale,'multipliers':short[key]}
            return None
        integers = [int(v*factor) for v in combo]
        assert tuple(sum(integers[j]*rows[j][i] for j in range(len(rows)))
                     for i in V) == tuple(factor*v for v in target)
        return {'factor':factor, 'multipliers':integers}
    return value,certificate,len(pivots),label_coords


def compositions(total, length=8):
    def recurse(prefix, remaining):
        if len(prefix) == length-1:
            yield tuple(prefix+[remaining])
        else:
            for value in range(remaining+1):
                yield from recurse(prefix+[value],remaining-value)
    yield from recurse([],total)


SQUAREFREE = {d:[tuple(int(i in c) for i in V) for c in combinations(V,d)]
              for d in (2,3,4)}
ALLWORDS = {d:list(compositions(d)) for d in (2,3,4,8)}
ORD4 = [word(c,t) for c in V for t in combinations(set(V)-{c},2)]


def exclude(rows, opened=((0,2),(1,2)), rivals=True):
    value, cert, rank, coords = normal(rows)
    for i,j in combinations(V,2):
        target = tuple(int(v==i)-int(v==j) for v in V)
        witness = cert(target)
        if witness:
            return {'kind':'label_collision','labels':(i,j),**witness},rank
    for edge in opened:
        for i in V:
            for j in V:
                if i == j:
                    continue
                target = [0]*8
                target[edge[0]] += 2
                target[edge[1]] -= 2
                target[i] -= 1
                target[j] += 1
                witness = cert(tuple(target))
                if witness:
                    return {'kind':'open_edge_closed','edge':edge,'difference':(i,j),**witness},rank
    for degree in (2,3,4):
        groups = {}
        for w in ALLWORDS[degree]:
            groups.setdefault(value(w),[]).append(w)
        for sf in SQUAREFREE[degree]:
            for w in groups[value(sf)]:
                if sf == w:
                    continue
                witness = cert(diff(sf,w))
                if witness:
                    return {'kind':'protected_collision','degree':degree,
                            'squarefree':sf,'other':w,**witness},rank
    groups = {}
    for w in ORD4:
        groups.setdefault(value(w),[]).append(w)
    for group in groups.values():
        if len(group) < 3:
            continue
        for triple in combinations(group,3):
            witnesses = [cert(diff(triple[0],w)) for w in triple[1:]]
            if all(witnesses):
                return {'kind':'ordinary_quartic_triple','words':triple,
                        'identities':witnesses},rank
    if rivals:
        target = (1,)*8
        target_value = value(target)
        for w in ALLWORDS[8]:
            if w != target and value(w) == target_value:
                witness = cert(diff(w,target))
                if witness:
                    return {'kind':'mass_eight_rival','word':w,**witness},rank
    return None,rank


def run(seconds, full):
    start = time.monotonic()
    records, survivors = [], []
    counts = {}
    roots_left = list(roots((0,2)))
    assert len(roots_left) == 2880
    for index,root in enumerate(roots_left):
        if time.monotonic()-start > seconds:
            raise TimeoutError('Half-core inventory incomplete; no exclusion conclusion.')
        rows = CENTRAL['rows']+root['rows']
        witness,rank = exclude(rows)
        record = {'index':index,'root_labels':root['split']['labels'],
                  'closure':root['closure'],'rank':rank,'witness':witness}
        records.append(record)
        key = witness['kind'] if witness else 'unresolved'
        counts[key] = counts.get(key,0)+1
        if witness is None:
            survivors.append(index)
    result = {'scope':'Canonical two-open central split with one root mark on xz; all labels reused within eight positions.',
              'half_complete':True,'half_counts':counts,'half_survivors':survivors,
              'half_records':records,'full_complete':False,'elapsed':time.monotonic()-start}
    print(json.dumps({k:v for k,v in result.items() if k!='half_records'}),flush=True)
    if full:
        # Central symmetry swaps x/y and a/c; it carries xz roots to yz roots.
        pi = {0:1,1:0,3:5,5:3}
        def perm(row):
            ans = [0]*8
            for i,v in enumerate(row):
                ans[pi.get(i,i)] = v
            return tuple(ans)
        full_records = []
        full_counts = {}
        for left in survivors:
            for right in survivors:
                if time.monotonic()-start > seconds:
                    result['full_records']=full_records
                    result['full_counts']=full_counts
                    result['elapsed']=time.monotonic()-start
                    Path('stage53_connected_split_probe_results.json').write_text(json.dumps(result)+'\n')
                    raise TimeoutError('Full core coverage incomplete; residuals remain.')
                rows = CENTRAL['rows']+roots_left[left]['rows']+tuple(perm(r) for r in roots_left[right]['rows'])
                witness,rank = exclude(rows)
                full_records.append({'left':left,'right':right,'rank':rank,'witness':witness})
                key = witness['kind'] if witness else 'unresolved'
                full_counts[key]=full_counts.get(key,0)+1
        result.update(full_complete=True,full_records=full_records,full_counts=full_counts)
    result['elapsed']=time.monotonic()-start
    Path('stage53_connected_split_probe_results.json').write_text(json.dumps(result)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('half_records','full_records')}),flush=True)


def propagation(seconds):
    started=time.monotonic()
    previous=json.loads(Path('stage53_connected_split_probe_results.json').read_text())
    left=list(roots((0,2)))
    other=list(attachments((1,2)))
    assert len(other)==720
    records=[]
    counts={}
    skipped=0
    for a in previous['half_survivors']:
        for b,model in enumerate(other):
            if tuple(sorted(model['words']))==tuple(sorted(CENTRAL['words'])):
                skipped+=1
                continue
            if time.monotonic()-started>seconds:
                raise TimeoutError('Propagation inventory incomplete.')
            x,y,z,*_=model['labels']
            opened=((0,2),(1,2),tuple(sorted((y,z))))
            witness,rank=exclude(CENTRAL['rows']+left[a]['rows']+model['rows'],opened)
            records.append({'root':a,'attachment':b,'labels':model['labels'],
                            'opened':opened,'rank':rank,'witness':witness})
            kind=witness['kind'] if witness else 'unresolved'
            counts[kind]=counts.get(kind,0)+1
    result={'scope':'One root, central auxiliary edge, and second two-open split incident to yz.',
            'complete':True,'counts':counts,'skipped_same_fiber':skipped,
            'records':records,'elapsed':time.monotonic()-started}
    Path('stage53_path_propagation_results.json').write_text(json.dumps(result)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='records'}))
    print(json.dumps([r for r in records if r['witness'] is None]))


def two_open_reuse(seconds):
    started=time.monotonic()
    models=list(attachments((0,2)))
    half=[]
    survivors=[]
    counts={}
    for b,model in enumerate(models):
        if tuple(sorted(model['words']))==tuple(sorted(CENTRAL['words'])):
            continue
        x,y,z,*_=model['labels']
        opened=((0,2),(1,2),tuple(sorted((y,z))))
        witness,rank=exclude(CENTRAL['rows']+model['rows'],opened)
        half.append({'attachment':b,'labels':model['labels'],
                     'opened':opened,'rank':rank,'witness':witness})
        kind=witness['kind'] if witness else 'unresolved'
        counts[kind]=counts.get(kind,0)+1
        if witness is None:
            survivors.append(b)
    result={'scope':'Two distinct two-open splits sharing xz, then three with distinct other source-center edges.',
            'half_complete':True,'half_counts':counts,'half_survivors':survivors,
            'half_records':half,'full_complete':False}
    print(json.dumps({k:v for k,v in result.items() if k!='half_records'}),flush=True)
    records=[]
    full_counts={}
    skipped=0
    for a in survivors:
        for b in survivors:
            ma,mb=models[a],models[b]
            ea=tuple(sorted((ma['labels'][1],ma['labels'][2])))
            eb=tuple(sorted((mb['labels'][1],mb['labels'][2])))
            if ea==eb:
                skipped+=1
                continue
            if time.monotonic()-started>seconds:
                result.update(full_records=records,full_counts=full_counts,elapsed=time.monotonic()-started)
                Path('stage53_three_open_reuse_results.json').write_text(json.dumps(result)+'\n')
                raise TimeoutError('Three-source degree inventory incomplete.')
            opened=((0,2),(1,2),ea,eb)
            witness,rank=exclude(CENTRAL['rows']+ma['rows']+mb['rows'],opened)
            records.append({'left':a,'right':b,'opened':opened,'rank':rank,'witness':witness})
            kind=witness['kind'] if witness else 'unresolved'
            full_counts[kind]=full_counts.get(kind,0)+1
    result.update(full_complete=True,full_records=records,full_counts=full_counts,
                  skipped_equal_other_edge=skipped,elapsed=time.monotonic()-started)
    Path('stage53_three_open_reuse_results.json').write_text(json.dumps(result)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('half_records','full_records')}),flush=True)
    print(json.dumps([r for r in records if r['witness'] is None]))


def repeated_marks(seconds):
    started=time.monotonic()
    previous=json.loads(Path('stage53_connected_split_probe_results.json').read_text())
    left=list(roots((0,2)))
    records=[]
    counts={}
    skipped=0
    for a in previous['half_survivors']:
        for b in previous['half_survivors']:
            if tuple(sorted(left[a]['split']['words']))==tuple(sorted(left[b]['split']['words'])):
                skipped+=1
                continue
            if time.monotonic()-started>seconds:
                raise TimeoutError('Repeated-mark inventory incomplete.')
            witness,rank=exclude(CENTRAL['rows']+left[a]['rows']+left[b]['rows'])
            records.append({'left':a,'right':b,'rank':rank,'witness':witness})
            kind=witness['kind'] if witness else 'unresolved'
            counts[kind]=counts.get(kind,0)+1
    result={'scope':'Two distinct one-open split fibers at xz adjacent to one two-open split.',
            'complete':True,'counts':counts,'skipped_same_fiber':skipped,
            'records':records,'elapsed':time.monotonic()-started}
    Path('stage53_repeated_marks_results.json').write_text(json.dumps(result)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='records'}))
    print(json.dumps([r for r in records if r['witness'] is None]))


def unused_bonuses(rows):
    value,cert,rank,_=normal(rows)
    labels=sorted(set(V)-{0,2})
    answers=[]
    for c,d in combinations(labels,2):
        tails=sorted(set(labels)-{c,d})
        for lt in combinations(tails,2):
            rt=sorted(set(tails)-set(lt))
            wl,wr=word(c,lt),word(d,rt)
            equality=cert(diff(wl,wr))
            if equality is None:
                continue
            tests=[]
            for added,third in ((0,2),(2,0)):
                lift=list(wl)
                lift[added]+=1
                for omitted in tails:
                    third_word=word(third,sorted(set(tails)-{omitted}))
                    witness,_=exclude(rows+(diff(tuple(lift),third_word),),((0,2),))
                    if witness is None:
                        break
                    tests.append({'added':added,'third':third,'omitted':omitted,'witness':witness})
                if len(tests)<(4 if added==0 else 8):
                    break
            if len(tests)==8:
                answers.append({'words':(wl,wr),'identity':equality,'unused_tests':tests})
                if len(answers)==2:
                    return answers
    return answers


def isolated_marks(seconds):
    started=time.monotonic()
    models=list(roots((0,2)))
    records=[]
    counts={}
    skipped=0
    for f in (6,7):
        for g in (4,5):
            closure=[0]*8
            closure[1]+=2
            closure[2]-=2
            closure[f]-=1
            closure[g]+=1
            base=CENTRAL['rows']+(tuple(closure),)
            for index,root in enumerate(models):
                if tuple(sorted(root['split']['words']))==tuple(sorted(CENTRAL['words'])):
                    skipped+=1
                    continue
                if time.monotonic()-started>seconds:
                    raise TimeoutError('Isolated root compensation inventory incomplete.')
                rows=base+root['rows']
                witness,rank=exclude(rows,((0,2),))
                rec={'first_closure':(1,2,f,g),'root':index,'rank':rank,'witness':witness}
                kind=witness['kind'] if witness else 'compensation'
                if witness is None:
                    bonuses=unused_bonuses(rows)
                    rec['bonuses']=bonuses
                    source=next(s for s in root['split']['sources']
                                if set(i for i,v in enumerate(s[0]) if v==2)|set(i for i,v in enumerate(s[1]) if v==2)=={0,2})
                    support=set(i for w in source for i,v in enumerate(w) if v)
                    initial=set(i for w in CENTRAL['sources'][0] for i,v in enumerate(w) if v)
                    rec['six_tail_union']=len((support|initial)-{0,2})==6
                    if len(bonuses)!=2:
                        kind='unresolved_compensation'
                records.append(rec)
                counts[kind]=counts.get(kind,0)+1
    result={'scope':'Two distinct root marks on one open source edge; all other source edges closed.',
            'complete':True,'counts':counts,'skipped_same_fiber':skipped,
            'records':records,'elapsed':time.monotonic()-started}
    Path('stage53_isolated_mark_compensation_results.json').write_text(json.dumps(result)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='records'}),flush=True)
    print(json.dumps([r for r in records if r['witness'] is None]))


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--seconds',type=float,default=120)
    parser.add_argument('--full',action='store_true')
    parser.add_argument('--propagation',action='store_true')
    parser.add_argument('--repeated-marks',action='store_true')
    parser.add_argument('--three-open',action='store_true')
    parser.add_argument('--isolated-marks',action='store_true')
    args=parser.parse_args()
    if args.isolated_marks:
        isolated_marks(args.seconds)
    elif args.three_open:
        two_open_reuse(args.seconds)
    elif args.repeated_marks:
        repeated_marks(args.seconds)
    elif args.propagation:
        propagation(args.seconds)
    else:
        run(args.seconds,args.full)
