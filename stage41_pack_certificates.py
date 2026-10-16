"""Package fixed positive witnesses; does not rerun discovery or certify absence."""
import gzip
import json
from pathlib import Path


CASES=[
    ('stage41_saturated_fiber_closure_results.json','stage41_quartic87_certificate.json.gz','leaf22',4,[2]),
    ('stage41_saturated_fiber_quintic_results.json','stage41_quintic157_certificate.json.gz','leaf22',5,[2,3]),
    ('stage41_hub22_quartic_results.json','stage41_hub22_quartic90_certificate.json.gz','hub22',4,[2]),
    ('stage41_fourO_quartic_results.json','stage41_fourO_quartic87_certificate.json.gz','fourO',4,[2]),
    ('stage41_fourO_quintic_results.json','stage41_fourO_quintic156_certificate.json.gz','fourO',5,[2,3]),
    ('stage41_purehub_quartic_results.json','stage41_purehub_quartic89_certificate.json.gz','purehub',4,[2])]


def main():
    summaries=[]
    for source,target,model,degree,units in CASES:
        d=json.loads(Path(source).read_text(encoding='utf-8'))
        data={'model':model,'degree':degree,'units':units,
              'words':[''.join(map(str,r['quartic_word'])) for r in d['selected']],
              'rivals':[(''.join(map(str,p['rival'])) if isinstance(p,dict) else p[2])
                        for p in d['pair_certificates']]}
        Path(target).write_bytes(gzip.compress(json.dumps(data,separators=(',',':')).encode(),mtime=0))
        summaries.append({'source':source,'certificate':target,'model':model,
                          'degree':degree,'units':units,'positive_clique_size':d['clique_size'],
                          'search_complete':d['search_complete'],'search_nodes':d['search_nodes'],
                          'elapsed_seconds':d['elapsed_seconds'],
                          'compressed_bytes':Path(target).stat().st_size})
    Path('stage41_discovery_summary.json').write_text(json.dumps({
        'retained_positive_certificates':summaries,
        'boundary':'Only positive certificates establish lower bounds. Search completion or optimality is unnecessary and is not claimed.'},indent=2)+'\n',encoding='utf-8')
    print(json.dumps(summaries,indent=2))


if __name__=='__main__':
    main()
