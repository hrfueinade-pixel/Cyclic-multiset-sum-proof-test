"""Independent coverage construction and direct integer identity checker.

Imports no producer, eliminator, or historical checker. Split patterns are
constructed from a shared source and its two unused labels rather than the
producer's ordered eight-label canonical loop. No rational rank is a premise.
"""
from collections import Counter
from itertools import combinations, product
from pathlib import Path
import copy
import gzip
import hashlib
import json

HERE=Path(__file__).parent
V=set(range(8))
IDENTITIES=0


def counts(indices):
    return tuple(indices.count(i) for i in range(8))


def subtract(a,b):
    return tuple(x-y for x,y in zip(a,b))


def add_label(w,i):
    a=list(w)
    a[i]+=1
    return tuple(a)


def canonical(labels):
    assert sorted(labels)==list(range(8))
    x,y,z,a,b,c,d,e=labels
    words=(counts((x,x,c,d,e)),counts((y,y,a,d,e)),counts((z,z,a,b,c)))
    return words,(subtract(words[0],words[1]),subtract(words[0],words[2]))


CW,CR=canonical(tuple(range(8)))
CK=tuple(sorted(CW))


def source_edges(words):
    ans=[]
    centers=[w.index(2) for w in words]
    tails=[{i for i,v in enumerate(w) if v==1} for w in words]
    for i,j in combinations(range(3),2):
        common=tails[i]&tails[j]
        if len(common)==1:
            ans.append(tuple(sorted((centers[i],centers[j]))))
    assert len(ans)==2
    return set(ans)


def presentations(edge):
    """All 720 genuine split fibers using this fixed open source edge."""
    left,right=edge
    fibers={}
    rooted={}
    for third in sorted(V-set(edge)):
        for added in sorted(V-set(edge)-{third}):
            four=sorted(V-set(edge)-{third,added})
            for ltail in combinations(four,2):
                rtail=sorted(set(four)-set(ltail))
                first=counts((left,left)+ltail+(added,))
                second=counts((right,right)+tuple(rtail)+(added,))
                for omission in four:
                    last=counts((third,third)+tuple(i for i in four if i!=omission))
                    words=(first,second,last)
                    key=tuple(sorted(words))
                    assert key not in fibers
                    edges=source_edges(words)
                    assert edge in edges
                    other=next(e for e in edges if e!=edge)
                    fibers[key]=other
                    # Recover the source on 'other' directly from the words.
                    ia=next(i for i,w in enumerate(words) if w.index(2)==third)
                    ib=next(i for i,w in enumerate(words) if w.index(2) in set(other)-{third})
                    common=next(iter({i for i,v in enumerate(words[ia]) if v==1}&
                                     {i for i,v in enumerate(words[ib]) if v==1}))
                    wa=list(words[ia]); wb=list(words[ib])
                    wa[common]-=1; wb[common]-=1
                    ta=[i for i,v in enumerate(wa) if v==1]
                    tb=[i for i,v in enumerate(wb) if v==1]
                    z=words[ib].index(2)
                    for f,g in product(ta,tb):
                        rooted[key,(third,z,f,g)]=other
    assert len(fibers)==720 and len(rooted)==2880
    return fibers,rooted


def closure_row(c):
    y,z,f,g=c
    assert len({y,z,f,g})==4
    return subtract(counts((y,y,g)),counts((z,z,f)))


def ordinary(w,degree):
    return len(w)==8 and sorted(v for v in w if v)==[1]*(degree-2)+[2]


def identity(rows,target,witness):
    global IDENTITIES
    factor=witness['factor']
    multipliers=witness['multipliers']
    assert isinstance(factor,int) and factor>0 and factor&(factor-1)==0
    assert len(multipliers)==len(rows) and all(isinstance(v,int) for v in multipliers)
    assert all(len(r)==8 and sum(r)==0 for r in rows)
    assert tuple(sum(z*r[i] for z,r in zip(multipliers,rows)) for i in range(8))==tuple(factor*v for v in target)
    IDENTITIES+=1


def check_witness(rows,opened,w):
    assert w is not None
    kind=w['kind']
    if kind=='label_collision':
        i,j=w['labels']; assert i in V and j in V and i!=j
        target=subtract(counts((i,)),counts((j,)))
    elif kind=='open_edge_closed':
        edge=tuple(w['edge']); assert tuple(sorted(edge)) in opened
        i,j=w['difference']; assert i in V and j in V and i!=j
        target=subtract(counts((edge[0],edge[0],j)),counts((edge[1],edge[1],i)))
    elif kind=='protected_collision':
        sf=tuple(w['squarefree']); other=tuple(w['other']); degree=w['degree']
        assert len(sf)==len(other)==8 and degree in (2,3,4)
        assert set(sf)<=set((0,1)) and sum(sf)==sum(other)==degree
        assert min(other)>=0 and sf!=other
        target=subtract(sf,other)
    elif kind=='mass_eight_rival':
        rival=tuple(w['word'])
        assert len(rival)==8 and min(rival)>=0 and sum(rival)==8 and rival!=(1,)*8
        target=subtract(rival,(1,)*8)
    elif kind=='ordinary_quartic_triple':
        words=[tuple(a) for a in w['words']]
        assert len(set(words))==3 and all(ordinary(a,4) for a in words)
        assert len(w['identities'])==2
        for a,cert in zip(words[1:],w['identities']):
            identity(rows,subtract(words[0],a),cert)
        return
    else:
        raise AssertionError('Unknown witness kind')
    identity(rows,target,w)


def keyed_roots(records):
    out={}
    for r in records:
        words,rows=canonical(r['root_labels'])
        key=tuple(sorted(words)),tuple(r['closure'])
        assert r['index'] not in out
        out[r['index']]={'key':key,'words':words,'rows':rows+(closure_row(r['closure']),),
                         'witness':r['witness']}
    return out


def check_closed(data):
    rows=((1,1,0),(0,1,0),(0,0,0),(2,0,1),(4,6,1),(0,0,1),(4,2,1),(0,2,1))
    assert data['coefficient_rows']==[list(r) for r in rows]
    def val(w):
        return tuple(sum(w[i]*rows[i][j] for i in range(8)) for j in range(3))
    target=val((1,)*8)
    assert list(target)==data['target']==[11,12,5]
    words=[tuple(w) for w in data['words']]
    assert len(words)==len(set(words))==116
    assert all(len(w)==8 and min(w)>=0 and sum(w)==4 and max(w)>1 for w in words)
    values=[val(w) for w in words]
    assert len(set(values))==116
    seen=set()
    for r in data['pairs']:
        i,j=r['indices']; assert 0<=i<j<116 and (i,j) not in seen
        seen.add((i,j))
        rival=tuple(r['rival']); factor=r['factor']; mult=r['multiplier']
        assert len(rival)==8 and min(rival)>=0 and sum(rival)==8 and rival!=(1,)*8
        assert factor>0 and factor&(factor-1)==0 and isinstance(mult,int) and mult
        assert tuple(factor*(a-b) for a,b in zip(val(rival),target))==tuple(mult*(a-b) for a,b in zip(values[i],values[j]))
    assert seen==set(combinations(range(116),2))
    # Independently check all sixteen both-closed tail placements. Twelve
    # have a protected squarefree cubic; two give 2a=2c; two are d/e mirrors.
    kinds=Counter()
    for f,g,ff,gg in product((6,7),(3,4),(6,7),(4,5)):
        left=counts((3,ff,g)); right=counts((5,f,gg))
        base=subtract(counts((0,0,5)),counts((1,1,3)))
        first=subtract(counts((0,0,g)),counts((2,2,f)))
        second=subtract(counts((1,1,gg)),counts((2,2,ff)))
        assert subtract(right,left)==tuple(b-c+d for b,c,d in zip(base,first,second))
        assert left!=right
        if max(left)==1 or max(right)==1:
            kinds['protected']+=1
        elif f==ff:
            assert g==3 and gg==5
            assert subtract(right,left)==subtract(counts((5,5)),counts((3,3)))
            kinds['dyadic_label']+=1
        else:
            assert g==3 and gg==5
            kinds['normal_form']+=1
    assert dict(kinds)=={'protected':12,'dyadic_label':2,'normal_form':2}
    return 6670


def main():
    blob=(HERE/'stage53_split_graph_certificates.json.gz').read_bytes()
    data=json.loads(gzip.decompress(blob))
    left_fibers,left_roots=presentations((0,2))
    right_fibers,right_roots=presentations((1,2))
    counts_out={}
    marked=data['marked_edge']
    assert marked['half_complete'] and marked['full_complete']
    roots=keyed_roots(marked['half_records'])
    assert {r['key'] for r in roots.values()}==set(left_roots)
    assert len(roots)==2880
    survivors={i for i,r in roots.items() if r['witness'] is None}
    assert survivors==set(marked['half_survivors']) and len(survivors)==10
    for r in roots.values():
        if r['witness'] is not None:
            check_witness(CR+r['rows'],{(0,2),(1,2)},r['witness'])
    pi={0:1,1:0,3:5,5:3}
    def perm(row):
        return tuple(row[next(k for k in range(8) if pi.get(k,k)==i)] for i in range(8))
    assert tuple(sorted(perm(w) for w in CW))==CK
    assert {(tuple(sorted(perm(w) for w in r['words'])),tuple(pi.get(i,i) for i in r['key'][1])) for r in roots.values()}==set(right_roots)
    full=marked['full_records']
    assert {(r['left'],r['right']) for r in full}==set(product(survivors,repeat=2)) and len(full)==100
    for r in full:
        rows=CR+roots[r['left']]['rows']+tuple(perm(a) for a in roots[r['right']]['rows'])
        check_witness(rows,{(0,2),(1,2)},r['witness'])
    counts_out['marked_edge']={'half_presentations':2880,'half_positive_exclusions':2870,'residual_pairs_closed':100}

    path=data['marked_path']; assert path['complete']
    expected=set(product(survivors,set(right_fibers)-{CK}))
    actual=set()
    for r in path['records']:
        words,rows=canonical(r['labels']); key=tuple(sorted(words))
        assert (r['root'],key) not in actual
        actual.add((r['root'],key))
        assert key in right_fibers and key!=CK
        opened={(0,2),(1,2),right_fibers[key]}
        assert set(map(tuple,r['opened']))==opened
        check_witness(CR+roots[r['root']]['rows']+rows,opened,r['witness'])
    assert actual==expected and len(actual)==7190 and path['skipped_same_fiber']==10
    counts_out['marked_path']={'all_extensions_closed':len(actual)}

    degree=data['degree_three']; assert degree['half_complete'] and degree['full_complete']
    half={}
    for r in degree['half_records']:
        words,rows=canonical(r['labels']); key=tuple(sorted(words))
        assert r['attachment'] not in half
        half[r['attachment']]={'key':key,'rows':rows,'other':left_fibers[key],'witness':r['witness']}
        if r['witness'] is not None:
            check_witness(CR+rows,{(0,2),(1,2),left_fibers[key]},r['witness'])
    assert {r['key'] for r in half.values()}==set(left_fibers)-{CK} and len(half)==719
    alive={i for i,r in half.items() if r['witness'] is None}
    assert alive==set(degree['half_survivors']) and len(alive)==34
    # These exclusions also rule out auxiliary parallel edges, without
    # silently using the historical shared-center theorem.
    assert all(half[i]['other']!=(1,2) for i in alive)
    expected={(a,b) for a,b in product(alive,repeat=2) if half[a]['other']!=half[b]['other']}
    records=degree['full_records']
    assert {(r['left'],r['right']) for r in records}==expected and len(records)==962
    for r in records:
        a,b=half[r['left']],half[r['right']]
        opened={(0,2),(1,2),a['other'],b['other']}
        check_witness(CR+a['rows']+b['rows'],opened,r['witness'])
    counts_out['degree_three']={'pair_presentations':719,'pair_exclusions':685,'survivor_pairs_closed':962,'parallel_edges_excluded':True}

    marks=data['two_marks']; assert marks['complete']
    expected=set(product({(1,2,f,g) for f,g in product((6,7),(4,5))},
                         {i for i,r in roots.items() if r['key'][0]!=CK}))
    seen=set()
    for r in marks['records']:
        first=tuple(r['first_closure']); key=(first,r['root'])
        assert key not in seen; seen.add(key)
        assert first in {(1,2,f,g) for f,g in product((6,7),(4,5))}
        check_witness(CR+(closure_row(first),)+roots[r['root']]['rows'],{(0,2)},r['witness'])
    assert seen==expected and len(seen)==11504 and marks['skipped_same_fiber']==16
    counts_out['two_marks']={'all_presentations_closed':len(seen)}

    inherited=check_closed(data['closed_split'])
    # Deliberate corruption: neither nonunit cancellation nor a wrong row
    # coefficient is permitted by the independent arithmetic checker.
    sample=next(r for r in marked['half_records'] if r['witness'] and r['witness']['kind']!='ordinary_quartic_triple')
    rows=CR+roots[sample['index']]['rows']
    for field in ('nonunit','coefficient'):
        bad=copy.deepcopy(sample['witness'])
        if field=='nonunit': bad['factor']=3
        else: bad['multipliers'][0]+=1
        rejected=False
        try: check_witness(rows,{(0,2),(1,2)},bad)
        except AssertionError: rejected=True
        assert rejected
    result={'complete':True,'new_integer_identities_checked':IDENTITIES,
            'coverage':counts_out,'closed_split_growth_pair_identities':inherited,
            'corruption_controls':'nonunit and changed multiplier rejected',
            'bundle_sha256':hashlib.sha256(blob).hexdigest(),
            'proof_boundary':'Computer-assisted local identities plus the written global graph proof; C4=0 branch only. No independent human or formal verification.'}
    (HERE/'stage53_independent_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
