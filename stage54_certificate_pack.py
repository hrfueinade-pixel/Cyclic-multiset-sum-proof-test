"""Compact positive proof: chosen words plus reproducible identity reconstruction.

The large local discovery witness files are retained locally. This archive
stores each complete model and its selected quartic words; the standalone
checker constructs and checks a positive rival identity for EVERY pair.
"""
from pathlib import Path
import gzip
import hashlib
import json

HERE=Path(__file__).parent


def load(name): return json.loads((HERE/name).read_text())


def positive(record):
    raw=json.loads(gzip.decompress((HERE/record['certificate']).read_bytes()))
    assert record['units']==[2]
    if raw.get('kind')=='direct_rival':
        return {'kind':'rival','word':raw['rival']}
    assert record['positive_bound']>=89 and raw['degree']==4
    return {'kind':'growth89','words':raw['words'][:89]}


def compact(record,keep_model=False):
    out={'index':record['index'],'direction':record['coefficient_direction'],
         'words':[''.join(map(str,w)) for w in record['words']]}
    if record['exclusion']:
        out['exclusion']=record['exclusion']
    else:
        out['U']=record['reduction']['U']
        out['gcd']=record['reduction']['gcd']
        out['odd_gcd']=record['reduction']['odd_gcd']
        if record['closed']:
            out['positive']=positive(record['growth'])
        else:
            assert keep_model
            out['residual']=True
    return out


def main():
    source=load('stage54_source_triple_results.json')
    first=load('stage54_source_path_cubic_inventory_results.json')
    second=load('stage54_source_path_second_cubic_results.json')
    assert first['inventory_complete'] and second['complete'] and second['all_closed']
    base=next(r for r in source['records'] if r['tail']==[3,6])
    data={'base_relations':base['relations'],'base_parameterization':base['parameterization'],
          'source_cases':[],'first':[compact(r,True) for r in first['cases']],
          'second':[],'boundary':'Complete symbolic source-triple exclusion in hypothetical odd N<248; general weighted inequality remains open.'}
    for r in source['records']:
        item={'tail':r['tail']}
        if r['exclusion']:
            item['exclusion']=r['exclusion']
        elif r['tail']==[4,6]:
            item['parameterization']=r['parameterization']; item['positive']=positive(r['growth'])
        elif r['tail'] in ([3,7],[4,7]):
            item['mirror_of']=[r['tail'][0],6]
        else:
            assert r['tail']==[3,6]
            item['path_inventory']=True
        data['source_cases'].append(item)
    for parent in second['parents']:
        assert parent['complete'] and all(r['closed'] for r in parent['cases'])
        data['second'].append({'parent':parent['parent'],'cases':[compact(r) for r in parent['cases']]})
    dest=HERE/'stage54_source_certificates.json.gz'
    dest.write_bytes(gzip.compress(json.dumps(data,separators=(',',':')).encode(),mtime=0))
    print(json.dumps({'file':dest.name,'bytes':dest.stat().st_size,
                      'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()}))


if __name__=='__main__': main()
