# Stage59 findings: triangle splits and the exact external-collision residual

The new theorem is that any quartic triangle supports at most ONE genuine quintic split output through its three cubic descents in the hypothetical odd N<248 setting.

The local proof covers12 presentations for a fixed descent. Eight give elementary protected collisions, label collisions or mass-eight rivals. Two symmetric presentations use one positively checked quartic-growth89 certificate. The two necessary residuals per descent give six presentations across the triangle; all15 presentation pairs are excluded by direct hand identities. No odd integer is canceled, and no weak discovery bound or timeout is an exclusion.

Globally, with D the set of ordinary cubic pairs occurring in triangles,

    q<=4(P-|D|)+t<=4P-5t.

Combining this with q<=h and the existing global count excludes all N<248 systems whose ordinary cubic collisions are exhausted by one triangle-bearing alignment class. The complete nine-shape forest table gives conditional lower bounds248 through279 and allows every pure-only refinement.

This gives a concrete contribution to the residual-case task. For a chosen class, let B0 be its table bound, r the number of ordinary cubic pairs outside it, and t_out the number of triangles outside it. Every counterexample must satisfy

    6r-3t_out>=B0-247.

For example, a primary(3,3,2) class requires at least three external ordinary pairs; a primary(5,3) class requires at least one. These are actual structural necessities for the full residual family, not incremental restrictions on selected moduli.

Start with stage59_one_split_per_triangle_proof.md and stage59_forest_residual_proof.md. Verify with `python -B stage59_certificate_check.py`. The standalone standard-library checker imports no producer, eliminator or prior checker. It reconstructs coverage, verifies3,916 positive mass-eight identities and all15 residual-pair identities, and independently enumerates the nine forest shapes. The archive is10,260 bytes, SHA2562f10f531380a470f3b73d586610b4a2136dcc32fecd087c1576814ca5b6798a2. This is separate implementation by the same assistant, not external or formal certification.

The full N>=248 theorem remains OPEN. The remaining task is the coupled external-collision allocation, or a complete positive closure of its residual configurations. General N>=207, all even orders below248 excluded, equality248, and historical discovery-only boundaries are unchanged. No earlier PR is merged.
