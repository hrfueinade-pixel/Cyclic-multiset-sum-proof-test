# Stage 14: closing singleton triple cones, not the full quartic bridge

Date: 2026-10-10. One focused continuation of the Stage 13 checkpoint.
The previous round was progress: it closed the pure and doubled-center
cones and saved an exact singleton residual. This round checks that
residual alone. No Lean, random sampling, all-modulus sweep, or rerun of
a completed historical check was performed. No novelty is asserted.

## 1. Proved result and exact boundary

**Computer-assisted proposition.** Let A be a valid eight-point set in
its odd cyclic difference-generated subgroup H with h=0. If

    Y=3z=2a+b=2d+e,
    P={z,a,b,d,e}, |P|=5,

then the entire repeated quartic fiber at Y+b (and likewise Y+e) is
connected by cubic propagation.

The proof combines the elementary reduction below with a COMPLETE
targeted finite calculation. It is NOT an elementary exclusion or a
formal certificate. The program shares BOTH the Stage 13 relation
generator and the Stage 10 prime-power kernel implementation. The
challenger audited the reduction and code, not an independent full run.

**Corollary.** Under those hypotheses, every quartic fiber obtained
by coning a cubic fiber of at least three marks is connected, including
its ENTIRE propagation fiber, not just its displayed cones.

For a no-pure triple use Stage 12 Proposition A. For a one-pure triple,
Stage 12 handles the three outside-core cones, Stage 13 handles the
pure cone computationally and two doubled-center cones elementarily,
and the new proposition handles its two singleton cones. Stage 9
excludes two pure marks in one cubic fiber. If there are at least four
marks, choose three nonpure marks and again use Stage 12 Proposition A.
Thus this corollary does NOT depend on the Stage 10 numerical exclusion
of four-way fibers. The shared kernel implementation is a distinct
computational dependency, which remains explicit.

This does NOT exclude cubic triples themselves, does NOT prove R3=0,
and does NOT prove D=0. Fresh quartic fibers coning no cubic triple
remain open. Even D=0 would still leave regular Sigma>=53 and h>0 for
the original |E4|>=60 at N<248 / N>=248 target.

## 2. Definitions and elementary reduction

Validity means the all-ones multiset is the unique eight-term multiset
drawn from A with sum sum(A). It implies that a squarefree k-term
multiset, k<=8, cannot equal a different k-term multiset: add the
complementary points of A. Pair sums are unique; in odd H all 56
nonzero ordered differences are unique. Put

    Delta=(A-A)\{0}, h=|{d in Delta:2d not in Delta}|/2.

Thus h=0 means doubling permutes Delta. Cubic marks are the 64 distinct
multisets 2p+q. The propagation graph has the 260 distinct repeated
quartic multisets as vertices and edges obtained by coning equal
repeated cubics with a common point. A fiber is fresh if its induced
graph is disconnected; D is the sum of its component excesses.

The audited Stage 12 support/type reduction is elementary, using
Stage 9's order-three exclusion. Any fresh core cone of the displayed
one-pure triple has exactly two components: one with support union P
and one isolated ordinary vertex 2u+v+w on its three-point complement.
This uses ENTIRE support unions and does not assume no other available
cubic partners. Deleting a shared point from equal repeated quartics
gives repeated cubics, since a squarefree deletion would contradict
validity. Consequently distinct components have disjoint support unions.

Translate z to 0 and suppose the singleton cone at b is fresh. Then

    b=-2a, e=-2d, b=2u+v+w,
    A={0,a,b,d,e,u,v,w}, all eight points distinct.

Write 2u=r-s using h=0. Its substitution gives the degree-three equality

    r+v+w=0+b+s.

If r is neither v nor w, the left is squarefree and cannot be the same
multiset as the right: v,w are both outside the core, whereas only s
could be outside on the right. Validity therefore forces r=v or w.
The right side must now repeat, so s is 0 or b. If s=0, then 2u=0+r
contradicts the squarefree-pair replacement rule. Hence s=b. Swap v,w
to arrange r=v. It follows that

    v=2u+b, w=-4u,
    III: A=(0,a,-2a,d,-2d,u,2u-2a,-4u).

The cone at e reduces to the same presentation by swapping the two
displayed pure partners. No odd integer was divided out, no distinct
partners were assigned distinct free points, and no incompatible
choices or partner-uniqueness hypothesis were introduced.

The ordinary value here is b, NOT 0. The Stage 13 I/II output cannot
exclude this presentation; a new III calculation was required.

## 3. Independently justified bounds for the targeted check

At h=0 the 28 unordered center pairs yield exactly 28 unordered cubic
collisions. If m_y is a cubic fiber size and
R3=sum_y binomial(m_y-1,2), then

    |T3|=64-28+R3=36+R3.

At any fixed center p, if k_p marks are unpaired, counting its seven
other-center incidences gives

    k_p=1+sum_(paired marks at p)(m_y-2).

Isolation of 2u+v+w means 2u+v and 2u+w are both unpaired: coning any
different partner would create a neighbor. Hence k_u>=2 and u lies
in some cubic fiber with at least three marks. That fiber is different
from the original one at 0, since a mark at u in the original fiber
would cone into the core component and enlarge its support beyond P.
Thus R3>=2, without using Stage 10's four-way exclusion.

For completeness, cubic packing gives |H|>=184+2R3. Translate 0 into A,
let S be the 128 distinct subset sums of A\{0}, and s=sum(A). Validity
gives T3 intersect S=A by padding at zero: a subset with at least two
nonzero terms would give a squarefree replacement after equalizing
lengths. Hence E3=T3\A has 28+R3 elements. Also s-S=S, so S and s-E3
are disjoint. Two E3 cubic representations summing to s, padded by two
zeros, would violate eight-term validity. Thus S,E3,s-E3 are disjoint
and |H|>=128+2(28+R3)>=188.

The upper bound |H|<=2187 is the general singleton-base tree bound,
not a regular R3=0 assumption. At a fixed base t, doubled-difference
uniqueness supplies seven distinct center edges from the seven other
labels. An undirected cycle, summed with traversal signs, gives a
nonzero balanced relation with coefficients +/-1 at its distinct
labels and only the coefficient at t potentially larger. Choose its
sign to make all negative coefficients at least -1. Adding all ones
would give a rival valid-length multiset. Thus the seven edges form
a tree. With t translated to 0 and its seven other differences bvec,
the equations are (I-2U)bvec=0, where U is its reduced oriented
incidence matrix in label order. Every minor of U is 0 or +/-1:
expand along a row with at most one nonzero; otherwise the rows have
two opposite nonzeros and row sums give dependence. Principal-minor
expansion bounds the odd nonzero determinant by

    |det(I-2U)|<=sum_(S subset [7])2^|S|=3^7=2187.

The adjugate annihilates all seven generating differences. Since H
is cyclic, its order divides this determinant. Therefore a fresh III
image must have odd 188<=|H|<=2187. These are proved necessary bounds,
not bounds inferred from failed sampled examples.

## 4. Finite coverage and what the check can prove

Before execution the proposed finite statement was specified as:

    No eight-distinct Sidon image of III has doubling-closed Delta
    in an odd cyclic subgroup of order 188..2187.

This is sufficient for the singleton proposition. It is not an
assertion that all formal III images are valid, nor a search over
every modulus for arbitrary eight-point sets. No freshness filter
is used to prune the enumeration; actual fresh images are a subset
of the checked necessary-condition images.

The eight points are fixed integer vectors in coordinates (a,d,u).
Their 56 formal ordered differences are distinct (asserted by the
program), symmetric under sign, and span Q^3 since a,d,u occur relative
to zero. Given relation rows of rational rank less than three, choose
a nonzero integer functional f annihilating their span. Let D maximize
f on the formal differences and M=f(D)>0. Doubling closure in a group
realization requires 2D=E for one of ALL 56 formal differences E.
For every such branch,

    f(2D-E)>=M>0,

so the new row increases rational rank. After three steps the matrix
has nonzero determinant. Every possible doubling-closed realization
appears on some branch. Only powers of two, signs, and row order are
normalized, all harmless at odd order; no odd gcd or rational-rowspace
identification is used to discard a torsion possibility.

Because a,d,u generate H, its odd order divides the determinant.
The program retains ALL its odd divisors in the independent range;
the determinant itself can exceed 2187 or be even. The matrix is
embedded as diag(M,1) for the shared kernel solver. That solver
enumerates primitive local kernel vectors modulo each prime power,
up to units, using elimination and digit lifting (or a unit cofactor
when rank is three). Independent local unit scalings are one global
unit by CRT. All vectors are checked against the rows and for gcd=1.
The fourth coordinate is forced zero. This covers generating cyclic
parameter images, not just adjugate images at low rank.

Filters check eight distinct points, all 36 unordered pair sums, and
EVERY doubled nonzero difference. Surviving images would undergo all
6435 eight-term multiset checks. None passed closure, so that final
loop was not invoked. Neither the proposed D=0 goal nor the conjectured
248 bound is used as a rejection criterion.

## 5. Reproduction, actual counts, and audit limits

Run with standard-library Python:

    python stage14_singleton_cone_closure.py --cap 30

Keep stage13_pure_cone_closure.py, stage10_modular_audit.py, and
stage10_fourway_templates.py beside it. Imports run no old searches.
The wrapper calls ONLY check_family("III",...) after defining III.

Recorded output: stage14_singleton_cone_results.json.
Status: COMPLETE, about 6.343 seconds under a cooperative global
30-second cap. Factorization or a single local kernel call is not
preempted; serialization is outside the checked deadline. There is
no live computation left. No historical I/II enumeration was rerun.

| Count | III |
| --- | ---: |
| Complete full-rank matrices | 154788 |
| Derived divisor-order incidences | 41859 |
| Cyclic quotient maps up to units per matrix | 40166 |
| Distinct recorded images | 36999 |
| Repeated-point images | 598 |
| Pair-sum failures | 21695 |
| Sidon images | 14706 |
| Sidon images failing doubling closure | 14706 |
| Doubling-closed images | 0 |

Matrix traversal SHA256:

    e89b96e4f654864b3afabfe341c136041c7cc44b6e948c617a03deca19c3adae

These counts are fixed-presentation maps. They are NOT a census of
valid sets, affine-equivalence classes, or independent structural
families. Matrix-specific unit normalization may leave equivalent
images with different recorded parameters. There were no valid h=0
survivors, and no degree-eight validity checks were needed.

The independent challenger read the reduction, subgroup bounds, new
wrapper, shared generator/kernel, and completion semantics. This is
a mathematical/implementation audit, not a numerical rerun or an
independent structural generator. This finite-computation dependency
must remain attached to both the proposition and corollary.

## 6. Elementary controls and the remaining bridge

The challenger constructed the valid non-h0 control

    A=(0,33,-66,1089,-2178,1,-64,-4), modulo 26137.

Its fresh quartic value is b=-66. It has 4 in Delta but 8 not in Delta.
Its complete elementary validity and exact fiber proofs are saved in
stage14_challenger_findings.md. It shows why the formal singleton
relations plus validity alone cannot exclude the obstruction. It is
NOT a counterexample to h=0=>D=0 or to the 248 target. No new numerical
fixture check is represented as having been run.

Once triple cones are connected, a fresh quartic fiber has only
pair-shadow edges. Its local graph has degree at most two, but the
GLOBAL unpaired-center/singleton permutation from Stage 8 still does
not follow: an isolated ordinary vertex can have two unpaired marks
because its center participates in a multiway cube elsewhere. The
mere existence of that other cube does not put its cone at this value.
The focused alternative-route analysis is saved separately in
stage14_alternative_findings.md. Its complete elementary conditional
proof localizes Stage 8 without importing the global regular permutation:

**Local-defect theorem.** Assume every multiway cubic cone has a
connected entire quartic fiber (MC). For a fresh quartic fiber X, let
U(X) be the SET of unpaired repeated cubic multisets obtained by
deleting one point from a repeated quartic at X. Then X contains
either an isolated ordinary vertex or two DISTINCT marks in U(X)
with the same singleton label.

Here 'distinct' means distinct literal multisets, not two occurrences
of the same cubic in different quartic deletions. The proof assumes
neither global R3=0 nor a chosen unique partner. Under MC all cubic
shadows at X have at most two marks; hence the local graph has degree
at most two. If X had no isolated ordinary vertex and singleton labels
were injective on U(X), the Stage 8 support/type proof applies locally:
fresh 31/31 is excluded using that local injectivity; all-ordinary
components need at least six points; the remaining ordinary/ordinary
cases give the sixteen exact algebraic contradictions and the exhausted
order-five coset calculation. Finally pure, 22, and 31 alternatives
are excluded by those support bounds and squarefree replacements.
The alternative note supplies every case and its complete proof.

For a center defect the incidence identity in Section 3 gives k_p>=2
and hence a multiway cubic mark at p elsewhere. The same identity
holds for each fixed singleton q: doubling bijects the 28 center pairs
and singleton pairs, so seven other-label incidences give

    k_q=1+sum_(paired marks with singleton q)(m_y-2).

A singleton defect therefore also forces a multiway fiber. Its value
is not specified by the identity. The UNPAIRED deletions at X cannot
themselves be members of this forced multiway fiber. Cone connectivity
therefore supplies no contradiction without an additional transport
argument. This is a precise gap, not a valid counterexample or a
refutation of h=0=>D=0.

**Stronger elementary nontransport restriction.** If X=2a+b+c is
isolated, NO paired cubic mark centered at a can cone to X. Indeed
X=(2a+q)+t implies b+c=q+t. Pair uniqueness forces {q,t}={b,c},
but both marks 2a+b and 2a+c are unpaired by isolation. Thus in the
center-defect case transporting the multiway cube forced at that
same center is impossible, not merely unproved. Any successful
same-value transport must find a DIFFERENT center, or exclude the
defect directly. The challenger independently audited this proof.

**Single most useful unresolved lemma (defect transport).** In the
current odd h=0 setting, a center or singleton defect of a fresh quartic
fiber X forces a multiway cubic value Y and a point t in A with
X=Y+t. Combined with MC and the local-defect theorem, this would prove
D=0. It is proposed, NOT proved or tested. Directly prohibiting both
local defects would also suffice. The one-pure shape remains possible
as a cubic fiber globally, but none of its cones is fresh.

## 7. Dependency ledger

| Claim | Status |
| --- | --- |
| Even H branch D=0 | Earlier elementary Stage 6, unchanged |
| Odd h=R3=0 branch D=0 | Earlier elementary Stage 8, unchanged |
| No order-three difference; at most one pure cubic per fiber | Earlier elementary Stage 9 |
| Four-way exclusion | Earlier Stage 10 finite computation, NOT needed as an exclusion for the new corollary |
| No-pure triple cones and one-pure support residual | Earlier elementary Stage 12, audited where used |
| Pure cone connected | Stage 13 complete finite computation, shared kernel |
| Doubled-center cones connected | Stage 13 elementary |
| Singleton reduction III; subgroup bounds and finite coverage | Elementary arguments above |
| Singleton cones connected | NEW COMPLETE finite computation plus coverage; shared generator/kernel, no independent execution |
| Every cubic multiway cone has connected ENTIRE fiber | Corollary, retaining Stage 13/14 computational dependencies |
| Valid non-h0 III control | Elementary challenger proof, not a valid h=0 counterexample |
| Local-defect theorem | Elementary CONDITIONAL on MC; complete alternative proof |
| Defects force multiway cubics somewhere | Elementary incidence identity, NOT same-value transport |
| Isolated ordinary forbids same-center paired-cubic transport | Elementary this round, proof above and independent audit |
| Same-value defect transport | OPEN, proposed sufficient lemma; not numerically tested |
| Fresh quartic fibers coning no multiway cube | OPEN |
| h=0=>D=0 | OPEN |
| Original E4-size >=60 at N<248 | OPEN; Sigma>=53 and h>0 still remain even after D=0 |

## 8. Stopping point and delivery

One focused round is complete. Do not rerun III as if still open or
expand its enumeration; the next obstacle is transport in a fresh
pair-shadow quartic fiber, not another one-pure cone role. All invoked
processes finished. The original goal remains active and unproved.

The local directory is not a Git checkout and has no configured local
remote. The intended private the source research archive repository is
available through the GitHub connector. Stage 13 PR3 was inspected as
open/unmerged; this round is delivered as a separate PR stacked on its
head, preserving unrelated archive entries. No PR is merged.
