# Stage 17: short quartic cycles and the remaining shadow budget

Research date: 2026-10-10. This is the global-bound agent's output.

**New elementary restrictions:** in the regular odd branch, every
quartic propagation cycle has length 3, 4, or 5. Every 4-cycle contains
a type-22 vertex and at least two ordinary vertices. Every 5-cycle
without a type-22 vertex contains exactly three ordinary vertices and
two type-31 vertices, so its full support is all eight points.

These restrictions do **not** prove the required 53-cycle lower bound.
The independently audited exact remaining obligation is

    I + t4 + 2*t5 <= 29 + c2,

where I counts internal vertices on nontrivial path components, tj
counts j-cycle components, and c2 counts isolated type-22 vertices.
The equivalence to the target is bookkeeping, not a proved inequality.

No novelty claim, external computational certification, random sampling,
modulus sweep, or Lean work is used. There is no new cyclic-set example.

## 1. Scope and previously proved dependencies

Assume a valid eight-element set A in its odd cyclic difference subgroup
H, with h=R3=0. The following dependencies remain essential:

* Stage 4: squarefree equal-length replacement is forbidden; all pair
  sums and all 56 ordered differences are unique; propagation is exactly
  support overlap within a quartic fiber.
* Stage 5: the propagation graph on 260 repeated quartic multisets has
  degree at most two, precisely 36 noncycle components, K=36+C and
  Sigma=C. Isolated vertices are the c2 reciprocal singleton-permutation
  pairs of type 22.
* Stage 8: D=0 in this branch. Lemma 2.1 says a disjoint 31/31 equality
  under doubled-center-difference closure has center difference of order
  five. Lemma 2.2 excludes disjoint 22/31 equalities under h=0.
* Stage 9, Theorem 9.1: Delta has no order-three difference in odd h=0.

Thus |T4|=36+C, and |T4|>=89 is precisely C>=53. In the full problem,
the weaker packing target has budget Sigma-D>=53-8(h+R3). The stronger
quartic-growth target has budget Sigma-D>=53-6(h+R3). They coincide
here, but must not be conflated outside this branch.

## 2. Cycle geometry and elementary exclusions

Distinct equal quartics share at most one point: canceling two shared
occurrences would give a different pair-sum equality. No three distinct
quartics at a value contain the same point: delete it and obtain three
distinct repeated cubic representations, contradicting R3=0. An ordinary
center occurs in no other distinct vertex, because deleting that center
would leave its squarefree triple.

Consequently a cycle of length L has L distinct shared edge-points,
one between each neighboring pair. If it has o ordinary vertices, their
private centers add o further points. Its support therefore has L+o
points, and L+o<=8. Pure quartics have degree one and cannot be on a
cycle. There is at most one 22 at a value, by odd doubling injectivity
and pair-sum uniqueness.

### Even cycles without a 22 are impossible

Write the cycle vertices as

    v_i = 2*y_i + x_(i-1) + x_i,

with indices modulo L. The y_i are their repeated centers. For a 31,
y_i equals one of its incident edge-points; for an ordinary vertex it
is private. All y_i are distinct: ordinary centers are private, and two
31s with the same center would have the same singleton and be identical.

For even L, alternating the equal vertex values cancels every x_i:

    2*sum_even(y_i) = 2*sum_odd(y_i).

Cancel two in odd H. The resulting distinct squarefree subsets have
the same length and sum, contrary to validity. This includes the earlier
all-ordinary four-cycle obstruction and all mixed even non-22 cycles.
It does not cover a cycle containing a 22.

### Three consecutive 31s with disjoint first/third supports are impossible

Adjacent 31s cannot share their center: they would be identical. They
cannot share their singleton: cancellation would give an order-three
center difference, excluded by Stage 9. Hence a run has coherent
orientation. Three consecutive vertices on four distinct edge-points
can be written

    3*x0+x1 = 3*x1+x2 = 3*x2+x3.

The first and third are disjoint in a path or a cycle of length at least
four. Stage 8 Lemma 2.1 gives 5*(x0-x2)=0. Put

    r1 = 3*x0-2*x1-x2,
    r2 = 3*x1-2*x2-x3,
    T  = 5*x0-5*x2.

The exact integer identity

    x0+x2-x1-x3 = 2*r1+r2-T

equates two distinct squarefree pairs, contradicting validity. A triangle
of three 31s is not covered, because its first and third share a point.

### The only possible lengths are three, four and five

For a cycle without 22, even lengths are excluded. If L>=7, then L+o<=8
allows at most one ordinary vertex. The remaining run of at least six
31s contains the forbidden three-31 run. The same run excludes an
all-31 five-cycle.

For a cycle with 22, every 31 must be adjacent to it: otherwise the
two support pairs are disjoint, contradicting Stage 8 Lemma 2.2. There
are at most two such neighbors. Thus o>=L-3 and L+o>=2L-3, forcing
L<=5. Four-cycles containing a 22 require separate treatment.

### Further exclusions of long-cycle type words

Use O=ordinary, P=31 and Q=22. A five-cycle without Q cannot have three
Ps. Without a three-P run, its only cyclic type word is P P O P O.
The isolated P is disjoint from the other two Ps. Lemma 2.1 puts all
three distinct repeated centers into one coset of the unique order-five
subgroup of cyclic H. Their six unique ordered differences cannot fit
into its four nonzero elements. Hence such a five-cycle has exactly
three Os and two Ps, and uses all of A.

A four-cycle of type Q P O P is also impossible. A 31 adjacent to a 22
cannot share its center with that 22: cancellation gives a forbidden
squarefree-pair/double equality. Therefore the shape is

    X = 2*p+2*q = 3*a+p = 2*d+a+b = 3*b+q,

on five distinct points. The two 31s are disjoint, so T=5*(a-b)=0.
Let r1=(3*a+p)-(3*b+q), r2=(2*p+2*q)-(3*b+q), and
r3=(2*d+a+b)-(3*b+q). Then

    2*(a+d-2*q) = 2*r1-r2+r3-T.

Cancel two in odd H to obtain the forbidden squarefree-pair equality
a+d=2*q. No division by an odd integer is involved.

These leave the following necessary long-cycle words, up to rotation
and reversal. They are unresolved patterns, not valid realizations:

| Length | Remaining words | Support size |
|---|---|---|
|4|Q O O O; Q P O O|7; 6|
|5|P P O O O; P O P O O|8; 8|
|5|Q P O O P; Q P O O O|7; 8|

## 3. The precise remaining structural inequality

Stage 5 gives 72-2*c2 degree-one vertices and c2 degree-zero vertices.
Hence the degree-two total is

    260-(72-2*c2)-c2 = 188+c2.

Let I count degree-two vertices on nontrivial paths. Every cycle has
length three, four or five by the new proof. Therefore

    I+3*t3+4*t4+5*t5 = 188+c2,
    3*C = 188+c2-I-t4-2*t5.

It follows exactly that

    C>=53  <=>  I+t4+2*t5 <= 29+c2.

No upper bound on this expression is proved here. The binary control
has I=20,c2=0,t4=t5=0,C=56. Its three-cycle behavior is a control, not
evidence that the six surviving long-cycle words are impossible.

The next global attack should bound internal path vertices jointly with
the remaining quadrilateral and pentagon components. An initial concrete
subproblem is to determine whether doubled-difference closure excludes
the four surviving pentagon words. Bounding or eliminating those alone
would still leave the internal-path budget; this report does not claim
that the subproblem suffices. Avoid turning the exact budget into a
claimed new numerical lower bound.

## 4. Independent audit and reproducible evidence

The challenger separately checked the shared-point accounting, even-cycle
argument, three-31 exclusion, five-cycle three-center exclusion, and
Q P O P exclusion. These are elementary proofs; agreement is review,
not an additional proof premise.

Run with standard-library Python 3:

    python stage17_global_checks.py

The checker enumerates all admissible even non-22 incidence roles on at
most eight points and verifies explicit integer certificates of the form
2^k*(rival-all-ones)=sum z_i*relation_i. It also checks the two displayed
local certificates, rejects a deliberately incorrect identity and
noninteger odd-denominator coefficients, exhaustively filters the bounded
cycle type words, and reconstructs one binary control graph. There is no
set or modulus search. Its JSON preserves every certificate and every
remaining long-cycle type word, and records completion separately from
timeout. It imports no project proof/search functions.

The completed run verified 194 certificates (192 even-cycle role
certificates and two local certificates) and filtered all 9801 ordered
type words of lengths four through eight. Both negative controls were
rejected. The binary control has 16 two-vertex paths, 20 three-vertex
paths and 56 triangles. These counts validate the displayed bookkeeping;
the run did not search for cyclic-set realizations of any surviving word.

An exploratory seven-cycle normalization produced twelve derived subgroup
orders, but that route was superseded before delivery by the elementary
three-31 proof. No exclusion depends on the exploratory order calculation.

## 5. Relation to the local agent and the original problem

The local defect exclusions concern the odd h=0,R3>0 branch of D=0.
They do not add a numerical lower bound for C in the regular branch,
where Stage 8 already gives D=0. Neither this report nor the new local
exclusion proves C>=53, controls h>0, or proves N>=248.

This round obtains a new structural restriction, satisfying the stated
progress criterion, while leaving the global numerical target explicit.
The recommendation is to prioritize the shadow budget next; further
local defect work should proceed only against a specific residual shape
with complete coverage and a checkable exclusion mechanism.
