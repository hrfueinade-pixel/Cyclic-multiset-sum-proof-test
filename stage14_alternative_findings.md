# Stage 14 alternative route: the exact pair-shadow defect obstruction

Research date: 2026-10-10. This note is elementary CONDITIONAL on
all multiway-cubic-coned quartic fibers being connected. The root's
Stage14 singleton calculation supplies the last required cone
exclusion, with computational dependencies preserved separately.
No computation was performed for this alternative note.

The full h=0 => D=0 statement and the original 248 target remain open.

## 1. Precise local-defect theorem

Let A be valid, with eight distinct points, in its odd cyclic
difference-generated subgroup H, and suppose h=0. Use Stage9's
elementary absence of order-three differences. Assume additionally:

    (MC) Every quartic fiber containing a cone of a cubic fiber
         with at least three marks is connected in its entirety.

A fresh quartic fiber means a fiber with at least two propagation
components. For such a fiber X, let U(X) consist of the UNPAIRED
repeated cubic multisets obtained by deleting a point from a repeated
quartic vertex in X. This is a set of literal cubic multisets, not
chosen representatives or singleton labels alone.

**Theorem (local defect).** Every fresh fiber X has at least one of:

* An isolated ordinary vertex 2a+b+c. Its two marks 2a+b,2a+c
  are distinct unpaired marks at the same center a.
* Two distinct marks 2a+b,2c+b in U(X) with the same singleton b.

Equivalently, if X has no isolated ordinary vertex and singleton
labels are injective on U(X), X cannot be fresh.

Both defects force a multiway cubic fiber elsewhere: centered at a
in the first case, and having singleton label b in the second.
The incidence proof does not identify that fiber's value or a cone
at X. This missing transport is the exact remaining obstruction;
(MC) by itself cannot be substituted for R3=0.

## 2. Dependency ledger and audited local consequences

Elementary inputs, whose complete earlier proofs are retained:

* Validity forbids squarefree replacements of degree <=8.
* Odd order gives pair/difference uniqueness and invertible doubling;
  h=0 gives 2Delta=Delta.
* The singleton-base tree pairs every pure cubic (Stage5), without R3=0.
* Stage9 excludes order-three differences.
* Support unions of distinct components are disjoint; an ordinary
  center appears in no other vertex of its fiber (Stage4/Stage12).
* The local disjoint 31/31 order-five lemma, disjoint 22/31 exclusion,
  4/31 closure, and overlapping-31 obstruction at an external pure
  value are elementary and reconstructed in Stage12.
* The elementary exterior packing gives |H|>=184 independently of
  R3=0; in fact |H|>=184+2R3. No n<=7 certification is used.

(MC) is an additional hypothesis for the theorem. Its application to
the current research uses the elementary Stage12 no-pure cone result,
the elementary doubled-center-cone result of Stage13, the Stage13
pure-cone computation, and the Stage14 singleton-cone computation.
The Stage10 four-way EXCLUSION THEOREM is not needed: a fiber with
at least four marks has at least three nonpure marks by Stage9;
their cones already give the elementary Stage12 no-pure result.
A three-mark fiber is either no-pure or one-pure, handled by the
listed results. The Stage13/14 calculations do use the kernel
IMPLEMENTATION originating in Stage10; that shared-code dependency
must remain recorded separately from the four-way exclusion theorem.
No bound m<=3 is assumed in this note.

If X is fresh, (MC) implies every cubic deletion of a vertex in X
has at most two marks in its fiber. Otherwise that vertex cones a
multiway cubic to X, making X connected. Therefore the propagation
graph on X has maximum degree two. Its components are paths, cycles,
or isolated vertices. No global singleton permutation is inferred.

Each pure quartic has degree exactly one: its pure cubic is paired,
and that cubic has exactly two marks locally. Each 31 has degree
one or two; its pure-cubic deletion is paired. Ordinary and 22
vertices can have degree zero. Distinct relevant deletions cannot
give the same neighbor, by pair uniqueness.

Throughout the proof below assume for contradiction that X is fresh,
has no isolated ordinary vertex, and singleton labels are injective
on U(X). These are LOCAL conditions, not R3=0.

## 3. No fresh 31/31 under local singleton injectivity

Suppose different components contain 3a+b and 3c+d. The disjoint
31/31 lemma puts a,c in one order-five coset and b,d in another.
Their two pairs exhaust all four nonzero differences of that subgroup.

Every pure-cubic partner of 3a, coned by b, lies in its component.
It must have the form 2p+q with two new distinct points: a is excluded
by cubic/pair uniqueness; the opposite support is excluded by component
separation; doubled center b would put b into the exhausted center
coset; singleton b gives a prohibited 22; a pure partner is excluded
by Stage9. Similarly 3c=2r+s uses two other new points. Thus

    support(U)={a,b,p,q}, support(V)={c,d,r,s},
    3a=2p+q, 3c=2r+s,

and the two components exhaust A. Any additional pure-cubic partner
would have to obey these exact support restrictions; local (MC)
also gives the uniqueness of these partners at X.

The mark 2a+b is unpaired. Otherwise cone its partner by a. The
new U-vertex avoids the ordinary center p and uses {a,b,q}. A 22
is forbidden against the opposite 31. A 31 centered at b or q
violates the exhausted order-five coset; a center-a cubic partner
would be identical. An ordinary centered at b meets the point b in
3a+b, and one centered at q meets q in 2p+q+b, violating center
exclusion. A pure coned vertex would be 4a, forcing b=a. All options
are exhausted.

The deletion mark 2p+b cannot also be unpaired: both it and 2a+b
would lie in U(X) with singleton b. Therefore it is paired. Cone
its partner by q. The new vertex avoids p, hence uses {a,b,q}.
The preceding type restrictions leave only 4q. Thus 4q has value X.
The mirrored argument gives 4s in V. Odd multiplication by four
forces q=s, contrary to disjoint supports. No fresh 31/31 is possible.

This proof explicitly retains the pure-quartic option. It uses local
injectivity on U(X), not a global unique-unpaired-singleton claim.

## 4. All-ordinary components have at least six points

An all-ordinary component cannot have one vertex, by the no-isolated
ordinary assumption. Nor can it have exactly two vertices: write
their tails as {u,v},{v,w}. Their only propagation edge deletes v;
the other cubic deletions are distinct unpaired marks with common
singleton v. This contradicts injectivity on U(X).

With at least three vertices their distinct centers are absent from
all tails. Distinct centers require distinct tail pairs, by odd
doubling. At least three tail points are therefore required. Four
centers require at least four tail points. Thus an all-ordinary
component has at least six points; if it has at most six it is
exactly the triangle

    x=2r+u+v=2s+v+w=2t+w+u.

Summing and dividing by two gives the squarefree six-term identity

    r+s+t+u+v+w=3x/2.

It cannot share x with an external pure 4z or 22 vertex 2a+2b:
that would replace the squarefree six-set by respectively 6z or
3a+3b. This uses no global unpaired-mark permutation.

## 5. No ordinary vertices in different components

Suppose U,V both contain ordinary vertices. If neither component
has three support points, they each have exactly four. Each then
has only one ordinary vertex, since two distinct ordinary centers
would leave only two possible tail points, giving equal tails and
then equal doubled centers. Because an ordinary vertex is not
isolated, each component has a nonordinary vertex.

If one has a 22, every nonordinary type in the other is excluded by
odd doubling or disjoint 22/31. Otherwise their nonordinary types
are pure and 31. They cannot both contain pure vertices, or both
contain 31s by Section 3. Consequently one component contains only
its ordinary vertex and pure vertices. There is at most one pure
vertex, so that component has support size three, a contradiction.

Thus one component has the three-point form

    U={4z, 2p+z+q}, 3z=2p+q,

with p,z,q distinct. It is exactly this two-vertex component: its
ordinary center p is absent from other vertices, and neither a 31
nor a 22 on the other two points can have the same value. Its other
ordinary deletion 2p+z is unpaired; this conclusion is local.

The opposite component V uses at most five points. Its vertices
are ordinary or 31, since its value is 4z. It has one or two
ordinary centers: three would leave only two tail points and make
their distinct tail pairs impossible. A 31-only component is
impossible, since overlapping 31s at the external pure value 4z
are forbidden, but every 31 must have a propagation neighbor.

### 5.1 Two ordinary vertices in V

Their tails are {u,v},{v,w}. They cannot form the whole component,
by Section 4's local unpaired-singleton argument. The other vertices
are 31s on the three tail points. At the pure value their supports
are disjoint, so there is at most one such vertex. It cannot contain
v: deleting v from all three vertices would give a three-way cubic
at a fresh fiber, contrary to (MC). Therefore, after relabeling,

    4z=2r+u+v=2s+v+w=3u+w.

Translate u=0 and put B=z, Q=v/2, P=p. The eight distinct points
are then

    z=B, p=P, q=3B-2P, u=0, v=2Q, w=4B,
    r=2B-Q, s=-Q.

The doubled-center difference restriction for a disjoint ordinary
equality forces the doubled difference to be a left-tail minus
a right-tail. For centers p,r it gives one of

    R1: 2P=5B-2Q, R2: 2P=5B-4Q,
    R3: 4P=7B-2Q, R4: 4P=7B-4Q.

For centers p,s it gives one of

    S1: 2P=B-4Q, S2: 2P=-3B-2Q,
    S3: 4P=3B-4Q, S4: 4P=-B-2Q.

The exact elementary contradiction table is unchanged from Stage8:

| |S1|S2|S3|S4|
|---|---|---|---|---|
|R1|r=w|z=u|2w=u+z|p+w=z+u|
|R2|z=u|2z=r+w|p+z=2u|r+p+z=3u|
|R3|z+w=p+r|p+u=z+w|r=w|z=u|
|R4|p+z=u+w|r+w=p+z|z=u|2z=r+w|

Each follows by adding the corresponding two displayed equations
and dividing only by powers of two. For example R2,S4 give 6Q=11B
and 2(r+p+z)=11B-6Q=0; R4,S2 give 13B=0 and
2(r+w-p-z)=13B. Every entry is a duplicate point, a forbidden pair
equality, or a squarefree-triple replacement. Stage8's saved exact
row certificates also record every identity; no rerun was needed.

### 5.2 One ordinary vertex in V

Every other vertex is 31, its center excludes all other vertices,
and the 31 supports are pairwise disjoint at 4z. There are at most
two, and at least one by the no-isolated ordinary condition.

One 31 alone is impossible. Its pure-cubic edge pairs it to the
ordinary vertex by deletion of its singleton. The other deletion
of that 31 and the other ordinary deletion are both unpaired
with the same singleton. This violates injectivity on U(X).

Two 31s give exactly

    4z=2a+b+c=3d+b=3e+c.

Set e=0 and delta=d-e of order five. Then

    d=delta, c=4z, b=4z+2delta, a=-2z-delta.

The elementary 4/31 closure forces 6z in A. It is none of
z,a,b,c,d,e: equality with c or b gives z=e or d; equality
with e gives c=z; equality with z or a puts z into the
exhausted order-five coset; equality with d gives 3z in that
subgroup and the additional prohibited order-five difference a-z.
Thus 6z is p or q in U.

If p=6z then q=-9z. The four tail possibilities for centers p,a
give 19z+4delta=0,19z+2delta=0,29z+4delta=0, or29z+2delta=0.
They put delta in <z> and all points in <z>, whose order divides
95 or145. This contradicts |H|>=184. If q=6z, then p=-3z/2;
the same four possibilities give z=-delta,2z=-delta,z=4delta,
or z=2delta, again violating the exhausted coset budget.

Thus ordinary vertices cannot occur in different components.
All uses of R3=0 in Stage8's shape reduction have been replaced
by (MC), no isolated ordinary, and injectivity on U(X). The
algebraic identities themselves never required R3=0.

## 6. Closing every type under the two local conditions

If X contains a pure vertex, let U be its component. Stage9 and
pure pairing give it an ordinary neighbor. Section 5 prohibits
ordinary vertices in any other component. An opposite component
has no pure or 22 by odd doubling, hence consists only of 31s.
But overlapping 31s at the external pure value are forbidden,
and a 31 cannot be isolated because its pure cubic is paired.
This is impossible.

If X contains a 22, any opposite component is all-ordinary by
odd doubling and disjoint 22/31. Its support has at most six
points. Section 4 gives the squarefree-six replacement against
the external 22, impossible.

If X contains a 31, all opposite components are all-ordinary:
the pure/22 cases are already excluded and Section 3 excludes
fresh 31/31. Its own component cannot contain an ordinary
vertex by Section 5. It is 31-only and needs at least three
support points: one 31 cannot be isolated and distinct equal
31s cannot use just two points at odd order. An opposite
all-ordinary component needs six points by Section 4, exceeding
eight. Finally, if all vertices are ordinary, Section 5 already
excludes more than one component. This proves the local-defect
theorem.

## 7. Exact defect transport identity and why it does not close D

For any fixed center a, let k_a be the number of unpaired marks
with that center. Each other center collides with a once; a mark
in a fiber of size m accounts for m-1 of those seven incidences.
Thus

    k_a=1+sum_(paired a-marks)(m-2).

The same formula holds for a fixed singleton b, because doubling
bijections center pairs and singleton pairs:

    k_b=1+sum_(paired b-marks)(m-2).

The theorem's first defect has k_a>=2 and its second has k_b>=2.
Hence each forces some multiway fiber. The two unpaired deletion
marks at X are NOT themselves members of that fiber: they are
unpaired by definition. The identity specifies no value for the
forced multiway cubic and no element t with value(X)=value(cubic)+t.
Therefore (MC) gives no contradiction until such a transport
statement is proved. This is an explicit logical gap, not a
counterexample or a failure of the original conjecture.

**Single useful next lemma:** under the current odd h=0 hypotheses,
a center or singleton defect in a fresh quartic fiber forces a
multiway cubic fiber whose cone lies at that SAME quartic value.
Combined with (MC) and the local-defect theorem, this would prove
D=0. It is proposed, not proved. A weaker sufficient version is
to prohibit both local defects directly using all singleton trees.

No new examples, set searches, computations, random sampling,
or modulus sweeps were performed. The conditional proof does not
imply R3=0. Harmless multiway cubic fibers may remain globally.
