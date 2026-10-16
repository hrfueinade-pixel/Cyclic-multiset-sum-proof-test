"""Bounded symbolic necessary-condition audit, not a valid-set search.

Scope: 588 pairs of partner choices and 2744 triples, five-second cap.
Coordinates are eight formal distinct points: c0,c1,c2,b0,b1,b2,x,y.
Every short-relation rejection carries an exact balanced certificate.
"""

from collections import Counter
from itertools import combinations, product
import argparse
import json
from pathlib import Path
from time import monotonic


NAMES = ("c0", "c1", "c2", "b0", "b1", "b2", "x", "y")


def vector(*terms):
    result = [0] * 8
    for index, coefficient in terms:
        result[index] += coefficient
    return tuple(result)


def choices(i):
    result = []
    for j in range(3):
        if j != i:
            result.extend((("U", i + 3, j + 3),
                           ("V", j + 3, i + 3)))
    for f in (6, 7):
        result.append(("S", i + 3, f))
        result.extend(("D", f, j + 3) for j in range(3))
        result.append(("M", f, 13 - f))
    assert len(result) == 14
    return tuple(result)


def partner_vector(i, choice):
    _, p, q = choice
    return vector((i, 3), (p, -2), (q, -1))


def short_certificate(i, a, j, b):
    rows = (partner_vector(i, a), partner_vector(j, b),
            vector((j, 2), (j + 3, 1), (i, -2), (i + 3, -1)))
    for coefficients in product((-1, 0, 1), repeat=3):
        relation = tuple(sum(k * row[t] for k, row in zip(coefficients, rows))
                         for t in range(8))
        assert sum(relation) == 0
        if not any(relation):
            continue
        if min(relation) >= -1:
            return {"coefficients": coefficients, "relation": relation,
                    "rival_counts": tuple(1 + v for v in relation)}
    return None


def reuse_failure(pattern):
    m_centers = [i for i, a in enumerate(pattern) if a[0] == "M"]
    if len(m_centers) > 1:
        return "free_free_at_two_centers"
    for i, j in combinations(range(3), 2):
        a, b = pattern[i], pattern[j]
        if a[1] == b[1] and a[1] in (6, 7):
            if a[2] != i + 3 or b[2] != j + 3:
                return "shared_free_double_wrong_singleton"
    for f in (6, 7):
        if sum(a[1] == f for a in pattern) == 3:
            return "free_double_at_three_centers"
        if sum(a[0] == "S" and a[2] == f for a in pattern) == 3:
            return "S_role_at_three_centers"
    return None


def tree_edges(pattern):
    trees = [[] for _ in range(8)]
    for i in range(3):
        for j in range(3):
            if i != j:
                trees[i + 3].append((i, j, j + 3))
    for i, (_, p, q) in enumerate(pattern):
        trees[i].append((i, p, q))
        trees[q].append((p, i, i))
    return trees


def tree_failure(trees):
    for base, edges in enumerate(trees):
        labels, endpoints = {}, {}
        parent = list(range(8))

        def root(v):
            while parent[v] != v:
                v = parent[v]
            return v

        for d, e, label in edges:
            if label == base or d == e or e == base:
                return {"reason": "forbidden_tree_edge", "base": base}
            if label in labels:
                if labels[label] != (d, e):
                    return {"reason": "duplicate_tree_label", "base": base}
                continue
            labels[label] = (d, e)
            pair = tuple(sorted((d, e)))
            if pair in endpoints:
                return {"reason": "duplicate_tree_edge", "base": base}
            endpoints[pair] = label
            r, s = root(d), root(e)
            if r == s:
                return {"reason": "tree_cycle", "base": base}
            parent[r] = s
    return None


def display(pattern):
    return [{"center": NAMES[i], "type": a[0],
             "doubled": NAMES[a[1]], "singleton": NAMES[a[2]]}
            for i, a in enumerate(pattern)]


def run(cap):
    start = monotonic()
    options = [choices(i) for i in range(3)]
    certificates = {}
    rejects = Counter()
    survivors = []
    pair_count = triple_count = 0
    complete = False
    try:
        for i, j in combinations(range(3), 2):
            for ai, a in enumerate(options[i]):
                for bj, b in enumerate(options[j]):
                    if monotonic() - start > cap:
                        raise TimeoutError
                    pair_count += 1
                    certificate = short_certificate(i, a, j, b)
                    if certificate:
                        assert min(certificate["rival_counts"]) >= 0
                        assert sum(certificate["rival_counts"]) == 8
                        certificates[(i, ai, j, bj)] = certificate
        for indices in product(range(14), repeat=3):
            if monotonic() - start > cap:
                raise TimeoutError
            triple_count += 1
            pattern = tuple(options[i][indices[i]] for i in range(3))
            if any((i, indices[i], j, indices[j]) in certificates
                   for i, j in combinations(range(3), 2)):
                rejects["short_balanced_certificate"] += 1
                continue
            failure = reuse_failure(pattern)
            if failure:
                rejects[failure] += 1
                continue
            if all(a[0] in ("U", "V") for a in pattern):
                rejects["stage11_all_B_selection"] += 1
                continue
            failure = tree_failure(tree_edges(pattern))
            if failure:
                rejects[failure["reason"]] += 1
                continue
            survivors.append(pattern)
        complete = True
    except TimeoutError:
        pass
    example = next((p for p in survivors
                    if tuple(a[0] for a in p) == ("D", "D", "S")
                    and p[0][1] == p[1][1]),
                   survivors[0] if survivors else None)
    result = {
        "scope": "formal partner choices, not moduli or valid sets",
        "runtime_cap_seconds": cap,
        "completion_status": "complete" if complete else "INCOMPLETE: cap reached",
        "elapsed_seconds": monotonic() - start,
        "partner_pairs_checked": pair_count,
        "partner_pairs_rejected_by_certificate": len(certificates),
        "triple_patterns_checked": triple_count,
        "first_rejection_counts": dict(sorted(rejects.items())),
        "surviving_selected_patterns": len(survivors),
        "survivor_type_counts": dict(sorted(Counter(
            "".join(a[0] for a in p) for p in survivors).items())),
        "example": display(example) if example else None,
        "example_tree_edges": {
            NAMES[b]: [[NAMES[d], NAMES[e], NAMES[label]] for d, e, label in edges]
            for b, edges in enumerate(tree_edges(example))} if example else None,
        "pair_certificates": [dict(centers=[i, j], option_indices=[a, b],
                                   **certificate)
                              for (i, a, j, b), certificate in certificates.items()],
        "limitations": [
            "Only coefficients -1,0,1 of two partner rows and one core row are checked.",
            "Known partial edges of all eight trees are checked, not simultaneous completion.",
            "One partner is selected per pure cubic; uniqueness is never assumed.",
            "Unspecified extra partners, full doubling closure and validity are not certified.",
            "Survivors are not group configurations or counterexamples."]}
    if complete:
        assert pair_count == 588 and triple_count == 2744
        assert sum(rejects.values()) + len(survivors) == triple_count
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--cap", type=float, default=5)
    parser.add_argument("--output", default="stage12_partner_results.json")
    args = parser.parse_args()
    result = run(args.cap)
    Path(args.output).write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items() if k != "pair_certificates"}, indent=2))
