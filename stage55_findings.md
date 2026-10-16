# Stage55: general q<=h and the entire t=0 branch closed

2026-10-12. Continues open PR24 at archived-source. The full N>=248 theorem remains OPEN. No earlier PR is merged.

**New global theorem:** every genuine quintic split admits an injective assignment to an incident open center edge in the full hypothetical odd N<248 setting. Thus q<=h holds without C4=0. Together with E>=2q, this closes the ENTIRE t=0 branch, including systems with ordinary quartic stars, paths and splits.

Every remaining counterexample has a quartic triangle and therefore, after exact translation, lies in A=(u,2u,v,2v,w,2w,p,r). This family remains open below248.

Read stage55_general_assignment_proof.md. All56 former cap-two inferences in the Stage53 graph coverage have valid replacements. Paths force explicit rivals, a violation of Stage54's source theorem, or quartic growth. The two repeated-mark triangle cases violate the same source theorem. Eight stars would support two distinct splits on one ordinary cubic triple, excluded by complete36-pattern/fifteen-pair coverage.

The new checker verifies93 positive cases,184,052 new quartic separation identities,168 new direct identities,23,255 retained general integer identities and6,670 closed-source growth identities. It checks every replacement and the complete old coverage, using only prior standalone verifier helpers and no discovery/eliminator imports. This is same-assistant separate-implementation verification, not independent human or formal certification.

The additional count q<=min(h,4P3ordinary-11c) will force actual further cubic relations in the remaining triangle family. No genericity, missing witness or failed search is a premise.

## Reproduce

Python3, standard library only, with the shipped Stage53/54 archives and verifier helpers:

    python -B stage55_certificate_check.py

The general source theorem is the proved Stage54 premise, whose full positive proof can separately be checked with stage54_certificate_check.py. No Stage53 cap-two conclusion is assumed in extending the assignment.

Optional positive discovery regeneration:

    python -B stage55_split_exception_probe.py
    python -B stage55_split_exception_probe.py --extend
    python -B stage55_split_exception_probe.py --triangle-marks
    python -B stage55_certificate_pack.py
    python -B stage55_certificate_check.py

The discovery reads the shipped Stage53 proof archive. Its bounded witness searches may be inconclusive; the saved-proof verifier uses no clique-search timeout. Old historical searches are not restarted.

The final full bound remains unproved. The assignment does not pay the triangle weight by itself, and unused sources per triangle still require proof. Equality248, residual558 and arbitrary odd207..247 retain their exact boundaries. The goal is not marked complete.
