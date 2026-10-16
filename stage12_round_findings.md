# Stage 12: partner reuse and a local multiway quartic bridge

Date: 2026-10-10. One focused round from the Stage 11 checkpoint,
with the main researcher, an independent challenger, and an
alternative-route researcher. No new research stage was started.

**Status:** neither h=0 => D=0 nor the original |E4|>=60 target is
proved. Both three-way shapes remain possible on the evidence here.
The substantive gain is a proved local bridge: every quartic cone
of a no-pure cubic triple has a connected ENTIRE quartic fiber.
No claim of literature novelty is made.

## 1. Scope, definitions, and baseline audit

A is valid if the all-ones multiset is the unique eight-term multiset
from A summing to s=sum A. A squarefree sum of degree at most eight
therefore cannot have a different equal-length multiset representation:
pad that replacement with its complement in A. Equivalently, a nonzero
balanced integer relation on the eight points with all coefficients
at least -1 is forbidden; adding one to each coefficient gives a rival.

Translate into the difference-generated cyclic subgroup H. In this
round H is odd and h=0, where h is half the number of ordered
nonzero differences whose doubles are missing. Thus 2Delta=Delta.
Pair sums and all 56 ordered differences are unique. Repeated cubic
marks are 2a+b, including 3a; repeated quartics have types 4,31,22,211.
An edge of the quartic propagation graph cones a repeated cubic
equality by a common point. Write K for its component count and
D=K-|T4|. Write R3=sum_y binomial(m_y-1,2) for cubic fiber multiplicities.

The checkpoint and Stages 8-11 were read before new work. Where used,
support separation, pure pairing, the local 31/31 and 22/31 lemmas,
ordinary-center exclusion, and the tree obstruction were reconstructed
from validity rather than accepted solely from summaries. Stage 11's
all-B argument was checked for its quantifier, not rerun computationally.
Stage 9's order-three exclusion remains an explicitly cited elementary
dependency. Stage 10's four-way exclusion remains computational, and
its kernel audits share structural generators. Completed prior checks
were not rerun. This is not an independent recertification of all
historical code or of the paper's computation.

The no-pure shape is

    Y=2ci+bi (i=0,1,2), B=Y-2C, A=C union B union {x,y}.

All eight points are distinct. The separate one-pure shape is

    Y=3z=2a+b=2d+e, P={z,a,b,d,e}, |A\P|=3.

Neither is excluded here. In particular a no-pure triple surviving
does not refute h=0 => D=0.

## 2. Strengthening Stage 11 without choosing unique partners

Every pure cubic has a partner by the singleton-base spanning tree.
Stage 11's ordinary-center argument shows every partner of 3ci is
2p+q with p,q distinct in B union {x,y}. The distinctness uses Stage 9
to exclude a pure partner 3p. For every partner set simultaneously:

1. At least one 3ci has NO B-only partner. Otherwise choose a B-only
   partner for each i, contradicting the complete Stage 11 all-B proof.
   Thus every partner of that particular cubic uses a free point.
2. If p=bj with j!=i, then q=bi. Compensation with the core equations
   gives ci+2cj-bi-bj-q=0; if q differs from bi,bj, its negative
   coefficients are at least -1. The pure possibility q=bj is excluded.
   Thus a free-singleton, B-doubled partner is exactly
   S_i(f): 3ci=2bi+f, or f=7ci-2Y.
3. If the same free point f doubles in partners of two different
   centers, both singleton labels are their own bi, and ci-cj has
   order five. A free point cannot double for all three centers:
   cyclic H has a unique order-five subgroup, so this would place
   three C-points in one coset, supplying six differences instead of four.
4. The same free point cannot occupy the S role for all three centers.
   The S equations would put C and B triples into order-seven cosets,
   supplying twelve distinct ordered differences in a subgroup with
   only six nonzero elements. This does NOT cover an M role plus two
   S roles, where M_i(f,g) denotes 3ci=2f+g with both points free.
5. At most one pure cubic can have ANY M partner. Its doubled free
   point cannot double in a partner of either other pure cubic.

Complete proofs and all-role caveats are in
[stage12_challenger_findings.md](stage12_challenger_findings.md).
These assertions quantify over all available partners. There is no
assumption that each cubic has a unique partner or that different
cubics must use different free points.

### A short complete proof of the free/free exclusion

Suppose two different centers have M partners. If they use the same
ordered free pair, then 3ci=3cj. Subtracting the core difference
2ci+bi=2cj+bj yields ci+bj=cj+bi, a forbidden squarefree pair equality.
If they use opposite pairs, say 3ci=2x+y and 3cj=2y+x, subtraction
gives x-y=3(ci-cj). The core gives bj-bi=2(ci-cj). Therefore

    ci+bj+y = cj+bi+x.

The six points are distinct, so these are different squarefree triples,
contradicting validity. This particular exclusion is entirely elementary
from the core and validity; it does not need Stage 9 or Stage 10.

For completeness, shared doubled f gives 3ci=2f+qi, 3cj=2f+qj.
If qi=qj, the same compensated squarefree pair contradiction applies.
Otherwise 3ci+qj=3cj+qi is a disjoint 31/31 equality. The local
order-five lemma gives ord(ci-cj)=5, hence
qi-qj=3(ci-cj)=-2(ci-cj)=bi-bj. Ordered-difference uniqueness forces
qi=bi and qj=bj. This applies to every possible partner pair. In
particular an M partner's doubled f cannot double for another center.

## 3. Precisely bounded symbolic check and its obstruction

Before execution, the proposed check was stated as follows: reject
a selected partner pattern only if it supplies a nonzero balanced
relation with all coefficients at least -1, a proved reuse obstruction,
or a violation among the known edges of one of ALL EIGHT singleton-base
trees. A survivor need not admit any cyclic realization, much less be valid.

The fourteen available formal choices per center are U_i(j), V_i(j)
(four B-only possibilities), S_i(f) (two), D_i(f,j):3ci=2f+bj
(six), and M_i(f,g) (two). One partner is selected per center solely
to audit simultaneous necessary conditions; no uniqueness is imposed.

For each of 3*14^2=588 pairs, the check forms all 27 combinations with
coefficients -1,0,1 of the two partner rows and the corresponding core
difference row. Every rejection saves the exact coefficient combination,
balanced relation, and nonnegative rival counts summing to eight.
Then all 14^3=2744 selected triples are checked against those certificates,
the elementary role restrictions, the Stage 11 all-B obstruction, and
the partial edges forced in every singleton-base tree:

    In T_bi: ci -> cj, label bj, for each j!=i.
    From 3ci=2p+q: in T_ci, ci -> p, label q;
                         in T_q, p -> ci, label ci.

Checks exclude duplicate labels or center edges, cycles, and edges
entering the base. They do NOT solve the missing simultaneous tree
equations or certify full doubling closure. Individual acyclic edge
patterns are only partial necessary trees.

Scope: no moduli, no random sampling, no set search. Runtime cap:
five seconds, including the enumeration but not output serialization.
Status: COMPLETE in about 0.109 seconds. Of 588 partner pairs, 195
have explicit short-relation certificates. Of 2744 selected triples:

| First rejection reason | Count |
| --- | ---: |
| Short balanced certificate | 1914 |
| One free point doubled at all three centers | 2 |
| One free point in the S role at all three centers | 2 |
| Stage 11 all-B selection | 10 |
| Additional partial-tree violation | 0 |
| Surviving selected patterns | 816 |

These are labeled partner choices, not group configurations or
inequivalent valid sets. Many are related by relabeling C or F. No
structural diversity of valid h=0 sets was added.

An explicit surviving necessary-choice configuration is

    3c0=2x+b0, 3c1=2x+b1, 3c2=2b2+x.

Here x doubles for two cubics and is singleton for the third; y is
not used by these selected partners. The first two force an order-five
center difference and their own singleton labels, exactly as proved.
All forced partial edges in the eight trees are listed in the result
file, and form forests. This defeats a simple free-point pigeonhole
argument, not the mathematical goal. It is NOT an actual valid set,
not a counterexample, and not a certificate of simultaneous full tree
completion. Extra partners and longer combinations of relations could
still exclude it. This round stops rather than enlarging that search.

Reproduce with standard-library Python:

    python stage12_partner_patterns.py --cap 5

Saved exact certificates, counts and completion status:
[stage12_partner_results.json](stage12_partner_results.json).

## 4. Direct bridge: the useful pivot

**Proposition.** Under odd h=0 and validity, for a no-pure core
Y=2c0+b0=2c1+b1=2c2+b2 with six distinct points, EVERY repeated
quartic fiber at Y+t, t in A, is connected. The proof has no Stage 10
computational dependency and does not require R3=0.

Here is the full support argument, with the local lemmas proved in
[stage12_bridge_findings.md](stage12_bridge_findings.md):

Equal repeated quartics sharing a point are adjacent: deleting that
point cannot leave a squarefree cubic, by validity. Thus different
components have disjoint entire support unions. Every pure cubic is
paired, because its singleton-base tree is connected and no edge
enters its base. Stage 9 excludes a pure partner, so every component
containing a pure quartic has at least three support points.

A disjoint 31/31 equality forces its center difference to have order
five: writing its doubled difference as u-v gives a cubic equality
whose two sides must both repeat; only u equal the left singleton and
v equal the right singleton survives. The center pair and singleton
pair exhaust all four nonzero differences of the order-five subgroup,
in different cosets. A disjoint 22/31 equality is impossible by the
local doubled-difference argument. A 31 component opposite another 31
has at least four points: cone any partner 3a=2p+q by its tail b.
Its points avoid the opposite component. q=b would make a forbidden
22; p=b would make another 31 whose center enters the exhausted
order-five center coset. Thus p,q are two new distinct points.

The component U containing the three cones has support containing
C union B union {t}. For t free, its support has at least seven
points, leaving at most one: no other component fits. For t=bi, U
contains a 22 and at least six points. A separated component on at
most two points can contain neither 4 or 22 (odd doubling and pair
uniqueness), nor 31 (disjoint 22/31), nor ordinary (three points).
For t=ci, U contains a 31 and at least six points. A separated pure
component needs three, a 22 is forbidden, an ordinary needs three,
and an opposite 31 component needs four. All cases are exhausted.
This proves connectivity of the entire fiber, even if U contains
additional vertices. It does not exclude the cubic triple. QED.

### Separate one-pure residual shape

The bridge note also proves: for the one-pure core P, outside-core
cones are connected. A fresh core cone must have exactly two components:
the core-five component and an isolated ordinary 2u+v+w on A\P.
Its marks 2u+v and 2u+w are unpaired. Seven center-collision incidences
then force a different multiway cubic fiber at center u, because

    unpaired_marks_at_u = 1 + sum_(paired marks at u) (m-2).

The second fiber is genuinely different: an original-fiber mark at u,
coned by t, would enlarge U beyond its exact five-point support.
Thus R3>=2 is ELEMENTARY. Only calling the second fiber exactly
three-way uses Stage 10. This is a restriction, not an exclusion.

## 5. One diagnostic, failed shortcuts, and limits

The independent challenger tested ONE fixed cyclic CRT candidate in
Z/3 x Z/1009 (modulus 3027), with a two-second cap, to challenge swapped
free/free partners. All 6435 eight-term multisets were checked;
the run completed below its cap and found three rivals. The saved
timer reads 0.0 seconds at its resolution; no sub-millisecond timing
accuracy is asserted.
It has unique pair sums and ordered differences and no order-three
difference, but h=21 and is INVALID. The squarefree triple identity
in Section 2 explains its failure. It is diagnostic evidence for
finding that identity, not a counterexample or an h=0 example.

    python stage12_challenger_checks.py

The script and [results](stage12_challenger_results.json) preserve scope,
cap, explicit rivals and completion status. New actual candidates: one;
new valid candidates: zero. Formal partner patterns are a different
count and must not be presented as actual candidates.

Failed or insufficient approaches:

* Distinct partners do not require distinct free points; the DDS pattern
  above survives the selected constraints, even reusing x in both roles.
* Reused S partners exhaust two order-seven pairs, but the remaining
  pair can be ANY of the six pairs among {c2,b2,x,y}; omitting b2 is wrong.
* Order-three torsion of a difference of sums is not an A-difference;
  Stage 9 cannot be used to exclude it. The explicit squarefree identity,
  not that shortcut, proves the swapped-M obstruction.
* The regular singleton permutation and degree-two propagation graph
  cannot be assumed when R3>0. Isolated ordinary vertices can occur in
  the necessary incidence framework and force multiway fibers elsewhere.
* Controlling cones of triples does not control every quartic fiber.
  Fresh fibers containing no coned triple remain unhandled.

## 6. Dependency ledger and the single next lemma

| Claim | Status and dependency |
| --- | --- |
| Even H branch D=0 | Earlier elementary Stage 6; unchanged |
| Odd h=R3=0 implies D=0 | Earlier elementary Stage 8; unchanged |
| No order-three A-difference | Earlier elementary Stage 9; used explicitly |
| Four-way fibers excluded | Earlier finite computation Stage 10; not rerun; shared generators in audits |
| Stage 11 all-B choices excluded | Earlier elementary proof; quantifier sharpened here |
| Free/free and shared-role restrictions | Elementary proofs in this round |
| All no-pure triple cones connected | Elementary proof using Stage 9, NOT Stage 10 |
| One-pure fresh-cone residual shape; R3>=2 | Elementary proof using Stage 9, NOT Stage 10 |
| Extra forced fiber is exactly three-way | Conditional on Stage 10 finite computation |
| 588/2744 symbolic check | Complete bounded diagnostic, not a theorem about realizability |
| One CRT candidate | Invalid diagnostic with h=21; not a counterexample |
| h=0 => D=0 | Open |
| No-pure or one-pure three-way fibers absent | Both open |
| |E4|>=60 for valid non-antipodal A8, N<248 | Open |
| Antipodal reduction via minimum124 at n=7 | External paper computation, separate from new results |

No new source/novelty search or external certification was performed in
this continuation. Existing references and the published-computation
boundary are preserved rather than relabeled as self-contained results.

**Single most useful next lemma:** in a valid odd h=0 eight-point set,
an isolated ordinary vertex cannot share a quartic value with the
disjoint five-point component coned from a one-pure cubic triple.

At the pure cone its explicit equations are

    3z=2a+b=2d+e, 4z=2u+v+w,
    A={z,a,b,d,e,u,v,w}.

All partners must be handled simultaneously. In particular, for the
unique 2(u-z)=r-s, the bridge note proves r in {v,w} and
s not in {z,v,w} or ANY doubled center of a partner of 3z.
Thus s in {u,b,e}; these placements remain unresolved. Other four
core cones must also be covered to prove the stated next lemma.

Proving it would eliminate the sole fresh triple-cone shape, NOT prove
global D=0: fresh fibers coning no triple would still need treatment.
Even a full proof of D=0 at h=0 would leave Sigma>=53 in the regular
branch and h>0 for 248. The next run should begin from this smaller
direct bridge obstruction, not repeat the fourteen-choice enumeration
or assume a three-way fiber is impossible.

## 7. Delivery state

The local folder is not a Git checkout and has no local remote.
The intended private repository the source research archive is available
through the GitHub connector, with the earlier archive merged as PR1.
Its main tree was inspected before uploading this round. Only Stage 12
artifacts and the checkpoint/index are proposed; previous evidence and
unrelated repository content are preserved. A branch and unmerged PR
are created for this update; no merge is authorized in this run.
