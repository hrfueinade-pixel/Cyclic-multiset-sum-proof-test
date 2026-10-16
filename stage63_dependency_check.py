"""Check saved proof-package integrity; does not replace proof checkers."""
from pathlib import Path
import hashlib,json


def main():
    root=Path(__file__).parent;p=json.loads((root/'stage63_proof_manifest.json').read_text())
    def read(name):
        if(root/name).exists():return(root/name).read_bytes()
        parts=p['archive_parts'][name]
        return b''.join((root/item['path']).read_bytes()for item in parts)
    for item in p['files']:
        raw=read(item['path'])
        assert len(raw)==item['bytes'] and hashlib.sha256(raw).hexdigest()==item['sha256']
    for items in p['archive_parts'].values():
        for item in items:
            raw=(root/item['path']).read_bytes()
            assert len(raw)==item['bytes']and hashlib.sha256(raw).hexdigest()==item['sha256']
    for archive,check in p['archive_checks']:
        record=json.loads((root/check).read_text())
        assert record['archive_sha256']==hashlib.sha256(read(archive)).hexdigest()
    c=json.loads((root/'stage62_check_results.json').read_text());assert c['checked_shapes']==['3221']
    f=json.loads((root/'stage63_finishing_results.json').read_text())
    assert f['distinct_pair_sum_rival_identities']==224
    assert all(f['forests'][s]['triangles']==1 and f['forests'][s]['open_paired_edges']>=2
               and f['forests'][s]['twice_N_lower']>494 for s in('22211','4211'))
    assert f['sharp_construction_coin_minima']==[8,9,11,12]
    print(json.dumps({'verified_package_files':len(p['files']),'matched_archive_checks':len(p['archive_checks']),
                     'full_conclusion':'N_min=248, using the proved prior chain and checked symbolic exclusions',
                     'scope':'Package integrity check; not an independent mathematical review.'}))


if __name__=='__main__':main()
