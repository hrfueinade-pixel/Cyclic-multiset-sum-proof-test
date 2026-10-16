"""Growth and propagation checks on the fifteen previously audited pairs.

No new random samples are generated. The eight nonbinary N=4093 fixtures
are the accepted sets from the earlier report's fixed-seed batch.
"""

import json
import argparse
from collections import defaultdict
from itertools import combinations, combinations_with_replacement, product
from pathlib import Path

from stage3_search import direct_valid_count


EXISTING_NONBINARY_4093 = (
    (0,380,2226,2296,2421,3225,3549,3966),
    (0,405,439,1003,2183,2657,2858,3956),
    (0,488,1235,1269,1602,2110,2533,3066),
    (0,496,1470,2147,2500,2646,3158,3757),
    (0,679,1161,1365,2422,2539,3636,3847),
    (0,692,1802,2258,2460,2819,3629,3989),
    (0,954,1239,1405,1478,1963,3411,3469),
    (0,1133,1576,2380,3169,3226,3537,3730),
)


def investigate(a,modulus):
    checked=direct_valid_count(a,modulus)
    assert checked["valid"] and checked["multisets_enumerated"]==6435
    cubic=defaultdict(list)
    for i in range(8):
        for j in range(8):
            cubic[(2*a[i]+a[j])%modulus].append((i,j))
    markings=[(i,j,k) for i in range(8)
              for j,k in combinations_with_replacement(range(8),2)]
    index={mark:i for i,mark in enumerate(markings)}
    parents=list(range(len(markings)))

    def find(i):
        while parents[i]!=i:
            parents[i]=parents[parents[i]]
            i=parents[i]
        return i

    def join(i,j):
        i,j=find(i),find(j)
        if i!=j:
            parents[j]=i

    propagation_edges=0
    for fiber in cubic.values():
        for (i,j),(k,l) in combinations(fiber,2):
            for z in range(8):
                left=(i,*sorted((j,z)))
                right=(k,*sorted((l,z)))
                join(index[left],index[right])
                propagation_edges+=1
    propagated_components=len({find(i) for i in range(len(markings))})
    for i,j in combinations(range(8),2):
        join(index[(i,j,j)],index[(j,i,i)])
    completed_components=len({find(i) for i in range(len(markings))})
    quartic=defaultdict(list)
    for i,mark in enumerate(markings):
        center,b,c=mark
        quartic[(2*a[center]+a[b]+a[c])%modulus].append(i)
    missing_merges=0
    disjoint_tail_pairs=0
    sample=None
    for value,fiber in quartic.items():
        roots={find(i) for i in fiber}
        missing_merges+=len(roots)-1
        for i,j in combinations(fiber,2):
            if find(i)==find(j):
                continue
            left,right=markings[i],markings[j]
            assert set(left[1:]).isdisjoint(right[1:])
            disjoint_tail_pairs+=1
            if sample is None:
                sample={"value":value,
                        "left":tuple(a[t] for t in left),
                        "right":tuple(a[t] for t in right)}
    assert missing_merges==completed_components-len(quartic)
    antipodal=8-len({2*x%modulus for x in a})
    gap=len(quartic)-2*len(cubic)
    return {"N":modulus,"A":a,"antipodal":antipodal,"T3":len(cubic),
            "T4":len(quartic),"growth_gap_T4_minus_2T3":gap,
            "candidate_plus17_passes":gap>=17,"candidate_plus20_passes":gap>=20,
            "propagation_edges":propagation_edges,
            "components_after_cubic_propagation":propagated_components,
            "components_after_type22_doublemarkings":completed_components,
            "further_quartic_component_identifications":missing_merges,
            "cross_component_disjoint_tail_collision_pairs":disjoint_tail_pairs,
            "first_disjoint_tail_new_collision":sample,
            "multisets_enumerated":checked["multisets_enumerated"]}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--mixed-radix",action="store_true")
    args=parser.parse_args()
    if args.mixed_radix:
        patterns=sorted({min(q[i:]+q[:i] for i in range(8))
                         for q in product((2,3),repeat=8)})
        rows=[]
        for q in patterns:
            prefix=1
            a=[]
            for base in q:
                a.append(prefix-1)
                prefix*=base
            result=investigate(tuple(a),prefix-1)
            result["bases"]=q
            rows.append(result)
        report={"family":"cyclic mixed radix","base_patterns":36,
                "rotation_representatives_not_affine_class_census":True,
                "minimum_growth_gap":min(r["growth_gap_T4_minus_2T3"] for r in rows),
                "plus17_failures":[r for r in rows if not r["candidate_plus17_passes"]],
                "results":rows,"universal_growth_bound_proved":False}
        Path("stage3_mixed_radix_probe.json").write_text(json.dumps(report,indent=2)+"\n",encoding="ascii")
        print(json.dumps({k:v for k,v in report.items() if k!="results"},indent=2))
        return
    binary=tuple((1<<i)-1 for i in range(8))
    fixtures=[(binary,N) for N in (248,254,255,256,1022)]
    fixtures.append(((0,2,38,722,6479,6839,6840,6858),54865))
    fixtures.append(((0,2,20,182,1093,1579,1633,1639),1640))
    fixtures.extend((a,4093) for a in EXISTING_NONBINARY_4093)
    assert len(fixtures)==15
    results=[investigate(a,N) for a,N in fixtures]
    report={"fixture_pairs":15,"new_random_draws":0,
            "nonantipodal_plus17_failures":[r for r in results if not r["antipodal"] and not r["candidate_plus17_passes"]],
            "nonantipodal_plus20_failures":[r for r in results if not r["antipodal"] and not r["candidate_plus20_passes"]],
            "results":results,"universal_bounds_proved":False}
    Path("stage3_growth_probe.json").write_text(json.dumps(report,indent=2)+"\n",encoding="ascii")
    print(json.dumps(report,indent=2))


if __name__=="__main__":
    main()
