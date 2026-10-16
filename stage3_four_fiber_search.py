"""Targeted exact search of the sharp ordinary-four-fiber configuration.

Completeness of the four normalization cases at N=247 is proved in
stage3_search_notes.md. This is not a search of all eight-element sets.
"""

import argparse
import json
from functools import lru_cache
from itertools import combinations_with_replacement
from math import gcd
from pathlib import Path
from time import monotonic

from stage3_search import Deadline, bits, direct_valid_count


POINT_COEFFICIENTS = ((0, 0, 0, 0), (0, 2, 0, 0), (0, 0, 2, 0),
                      (0, 0, 0, 2), (1, -1, 0, 0), (1, 0, -1, 0),
                      (1, -1, -1, 0), (1, 0, -1, -1))
BASELINE = (4, 0, -1, 1)


def configuration(u, v, w, h, modulus):
    return tuple(x % modulus for x in
                 (0, 2*u, 2*v, 2*w, h-u, h-v, h-u-v, h-v-w))


@lru_cache(maxsize=1)
def rival_vectors():
    vectors = set()
    for indices in combinations_with_replacement(range(8), 8):
        if indices == tuple(range(8)):
            continue
        vector = tuple(sum(POINT_COEFFICIENTS[i][j] for i in indices) - BASELINE[j]
                       for j in range(4))
        assert vector != (0, 0, 0, 0)
        vectors.add(vector)
    return tuple(sorted(vectors))


def forbidden_forms(modulus):
    balanced = set()
    h_forms = set()
    for ch, cu, cv, cw in rival_vectors():
        if ch == 0:
            vector = (cu % modulus, cv % modulus, cw % modulus)
            balanced.add(min(vector, tuple(-x % modulus for x in vector)))
        else:
            assert gcd(ch, modulus) == 1, "This fast encoding needs 1,2,3,4 invertible."
            inverse = pow(ch, -1, modulus)
            h_forms.add(tuple(-c * inverse % modulus for c in (cu, cv, cw)))
    return tuple(sorted(balanced)), tuple(sorted(h_forms))


def orbit_parameters(name, x, y):
    if name == "triangle_base":
        return 1, x, y
    if name == "central_edge":
        return x, 1, y
    if name == "missing_edge":
        return x, y, 1
    if name == "pendant_edge":
        return x, y, y + 1
    raise ValueError(name)


def substitute(vector, name, modulus):
    cu, cv, cw = vector
    if name == "triangle_base":
        result = cu, cv, cw
    elif name == "central_edge":
        result = cv, cu, cw
    elif name == "missing_edge":
        result = cw, cu, cv
    elif name == "pendant_edge":
        result = cw, cu, cv + cw
    else:
        raise ValueError(name)
    return tuple(x % modulus for x in result)


def solve_mask(coefficient, rhs, modulus):
    coefficient %= modulus
    rhs %= modulus
    divisor = gcd(coefficient, modulus)
    if rhs % divisor:
        return 0
    reduced = modulus // divisor
    first = 0 if reduced == 1 else (rhs // divisor) * pow(coefficient // divisor, -1, reduced) % reduced
    return sum(1 << (first + k * reduced) for k in range(divisor))


def validate():
    comparisons = 0
    for modulus in (19, 23):
        balanced, h_forms = forbidden_forms(modulus)
        for u in range(1, 4):
            for v in range(1, 4):
                for w in range(1, 4):
                    balanced_ok = all((a*u+b*v+c*w) % modulus for a,b,c in balanced)
                    forbidden = {(a*u+b*v+c*w) % modulus for a,b,c in h_forms}
                    for h in range(modulus):
                        a = configuration(u,v,w,h,modulus)
                        if len(set(a)) != 8:
                            continue
                        predicted = balanced_ok and h not in forbidden
                        actual = direct_valid_count(a,modulus)["valid"]
                        assert predicted == actual
                        comparisons += 1
    modulus = 54865
    u,v,w,h = 1,19,361,6859
    balanced,h_forms = forbidden_forms(modulus)
    assert all((a*u+b*v+c*w) % modulus for a,b,c in balanced)
    assert h not in {(a*u+b*v+c*w) % modulus for a,b,c in h_forms}
    a = configuration(u,v,w,h,modulus)
    verified = direct_valid_count(a,modulus)
    assert verified["valid"] and verified["multisets_enumerated"] == 6435
    return {"independent_structured_comparisons": comparisons,
            "known_sharp_four_fiber_case": {"N":modulus,"A":a,**verified}}


def search(modulus, seconds, checkpoint):
    balanced,h_forms = forbidden_forms(modulus)
    names = ("triangle_base","central_edge","missing_edge","pendant_edge")
    full = (1 << modulus) - 1
    start = monotonic()
    records = []
    accepted = []
    active = None

    def record(status):
        result = {"status":status,"N":modulus,"seconds_limit":seconds,
                  "elapsed_seconds":monotonic()-start,
                  "rival_linear_vectors":len(rival_vectors()),
                  "balanced_tail_constraints":len(balanced),
                  "forbidden_h_forms":len(h_forms),
                  "normalizations":records,"active_parameters":active,
                  "accepted_sets":accepted,"complete_search":status=="COMPLETE"}
        Path(checkpoint).write_text(json.dumps(result,indent=2)+"\n",encoding="ascii")
        return result

    try:
        for name in names:
            bforms = tuple({substitute(c,name,modulus) for c in balanced})
            hforms = tuple({substitute(c,name,modulus) for c in h_forms})
            row = {"name":name,"fully_completed_x":[],"balanced_rejected_pairs":0,
                   "balanced_passing_pairs":0,"h_values_excluded":0}
            records.append(row)
            for x in range(modulus):
                active = {"normalization":name,"x":x,"y":None}
                if monotonic()-start >= seconds:
                    raise Deadline
                bad_y = 0
                for c0,c1,c2 in bforms:
                    bad_y |= solve_mask(c2,-c0-c1*x,modulus)
                    if bad_y == full:
                        break
                row["balanced_rejected_pairs"] += bad_y.bit_count()
                for y in bits(full & ~bad_y):
                    active["y"] = y
                    if monotonic()-start >= seconds:
                        raise Deadline
                    row["balanced_passing_pairs"] += 1
                    forbidden = 0
                    for c0,c1,c2 in hforms:
                        forbidden |= 1 << ((c0+c1*x+c2*y) % modulus)
                        if forbidden == full:
                            break
                    row["h_values_excluded"] += forbidden.bit_count()
                    for h in bits(full & ~forbidden):
                        u,v,w = orbit_parameters(name,x,y)
                        a = configuration(u,v,w,h,modulus)
                        assert len(set(a)) == 8
                        verified = direct_valid_count(a,modulus)
                        assert verified["valid"] and verified["multisets_enumerated"] == 6435
                        accepted.append({"normalization":name,"u":u,"v":v,"w":w,
                                         "H":h,"A":a,**verified})
                row["fully_completed_x"].append(x)
                record("RUNNING")
        status = "COMPLETE"
    except Deadline:
        status = "TIMEOUT"
    return record(status)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--N",type=int,default=247)
    parser.add_argument("--seconds",type=float,default=180)
    parser.add_argument("--checkpoint",default="stage3_four_fiber_247.json")
    parser.add_argument("--validate",action="store_true")
    args=parser.parse_args()
    if args.validate:
        print(json.dumps(validate(),indent=2))
    print(json.dumps(search(args.N,args.seconds,args.checkpoint),indent=2))


if __name__=="__main__":
    main()
