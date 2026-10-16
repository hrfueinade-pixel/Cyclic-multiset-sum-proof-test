"""New targeted remaining two complement classes; reuse completed C8 record.

This is exactly three symbolic graph classes, no cyclic-set/modulus sweep.
"""
from itertools import combinations, permutations
from pathlib import Path
import json
import time


def run(name, cycles):
    labels = set(range(8))
    omitted = {tuple(sorted((cycle[i], cycle[(i+1) % len(cycle)])))
               for cycle in cycles for i in range(len(cycle))}
    edges = [e for e in combinations(range(8), 2) if e not in omitted]
    neighbors = {c: {d for d in labels if tuple(sorted((c,d))) in edges} for c in labels}
    assert len(edges) == 20 and all(len(x) == 5 for x in neighbors.values())
    options = {}
    for c,d in edges:
        options[c,d] = []
        for a,b in permutations(sorted(neighbors[c] & neighbors[d]), 2):
            free = labels-{c,d,a,b}
            options[c,d].append((a,b,{tuple(sorted((a,e))) for e in free},
                                {tuple(sorted((b,e))) for e in free}))
    used = {c:set() for c in labels}
    chosen = {}
    nodes = 0
    timeout = False
    start = time.monotonic()

    def solve():
        nonlocal nodes, timeout
        nodes += 1
        if time.monotonic()-start > 5:
            timeout = True
            return None
        if len(chosen) == 20:
            return dict(chosen)
        best, available = None,None
        for c,d in edges:
            if (c,d) in chosen:
                continue
            candidates = [o for o in options[c,d]
                          if not(o[2]&used[c]) and not(o[3]&used[d])]
            if not candidates:
                return None
            if available is None or len(candidates)<len(available):
                best,available=(c,d),candidates
        c,d=best
        for a,b,cw,dw in available:
            used[c].update(cw)
            used[d].update(dw)
            chosen[c,d]=(a,b)
            result=solve()
            if result is not None or timeout:
                return result
            del chosen[c,d]
            used[c].difference_update(cw)
            used[d].difference_update(dw)
        return None

    assignment=solve()
    return {'name':name,'cycles':cycles,'edges':edges,
            'option_counts':[len(options[e]) for e in edges],
            'status':'SYMBOLIC_ASSIGNMENT' if assignment else
                     ('TIMEOUT' if timeout else 'COMPLETE_NO_ASSIGNMENT'),
            'nodes':nodes,'runtime_seconds':time.monotonic()-start,'cap_seconds':5,
            'assignment':[{'centers':e,'tails':assignment[e]} for e in edges]
                         if assignment else None}


if __name__=='__main__':
    old=json.loads(Path('stage48_fixed_cubic_graph_probe_results.json').read_text())
    assert old['status']=='COMPLETE_NO_ASSIGNMENT'
    c8={k:old[k] for k in ('edges','option_counts','status','nodes','runtime_seconds','cap_seconds','assignment')}
    c8.update({'name':'C8','cycles':[list(range(8))],'reused_completed_record':True})
    results=[c8,run('C5+C3',[[0,1,2,3,4],[5,6,7]]),
             run('C4+C4',[[0,1,2,3],[4,5,6,7]])]
    output={'scope':'Three complement two-regular graphs forced by R3=0,C4=0,P3ordinary20.',
            'C8_record':'stage48_fixed_cubic_graph_probe_results.json',
            'results':results,
            'boundary':'Symbolic necessary tail/lift consistency only. No actual group parameters.'}
    Path('stage48_cubic_graph_family_probe_results.json').write_text(
        json.dumps(output,indent=2)+'\n',encoding='utf-8')
    print(json.dumps([{k:r[k] for k in ('name','status','nodes','runtime_seconds')} for r in results]))
