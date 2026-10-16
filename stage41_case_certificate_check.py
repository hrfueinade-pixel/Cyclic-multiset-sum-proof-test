"""Check two positive symbolic growth certificates, independently of discovery.

No discovery imports, graph search, residue search, or old certificate runs.
Each pair of selected words has an explicit eight-term rival that would be
forced by equality of that pair. Only declared unit factors are canceled.
"""
import gzip
import itertools
import json


def coordinates(word,model):
    a,b,c,d,e,f,g,h=word
    if model=='leaf22':
        return (2*b+f+2*g+2*h, 2*c-g, 2*d-h, e+f+g+h)
    if model=='hub22':
        return (2*b-f, 2*c-g, 2*d-h, e+f+g+h)
    if model=='fourO':
        return (2*b-e-g, 2*c-f-g-h, 2*d-h, e+f+g+h)
    if model=='purehub':
        return (2*b-e, 2*c-f, 2*d-g, h)
    raise AssertionError('Unknown model')


def decode(word,degree):
    assert isinstance(word,str) and len(word)==8 and word.isdigit()
    c=tuple(int(x) for x in word)
    assert sum(c)==degree
    return c


def check_pair(left,right,rival,units,model):
    d=[x-y for x,y in zip(coordinates(left,model),coordinates(right,model))]
    assert any(d)
    for p in units:
        assert p in (2,3)
        while all(x % p==0 for x in d):
            d=[x//p for x in d]
    assert rival !=(1,)*8 and sum(rival)==8
    f=[x-y for x,y in zip(coordinates(rival,model),coordinates((1,)*8,model))]
    pivot=next(i for i,x in enumerate(d) if x)
    assert f[pivot] % d[pivot]==0
    multiplier=f[pivot]//d[pivot]
    assert multiplier !=0
    assert all(y==multiplier*x for x,y in zip(d,f))


def check_file(path):
    with gzip.open(path,'rt',encoding='utf-8') as f:
        data=json.load(f)
    assert data['units'] in ([2],[2,3])
    model=data['model']
    selected=[decode(w,data['degree']) for w in data['words']]
    assert all(max(w)>=2 for w in selected)
    assert len(set(selected))==len(selected)
    assert len({coordinates(w,model) for w in selected})==len(selected)
    pairs=list(itertools.combinations(selected,2))
    assert len(pairs)==len(data['rivals'])
    for (left,right),r in zip(pairs,data['rivals']):
        check_pair(left,right,decode(r,8),data['units'],model)
    # Check that the checker rejects a rival without the required mass.
    rejected=False
    try:
        check_pair(*pairs[0],(0,)*8,data['units'],model)
    except AssertionError:
        rejected=True
    assert rejected
    # A mass-eight vector on a single wrong label must fail the relation.
    bad_rivals=[tuple(8 if i==j else 0 for i in range(8)) for j in range(8)]
    rejected_count=0
    for bad in bad_rivals:
        try:
            check_pair(*pairs[0],bad,data['units'],model)
        except AssertionError:
            rejected_count+=1
    assert rejected_count>0
    return {'file':path,'model':model,'degree':data['degree'],'units':data['units'],
            'forced_distinct_repeated_values':len(selected),
            'positive_pair_certificates_checked':len(pairs),
            'wrong_mass_rejected':True,
            'mass_preserving_pure_corruptions_rejected':rejected_count}


def main():
    paths=['stage41_quartic87_certificate.json.gz',
           'stage41_quintic157_certificate.json.gz',
           'stage41_hub22_quartic90_certificate.json.gz',
           'stage41_fourO_quartic87_certificate.json.gz',
           'stage41_fourO_quintic156_certificate.json.gz',
           'stage41_purehub_quartic89_certificate.json.gz']
    results=[check_file(path) for path in paths]
    assert [x['forced_distinct_repeated_values'] for x in results]==[87,157,90,87,156,89]
    result={'positive_certificates':results,
            'case_proof':'leaf22/fourO: quartic87 gives odd N>=245; remaining sub-248 orders 245,247 are coprime to 3; quintic157/156 and cubic>=92 give N>=249/248. hub22/purehub: quartic90/89 give N>=251/249.',
            'boundary':'Excludes four stated symbolic configurations only. Same-author separate checker; no general interval exclusion or formal verification.'}
    with open('stage41_case_certificate_check_results.json','w',encoding='utf-8') as f:
        json.dump(result,f,indent=2)
        f.write('\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
