# Triangle ownership and alignment forests

Assume a valid eight-set in an odd cyclic group of order N<248. Dependencies
entering this chapter are [Lemmas 5–6](counting.md) and [Lemmas 7–8](assignment.md).
Computer-assisted statements below use exact integer identities and complete local
coverage; odd torsion is retained. The elementary terminal-edge lemma is proved
early because it simplifies both the collision floor and the final contradiction.

## Lemma 9. Triangle-edge ownership (computer-assisted)

The next argument gives q<=h-o, counting distinct paired edges once.

## A paired triangle edge cannot be a genuine split source

Choose any edge in a quartic triangle. Translate its common alignment value to zero,
giving the exact surjective family

$$
A=(u,2u,v,2v,w,2w,p,r).
$$

Take the paired center edge (u,2u). The complete genuine-split normal form, with all
eight physical positions shared, has 720 source presentations on this edge. A
presentation has three distinct centers and omitted-tail edges forming a two-edge
path plus a disjoint edge. It includes every possible third center, source tails,
free lift label and omitted tail.

Every presentation is excluded below 248. There are 190 exact relation models after
parameter symmetries that fix the chosen pair. In184 models a physical label
collision or an equality between a protected squarefree word and a different word is
forced. In the remaining six models, 89 repeated quartic words have pairwise
positive mass-eight separation identities. Their 23,496 pair identities contradict
T4<=88.

The standalone checker reconstructs 720 presentations from all ordered eight-label
canonical frames, independently of the producer's shared-source construction. It
verifies integer unimodular row/column reductions, keeps every odd diagonal factor
as torsion, and checks both directions of each reused model implication. Only the
four parameter permutations that fix (u,2u) may reuse a conditional edge proof. It
imports no producer, eliminator or earlier checker. No witness-search absence or
timeout is a premise. Every accepted model in this archive is excluded outright;
edge closure alone is not used as an exclusion.

The same theorem applies to every paired center edge occurring in any quartic
triangle, by physical label symmetry and translation.

## Count the unused edges once

Let F be the set of unordered paired center edges occurring in at least one actual
quartic triangle, and let o be the number of its open members. An edge reused by
several triangles is counted once. The ownership argument above says no genuine
split has a source on any edge in F. The o open vertices are therefore unused by
every assignment in the general assignment lemma's auxiliary graph. Applying that
injection to the remaining vertices gives the bound

$$
q\le h-o.
$$

Also, every two-ordinary disjoint-tail source counted in E whose center edge lies in
F is unused by genuine splits. These sources give a literal subset of U=E-2q,
without requiring their values to be fresh per triangle. Their distinct outputs and
center pairs must still be counted explicitly.

Write P=P3 ordinary and J=P3total-P. The global count now gives

$$
N\ge 260-P+J+R_3+2c+2w-2t+2o.
$$

This is stronger than an assumed separate credit per triangle: o counts actual
unused edges, including all reuse.

## Lemma 10. Terminal paired edges are open (elementary)

**Hypotheses:** a valid eight-set in odd order, containing a quartic triangle. No
forest exclusion or no-new-equality assumption is needed. Translate its alignment to
zero, giving $A=(u,2u,v,2v,w,2w,p,r)$ with all eight physical labels distinct.

No two distinct physical labels x,y satisfy x+y=z for a label z of A. Choose one of
the three doubling pairs b,2b disjoint from x,y. In the original word replace
x,y,b,2b by z,b,b,b. This is a nonnegative mass-eight word with the same value. It
differs from the original, since the single added label z cannot restore both
removed labels x,y. Validity forbids it.

For an aligned edge a->b=2a, closure means 2(a-b)=x-y, or y=x+b. The preceding fact
forces x=b, y=2b. Conversely an outgoing edge b->2b provides this difference. Thus a
paired edge is open exactly when it is terminal in its actual alignment class, under
all ordinary and pure refinements. This lemma also applies to the paired edges of
every triangle in the class. It replaces the weaker conditional terminal-credit
analysis.

## Lemma 11. Alignment cycles and the nine forests (elementary)

For a fixed alignment value tau, draw x->a when 2x-a=tau. Physical distinctness and
oddness give indegree and outdegree at most one. Translate all labels by -tau; the
edges become x->2x. A quartic triangle is exactly a matching of three such edges, on
six distinct labels.

## A block saturation lemma

Suppose a directed cycle has r distinct vertices. Its block is
B={delta,2delta,...,2^(r-1)delta}, where d=ord(delta) divides 2^r-1 and the doubling
orbit has length r. If d=2^r-1, then rB=H=<delta>.

Indeed every nonzero residue modulo d has a binary representation using at most r
block terms. Split any term into two copies of its predecessor along the cycle until
there are exactly r terms. Each split preserves its value, including the wrap
delta=2*2^(r-1)delta. The zero residue is the sum of all r block terms. Thus kB=H
for every k>=r.

Let C be the other m=8-r labelled positions and project to G/H. Any word on C of
degree at most m at the projected original sum can be completed by at least r block
terms to a mass-eight word at sum(A). Full validity therefore forces that word to be
exactly the original C word.

This graded property makes the 2^m subset sums distinct: equal different subsets
U,V, oriented so |V|<=|U|, would give the non-original word V+(C\U) of degree at
most m at the original sum. For m>0 the midpoint of the original sum is outside the
subset cube, by complementation and oddness. Hence the quotient order M=N/d is at
least 2^m+1.

## Exclude cycles of length at least three

The possible block orders follow by factoring 2^r-1 and retaining only orders with
doubling orbit length exactly r. The proper-order rivals below have r nonnegative
terms at the block's original sum, which is zero. Appending every other original
label once gives a non-original mass-eight word. Every listed rival repeats a label,
so differs from the original.

|Cycle length r|Possible d|Exclusion|
|---|---|---|
| 3 | 7 | The graded-five quotient lemma below gives $M\ge37$, so $N\ge259$. |
| 4 | 5, 15 | For $d=5$ use $3\delta+2\delta=0$. For $d=15$ use $M\ge17$, so $N\ge255$. |
| 5 | 31 | $M\ge9$, so $N\ge279$. |
| 6 | 9, 21, 63 | For $d=9$ use $3\delta+3(2\delta)=0$. For $d=21$ use $5\delta+16\delta=0$. For $d=63$ use $M\ge5$, so $N\ge315$. |
| 7 | 127 | $M\ge3$, so $N\ge381$. |
| 8 | 17, 51, 85, 255 | For $d=17$ use $6\delta+2\delta+128\delta=136\delta=0$. For $d=51$ use $6\delta+32\delta+64\delta=102\delta=0$. For $d=85$ use $5\delta+16\delta+2(32\delta)=85\delta=0$. The order $d=255$ gives $N\ge255$. |

The cycles have length at most eight because there are eight labels. Thus no
alignment class contains a cycle of length at least three below 248.

For completeness, here is the order-seven quotient lemma. A graded-valid
five-position set has 32 distinct subset sums S. Complementation gives s-S=S and
leaves the unique midpoint mu=s/2 outside S, so odd M>=33. If 2c belongs to S, its
subset must be a singleton: a subset U with at least two terms gives the forbidden
word 2c+(C\U) of degree at most five, and the empty subset would give c=0. Thus draw
c->2c whenever the double belongs to C. Doubling is injective, and a cycle would
have its labels sum to zero, contradicting the subset cube. These arrows form paths.
The double of each terminal vertex is a distinct hole of S, and cannot be mu, since
4c=s is a forbidden degree-four word. This excludes M=33. For M=35 the only two
holes apart from mu form a complementary pair. Two different path exits would give
2c+2d=s, another forbidden degree-four word. Hence there is one five-vertex path
C={t,2t,4t,8t,16t}, with s=31t. But 4*(16t)+2t=66t=31t in order 35 is a non-original
degree-five word. Therefore odd M>=37, and an order-seven block forces N>=7*37=259.

## Exclude a two-cycle in a triangle-bearing class

A two-cycle is {delta,2delta}, where 3delta=0. A class with a three-edge matching
has two further mutually disjoint edges u->2u and v->2v, disjoint from this cycle.
If its matching avoids the cycle, choose any two of its edges; otherwise use its
other two. Let p,r be the remaining two labels. The original sum is 3u+3v+p+r. The
non-original mass-eight word with three copies each of u and v and one each of p,r
has that same sum. Thus a triangle-bearing class contains no two-cycle either.

Four disjoint aligned edges are excluded by the ordinary quintic cap: writing their
labels as xi,2xi for i=1..4, the four distinct ordinary quintic words
2xi+sum(j!=i)2xj have the same value. Consequently the alignment graph of a
triangle-bearing class is a disjoint union of paths whose maximum matching has size
exactly three.

## Complete primary forest shapes

Include isolated labels as paths with one vertex. The possible partitions of eight
vertices are exactly

$$
\begin{gathered}
(2,2,2,1,1), (4,2,1,1), (3,2,2,1), \\
(6,1,1), (5,2,1), (4,3,1), (3,3,2), (7,1), (5,3).
\end{gathered}
$$

The six shapes with at least five edges have only the three- or two-root models of
successive powers of two. This classification covers a chosen triangle-bearing
alignment class. Other alignment classes and additional cubic relations remain
possible; the classification alone does not prove the full bound or assume their
absence.

## Complete forest incidence table

By Lemma 11, each triangle-bearing alignment class is a path forest on eight labels
with maximum matching three. For a class with m edges, each pair of disjoint edges
gives an ordinary cubic pair. Adjacent edges give a pair involving a pure cubic
word. These cubic pairs have a unique alignment value, so classes contribute
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

For example, Pclass=binom(m,2)-sum(max(s-2,0)) and Jclass=sum(max(s-2,0)), where s
runs over path vertex sizes. The nine partitions are exhaustive: a matching of size
four is forbidden by the ordinary quintic cap, and smaller matching numbers have no
triangle.

## Lemma 12. Nine ordinary cubic pairs are necessary (elementary)

Suppose P<=8. If t<=2, the ownership counting bound immediately gives
N>=260-8-4=248. The incidence table leaves only these cases with t>=3:

* One class with three triangles: its shape is (5,2,1), contributes at
  least seven ordinary pairs and at least three pure-involving pairs.   Thus
N>=260-8+3-6=249.
* A two-triangle class and a one-triangle class: their minimum ordinary
  counts are 5+3=8. Both minima must hold, so the first shape is (3,2,2,1),   the
second is (2,2,2,1,1), and there are no other ordinary pairs.
* One four-triangle class: with P<=8 its shape must be(3,3,2), accounts
  for all eight ordinary pairs, and has at least two pure-involving pairs.

Three triangle-bearing classes already require P>=9. Two classes with at least two
triangles each require P>=10. Larger single-class triangle counts require P>=11. No
other t>=3 case occurs with P<=8.

For the second case, the (3,2,2,1) class has three terminal paired edges, all
belonging to triangles. Lemma 10 gives o>=3 under arbitrary further equalities. Thus
the ownership counting bound gives N>=260-8-6+6=252. For the third case, the (3,3,2)
class has three such edges and at least two pure-involving pairs; hence
N>=260-8+2-8+6=252.

These exclusions cover P<=8, proving the global necessary condition

$$
P_3^{\mathrm{ord}}\ge 9
$$

The resulting nine-pair requirement is used by the complete refinement arguments
below.

## Lemma 13. At most one split per triangle (computer-assisted)

A quartic triangle is equivalent to three disjoint aligned edges with common value
tau=2x-a. Translate every label by -tau. Its six labels become three doubling pairs,
and all eight physical positions are

$$
A=(u,2u,v,2v,w,2w,p,r).
$$

This normalization uses no division. Full validity and protected equal-degree
identities are invariant under translation.

Fix the triangle's ordinary cubic descent

$$
2u+2v = 2v+2u.
$$

The genuine-split normal form from the source-budget lemma gives

$$
2u+2v+d+e = 2v+2u+d+e = 2z+2u+b+2v,
$$

where z,b,d,e are exactly the remaining four labels w,2w,p,r, all distinct. Thus the
only remaining equation is

$$
d+e=2z+b.
$$

There are exactly 12 ordered choices of z,b; d,e are the unordered complement. This
covers every genuine split descending to this cubic pair, with no assumptions about
additional cubic relations. Once z,b are specified, all three quintic words and the
output are determined.

## Eliminate ten of the twelve choices

The following table is literal coverage of the split equation. The p/r alternatives
are displayed together; the checker reconstructs all 12 presentations from ordered
physical frames.

|z|b|Necessary equation|Exclusion or residual|
|---|---|---|---|
|w|2w|p+r=4w|The protected squarefree pair p+r equals the repeated pair 2(2w).|
|w|p or r|r=p or p=r|Physical labels collide.|
|2w|w|p+r=5w|The protected squarefree triple w+p+r equals 3(2w).|
|2w|p or r|r=p+3w or p=r+3w|A non-original mass-eight word is 3u+3v+2r, or 3u+3v+2p, respectively.|
|p or r|w|w+r=2p or w+p=2r|A protected squarefree pair equals a repeated pair.|
|p or r|2w|r=2p+w or p=2r+w|Positive quartic growth to 89 values, below.|
|p|r|3w=2p+r|Necessary residual.|
|r|p|3w=p+2r|Necessary residual.|

For the mass-eight rival row, the original sum is 3u+3v+3w+p+r. Substituting r=p+3w
changes its last three summands to 2r. The proposed rival has exactly eight terms; it
repeats u,v,r and differs from the original word. The swapped case is identical.

For the growth row, it suffices to exclude p=w+2r. This equation has the exact,
surjective parameterization

$$
A=(u,2u,v,2v,w,2w,w+2r,r)
$$

over any abelian group. The coefficient of p is one, so no odd torsion is discarded.
The saved certificate selects 89 repeated quartic words. For every pair Wi,Wj it
supplies a nonnegative mass-eight word R different from the original, an integer k,
and a positive power of two f, with the exact integer identity

$$
f\cdot (\operatorname{val}(R)-\sum A) = k\cdot (\operatorname{val}(W_i)-\operatorname{val}(W_j)).
$$

There are 89*88/2=3,916 such identities, checked directly in the four free
coordinates u,v,w,r. If Wi and Wj coincided in an odd group, the separation identity
would force value(R)=sum(A), since f is invertible. Full validity forbids this.
Therefore all 89 quartic values are distinct, contradicting T4<=88. Swapping p and r
excludes r=w+2p with the same certificate.

The only necessary residuals for this fixed cubic descent are therefore

$$
3w=2p+r,\quad\text{or}\quad 3w=p+2r.
$$

No bound obtained by the absence of witnesses or by a timeout is used.

## Six residual presentations, at most one compatible

Apply the ten-choice elimination to each of the triangle's three cubic descents. The
six necessary presentations are

$$
3x_i=2p+r\quad\text{or}\quad 3x_i=p+2r,    x_i \in  \{u,v,w\}.
$$

Each presentation determines its quintic fiber uniquely. All 15 pairs of distinct
presentations are incompatible:

1. **Different xi, same orientation.** The two equations give 3xi=3xj. This equates the distinct protected squarefree pairs xi+2xi and xj+2xj. There are six such pairs of presentations.
2. **Same xi, opposite orientation.** Subtraction gives p=r, a physical label collision. There are three such pairs.
3. **Different xi, opposite orientation.** Name them so 3xi=2p+r and 3xj=p+2r, and let xk be the other triangle center. The original sum is

$$
3x_k+3x_i+3x_j+p+r = 3x_k+4p+4r.
$$

   Take xk and 2xk once each, xi and 2xi twice each, and r twice. This non-original
eight-term word has value

$$
3x_k+6x_i+2r = 3x_k+4p+4r.
$$

   It is a forbidden mass-eight rival. There are six such pairs.

These identities use no cancellation by three. The checker verifies all 15 pairs in
the exact five-coordinate triangle family. Two distinct genuine split outputs
supported by the triangle would give two distinct presentations in the six-case
list, which is impossible. This proves the theorem.

## Global split compression

Let P=P3 ordinary. Let D be the set of ordinary cubic pairs that occur in at least
one actual quartic triangle, counted once even when reused. Every split has a unique
cubic descent.

- At most 4(P-|D|) splits descend outside D, by the four-splits-per-pair bound in Lemma 7.
- At most t splits descend inside D: assign each such split to any triangle containing its descent. No triangle can receive two splits by the theorem just proved, so this assignment is injective.

Consequently

$$
q \le  4(P-|D|)+t.
$$

A cubic pair fixes two disjoint directed aligned edges. Its third triangle edge lies
on the other four labels. Three such edges in a path forest would contain two
disjoint edges, producing a matching of size four with the fixed pair, forbidden by
the quintic cap. Hence each pair feeds at most two triangles, and 3t<=2|D|. Hence
also

$$
q \le  4P-5t.
$$

The set-level form is often stronger and is needed for the forest corollary. These
split bounds alone do not prove the full theorem.

## A counting bound that allows all pure refinements

For a hypothetical full-valid eight-set in odd N<248, retain the general count

$$
N \ge  288+h+R_3+2c+2w-2(t+q+P).
$$

Here P=P3 ordinary. The general assignment q<=h gives h-2q>=-q. All other displayed
correction terms are nonnegative. Thus

$$
N \ge  288-q-2t-2P.
$$

This inequality does not fix the pure cubic partition or forbid new pure collisions.
It uses no assumption that formally different outputs remain different.

## All nine ordinary-collision-exhausted forest families are excluded

Choose an actual triangle-bearing alignment class. By Lemma 11, its graph is a path
forest on eight physical labels, with maximum matching exactly three. Let P0 be its
number of disjoint edge pairs, t0 its number of three-edge matchings, and D0 the set
of its edge pairs occurring in at least one such matching.

Every disjoint edge pair gives an ordinary cubic collision pair with the class's
alignment value. That value is uniquely recoverable from the pair. Distinct classes
therefore have disjoint cubic-pair inventories. Different matchings produce
different quartic triangle outputs under the ordinary cap; otherwise the union of
their representations would contain more than three ordinary words, and the
three-word fiber recovers its matching uniquely.

Suppose every ordinary cubic pair in the set belongs to the chosen class. Then P=P0.
Another triangle-bearing class would contribute ordinary cubic pairs of its own
alignment value, so no such class exists; t=t0 and |D|=|D0|. The global
split-compression formula gives

$$
q \le  Q_0 := 4(P_0-|D_0|)+t_0.
$$

Combining with the preceding N bound proves N>=B0:=288-Q0-2t0-2P0.

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

The nine shapes are exhaustive. Their counts are obtained by selecting disjoint edge
pairs and triples in literal paths; the checker independently reconstructs this
table from all integer partitions of eight. In particular, D0 is not assumed equal
to P0. For example, the six-vertex path has six disjoint edge pairs but only three
of them occur in its unique matching of size three.

Every B0 is at least 248. Thus the whole family in which ordinary collisions are
exhausted by one triangle class is excluded. Equivalently, every chosen
triangle-bearing class of a remaining counterexample must have at least one ordinary
cubic pair outside it. Pure-only refinements cannot evade this conclusion.

## Lemma 14. Six large forests are impossible (computer-assisted)

The cycle lemma excludes every directed alignment cycle of length at least three in
the hypothetical small-order setting. A two-cycle cannot belong to a
triangle-bearing class. Four disjoint aligned edges violate the ordinary quintic
multiplicity cap. Hence a triangle-bearing class is one of the nine path-forest
shapes listed in Lemma 11.

The triangle-split lemma proves that every such class needs an ordinary cubic
collision outside the class. Equivalently, in a normalization of one of these
forests, a counterexample must add an ordinary cubic equality not forced by its free
path-root coordinates. Pure-only refinements cannot evade this requirement.

Every ordinary cubic collision pair can be taken in private form

$$
2x+b=2y+a,
$$

with x,y,a,b all distinct. The centers cannot coincide, equal tails force equal
centers by invertibility of two, and a cross center/tail overlap gives a forbidden
protected squarefree pair. Thus the fixed four-distinct-label coverage below is
complete for the required new ordinary equalities.

## Exclude the entire (5,3) family by positive quartic separation

After translating the alignment value to zero, this family is

$$
A=(u,2u,4u,8u,16u,v,2v,4v).
$$

An existing discovery certificate selects 89 repeated quartic words in this exact
two-root family. Every pair has a positive integer identity

$$
f\cdot (\operatorname{val}(R)-\sum A)=k\cdot (\operatorname{val}(W_i)-\operatorname{val}(W_j)),
$$

where R is a non-original nonnegative mass-eight word and f is a positive power of
two. All 3,916 identities have now been checked directly in the two free coordinates
u,v. A coincidence of two selected words would give a mass-eight rival, since f is
invertible in an odd group. Therefore T4>=89, contradicting the small-order quartic
budget.

This excludes all refinements of the family, not just its free-root or
no-extra-collision branch.

## A hand root-order lemma for the (7,1) family

Write

$$
A=(u,2u,4u,8u,16u,32u,64u,p),    \sum A=127u+p.
$$

Let d=ord(u). Under full validity and odd N<248, d>=159.

The following elementary coin observation is useful. A positive integer expressed as
at most seven coins from {1,2,4,8,16,32,64}, with total value at least seven, can be
expressed in exactly seven coins: split a coin of value at least two into two halves
until seven coins are present. Before reaching seven, not all coins can be ones,
because their total value would then be less than seven.

- For odd d<=119, the integer 127-d is between 8 and 126. Its binary expansion uses at most six permitted coins, so it has a seven-coin representation. Modulo d this represents the same block sum as 127, and differs from the original seven distinct powers. Appending p gives a forbidden mass-eight word.
- For d=121,123,125, seven-coin totals 127+d are respectively

$$
\begin{gathered}
3\cdot 64+32+16+2\cdot 4=248, \\
3\cdot 64+32+16+8+2=250, \\
3\cdot 64+32+16+8+4=252.
\end{gathered}
$$

  Again these are explicit seven-term block rivals.
- For odd 129<=d<=157, write 127+d=256+2m, where 0<=m<=14. Four 64-coins plus the binary expansion of 2m use at most seven coins, since m has at most three binary ones. Splitting yields a seven-term rival.
- The remaining d=127 is excluded by saturation. Every residue has a seven-coin word: zero uses the original block, residues 7..126 use binary expansion and splitting, and residues 1..6 use their representative r+127, whose minimum coin count is at most four. Thus 7B=H=<u>, and 8B=H as well. Since 127 divides N<248, the ambient group equals H. An eight-term word using only the block represents 127u+p, omitting p, and is forbidden.

This covers every odd d<159 without enumerating ambient moduli or parameter
assignments. It uses the order of a single structural block and explicit range
arguments.

## Complete external-relation closure for (7,1)

The required new private cubic pair gives

$$
\alpha\cdot u+\beta\cdot p=0.
$$

If neither word involves p, then beta=0 and the nonzero coefficient alpha has
absolute value at most 156: an ordinary cubic word on the seven powers has integer
value between 4 and 160. This contradicts d>=159.

Otherwise p occurs once in one of the four private positions, so its coefficient has
absolute value one or two. Cancel only common powers of two and orient the sign so
beta>0. Every remaining relation is parameterized surjectively in an odd group by

$$
u=\beta\cdot t, p=-\alpha\cdot t,    \beta \in  \{1,2\}.
$$

No odd factor is removed. The complete coverage contains 830 literal private cubic
pairs and 261 normalized coefficient types. Of these,64 are the root-order cases
above. The remaining 197 types are excluded by 176 direct
protected/label/multiplicity contradictions, six explicit mass-eight rivals, and
fifteen positive quartic growth certificates reaching 89 values. Every possibility
is closed outright, so the whole (7,1) family is excluded.

## Complete closure of the four three-root forests

Use the exact triangle frame A=(u,2u,v,2v,w,2w,p,r). The following two equations
impose each primary forest, with one independent root per path component:

|Shape|Primary relations|Literal first private cases|Normalized first directions|
|---|---|---:|---:|
|(3,3,2)|p=4u, r=4v|832|701|
|(5,2,1)|v=4u, p=16u|833|701|
|(4,3,1)|v=4u, r=4w|833|701|
|(6,1,1)|v=4u, w=16u|834|701|

The triangle-split lemma forces a new ordinary equality in every hypothetical
counterexample. The coverage takes all pairs of private ordinary cubic words that
are not equal in the primary free-root model, keeps their exact integer equations,
and cancels only powers of two. Integer unimodular reductions retain every odd
diagonal factor as torsion.

All first cases for (3,3,2), (4,3,1) and (6,1,1) are excluded outright by direct
identities, inherited cycle/source/multiplicity theorems with their premises
checked, explicit mass-eight rivals, or positive 89 quartic separation certificates.

For (5,2,1), exactly three first relation modules remain after those positive
exclusions:

$$
\begin{gathered}
5w=2p+r, \\
u+2r=5w, \\
u+2p=w+2r,
\end{gathered}
$$

always with v=4u and p=16u. Each formal ordinary cubic partition has P=8. Lemma 12 already proves $P\ge9$ in any counterexample. Thus every
realization of one of these modules must add another ordinary equality, even
allowing arbitrary pure refinements. The triangle-split lemma set-level count also
gives the stronger no-new-ordinary lower bound 259 in each case.

For each of the three modules, complete next-private-pair coverage has 832 literal
cases and 700 normalized directions. All are excluded outright. No third relation
branch is needed, and no weak bound from a first residual is treated as an
exclusion. This closes the entire (5,2,1) family as well.

## Uniform alignment cap and remaining triangle types

The six excluded shapes are precisely the triangle-bearing path forests with at
least five edges. Only the three small shapes at the start remain, and they have
three or four edges and one or two triangle matchings.

In fact the four-edge cap holds for every alignment class, whether or not it
initially contains a triangle. A cycle-free class with at least five edges has at
most three path components on eight vertices, hence at least three disjoint edges.
It would be a triangle-bearing forest of an excluded shape (or would have four
disjoint edges, already forbidden).

Cycles of length at least three are excluded by the cycle-saturation argument above.
If a class contains a two-cycle, it cannot have a matching of size three. There can
be at most one two-cycle in a cyclic group: after translating the common alignment
to zero, its two vertices are exactly the two nonzero points of the unique subgroup
of order three. The remaining path forest must have matching number at most one, and
therefore has at most two edges. Together with the two-cycle, the class has at most
four edges.

Thus every alignment class has at most four edges. Those carrying triangles are
exactly the three remaining forest shapes and have at most two triangles. This
limits triangle reuse uniformly across all alignment values; the global allocation
is supplied in the subsequent argument.

## Lemma 15. Only one triangle alignment class (computer-assisted)

Normalize one triangle to A=(u,2u,v,2v,w,2w,p,r). A second triangle consists of
three disjoint directed edges on these same eight physical labels, with a common
alignment gamma. There are 3,360 literal presentations: choose three centers, three
tails among the remaining five labels, and a bijection. For edges (xi,ai), impose
the two equations 2Axi-Aai=2Ax0-Aa0. No odd integer is divided out.

Exactly one presentation has gamma=0 formally. Another 603 force gamma=0 through
their integer relation modules. These are rejected only under the selected
hypothesis that the second class is DIFFERENT; they are not full-model exclusions.
The remaining 2,756 presentations use unconditional model exclusions or a complete
residual proof.

The initial residual modules give 14 types under permutation of the three primary
doubling pairs and of p,r. By explicit relabeling and translation using an actual
triangle, they reduce to nine affine families. Each has six formal ordinary cubic
collision pairs. A counterexample needs at least nine by Lemma 12, so every family
must acquire a new private ordinary collision.

The alternating seven-vertex-path family is represented by

$$
u+4v=5w,    20v+r=21w.
$$

Its complete first refinement leaves one system with eight ordinary pairs, so
another ordinary equality is compulsory. All next cases close positively. This
excludes the entire alternating family, allowing all additional relations and
retaining all odd torsion.

For the other eight affine families, complete first-private-pair coverage leaves
precisely two unresolved modules. They have seven and eight ordinary pairs,
respectively. Another ordinary equality is compulsory in both, and all of those next
cases close positively. No further branch is needed. Weak quartic-growth bounds in
the first residuals are never used as exclusions.

All accepted closures are direct protected/label/multiplicity contradictions,
explicit mass-eight rivals, checked alignment-cycle/source premises, applications of
the large-forest lemma's four-edge bound, an explicit affine map to the already
excluded alternating family, or positive separation of 89 repeated quartic words.
Every affine map is a permutation of all eight physical positions followed by
translation; it preserves full validity and cancels no odd factor.

## A shared triangle descent supports no split (elementary)

**Dependencies:** Lemma 13 and the cycle exclusion in Lemma 11. An ordinary cubic
pair fixes two directed aligned edges: its centers and cross tails are physical
labels. The twelve-choice proof of Lemma 13 shows that the two labels added to form
a genuine split must be exactly the labels of the third edge of any triangle
containing that descent. If two distinct triangles contained the descent, their
third edges would have to use the same two labels. They cannot be distinct with the
same direction, and opposite directions form a forbidden two-cycle. Thus no such
split exists. This is the sole split-guard leaf in the final archive.

## Persistent credits used by the final archive (elementary)

**Dependencies:** Lemmas 5–9, 14–15. Let R0 be the formal total cubic excess, c0 the
number of formal ordinary cubic triples, and w0 the number of formal ordinary
quartic split outputs. Further equalities may be ordinary or pure. Merging cubic
fibers cannot decrease R3. A three-ordinary fiber cannot acquire a fourth ordinary
word or merge with a different ordinary fiber, by Lemma 5. Hence R3>=R0, c>=c0, and
w>=w0. Lemmas 14–15 give t<=2. The weighted count and assignment imply the necessary
counterexample bound

$$5t\ge2+2(o+R_3+c)+5w+(E-2q).$$

It follows that a model is excluded outright if

$$2+2(R_0+c_0)+5w_0>10.$$

The five global-credit leaves all have R0=c0=w0=1, giving 11>10. This conclusion
allows all refinements. It does not presume that formally different generic values
remain distinct.

All 31 refinement nodes in the final archive instead use only P<=8 and Lemma 12,
which force an additional ordinary cubic equality. Every required new private pair
is branched over; no condition excluding pure refinements is imposed. The checker
rejects conditional quintic-credit rules, which are not used by this archive. Their
obsolete exposition remains in the [preserved research
archive](../docs/provenance.md).

## Lemma 16. Excluding the two-triangle class (computer-assisted)

Assume a full-valid eight-point set in an odd cyclic group of order N<248. The
general assignment lemma forces a quartic triangle. The large-forest lemma gives
four aligned edges at most, and the interaction lemma permits only one
triangle-bearing alignment class. Lemma 12 requires at least nine ordinary cubic
collision pairs.

**Theorem.** The remaining two-triangle class (3,2,2,1) is impossible. Every
hypothetical counterexample therefore has exactly one quartic triangle, in
(2,2,2,1,1) or (4,2,1,1). The two one-triangle forests are handled by the closing
argument.

Translate the common alignment to zero and use the exact family

$$
A=(u,2u,v,2v,w,2w,p=4u,r).
$$

It has five formal ordinary cubic pairs. Therefore another actual ordinary cubic
pair must collide, regardless of any pure refinements. An ordinary cubic word
consists of two copies of one center and one other label. Protection makes the two
words of a collision use four different physical labels. There are 56 such words.
All private pairs not already forced are covered, and only common powers of two and
signs are normalized in their equations. Every odd integer factor is retained
through exact integer unimodular diagonalization.

The resulting finite proof graph has 31 nodes requiring further ordinary equalities.
At each such node the formal ordinary pair count is at most eight, so Lemma 12 again
forces a new pair. This count strictly increases along every refinement; pure
collisions are never forbidden or assumed absent. Every leaf closes by a literal
protected/label/cap contradiction, a non-original mass-eight word, a positive
quartic-growth certificate showing 89 distinct repeated values, the checked triangle
interaction, or one of the unconditional credit/split restrictions immediately
above. Only explicit identities from incomplete research trees are reused; the
complete checker reconstructs each required identity and case.

The separate checker imports standard-library helpers from the large-forest lemma
checker and no producer or search routine. It independently reconstructs all
private-pair coverage, every integer reduction and every physical pair permutation.
Each positive quartic pair is supported by an exact identity
f*(value(R)-sum(A))=k*(value(Wi)-value(Wj)), where R is a different nonnegative
mass-eight word and f is a positive power of two. A collision of Wi and Wj would
force the forbidden rival because N is odd.

The completed check passed 13,333 nodes, 21,761 private direction cases, 25,851
literal private pairs and 7,945,564 positive mass-eight identities. The archive
content hash is recorded in the release manifest.

This certificate closes the two-triangle component. The closing chapter handles both
remaining one-triangle forests.
