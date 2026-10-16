"""Independent bit-mask check of ONE declared cubic-center graph.

Functional fixed-edge-order recursion, no producer imports and no residues.
"""
from itertools import combinations
from pathlib import Path
import json
import time


def main():
    started = time.monotonic()
    vertex = tuple(range(8))
    graph = tuple((a,b) for a,b in combinations(vertex,2) if (b-a)%8 not in (1,7))
    adjacency = [sum(1<<b for b in vertex if (min(a,b),max(a,b)) in graph) for a in vertex]
    assert len(graph) == 20 and all(m.bit_count() == 5 for m in adjacency)
    pairbits = {p: 1<<i for i,p in enumerate(combinations(vertex,2))}
    options = []
    for c,d in graph:
        common = adjacency[c] & adjacency[d]
        opts = []
        for a in vertex:
            if not common>>a&1: continue
            for b in vertex:
                if b == a or not common>>b&1: continue
                free = [e for e in vertex if e not in (a,b,c,d)]
                left = sum(pairbits[tuple(sorted((a,e)))] for e in free)
                right = sum(pairbits[tuple(sorted((b,e)))] for e in free)
                assert left.bit_count() == right.bit_count() == 4
                opts.append((a,b,left,right))
        options.append(opts)
    nodes = 0
    def descend(depth, used):
        nonlocal nodes
        nodes += 1
        if time.monotonic()-started > 5:
            raise TimeoutError
        if depth == len(graph): return True
        c,d = graph[depth]
        for a,b,left,right in options[depth]:
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
    result = {'scope':'ONE fixed K8-minus-012345670-cycle graph; no universal graph coverage.',
              'status':status,'nodes':nodes,'cap_seconds':5,
              'runtime_seconds':time.monotonic()-started,
              'edges':graph,'option_counts':[len(o) for o in options],
              'boundary':'Conditional symbolic graph exclusion only. No cyclic set or modulus search.'}
    (Path(__file__).with_name('stage48_fixed_graph_independent_results.json')).write_text(
        json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ('status','nodes','runtime_seconds')}))


if __name__ == '__main__': main()
