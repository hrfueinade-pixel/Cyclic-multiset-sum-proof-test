"""Verify general assignment by replacing ALL Stage 53 cap-two inferences.

Uses prior standalone coverage/arithmetic verifier helpers, never discovery
or elimination code. The source lemma is the proved Stage 54 premise.
"""
from collections import Counter
from itertools import combinations,product
from math import gcd
from pathlib import Path
import gzip
import hashlib
import json

import stage53_certificate_check as old
import stage54_certificate_check as arithmetic

HERE=Path(__file__).parent
REPLACEMENTS=0
NEW_CASES=0


def read(name):
    return json.loads(gzip.decompress((HERE/name).read_bytes()))


def source_pair(labels,index):
    x,y,z,a,b,c,d,e=labels
    if index==0: return old.counts((x,x,d,e)),old.counts((z,z,a,b))
    assert index==1
    return old.counts((y,y,d,e)),old.counts((z,z,b,c))


def verify_parameter(r):
    rows=r['rows']; unit=r['unit']; M=unit['rows']; free=unit['free_labels']; piv=unit['pivots']; selected=unit['selected_rows']; D=unit['scale']
    assert old.ordinary(old.counts((0,0,1,2)),4)
    assert arithmetic.unit2(D) and sorted(free+piv)==list(range(7))
    assert len(selected)==len(piv) and len(set(selected))==len(selected)
    assert len(M)==8 and M[7]==[0]*len(free) and all(len(a)==len(free) for a in M)
    assert all(M[c]==[D*int(i==j) for j in range(len(free))] for i,c in enumerate(free))
    assert arithmetic.unit2(abs(arithmetic.determinant([[rows[i][j] for j in piv] for i in selected])))
    L=[[sum(row[i]*M[i][j] for i in range(8)) for j in range(len(free))] for row in rows]
    assert all(not any(L[i]) for i in selected)
    U=r['U']
    if U is None:
        assert not any(any(a) for a in L)
        return M,[0]*8,1
    n=len(free)
    assert len(U)==n and all(len(a)==n for a in U) and abs(arithmetic.determinant(U))==1
    converted=[[sum(a[i]*U[i][j] for i in range(n)) for j in range(n)] for a in L]
    assert not any(any(a[1:]) for a in converted)
    g=gcd(*(a[0] for a in converted)); assert g==r['gcd'] and g>0
    odd=g
    while odd%2==0: odd//=2
    assert odd==r['odd_gcd']
    labels=[[sum(a[i]*U[i][j] for i in range(n)) for j in range(n)] for a in M]
    return [a[1:] for a in labels],[a[0]%odd for a in labels],odd


def verify_new(r,rows,models):
    global NEW_CASES
    assert r['rows']==[list(a) for a in rows] and r['splits']==[list(a) for a in models]
    assert not r.get('residual')
    if 'exclusion' in r:
        c=r['exclusion']
        if c['kind']=='split_source_triple':
            labels=tuple(c['split_labels']); assert labels in models
            old.canonical(labels)
            first,second=source_pair(labels,c['source_index'])
            third=tuple(c['third_word'])
            assert old.ordinary(third,4) and third not in (first,second)
            arithmetic.direct_identity(rows,arithmetic.sub(first,second),c['source_identity'])
            arithmetic.direct_identity(rows,arithmetic.sub(first,third),c['third_identity'])
        else: arithmetic.check_exclusion(rows,c)
    else:
        M,tor,order=verify_parameter(r)
        arithmetic.check_positive(M,tor,order,r['positive'])
    NEW_CASES+=1


def c3_configurations():
    ans={}
    for i,j in combinations(range(3),2):
        eligible=set(range(8))-{i,j,i+3,j+3}
        for added in combinations(sorted(eligible),2):
            unused=sorted(eligible-set(added))
            for third in unused:
                middle=next(c for c in unused if c!=third)
                labels=(i,j,third,j+3,middle,i+3,*added)
                words,_=old.canonical(labels)
                ans[tuple(sorted(words))]=labels
    assert len(ans)==36
    return ans


def verify_cubic_lemma(data):
    base=(arithmetic.sub(old.counts((0,0,3)),old.counts((1,1,4))),
          arithmetic.sub(old.counts((0,0,3)),old.counts((2,2,5))))
    expected=c3_configurations(); seen=set(); first={}; alive=set()
    for r in data['cubic_first']:
        labels=tuple(r['splits'][0]); words,rows=old.canonical(labels); key=tuple(sorted(words))
        assert key in expected and key not in seen; seen.add(key)
        first[r['index']]=labels
        expected_rows=base+(rows[1],)
        if r.get('residual'):
            assert r['rows']==[list(a) for a in expected_rows]
            x,y,z,a,b,c,d,e=labels
            k=next(n for n in range(3) if n not in (x,y))
            assert z in (6,7) and b==k+3 and set((d,e))=={k,13-z}
            alive.add(r['index'])
        else: verify_new(r,expected_rows,(labels,))
    assert seen==set(expected) and len(first)==36 and alive=={7,10,19,22,31,34}
    pair_keys=set()
    for r in data['cubic_pairs']:
        i,j=r['left'],r['right']; assert i<j and i in alive and j in alive and (i,j) not in pair_keys
        pair_keys.add((i,j)); a,b=first[i],first[j]
        rows=base+(old.canonical(a)[1][1],old.canonical(b)[1][1])
        verify_new(r,rows,(a,b))
    assert pair_keys==set(combinations(sorted(alive),2))


def main():
    data=read('stage55_general_assignment_certificates.json.gz')
    prior_blob=(HERE/'stage53_split_graph_certificates.json.gz').read_bytes()
    assert hashlib.sha256(prior_blob).hexdigest()==data['prior53_sha256']
    assert hashlib.sha256((HERE/'stage54_source_certificates.json.gz').read_bytes()).hexdigest()==data['prior54_sha256']
    prior=json.loads(gzip.decompress(prior_blob))
    verify_cubic_lemma(data)
    mapping={}
    for r in data['graph_exceptions']:
        key=(r['scope'],r['index'])
        assert key not in mapping; mapping[key]=r
    triangles={(r['root'],tuple(r['first_closure'])):r for r in data['triangle_marks']}
    assert len(mapping)==46 and len(triangles)==2
    used=set(); used_tri=set(); stars=0

    def old_case(rows,opened,witness,key,models,closure=None):
        nonlocal stars
        global REPLACEMENTS
        if witness['kind']!='ordinary_quartic_triple':
            old.check_witness(rows,opened,witness); return
        words=[tuple(a) for a in witness['words']]
        assert len(set(words))==3 and all(old.ordinary(a,4) for a in words)
        for a,c in zip(words[1:],witness['identities']):
            arithmetic.direct_identity(rows,arithmetic.sub(words[0],a),c)
        degrees=Counter(i for a in words for i,n in enumerate(a) if n==1)
        signature=tuple(sorted(degrees.values(),reverse=True))
        if signature==(3,1,1,1):
            hub=next(i for i,n in degrees.items() if n==3)
            cubes=[tuple(v-int(i==hub) for i,v in enumerate(a)) for a in words]
            assert len({i for a in cubes for i,v in enumerate(a) if v})==6
            assert all(old.ordinary(a,3) for a in cubes)
            pairs={tuple(sorted(p)) for p in combinations(cubes,2)}
            for labels in models:
                x,y,z,a,b,c,d,e=labels
                assert tuple(sorted((old.counts((x,x,c)),old.counts((y,y,a))))) in pairs
            assert tuple(sorted(old.canonical(models[0])[0]))!=tuple(sorted(old.canonical(models[1])[0]))
            # The two actual split descents belong to this ordinary cubic
            # triple, contradicting the fully checked preceding lemma.
            stars+=1
        elif signature==(2,2,1,1):
            assert key in mapping and key not in used; used.add(key)
            verify_new(mapping[key],rows,models)
        elif signature==(2,2,2):
            assert closure is not None
            tkey=(key[1],tuple(closure))
            assert tkey in triangles and tkey not in used_tri; used_tri.add(tkey)
            verify_new(triangles[tkey],rows,models)
        else: raise AssertionError('Uncovered former cap-two inference')
        REPLACEMENTS+=1

    fibers_l,roots_l=old.presentations((0,2)); fibers_r,roots_r=old.presentations((1,2))
    marked=prior['marked_edge']; roots=old.keyed_roots(marked['half_records'])
    assert {r['key'] for r in roots.values()}==set(roots_l) and len(roots)==2880
    live={i for i,r in roots.items() if r['witness'] is None}; assert live=={1561,1563,1567,1573,1575,1579,1847,1851,1895,1899}
    labels_by_root={r['index']:tuple(r['root_labels']) for r in marked['half_records']}
    central=tuple(range(8))
    for i,r in roots.items():
        if r['witness']:
            old_case(old.CR+r['rows'],{(0,2),(1,2)},r['witness'],('root',i),(central,labels_by_root[i]))
    pi={0:1,1:0,3:5,5:3}
    def perm(row): return tuple(row[next(k for k in range(8) if pi.get(k,k)==i)] for i in range(8))
    assert tuple(sorted(perm(a) for a in old.CW))==old.CK
    assert {(tuple(sorted(perm(a) for a in r['words'])),tuple(pi.get(i,i) for i in r['key'][1])) for r in roots.values()}==set(roots_r)
    assert {(r['left'],r['right']) for r in marked['full_records']}==set(product(live,repeat=2))
    for r in marked['full_records']:
        assert r['witness']['kind']!='ordinary_quartic_triple'
        old.check_witness(old.CR+roots[r['left']]['rows']+tuple(perm(a) for a in roots[r['right']]['rows']),{(0,2),(1,2)},r['witness'])

    seen=set(); path=prior['marked_path']
    for r in path['records']:
        words,rows=old.canonical(r['labels']); key=tuple(sorted(words)); pair=r['root'],key
        assert pair not in seen and key!=old.CK; seen.add(pair)
        opened={(0,2),(1,2),fibers_r[key]}
        assert r['witness']['kind']!='ordinary_quartic_triple'
        old.check_witness(old.CR+roots[r['root']]['rows']+rows,opened,r['witness'])
    assert seen==set(product(live,set(fibers_r)-{old.CK})) and len(seen)==7190

    degree=prior['degree_three']; half={}
    for r in degree['half_records']:
        labels=tuple(r['labels']); words,rows=old.canonical(labels); key=tuple(sorted(words))
        assert r['attachment'] not in half
        half[r['attachment']]={'key':key,'rows':rows,'other':fibers_l[key],'witness':r['witness']}
        if r['witness']:
            old_case(old.CR+rows,{(0,2),(1,2),fibers_l[key]},r['witness'],('edge',r['attachment']),(central,labels))
    assert {r['key'] for r in half.values()}==set(fibers_l)-{old.CK} and len(half)==719
    active={i for i,r in half.items() if r['witness'] is None}; assert len(active)==34
    assert all(half[i]['other']!=(1,2) for i in active)
    expected={(i,j) for i,j in product(active,repeat=2) if half[i]['other']!=half[j]['other']}
    assert {(r['left'],r['right']) for r in degree['full_records']}==expected
    for r in degree['full_records']:
        a,b=half[r['left']],half[r['right']]
        assert r['witness']['kind']!='ordinary_quartic_triple'
        old.check_witness(old.CR+a['rows']+b['rows'],{(0,2),(1,2),a['other'],b['other']},r['witness'])

    seen=set(); marks=prior['two_marks']
    for r in marks['records']:
        closing=tuple(r['first_closure']); key=closing,r['root']; assert key not in seen; seen.add(key)
        rows=old.CR+(old.closure_row(closing),)+roots[r['root']]['rows']
        old_case(rows,{(0,2)},r['witness'],('marks',r['root']),(central,labels_by_root[r['root']]),closing)
    expected=set(product({(1,2,f,g) for f,g in product((6,7),(4,5))},{i for i,r in roots.items() if r['key'][0]!=old.CK}))
    assert seen==expected and len(seen)==11504
    assert used==set(mapping) and used_tri==set(triangles) and stars==8 and REPLACEMENTS==56
    old.check_closed(prior['closed_split'])
    result={'complete':True,'cubic_single_patterns':36,'cubic_residual_patterns':6,'cubic_pairs_closed':15,
            'former_cap_two_inferences_replaced':REPLACEMENTS,'cubic_star_replacements':stars,
            'new_positive_cases_checked':NEW_CASES,'new_quartic_pair_identities':arithmetic.PAIR_IDENTITIES,
            'new_integer_identities':arithmetic.DIRECT_IDENTITIES,
            'old_general_positive_identities':old.IDENTITIES,
            'closed_source_growth_pairs':6670,
            'bundle_sha256':hashlib.sha256((HERE/'stage55_general_assignment_certificates.json.gz').read_bytes()).hexdigest(),
            'proof_boundary':'General q<=h and t=0 exclusion use the written graph/packing argument. Full N>=248 remains open for t>0.'}
    (HERE/'stage55_independent_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__': main()
