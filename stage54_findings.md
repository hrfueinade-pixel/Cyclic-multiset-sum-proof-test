# Stage 54: the split-source budget now holds in the general branch

2026-10-12. Continues open PR23 at archived-source. The full N>=248 theorem remains OPEN. No earlier PR is merged.

**New theorem:** under the hypothetical full-valid odd N<248 hypotheses, every quartic source of a genuine quintic split has exactly two ordinary quartic representations. Therefore E>=2q holds with E counting two-ordinary disjoint-tail quartic fibers, even when C4>0. Mixed representations at those source values are allowed.

This closes the entire source-path family that could otherwise let genuine splits consume the quartic path/split contributions in S4=p+2w+E. It is not a scalar refinement of the cubic-center bound. Read stage54_source_triple_proof.md and stage54_split_count_hand_proof.md.

The elementary count q<=4P3ordinary also gives a global premise: at least six unordered cubic collision pairs are compulsory below248. That forces first and second additional cubic equalities in the one residual source-path model. The complete symbolic inventories then close every possibility while retaining odd torsion.

## Proof and validation scope

The 901 first directions have 568 direct exclusions,327 quartic-growth exclusions and six necessary residuals. Every residual requires a second equality by the written global count. All4,339 second directions close:3,286 direct and1,053 growth exclusions. All model transformations are surjective by dyadic free-label recovery and integer unimodular changes; odd gcds are retained.

The independent implementation constructs all coverage directions without importing discovery code. It verifies5,407,996 positive quartic pair-separation identities and3,860 direct identities, including retained torsion3,5,7,9. It reconstructs positive rival witnesses from all6,435 mass-eight words instead of shipping millions of repetitive witness records. The compact certificate archive contains the exact chosen quartic words, model transformations, representative relations and direct identities. The larger discovery witness files remain locally saved.

This is computer-assisted proof with a separate implementation by the same assistant, not independent human review or formal certification. Neither a timeout nor a weak growth bound supplies an exclusion. No moduli, group elements or numerical parameters are swept, and no historical search is restarted. A bounded second-inventory run resumed its saved cases without recomputing finished cases or increasing the two-second per-model witness-search limit.

## Verify the saved proof

Python3, standard library only:

    python -B stage54_certificate_check.py

The shipped verifier uses no clique-search timeout. Its acceptance requires positive witnesses for every selected quartic pair and complete first/second coverage.

Optional discovery regeneration uses the existing archive helpers and may be inconclusive on a slower machine; it is not a premise of the shipped proof:

    python -B stage54_source_triple_probe.py
    python -B stage54_source_path_cubic_inventory.py --growth --seconds 180
    python -B stage54_source_path_second_cubic.py --seconds 180
    python -B stage54_source_path_second_cubic.py --seconds 180 --resume
    python -B stage54_certificate_pack.py
    python -B stage54_certificate_check.py

Use --resume only if the second inventory is incomplete. Finished cases and their exact relations are retained; missing evidence or differing inventory keys raises an error. A partial run does not establish the source theorem.

## Remaining full proof

U=E-2q is now a genuine general inventory of two-ordinary disjoint-tail sources unused by all splits. The remaining sufficient target is

    5t+2q <=2(h+R3+c)+5w+U.

The general assignment/ownership theorem and triangle reuse remain OPEN. Ordinary quartic triples are still allowed elsewhere, and source uniqueness does not justify q<=h outside the closed C4=0 branch. All arbitrary odd207..247 cases retain the existing proof boundary. The goal remains active.
