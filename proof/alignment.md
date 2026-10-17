# Triangle ownership and alignment forests

Read this chapter after [Assignment](assignment.md). Every lemma assumes
the hypothetical full-valid eight-set in odd N<248. Models retain odd
torsion. Complete finite coverage, rather than the absence of a discovered
witness, closes each computational case. The final two small forests are
handled by the unconditional terminal-edge argument in [Closing](closing.md).

## Triangle edge ownership

The next argument gives q<=h-o, counting distinct paired edges once.

## A paired triangle edge cannot be a genuine split source

Choose any edge in a quartic triangle. Translate its common alignment
value to zero, giving the exact surjective family

    A=(u,2u,v,2v,w,2w,p,r).

Take the paired center edge (u,2u). The complete genuine-split normal
form, with all eight physical positions shared, has720 source presentations
on this edge. A presentation has three distinct centers and omitted-tail
edges forming a two-edge path plus a disjoint edge. It includes every
possible third center, source tails, free lift label and omitted tail.

Every presentation is excluded below248. There are190 exact relation
models after parameter symmetries that FIX the chosen pair. In184 models
a physical label collision or an equality between a protected squarefree
word and a different word is forced. In the remaining six models,
89 repeated quartic words have pairwise positive mass-eight separation
identities. Their23,496 pair identities contradict T4<=88.

The standalone checker reconstructs720 presentations from all ordered
eight-label canonical frames, independently of the producer's shared-source
construction. It verifies integer unimodular row/column reductions, keeps
every odd diagonal factor as torsion, and checks both directions of each
reused model implication. Only the four parameter permutations that fix
(u,2u) may reuse a conditional edge proof. It imports no producer,
eliminator or earlier checker. No witness-search absence or timeout is a
premise. Every accepted model in this archive is excluded outright; edge
closure alone is not used as an exclusion.

The same theorem applies to every paired center edge occurring in any
quartic triangle, by physical label symmetry and translation.

## Count the unused edges once

Let F be the SET of unordered paired center edges occurring in at least
one actual quartic triangle, and let o be the number of its open members.
An edge reused by several triangles is counted once. The ownership argument above says no
genuine split has a source on any edge in F. The o open vertices are
therefore unused by every assignment in the general assignment lemma's auxiliary graph.
Applying that injection to the remaining vertices gives the GENERAL bound

    q<=h-o.                                             (6)

Also, every two-ordinary disjoint-tail source counted in E whose center
edge lies in F is unused by genuine splits. These sources give a literal
subset of U=E-2q, without requiring their values to be fresh per triangle.
Their distinct outputs and center pairs must still be counted explicitly.

Write P=P3ordinary and J=P3total-P. The global count now gives

    N>=260-P+J+R3+2c+2w-2t+2o.                      (7)

This is stronger than an assumed separate credit per triangle: o counts
actual unused edges, including all reuse.

## Complete forest incidence table

By the cycle lemma_alignment_cycle_hand_proof.md, each triangle-bearing alignment
class is a path forest on eight labels with maximum matching three.
For a class with m edges, each pair of disjoint edges gives an ordinary
cubic pair. Adjacent edges give a pair involving a pure cubic word.
These cubic pairs have a unique alignment value, so classes contribute
disjoint sets of pairs. A triangle is a matching of three edges.

|Path vertex sizes|Ordinary pairs Pclass|Pure-involving pairs Jclass|Triangles|
|---|---:|---:|---:|
|(2,2,2,1,1)|3|0|1|
|(4,2,1,1)|4|2|1|
|(3,2,2,1)|5|1|2|
|(6,1,1)|6|4|1|
|(5,2,1)|7|3|3|
|(4,3,1)|7|3|2|
|(3,3,2)|8|2|4|
|(7,1)|10|5|4|
|(5,3)|11|4|6|

For example, Pclass=binom(m,2)-sum(max(s-2,0)) and
Jclass=sum(max(s-2,0)), where s runs over path vertex sizes.
The nine partitions are exhaustive: a matching of size four is forbidden
by the ordinary quintic cap, and smaller matching numbers have no triangle.

## Every counterexample has at least nine ordinary cubic pairs

Suppose P<=8. If t<=2, (7) immediately gives N>=260-8-4=248.
The incidence table leaves only these cases with t>=3:

* One class with three triangles: its shape is(5,2,1), contributes at
  least seven ordinary pairs and at least three pure-involving pairs.
  Thus N>=260-8+3-6=249.
* A two-triangle class and a one-triangle class: their minimum ordinary
  counts are5+3=8. Both minima must hold, so the first shape is(3,2,2,1),
  the second is(2,2,2,1,1), and there are no other ordinary pairs.
* One four-triangle class: with P<=8 its shape must be(3,3,2), accounts
  for all eight ordinary pairs, and has at least two pure-involving pairs.

Three triangle-bearing classes already require P>=9. Two classes with
at least two triangles each require P>=10. Larger single-class triangle
counts require P>=11. No other t>=3 case occurs with P<=8.

For the second case, the(3,2,2,1) class has three terminal paired edges
forming a matching on six labels. All three occur in triangles, and none
can be closed by an ordinary pair from that same alignment class: their
terminal labels have no outgoing edge in it. The other class's three
ordinary pairs have center edges forming a triangle on its three centers.
Such a triangle can contain at most ONE edge from the terminal matching.
At least two of the terminal paired edges are therefore either open or
closed by new pure-involving cubic pairs. Each such pure closure uses a
distinct center edge and contributes a distinct pair to J, beyond the
primary class's one adjacent-edge pair. Consequently J+2o>=1+2=3.
Equation(7) gives N>=260-8-6+3=249.

For the third case, the(3,3,2) class likewise has three terminal paired
edges forming a matching. All its ordinary pairs are already used, so
none of these terminal edges can be closed by an ordinary pair outside
the class. If r terminal edges are closed, they contribute r additional
pure-involving pairs, while the others contribute3-r to o. The two
adjacent-edge pairs are distinct from these closures. Hence

    J+2o>=2+r+2(3-r)>=5.

Equation(7) gives N>=260-8-8+5=249. These exclusions cover P<=8,
proving the global necessary condition

    P3ordinary>=9                                      (COUNTEREXAMPLE).

The resulting nine-pair requirement is used by the complete refinement arguments below.

## Alignment cycles and the nine forests

For a fixed alignment value tau, draw x->a when 2x-a=tau. Physical
distinctness and oddness give indegree and outdegree at most one. Translate
all labels by -tau; the edges become x->2x. A quartic triangle is exactly
a matching of three such edges, on six distinct labels.

## A block saturation lemma

Suppose a directed cycle has r distinct vertices. Its block is
B={delta,2delta,...,2^(r-1)delta}, where d=ord(delta) divides 2^r-1 and
the doubling orbit has length r. If d=2^r-1, then rB=H=<delta>.

Indeed every nonzero residue modulo d has a binary representation using
at most r block terms. Split any term into two copies of its predecessor
along the cycle until there are exactly r terms. Each split preserves its
value, including the wrap delta=2*2^(r-1)delta. The zero residue is the
sum of all r block terms. Thus kB=H for every k>=r.

Let C be the other m=8-r labelled positions and project to G/H. Any word
on C of degree at most m at the projected original sum can be completed
by at least r block terms to a mass-eight word at sum(A). Full validity
therefore forces that word to be exactly the original C word.

This graded property makes the 2^m subset sums distinct: equal different
subsets U,V, oriented so |V|<=|U|, would give the non-original word
V+(C\U) of degree at most m at the original sum. For m>0 the midpoint
of the original sum is outside the subset cube, by complementation and
oddness. Hence the quotient order M=N/d is at least 2^m+1.

## Exclude cycles of length at least three

The possible block orders follow by factoring 2^r-1 and retaining only
orders with doubling orbit length exactly r. The proper-order rivals below
have r nonnegative terms at the block's original sum, which is zero.
Appending every other original label once gives a non-original mass-eight
word. Every listed rival repeats a label, so differs from the original.

|Cycle length r|Possible d|Exclusion|
|---|---|---|
|3|7|The graded-five quotient lemma below gives M>=37, so N>=259.|
|4|5,15|For d=5 use 3*delta+2delta=0. For d=15 use M>=17, so N>=255.|
|5|31|M>=9, so N>=279.|
|6|9,21,63|For d=9 use 3*delta+3*(2delta)=0. For d=21 use 5*delta+16delta=0. For d=63 use M>=5, so N>=315.|
|7|127|M>=3, so N>=381.|
|8|17,51,85,255|For d=17 use 6*delta+2delta+128delta=136delta=0. For d=51 use 6*delta+32delta+64delta=102delta=0. For d=85 use 5*delta+16delta+2*(32delta)=85delta=0. The order d=255 itself gives N>=255.|

The cycles have length at most eight because there are eight labels. Thus
no alignment class contains a cycle of length at least three below248.

For completeness, here is the order-seven quotient lemma. A graded-valid
five-position set has 32 distinct subset sums S. Complementation gives
s-S=S and leaves the unique midpoint mu=s/2 outside S, so odd M>=33.
If 2c belongs to S, its subset must be a singleton: a subset U with at
least two terms gives the forbidden word 2c+(C\U) of degree at most five,
and the empty subset would give c=0. Thus draw c->2c whenever the double
belongs to C. Doubling is injective, and a cycle would have its labels
sum to zero, contradicting the subset cube. These arrows form paths.
The double of each terminal vertex is a distinct hole of S, and cannot
be mu, since 4c=s is a forbidden degree-four word. This excludes M=33.
For M=35 the only two holes apart from mu form a complementary pair. Two
different path exits would give 2c+2d=s, another forbidden degree-four
word. Hence there is one five-vertex path C={t,2t,4t,8t,16t}, with s=31t.
But 4*(16t)+2t=66t=31t in order35 is a non-original degree-five word.
Therefore odd M>=37, and an order-seven block forces N>=7*37=259.

## Exclude a two-cycle in a triangle-bearing class

A two-cycle is {delta,2delta}, where 3delta=0. A class with a three-edge
matching has two further mutually disjoint edges u->2u and v->2v,
disjoint from this cycle. If its matching avoids the cycle, choose any two
of its edges; otherwise use its other two. Let p,r be the remaining two
labels. The original sum is 3u+3v+p+r. The non-original mass-eight word
with three copies each of u and v and one each of p,r has that same sum.
Thus a triangle-bearing class contains no two-cycle either.

Four disjoint aligned edges are excluded by the ordinary quintic cap:
writing their labels as xi,2xi for i=1..4, the four distinct ordinary
quintic words 2xi+sum(j!=i)2xj have the same value. Consequently the
alignment graph of a triangle-bearing class is a disjoint union of paths
whose maximum matching has size exactly three.

## Complete primary forest shapes

Include isolated labels as paths with one vertex. The possible partitions
of eight vertices are exactly

    (2,2,2,1,1), (4,2,1,1), (3,2,2,1),
    (6,1,1), (5,2,1), (4,3,1), (3,3,2), (7,1), (5,3).

The six shapes with at least five edges have only the three- or two-root
models of successive powers of two. This classification covers a chosen
triangle-bearing alignment class. Other alignment classes and additional
cubic relations remain possible; the classification alone does not prove
the full bound or assume their absence.

## Exact triangle normalization and split coverage

A quartic triangle is equivalent to three disjoint aligned edges with common value tau=2x-a. Translate every label by -tau. Its six labels become three doubling pairs, and all eight physical positions are

    A=(u,2u,v,2v,w,2w,p,r).

This normalization uses no division. Full validity and protected equal-degree identities are invariant under translation.

Fix the triangle's ordinary cubic descent

    2u+2v = 2v+2u.

The genuine-split normal form from the source-budget lemma gives

    2u+2v+d+e = 2v+2u+d+e = 2z+2u+b+2v,

where z,b,d,e are exactly the remaining four labels w,2w,p,r, all distinct. Thus the only remaining equation is

    d+e=2z+b.                                             (1)

There are exactly12 ordered choices of z,b; d,e are the unordered complement. This covers every genuine split descending to this cubic pair, with no assumptions about additional cubic relations. Once z,b are specified, all three quintic words and the output are determined.

## Eliminate ten of the twelve choices

The following table is literal coverage of (1). The p/r alternatives are displayed together; the checker reconstructs all12 presentations from ordered physical frames.

|z|b|Necessary equation|Exclusion or residual|
|---|---|---|---|
|w|2w|p+r=4w|The protected squarefree pair p+r equals the repeated pair 2(2w).|
|w|p or r|r=p or p=r|Physical labels collide.|
|2w|w|p+r=5w|The protected squarefree triple w+p+r equals 3(2w).|
|2w|p or r|r=p+3w or p=r+3w|A non-original mass-eight word is 3u+3v+2r, or 3u+3v+2p, respectively.|
|p or r|w|w+r=2p or w+p=2r|A protected squarefree pair equals a repeated pair.|
|p or r|2w|r=2p+w or p=2r+w|Positive quartic growth to89 values, below.|
|p|r|3w=2p+r|Necessary residual.|
|r|p|3w=p+2r|Necessary residual.|

For the mass-eight rival row, the original sum is 3u+3v+3w+p+r. Substituting r=p+3w changes its last three summands to2r. The proposed rival has exactly eight terms; it repeats u,v,r and differs from the original word. The swapped case is identical.

For the growth row, it suffices to exclude p=w+2r. This equation has the exact, surjective parameterization

    A=(u,2u,v,2v,w,2w,w+2r,r)

over any abelian group. The coefficient of p is one, so no odd torsion is discarded. The saved certificate selects89 repeated quartic words. For every pair Wi,Wj it supplies a nonnegative mass-eight word R different from the original, an integer k, and a positive power of two f, with the exact integer identity

    f*(value(R)-sum(A)) = k*(value(Wi)-value(Wj)).          (2)

There are89*88/2=3,916 such identities, checked directly in the four free coordinates u,v,w,r. If Wi and Wj coincided in an odd group, (2) would force value(R)=sum(A), since f is invertible. Full validity forbids this. Therefore all89 quartic values are distinct, contradicting T4<=88. Swapping p and r excludes r=w+2p with the same certificate.

The only necessary residuals for this fixed cubic descent are therefore

    3w=2p+r, or 3w=p+2r.                                 (3)

No bound obtained by the absence of witnesses or by a timeout is used.

## Six residual presentations, at most one compatible

Apply the ten-choice elimination to each of the triangle's three cubic descents. The six necessary presentations are

    3xi=2p+r or 3xi=p+2r,    xi in {u,v,w}.                (4)

Each presentation determines its quintic fiber uniquely. All15 pairs of distinct presentations are incompatible:

1. **Different xi, same orientation.** The two equations give 3xi=3xj. This equates the distinct protected squarefree pairs xi+2xi and xj+2xj. There are six such pairs of presentations.
2. **Same xi, opposite orientation.** Subtraction gives p=r, a physical label collision. There are three such pairs.
3. **Different xi, opposite orientation.** Name them so 3xi=2p+r and 3xj=p+2r, and let xk be the other triangle center. The original sum is

       3xk+3xi+3xj+p+r = 3xk+4p+4r.

   Take xk and2xk once each, xi and2xi twice each, and r twice. This non-original eight-term word has value

       3xk+6xi+2r = 3xk+4p+4r.

   It is a forbidden mass-eight rival. There are six such pairs.

These identities use no cancellation by three. The checker verifies all15 pairs in the exact five-coordinate triangle family. Two distinct genuine split outputs supported by the triangle would give two distinct presentations in (4), which is impossible. This proves the theorem.

## Global split compression

Let P=P3ordinary. Let D be the SET of ordinary cubic pairs that occur in at least one actual quartic triangle, counted once even when reused. Every split has a unique cubic descent.

- At most4(P-|D|) splits descend outside D, by the source-budget lemma four-splits-per-pair lemma.
- At most t splits descend inside D: assign each such split to any triangle containing its descent. No triangle can receive two splits by the theorem just proved, so this assignment is injective.

Consequently

    q <= 4(P-|D|)+t.                                    (5)

The established triangle-incidence bound says each cubic pair feeds at most two triangles, so3t<=2|D|. Hence also

    q <= 4P-5t.                                         (6)

The set-level form (5) is often stronger and is needed for the forest corollary. Neither (5) nor (6) alone proves the full bound.

## A counting bound that allows all pure refinements

For a hypothetical full-valid eight-set in odd N<248, retain the general count

    N >= 288+h+R3+2c+2w-2(t+q+P).                       (1)

Here P=P3ordinary. The general assignment q<=h gives h-2q>=-q. All other displayed correction terms are nonnegative. Thus

    N >= 288-q-2t-2P.                                  (2)

This inequality does not fix the pure cubic partition or forbid new pure collisions. It uses no assumption that formally different outputs remain different.

## All nine ordinary-collision-exhausted forest families are excluded

Choose an ACTUAL triangle-bearing alignment class. By the cycle exclusion below, its graph is a path forest on eight physical labels, with maximum matching exactly three. Let P0 be its number of disjoint edge pairs, t0 its number of three-edge matchings, and D0 the set of its edge pairs occurring in at least one such matching.

Every disjoint edge pair gives an ordinary cubic collision pair with the class's alignment value. That value is uniquely recoverable from the pair. Distinct classes therefore have disjoint cubic-pair inventories. Different matchings produce different quartic triangle outputs under the ordinary cap; otherwise the union of their representations would contain more than three ordinary words, and the three-word fiber recovers its matching uniquely.

Suppose EVERY ordinary cubic pair in the set belongs to the chosen class. Then P=P0. Another triangle-bearing class would contribute ordinary cubic pairs of its own alignment value, so no such class exists; t=t0 and |D|=|D0|. The global split-compression formula gives

    q <= Q0 := 4(P0-|D0|)+t0.

Combining with (2) proves N>=B0:=288-Q0-2t0-2P0.

|Path vertex sizes|P0|t0|D0 count|Q0|B0|
|---|---:|---:|---:|---:|---:|
|(2,2,2,1,1)|3|1|3|1|279|
|(4,2,1,1)|4|1|3|5|273|
|(3,2,2,1)|5|2|5|2|272|
|(6,1,1)|6|1|3|13|261|
|(5,2,1)|7|3|7|3|265|
|(4,3,1)|7|2|5|10|260|
|(3,3,2)|8|4|8|4|260|
|(7,1)|10|4|9|8|252|
|(5,3)|11|6|11|6|248|

The nine shapes are exhaustive. Their counts are obtained by selecting disjoint edge pairs and triples in literal paths; the checker independently reconstructs this table from all integer partitions of eight. In particular, D0 is not assumed equal to P0. For example, the six-vertex path has six disjoint edge pairs but only three of them occur in its unique matching of size three.

Every B0 is at least248. Thus the whole family in which ordinary collisions are exhausted by one triangle class is excluded. Equivalently, EVERY chosen triangle-bearing class of a remaining counterexample must have at least one ordinary cubic pair outside it. Pure-only refinements cannot evade this conclusion.

## Quantify the additional structure rather than branch blindly

Keep the chosen class, but now allow r ordinary cubic pairs outside it and t_out triangles in other classes. Then P=P0+r and t=t0+t_out. Let D_out be the ordinary pairs in those other triangles. Alignment uniqueness makes D_out disjoint from the chosen class, and the two-triangles-per-pair bound gives |D_out|>=3t_out/2.

The set-level split bound consequently gives

    q <= Q0+4(r-|D_out|)+t_out
      <= Q0+4r-5t_out.

Use this in (2) to obtain the GENERAL bound

    N >= B0-6r+3t_out.                                  (3)

Therefore a counterexample, with integer N<=247, must satisfy

    6r-3t_out >= B0-247.                                (4)

This is an additional structural necessity, not a claim that satisfying it realizes a cyclic set. It implies the following minimum external ordinary-pair counts, and extra triangle classes can raise the requirement further:

|Chosen shape|Minimum r|
|---|---:|
|(2,2,2,1,1)|6|
|(4,2,1,1)|5|
|(3,2,2,1)|5|
|(6,1,1)|3|
|(5,2,1)|3|
|(4,3,1)|3|
|(3,3,2)|3|
|(7,1)|1|
|(5,3)|1|

All these inequalities hold while allowing arbitrary additional pure cubic collisions. Additional ordinary triples and quartic splits only contribute nonnegative terms omitted in (2).

## The prior structural premises

the cycle lemma excludes every directed alignment cycle of length at least three in the hypothetical small-order setting. A two-cycle cannot belong to a triangle-bearing class. Four disjoint aligned edges violate the ordinary quintic multiplicity cap. Hence a triangle-bearing class is one of the nine path-forest shapes listed in the triangle-ownership lemma.

the triangle-split lemma proves that every such class needs an ordinary cubic collision outside the class. Equivalently, in a normalization of one of these forests, a counterexample must add an ordinary cubic equality not forced by its free path-root coordinates. Pure-only refinements cannot evade this requirement.

Every ordinary cubic collision pair can be taken in private form

    2x+b=2y+a,

with x,y,a,b all distinct. The centers cannot coincide, equal tails force equal centers by invertibility of two, and a cross center/tail overlap gives a forbidden protected squarefree pair. Thus the fixed four-distinct-label coverage below is complete for the required new ordinary equalities.

## Exclude the entire (5,3) family by positive quartic separation

After translating the alignment value to zero, this family is

    A=(u,2u,4u,8u,16u,v,2v,4v).

An existing discovery certificate selects89 repeated quartic words in this exact two-root family. Every pair has a positive integer identity

    f*(value(R)-sum(A))=k*(value(Wi)-value(Wj)),

where R is a non-original nonnegative mass-eight word and f is a positive power of two. All3,916 identities have now been checked directly in the two free coordinates u,v. A coincidence of two selected words would give a mass-eight rival, since f is invertible in an odd group. Therefore T4>=89, contradicting the small-order quartic budget.

This excludes all refinements of the family, not just its free-root or no-extra-collision branch.

## A hand root-order lemma for the (7,1) family

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

## Complete external-relation closure for (7,1)

The required new private cubic pair gives

    alpha*u+beta*p=0.

If neither word involves p, then beta=0 and the nonzero coefficient alpha has absolute value at most156: an ordinary cubic word on the seven powers has integer value between4 and160. This contradicts d>=159.

Otherwise p occurs once in one of the four private positions, so its coefficient has absolute value one or two. Cancel only common powers of two and orient the sign so beta>0. Every remaining relation is parameterized surjectively in an odd group by

    u=beta*t, p=-alpha*t,    beta in {1,2}.

No odd factor is removed. The complete coverage contains830 literal private cubic pairs and261 normalized coefficient types. Of these,64 are the root-order cases above. The remaining197 types are excluded by176 direct protected/label/multiplicity contradictions, six explicit mass-eight rivals, and fifteen positive quartic-growth89 certificates. Every possibility is closed outright, so the whole (7,1) family is excluded.

## Complete closure of the four three-root forests

Use the exact triangle frame A=(u,2u,v,2v,w,2w,p,r). The following two equations impose each primary forest, with one independent root per path component:

|Shape|Primary relations|Literal first private cases|Normalized first directions|
|---|---|---:|---:|
|(3,3,2)|p=4u, r=4v|832|701|
|(5,2,1)|v=4u, p=16u|833|701|
|(4,3,1)|v=4u, r=4w|833|701|
|(6,1,1)|v=4u, w=16u|834|701|

the triangle-split lemma forces a new ordinary equality in every hypothetical counterexample. The coverage takes all pairs of private ordinary cubic words that are not equal in the primary free-root model, keeps their exact integer equations, and cancels only powers of two. Integer unimodular reductions retain every odd diagonal factor as torsion.

All first cases for (3,3,2), (4,3,1) and (6,1,1) are excluded outright by direct identities, inherited cycle/source/multiplicity theorems with their premises checked, explicit mass-eight rivals, or positive89 quartic separation certificates.

For (5,2,1), exactly three first relation modules remain after those positive exclusions:

    5w=2p+r,
    u+2r=5w,
    u+2p=w+2r,

always with v=4u and p=16u. Each formal ordinary cubic partition has P=8. the triangle-ownership lemma already proves P>=9 in any counterexample. Thus every realization of one of these modules must add another ORDINARY equality, even allowing arbitrary pure refinements. The the triangle-split lemma set-level count also gives the stronger no-new-ordinary lower bound259 in each case.

For each of the three modules, complete next-private-pair coverage has832 literal cases and700 normalized directions. All are excluded outright. No third relation branch is needed, and no weak bound from a first residual is treated as an exclusion. This closes the entire (5,2,1) family as well.

## Uniform alignment cap and remaining triangle types

The six excluded shapes are precisely the triangle-bearing path forests with at least five edges. Only the three small shapes at the start remain, and they have three or four edges and one or two triangle matchings.

In fact the four-edge cap holds for EVERY alignment class, whether or not it initially contains a triangle. A cycle-free class with at least five edges has at most three path components on eight vertices, hence at least three disjoint edges. It would be a triangle-bearing forest of an excluded shape (or would have four disjoint edges, already forbidden).

Cycles of length at least three are excluded by the cycle-saturation argument above. If a class contains a two-cycle, it cannot have a matching of size three. There can be at most one two-cycle in a cyclic group: after translating the common alignment to zero, its two vertices are exactly the two nonzero points of the unique subgroup of order three. The remaining path forest must have matching number at most one, and therefore has at most two edges. Together with the two-cycle, the class has at most four edges.

Thus every alignment class has at most FOUR edges. Those carrying triangles are exactly the three remaining forest shapes and have at most TWO triangles. This limits triangle reuse uniformly across all alignment values; the global allocation is supplied in the subsequent argument.

## Complete interaction coverage

Normalize one triangle to A=(u,2u,v,2v,w,2w,p,r). A second triangle consists of three disjoint directed edges on these same eight physical labels, with a common alignment gamma. There are3,360 literal presentations: choose three centers, three tails among the remaining five labels, and a bijection. For edges (xi,ai), impose the two equations2Axi-Aai=2Ax0-Aa0. No odd integer is divided out.

Exactly one presentation has gamma=0 formally. Another603 force gamma=0 through their integer relation modules. These are rejected only under the selected hypothesis that the second class is DIFFERENT; they are not full-model exclusions. The remaining2,756 presentations use unconditional model exclusions or a complete residual proof.

The initial residual modules give14 types under permutation of the three primary doubling pairs and of p,r. By explicit relabeling and translation using an actual triangle, they reduce to nine affine families. Each has six formal ordinary cubic collision pairs. A counterexample needs at least nine by the triangle-ownership lemma, so every family must acquire a new PRIVATE ordinary collision.

The alternating seven-vertex-path family is represented by

    u+4v=5w,    20v+r=21w.

Its complete first refinement leaves one system with eight ordinary pairs, so another ordinary equality is compulsory. All next cases close positively. This excludes the entire alternating family, allowing all additional relations and retaining all odd torsion.

For the other eight affine families, complete first-private-pair coverage leaves precisely two unresolved modules. They have seven and eight ordinary pairs, respectively. Another ordinary equality is compulsory in both, and all of those next cases close positively. No further branch is needed. Weak quartic-growth bounds in the first residuals are never used as exclusions.

All accepted closures are direct protected/label/multiplicity contradictions, explicit mass-eight rivals, checked alignment-cycle/source premises, applications of the large-forest lemma's four-edge bound, an explicit affine map to the already excluded alternating family, or positive separation of89 repeated quartic words. Every affine map is a permutation of all eight physical positions followed by translation; it preserves full validity and cancels no odd factor.

Assume a full-valid eight-point set in an odd cyclic group of order
N<248. the large-forest lemma restricts a triangle-bearing alignment class to one of
(2,2,2,1,1), (4,2,1,1), (3,2,2,1), and the interaction lemma proves that there is
at most one such class globally. These are already checked premises.

**Theorem.** At most one genuine quintic split has its unique ordinary
cubic descent in any quartic triangle of A. Hence, with D the set of
ordinary cubic pairs contained in triangles,

    q <= 4(P-|D|)+1.

For the first two shapes there is one triangle, so the triangle-split lemma proves the
claim. For the last shape, translate the alignment to zero and label

    A=(u,2u,v,2v,w,2w,p=4u,r).

There are exactly two triangles:

    L=(u->2u,v->2v,w->2w),
    H=(2u->p,v->2v,w->2w).

First, a cubic pair in two distinct triangles supports no genuine split.
The pair fixes two directed edges, since its ordinary centers and cross
tails are physical labels. the triangle-split lemma proves that the two labels added in
the quintic lift must be exactly the two labels on the third edge of
the supporting triangle. Two different third edges cannot give the
same added-label pair. The only other possibility is opposite directions
on the same pair, a two-cycle in the triangle-bearing class, already
excluded. This uses label sets, without cancelling by an odd integer.
In particular H's v/w descent supports no split.

Consider H's 2u/v descent, omitting the w->2w edge. Relative to H the
two free labels are u and r. the triangle-split lemma's complete normal-form theorem
leaves only

    3w=2u+r, or 3w=u+2r.

In the first case the third quintic center is u. One source has centers
u and 2u, the paired edge of L. the triangle-ownership lemma forbids a genuine split with
that source. In the second case the original sum is

    sum(A)=7u+3v+3w+r=8u+3v+3r.

It equals the eight-term word consisting of two copies of p=4u, three
copies of v, and three copies of r. This is a different nonnegative
mass-eight word and contradicts full validity. The 2u/w descent is
identical after interchanging v and w. Thus H supports no split at all.

Every surviving split descending inside D must therefore be attached
to L, which supports at most one by the triangle-split lemma. Splits descending outside
D are bounded by four per ordinary cubic pair, proving the displayed
inequality. This theorem alone does not prove N>=248.

## Credit leaves and refinements

Fix an exact relation model of A=(u,2u,v,2v,w,2w,p,r), retaining all odd torsion. Its primary triangle alignment is zero. Assume an actual full-valid odd N<248 realization adds NO ordinary cubic equality beyond the model; arbitrary pure refinements are permitted. Let F be the distinct paired edges of the model's quartic triangles, and o0 their formally open count.

## The primary alignment graph cannot acquire another edge

Any new aligned edge has two endpoints, so among the primary triangle's three disjoint edges there is an edge disjoint from it. These two edges give an ordinary cubic collision pair. If that pair were already formal, the formal alignment of the existing edge would force the new edge to be formal as well. Thus a newly aligned edge forces a new ordinary equality, contrary to the hypothesis. The primary path forest is therefore fixed under pure-only refinements.

## Long terminal edges cannot close purely

Translate the alignment to zero. A terminal edge a->b=2a on a path of at least three vertices has a predecessor c with a=2c and b=4c. Pure-involving cubic closure of its center edge has one of the forms

    3a=2b+f,    3b=2a+g,    3a=3b.

The first gives f=-a, so the protected squarefree triple c+b+f equals3c. The three labels are distinct: coincidence of f with c forces a two-cycle, and coincidence with b forces a collision in an odd group. The second gives g=2b, extending the path, contrary to terminality and the fixed graph. The third gives3a=0 and a reverse edge b->a, a forbidden two-cycle in a triangle-bearing class. Thus a formally open long terminal remains open when no new ordinary equality is added.

An internal paired edge a->b with b->2b is already formally closed through3b=2a+2b. Hence the formally open edges of F are terminal edges.

## A new pure closure of a short terminal uses an isolated label

For a two-vertex component a->2a, the only possible pure closure is f=-a; the other two closure forms extend the path or create a two-cycle. If f has an outgoing edge f->2f, then either that edge is disjoint from a->2a or the two edges create a forbidden two-cycle/collision. In the disjoint case a=-f gives a literal mass-eight rival: replace the four original labels a,2a,f,2f by two copies each of a and f, leaving every other label once. Both block sums are zero.

If f is a non-isolated terminal label, write f=2b for its predecessor. The short component is disjoint from that path, so a,2a,b,f are four different labels. From a=-2b we get the private ordinary cubic equality

    2[f]+[2a] = 2[b]+[a].

Brackets denote one occurrence of a physical label, so [2a] is the
terminal label, not two occurrences of the center a. Both sides have
degree three. Their common value is zero when f=2b=-a.

Conversely its difference, using f=2b, is2b+a. If the equality were already formal, a=-f would be formal and the paired edge would not be formally open. Therefore a NEW pure closure through such f adds an ordinary equality, contrary to the hypothesis.

Only an isolated vertex can supply a new pure closure of a formally open short terminal. Each isolated vertex can supply at most one, because distinct terminal centers have distinct negatives in the actual group.

## Count which isolated labels are still available

An isolated label f is unavailable if its negative already equals ANY formal point of A. Then it cannot newly equal the negative of another physical label in a full-valid realization without a label collision; if it equals the relevant center formally, the edge was already closed. This includes f=0 and formal opposite pairs of isolated labels.

Let b0 count isolated labels whose negative is absent from the formal point set. Let ell0 count formally open paired terminal edges on paths of at least three vertices. Pure-only refinements can close at most b0 of the o0 edges, and none of the ell0 long terminals. Therefore

    o_actual >= o_lower := max(ell0,o0-b0).               (1)

The remaining shapes have respectively two, two and one isolated vertices. This does not assume independent fresh credits per triangle: F is a set, and every potential pure closure is charged to an actual isolated label once.

## A stronger proof-forcing quintic target

P=P3ordinary, t and c=C3ordinary are fixed if no new ordinary equality is added. R3_actual>=R0, where R0 is the formal repeated-cubic excess: merging formal cubic fibers cannot decrease sum binom(size-1,2). Use the general count and q<=h-o:

    N>=288+h+R3+2c+2w-2(t+q+P)
      >=288-h+R3+2c+2w+2o-2t-2P.

Since a counterexample has N<=247, and T3=36+h+R3,

    T3 >= 77+2R0+2c+2o_lower-2t-2P.                    (2)

Consequently a positive quintic separation certificate at

    T5 >= 115-2R0-2c-2o_lower+2t+2P                    (3)

contradicts N>=56+T3+T5 and N<=247, under the no-new-ordinary hypothesis. It therefore forces another ORDINARY equality. It is not an unconditional whole-model exclusion unless the independent T5>=156-R0 bound also holds.

Equation(3) gives a smaller rigorous target than the universal quintic156 bound. The distinction between a conditional forcing leaf and an unconditional exclusion is part of the certificate contract.

## Persistent quartic and quintic credits

Let E0 be the number of formal quartic fibers consisting of exactly two
ordinary words with private centers and disjoint two-label tails. Under
the no-new-ordinary hypothesis, each remains an E fiber. A third ordinary
word would have a new private center outside the four old tail labels
and the two old centers. Its two tails must intersect the union of those
four old tails. Subtract a common tail from it and an old word: this gives
a new ordinary cubic equality. If this equality had already been formal,
the third quartic word would already have been in the formal fiber.
Two formal E fibers cannot merge because that would give four ordinary
quartic words, forbidden by the established cap. Therefore E>=E0.

Let U0 count those E0 outputs whose center edge belongs to F, once per
output. the triangle-ownership lemma forbids their consumption by genuine splits. Thus
U=E-2q>=U0 under the same hypothesis. Formal quartic split triples w0
and formal genuine quintic split triples q0 persist even when new
ordinary equalities are allowed: adding another ordinary word or merging
their fibers violates the cap of three. Consequently w>=w0, q>=q0 and
T3=36+h+R3>=36+q0+R0.

The necessary counterexample ledger is

    5t >= 2+2(o+R3+c)+5w+U.

With P,t,c fixed under pure refinements, its formal lower credits force
another ordinary equality whenever

    2+2(o_lower+R0+c)+5w0+U0 > 5t.                    (4)

The quartic budget also gives E>=80+t+2c-w-4P. From the exact weighted
count 2N>=496+2(h+R3+c)-5t+5w+E-4q and q<=h-o,

    2T3 >= 74+4R0+2c-5t+4o_lower
           +max(E0+5w0,80+t+2c-4P+4w0).             (5)

Take the integer ceiling of half the right side, and the maximum with
(2) and 36+R0+q0. A positive quintic certificate at 192 minus this
lower bound forces another ordinary equality. At 156-R0-q0 it excludes
the whole model. These two conclusions must remain separate.

For the robust N bound, let h0 and o0 be the formal open-center and
paired-edge counts. Every paired edge that becomes closed adds a
different repeated-cubic collision pair, recoverable from its two
centers. Thus h0-h_actual >= o0-o_actual, even if one cubic fiber gains
several pure words. Consequently

    q <= h_actual-o_actual <= h0-o0.

Combining this with the single-class split theorem gives

    q <= min(h0-o0,4(P-|D|)+1,4P-11c).

Under no new ordinary equality this yields the robust bound

    N >= 288-q_max+R0+2c+2w0-2t-2P.                  (6)

With four primary aligned edges, the actual triangle count is already
fixed even when new ordinary equalities are allowed: the large-forest lemma forbids a
fifth edge, and the interaction lemma forbids another triangle-bearing class. Otherwise
the unconditional maximum is two. These facts justify the unconditional
credit exclusion 2+2(R0+c)+5w0>5*t_max.

## Excluding the two-triangle class

Assume a full-valid eight-point set in an odd cyclic group of order
N<248. the general assignment lemma forces a quartic triangle. the large-forest lemma gives four aligned
edges at most, and the interaction lemma permits only one triangle-bearing alignment
class. the triangle-ownership lemma requires at least nine ordinary cubic collision pairs.

**Theorem.** The remaining two-triangle class (3,2,2,1) is impossible.
Every hypothetical counterexample therefore has exactly one quartic
triangle, in (2,2,2,1,1) or (4,2,1,1). The two one-triangle forests are handled by the closing argument.

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
eight, so the triangle-ownership lemma again forces a new pair. This count strictly increases
along every refinement; pure collisions are never forbidden or assumed
absent. Every leaf closes by a literal protected/label/cap contradiction,
a non-original mass-eight word, a positive quartic-growth certificate
showing89 distinct repeated values, the checked triangle interaction,
or an exact credit/split restriction. The latter restrictions are
documented in the single-class split and credit arguments above. Only explicit identities from incomplete research trees are reused; the complete checker reconstructs each required identity and case.

The separate checker imports standard-library helpers from the large-forest lemma
checker and no producer or search routine. It independently reconstructs
all private-pair coverage, every integer reduction and every physical
pair permutation. Each positive quartic pair is supported by an exact
identity f*(value(R)-sum(A))=k*(value(Wi)-value(Wj)), where R is a different
nonnegative mass-eight word and f is a positive power of two. A collision
of Wi and Wj would force the forbidden rival because N is odd.

The completed check passed13,333 nodes,21,761 private direction cases,
25,851 literal private pairs and7,945,564 positive mass-eight identities.
The archive content hash is recorded in the release manifest.

This certificate closes the two-triangle component. The closing chapter handles both remaining one-triangle forests.
