"""Bounded relation-template tests, not a search over all moduli.

The first family consists of every rooted path with marked endpoint 0
on eight vertices, with all admissible permutations of its seven labels.
Completeness of this family requires the injective h=0, R3=0 hypotheses.
"""

from collections import Counter
from itertools import permutations
import json
from pathlib import Path
from time import monotonic


def determinant(matrix):
    a = [row[:] for row in matrix]
    sign = previous = 1
    for k in range(len(a) - 1):
        pivot = next((i for i in range(k, len(a)) if a[i][k]), None)
        if pivot is None:
            return 0
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        value = a[k][k]
        for i in range(k + 1, len(a)):
            for j in range(k + 1, len(a)):
                numerator = a[i][j] * value - a[i][k] * a[k][j]
                assert numerator % previous == 0
                a[i][j] = numerator // previous
            a[i][k] = 0
        previous = value
    return sign * a[-1][-1]


def relation_matrix(edges, labels):
    a = [[int(i == j) for j in range(7)] for i in range(7)]
    for (source, destination), label in zip(edges, labels):
        if source:
            a[label - 1][source - 1] -= 2
        if destination:
            a[label - 1][destination - 1] += 2
    return a


def path_edges(root):
    return [(i, i + 1) if i < root else (i + 1, i) for i in range(7)]


def main():
    start = monotonic()
    limit = 25
    counts = Counter()
    determinant_counts = Counter()
    examples = {}
    complete = True
    for root in range(1, 8):
        edges = path_edges(root)
        for labels in permutations(range(1, 8)):
            if monotonic() - start > limit:
                complete = False
                break
            counts["label_permutations"] += 1
            if any(label == source for (source, _), label in zip(edges, labels)):
                continue
            counts["admissible_labelings"] += 1
            m = relation_matrix(edges, labels)
            det = abs(determinant(m))
            assert det % 2 == 1 and det <= 2187
            determinant_counts[det] += 1
            if det >= 128:
                counts["determinant_at_least_128"] += 1
                examples.setdefault(det, {"root": root, "labels": labels, "matrix": m})
        if not complete:
            break
    result = {"family": "rooted paths with marked endpoint, R3=0",
              "seconds_limit": limit, "elapsed_seconds": monotonic() - start,
              "complete_template_family": complete, "counts": dict(counts),
              "determinant_counts": dict(sorted(determinant_counts.items())),
              "large_determinant_examples": examples}
    Path("stage6_path_determinants.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(json.dumps({k: v for k, v in result.items()
                      if k != "large_determinant_examples"}, indent=2))


if __name__ == "__main__":
    main()
