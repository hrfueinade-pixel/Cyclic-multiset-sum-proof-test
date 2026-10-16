"""Bounded checks of every rooted double-star template, R3=0 branch.

A double star has two adjacent internal vertices and diameter three.
The marked base is a leaf. Only its relation-derived cyclic quotients
are examined; this is not a sweep over moduli or all tree shapes.
"""

from collections import Counter
from itertools import combinations_with_replacement, permutations
import json
from pathlib import Path
from time import monotonic

from stage6_path_quotients import cyclic_images, valid_with_witness
from stage6_tree_templates import determinant, relation_matrix


def families():
    for p in range(1, 6):
        left = [0] + list(range(3, p + 2))
        right = list(range(p + 2, 8))
        undirected = [(1, 2)] + [(v, 1) for v in left] + [(v, 2) for v in right]
        roots = [1, 2, right[0]] + ([left[1]] if len(left) > 1 else [])
        graph = {i: set() for i in range(8)}
        for x, y in undirected:
            graph[x].add(y)
            graph[y].add(x)
        for root in roots:
            parents = {root: None}
            pending = [root]
            while pending:
                parent = pending.pop()
                for child in graph[parent]:
                    if child not in parents:
                        parents[child] = parent
                        pending.append(child)
            edges = [(i, parents[i]) for i in range(8) if i != root]
            yield p, root, edges


def main():
    start = monotonic()
    limit = 30
    counts = Counter()
    seen = set()
    retained = []
    rejected = []
    complete = True
    family_count = 0
    for p, root, edges in families():
        family_count += 1
        for labels in permutations(range(1, 8)):
            if monotonic() - start > limit:
                complete = False
                break
            counts["label_permutations"] += 1
            if any(label == source for (source, _), label in zip(edges, labels)):
                continue
            counts["admissible_templates"] += 1
            m = relation_matrix(edges, labels)
            if abs(determinant(m)) < 128:
                counts["small_determinant"] += 1
                continue
            verify = counts["admissible_templates"] % 100 == 0
            counts["integer_decomposition_audits"] += verify
            for n, a in cyclic_images(m, verify):
                counts["cyclic_quotient_maps_up_to_units"] += 1
                if len(set(a)) != 8:
                    counts["repeated_point"] += 1
                    continue
                key = n, tuple(sorted(a))
                if key in seen:
                    counts["duplicate_outputs"] += 1
                    continue
                seen.add(key)
                counts["distinct_eight_point_outputs"] += 1
                pairs = {(x + y) % n for x, y in combinations_with_replacement(a, 2)}
                if len(pairs) != 36:
                    counts["pair_sum_failure"] += 1
                    continue
                counts["sidon_outputs"] += 1
                delta = {(x - y) % n for x in a for y in a if x != y}
                assert len(delta) == 56
                if {2 * d % n for d in delta} != delta:
                    counts["doubling_closure_failure"] += 1
                    continue
                counts["h0_outputs"] += 1
                valid, witness = valid_with_witness(a, n)
                record = {"N": n, "A": a, "left_leaf_count": p,
                          "root": root, "labels": labels}
                if valid:
                    counts["valid_h0_outputs"] += 1
                    retained.append(record)
                else:
                    counts["validity_failure"] += 1
                    if len(rejected) < 5:
                        rejected.append({**record, "rival": witness})
        if not complete:
            break
    result = {"family": "rooted double stars with marked leaf, R3=0",
              "rooted_shape_representatives": family_count,
              "seconds_limit": limit, "elapsed_seconds": monotonic() - start,
              "complete_template_family": complete, "counts": dict(counts),
              "valid_retained": retained, "invalid_h0_examples": rejected,
              "scope": "Not all trees; not R3>0; not all h0 sets or moduli."}
    Path("stage6_double_star_quotients.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
