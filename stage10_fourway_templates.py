"""Bounded templates for the two possible four-way cubic fibers.

Only quotient groups of explicit four-variable relation matrices are
examined. This is not a sweep over moduli and does not cover any
three-way fiber. Use --pure for the one-pure branch. The mathematical
reductions and completeness boundary are in stage10_fourway_findings.md.
"""

import argparse
from collections import Counter, defaultdict
from itertools import combinations, combinations_with_replacement, permutations, product
import json
from pathlib import Path
from time import monotonic

from stage6_path_quotients import cyclic_images, valid_with_witness
from stage6_tree_templates import determinant


def vertices():
    # Variables (Y,c1,c2,c3); c0=0 and bj=Y-2cj.
    c = [(0, 0, 0, 0)] + [tuple(int(i == j) for i in range(4)) for j in range(1, 4)]
    b = [tuple(int(i == 0) - 2 * v[i] for i in range(4)) for v in c]
    return c + b


def structural_templates():
    for k in range(4):
        for selected in combinations(range(1, 4), k):
            cluster = (0,) + selected
            for anchor in cluster:
                attached_b = (anchor,) + tuple(j for j in range(1, 4) if j not in selected)
                for destinations in product(range(4), repeat=len(attached_b)):
                    possibilities = []
                    for j, i in zip(attached_b, destinations):
                        outgoing = (4 + j, i)
                        possibilities.append((outgoing,) if j == 0 or i == 0
                                             else (outgoing, (i, 4 + j)))
                    for cross in product(*possibilities):
                        edges = tuple((4, 4 + j) for j in selected) + cross
                        assert len(edges) == 4
                        for labels in permutations(range(4)):
                            yield selected, edges, labels


def pure_structural_templates():
    seen_trees = set()
    for word in product(range(5), repeat=3):
        degree = [1 + word.count(i) for i in range(5)]
        undirected = []
        for parent in word:
            leaf = next(i for i in range(5) if degree[i] == 1)
            undirected.append((leaf, parent))
            degree[leaf] -= 1
            degree[parent] -= 1
        last = [i for i in range(5) if degree[i] == 1]
        undirected.append(tuple(last))
        key = tuple(sorted(tuple(sorted(e)) for e in undirected))
        assert key not in seen_trees
        seen_trees.add(key)
        bb = [i for i, (a, b) in enumerate(undirected) if a in (1, 2, 3) and b in (1, 2, 3)]
        if len(bb) > 1:
            continue
        incident = [i for i, edge in enumerate(undirected) if 0 in edge]
        for attachments in product((1, 2, 3), repeat=len(incident)):
            assigned = dict(zip(incident, attachments))
            lifted = []
            for i, (a, b) in enumerate(undirected):
                def point(v):
                    return assigned[i] if v == 0 else (3 + v if v <= 3 else 7)
                lifted.append((point(a), point(b)))
            for edges in product(*((edge, edge[::-1]) for edge in lifted)):
                for labels in permutations((1, 2, 3, 7)):
                    if any(labels[i] != 7 for i in bb):
                        continue
                    yield tuple(bb), edges, labels
    assert len(seen_trees) == 125


def allowed(edges, labels, k, pure=False):
    if not pure and any(labels[i] == 0 for i in range(k)):
        return False
    groups = defaultdict(list)
    for (source, destination), label in zip(edges, labels):
        assert source != 0 and destination != (0 if pure else 4)
        groups[source].append((destination, label))
    for source, partners in groups.items():
        marks = [(source, 0 if pure else 4)] + partners
        if len(marks) > 4:
            return False
        centers = {c for c, _ in marks}
        assert len(centers) == len(marks)
        if any(label in centers and label != c for c, label in marks):
            return False
        if sum(c == label for c, label in marks) > 1:
            return False
    return True


def make_matrix(edges, labels, pure=False):
    if pure:
        c = [(0, 0, 0, 0)] + [tuple(int(i == j) for i in range(4)) for j in range(3)]
        v = c + [tuple(-2 * x for x in c[i]) for i in range(1, 4)] + [(0, 0, 0, 1)]
        row_index = {label: i for i, label in enumerate((1, 2, 3, 7))}
    else:
        v = vertices()
        row_index = {i: i for i in range(4)}
    rows = [None] * 4
    for (source, destination), label in zip(edges, labels):
        rows[row_index[label]] = tuple(2 * v[source][i] + (int(i == 0) if not pure else 0)
                                       - 2 * v[destination][i] - v[label][i] for i in range(4))
    assert all(row is not None for row in rows)
    return tuple(rows)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pure", action="store_true", help="Use the one-pure four-way branch")
    pure = parser.parse_args().pure
    start = monotonic()
    seconds_limit = 15 if pure else 12
    counts = Counter()
    det_counts = Counter()
    matrices = set()
    output_sets = set()
    valid_sets = []
    invalid_h0 = []
    complete = True
    templates = pure_structural_templates() if pure else structural_templates()
    for selected, edges, labels in templates:
        if monotonic() - start > seconds_limit:
            complete = False
            break
        counts["labeled_structural_templates"] += 1
        assert counts["labeled_structural_templates"] <= (395136 if pure else 116640)
        if not allowed(edges, labels, len(selected), pure):
            counts["local_support_rejection"] += 1
            continue
        counts["locally_admissible_templates"] += 1
        matrix = make_matrix(edges, labels, pure)
        if matrix in matrices:
            counts["duplicate_matrices"] += 1
            continue
        matrices.add(matrix)
        counts["distinct_matrices"] += 1
        det = abs(determinant([list(row) for row in matrix]))
        assert det % 2 == 1 and det <= 2187
        det_counts[det] += 1
        if det < 184:
            counts["determinant_below_184"] += 1
            continue
        counts["large_matrices"] += 1
        for n, image in cyclic_images([list(row) for row in matrix],
                                      verify=True, minimum_order=184):
            counts["cyclic_quotient_maps_up_to_units"] += 1
            if pure:
                *c, x = image[1:]
                a = (0,) + tuple(c) + tuple(-2 * z % n for z in c) + (x,)
            else:
                y, *tail = image[1:]
                c = (0,) + tuple(tail)
                a = c + tuple((y - 2 * x) % n for x in c)
            assert len(a) == 8
            if len(set(a)) != 8:
                counts["repeated_point"] += 1
                continue
            key = n, tuple(sorted(a))
            if key in output_sets:
                counts["duplicate_eight_point_outputs"] += 1
                continue
            output_sets.add(key)
            counts["distinct_eight_point_outputs"] += 1
            if len({(x + z) % n for x, z in combinations_with_replacement(a, 2)}) != 36:
                counts["pair_sum_failure"] += 1
                continue
            counts["sidon_outputs"] += 1
            delta = {(x - z) % n for x in a for z in a if x != z}
            assert len(delta) == 56
            if {2 * d % n for d in delta} != delta:
                counts["doubling_closure_failure"] += 1
                continue
            counts["h0_outputs"] += 1
            accepted, rival = valid_with_witness(a, n)
            record = {"N": n, "A": a, "matrix": matrix,
                      "BB_structure": selected, "edges": edges, "labels": labels}
            if accepted:
                counts["valid_h0_outputs"] += 1
                valid_sets.append(record)
            else:
                counts["validity_failure"] += 1
                if len(invalid_h0) < 12:
                    invalid_h0.append({**record, "rival": rival})
    result = {"family": "Four-way cubic fibers, " + ("one pure cubic" if pure else "disjoint centers and labels (no pure cubic)"),
              "seconds_limit": seconds_limit, "elapsed_seconds": monotonic() - start,
              "complete_template_family": complete, "counts": dict(counts),
              "determinant_counts": dict(sorted(det_counts.items())),
              "valid_retained": valid_sets, "invalid_h0_examples": invalid_h0,
              "scope": "Only this four-way branch; not three-way fibers or all h0 sets/moduli."}
    output = "stage10_fourway_pure_results.json" if pure else "stage10_fourway_template_results.json"
    Path(output).write_text(
        json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(json.dumps({k: v for k, v in result.items() if k != "determinant_counts"}, indent=2))


if __name__ == "__main__":
    main()
