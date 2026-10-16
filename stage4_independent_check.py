"""Independent small verifier, using unmarked multisets and support graphs.

No project verification functions or propagation code are imported.
"""

from collections import defaultdict
from itertools import combinations_with_replacement
import json
from pathlib import Path
from time import monotonic


CASES = (
    (255, (0, 1, 3, 7, 15, 31, 63, 127), (36, 92, 92)),
    (256, (0, 1, 3, 7, 15, 31, 63, 127), (37, 93, 94)),
    (6560, (0, 2, 8, 26, 80, 242, 728, 2186), (64, 232, 260)),
    (4373, (0, 2, 8, 26, 80, 242, 728, 2186), (64, 239, 260)),
    (229753, (0, 1, 13, 169, 2043, 2197, 28561, 28719), (64, 257, 260)),
    (78337, (0, 4609, 4610, 4626, 4898, 9248, 9522, 9792), (62, 241, 244)),
    (2197065, (0, 1, 65, 67, 4225, 4229, 274625, 274633), (61, 234, 236)),
)


def verify(n, a, expected):
    target = sum(a) % n
    rivals = [u for u in combinations_with_replacement(range(8), 8)
              if sum(a[i] for i in u) % n == target]
    assert rivals == [tuple(range(8))]
    assert len({(x - y) % n for x in a for y in a if x != y}) == 56
    counts = {}
    quartics = None
    for degree in (3, 4):
        repeated = defaultdict(list)
        squarefree = {}
        for u in combinations_with_replacement(range(8), degree):
            value = sum(a[i] for i in u) % n
            if len(set(u)) == degree:
                assert value not in squarefree
                squarefree[value] = u
            else:
                repeated[value].append(u)
        assert squarefree.keys().isdisjoint(repeated)
        counts[degree] = len(repeated)
        if degree == 4:
            quartics = repeated
    k = 0
    fresh = []
    for value, fiber in quartics.items():
        remaining = set(range(len(fiber)))
        supports = []
        while remaining:
            first = remaining.pop()
            pending = [first]
            support = set(fiber[first])
            while pending:
                current = pending.pop()
                neighbors = [j for j in remaining
                             if set(fiber[current]).intersection(fiber[j])]
                for j in neighbors:
                    remaining.remove(j)
                    pending.append(j)
                    support.update(fiber[j])
            supports.append(support)
        k += len(supports)
        if len(supports) > 1:
            fresh.append({"value": value, "multisets": fiber,
                          "support_sizes": sorted(map(len, supports))})
    assert (counts[3], counts[4], k) == expected
    return {"N": n, "A": a, "T3": counts[3], "T4": counts[4],
            "K": k, "D": k - counts[4], "valid": True,
            "multisets_checked": 6435, "fresh_fibers": fresh}


def main():
    start = monotonic()
    results = []
    for case in CASES:
        assert monotonic() - start < 10
        results.append(verify(*case))
    report = {"seconds_limit": 10, "elapsed_seconds": monotonic() - start,
              "distinct_pairs_tested": len(results), "results": results}
    Path("stage4_independent_results.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="ascii")
    print(json.dumps([{k: v for k, v in r.items() if k != "fresh_fibers"}
                      for r in results], indent=2))


if __name__ == "__main__":
    main()
