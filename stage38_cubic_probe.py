"""Discovery experiment for the strictly stronger cubic-separation hypothesis.

First check every one-point extension of the fixed integer binary seven-set
at the named orders. Then make 12*5000 deterministic seeded annealing moves
at each of 239,247,255, then the stated two-coordinate follow-up at 247.
A zero score is an explicit verifiable witness;
nonzero minima, exhaustion of this family, or timeout exclude no modulus.
Requires numpy; no research producer/verifier is imported by this file.
"""
import argparse
import json
import math
import random
from collections import Counter
from itertools import combinations, combinations_with_replacement
from pathlib import Path
from time import monotonic

import numpy as np


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seconds", type=float, default=30)
    args = parser.parse_args()
    start = monotonic()
    words = list(combinations_with_replacement(range(8), 3))
    square = [i for i, w in enumerate(words) if len(set(w)) == 3]
    matrix = np.zeros((120, 8), dtype=np.int64)
    for i, w in enumerate(words):
        for j in w:
            matrix[i, j] += 1
    assert len(square) == 56
    counters = Counter()
    best = {}
    witnesses = set()
    partial = None
    complete = True

    def evaluate(a, n, kind):
        values = (matrix @ np.asarray(a, dtype=np.int64)) % n
        total = np.bincount(values, minlength=n)
        # Each of the 56 squarefree words must be alone in its residue fiber.
        score = int(total[values[square]].sum()) - 56
        counters[kind] += 1
        if n not in best or score < best[n]["score"]:
            best[n] = {"score": score, "A": list(a), "kind": kind}
        if score == 0:
            witnesses.add((n, tuple(sorted(a))))
        return score

    def tick(state):
        nonlocal partial
        if monotonic() - start >= args.seconds:
            partial = state
            raise TimeoutError

    try:
        base = tuple((1 << i) - 1 for i in range(7))
        for n in (*range(207, 248, 2), 255, 259, 271, 283, 285, 301):
            for x in range(n):
                tick({"phase": "extensions", "N": n, "x": x})
                if x not in base:
                    evaluate((*base, x), n, "fixed_extensions")
        for n in (239, 247, 255):
            for restart in range(12):
                rng = random.Random(380000 + 100 * n + restart)
                a = [(1 << i) - 1 for i in range(8)] if restart % 2 == 0 else [0, 1, *rng.sample(range(2, n), 6)]
                score = evaluate(a, n, "anneal_initial")
                for step in range(5000):
                    tick({"phase": "annealing", "N": n, "restart": restart, "step": step})
                    i = rng.randrange(2, 8)
                    x = rng.randrange(n)
                    if x in a:
                        counters["duplicate_moves"] += 1
                        continue
                    trial = a.copy()
                    trial[i] = x
                    value = evaluate(trial, n, "anneal_moves")
                    temperature = 2.5 * (0.1 / 2.5) ** (step / 4999)
                    if value <= score or rng.random() < math.exp((score - value) / temperature):
                        a, score = trial, value
        # Adaptive follow-up fixed before this second run: challenge whether
        # the N=247 cubic witness necessarily retains its six-fold overlap.
        # Freeze 0,1,3,7 and change two of its four remaining coordinates.
        anchor = (0, 1, 3, 7, 15, 31, 63, 165)
        for i, j in combinations(range(4, 8), 2):
            fixed = {anchor[k] for k in range(8) if k not in (i, j)}
            for x in range(247):
                for y in range(x + 1, 247):
                    tick({"phase": "coupled_neighbors", "i": i, "j": j, "x": x, "y": y})
                    if x in fixed or y in fixed:
                        continue
                    a = list(anchor)
                    a[i], a[j] = x, y
                    evaluate(a, 247, "coupled_neighbors")
    except TimeoutError:
        complete = False
    out = {"completion": "COMPLETE_DECLARED_EXPERIMENT" if complete else "INCOMPLETE_DECLARED_EXPERIMENT",
           "seconds_limit": args.seconds, "elapsed_seconds": monotonic() - start,
           "planned_annealing_steps": 180000, "planned_coupled_neighbor_presentations": 182286,
           "counters": dict(counters),
           "best": best, "zero_score_witnesses": [{"N": n, "A": list(a)} for n, a in sorted(witnesses)],
           "partial_state": partial, "new_modulus_exclusion": False,
           "hypothesis_proved_by_absence": False}
    Path("stage38_cubic_probe_results.json").write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
