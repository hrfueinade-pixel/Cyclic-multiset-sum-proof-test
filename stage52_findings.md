# Stage 52: audited near-saturated cubic-center reduction

2026-10-12. Review of the supplied OpenMath center-graph report, with a
fresh reconstruction of its finite graph check and a separate implementation
of coverage and certificate verification. The named ZIP and its original
checker files were not supplied or found in this workspace. The computations
below are new, reproducible evidence, not an audit of unseen source code.

**The reduction P3 <= 17 is supported by complete computer-assisted coverage
under the hypotheses stated below. The full compensation lemma and the
global theorem N >= 248 remain OPEN. No novelty claim is made.**

The elementary E >= 2q argument was already recorded locally in Stage 49.
This report includes a self-contained proof so the checkpoint does not
depend on unpublished Stage 49--51 files. It does not publish or certify the
other results of those intervening local research rounds.

## 1. Definitions and exact hypotheses

A consists of eight distinct labels in an odd finite abelian group G.
Full validity means the all-ones count vector is the unique nonnegative
mass-eight vector representing s = sum(A). In particular every squarefree
degree-d word is protected against all different degree-d multiset words:
add its squarefree complement to obtain a forbidden mass-eight rival.

An ordinary degree-d word is 2c plus d-2 different labels, none equal to c.
For the elementary graph results and the computer-assisted theorem, assume
**every ordinary quartic fiber has at most two words**. This is precisely
the no-ordinary-quartic-triple branch when the inherited ordinary cap three
is in force. Do not export a count C4 = 0 of exactly-three-word fibers to
a setting that permits four or more ordinary words at one value.

P3 counts unordered equal pairs of ordinary cubic WORDS. The cubic-center
graph Gamma has an edge between their two doubled centers. E = S4 counts
disjoint-tail equal ordinary quartic WORD PAIRS. q counts split-type
ordinary quintic triple OUTPUTS. Under the hypothetical odd N < 248
restrictions, the inherited quintic cap is three and k = h + R3 >= 0.

For the quartic budget, T4 denotes the number of REPEATED quartic values,
not the size of the entire set 4A. Full protection gives |4A| = 70 + T4.
The inherited packing bound N >= 71 + 2T4 implies T4 <= 88 below 248.

An ordinary pair has private doubled centers: neither center appears in
the other word, since canceling it would leave an equality against a
protected squarefree word. A cubic pair thus uses four different labels.
There cannot be three ordinary cubic words at one value, since their
private centers and distinct tails use at most six labels; adding an unused
label would produce three ordinary quartics.

Gamma is simple. Two cubic pairs on the same oriented centers give equal
ordered tail differences. Protection of squarefree pairs gives uniqueness
of a nonzero ordered difference; the reversed repeated-pair alternative
is excluded by cancellation of two. At a center, different partners
therefore use different cubic tails.

## 2. Hand proof of E >= 2q

Write a disjoint-tail quartic pair as

    X = 2a+u+v = 2c+x+y,
    B = u+v+x+y,

using six different labels. Let b,z be the two unused labels. If both
quintic lifts X+b and X+z were genuine split triples, privacy forces their
third centers to be z and b, respectively. The third tail is three of the
four labels in B. Thus for r,r' in {u,v,x,y}, allowing r = r',

    X+b = 2z+B-r,       X+z = 2b+B-r'.

Adding gives 2X = b+z+2B-r-r', while the two original quartics give
2X = 2a+2c+B. Substitution in s = a+c+b+z+B gives

    s = 3a+3c+r+r'.

This is a nonnegative mass-eight rival, different from all-ones since it
omits b,z. Hence a quartic source supports at most one split lift.

The three omitted two-label edges of a split quintic triple consist of
two adjacent edges and a separate edge. Two word pairs have exactly one
common tail label; deleting it gives two different disjoint-tail quartic
sources. The remaining word pair has two common labels and descends to a
cubic pair. The deletion inverse recovers each source and its lift label.
Neither source can belong to another split, by the preceding contradiction.
Consequently E >= 2q globally. This counts word pairs, not center edges.

This proof uses no division and does not prove surplus compensation.
With the Stage 48 bound N >= 248+k-2q+E/2 it gives N >= 248+k-q, closing
the q <= k branch below 248. The q > k branch remains open.

## 3. Hand proof: degree five forbids a disjoint-tail quartic incidence

At a center c there are 21 ordinary quartic words, corresponding to
two-element tails among the other seven labels. Every incident cubic pair

    2c+a = 2d+b

has four ordinary quartic lifts, obtained by adding a label outside
{c,d,a,b}. At c these form a four-edge star on tail pairs {a,f}, with
the two incident pairs {a,d}, {a,b} omitted. Stars for different partners
are disjoint: a shared c-centered word would have two different opposing
centers, giving three ordinary quartics. Thus deg_Gamma(c) <= 5.

Suppose the degree is five. Let T be the five different active cubic tails
at c, and U,V the other two labels outside {c} union T. Each star omits
two pairs, giving ten directed omissions. Each of the ten pairs within T
must be omitted by at least one of its endpoint stars to avoid overlap.
All ten omissions are therefore used within T, exactly once per pair.
No star omits U or V. Its opposing center d and opposing tail b both lie
in T. There are five different opposing centers, so T is exactly the
neighbor set of c. The twenty star edges cover every pair except {U,V}.

If a disjoint-tail quartic pair involved c, its c-centered word could not
be one of these twenty paired words. It would have to be

    2c+U+V = 2d+x+y.

Privacy forces d into T. The cubic edge cd has 2c+a = 2d+b, with different
a,b in T. Subtracting gives

    a+x+y = b+U+V.

The right side is squarefree. The count vectors differ, since a is neither
b nor U nor V. This contradicts cubic squarefree protection. Therefore

    deg_Gamma(c) = 5  implies  d_E(c) = 0.

This also proves the tail restriction used in the checker: at a degree-five
endpoint, BOTH tails of every incident cubic pair are neighbors of that
endpoint. At vertices of lower degree the checker imposes no such restriction.

Every split has two E sources whose center edges cover its three centers,
so all its centers have cubic degree at most four.

## 4. The degree budget is exact

Let u(v) count c-centered ordinary quartic words without any other ordinary
representation, even if mixed words represent the same value. With the
ordinary quartic cap two, the words partition into cubic lifts, disjoint-
tail pairs, and such unpaired words:

    4d3(v) + d_E(v) + u(v) = 21.

If P4 counts all ordinary quartic collision pairs, then P4 = 4P3+E and
the number of ordinary quartic values is 168-P4 <= T4 <= 88. Hence

    P4 >= 80,       sum_v u(v) = 168-2P4 <= 8.

Put d(v) = 5-d3(v) and e = 20-P3. Then

    d_E(v)+u(v) = 1+4d(v),
    sum_v d(v) = 2e,
    E >= 4e.

The complement of Gamma has degree 2+d(v) at v, so

    sum_v (deg_complement(v)-2) = 2e <= 2k,

where the last step uses the inherited P3 >= 20-k. These are necessary
constraints; they do not themselves provide the missing injective surplus.

## 5. Complete reconstructed computer-assisted exclusion

The degree bound gives P3 <= 20. To rule out 18,19,20, relabel each graph
so its complement degrees are nondecreasing. Generate EVERY simple graph
with each possible such degree vector. This is coverage up to relabeling,
not an assertion that all these graphs are nonisomorphic.

For every cubic edge cd enumerate all 30 private ordered distinct tails
a,b among the other six labels. Restrict both tails to the neighbors of
an endpoint only when that endpoint has degree five, as proved above.
Require the four lifted tail pairs of each incident edge to be disjoint
from those of all other edges at the same center. No constraint claims
that a locally surviving assignment is a group realization.

| P3 | Graphs with sorted complement degrees | Complete local assignments | Result |
| --- | ---: | ---: | --- |
| 20 | 3,507 | 0 | No necessary assignment |
| 19 | 6,890 | 0 | No necessary assignment |
| 18 | 13,527 | 1,536 | Every assignment excluded by an integer certificate |

The complete P3=18 inventory is:

| Complement degrees | Graphs | Local assignments |
| --- | ---: | ---: |
| (2,2,2,2,2,2,2,6) | 315 | 0 |
| (2,2,2,2,2,2,3,5) | 1,365 | 0 |
| (2,2,2,2,2,2,4,4) | 2,150 | 240 |
| (2,2,2,2,2,3,3,4) | 3,640 | 0 |
| (2,2,2,2,3,3,3,3) | 6,057 | 1,296 |

The supplied report's 6,057 / 1,296 numbers match the last row, but do
not describe the entire P3=18 inventory. They can be sufficient in a
budget-sensitive counterexample argument after excluding cases with too
few split-capable centers. By themselves they do not certify the broader
C4=0 => P3<=17 claim. The reconstructed 240 extra cases repair this gap.

For each survivor form the 18 zero-sum integer rows

    R_cd = 2e_c-2e_d+e_a-e_b.

Deleting coordinate 7 identifies the zero-sum lattice in Z^8 with Z^7.
Exact integer row operations give index one for every survivor. More
strongly, the saved certificate supplies SEVEN explicit integer linear
combinations of the ORIGINAL rows equal to e_i-e_7, for i=0,...,6.
Evaluating in ANY abelian group forces every a_i=a_7, violating distinctness.
The verifier checks these eight-coordinate identities by direct integer
multiplication. No determinant is inverted, no prime is canceled, and no
rational row-span conclusion is substituted for a group identity.

Thus the complete computer-assisted theorem is:

> For a full-valid eight-set in an odd finite abelian group with every
> ordinary quartic fiber of size at most two, P3ordinary <= 17.

The theorem itself does not need T4<=88. Its consequences for a putative
small cyclic counterexample do use the quartic budget and the inherited
Stage 48 / Stage 44 bounds.

## 6. Consequences below 248 and the two degree sequences

In the C4=0 branch under the inherited caps, all ordinary quintic triples
are splits. The theorem gives e>=3. Combining E>=4e with Stage 48 yields

    N >= 248+k-2q+2e >= 254+k-2q.

For N<=247 the necessary conditions are therefore

    k >= e >= 3,
    q >= k+1,
    q >= ceil((k+7)/2).

In particular q>=5. Stage 44 shared-center rigidity allows at most one
genuine split per triple of centers in this branch. If there were at most
four centers of degree <=4, there would be at most binomial(4,3)=4 splits.
Thus at least five centers have degree <=4.

If P3=17, the complement has total degree excess six over the all-two
baseline. At least five excesses are positive, so its ONLY possible degree
sequences, up to order, are

    (3,3,3,3,3,3,2,2),
    (4,3,3,3,3,2,2,2).

This deduction requires the small-order count bounds AND the inherited
shared-center theorem. The sum-of-degrees identity alone is insufficient.
No exclusion of P3=17, or of arbitrary odd orders 207..247, is claimed.

## 7. Fixed large control and notation correction

The independently checked fixed set is

    A = (0,136,518,556,640,700,912,944),   N = 7553.

All 6,435 mass-eight multisets were checked against its original sum; no
alternative representation exists. Its ordinary quartic cap is two,
q=2, and E=4. The two split values are 2724 and 2892, with center triples
{518,556,944} and {518,556,640}. Their quartic sources share the open center
edge {518,556}: its doubled difference is outside the ordered difference
set. Nevertheless E=2q, giving no unused disjoint-tail pairs.

Its entire quartic sumset has |4A|=297; its repeated quartic count is
**T4=227**, correcting the supplied T4=297 label. Both exceed the required
budget. This is a verified control against unconditional local surplus
from a shared open source edge. It is not a sub-248 counterexample and
does not refute conditional global compensation.

## 8. Assignment graph assessment and remaining proof boundary

Regard the h open doubled-center edges as vertices of the split assignment
graph. A split with two open sources gives an auxiliary edge; one with a
single open source gives a mark. For a connected component with d vertices,
e edges and m marks, the minimum unmatched count in an assignment of outputs
to distinct incident vertices is exactly max(e+m-d,0).

For an unmarked tree, orient toward children to match all d-1 edges. For
a marked component, match one mark and orient a spanning tree away from
its vertex, matching d outputs. For an unmarked component containing a
cycle, orient a spanning unicyclic subgraph to match d outputs. These
constructions prove the formula; capacity d gives the converse. Isolated
vertices are included. Let D be the sum of these component deficits.
Since at most h vertices exist, D>=q-h. A sufficient unresolved statement is

    (E-2q) + 2R3 >= 2D.

It would imply E-2q >= 2 max(q-k,0), since E-2q>=0 is already proved.
The small degree-excess budget and the low-degree-center restriction now
constrain this problem, but they do not establish fresh witnesses. A tree
with two marks, a marked cycle (possibly reached along a tree path), or a
connected bicyclic core remains an obstruction requiring algebra or actual
quartic growth. Components with larger excess require their full credit,
with an ownership proof controlling overlap across all components.

The proposed next route is reasonable: add actual split equations in the
two P3=17 degree classes, then either derive a rival, violate the quartic
budget, or produce globally unused pairs with a proved inverse. The
asymmetric five-tail cases and injective witness accounting remain open.
The full weighted triangle/split problem outside C4=0 also remains open.

## 9. Reproduction and audit limits

Use Python 3, standard library only:

    python -B stage52_center_graph_check.py --seconds 120
    python -B stage52_independent_check.py

The producer uses forward vertex graph generation, bit masks and exact
integer elimination. The verifier imports no producer code: it uses reverse
vertex graph generation and sets, reconstructs all tail assignments,
matches the entire survivor inventory, and verifies every saved integer
identity by multiplication. It rejects a changed coefficient and doubled
identities that would establish only torsion, not equality. It separately
reconstructs the fixed large control.

Evidence files: stage52_center_graph_results.json,
stage52_integer_certificates.json.gz, stage52_independent_results.json.
Every listed inventory completed; a timeout is an error, never an exclusion.
No moduli or group parameters were swept, no historical search was restarted,
and no Lean or other proof assistant was used. This is same-assistant
separate-implementation verification, not independent human review, an
independent challenger, or formal certification. The original report's
claimed SymPy check was not independently reproduced and is not a premise.

The new PR is based on the live Stage 48-containing research branch
research/stage37-even-248-and-aperiodicity at
archived-source. PR #20 was already merged into
that branch; main still ends at Stage 14. This checkpoint does not merge
anything into main or claim the missing global proof.
