"""Stage 17: two prescribed directions and one rank-forcing role extension.

This checks only symbolic presentations, never moduli or candidate sets.
The elementary reduction has coordinates (u,t,e), where w=0,
t=a-u and e=c-a.  Every rejection has an exact dyadic integer identity.
All surviving role assignments and every exclusion witness are saved.
"""

import argparse
from collections import Counter
from fractions import Fraction
from itertools import product
import json
from math import gcd, lcm
from pathlib import Path
from time import monotonic


NAMES = ("w", "u", "a", "c", "b", "p", "q", "v")
POINTS = ((0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 1, 1),
          (0, -4, 0), (0, 2, 4), (0, 2, 2), (0, 0, 4))
DIRECTIONS = (("double_v_minus_w", (0, 0, 8)),
              ("double_b_minus_w", (0, -8, 0)))
ROLES = tuple((i, j) for i in range(8) for j in range(8) if i != j)


def compositions(total, length):
    if length == 1:
        yield (total,)
    else:
        for first in range(total + 1):
            for rest in compositions(total - first, length - 1):
                yield (first,) + rest


def forbidden_sums():
    target = tuple(sum(point[j] for point in POINTS) for j in range(3))
    for counts in compositions(8, 8):
        if counts == (1,) * 8:
            continue
        vector = tuple(sum(counts[i] * POINTS[i][j] for i in range(8))
                       - target[j] for j in range(3))
        yield counts, vector


def relation(direction, role):
    i, j = role
    return tuple(direction[k] - POINTS[i][k] + POINTS[j][k]
                 for k in range(3))


def row_reduction(rows):
    count = len(rows)
    matrix = [[Fraction(rows[j][i]) for j in range(count)]
              + [Fraction(int(i == j)) for j in range(3)] for i in range(3)]
    pivots = []
    for column in range(count):
        rank = len(pivots)
        pivot = next((i for i in range(rank, 3) if matrix[i][column]), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        divisor = matrix[rank][column]
        matrix[rank] = [x / divisor for x in matrix[rank]]
        for i in range(3):
            if i != rank and matrix[i][column]:
                factor = matrix[i][column]
                matrix[i] = [x - factor * y for x, y in zip(matrix[i], matrix[rank])]
        pivots.append(column)
    transforms = []
    for row in matrix:
        denominator = lcm(*(x.denominator for x in row[count:]))
        transforms.append((tuple(int(x * denominator) for x in row[count:]),
                           denominator))
    return tuple(pivots), tuple(transforms)


def verify_identity(rows, vector, multiplier, coefficients):
    if (type(multiplier) is not int or multiplier <= 0
            or multiplier & (multiplier - 1) or len(rows) != len(coefficients)
            or any(type(x) is not int for x in coefficients)):
        return False
    return all(multiplier * vector[j]
               == sum(z * row[j] for z, row in zip(coefficients, rows))
               for j in range(3))


def verify_certificate(rows, rival_counts, multiplier, coefficients):
    if (len(rival_counts) != 8 or any(type(x) is not int or x < 0 for x in rival_counts)
            or sum(rival_counts) != 8 or tuple(rival_counts) == (1,) * 8):
        return False
    target = tuple(sum(point[j] for point in POINTS) for j in range(3))
    rival_vector = tuple(sum(rival_counts[i] * POINTS[i][j] for i in range(8))
                         - target[j] for j in range(3))
    return verify_identity(rows, rival_vector, multiplier, coefficients)


def find_identity(rows, candidates):
    pivots, transforms = row_reduction(rows)
    rank = len(pivots)
    for counts, vector in candidates:
        products = [sum(x * y for x, y in zip(row, vector))
                    for row, _ in transforms]
        if any(products[rank:]):
            continue
        coefficients = [Fraction(0)] * len(rows)
        for i, pivot in enumerate(pivots):
            coefficients[pivot] = Fraction(products[i], transforms[i][1])
        multiplier = lcm(*(x.denominator for x in coefficients))
        if multiplier & (multiplier - 1):
            continue
        integers = tuple(int(x * multiplier) for x in coefficients)
        assert verify_identity(rows, vector, multiplier, integers)
        return {"rival_counts": counts, "multiplier": multiplier,
                "coefficients": integers, "vector": vector, "rank": rank}
    return None


def find_certificate(rows, forbidden):
    witness = find_identity(rows, forbidden)
    if witness is not None:
        assert verify_certificate(rows, witness["rival_counts"],
                                  witness["multiplier"], witness["coefficients"])
    return witness


def extra_quartics():
    expected = ((1, 2, 0, 0, 0, 0, 0, 1),
                (0, 0, 2, 0, 1, 1, 0, 0),
                (0, 0, 0, 2, 1, 0, 1, 0))
    target = (2, 0, 4)
    for counts in compositions(4, 8):
        if counts in expected:
            continue
        vector = tuple(sum(counts[i] * POINTS[i][j] for i in range(8))
                       - target[j] for j in range(3))
        yield counts, vector


def encode_roles(roles):
    return [[NAMES[i], NAMES[j]] for i, j in roles]


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def difference(role):
    i, j = role
    return tuple(POINTS[i][k] - POINTS[j][k] for k in range(3))


def rank_forcing_direction(rows):
    x, y = rows
    functional = (x[1]*y[2]-x[2]*y[1],
                  x[2]*y[0]-x[0]*y[2],
                  x[0]*y[1]-x[1]*y[0])
    assert any(functional) and all(dot(functional, row) == 0 for row in rows)
    divisor = gcd(*functional)
    functional = tuple(z // divisor for z in functional)
    source = max(ROLES, key=lambda role: dot(functional, difference(role)))
    maximum = dot(functional, difference(source))
    assert maximum > 0
    direction = tuple(2*z for z in difference(source))
    return functional, source, direction, maximum


def check(seconds):
    start = monotonic()
    deadline = start + seconds
    forbidden = tuple(forbidden_sums())
    assert len(forbidden) == 6434 and len(ROLES) == 56
    exclusions, survivors, singles = [], [], []
    counts = Counter()
    complete = True
    for name, direction in DIRECTIONS:
        retained = []
        for role in ROLES:
            if monotonic() > deadline:
                complete = False
                break
            row = relation(direction, role)
            witness = find_certificate((row,), forbidden)
            entry = {"directions": [name], "roles": encode_roles((role,)), "rows": [row]}
            counts["single_roles_examined"] += 1
            if witness:
                counts["single_roles_excluded"] += 1
                exclusions.append(dict(entry, certificate=witness))
            else:
                counts["single_roles_survived"] += 1
                retained.append(role)
        singles.append({"direction": name, "retained_roles": encode_roles(retained)})
        if not complete:
            break
    if complete:
        domains = [tuple((NAMES.index(x), NAMES.index(y)) for x, y in entry["retained_roles"])
                   for entry in singles]
        for roles in product(*domains):
            if monotonic() > deadline:
                complete = False
                break
            rows = tuple(relation(direction, role)
                         for (_, direction), role in zip(DIRECTIONS, roles))
            witness = find_certificate(rows, forbidden)
            entry = {"directions": [name for name, _ in DIRECTIONS],
                     "roles": encode_roles(roles), "rows": rows}
            counts["combined_roles_examined"] += 1
            if witness:
                counts["combined_roles_excluded"] += 1
                exclusions.append(dict(entry, certificate=witness))
            else:
                counts["combined_roles_survived"] += 1
                survivors.append(entry)
    quartic_exclusions, quartic_survivors = [], []
    if complete:
        quartics = tuple(extra_quartics())
        assert len(quartics) == 327
        for entry in survivors:
            if monotonic() > deadline:
                complete = False
                break
            counts["extra_quartic_presentations_examined"] += 1
            witness = find_identity(entry["rows"], quartics)
            if witness:
                counts["extra_quartic_presentations_excluded"] += 1
                quartic_exclusions.append(dict(entry, certificate=witness))
            else:
                counts["extra_quartic_presentations_survived"] += 1
                quartic_survivors.append(entry)
    final_exclusions, final_survivors, rank_forcing_coverage = [], [], []
    if complete:
        for entry in quartic_survivors:
            functional, source, direction, maximum = rank_forcing_direction(entry["rows"])
            coverage = {"parent_roles": entry["roles"], "functional": functional,
                        "source_difference": encode_roles((source,))[0],
                        "doubled_direction": direction, "maximum": maximum,
                        "partners_examined": 0, "complete": False}
            rank_forcing_coverage.append(coverage)
            for role in ROLES:
                if monotonic() > deadline:
                    complete = False
                    break
                row = relation(direction, role)
                assert dot(functional, row) >= maximum > 0
                rows = tuple(entry["rows"]) + (row,)
                assert len(row_reduction(rows)[0]) == 3
                candidate = {"parent_roles": entry["roles"],
                             "source_difference": encode_roles((source,))[0],
                             "partner_role": encode_roles((role,))[0],
                             "functional": functional, "rows": rows}
                witness = find_certificate(rows, forbidden)
                counts["rank_forcing_roles_examined"] += 1
                coverage["partners_examined"] += 1
                if witness:
                    counts["rank_forcing_roles_excluded"] += 1
                    final_exclusions.append(dict(candidate, certificate=witness))
                else:
                    counts["rank_forcing_roles_survived"] += 1
                    final_survivors.append(candidate)
            coverage["complete"] = coverage["partners_examined"] == 56
            if not complete:
                break
    # This rejects tampered integer identities and illegal multipliers.
    verification = {"all_saved_certificates_pass": all(verify_certificate(
        entry["rows"], entry["certificate"]["rival_counts"],
        entry["certificate"]["multiplier"], entry["certificate"]["coefficients"])
        for entry in exclusions + final_exclusions)}
    sample = exclusions[0] if exclusions else None
    if sample:
        witness = sample["certificate"]
        changed = list(witness["coefficients"])
        nonzero = next(i for i, row in enumerate(sample["rows"]) if any(row))
        changed[nonzero] += 1
        verification["tampered_coefficient_rejected"] = not verify_certificate(
            sample["rows"], witness["rival_counts"], witness["multiplier"], changed)
        verification["odd_multiplier_rejected"] = not verify_certificate(
            sample["rows"], witness["rival_counts"], 3, witness["coefficients"])
        verification["all_ones_rival_rejected"] = not verify_certificate(
            sample["rows"], [1]*8, witness["multiplier"], witness["coefficients"])
    assert all(verification.values())
    return {"scope": "two prescribed doubled differences, optional zero-exclusion quartic diagnostic, and one justified rank-forcing extension",
            "point_names": NAMES, "point_vectors": POINTS,
            "coordinates": ["u", "t=a-u", "e=c-a"], "w": 0,
            "completion": "COMPLETE" if complete else "TIMEOUT",
            "complete": complete, "timed_out": not complete,
            "runtime_cap_seconds": seconds, "elapsed_seconds": round(monotonic()-start, 6),
            "counts": dict(counts), "single_domains": singles,
            "exclusions": exclusions, "survivors": survivors,
            "extra_quartic_exclusions": quartic_exclusions,
            "extra_quartic_survivors": quartic_survivors,
            "rank_forcing_coverage": rank_forcing_coverage,
            "rank_forcing_exclusions": final_exclusions,
            "rank_forcing_survivors": final_survivors,
            "verification": verification,
            "limits": ["Survivors are symbolic necessary conditions, not valid counterexamples.",
                       "Only dyadic integer witnesses are accepted; no odd denominator cancellation.",
                       "Rank-deficient free coefficients zero can miss witnesses.",
                       "No residue sets, candidate moduli, or historical checker imports."]}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--seconds", type=float, default=60)
    parser.add_argument("--output", default="stage17_local_results.json")
    args = parser.parse_args()
    result = check(args.seconds)
    Path(args.output).write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: result[k] for k in ("completion", "elapsed_seconds", "counts", "verification")}, indent=2))
