# Stage 13: computer-assisted exclusion of the fresh pure cone

Date: 2026-10-10. One bounded goal-continuation round from Stage 12.
The previous turn made proved progress; this round targets its exact
pure-cone residual, not a restart or a new all-modulus search.

## 1. Result, scope, and proof boundary

**Computer-assisted proposition.** Let A be a valid eight-point set
in its odd cyclic difference-generated subgroup H, with h=0. Suppose

    Y=3z=2a+b=2d+e,
    P={z,a,b,d,e}, with five distinct points.

Then the entire repeated quartic fiber at Y+z=4z is connected.

The elementary reduction and coverage proof below, together with the
complete finite calculation in stage13_pure_cone_results.json, establish
this proposition with an explicit computational dependency. It is NOT
an elementary exclusion, a Lean/formal certificate, or a literature
novelty claim. The independent challenger audited the implementation
and mathematical coverage but did NOT independently rerun the enumeration.
The primary calculation reuses the previously audited prime-power
kernel routine from Stage 10. Its structural generator is new.

This does not exclude the one-pure cubic triple. Stage 12 already
connects its three outside-core cones. This stage connects its pure
core cone computationally and its two doubled-center cones t=a,d
elementarily. Only the singleton cones t=b,e remain open among its
eight cones, as do fresh quartic fibers containing no coned triple.
Neither h=0 => D=0 nor the original |E4|>=60 / N>=248 target is proved.

## 2. Audited elementary reduction to exactly two families

Suppose the pure cone is fresh. Stage 12's support/type proof gives
exactly two components: the five-point core and an isolated ordinary
vertex 2u+v+w on its three-point complement. Translate z to zero.
Then

    A={0,a,b,d,e,u,v,w},
    b=-2a, e=-2d, 2u+v+w=0.

All eight points are distinct. Any additional mark in the ORIGINAL
cubic fiber at zero would cone into the core component and enlarge
its support beyond five, which is impossible. This excludes extra
partners of 3z in this fresh configuration, not extra partners of
other pure cubics.

Write the unique doubled difference 2u=r-s. Substitution in the
ordinary equality gives r+v+w=s. Its left triple must repeat,
so r is v or w. Pair uniqueness excludes s=0,v,w. For either
pure partner 0=2p+q, the option s=p would give

    2u+0=p+q+r,

whose right triple is squarefree across the separated supports.
Thus s cannot be either doubled center a or d. Therefore
r in {v,w} and s in {u,b,e}. Swap v,w to set r=v; swap the
two pure partners to identify s=e with s=b. This leaves precisely:

    I:  (0,a,-2a,d,-2d,u,3u,-5u);
    II: (0,a,-2a,d,-2d,u,2u-2a,2a-4u).

No division by an odd integer, assumption of partner uniqueness,
or choice incompatibility occurs. These are formal rank-three
presentations. Actual eight-distinct valid images still have to satisfy
the global h=0 conditions. The independent reduction audit is in
[stage13_challenger_findings.md](stage13_challenger_findings.md).

## 3. Independent subgroup bounds used in the check

### 3.1 Lower bound |H|>=188

For every center u, h=0 gives seven collision incidences, one with
each other center. Marks in one cubic fiber have distinct centers.
A mark in a fiber of size m accounts for m-1 incidences. If k marks
at u are unpaired, the eight available labels give

    k = 1 + sum_(paired marks at u) (m-2).

The isolated ordinary vertex has both 2u+v and 2u+w unpaired. Hence
k>=2, forcing a multiway cubic fiber at u. It is distinct from the
original fiber: an original-fiber mark at u would cone into the core
component, enlarging its support beyond P. Thus R3>=2, with no use
of Stage 10's four-way exclusion.

At odd h=0, the 64 cubic marks have exactly 28 unordered pair
collisions, since doubling permutes the 56 distinct ordered differences.
Consequently

    |T3|=64-28+R3=36+R3.

After translating zero into A, T3 meets the subset sums S exactly in A,
and S, E3=T3\A, s-E3 are disjoint by squarefree replacement and padding
two cubics with two zero terms. Since |S|=128,

    |H|>=128+2(28+R3)>=188.

This is the earlier elementary cubic packing bound, not an inference
from any absence of sampled sets.

### 3.2 Upper bound |H|<=2187

For each singleton base t, its seven label pairs give equations
2p+t=2q+r with distinct center edges and distinct labels r!=t.
An undirected cycle, summed with traversal signs, gives a nonzero
balanced relation whose label coefficients are +/-1 and whose only
possibly larger coefficient is at t. Choose its sign so all negative
coefficients are at least -1; it contradicts validity. The seven edges
therefore form a spanning tree. This does not require R3=0.

Translate t to zero. In label order, let U contain its seven reduced
oriented incidence rows. Then (I-2U)b=0 for the seven point differences.
Every square minor of U is 0 or +/-1: expand along a row with at most
one nonzero entry, or, if all rows have two opposite entries, use the
zero row sums. Expanding the determinant by principal minors gives

    det(I-2U)=sum_S (-2)^|S| det U[S,S].

It is odd, nonzero, and has absolute value at most 3^7=2187. Its
adjugate annihilates all generating differences. Because H is cyclic,
its ORDER divides that determinant. This is Stage 5 Corollary 2a,
rechecked here without the regular singleton-permutation hypothesis.

Thus any actual fresh pure-cone image has odd 188<=|H|<=2187.

## 4. Complete coverage of the targeted finite check

This was stated before execution as a proposed check of only the two
presentations, with a cooperative 30-second global deadline. A timeout
would certify only a prefix. No modulus interval was swept: subgroup
orders arise only as divisors of generated presentation determinants.

For each family, write its points as the eight integer vectors in
coordinates (a,d,u), and Delta_form for its 56 ordered difference
vectors. They are distinct and span Q^3, since a,d,u occur relative
to zero. This cardinality is asserted in the script, not assumed from
a potentially colliding group realization.

Given independent integer relation rows R of rank less than three,
choose a nonzero integer functional f annihilating their rational
span. Signed symmetry gives M=max_D f(D)>0. Choose D attaining M.
If doubling closure holds in a cyclic realization, then 2D equals
some E in Delta_form modulo H. Branch over every such E. For all E,

    f(2D-E)>=M>0.

Every branch therefore raises the rational rank. After three relations,
the generated 3x3 integer matrix has nonzero determinant. Every actual
h=0 realization lies on at least one branch, and its parameters obey
the corresponding integer rows.

Only a common POWER OF TWO is divided from a row; that is invertible
in every odd target group. Signs and row permutations are also harmless.
Deduplication compares exact resulting integer row matrices, not merely
their rational rowspace. No odd gcd is divided away and no torsion
possibility is silently lost.

The parameter images a,d,u generate H, so its order is an ODD divisor
of the absolute determinant. The determinant itself need not be odd
or at most 2187; the check retains all its odd divisors in the independently
proved range. Each matrix is embedded as diag(M,1) solely to reuse the
four-coordinate local kernel routine; the fourth parameter is forced zero.

For each derived order, the routine computes primitive kernel vectors
at every prime power, modulo multiplication by units, and combines
them by CRT. Its coverage is standard exact Gaussian elimination modulo
p followed by digit lifting: normalize the first unit coordinate to one,
enumerate all affine solutions for the next digit while fixing that
coordinate, and repeat. If a cofactor is a unit modulo p, the kernel
has one primitive unit orbit, obtained from that adjugate column.
Independent local unit normalizations combine to a global unit by CRT.
Every vector is checked against the rows and gcd(order,parameters)=1.

Every image is filtered by eight distinct points, 36 distinct pair
sums, and ALL 56 doubled differences belonging to Delta. A surviving
image would receive direct degree-eight multiset verification. There
were no doubling-closed images, so that last validity loop was never
needed. No rejection uses the proposed goal as a premise.

This establishes mathematical coverage of the exact finite program.
It is still a computational proof dependency, not an elementary
enumeration-free theorem or a separate formal verifier.

## 5. Execution, counts, and audit limits

Run:

    python stage13_pure_cone_closure.py --cap 30

Default result:
[stage13_pure_cone_results.json](stage13_pure_cone_results.json).
The program imports `factors` and `local_projective_kernel` from
stage10_modular_audit.py; that in turn imports the Stage 10 structural
template module. No historical template search is executed on import.
These dependencies must remain beside the script for reproduction.

Status: COMPLETE for BOTH families, about 15.89 seconds total under
the checked 30-second deadline. No computation remains running.
The deadline is cooperative: traversal, divisor/map generation, and
validity loops check it, but a single factorization or local kernel
call is not preempted. Output serialization is outside that deadline.

| Count | Family I | Family II |
| --- | ---: | ---: |
| Complete full-rank matrices | 160424 | 157834 |
| Derived divisor-order incidences | 80668 | 42148 |
| Cyclic quotient maps up to units per matrix | 75372 | 40559 |
| Distinct images after recorded-map deduplication | 65451 | 37393 |
| Repeated-point images | 1619 | 550 |
| Pair-sum failures | 41615 | 22970 |
| Sidon images | 22217 | 13873 |
| Sidon images failing doubling closure | 22217 | 13873 |
| Doubling-closed images | 0 | 0 |

The numbers are fixed-presentation candidate maps, not a census of
valid eight-element cyclic sets. Different images can remain unit-
equivalent because normalization can depend on their matrix; these
are not asserted to be affine equivalence classes. No new valid h=0
set was found, and no degree-eight validity loop was run.

The challenger independently audited reduction, rank coverage,
power-of-two normalization, determinant bounds and eligible divisors,
kernel/CRT coverage, filters, and completion semantics. No gap was
found. That is an implementation/read audit, not an independent full
execution. The kernel implementation is shared with earlier checks;
the present zero-survivor exclusion retains that explicit dependency.
Prior Stage 10/11/12 completed numerical checks were not rerun.

## 6. Additional elementary progress and non-h0 controls

The alternative-route researcher proved smaller restrictions without
computation, preserved in
[stage13_alternative_findings.md](stage13_alternative_findings.md):

* In I, additional partners of 3u must be 2b+e,2e+b,2w+b,or2w+e;
  at most one exists. Its fiber has at most three marks elementarily.
  The mark 2u+0 cannot be multiway.
* In II, the forced fiber v=2*0+v=2u+b is exactly a pair.

These exclude selected roles elementarily, not both families by themselves.
The note's remaining-role statements describe that elementary route's
boundary; the complete finite computation above separately closes the
fresh PURE-cone configuration, not every occurrence of either relation
family when its stated hypotheses are dropped.

The challenger supplied complete ELEMENTARY proofs that both families
can be valid and have a fresh pure quartic fiber without h=0:

    I:  (0,41,-82,1681,-3362,1,3,-5), modulo 40345;
    II: (0,33,-66,1089,-2178,1,-64,62), modulo 26137.

No numerical rerun was needed. An eight-term lift-sum interval has
width N-1, so no wrap is possible; base-R coefficient comparisons
and a slot count force all counts to one. The quartic fiber at zero
has exactly the three connected core vertices and the isolated ordinary.
Both have 2 in Delta but 4 not in Delta. These are explicit valid
h>0 controls, NOT counterexamples to any h=0 theorem or to 248.
They show precisely why validity and the local equations alone do
not suffice: global doubling closure is essential.

### Elementary exclusion of doubled-center cones

Normalize z=0. Suppose a NONPURE core cone t in {a,b,d,e} is fresh.
Stage 12 gives the disjoint core P={0,a,b,d,e} and an isolated ordinary
vertex 2u+v+w=t on F={u,v,w}. By h=0 there are r,s in A with
2u=r-s. Consequently

    r+v+w = 0+t+s.

We use the elementary consequence of validity that a squarefree
k-term multiset cannot equal a different k-term multiset for k<=8:
adding the complementary points would contradict eight-term validity.
If r is not v or w, the left side is squarefree, and cannot be the
same multiset as the right side: v,w are both outside P, whereas the
right side has two distinct points 0,t in P and at most one outside.
Thus r is v or w. The left side now repeats, so the right side must
repeat too, giving s in {0,t}. The possibility s=0 would give
2u=0+r, a forbidden replacement of a squarefree pair. Hence s=t.
Swapping v,w when necessary, we have

    v=2u+t, w=-4u.

For t=a or d, the displayed pure-cubic partner is 0=2t+B_t,
where B_a=b and B_d=e. Therefore

    2u+0 = t+B_t+v.

The right side is squarefree: t,B_t are distinct core points and v
is outside P. The left side is a different multiset. Validity rules
out this equality. The doubled-center cones t=a,d therefore have
connected ENTIRE quartic fibers, elementarily. No uniqueness of
other available cubic partners was assumed, and no Stage 10 numerical
exclusion or Stage 13 computation was used for this result.

For the remaining singleton cones, swap the two displayed partners
to take t=b=-2a. The same argument leaves exactly the necessary family

    III: (0,a,-2a,d,-2d,u,2u-2a,-4u).

Its ordinary quartic value is b, NOT zero. It is not family II:
their final coordinates differ. No computation of III was performed
this round. These equations alone do not certify a valid h=0 set.

## 7. Dependency ledger and next checkpoint

| Claim | Status |
| --- | --- |
| Even H branch D=0; odd h=R3=0 branch D=0 | Earlier elementary Stages 6 and 8, unchanged |
| No order-three difference | Earlier elementary Stage 9, used by Stage 12 support/type reduction |
| Four-way cubic fibers excluded | Earlier finite computation Stage 10, unchanged and not required as an exclusion here |
| No-pure triple cones connected | Elementary Stage 12, unchanged |
| Fresh one-pure cone residual and R3>=2 | Elementary Stage 12, reconstructed where used |
| Two-family pure-cone coverage; subgroup bounds | Elementary proofs above |
| Fresh PURE one-pure cone excluded | NEW COMPLETE finite computation plus coverage; shared kernel implementation, no independent full rerun |
| Family I/II additional partner-role restrictions | Elementary this round |
| Both explicit valid non-h0 controls | Elementary this round, not inferred from testing |
| Doubled-center cones t=a,d connected | Elementary this round, using Stage 12 support reduction |
| Singleton cones t=b,e, necessary family III | OPEN; elementary reduction, not numerically tested |
| Fresh quartic fibers containing no coned triple | OPEN |
| h=0 => D=0 | OPEN |
| |E4|>=60 at N<248 | OPEN; regular Sigma>=53 and h>0 remain even after D=0 |

**Single most useful next lemma:** a fresh SINGLETON cone at Y+b
cannot have the five-point one-pure core component and an isolated
ordinary vertex on its three-point complement in odd h=0.

After translating z=0 and swapping the two displayed pure partners,
the exact remaining necessary presentation is

    0=2a+b=2d+e,
    b=2u+v+w,
    A=(0,a,-2a,d,-2d,u,2u-2a,-4u).

All eight points must be distinct, the five-point core component
and three-point ordinary support must be disjoint, and the ENTIRE
quartic fiber at b must be disconnected as specified by Stage 12.
The forced extra multiway cubic gives R3>=2. Global doubling closure
and validity are still required. The proved subgroup bounds would
again be 188<=|H|<=2187. A later targeted check must justify coverage
for III itself; the I/II computation does not apply to it.

The pure and doubled-center roles are closed with the dependencies
recorded above. Neither the whole one-pure shape nor global D=0 is
proved. This round saves a stopping point without computing the
singleton presentation. No novelty assessment was performed.
