# Stage 12 alternative route: local multiway quartic bridges

Research date: 2026-10-10. This is a focused elementary restriction,
not a proof of h=0 => D=0 or of |E4|>=60. No novelty is asserted.
No new computation was performed for this note.

## 1. Statements and dependency ledger

Throughout, A is a valid eight-point set in its odd cyclic
difference-generated subgroup H, and h=0. Thus doubling permutes
the 56 nonzero ordered differences. The propagation graph has the
distinct repeated quartic multisets as vertices. A quartic fiber is
fresh if its induced propagation graph has two or more components.

**Proposition A (no-pure cones).** Suppose three distinct cubic marks
have common value Y and disjoint center and singleton sets,

    Y=2c0+b0=2c1+b1=2c2+b2,
    C={c0,c1,c2}, B={b0,b1,b2}, A=C union B union F, |F|=2.

For EVERY t in A, the entire repeated quartic fiber at Y+t is
connected. It is not merely the three displayed cones that are
connected. This statement does not exclude the cubic triple itself.

**Proposition B (one-pure cones).** Suppose

    Y=3z=2a+b=2d+e,
    P={z,a,b,d,e}, |P|=5.

For t outside P the entire repeated quartic fiber at Y+t is
connected. If t is in P and that quartic fiber is fresh, it has
exactly two components: one whose support union is precisely P,
and an isolated ordinary vertex on the three complementary points.
The center of the isolated vertex participates in a different cubic
fiber with at least three marks.

The elementary dependencies are:

* Validity forbids a different equal-length representation of any
  squarefree sum of degree at most eight. It implies pair-sum and
  ordered-difference uniqueness in odd H.
* Stage5's singleton-base spanning-tree lemma, whose short proof is
  reconstructed below, pairs every pure cubic without assuming R3=0.
* Stage9's elementary order-three exclusion. It ensures that a pure
  cubic cannot have another pure partner. Proposition A and B use
  this theorem, not the Stage10 finite computation.
* The local disjoint 31/31, disjoint 22/31, and overlapping-31-at-pure
  lemmas, reconstructed below from validity and doubling closure.

Only the additional conclusion that Proposition B's second multiway
cubic fiber has EXACTLY three marks uses Stage10's finite-computation
exclusion of four-way fibers. Its kernel audits share structural
generators; that computational dependency is not promoted to an
elementary theorem here. A fresh cone of a three-way cubic fiber
requires a one-pure shape and at least two distinct multiway cubic
fibers, hence R3>=2, already elementarily. After Stage10 both are
three-way fibers.

The one-pure shape remains unresolved. Neither proposition excludes
fresh quartic fibers that cone no cubic triple. Even h=0 => D=0
would still leave Sigma>=53 in the regular branch and the h>0
cases for the original 248 target.

## 2. Audited foundations without R3=0

### 2.1 Squarefree replacements and support separation

If two repeated quartic representations at one value share a point t,
delete one copy of t from each. The remaining distinct cubic multisets
cannot include a squarefree multiset: its equality to the other cubic
would be a forbidden squarefree replacement. Therefore both cubics
are repeated, and their equality gives a propagation edge by coning t.

It follows that support unions of different components at one value
are disjoint. If two such unions intersected, a vertex from each
containing the shared point would be joined by the preceding edge.
This uses ENTIRE support unions, not one chosen representative per
component, and does not require a bound on cubic fiber multiplicity.

For an ordinary vertex 2a+b+c, the three points are distinct. Its
center a occurs in no other distinct representation of that value:
deleting a would equate the squarefree triple a+b+c to a different
cubic. In particular different ordinary vertices have different
centers, and each ordinary center is absent from every other vertex.
On a support union of at most three points there is therefore at most
one ordinary vertex.

### 2.2 Every pure cubic is paired

Fix a singleton base x in A. For each r!=x, doubled-difference
uniqueness supplies a unique equation

    2u+x=2v+r,

with oriented edge u -> v and label r. The seven underlying center
edges are distinct, since doubling bijects the unordered difference
pairs. If they had an undirected cycle, sum its equations with signs
according to a traversal. The resulting nonzero balanced relation
has coefficients in {-1,0,1} at the distinct labels and only the
coefficient at x can have larger magnitude. One of that relation or
its negative has every coefficient at least -1, and adding it to the
all-ones vector gives a rival eight-term multiset. Thus the seven
edges form a spanning tree.

No edge enters x: 2u+x=2x+r would give 2u=x+r, a forbidden pair
replacement. Since x cannot be an isolated vertex in the spanning
tree, some edge leaves x. Its equation pairs 3x with 2v+r.

Neither v nor r is x, by the same pair/trivial equality argument.
Nor is v=r: this would give 3x=3v, contrary to Stage9's absence of
order-three differences. Hence every pure quartic 4x has a propagated
ordinary neighbor 2v+r+x using three distinct points. Its propagation
component has support size at least three, regardless of R3.

## 3. Local type restrictions and the four-point 31 bound

### 3.1 Disjoint 31/31 and the exhausted order-five cosets

Suppose 3a+b=3c+d with four distinct points. Write
2(a-c)=u-v using h=0. Substitution gives

    a+b+u=c+d+v.

These triples are different (the disjoint pairs {a,b},{c,d} cannot
both be supplied by one extra point). Neither can be squarefree.
Thus u is a or b, and v is c or d. The four cases give respectively
a=c, 2c=a+d, 2a=b+c, or 5(a-c)=0. Only the last survives. Thus
a-c has order five, and b-d=-3(a-c).

Let J=<a-c>. The two unordered pairs {a,c} and {b,d} use all four
nonzero ordered differences of J. Their J-cosets must be different:
if the four points shared one J-coset, their twelve ordered
differences could not fit into J\{0}. Hence no other pair of A
has a nonzero difference in J, and the only A-points in the center
coset are a,c; the only A-points in the singleton coset are b,d.

### 3.2 Disjoint 22/31

A disjoint equality 2a+2b=3c+d is impossible at h=0. Indeed write
2(a-c)=u-v. The quartic equality yields 2b+u=c+d+v.
The right triple must repeat, so v is c or d. If v=c then
2a=c+u, forbidden by pair uniqueness. Thus v=d and
u=2a-2c+d is in A. Similarly w=2b-2c+d is in A. Then

    u+w+c=3d.

The left triple is squarefree: u=w would give a=b, u=c would
give b=d, and w=c would give a=d, using doubling injectivity.
This is a forbidden replacement.

At odd order, different equal quartics of types 4/4, 4/22,
or 22/22 are also impossible by doubling injectivity and pair
uniqueness.

### 3.3 Overlapping 31s at an external pure value

First, if 4w=3a+b with three distinct points, write
2(w-a)=u-v. It gives 2w+u=a+b+v, so v is a or b.
The first case gives 2u=a+b, forbidden. Consequently v=b and

    u=6w-5a is in A.                                      (1)

Two different 31 representations at 4w, with w outside their
supports, cannot overlap. A shared center makes them identical.
A shared singleton would give 3a=3c and an order-three difference,
which Stage9 excludes. The remaining overlap is a chain,

    4w=3a+b=3b+c.

Using E=6w-5a from (1), these equations imply
E+b+c=2w+a. Hence E must be b or c. If E=b, subtraction gives
w=a. If E=c, the same equations give w=2b-a and c=3a-2b,
so c+w=2a, a forbidden squarefree-pair replacement.

### 3.4 A 31 component opposite another 31 needs four points

Suppose different components at one value contain 3a+b and 3c+d.
By Section 2.2, choose ANY different pure-cubic partner
3a=2p+q. Its cone by b lies in the component of 3a+b.
Here p,q are distinct and neither is a. Support separation places
p,q outside the opposite component, in particular outside {c,d}.

If p=b, the coned vertex is 3b+q. Apply Section 3.1 to this
vertex and the opposite 3c+d. It forces b-c to have order five,
which puts b in the exhausted center coset containing a,c,
contrary to Section 3.1 for the original pair of 31s.

If q=b, the coned vertex is 2p+2b, forbidden opposite 3c+d
by Section 3.2. Thus p and q are two new points distinct from
a,b. The component of 3a+b has support size at least four.
The argument uses existence, not uniqueness, of a pure partner;
it excludes these roles for every available partner.

Similarly, a 31 component opposite an external pure quartic
4w has support size at least four. The option p=b would give
two overlapping 31s at 4w, excluded by Section 3.3; q=b would
give a 22 at 4w, excluded by odd doubling and pair uniqueness.
Again p,q are two new points.

## 4. Proof of Proposition A: every C/B/F cone

The three coned representations 2ci+bi+t are distinct and lie
in one component U, since each pair deletes the common point t.
Their support union contains C union B union {t}.

If t is in F, U has at least seven support points. Any other
component would have at most one. A pure component needs at least
three by Section 2.2; every other repeated quartic uses at least
two points. Thus there is no other component.

If t=bi, U contains 2ci+2bi, a 22, and has at least six support
points. Another component has at most two. A 4 or 22 there is
excluded by odd doubling and pair uniqueness; a 31 is excluded
by Section 3.2; an ordinary needs three distinct points. These
exhaust the repeated quartic types.

If t=ci, U contains 3ci+bi, a 31, and has at least six support
points. Another component has at most two. A pure component
needs at least three by Section 2.2, a 22 is excluded by
Section 3.2, and an ordinary needs three. A 31 component
opposite U needs at least four by Section 3.4. Again every
type is excluded. This proves Proposition A for all eight t.

No assumption was made that U contains only the three displayed
vertices. Additional vertices can only increase its support union.

## 5. Proof of Proposition B and its separate remaining shape

Cone the three marks 3z,2a+b,2d+e by t. They lie in one component
U whose support union contains P union {t}.

If t is outside P, U has at least six points and contains the
31 vertex 3z+t. An opposite component has at most two points.
Pure components need three; 22 is excluded against this 31;
ordinary needs three; and an opposite 31 component needs four.
The fiber is therefore connected.

Now t is in P. There are only three cases up to swapping
(a,b) with (d,e):

* t=z: U contains 4z. An opposite component of at most three
  points has no 4 or 22 by odd doubling. Its 31 component
  would need four points by Section 3.4's pure-value version.
  Only an ordinary can remain.
* t=a: U contains 3z+a and 3a+b, two overlapping 31s. An
  opposite pure 4w is excluded by Section 3.3, an opposite
  22 by Section 3.2, and an opposite 31 component needs
  four points by Section 3.4. Only an ordinary can remain.
* t=b: U contains 2a+2b and 3z+b. Odd doubling excludes
  an opposite 4 or 22; Section 3.2 excludes a 31. Only
  an ordinary can remain.

An opposite ordinary uses three points, so U must have exactly
the five support points P and the opposite support must be the
three-point complement. On those three points there is at most
one ordinary vertex by center exclusion. All other types have
just been excluded, so the opposite vertex is isolated. There
can be no third component, since all eight points are used.

Write the isolated vertex as 2u+v+w. Its two cubic marks
2u+v and 2u+w are unpaired: any different partner, coned by
the other tail, would give a different neighboring quartic.

For a fixed cubic center u, each of the other seven centers
collides with it exactly once at h=0. A mark belonging to a
fiber of size m accounts for m-1 of these incidences. If k
marks at center u are unpaired, then

    k = 1 + sum_(paired marks with center u) (m-2).       (2)

Indeed the total incidence sum is seven, while there are 8-k
paired marks. Since here k>=2, some cubic mark centered at u
has fiber size at least three. Its fiber is different from
the original one: any original-fiber mark centered at u, coned
by t, would belong to U and enlarge its support beyond P. This
contradicts the exact five-point support already established.
This argument does not assume that the original fiber has only
the three displayed marks. In fact freshness itself excludes an
additional original mark, by support separation and the cubic
foreign-center exclusion. This proves the elementary form of
Proposition B.

Each distinct fiber with at least three marks contributes at least
one to R3, so R3>=2 follows elementarily. Only after using Stage10
can one replace "at least three" by "exactly three" for the extra
fiber. Without Stage10 that fiber could have four marks; this note
does not silently exclude that possibility.

## 6. A further role restriction at a fresh pure value

This independent elementary observation may help a later focused
round, but is not used to close either proposition.

Suppose 4z=2u+v+w belongs to a fresh fiber, with the ordinary
component separated from the pure component. Write the unique
doubled difference

    2(u-z)=r-s.

Substitution gives r+v+w=2z+s, so r is v or w; otherwise
the left triple is squarefree. Pair uniqueness gives
s not in {z,v,w}. For EVERY available pure-cubic partner
3z=2p+q, one also has s!=p. Otherwise substituting s=p
and then 3z=2p+q gives

    2u+z=p+q+r,

a forbidden squarefree-triple replacement: p,q lie in the
pure component and r in the separated ordinary component.
This excludes all doubled partner centers simultaneously and
does not choose one preferred partner.

In particular if 3z has two partners 2p+q and 2d+e, those
partners use four distinct points by Stage9. Proposition B
at t=z forces

    A={z,p,q,d,e,u,v,w},   s in {u,q,e}.

The surviving placements s=u or s=q or s=e have NOT been
excluded. They describe necessary role constraints, not valid
counterexamples. The pure component at this value has the three
coned vertices forming a triangle, since each pair deletes z;
it must not be described as a path or a star.

## 7. Precise obstruction and next direct-route checkpoint

Stage8's singleton permutation and degree-two graph conclusions
do not extend merely because triple cones are now controlled.
An ordinary vertex can still be isolated: two unpaired marks
at its center force a multiway fiber elsewhere by (2), not
necessarily one coning to the same quartic value. Likewise
two unpaired marks with the same singleton can replace the
regular injectivity argument used to exclude short components.

The most useful next direct-route lemma is therefore precise:

    Under odd h=0 and validity, an isolated ordinary vertex
    cannot share a quartic value with a component coned from
    a one-pure cubic triple whose five-point core is disjoint
    from that ordinary vertex.

It would eliminate the only residual fresh triple-cone shape
in Proposition B. It would NOT by itself settle fresh fibers
that contain no coned triple, nor the global D=0 statement.

Proposition A is already a genuinely stronger bridge restriction:
all no-pure triple cones are harmless for D even if the triple
itself survives. No computation, random sampling, modulus sweep,
or rerun of completed checks is part of this proof. The note
supplies algebraic coverage rather than an inference from tests.
