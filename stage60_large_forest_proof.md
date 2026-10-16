# Stage60: a uniform four-edge cap for every doubling-alignment class

This is a local proof checkpoint. No new PR was created. The full theorem that every full-valid eight-point cyclic set has N>=248 remains OPEN.

**New theorem, conditional on a hypothetical odd N<248 counterexample:** every alignment class of directed edges x->a with fixed value 2x-a has at most FOUR edges. Its quartic triangles number at most TWO.

The main ingredient is complete exclusion of six of the nine triangle-bearing path-forest shapes. The remaining shapes are

    (2,2,2,1,1), (4,2,1,1), (3,2,2,1).

These are exclusions of entire structural families, allowing arbitrary additional ordinary and pure cubic collisions. They are not conclusions from weak witness bounds. The proof is partly elementary and partly supported by positive integer certificates checked by a separate implementation from the same assistant. It is not external or formal certification.

## 1. The prior structural premises

Stage56 excludes every directed alignment cycle of length at least three in the hypothetical small-order setting. A two-cycle cannot belong to a triangle-bearing class. Four disjoint aligned edges violate the ordinary quintic multiplicity cap. Hence a triangle-bearing class is one of the nine path-forest shapes listed in Stage58.

Stage59 proves that every such class needs an ordinary cubic collision outside the class. Equivalently, in a normalization of one of these forests, a counterexample must add an ordinary cubic equality not forced by its free path-root coordinates. Pure-only refinements cannot evade this requirement.

Every ordinary cubic collision pair can be taken in private form

    2x+b=2y+a,

with x,y,a,b all distinct. The centers cannot coincide, equal tails force equal centers by invertibility of two, and a cross center/tail overlap gives a forbidden protected squarefree pair. Thus the fixed four-distinct-label coverage below is complete for the required new ordinary equalities.

## 2. Exclude the entire (5,3) family by positive quartic separation

After translating the alignment value to zero, this family is

    A=(u,2u,4u,8u,16u,v,2v,4v).

An existing discovery certificate selects89 repeated quartic words in this exact two-root family. Every pair has a positive integer identity

    f*(value(R)-sum(A))=k*(value(Wi)-value(Wj)),

where R is a non-original nonnegative mass-eight word and f is a positive power of two. All3,916 identities have now been checked directly in the two free coordinates u,v. A coincidence of two selected words would give a mass-eight rival, since f is invertible in an odd group. Therefore T4>=89, contradicting the small-order quartic budget.

This excludes all refinements of the family, not just its free-root or no-extra-collision branch.

## 3. A hand root-order lemma for the (7,1) family

Write

    A=(u,2u,4u,8u,16u,32u,64u,p),    sum(A)=127u+p.

Let d=ord(u). Under full validity and odd N<248, d>=159.

The following elementary coin observation is useful. A positive integer expressed as at most seven coins from {1,2,4,8,16,32,64}, with total value at least seven, can be expressed in exactly seven coins: split a coin of value at least two into two halves until seven coins are present. Before reaching seven, not all coins can be ones, because their total value would then be less than seven.

- For odd d<=119, the integer127-d is between8 and126. Its binary expansion uses at most six permitted coins, so it has a seven-coin representation. Modulo d this represents the same block sum as127, and differs from the original seven distinct powers. Appending p gives a forbidden mass-eight word.
- For d=121,123,125, seven-coin totals127+d are respectively

      3*64+32+16+2*4=248,
      3*64+32+16+8+2=250,
      3*64+32+16+8+4=252.

  Again these are explicit seven-term block rivals.
- For odd129<=d<=157, write127+d=256+2m, where0<=m<=14. Four64-coins plus the binary expansion of2m use at most seven coins, since m has at most three binary ones. Splitting yields a seven-term rival.
- The remaining d=127 is excluded by saturation. Every residue has a seven-coin word: zero uses the original block, residues7..126 use binary expansion and splitting, and residues1..6 use their representative r+127, whose minimum coin count is at most four. Thus7B=H=<u>, and8B=H as well. Since127 divides N<248, the ambient group equals H. An eight-term word using only the block represents127u+p, omitting p, and is forbidden.

This covers every odd d<159 without enumerating ambient moduli or parameter assignments. It uses the order of a single structural block and explicit range arguments.

## 4. Complete external-relation closure for (7,1)

The required new private cubic pair gives

    alpha*u+beta*p=0.

If neither word involves p, then beta=0 and the nonzero coefficient alpha has absolute value at most156: an ordinary cubic word on the seven powers has integer value between4 and160. This contradicts d>=159.

Otherwise p occurs once in one of the four private positions, so its coefficient has absolute value one or two. Cancel only common powers of two and orient the sign so beta>0. Every remaining relation is parameterized surjectively in an odd group by

    u=beta*t, p=-alpha*t,    beta in {1,2}.

No odd factor is removed. The complete coverage contains830 literal private cubic pairs and261 normalized coefficient types. Of these,64 are the root-order cases above. The remaining197 types are excluded by176 direct protected/label/multiplicity contradictions, six explicit mass-eight rivals, and fifteen positive quartic-growth89 certificates. Every possibility is closed outright, so the whole (7,1) family is excluded.

## 5. Complete closure of the four three-root forests

Use the exact triangle frame A=(u,2u,v,2v,w,2w,p,r). The following two equations impose each primary forest, with one independent root per path component:

|Shape|Primary relations|Literal first private cases|Normalized first directions|
|---|---|---:|---:|
|(3,3,2)|p=4u, r=4v|832|701|
|(5,2,1)|v=4u, p=16u|833|701|
|(4,3,1)|v=4u, r=4w|833|701|
|(6,1,1)|v=4u, w=16u|834|701|

Stage59 forces a new ordinary equality in every hypothetical counterexample. The coverage takes all pairs of private ordinary cubic words that are not equal in the primary free-root model, keeps their exact integer equations, and cancels only powers of two. Integer unimodular reductions retain every odd diagonal factor as torsion.

All first cases for (3,3,2), (4,3,1) and (6,1,1) are excluded outright by direct identities, inherited cycle/source/multiplicity theorems with their premises checked, explicit mass-eight rivals, or positive89 quartic separation certificates.

For (5,2,1), exactly three first relation modules remain after those positive exclusions:

    5w=2p+r,
    u+2r=5w,
    u+2p=w+2r,

always with v=4u and p=16u. Each formal ordinary cubic partition has P=8. Stage58 already proves P>=9 in any counterexample. Thus every realization of one of these modules must add another ORDINARY equality, even allowing arbitrary pure refinements. The Stage59 set-level count also gives the stronger no-new-ordinary lower bound259 in each case.

For each of the three modules, complete next-private-pair coverage has832 literal cases and700 normalized directions. All are excluded outright. No third relation branch is needed, and no weak bound from a first residual is treated as an exclusion. This closes the entire (5,2,1) family as well.

## 6. Uniform alignment cap and remaining triangle types

The six excluded shapes are precisely the triangle-bearing path forests with at least five edges. Only the three small shapes at the start remain, and they have three or four edges and one or two triangle matchings.

In fact the four-edge cap holds for EVERY alignment class, whether or not it initially contains a triangle. A cycle-free class with at least five edges has at most three path components on eight vertices, hence at least three disjoint edges. It would be a triangle-bearing forest of an excluded shape (or would have four disjoint edges, already forbidden).

Cycles of length at least three are excluded by the published saturation argument. If a class contains a two-cycle, it cannot have a matching of size three. There can be at most one two-cycle in a cyclic group: after translating the common alignment to zero, its two vertices are exactly the two nonzero points of the unique subgroup of order three. The remaining path forest must have matching number at most one, and therefore has at most two edges. Together with the two-cycle, the class has at most four edges.

Thus every alignment class has at most FOUR edges. Those carrying triangles are exactly the three remaining forest shapes and have at most TWO triangles. This limits triangle reuse uniformly across all alignment values; it is not a complete global allocation proof.

## 7. Independent implementation, checked coverage, and boundaries

Run `python -B stage60_certificate_check.py` with the adjacent `stage60_forest_certificates.json.gz` archive. The standard-library checker imports no producer, elimination code or prior checker. It builds private-pair coverage from the56 ordinary cubic words, independently of the producer's ordered physical frames. It checks unimodular reductions, retains all odd torsion, and verifies every coverage case implies the reused proof module. Reused exclusions are unconditional under the small-order hypotheses; the three conditional nodes have complete compulsory-next-equality coverage.

The complete check passed:2,666 proof nodes;4,904 normalized coverage cases;6,658 literal private cases including the long-path inventory; and1,723,040 positive mass-eight pair identities. All first and next inventories are terminal and complete. No helper is left running. The archive SHA256 is292630fd2b93571598eb4f894f791b168888c27939952ad59dad80edd704101b.

The proof depends on the established protected-word and ordinary/cubic caps, the general source theorem, the alignment-cycle theorem, and the global P>=9 theorem. The separate checker is by the same assistant, not formal or external certification. No historical modulus search or incomplete broad tree is a premise.

Full N>=248 remains OPEN. General N>=207 and all even N<248 exclusions are unchanged. The remaining odd207..247 cases must be handled through interaction of the three small alignment classes and their compulsory external collisions.
