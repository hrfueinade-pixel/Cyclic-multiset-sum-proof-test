"""A bounded proof experiment on quartic WORDS, not cyclic residue sets.

An edge means validity in an odd group forbids the two words from sharing
a value, even after cancelling a common power of two in their difference.
A clique of 89 repeated words would prove the desired growth outright.
The search does not certify moduli or infer absence from a timeout.
"""
import argparse
import itertools
import json
import time
from collections import Counter


def words():
    result = []
    for indices in itertools.combinations_with_replacement(range(8), 4):
        c = tuple(indices.count(i) for i in range(8))
        if max(c) > 1:
            result.append(c)
    return result


def separated(u, v):
    d = [a - b for a, b in zip(u, v)]
    while all(x % 2 == 0 for x in d):
        d = [x // 2 for x in d]
    return min(d) >= -1 or max(d) <= 1


def maximum_clique(adj, seconds):
    deadline = time.monotonic() + seconds
    best = []
    nodes = 0
    complete = True

    def color_sort(vertices):
        order, bounds = [], []
        color = 0
        remaining = vertices
        while remaining:
            color += 1
            available = remaining
            while available:
                bit = available & -available
                v = bit.bit_length() - 1
                remaining ^= bit
                available ^= bit
                available &= ~adj[v]
                order.append(v)
                bounds.append(color)
        return order, bounds

    def expand(clique, candidates):
        nonlocal best, nodes
        nodes += 1
        if nodes % 256 == 0 and time.monotonic() > deadline:
            raise TimeoutError
        order, bounds = color_sort(candidates)
        for i in range(len(order) - 1, -1, -1):
            if len(clique) + bounds[i] <= len(best):
                return
            v = order[i]
            next_clique = clique + [v]
            next_candidates = candidates & adj[v]
            if next_candidates:
                expand(next_clique, next_candidates)
            elif len(next_clique) > len(best):
                best = next_clique
            candidates &= ~(1 << v)

    root = (1 << len(adj)) - 1
    root_order, root_bounds = color_sort(root)
    root_bound = root_bounds[-1]
    root_colors = [0] * len(adj)
    for v, color in zip(root_order, root_bounds):
        root_colors[v] = color
    assert all(root_colors[i] != root_colors[j] for i in range(len(adj))
               for j in range(i) if (adj[i] >> j) & 1)
    try:
        expand([], root)
    except TimeoutError:
        complete = False
    return best, root_bound, complete, nodes, root_colors


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--seconds', type=float, default=10)
    p.add_argument('--output', default='stage40_odd_collision_graph_results.json')
    args = p.parse_args()
    start = time.monotonic()
    w = words()
    adj = [0] * len(w)
    for i, u in enumerate(w):
        for j in range(i):
            if separated(u, w[j]):
                adj[i] |= 1 << j
                adj[j] |= 1 << i
    clique, upper, complete, nodes, colors = maximum_clique(adj, args.seconds)
    assert all(separated(w[i], w[j]) for i, j in itertools.combinations(clique, 2))
    result = {
        'scope': '260 repeated quartic count vectors; no moduli enumerated',
        'edge_rule': 'divide difference by its common power of two; one sign bounded by one',
        'target_clique_size': 89,
        'clique_size': len(clique),
        'root_coloring_upper_bound': upper,
        'maximum_clique_search_complete': complete,
        'maximum_clique_upper_bound': len(clique) if complete else upper,
        'search_nodes': nodes,
        'clique': [w[i] for i in clique],
        'proper_coloring': [{'word': c, 'color': color} for c, color in zip(w, colors)],
        'clique_types': dict(Counter(''.join(map(str, sorted((x for x in w[i] if x), reverse=True))) for i in clique)),
        'elapsed_seconds': time.monotonic() - start,
        'boundary': 'The 36-clique alone does not determine chromatic number. The explicit proper 65-coloring bounds chromatic number above, but is not a cyclic sumset realization; separation is only a sufficient pairwise rule.'
    }
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2)
        f.write('\n')
    print(json.dumps({k: v for k, v in result.items()
                      if k not in ('clique', 'proper_coloring')}, indent=2))


if __name__ == '__main__':
    main()
