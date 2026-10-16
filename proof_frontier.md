# Current proof frontier: full cyclic-eight bound completed

The sharp minimum cyclic modulus for a full-valid eight-point set is248.
Read stage63_full_bound_proof.md for the assembled computer-assisted proof,
and stage63_finishing_check.py for the elementary final identities.
Independent external mathematical review and formalization remain separate.

The final lemma says that, after translating a quartic triangle to three
disjoint doubling pairs, two distinct labels cannot sum to another label.
A disjoint doubling pair converts that equality into a different degree-eight
word with the original value. Therefore a paired edge is closed exactly
when its tail has an outgoing doubling edge; every terminal paired edge is
OPEN under all additional ordinary and pure collisions.

Stage60 bounds alignment classes by four edges, Stage61 allows at most one
triangle-bearing class globally, and the completed Stage62 proof excludes
the two-triangle shape(3,2,2,1). The remaining one-triangle shapes are
(2,2,2,1,1) with three open paired edges and(4,2,1,1) with two. Stage58 gives
q<=h-o, hence h-q>=2. The GENERAL weighted count now gives

    2N>=496+2(h-q+R3+c)-5t+5w+U>=496+4-5=495.

This contradicts N<=247. The established even-order exclusions complete
the lower bound. A={0,1,3,7,15,31,63,127} is full-valid modulo248 by the
binary coin-count argument in the proof, so the lower bound is attained.

Checks passed:
- Stage60:2,666 proof nodes and1,723,040 positive mass-eight identities.
- Stage61:3,360 second-triangle presentations and1,570,316 identities.
- Stage62:13,333 proof nodes,21,761 private directions,25,851 literal pairs
  and7,945,564 identities, covering ALL ordinary and pure refinements.
- Stage63:224 elementary rival identities, the two final forest counts,
  the integer ledger contradiction and the equality construction.

The Stage60/61/62 checker implementations are separate from producers;
Stage60 and Stage63 use only standard-library code, while Stage61/62 reuse
Stage60 verifier helpers. These are same-assistant checks, not external
review or proof-assistant formal certification. All odd torsion is retained.

The full proof uses the already proved counting/parity chain and completed
positive symbolic graphs. Timeouts, weak witness bounds, modulus sweeps,
and unfinished inventories are not premises. The old broad Stage56/57 and
single-triangle Stage62 discovery trees are terminal and superseded by the
hand finish. Preserve their positive certificates; do not restart them.
