"""Targeted falsification of the Stage 38 cubic--overlap alternative.

Batch every replacement value for one coordinate, optimizing cubic protection
AND overlap <=5. Fixed finite schedules; timeouts/minima certify no absence.
No historical producer or verifier is imported. Requires numpy.
"""
import argparse
import json
import random
from itertools import combinations_with_replacement
from pathlib import Path
from time import monotonic

import numpy as np


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--seconds', type=float, default=45)
    parser.add_argument('--restarts', type=int, default=64)
    parser.add_argument('--steps', type=int, default=400)
    parser.add_argument('--collect', type=int, default=1)
    parser.add_argument('--output', default='stage39_cubic_overlap_results.json')
    parser.add_argument('--avoid-midpoint', action='store_true',
                        help='also require 70 distinct squarefree quartics (given protected cubics)')
    args = parser.parse_args()
    start = monotonic()
    words = list(combinations_with_replacement(range(8), 3))
    mat = np.array([[w.count(i) for i in range(8)] for w in words], dtype=np.int64)
    square = np.array([j for j, w in enumerate(words) if len(set(w)) == 3])
    overlap_mat = np.array([[2 * (k == i) - (k == j) for k in range(8)]
                            for i in range(8) for j in range(8)], dtype=np.int64)
    from itertools import combinations
    half_words = [w for w in combinations(range(8), 4) if 0 in w]
    half_mat = np.array([[2 * (i in w) - 1 for i in range(8)] for w in half_words])
    best = {}
    counters = {'batches': 0, 'distinct_presentations': 0, 'cubic_protected': 0}
    witness = None
    witnesses = {}
    state = None
    completed = True
    schedule = (247, 239, 243)
    try:
        for n in schedule:
            values = np.arange(n)
            offsets = n * values[:, None]
            for restart in range(args.restarts):
                rng = random.Random(3900000 + 1000 * n + restart)
                anchor = [0, 1, 3, 7, 15, 31, 63, 165 % n]
                a = np.array(anchor if restart % 4 == 0 else [0, 1, *rng.sample(range(2, n), 6)])
                tabu = set()
                for step in range(args.steps):
                    state = {'N': n, 'restart': restart, 'step': step}
                    if monotonic() - start >= args.seconds:
                        raise TimeoutError
                    # Every coordinate is mutable except the translated zero.
                    i = 1 + step % 7
                    dv = values - a[i]
                    cv = ((mat @ a)[None, :] + dv[:, None] * mat[:, i]) % n
                    hist = np.bincount((cv + offsets).ravel(), minlength=n * n).reshape(n, n)
                    loss = np.take_along_axis(hist, cv[:, square], axis=1).sum(axis=1) - 56
                    ov = ((overlap_mat @ a)[None, :] + dv[:, None] * overlap_mat[:, i]) % n
                    ohist = np.bincount((ov + offsets).ravel(), minlength=n * n).reshape(n, n)
                    maximum = ohist.max(axis=1)
                    midpoint = np.any(((half_mat @ a)[None, :] + dv[:, None] * half_mat[:, i]) % n == 0, axis=1)
                    forbidden = set(a.tolist()) - {int(a[i])}
                    allowed = np.array([x not in forbidden for x in range(n)])
                    counters['batches'] += 1
                    counters['distinct_presentations'] += int(allowed.sum())
                    protected = np.flatnonzero(allowed & (loss == 0))
                    counters['cubic_protected'] += len(protected)
                    for x in protected:
                        if maximum[x] <= 5 and (not args.avoid_midpoint or not midpoint[x]):
                            trial = a.copy()
                            trial[i] = x
                            found = {'N': n, 'A': sorted(trial.tolist()),
                                       'cubic_loss': 0, 'maximum_overlap': int(maximum[x]),
                                       'midpoint_quartic_collision': bool(midpoint[x]),
                                       'discovery_state': state}
                            witnesses.setdefault((n, tuple(found['A'])), found)
                            if witness is None:
                                witness = found
                    if len(witnesses) >= args.collect:
                        break
                    score = loss + 4 * np.maximum(maximum - 5, 0)
                    if args.avoid_midpoint:
                        score += 4 * midpoint
                    eligible = np.flatnonzero(allowed)
                    xbest = min(eligible, key=lambda x: (int(score[x]), int(loss[x]), int(maximum[x])))
                    candidate = {'score': int(score[xbest]), 'cubic_loss': int(loss[xbest]),
                                 'maximum_overlap': int(maximum[xbest]),
                                 'midpoint_quartic_collision': bool(midpoint[xbest])}
                    if n not in best or tuple(candidate.values()) < tuple(best[n][k] for k in candidate):
                        trial = a.copy()
                        trial[i] = xbest
                        best[n] = {**candidate, 'A': sorted(trial.tolist()), 'state': state}
                    # Random equal-best moves and short tabu memory; periodically
                    # perturb two mutable coordinates to leave local minima.
                    choices = [int(x) for x in eligible if score[x] == score[xbest]
                               and tuple(sorted([*a[:i], x, *a[i + 1:]])) not in tabu]
                    x = rng.choice(choices) if choices else int(xbest)
                    a[i] = x
                    tabu.add(tuple(sorted(a.tolist())))
                    if len(tabu) > 80:
                        tabu.clear()
                    if step % 35 == 34:
                        for j in rng.sample(range(1, 8), 2):
                            a[j] = rng.choice([x for x in range(1, n) if x not in a])
                if len(witnesses) >= args.collect:
                    break
            if len(witnesses) >= args.collect:
                break
    except TimeoutError:
        completed = False
    out = {'completion': 'WITNESS_TARGET_REACHED' if len(witnesses) >= args.collect else ('COMPLETE_DECLARED_EXPERIMENT' if completed
           else 'INCOMPLETE_DECLARED_EXPERIMENT'), 'schedule': list(schedule),
           'restarts_per_order': args.restarts, 'steps_per_restart': args.steps,
           'seconds_limit': args.seconds, 'elapsed_seconds': monotonic() - start,
           'counters': counters, 'best': best, 'witness': witness,
           'witness_target': args.collect, 'witnesses': list(witnesses.values()),
           'require_no_midpoint_collision': args.avoid_midpoint,
           'last_state': state, 'modulus_exclusion': False, 'absence_is_proof': False}
    Path(args.output).write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps({k: v for k, v in out.items() if k != 'witnesses'}, indent=2))


if __name__ == '__main__':
    main()
