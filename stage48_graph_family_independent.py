"""Independent complete cubic-center graph-class consistency checks.

Reuses the already checked C8 record. New fixed-order bit-mask checks only
for C5+C3 and C4+C4; no producer imports, residues or group parameters.
"""
from itertools import combinations
from pathlib import Path
import json
import time


def run(name, cycles):
    started = time.monotonic()
    vertices = tuple(range(8))
    omitted = set()
    for cycle in cycles:
        for a,b in zip(cycle,cycle[1:]+cycle[:1]):
            omitted.add(tuple(sorted((a,b))))
    graph = tuple(e for e in combinations(vertices,2) if e not in omitted)
    adjacency = [sum(1<<b for b in vertices if tuple(sorted((a,b))) in graph) for a in vertices]
    assert len(graph) == 20 and all(m.bit_count() == 5 for m in adjacency)
    pairbits = {p:1<<i for i,p in enumerate(combinations(vertices,2))}
    options = []
    for c,d in graph:
        common = adjacency[c]&adjacency[d]
        opts = []
        for a in vertices:
            for b in vertices:
                if a==b or not(common>>a&1) or not(common>>b&1): continue
                free = [e for e in vertices if e not in (a,b,c,d)]
                left = sum(pairbits[tuple(sorted((a,e)))] for e in free)
                right = sum(pairbits[tuple(sorted((b,e)))] for e in free)
                opts.append((left,right))
        options.append(opts)
    nodes = 0
    def descend(depth,used):
        nonlocal nodes
        nodes += 1
        if time.monotonic()-started>5: raise TimeoutError
        if depth==20: return True
        c,d = graph[depth]
        for left,right in options[depth]:
            if used[c]&left or used[d]&right: continue
            following = list(used)
            following[c] |= left
            following[d] |= right
            if descend(depth+1,tuple(following)): return True
        return False
    try:
        found = descend(0,(0,)*8)
        status = 'ASSIGNMENT' if found else 'COMPLETE_NO_ASSIGNMENT'
    except TimeoutError:
        status = 'TIMEOUT'
    return {'name':name,'cycles':cycles,'edges':graph,'option_counts':[len(o) for o in options],
            'status':status,'nodes':nodes,'cap_seconds':5,
            'runtime_seconds':time.monotonic()-started}


def main():
    here = Path(__file__).parent
    old = json.loads((here/'stage48_fixed_graph_independent_results.json').read_text())
    assert old['status']=='COMPLETE_NO_ASSIGNMENT'
    old.update({'name':'C8','cycles':[list(range(8))],'reused_independent_completed_record':True})
    records = [old,run('C5+C3',[[0,1,2,3,4],[5,6,7]]),
               run('C4+C4',[[0,1,2,3],[4,5,6,7]])]
    producer = json.loads((here/'stage48_cubic_graph_family_probe_results.json').read_text())
    for actual,reference in zip(records,producer['results']):
        assert [list(e) for e in actual['edges']] == reference['edges']
        assert actual['option_counts'] == reference['option_counts']
        assert actual['status']==reference['status']=='COMPLETE_NO_ASSIGNMENT'
    # Every simple two-regular graph on8 vertices is a union of cycles>=3;
    # these are exactly the integer partitions of8 into parts>=3.
    partitions=[]
    def parts(left,minimum,prefix):
        if left==0: partitions.append(prefix); return
        for k in range(minimum,left+1): parts(left-k,k,prefix+[k])
    parts(8,3,[])
    assert partitions==[[3,5],[4,4],[8]]
    # Uniform degree bound 4deg<=21 and degree sum40 force all degrees5.
    assert 21//4==5 and 8*5==40
    result={'scope':'All3 necessary complement2-regular graphclasses under C4=0,P3ordinary20 and ordinary quartic cap3; R3 need not be zero.',
            'records':records,'cycle_type_coverage':partitions,
            'conditional_consequence':'Under full validity in odd order,ordinary quartic cap3 and C4=0, P3ordinary<=19.',
            'boundary':'Computer-assisted symbolic tail/lift exclusion. No cyclic-set or modulus sweep.'}
    (here/'stage48_graph_family_independent_results.json').write_text(
        json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps([{k:r[k] for k in ('name','status','nodes')} for r in records]))


if __name__=='__main__': main()
