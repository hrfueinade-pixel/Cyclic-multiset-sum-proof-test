# Stage 12 independent challenger notes

Scope: one focused round on the no-pure three-way fiber. The original
248 target and the intermediate h=0 => D=0 remain open. These notes
do not concern the one-pure shape with three free points.

## Audited setup and quantifiers

Let A be valid, with odd difference-generated subgroup and h=0. Write

    C={c0,c1,c2}, bi=Y-2ci, B={b0,b1,b2}, F={x,y}.

All eight points are distinct. Stage 9 excludes order-three differences.
Stage 11's ordinary-center argument correctly excludes C from every
different partner 3ci=2p+q. Thus p,q are distinct points of B union F.

The Stage 11 all-B proof rules out EVERY simultaneous selection of
B-only partners for all three pure cubics. Since each pure cubic has
a nonempty partner set, at least one pure cubic has NO B-only partner.
Every available partner for that particular cubic therefore uses F.
This is stronger than merely asserting the existence of one free-point
partner. It does not identify that cubic or make partner choices unique.

## Elementary role restrictions

For a partner 3ci=2bj+q with j!=i, compensation with the core equations
gives

    ci+2cj-bi-bj-q=0.

If q differs from bi,bj, its negative coefficients are all at least -1
and its coefficient at cj is 2, giving a rival to the all-ones multiset.
The possibility q=bj gives 3ci=3bj and is excluded by Stage 9.
Consequently q=bi. In particular every free SINGLETON partner whose
doubled point lies in B has form

    3ci=2bi+x,       x=7ci-2Y.

Individual free DOUBLE partners 3ci=2x+bj need not have j=i.

If the same free double center x partners two pure cubics,

    3ci=2x+qi,       3cj=2x+qj,       i!=j,

then qi!=qj: equality would give 3ci=3cj, and adding the core relation
Rj-Ri gives the forbidden pair equality ci+bj=cj+bi. The disjoint
quartics 3ci+qj=3cj+qi invoke the elementary disjoint-31/31 lemma from
Stage 8, so ci-cj has order five. Therefore

    qi-qj=3(ci-cj)=-2(ci-cj)=bi-bj.

Ordered-difference uniqueness forces qi=bi and qj=bj. This conclusion
applies to ALL choices of two such partners, not only chosen witnesses.

A free point cannot be a double partner for all three pure cubics:
the preceding argument, and uniqueness of the order-five subgroup in
cyclic H, put three distinct C-points in one order-five coset, giving
six ordered differences in a subgroup having
only four nonzero elements.

A free point cannot appear in this B-doubled singleton role for all
three either. Its role equations force all C-points into one order-seven coset, and
all B-points into another. Those two triples supply twelve distinct
ordered differences in a subgroup having only six nonzero elements.
This statement does not cover a free/free partner plus two B-doubled
singleton appearances. Such mixed roles must remain explicitly separate.

The shared-double result does cover free/free partners: if
3ci=2x+y with both points free, x cannot be the doubled point of any
partner of another pure cubic. Otherwise the shared-double conclusion
would force its singleton y to equal bi, contradicting F disjoint B.

## Free/free partners: at most one pure cubic can have one

Suppose both p,q are free. There are only two ordered possibilities:
2x+y and 2y+x. Two distinct pure cubics cannot use the same ordered
possibility. Indeed 3ci=3cj, compensated by Rj-Ri, gives
ci+bj=cj+bi on four distinct core points, forbidden by validity.

They also cannot use opposite possibilities. Indeed, if

    3ci=2x+y,        3cj=2y+x,        i!=j,

then x-y=3(ci-cj), while bj-bi=2(ci-cj). Hence

    ci+bj+y = cj+bi+x.

Both sides are squarefree triples, and their six support points are
distinct. This violates validity by padding either replacement with
its complement. Thus at most ONE of the three pure cubics can have
any free/free partner. This proof uses neither Stage9's order-three
exclusion nor Stage10's finite computation: both orders are excluded
by the core relations and squarefree replacements alone.

## Correct order-seven exhaustion statement

If a free singleton x is reused for centers 0,t, then t has order
seven and x=-2Y. The pairs {0,t} and {Y,Y-2t} exhaust differences
plus/minus t and plus/minus 2t. Doubling closure supplies the remaining
plus/minus 4t, represented by exactly one further unordered pair.
No other point can enter either existing two-point order-seven coset:
three points there would supply six differences in addition to the
other pair's two. The third pair must consequently lie among

    {c2,b2,x,y}.

There are six possible pairs. Omitting b2, or asserting that y must
participate, is unjustified. This restriction alone is not an exclusion.

## One bounded diagnostic, explicitly invalid

Scope announced before execution: one fixed selected-constraint set
in Z/3 x Z/1009, runtime cap two seconds, all 6435 eight-term multisets.
The cyclic modulus is 3027, with points in C,B,F order

    ((0,0),(0,1),(0,51),(0,119),(0,117),(0,17),(2,2),(2,-1)).

It has the three-way core at Y=(0,119), the two swapped free/free
partners of the first two pure cubics, and the B-only partner
3*(0,51)=2*(0,17)+(0,119). The run completed below its cap:
eight distinct points, 36 distinct pair sums, 56
distinct ordered differences, no order-three difference, and 42
missing doubled differences. All 6435 multisets were checked.

The saved result's timer reads 0.0 seconds at its measurement resolution;
the completion flag and all 6435 checked multisets, rather than that
timing precision, establish completion under the two-second cap.

It is NOT valid. The triple equality above becomes

    (0,0)+(0,117)+(2,2) = (0,1)+(0,119)+(2,-1).

Padding gives the rival multiset with point indices
(0,0,2,4,4,5,6,6), where indices start at zero. This diagnostic exposed
the general squarefree replacement; the proof, not the check, supports
the restriction. It is neither an h=0 example nor a counterexample to
any research goal. No completed prior check was rerun.

Reproduction, using standard-library Python:

```python
from itertools import combinations_with_replacement
from time import monotonic

A = [(0,0),(0,1),(0,51),(0,119),(0,117),(0,17),(2,2),(2,-1)]
def total(points):
    points = tuple(points)
    return (sum(a for a,b in points) % 3,
            sum(b for a,b in points) % 1009)
target = total(A)
start = monotonic()
tested = 0
rivals = []
for indices in combinations_with_replacement(range(8), 8):
    if monotonic() - start > 2:
        raise RuntimeError('INCOMPLETE: runtime cap reached')
    tested += 1
    if indices != tuple(range(8)) and total(A[i] for i in indices) == target:
        rivals.append(indices)
assert tested == 6435
assert (0,0,2,4,4,5,6,6) in rivals
```

The saved `stage12_challenger_checks.py` also records pair/difference
statistics and writes explicit completion status to the result file.

## Exact unresolved boundary

These restrictions permit multiple free-point partners and mixed
singleton/double appearances. They do not prove that two free points
are insufficient, and do not prove R3=0 or D=0. No compatibility of
different selected partners should be inferred without the actual
equations and all singleton-base trees. The one-pure shape remains
separate and unresolved. The regular Sigma>=53 and h>0 branches
remain necessary for the original target.

An attempted shortcut before finding the squarefree replacement was
invalid: swapped free/free partners imply that
w=2ci-cj-x has order three, but w is NOT necessarily an A-difference.
Stage 9 excludes order-three differences, not all order-three elements
of H or torsion differences of pair sums. The squarefree triple identity,
not that torsion shortcut, supplies the contradiction.

## Consolidation audit of the alternative bridge

Proposition A of `stage12_bridge_findings.md` has complete type coverage:
the coned core occupies at least six support points; an external free
tail makes seven, a B-tail supplies a 22, and a C-tail supplies a 31.
Full component-support separation, pure component size at least three,
and the four-point lower bound for a 31 component opposite another 31
exclude all possible remaining repeated-quartic types. This controls
the entire fiber, not only its three displayed coned vertices.

Proposition B's support and type analysis likewise isolates the
three-point ordinary vertex as its sole residual fresh-cone shape.
Two dependency clarifications are essential:

1. The displayed initial three marks do not by themselves assert an
   exactly-three fiber. Distinctness of the additional multiway fiber
   follows because any original-fiber mark centered at the isolated
   ordinary center would cone into U and enlarge its support beyond P.
2. Two distinct fibers of size at least three already imply R3>=2
   elementarily. Stage10 is needed only to conclude that the additional
   fiber has exactly three marks, not for this lower bound on R3.

No additional computation was performed for this consolidation audit.
