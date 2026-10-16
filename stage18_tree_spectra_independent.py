"""Independent row-pattern enumeration; no producer imports."""
from collections import Counter
from itertools import combinations_with_replacement
import json
from pathlib import Path
from time import monotonic


def partitions(n, maximum=5):
    if n == 0:
        yield ()
    for x in range(min(n, maximum), 0, -1):
        for tail in partitions(n-x, x):
            yield (x,)+tail


def main():
    start=monotonic()
    rows=tuple(partitions(7))
    found={}
    traversed=0
    for indices in combinations_with_replacement(range(len(rows)),8):
        if monotonic()-start > 30:
            raise TimeoutError('Independent relaxation unfinished; no claim')
        traversed+=1
        counts=Counter(x for i in indices for x in rows[i])
        if any(counts[w] % (w+1) for w in range(1,6)):
            continue
        spectrum=tuple(counts[w]//(w+1) for w in range(1,6))
        assert sum(a*m*(m-1)//2 for m,a in enumerate(spectrum,2))==28
        found.setdefault(spectrum,[rows[i] for i in indices])
    saved=json.loads(Path('stage18_tree_spectra_results.json').read_text())
    assert saved['completion']=='COMPLETE'
    assert set(found)=={tuple(r['spectrum_a2_to_a6']) for r in saved['survivors']}
    for entry in saved['survivors']:
        assert len(entry['row_witness'])==8 and all(sum(r)==7 for r in entry['row_witness'])
        assert Counter(x for row in entry['row_witness'] for x in row)==Counter({int(k):v for k,v in entry['items'].items()})
    maximum=max(sum(a*m*(m-1)*(m-2)//6 for m,a in enumerate(s,2)) for s in found)
    assert maximum==saved['maximum_triangles_without_22']
    result={'completion':'COMPLETE','seconds_limit':30,'elapsed_seconds':monotonic()-start,
            'row_patterns':[list(r) for r in rows], 'row_pattern_multisets':traversed,
            'spectrum_count':len(found),'maximum_triangles_without_22':maximum,
            'independent_survivors':[{'spectrum':s,'rows':r} for s,r in sorted(found.items())]}
    Path('stage18_tree_spectra_independent_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('independent_survivors','row_patterns')},indent=2))


if __name__=='__main__':
    main()
