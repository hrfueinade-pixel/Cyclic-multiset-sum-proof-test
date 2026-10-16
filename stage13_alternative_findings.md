# Stage 13 alternative route: restrictions on the forced u-fiber

Research date: 2026-10-10. One focused elementary round.
The fresh pure-cone obstruction, h=0 => D=0, and |E4|>=60
remain open in this note. No novelty is asserted. No computation
was performed.

This is the boundary of the elementary route in this note. The joint
stage13_pure_cone_findings.md separately closes the pure cone by a
complete finite computation and the doubled-center cones elementarily.
The singleton cones and full h=0 => D=0 remain open.

## 1. Hypotheses and the two distinct families

Assume validity, odd difference-generated subgroup H, h=0, and
the elementary Stage9 absence of order-three differences. Suppose
the quartic value 0 has separated components containing

    0=3*0=2a+b=2d+e,
    0=2u+v+w,
    A={0,a,b,d,e,u,v,w}, all eight points distinct.

The first line is a cubic triple; its cone by 0 contains 4*0,
2a+b+0,2d+e+0. Stage12 implies that its support is exactly
P={0,a,b,d,e}, while 2u+v+w is an isolated ordinary vertex
on the three complementary points. The two marks 2u+v and
2u+w are therefore unpaired.

The doubled-difference role restriction in Stage12 reduces,
up to swapping a,d and v,w, to:

    I:  b=-2a, e=-2d, v=3u, w=-5u;
    II: b=-2a, e=-2d, v=2u+b, w=-2u-v.

These are necessary relation families, not assertions of valid
realizations. Family I and II must remain separate.

## 2. Proved restrictions

**Proposition I.** In Family I, every additional partner of
the pure cubic 3u beyond the two marks

    3u=2u+u=2*0+v

must be one of the following four role patterns:

    3u=2b+e, 3u=2e+b, 3u=2w+b, 3u=2w+e.           (1)

At most one additional partner exists. Thus this particular
fiber has at most three marks elementarily, without Stage10.
Also the mark 2u+0 cannot belong to a fiber with three or
more marks.

Consequently the extra multiway fiber forced at center u by
the isolated ordinary vertex is either the pure fiber 3u
with one of the patterns (1), or a fiber whose u-mark has
singleton label in {a,b,d,e}.

**Proposition II.** In Family II the forced cubic fiber

    v=2*0+v=2u+b

has exactly two marks. It is not the extra multiway fiber
forced at center u. A forced multiway fiber at center u must
instead have its u-mark's singleton label in {0,a,d,e,u}.

None of these restrictions excludes the required extra fiber.
The one-pure core obstruction is therefore not settled by them.

## 3. Audited elementary tools

### 3.1 Distinct fibers cannot share a center pair or label pair

The centers in a cubic fiber are distinct, as are its singleton
labels. In an odd group, difference uniqueness and invertibility
of doubling imply:

* A fixed pair of different centers can collide only once: its
  doubled difference has only one representation as a singleton
  difference.
* A fixed pair of different singleton labels can collide only
  once: their difference has only one halved center difference.

Thus two distinct cubic fibers share at most one center and at
most one singleton label. This does not assume R3=0 or Stage10.

If a singleton label in one mark is a foreign center in another
mark of the same fiber, the equality would give a forbidden
pair replacement. Explicitly 2p+r=2r+q gives 2p=r+q.
The only possible common center/label is its own pure point.
Stage9 excludes two pure marks in one fiber.

### 3.2 Two universal exclusions at the value v

Consider ANY additional cubic representation

    2p+q=2*0+v.                                      (2)

If q=a or d, let Bq be its original singleton partner b or e,
so 2q+Bq=3*0. Subtracting this equality from (2) gives

    2p+0=q+Bq+v.

The right side is squarefree: q,Bq are distinct core points,
and v is outside the core. This contradicts validity. Hence
q is neither a nor d, for EVERY available representation (2).
No preferred partner is selected.

If q=w, combine 2p+w=v with 2u+v+w=4*0. Division by two
is legitimate in odd H and gives

    p+0=u+v.

The right pair is squarefree and contains no 0; it cannot be
the same multiset as the left. Pair uniqueness gives a
contradiction. Thus q cannot be w either.

## 4. Proof of Proposition I

At v=3u, the two known centers are u,0 and the two known
singleton labels are u,v. A further mark 2p+q has neither
p nor q in {0,u,v}: duplicate centers or labels, or a foreign
center/label occurrence, would violate Section 3.1.

Its center p cannot be a or d either. The pair {0,a}, or
{0,d}, already collides in the distinct original cubic fiber
of value 0. The values 0 and v are distinct because v is
one of the eight distinct points. Section 3.1 excludes a
second collision with that center pair.

Section 3.2 excludes singleton q=a,d,w. Therefore

    p in {b,e,w}, q in {b,e}.

The option p=q would be another pure mark in the pure-u
fiber, forbidden by Stage9. Removing those options leaves
exactly the four patterns (1).

There cannot be two additional partners: they would have
distinct centers and distinct singleton labels, and every
intersection between these center and singleton sets would
be foreign or a second pure point. Their four points would
therefore have to be distinct, but all lie in the three-point
set {b,e,w}. This proves the at-most-three bound for this
fiber, without the Stage10 computation.

Now consider the fiber containing 2u+0. Its value is 2u,
which is neither 0 nor v=3u because u!=0 and doubling is
invertible. Its center cannot be 0: the pair {u,0} already
collides in the fiber v. Any other singleton label q is
neither 0 nor u, by uniqueness and foreign-center exclusion.
It also cannot be b or e: either label pair {0,b} or {0,e}
already collides in the original cubic fiber 0. Thus

    q in {a,d,v,w}.

If q=a or d, a partner 2p+q=2u, together with
2q+Bq=3*0 and 3u=2*0+v, gives

    2p+u=q+Bq+v.

Its right triple is squarefree, contradicting validity.
If q=v, the equality 2p+v=2u and v=3u give
2p+u=3*0. This would add a mark using the outside point
u to the original cubic fiber. Coning by 0 would join
its quartic representation to the pure component and
enlarge that component's support beyond P, contradicting
the separated ordinary component. Hence q is not v.

Only q=w remains. Singleton labels in a cubic fiber are
distinct, so there can be at most one partner. The mark
2u+0 cannot belong to a multiway fiber. Finally the labels
v,w are already unpaired at center u by isolation. Removing
0,v,w from the eight possible labels leaves precisely
u,a,b,d,e as the labels of a forced multiway u-mark.
This proves Proposition I.

## 5. Proof of Proposition II

At the value v the two known marks are 2*0+v and 2u+b.
For any additional mark 2p+q, center uniqueness and foreign
center/label exclusion remove p=0,u,v,b. The centers a,d
are also excluded because their pair with 0 already collides
in the original fiber 0. Consequently

    p in {e,w}.

The singleton q is not v or b by label uniqueness, and
not 0 or u by foreign-center exclusion. Section 3.2
excludes q=a,d,w. The only remaining possible label e
is excluded as well: singleton pair {b,e} already collides
in the original cubic fiber 0. These two fibers are
distinct since v!=0. Thus there is no additional mark.

This proves the exact-pair assertion. At center u, label b
belongs to this pair, and labels v,w are unpaired. The only
remaining labels for the forced multiway u-mark are
0,a,d,e,u, as stated.

## 6. Dependency ledger and precise remaining work

Elementary dependencies:

* Validity and odd-group pair/difference uniqueness.
* Stage5's singleton-base spanning tree, to pair pure cubics
  and to force a multiway mark when a center has two
  unpaired marks.
* Stage9's no-order-three theorem, for the foreign-center
  and single-pure restrictions used above.
* Stage12's elementary fresh pure-cone support split.

No Stage10 finite computation is needed for Propositions I
or II. Stage10 can independently assert that the other
multiway fibers still sought have exactly three marks.
Its computational dependency must remain explicit when
that exact size is used.

The four patterns (1), the other labels {a,b,d,e} in
Family I, and {0,a,d,e,u} in Family II remain unexcluded.
They are surviving ROLE patterns, not configurations shown
to satisfy all singleton trees, not valid examples, and
not counterexamples to D=0. No conclusion is inferred
from the absence of a contradiction in this round.

The specific next lemma is:

    For either family, the extra cubic fiber forced at
    center u cannot occupy the remaining labels and role
    patterns while all singleton-base trees and validity
    are satisfied.

This note handles only the pure cone t=0. The other four
core cones of a one-pure triple and quartic fibers coning
no triple remain separate. The global target is unchanged.
