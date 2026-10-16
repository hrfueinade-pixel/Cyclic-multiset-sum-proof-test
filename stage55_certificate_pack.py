"""Compact new proof data replacing every cap-two exception of Stage 53."""
from itertools import combinations
from pathlib import Path
import gzip
import hashlib
import json

from stage54_certificate_check import determinant,unit2

HERE=Path(__file__).parent


def compact(r):
    out={k:r[k] for k in ('scope','index','root','first_closure','left','right') if k in r}
    out['rows']=r['rows']; out['splits']=r['splits']
    if r.get('exclusion'):
        out['exclusion']=r['exclusion']; return out
    if not r['closed']:
        out['residual']=True; return out
    raw=json.loads(gzip.decompress((HERE/r['growth']['certificate']).read_bytes()))
    assert r['growth']['units']==[2]
    if raw.get('kind')=='direct_rival': out['positive']={'kind':'rival','word':raw['rival']}
    else:
        assert r['growth']['positive_bound']>=89
        out['positive']={'kind':'growth89','words':raw['words'][:89]}
    if r.get('complete_parameterization'):
        p=r['complete_parameterization']
        out['unit']=p['unit']; out['U']=p['U']
        if p['U'] is not None: out['gcd']=p['gcd']; out['odd_gcd']=p['odd_gcd']
    else:
        p=r['parameterization']; piv=p['pivots']; k=len(piv)
        chosen=next(c for c in combinations(range(len(r['rows'])),k)
                    if unit2(abs(determinant([[r['rows'][i][j] for j in piv] for i in c]))))
        out['unit']={k:p[k] for k in ('rows','scale','free_labels','pivots')}
        out['unit']['selected_rows']=chosen; out['U']=None
    return out


def main():
    data=json.loads((HERE/'stage55_split_exception_results.json').read_text())
    selected=[r for r in data['records'] if r['scope'] in ('root','edge','marks')]
    assert len(selected)==46 and all(r['closed'] for r in selected)
    assert len(data['triangle_marks'])==2 and all(r['closed'] for r in data['triangle_marks'])
    assert len(data['cubic_first'])==36 and data['cubic_survivors']==[7,10,19,22,31,34]
    assert len(data['cubic_pairs'])==15 and all(r['closed'] for r in data['cubic_pairs'])
    proof={'graph_exceptions':[compact(r) for r in selected],
           'triangle_marks':[compact(r) for r in data['triangle_marks']],
           'cubic_first':[compact(r) for r in data['cubic_first']],
           'cubic_pairs':[compact(r) for r in data['cubic_pairs']],
           'prior53_sha256':hashlib.sha256((HERE/'stage53_split_graph_certificates.json.gz').read_bytes()).hexdigest(),
           'prior54_sha256':hashlib.sha256((HERE/'stage54_source_certificates.json.gz').read_bytes()).hexdigest()}
    dest=HERE/'stage55_general_assignment_certificates.json.gz'
    dest.write_bytes(gzip.compress(json.dumps(proof,separators=(',',':')).encode(),mtime=0))
    print(json.dumps({'file':dest.name,'bytes':dest.stat().st_size,
                      'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()}))


if __name__=='__main__': main()
