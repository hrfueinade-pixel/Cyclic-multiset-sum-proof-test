# Stage 8: the complete quartic bridge when h=R3=0

Follow-up: stage9_cubic_torsion_findings.md proves that odd h=0
instances have no order-three difference, at most four cubic marks
per fiber, and at most one pure cubic per fiber. The remaining
R3>0 branch and full goal are still open; this regular-branch proof
is unchanged.

## Result and scope

**Theorem.** Let A be a valid eight-element set, with no antipodal pair,
in a cyclic group. Let H be its difference-generated subgroup. If H
has odd order and h=R3=0, every repeated quartic fiber is connected by
cubic propagation. Equivalently, D=0.

This settles ALL quartic collision types in the regular odd branch,
not only ordinary/ordinary collisions. The proof below does not use a
modulus search or the paper's n<=7 computational certification.

The full goal h=0 => D=0 is STILL OPEN: the odd R3>0 branch remains.
The even branch was proved in stage6_h0_findings.md. Combining that
result with this theorem proves h=R3=0 => D=0 without a parity restriction.
This does NOT prove the 248 bound. At h=R3=0 it still needs Sigma>=53.
There is no assertion of literature novelty.

## 1. Foundations and exact dependencies

Write Delta for the 56 ordered nonzero differences. Define

    h = |{d in Delta: 2d not in Delta}|/2,
    R3 = sum_y binomial(m_y-1,2),

where m_y counts the distinct multisets 2a+b with value y. Quartic types
are 4,31,22,211. Type 211, or "ordinary", has three distinct points.

The quartic propagation graph has the 260 distinct repeated quartic
multisets as vertices. An edge cones an equality of two repeated cubics
by one common point. K is its number of components, and

    D=K-|T4|.

All arguments take place in H, after a translation. Multiplication by
2, and hence by every power of 2, is invertible in H. Fractions with
power-of-two denominators below denote this group automorphism; NO
division by 3,5,7,13,19,29 is used.

Validity implies that no squarefree sum of degree <=8 has a different
equal-length multiset representation: pad any such replacement by its
complement in A. In particular all pair sums are unique, and all ordered
nonzero differences are unique in the absence of antipodes.

The following previously proved lemmas are used, with their complete
proofs in the indicated reports:

* stage5_h0_findings.md, Proposition 2: under odd h=R3=0 the unpaired
  cubic marks are precisely 2a+f(a), where f is a fixed-point-free
  permutation of A. Thus there is one unpaired mark per center AND per
  singleton label; every pure cubic 3a is paired.
* stage4_lemma_findings.md, Proposition 1: two equal repeated quartics
  sharing a point are directly joined by propagation. Entire support
  unions of different components at a value are disjoint. Deleting the
  shared point leaves repeated cubics: a squarefree deletion would be
  a forbidden replacement.
* stage7_h0_findings.md, Section 3: under odd h=R3=0, two type-31
  quartics cannot lie in different components at one value. This uses
  full support separation, the order-five lemma, and the unique
  unpaired singleton label; it is NOT an injection of representations.

For clarity, the consequences of the first lemma used below follow
directly. A quartic has at most two deletions leaving a repeated cubic,
each of which has at most one partner. Different deletions cannot give
the same neighbor, since canceling their common points would violate
pair-sum uniqueness. Thus every component is a path, cycle, or isolated
vertex. Every ordinary vertex has positive degree: its two relevant
marks have the same center, and at most one can be unpaired. Every pure
quartic has degree one, because its pure cubic is paired.

An ordinary center is absent from every other distinct representation
in its fiber. Otherwise deleting that center equates its squarefree
triple to a different triple. Consequently ordinary centers are all
distinct, and none is in any other ordinary vertex's tail.

We also use the self-contained bound |H|>=184. Translate 0 into A.
The 128 subset sums S of A\{0} are distinct, and s-S=S. For
T3={2a+b}, validity gives T3 intersect S=A: after deleting zeros,
any repeated cubic representation of a subset of size at least two
is forbidden by padding the replacement at zero. Subsets of size zero
or one give exactly A. Thus E3=T3\A has size 28 when h=R3=0, since the
64 marks have 28 paired fibers and eight singleton fibers. The sets
S,E3,s-E3 are disjoint. In particular E3 intersect (s-E3) is empty:
two cubic representations summing to s, padded by two zeros, would be
a rival eight-term multiset. Hence |H|>=128+2*28=184.

## 2. Local restrictions, including a useful pure-quartic lemma

Here the local statements need only validity, odd H, and the stated
doubled-difference conditions.

**Lemma 2.1 (disjoint 31/31).** If 3a+b=3c+d with disjoint support
pairs and 2(a-c) in Delta, then a-c has order five.

Proof. Write 2(a-c)=e-f. Subtracting from the quartic equality gives
a+b+e=c+d+f. These different triples must both repeat, so e is a or b
and f is c or d. The first three choices force a=c, 2c=a+d, or
2a=b+c. The last gives 2(a-c)=b-d=-3(a-c), hence order five. QED.

The center pair and singleton pair then exhaust the four nonzero
differences of the order-five subgroup J, in two DIFFERENT J-cosets.
Thus no other A-pair can have a nonzero difference in J.

**Lemma 2.2 (disjoint 22/31).** A disjoint equality 2a+2b=3c+d is
impossible if both 2(a-c),2(b-c) belong to Delta.

Proof. Write 2(a-c)=u-v. Then 2b+u=c+d+v, so v is c or d. The first
choice makes 2a=c+u a forbidden pair equality. Thus v=d and
u=2a-2c+d. Similarly w=2b-2c+d is in A. The quartic equality gives
u+w+c=3d. Its left side is squarefree: u=w, u=c, or w=c would give
respectively 2a=2b, 2b=2d, or 2a=2d. Contradiction. QED.

At odd order, different equal quartics of types 4/4,4/22,22/22 are
impossible simply by doubling injectivity and pair-sum uniqueness.

**Lemma 2.3 (4/31 closure).** If 4z=3a+b and z,a,b are distinct,
and 2(z-a) is in Delta, then 6z-5a is a point of A.

Proof. Write 2(z-a)=e-f. The equality becomes

    2z+e=a+b+f.

Its right side must repeat, so f=a or b. If f=a, comparison of the
two equations gives 2e=a+b, forbidden. Therefore f=b and
e=2z-2a+b=6z-5a. QED.

**Lemma 2.4 (shared-singleton obstruction).** Under odd h=0, a pure
quartic 4z cannot equal both 3a+b and 3c+b when a,c,b,z are distinct.

Proof. Here a-c has order three. Lemma 2.3 produces points
e=6z-5a and f=6z-5c. Then e-f=-5(a-c)=a-c. Difference uniqueness
forces e=a and f=c. Thus 3(z-a)=0. The three distinct points z,a,c
are in one coset of the order-three subgroup, which violates pair-sum
uniqueness. QED.

**Lemma 2.5 (six-point bridge precursor).** A disjoint ordinary equality

    2a+b+c=2d+e+f

with 2(a-d) in Delta forces its unique representation as v-u, where
v is a tail on the left and u is a tail on the right.

Proof. The cubic equality 2a+u=2d+v, subtracted from the quartic
equality, gives b+c+v=e+f+u. If v were outside {b,c}, the left triple
would be squarefree and the multisets could not be identical, because
a single u cannot supply both b and c. Thus v is a left tail, and
symmetrically u is a right tail. Writing the other tails b',e' gives
2(v-u)=e'-b'. These are six distinct points in difference pairs
a-d,v-u,e'-b' of sizes delta,2delta,4delta. QED.

**Lemma 2.6 (overlapping 31s at a pure value).** Under odd h=0, two
distinct 31s at value 4z, with z outside their supports, cannot have
overlapping supports.

Proof. A shared center would make the vertices identical. A shared
singleton is excluded by Lemma 2.4. The remaining possibility is a
chain, written 4z=3a+b=3b+c with four distinct points z,a,b,c.
Lemma 2.3 gives E=6z-5a in A. The two quartic equalities imply

    E+b+c=2z+a.

Thus E must be b or c, since otherwise the left triple is squarefree.
If E=b, subtracting 4z=3a+b from 6z=5a+b gives z=a. If E=c,
then c=3a-2b and 6z=8a-2b, hence 3z=4a-b and z=2b-a.
Consequently c+z=2a, a forbidden squarefree-pair replacement. QED.

## 3. Ordinary/ordinary collisions cannot be fresh

**Proposition 3.1.** Under odd h=R3=0, a quartic fiber cannot have
ordinary representations in two different propagation components.

Suppose otherwise, with components U,V. Each has support size at least
three. A three-point ordinary component has EXACTLY two vertices,

    4z, 2p+z+q, with 3z=2p+q and f(p)=z.

Indeed its other vertices exclude p. On the other two points, a 31
would force equality of doubled centers and a 22 would equate a double
to a squarefree pair. Only a pure quartic is possible; it is unique.
The ordinary mark 2p+z is unpaired since 2p+q=3z is paired.

If neither component has three points, both have exactly four. There
is at most one ordinary vertex in each: two ordinary centers would
leave only two possible tail points and hence identical tails, which
is impossible. Each component therefore has a nonordinary vertex.
If one contains a 22, every nonordinary type in the other is forbidden
by Lemma 2.2 or doubling injectivity. Otherwise their nonordinary
types are 4 and 31. Both cannot contain 4, and both cannot contain 31
(the stage7 theorem). The only remaining allocation has one component
with pure quartics but no 31 or 22. Such a connected component has
just a pure and an ordinary vertex, using three points, not four.
Thus one component is the three-point U displayed above.

The other component V has at most five points. It contains no pure
quartic and no 22, since its value is 4z. Its vertices are ordinary or
31. There are at most two ordinary centers: with three centers and at
most five points all ordinary tails would be the same two-point pair.

### 3.1 Two ordinary vertices in V: sixteen complete algebra cases

Their tails must be distinct edges on at most three other points, so
they can be written {u,v},{v,w}. A component with only these two
vertices would have f(r)=v=f(s), impossible. Any additional 31 uses
the three tail points and meets both ordinary vertices. There is at
most one such vertex by degree <=2. It cannot contain v: otherwise
all three vertices contain v, giving three cubic representations after
deletion and contradicting R3=0. Up to relabeling it is 3u+w. Thus

    4z=2r+u+v=2s+v+w=3u+w.

Translate u=0 and put B=z, Q=v/2, P=p. The EIGHT DISTINCT points are

    b=B, p=P, c=3B-2P, u=0, v=2Q, w=4B,
    r=2B-Q, s=-Q.

Here b denotes the former pure point z, and c the former point q.
Lemma 2.5 for centers p,r gives one of

    R1: 2P=5B-2Q,   R2: 2P=5B-4Q,
    R3: 4P=7B-2Q,   R4: 4P=7B-4Q.

For centers p,s it gives one of

    S1: 2P=B-4Q,    S2: 2P=-3B-2Q,
    S3: 4P=3B-4Q,   S4: 4P=-B-2Q.

Every combination gives the following contradiction. Juxtaposition
in this table means addition of points, NOT multiplication.

| | S1 | S2 | S3 | S4 |
|---|---|---|---|---|
|R1|r=w|b=u|2w=u+b|p+w=b+u|
|R2|b=u|2b=r+w|p+b=2u|r+p+b=3u|
|R3|b+w=p+r|p+u=b+w|r=w|b=u|
|R4|p+b=u+w|r+w=p+b|b=u|2b=r+w|

Each identity follows by adding the corresponding equations and
dividing only by powers of two. For example R2,S4 imply
6Q=11B, and then 2(r+p+b)=11B-6Q=0. R4,S2 imply 13B=0 and
2(r+w-p-b)=13B. R1,S3 imply 7B=0 and hence 2w=u+b.
Duplicate points, different pair multisets, or the squarefree triple
r+p+b=3u all contradict validity. Exact row-combination certificates
for ALL sixteen entries are provided by the independent checker.

### 3.2 One ordinary vertex in V: disjoint 31 endpoints

Its center is absent from all other vertices. The latter are 31s on
at most four other support points. Lemma 2.6 says their support pairs
are pairwise disjoint, so there are at most two. There is at least one,
because an ordinary vertex is not isolated. Each 31 is an endpoint
joined only to the ordinary vertex.

One 31 alone is impossible. Its endpoint edge must delete its
singleton, since its pure cubic is paired. The ordinary endpoint
would then have the same unpaired singleton label as that 31 center,
violating injectivity of f.

With two 31s their endpoint edges to the ordinary vertex must delete
their singletons, so this shape is

    4z=2a+b+c=3d+b=3e+c.

Lemma 2.1 gives delta=d-e of order five. Translate e=0. Then

    d=delta, c=4z, b=4z+2delta, a=-2z-delta.

Lemma 2.3 forces the point 6z into A. It is none of z,a,b,c,d,e:
6z=c or b would give z=e or d; 6z=e would give c=z. If 6z=z or a,
then z lies in the order-five coset of d,e, violating its exhausted
difference budget. If 6z=d, then 3z belongs to that subgroup and
a-z=-3z-delta creates another forbidden order-five difference.
Consequently 6z must be p or q in U.

If p=6z then q=-9z. Lemma 2.5 for centers p,a, and tails {z,q},{b,c},
gives one of

    19z+4delta=0, 19z+2delta=0,
    29z+4delta=0, 29z+2delta=0.

Because 2 and 4 are invertible, delta belongs to <z>. Every A-point
now belongs to <z>, whose order divides 95 or 145 since 5delta=0.
This contradicts the elementary bound |H|>=184.

If q=6z then p=-3z/2. The same four tail choices give respectively

    z=-delta, 2z=-delta, z=4delta, z=2delta.

All put z into the already exhausted order-five coset, contradiction.
All possibilities for V have now been excluded, proving Proposition
3.1. No incomplete configuration search is hidden in this proof. QED.

## 4. Closing every remaining quartic collision type

Two elementary component observations finish the regular branch.

**Lemma 4.1 (all-ordinary components).** An all-ordinary component
has at least six support points. If it has at most six, it is a triangle
of three centers r,s,t and three tail points u,v,w, with value

    x=2r+u+v=2s+v+w=2t+w+u.

Proof. No ordinary vertex is isolated. Two ordinary vertices alone
would have the same unpaired singleton label at their two endpoints,
contradicting f. With k>=3 ordinary vertices, their k distinct centers
are absent from every tail. Their tail pairs are distinct, so at least
three additional points are needed; k>=4 needs at least four tail
points. Therefore support <=6 forces exactly three centers and three
tail points, with all three tail edges forming a triangle. QED.

In this triangle, summing the three equalities gives

    2(r+s+t+u+v+w)=3x.

It cannot share its value with an external pure 4z or external 22,
2a+2b: these would give respectively the squarefree replacements

    r+s+t+u+v+w=6z,
    r+s+t+u+v+w=3a+3b.

Both have degree six and violate validity.

**Lemma 4.2 (31-only components versus a pure quartic).** A component
containing only type-31 vertices cannot have value 4z with z outside
its support, under odd h=R3=0.

Proof. By Lemma 2.6 no two vertices of this component could share a
point, so there could be no edge. But a 31 cannot be isolated, since
its pure cubic is paired. QED.

**Proof of the theorem.** Suppose a quartic fiber has two components.

If it contains a pure quartic, let U be that component. If U contains
an ordinary vertex, Proposition 3.1 excludes ordinary vertices in any
other component. Odd doubling excludes types 4 and 22 there, leaving
a 31-only component, contrary to Lemma 4.2. If U has no ordinary
vertex, its pure cubic partner must itself be pure: a nonpure cubic
partner would cone to an ordinary quartic. Thus U contains a 31 as
well and has support at least two. Another component has no 31 by
the stage7 theorem, nor 4 or 22, so is all-ordinary. Its support is
at most six, hence Lemma 4.1 gives the forbidden pure/triangle sum.
This excludes every fresh fiber containing a pure quartic.

If it contains a 22, every other component is all-ordinary by
Lemma 2.2 and odd doubling. The 22 component has at least two support
points, so the other has at most six and Lemma 4.1 gives the forbidden
22/triangle sum. Thus no fresh fiber contains a 22.

If it contains a 31, every other component is all-ordinary: fresh
31/31 is excluded by stage7, and pure and 22 cases have just been
excluded. Its own component cannot contain an ordinary vertex by
Proposition 3.1; it is therefore 31-only. Such a component has at
least three support points. Indeed one 31 cannot be isolated since
its pure cubic is paired, and two different 31s cannot live on just
two points. The other component needs at least six points by
Lemma 4.1, exceeding the eight available.

All remaining possible fresh fibers would have two ordinary
components, already excluded by Proposition 3.1. Hence every fiber
is connected and D=0. QED.

## 5. Verification, limitations, and the next obstruction

### A concrete control: dropping doubling closure fails

Let R=33, Q=8*R^4+1=9487369 and work in Z/3 x Z/Q. Take the low
points a=(0,0), c=(1,0), z=(0,1), b=(0,4), together with the four
high points (0,R^j), j=1,2,3,4. This group is cyclic because Q=1 mod 3.
The corresponding eight residues modulo 3Q=28462107 are

    (0,9487369,18974739,18974742,33,1089,35937,1185921).

This set is valid. Every eight-term second-coordinate sum is at most
8*R^4<Q, so there is no modular wrap. The low digit is at most 32<R,
and each high-digit coefficient is at most eight, so there is no carry.
The target forces each high point once. Four low slots remain, with
4*#b+#z=5; hence #b=#z=1. The remaining two slots are a,c, and the
first coordinate forces #c=1, hence #a=1.

Nevertheless its low quartic fiber has

    4z=3a+b=3c+b.

The pure quartic is isolated, while the two 31s are connected through
3a=3c. The required doubled differences 2(z-a),2(z-c) are missing
from Delta, so this does not contradict Lemmas 2.4 or 2.6. Only one
cubic pair exists in the whole set, giving h=27,R3=0; the checker
finds D=1. This is an explicit obstruction to dropping global closure,
not a counterexample to the goal or to the 248 bound.

### Reproducible bounds and remaining work

Reproduce with standard-library Python 3:

    python stage8_regular_bridge_checks.py

The checker has no project imports. It verifies sixteen exact
row-combination certificates and three pure-chain identities, including
that every denominator is a power of two. It independently checks 4164 support masks across
three-, four-, and five-point supports, leaving four shape categories.
Lemma 2.6 excludes all three categories with overlapping 31 supports
at a pure value; Section 3.2 excludes the disjoint-31 category. These
are abstract incidence
patterns, NOT valid cyclic sets or affine equivalence classes.

Seven fixed valid fixtures each undergo all 6435 degree-eight multiset
checks, plus reconstruction of the literal cubic propagation graph.
Exactly one satisfies the regular odd hypotheses (the binary family
at 255), and has D=0. Other controls have (h,R3,D) respectively
(1,0,1), (0,0,0) at even 254, (28,0,3), (25,1,3), (26,0,2),
and (27,0,1) for the new CRT control.
They expose the omitted hypotheses rather than prove the theorem.
There are seven candidates and seven valid fixtures: six reused, plus
one newly constructed non-h0 CRT control with a pure/31 obstruction.
It adds no h=0 example or nonbinary regular-odd structural diversity.
There is no set search in this stage. Results are recorded in
stage8_regular_bridge_results.json. The proof is algebraic, not an
inference from these controls or from an incomplete modulus search.

The useful missing lemma is now sharply different:

    In an odd h=0 valid eight-element set, every cubic fiber has
    at most two representations (equivalently R3=0).

This is a proposed sufficient lemma, NOT proved or assumed. A
counterexample to it would not refute h=0=>D=0; it would require a
multiway replacement for the singleton-permutation argument instead.
The current proof depends essentially on that permutation and graph
degree <=2. Both disappear at R3>0, so simply repeating its case
analysis would be invalid.

An audit correction matters: the endpoint condition alone does NOT
force two adjacent 31s in a three-vertex path to share a singleton.
The mixed chain 3a+b=3b+c was an additional possible orientation.
Lemma 2.6, including its explicit squarefree replacement, is what
excludes that orientation. No assertion that repeated representations
cannot coincide has been used.

For the original 248 target, the regular branch still needs the
independent shadow-credit inequality Sigma>=53. Since D=0 here and
Sigma is the number C of quartic cycle components, the remaining
regular counting target is C>=53; the diagnostic theorem alone does
not establish it.

No external computational result is needed for this theorem. The
paper's reported n=7 minimum 124 remains an external dependency only
of the separate antipodal reduction. Literature novelty was not
established, and is not claimed here.

The active full goal remains unproved. This workspace has no Git
repository or configured remote (git status reports "not a git
repository"), so a PR cannot be created from these files.

## Appendix: reconstructed proofs of the regular dependencies

These proofs are included so the odd-branch theorem can be read without
assuming the earlier reports are correct.

### A. The singleton permutation and pairing of every pure cubic

In odd h=0, doubling permutes Delta. For every unordered pair of
different centers there is exactly one cubic collision: its doubled
center difference has a unique representation as a singleton-label
difference. Distinct centers cannot collide twice, by difference
uniqueness. R3=0 means that every cubic fiber has size at most two.
For a fixed center its seven collisions therefore use seven different
marks, leaving one unpaired label f(a).

Doubling also gives a bijection from the 28 unordered center pairs to
the 28 unordered singleton pairs. Each label belongs to seven pairs,
so precisely seven marks with that singleton are paired, and one is
unpaired. Hence f is a permutation.

Fix a singleton label a. For each r!=a, orient its unique singleton
pair collision as 2d+a=2e+r, with edge d->e labeled r. Each center
except g=f^(-1)(a) has outdegree one; g has outdegree zero. No edge
enters a, since that would imply 2d=a+r. A directed cycle would give,
on summing, k*a equal to the sum of its k distinct labels, all
different from a. This is a forbidden squarefree replacement.
Thus every walk ends at the unique sink g and the graph is a tree.
Since a has indegree zero, it cannot equal g (it would be isolated).
Therefore f(a)!=a for every a, and 3a is always paired. This proves
the regular dependencies used in Section 1.

### B. No fresh 31/31 collision in the regular branch

Suppose 3a+b and 3c+d lie in different components U,V. Lemma 2.1
puts {a,c} and {b,d} in the two order-five cosets described there.
Pair 3a with a different cubic 2p+q and cone by b. Neither p nor q
is a, by cubic uniqueness, or c,d, by full support separation.
If p=b, the new 31 center b against the opposite center c violates
the order-five coset budget. If q=b, Lemma 2.2 excludes the new 22.
If p=q, Lemma 2.1 forces p into c's coset, whose only A-points are
a,c. Hence p,q are two distinct new points. The mirrored partner
3c=2r+s uses the two other new points. Thus U,V have supports
{a,b,p,q} and {c,d,r,s}, exhausting A.

The ordinary center p cannot occur in any other vertex in U. If 2a+b
were paired, coning its partner by a would give another U-vertex
containing a and avoiding p. Its cubic center cannot be a; its points
therefore lie in {a,b,q}. A 22 is excluded against the opposite 31.
A 31 centered at b or q violates Lemma 2.1's coset budget. An
ordinary centered at b would overlap that center with 3a+b; one
centered at q would overlap its center with 2p+q+b. A pure quartic
would have to be centered at a, contrary to different cubic centers.
These exhaust the possibilities. Thus 2a+b is unpaired.

Uniqueness of the unpaired mark with singleton b forces 2p+b to be
paired. Cone its partner by q, obtaining a U-vertex avoiding p and
using {a,b,q}. A 22 is again excluded. A 31 centered at b or q
violates the coset budget; one centered at a would make
3a+q=3a+b, hence q=b. Ordinary centers a,b violate the center
exclusion from 3a+b. The only surviving vertex is 4q.
Symmetrically 4s lies in V at the same value. Odd-order multiplication
by four forces q=s, contradicting disjoint supports. QED.

In particular the pure-quartic option is retained in this proof, not
incorrectly discarded as another unpaired mark. Cubic and quartic
multiway collisions were excluded ONLY where R3=0 justifies doing so.
