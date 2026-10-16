# Stage 11 checkpoint: a three-way fiber must use a free point

Research date: 2026-10-10. The full goal h=0 => D=0 remains OPEN.
Work is stopping at the user's request. This is a checkpoint, not a
claim that the three-way exclusion or the 248 bound has been proved.

## 1. Proved restriction

**Proposition.** Let A be a valid eight-point set in its odd cyclic
difference-generated subgroup H, with h=0. Suppose it has a three-way
cubic fiber with no pure representation. Translate one center to zero:

    C={c0=0,c1,c2}, B={b0=Y,b1=Y-2c1,b2=Y-2c2},
    A=C union B union F,   |F|=2,

with all eight points distinct. Every pure cubic 3ci has a partner
2p+q, with p,q distinct and lying in B union F. Moreover it is
impossible to choose partners for all three pure cubics using only B.
Thus at least one pure cubic must have a partner containing a free point.

This is an elementary restriction, not a computational template exclusion.
It is weaker than excluding the three-way fiber. No novelty is asserted.

### Dependencies

Stage5 proves that the singleton-label equations form a spanning tree
with no edge entering its base, so every pure cubic 3a has a different
partner at h=0. Stage9 proves that Delta has no order-three element.
Stage4 proves that the repeated center of an ordinary quartic is absent
from every other distinct representation of its value. Each follows
from validity and the stated h=0 hypotheses, not the n<=7 computation.
Stage10's computer-assisted four-way exclusion is useful context but
is NOT needed for this proposition.

## 2. Pure partners cannot use C

Fix i. For j!=i the quartic

    Qj=2cj+bj+ci

is ordinary, with repeated center cj. Its value is Y+ci, also the
value of 3ci+bi. If 3ci=2p+q is a different partner, then

    R=2p+q+bi

has this same quartic value. Since bi belongs to none of the supports
{cj,bj,ci}, R cannot equal Qj. The ordinary-center restriction therefore
forces p,q!=cj for each j!=i. Neither p nor q can equal ci either:
that would give a trivial equality or a forbidden pair-sum equality.
Finally p=q would give 3(ci-p)=0, contradicting the absence of an
order-three difference. Thus p,q are distinct points of B union F.

## 3. A compensation identity for B-only partners

Write

    Ri=2ci+bi-2c0-b0=0,    R0=0.

If 3ci=2bj+q with j!=i, then

    (3ci-2bj-q)+(Rj-Ri)=ci+2cj-bi-bj-q=0.             (1)

If q is neither bi nor bj, all negative coefficients of (1) are
>=-1 and its coefficient at cj is 2. Adding (1) to the all-ones
vector gives an eight-term rival. The case q=bj was already excluded
by the order-three restriction. Consequently q=bi.

Assume now, for contradiction, that all three pure cubics have B-only
partners. Each chosen partner has one of exactly two forms, for j!=i:

    U: 3ci=2bi+bj, equivalently 7ci+2cj=3Y;
    V: 3ci=2bj+bi, equivalently 5ci+4cj=3Y.

Assign the arrow i->j and its type U or V. This is a functional graph
on three vertices without a fixed point: a three-cycle or a two-cycle
with a tail. These possibilities are exhaustive, even if a pure cubic
has additional partners not chosen here.

## 4. Two-cycle with a tail

For a two-cycle i<->j, subtract the two equations. The result is
5(ci-cj)=0 for U/U, 3(ci-cj)=0 for U/V, and ci=cj for V/V.
The last two are forbidden; only U/U survives.

Translate ci to zero and put cj=t. Then t has order five and 3Y=2t.
The order of Y is five or fifteen. If five, the four distinct points
0,t,Y,Y-2t belong to one order-five coset, contradicting uniqueness
of ordered differences. Hence Y has order fifteen, with order-five
component 4t and a nonzero order-three component.

Let ck be the tail center, pointing to r=0 or t.

* Tail U gives 7ck=2t-2r. For r=0, ck has order 35 and order-five
  component t: an order-five solution would equal t, an existing point.
  For r=t, ck has order seven: the zero solution is an existing point.
  In either case Delta contains differences of orders 5,7,15,35,105.
  The order-105 difference is Y-ck: its components of orders 3,5,7
  are all nonzero. The order-seven and order-35 differences are ck
  and ck-t in the appropriate order.
* Tail V gives 5ck=2t-4r=+/-2t. Therefore ck has order 25, while
  Y-ck has order 75. Delta contains orders 5,15,25,75.

Since 2Delta=Delta and Delta=-Delta, any difference brings its entire
joint doubling/negation orbit into Delta. The orbit sizes for the
displayed orders are

    order       5   7   15   25   35   75   105
    orbit size  4   6    8   20   24   40    24.

Different orders have disjoint orbits. Tail U thus requires at least
4+6+8+24+24=66 differences; tail V requires at least 4+8+20+40=72.
Both contradict |Delta|=56. These fixed orbit sizes follow directly
by taking the order of 2 modulo the displayed order and adjoining -1;
the checkpoint checker verifies the same finite arithmetic.

## 5. Three-cycle

Relabel the cycle 0->1->2->0. Its equations have the form

    ai ci+bi c_(i+1)=3Y,   ai in {7,5}, bi=9-ai in {2,4}.

Here bi denotes an equation coefficient only in this paragraph, not
the B-points. As these coefficients are powers of two, c1 and c2
are multiples of Y. Thus Y generates the six-point core subgroup J.
Eliminating c1,c2 gives

    ((a0*a1*a2+b0*b1*b2)/3)Y=0.

The possible annihilators are 117 (UUU), 87 (UUV), 69 (UVV), 63 (VVV).
Rotation of the cycle covers the mixed-type positions.

### Elementary lower bound for the six-point core

The core C union B is valid for six terms, by hereditary validity.
In an odd cyclic group, a valid six-point set has 30 distinct ordered
differences. Its 36 repeated cubic marks have at most 15 pairwise
collisions, since each center pair determines at most one singleton
pair. Therefore |T3|>=21. Its translated subset cube S has 32 points.
The cubic intersection with S is exactly A: a subset of size >=3
could otherwise be replaced by the cubic and padded with zeros; for
size two, include the single zero in the squarefree subset first.
Size zero or one already gives a point of A. Thus E3=T3\A has size
at least 15. S,E3,s-E3 are disjoint: two exterior cubics summing to s
would give a six-term rival. Consequently |J|>=32+2*15=62.

Only the full displayed annihilator is a divisor >=62. Hence |J| is
117,87,69,63 respectively, and Y is a generator in each case.

* UUV: Delta contains Y of order 87 and c1 of order 29. Their joint
  orbits have sizes 56 and 28, requiring at least 84 differences.
* UVV: Delta contains Y of order 69 and c1 of order 23. Their orbit
  sizes are 44 and 22, requiring at least 66 differences.
* UUU: in generator-Y coordinates modulo 117, the six core points are
  {0,60,84,1,115,67}. Y and 67Y are in different joint unit orbits,
  each of size 24. Indeed <2> modulo 117 is
  {1,2,4,8,16,32,64,11,22,44,88,59}, and neither it nor its negative
  contains 67. The difference 60Y has order 39 and orbit size 24.
  These require at least 72 differences, again impossible.
* VVV: the equations give 21c1=0 and 4c2=-c1, so c2=5c1. The sum
  of the six core points is 3Y-c1-c2=3(Y-2c1). Hence three copies
  of c0 and three copies of the B-point Y-2c1 form a six-term rival.

Every graph case is impossible. This proves the proposition.

## 6. A valid control and a failed shortcut

The local conclusion is NOT that a pure cubic can never have a B-only
partner. The fixed valid eight-point control, in integer lifts, is

    A=(0,3,41,4,-2,-78,1000,1000000), N=8000625.

It has the three-way fiber

    4=2*0+4=2*3+(-2)=2*41+(-78),

and the B-only pure partner 3*0=2*(-2)+4. It has h=23, not h=0;
the other pure cubics need not be paired. It is not a counterexample
to the proposition or to the full goal.

Complete validity proof: all eight-term lifted sums lie between -624
and 8000000, an interval of width N-1. Congruence with the target
1000968 is therefore integer equality. The bounds force one copy of
1000000 and then one copy of 1000. For the remaining six terms let
k count 41 and m count -78=4-2*41. Equality with target -32=9-41
forces k-2m=-1, since the remaining constant expression lies in
[-12,24] and 9 minus it in [-15,21], containing no nonzero multiple
of 41. Thus (k,m)=(1,1) or (3,2). The latter leaves one low point
of required value 1, not available. The former requires four terms
from {0,3,4,-2} summing to 5. Write their counts r,s,t,u respectively
for 3,4,-2,0. The equation 3r+4s-2t=5 makes r odd. r=3 would
require t>=2, exceeding four terms. r=1 gives t=2s-1 and 3s<=4,
forcing r=s=t=u=1. Every original point therefore occurs once.

This control has no order-three difference: every lifted difference
has absolute value <=1000078<N/3. It demonstrates why both global
pairing and doubling closure matter, not just the local fiber shape.

## 7. Reproduction and exact resume point

    python stage11_threeway_checks.py

The checks are restricted to 64 three-vertex arrow/type patterns,
thirteen fixed order-orbit calculations, the two displayed cyclic cores,
and ONE valid eight-point fixture through all 6435 multisets. These
check bookkeeping; the proofs above supply the logical case coverage.
They are not an exhaustive set/modulus search and provide no new
valid h=0 structural diversity.

**Next unresolved step:** in the no-pure three-way case, use the two
free points to constrain the forced pure-cubic partners and the
singleton-base trees simultaneously. The proposition forces at least
one use of a free point, but does not prove that two free points are
insufficient. The one-pure three-way configuration remains untouched.
One must not infer R3=0 or D=0 from the restrictions saved here.

Stage10 records the completed, independently audited four-way template
exclusion. Stage8 records the proved h=R3=0 quartic bridge. Even after
the diagnostic goal, the original 248 bound still needs Sigma>=53 in
the regular branch and control of h>0. No PR can be created here:
the workspace is not a Git repository and has no configured remote.
