"""Targeted fixed K8-minus-cycle cubic-tail consistency check.

No residues/group parameters. Tests R3=0, C4=0, P4=4*P3 for THIS graph.
Stop on a symbolic assignment, complete exhaustion, or a new five-second cap.
"""
from itertools import combinations, permutations
from pathlib import Path
import json
import time


def main():
    labels = set(range(8))
    edges = [(c, d) for c, d in combinations(range(8), 2)
             if (d-c) not in (1, 7)]
    neighbors = {c: {d for d in labels if tuple(sorted((c, d))) in edges} for c in labels}
    assert len(edges) == 20 and all(len(n) == 5 for n in neighbors.values())
    options = {}
    for c, d in edges:
        common = neighbors[c] & neighbors[d]
        opts = []
        for a, b in permutations(sorted(common), 2):
            free = labels - {c, d, a, b}
            cwords = {tuple(sorted((a, e))) for e in free}
            dwords = {tuple(sorted((b, e))) for e in free}
            assert len(cwords) == len(dwords) == 4
            opts.append((a, b, cwords, dwords))
        options[c, d] = opts
    used = {c: set() for c in labels}
    chosen = {}
    nodes = 0
    started = time.monotonic()
    timed_out = False

    def solve():
        nonlocal nodes, timed_out
        nodes += 1
        if time.monotonic()-started > 5:
            timed_out = True
            return None
        if len(chosen) == len(edges):
            return dict(chosen)
        best_edge, best = None, None
        for c, d in edges:
            if (c, d) in chosen:
                continue
            available = [o for o in options[c, d]
                         if not (o[2] & used[c]) and not (o[3] & used[d])]
            if not available:
                return None
            if best is None or len(available) < len(best):
                best_edge, best = (c, d), available
        c, d = best_edge
        for a, b, cw, dw in best:
            used[c].update(cw)
            used[d].update(dw)
            chosen[c, d] = (a, b)
            result = solve()
            if result is not None or timed_out:
                return result
            del chosen[c, d]
            used[c].difference_update(cw)
            used[d].difference_update(dw)
        return None

    result = solve()
    status = 'SYMBOLIC_ASSIGNMENT' if result else ('TIMEOUT' if timed_out else 'COMPLETE_NO_ASSIGNMENT')
    output = {'scope': 'Only fixed cubic center graph K8 minus cycle012345670.',
              'status': status, 'nodes': nodes, 'runtime_seconds': time.monotonic()-started,
              'cap_seconds': 5,
              'edges': edges, 'option_counts': [len(options[e]) for e in edges],
              'assignment': [{'centers': e, 'tails': result[e]} for e in edges] if result else None,
              'constraints': ['Each cubic pair 2c+a=2d+b has tails in common graph neighbors.',
                              'Its four ordinary quartic lifts at each center are distinct from '
                              'all lifts of other cubic pairs at that center.'],
              'boundary': 'No cyclic-set realization or universal graph coverage is asserted.'}
    Path('stage48_fixed_cubic_graph_probe_results.json').write_text(
        json.dumps(output, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k: output[k] for k in ('status', 'nodes', 'runtime_seconds')}))


if __name__ == '__main__':
    main()
