# Stage 13 independent challenger: the fresh pure-cone reduction

Scope: audit of the PURE cone of a one-pure cubic triple, with an
elementary doubled-center proof in the final consolidation. No numerical
computation was performed by this challenger. The joint report
stage13_pure_cone_findings.md separately closes the pure cone by a
complete finite computation whose implementation and coverage I audited.
Earlier unresolved statements below describe the elementary route alone,
not a contradiction of that joint result. Singleton cones, triple-free
fresh fibers, h=0 => D=0, and the original 248 target remain open.

## 1. Audited two-family coverage

Assume the Stage12 fresh pure-cone hypotheses, translate z=0, and write

    A={0,a,b,d,e,u,v,w}, b=-2a, e=-2d, 2u+v+w=0.

The unique ordered difference 2u=r-s must have r in {v,w} and
s in {u,b,e}, by Stage12's squarefree replacement argument. Swap
v,w to arrange r=v. If s=u, then v=3u and w=-5u. If s=b,
then v=2u-2a and w=2a-4u. Swapping (a,b) with (d,e) converts
s=e to this second case. Thus the two formal families are

    I:  (0,a,-2a,d,-2d,u,3u,-5u),
    II: (0,a,-2a,d,-2d,u,2u-2a,2a-4u).

These are rank-three integer linear presentations, not an assertion
of eight distinct valid points or a cyclic h=0 realization.

Freshness also excludes any additional mark of the original cubic
fiber at zero. Its center cannot be one of the existing centers
(doubling injectivity), nor one of the existing foreign singleton
labels. It would therefore lie outside the five-point core, and its
cone would enlarge the core component's support, contradicting the
exact five-point support proved in Stage12. This argument establishes
exactly the two displayed DIFFERENT partners of 3z; it says nothing
about uniqueness of partners of other pure cubics.

## 2. Additional known Family II tree equations

In Family II one has

    2u+b=v,       2v+w=b.

In the singleton-base tree with base b, the following edges are forced:

    a -> 0 (label 0),       a -> d (label e),
    u -> 0 (label v),       0 -> v (label w).

They are four edges forming a tree on {a,d,0,u,v}, not a contradiction.
The base-w tree also contains v -> 0 with label b. In particular a
claim that the two-family reduction alone creates an undirected cycle
in one singleton tree would be false. Completing every simultaneous
singleton-tree equation remains unresolved.

## 3. Explicit valid controls without h=0

Both formal families can actually be valid at large modulus and have
the stated fresh quartic value. This establishes that their local
relations alone cannot be excluded using validity alone.

Set u=1, a=R, d=R^2, N=24R^2+1. Use R=41 in Family I and R=33
in Family II. Thus the integer lifts are respectively

    I:  (0,41,-82,1681,-3362,1,3,-5), N=40345;
    II: (0,33,-66,1089,-2178,1,-64,62), N=26137.

The two groups have odd order, not divisible by three. All eight
points are distinct. Both contain difference 2, but not difference 4:
in I the difference is 3-1; in II it is (-64)-(-66). Inspection of
the eight fixed lifts gives no difference 4 or -4, and their largest
absolute difference is less than N-4. Hence both fail doubling closure,
independently of any unproved theorem.

### 3.1 No-wrap and no-carry justification

Every eight-term lift sum lies in [-16R^2,8R^2], an interval of
width N-1. Equality modulo N with the target therefore means equality
of integers. The target is -R^2-R-1 in both families.

Write each lift in the three formal coordinates (a,d,u). Relative
to the target, the coefficient at u in I belongs to [-39,25], and
in II to [-31,17]. Both intervals contain zero but no other multiple
of the chosen R. Reducing an equal integer sum modulo R therefore
forces its u-coefficient to be -1. Dividing by R then does the same
for its a-coefficient: its difference from -1 belongs to [-15,9]
in I and [-15,17] in II. Finally its d-coefficient is -1.
Thus integer equality is exactly equality of the formal coefficients.

### 3.2 Uniqueness for Family I

Let k_t count point t. The coefficient equations are

    k_a-2k_b=-1,     k_d-2k_e=-1,
    k_u+3k_v-5k_w=-1,

with nonnegative counts totaling eight including k_0. The first two
equations require k_b,k_e>=1. If either exceeds one, those two
coordinate blocks already use at least seven slots, leaving at most
one low slot. No one point from {0,u,v,w} has coefficient -1, so this
is impossible. Consequently k_a=k_b=k_d=k_e=1 and four low slots remain.

Now k_w>=1. For k_w=1, k_u+3k_v=4; the slot bound leaves only
k_u=k_v=1. For k_w>=2, k_u+3k_v=5k_w-1 but at most 4-k_w slots
remain, with maximum coefficient 3(4-k_w); this is already less
than 5k_w-1 for k_w>=2. Hence all eight counts equal one.

### 3.3 Uniqueness for Family II

The equations are

    k_d-2k_e=-1,
    k_a-2k_b-2k_v+2k_w=-1,
    k_u+2k_v-4k_w=-1.

If k_e>=2, its coordinate block uses at least five slots. The
last equation needs at least three additional slots, uniquely
k_u=k_v=k_w=1 when only three slots are available. Their a-coefficient
is zero, not -1, so additional a/b slots would be needed. Thus
k_d=k_e=1 and six remaining slots are available.

Put q=k_w. The last equation gives k_u=4q-2k_v-1, so q>=1.
For q=1, k_v is zero or one. If zero then k_u=3 and the a-equation
gives k_a=2k_b-3, requiring at least three a/b slots in addition
to the four u/w slots. If k_v=1, k_u=1 and k_a=2k_b-1, forcing
k_a=k_b=1 and k_0=1. For q=2, the slot bound forces k_v=3,k_u=1
and no a/b slots; the a-coefficient is then -2, not -1. For q>=3,
the u/v/w block has at least 3q slots (since k_v<=2q-1), exceeding
six. Again the all-ones multiset is unique.

### 3.4 Their quartic fiber at zero is exactly the four stated vertices

The same no-wrap/no-carry reasoning applies to degree four. If a
quartic sum is zero, the d-coordinate requires k_d=2k_e. A nonzero
such block needs three slots and leaves at most one slot, whose
other coordinates vanish only at the point zero. It gives the
vertex 2d+e+0. Otherwise k_d=k_e=0.

For I, the a-coordinate similarly gives 2a+b+0, or leaves only
the low block. The zero u-coordinate then gives either four zeros
or k_w=k_v=1,k_u=2, namely 2u+v+w. No larger k_w fits four slots.

For II, if k_w=0 the u-coordinate gives k_u=k_v=0 and the
a-coordinate gives either four zeros or 2a+b+0. If k_w=1,
k_u=4-2k_v. The four-slot bound allows k_v=1,k_u=2, yielding
2u+v+w. The other possibility k_v=2,k_u=0 needs two extra a-points
to satisfy its a-coordinate, exceeding four slots. Values k_w>=2
need at least 3k_w slots, so are impossible.

Thus at zero the three core vertices (4*0, 2a+b+0, 2d+e+0)
form one component and the disjoint ordinary 2u+v+w is isolated.
These are explicit valid h>0 controls, not counterexamples to any
h=0 claim. No numerical check is substituted for the proofs above.

## 4. Exact remaining obstacle

Neither family has been excluded under h=0. The local relations,
eight-point validity, and support separation are compatible, as the
controls prove. The missing step must use additional global doubling
closure or all singleton-base tree equations. Even excluding this
PURE-cone residual would not settle the other four core cones or
fresh quartic fibers having no coned triple.

## 5. Coverage audit for the proposed targeted closure check

This audits the mathematical coverage of a proposed finite-presentation
check, not its implementation or execution results.

The 56 formal differences span rank three because the points a,d,u
occur relative to zero. Given integer relation rows of rank less than
three, choose a nonzero integer functional f annihilating their rational
span. Signed symmetry of the differences implies M=max_D f(D)>0.
Choose D attaining M. For every formal difference E one has

    f(2D-E) >= M > 0.

Thus each of the 56 possible next closure equations 2D-E=0 raises the
rational rank. Every actual h=0 realization satisfies at least one
of them, so exhaustive branching to depth three covers that realization
by a full-rank integer matrix. Its generated cyclic subgroup has order
dividing the absolute determinant.

Two implementation conditions are essential for this coverage:

* The determinant itself need not be odd or at most 2187. The actual
  subgroup order is an odd divisor in the independently established
  range 188<=|H|<=2187. Matrices with even or larger determinant must
  retain all eligible odd divisor orders.
* Rational row reduction may choose f but cannot silently replace
  integer relation lattices. Dividing a row by an odd gcd can discard
  legitimate torsion solutions. Use raw integer rows, unimodular integer
  transformations, or certified integer row-lattice equivalence.

A time-capped prefix cannot certify exclusion. A complete zero-survivor
run would be a computational exclusion, with coverage established by
the argument above and solver dependencies stated separately.

The saved `stage13_pure_cone_closure.py` implementation was subsequently
read in full, together with its reused local kernel routine. It follows
these coverage conditions: exact 56-vector support; rank-increasing
branching; only power-of-two row divisions; exact sorted-row dedup;
verified determinant/adjugate embedding; all eligible odd divisors;
primitive local kernel orbits combined by CRT; explicit point, pair,
doubling-closure and degree-eight validity filters. No missing branch
was found in this code audit. This is not an independent numerical
rerun of the solver.

The deadline is cooperative, checked in traversal, divisor/map loops
and validity loops. Factoring or one local kernel call can overrun
the deadline before the next check; the cap is not a preemptive
wall-clock termination. The complete flag nevertheless requires
exhaustion of the full two-family traversal, not passing a prefix.

## 6. Consolidation-only elementary exclusion of doubled-center cones

After the focused computation, an adjacent local consequence was
audited without any new computation or search. It refines the next
checkpoint but does not alter the computational dependency of I/II.

Suppose a fresh NONPURE core cone has t in {a,b,d,e} and its isolated
ordinary vertex satisfies 2u+v+w=t. All three ordinary support points
are outside the five-point core. Write the unique doubled difference
2u=r-s. Then, explicitly padding the right side with zero,

    r+v+w = 0+t+s.

If the left were squarefree, validity would force multiset identity.
But its two outside-core points v,w cannot both occur among 0,t,s,
since only s could be outside the core. Thus the left repeats, and
r belongs to {v,w}. The right cannot now be squarefree, because it
equals a repeated triple. As 0 and t are distinct, s is 0 or t.
If s=0 then 2u=0+r, a forbidden pair equality on distinct points.
Therefore s=t. Swap the two tails to arrange r=v; consequently

    v=2u+t,       w=-4u.

If t=a or t=d, let B_t be its displayed singleton core partner, so
0=2t+B_t. The difference equation then gives

    2u+0 = t+B_t+v.

The right is a squarefree triple, with t,B_t in the core and v outside;
the left repeats u. Validity contradicts this equality. Thus the
two doubled-center core cones have connected entire quartic fibers,
elementarily using the Stage12 residual-shape theorem and h=0.
No uniqueness of other pure partners was assumed.

Only singleton tails t=b or e remain among nonpure core cones.
After swapping the two displayed pure partners, their residual formal
family is precisely

    III: (0,a,-2a,d,-2d,u,2u-2a,-4u).

No computation of III was performed this round, and this reduction
does not exclude III. Even exclusion of III would not by itself
settle fresh quartic fibers coning no triple or global D=0.
