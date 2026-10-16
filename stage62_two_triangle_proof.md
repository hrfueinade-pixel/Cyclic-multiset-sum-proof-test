# Stage62: the entire two-triangle class is excluded

Assume a full-valid eight-point set in an odd cyclic group of order
N<248. Stage55 forces a quartic triangle. Stage60 gives four aligned
edges at most, and Stage61 permits only one triangle-bearing alignment
class. Stage58 requires at least nine ordinary cubic collision pairs.

**Theorem.** The remaining two-triangle class (3,2,2,1) is impossible.
Every hypothetical counterexample therefore has exactly one quartic
triangle, in (2,2,2,1,1) or (4,2,1,1). The full bound remains open.

Translate the common alignment to zero and use the exact family

    A=(u,2u,v,2v,w,2w,p=4u,r).

It has five formal ordinary cubic pairs. Therefore another actual
ordinary cubic pair must collide, regardless of any pure refinements.
An ordinary cubic word consists of two copies of one center and one
other label. Protection makes the two words of a collision use four
different physical labels. There are 56 such words. All private pairs
not already forced are covered, and only common powers of two and signs
are normalized in their equations. Every odd integer factor is retained
through exact integer unimodular diagonalization.

The resulting finite proof graph has31 nodes requiring further ordinary
equalities. At each such node the formal ordinary pair count is at most
eight, so Stage58 again forces a new pair. This count strictly increases
along every refinement; pure collisions are never forbidden or assumed
absent. Every leaf closes by a literal protected/label/cap contradiction,
a non-original mass-eight word, a positive quartic-growth certificate
showing89 distinct repeated values, the checked triangle interaction,
or an exact credit/split restriction. The latter restrictions are
documented in stage62_single_class_split_proof.md and
stage62_open_credit_proof.md. The unfinished historical Stage57 tree is
used only for explicit positive identities, not its status or conclusions.

The separate checker imports standard-library helpers from the Stage60
checker and no producer or search routine. It independently reconstructs
all private-pair coverage, every integer reduction and every physical
pair permutation. Each positive quartic pair is supported by an exact
identity f*(value(R)-sum(A))=k*(value(Wi)-value(Wj)), where R is a different
nonnegative mass-eight word and f is a positive power of two. A collision
of Wi and Wj would force the forbidden rival because N is odd.

The completed check passed13,333 nodes,21,761 private direction cases,
25,851 literal private pairs and7,945,564 positive mass-eight identities.
Archive SHA256:

    868ddf0fff6d4059039b177c8fa0f237336d6f843966da765e77127a955a0108

This is a computer-assisted symbolic proof checked by a separate
implementation written by the same assistant. It is not external review
or a proof-assistant formalization. No arbitrary odd order207..247 is
newly excluded in full until the remaining one-triangle family closes.
