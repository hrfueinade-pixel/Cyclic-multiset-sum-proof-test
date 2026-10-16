# Stage58: paired triangle sources excluded; the P<=8 branch closed

2026-10-12. Continues open PR25 at905bc9f2fe19a8655052fca8f0f8933bca0ad504.
The full N>=248 theorem remains OPEN; no earlier PR is merged.

Every paired center edge occurring in a quartic triangle is unavailable
as a genuine quintic split source below248. The complete720-presentation
proof has184 direct model exclusions and six quartic-growth89 exclusions.
The standalone checker imports no discovery or prior verifier code and
checks all odd torsion, both model implications under source-fixing
symmetries, and23,496 positive mass-eight pair identities.

Let o count the DISTINCT open paired center edges occurring in actual
triangles. They are unused vertices in Stage55's general assignment,
proving q<=h-o. Closed paired edges also cannot support genuine splits;
any E source on them is a literal unused source in U, with reuse counted
at output level. No fresh source or per-triangle vertex is assumed.

The path-forest incidence argument closes EVERY hypothetical counterexample
with P3ordinary<=8. Thus every remaining system has a triangle and at
least nine ordinary cubic collision pairs. This is a global family
exclusion, not an ambient modulus exclusion. The full triangle allocation
still needs proof for the surviving high-collision family.

Read stage58_triangle_edge_ownership_proof.md. The elementary cycle and
quotient proof is self-contained in stage56_alignment_cycle_hand_proof.md.
The earlier ordinary-only and quintic forcing bounds are explained in
stage57_ordinary_forcing_hand_proof.md. Its first-root inventory counts are
explicitly discovery and are not a premise of the new hand theorem.

Reproduce the new proof arithmetic with Python3, standard library only:

    python -B stage58_certificate_check.py

The saved proof archive is sufficient; its checker reconstructs all720
canonical presentations without a clique search or producer import. The
general split-assignment premise is the written and separately checked
Stage55 proof. This is same-assistant separate-implementation verification,
not independent human or formal certification.

The larger ordinary-cubic closure tree remains local, INCOMPLETE discovery.
Positive terminal identities remain useful. Weak bounds, fixed discovery
timeouts and partial coverage prove nothing. The full goal is active.
