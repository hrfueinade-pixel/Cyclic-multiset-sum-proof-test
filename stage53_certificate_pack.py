"""Package only explicit Stage 53 identities and the needed closed-split bound."""
import gzip
import hashlib
import json
from pathlib import Path

HERE=Path(__file__).parent
names={
    'marked_edge':'stage53_connected_split_probe_results.json',
    'marked_path':'stage53_path_propagation_results.json',
    'degree_three':'stage53_three_open_reuse_results.json',
    'two_marks':'stage53_isolated_mark_compensation_results.json',
}
data={key:json.loads((HERE/name).read_text()) for key,name in names.items()}
source=HERE/'stage49_closed_split_quartic_probe_results.json'
if source.exists():
    old=json.loads(source.read_text())
    selected=sorted(old['clique_nodes'])
    lookup={node:i for i,node in enumerate(selected)}
    data['closed_split']={
        'coefficient_rows':old['coefficient_rows'],
        'target':old['target'],
        'words':[old['nodes'][i]['quartic_word'] for i in selected],
        'pairs':[{'indices':[lookup[i] for i in r['nodes']],
                  'rival':r['rival'],'factor':r['unit_multiplier'],
                  'multiplier':r['quartic_difference_multiplier']}
                 for r in old['pair_certificates']],
        'source':'Positive 116-value Stage 49 certificate; no historical producer rerun.',
    }
else:
    shipped=json.loads(gzip.decompress((HERE/'stage53_split_graph_certificates.json.gz').read_bytes()))
    data['closed_split']=shipped['closed_split']
data['boundary']='Symbolic coverage and integer identities only; no moduli/parameters enumerated; full triangle branch remains open.'
dest=HERE/'stage53_split_graph_certificates.json.gz'
raw=json.dumps(data,separators=(',',':')).encode()
dest.write_bytes(gzip.compress(raw,mtime=0))
print(json.dumps({'file':dest.name,'bytes':dest.stat().st_size,
                  'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()}))
