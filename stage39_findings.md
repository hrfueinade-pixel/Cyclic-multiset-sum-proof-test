# Stage 39: cubic--overlap counterexample and the five-block hole gap

Saved 2026-10-11. Continuation of Stage 38 / open PR #10, following the
instruction to execute the proposed attacks. The universal N>=248 theorem
is still OPEN. No modulus is newly excluded. No earlier PR is merged.

The main deliverable is a positively verified counterexample to the
Stage 38 cubic--overlap alternative. The planned pivot was then performed:
the five-block constraints were analyzed structurally and tested on a
targeted cohort. This yields elementary support reductions, an exact
hole-placement formulation, and a proof that its cardinality bound cannot
exclude the top two odd orders. These reductions do not themselves prove
the original theorem. No novelty claim is made.

## 1. The proposed cubic--overlap alternative is false

Take

    N=247, A={0,33,56,82,155,156,202,217}.

Every one of its 56 squarefree cubic sums has exactly one representation
among ALL 120 unordered three-term multisets. Nevertheless

    max_t |(2.A) intersect(A+t)| = 4,

where 2.A={2a:a in A} is dilation, not the two-fold sumset. The maximum is
attained only at t=157; its four pairs (a,b), with 2a-b=t, are

    (33,156), (56,202), (156,155), (202,0).

There are no five-fold or six-fold intersections. Thus the Stage 38 claim
that cubic protection forces overlap at least six in odd 207<=N<248 is
refuted. It cannot be combined with Stage 29 to finish the interval.
Stage 29 itself is not contradicted: the example is invalid, and its
overlap is already below that theorem's upper bound for valid sets.

The example has |3A|=106, |4A|=202, and 69 distinct squarefree quartics.
In particular it does NOT refute |4A|>=159, and it is NOT a counterexample
to the original minimum-modulus problem. An especially simple failure is

    33+56+82+156 = 327 = 574 = 0+155+202+217 (mod 247).

Both complementary four-subsets have residue 80. The total eight-point
sum is 901=160 modulo 247. Taking two copies of the first four-subset
gives the non-original eight-term representation

    2*33+2*56+2*82+2*156 = 654 = 901 (mod 247).

Its multiplicities in the displayed increasing A are
(0,2,2,2,0,2,0,0). The separate checker finds 23 eight-term rivals in total
after checking all 6435 degree-eight count vectors. Its evidence includes
all 56 protected cubic fibers, every nonempty dilation-overlap fiber,
every rival, and the quartic failures. The witness was reproduced with
the final discovery code, at the same restart and step.

## 2. First attack: what changed in the experiment

Stage 38's cubic experiment minimized cubic collisions without explicitly
penalizing high overlap, and explored substantial binary-shaped families.
The new attack directly optimizes both requirements. It batches every
replacement value for one mutable coordinate (only the translated zero is
fixed), using the objective

    cubic_loss + 4*max(maximum_overlap-5,0).

Here cubic_loss is the sum, over squarefree cubic words, of their residue
fiber size minus one. It is zero exactly when all squarefree cubics are
protected. Replacement values that would repeat a point are discarded.
Seeded random equal-best moves, short tabu memory, and declared periodic
two-coordinate perturbations leave local minima. The witness appears at
N=247, restart 4, step 232, after 1833 batches / 439920 distinct-point
presentations, in about two seconds. These are presentations, NOT 439920
different sets or affine classes. Discovery stops on a positive witness;
no claim about the unvisited schedule follows.

The positive witness is checked by a separate implementation using weak
compositions rather than word lists or the discovery matrices. It imports
neither numpy, the discovery producer, nor any historical research kernel.
Both implementations are by the same agent, not separate human review or
a formal proof assistant. The positive counterexample, rather than a
heuristic absence, establishes the mathematical falsification.

## 3. Second attack: cancellation localizes every eight-term rival

Call A cubic-protected when every squarefree three-element sum is unique
among all three-term multisets on A. Such protection also holds for
squarefree sums of one or two elements: append the same distinct elements
outside the original support to both representations, reaching a
squarefree cubic on the original side. A different count vector remains
different after this padding, even if the appended labels already occur
on the opposing side.

**Support cancellation lemma.** In any abelian group, if an eight-element
A is cubic-protected, every non-original eight-term representation of
s=sum A uses at most FOUR distinct elements.

Proof. Let its multiplicities be c_i, and let J={i:c_i>0}, |J|=k. If k=8,
the total mass eight forces all c_i=1, so the representation is original.
Otherwise cancel one copy of each present label from both sides:

    sum_(i not in J) a_i = sum_(i in J) (c_i-1)*a_i.

Both sides have degree m=8-k, and the left side is squarefree. If k>=5,
then 1<=m<=3, contradicting hereditary cubic protection. Therefore k<=4.

Two useful consequences, with the same cancellation argument:

1. For a five-subset B of a cubic-protected A, a non-original quintic
   representation of sum B supported on B must be a pure word 5b. Thus B
   is hereditary valid precisely when 5b!=sum B for every b in B.
2. If all squarefree quartics of A are protected among ALL quartic
   multisets, every eight-term rival uses at most THREE distinct labels.
   Protection through degree four forbids m<=4 in the same equation.

This uses arbitrary abelian groups; it supplies no odd cyclic growth by
itself. In particular, it is a support reduction rather than an exclusion.

Define the restricted eight-term sumset

    S8_<=4(A) = union_(B subset A, |B|=4) 8B.

Every degree-eight multiset with support at most four occurs in this
union, including those with fewer labels (fill the supporting B to four).
Conversely every word in 8B has support at most four. Consequently, for
a cubic-protected eight-set,

    A is valid  <=>  s NOT in S8_<=4(A).

There are 70 four-subsets, and 8B has at most binomial(11,3)=165 values.
The union's cardinality or the location of s is NOT controlled by these
word caps. Blocks must include nonprimitive ones: a rival's support cannot
be assumed to generate the ambient group. Restricting this equivalence to
primitive four-blocks would leave a coverage gap.

## 4. Complementary quartic collisions and the midpoint

**Disjoint-support lemma.** If A is cubic-protected and a squarefree
quartic S has another quartic representation M, their supports are
disjoint. If they shared a label, cancel one occurrence of that label.
This would equate a squarefree cubic to a different cubic count vector,
contradicting protection. Thus M is supported in A\S.

In particular two different squarefree quartics with the same value must
be complementary four-subsets. Their common value q satisfies 2q=s.
In an odd cyclic group doubling is injective, so only one residue can
carry such a collision. A fiber contains at most the complementary pair:
any further four-subset would also have to be the complement of the first.
Hence a cubic-protected eight-set in odd order has exactly 69 or 70
distinct squarefree quartic values.

If there are 69, two copies of either colliding four-subset already form
an eight-term rival. Thus a remaining valid set must have 70. This
condition is still weaker than quartic PROTECTION: seventy distinct
squarefree values says nothing about a repeated quartic representing one
of them. Under cubic protection such an opposing word lies in the
complementary four-block, as just proved.

These arguments challenge three tempting shortcuts: a shared-label
quartic collision is impossible here; a complementary collision is
allowed by cubic protection; and excluding the midpoint collision alone
does not establish full quartic protection or eight-term validity.

## 5. Five-block holes: exact placement, and a decisive counting gap

Write A=B disjoint-union C, |B|=5, |C|=3, with s_B=sum B and s_C=sum C.
For k=5,6,7,8 put

    H_k = s_B - (Z_N \ kB).

This is a reflected hole set with the SAME center s_B at every degree.
The exact erosion relation is

    x in H_(k+1)  <=>  x+b in H_k for EVERY b in B.

Indeed s_B-x is missing from (k+1)B precisely when
s_B-x-b is missing from kB for every b. The plus sign in x+b matters.
If zero is not in B, H_(k+1) need not be a subset of H_k.

The Stage 33 conditions for eight-term representations using q>=5 terms
from B are

    repeated 3C - s_C subset H_5,
    2C - s_C subset H_6,
    C - s_C subset H_7,
    -s_C in H_8.

The first line includes all nine non-original cubic multisets of C; their
values can repeat, so nine words are not necessarily nine different
holes. Assume whole-set cubic protection. Expanding the last three lines
through erosion, the four lines together say exactly

    (3A - s_C) \ {0} subset H_5,

or equivalently

    5B intersect (s - 3A) = {s_B}.                         (H)

To see the union explicitly, the required values are repeated 3C-s_C,
2C+B-s_C, C+2B-s_C, and 3B-s_C. They are every cubic on A except the
original C. Cubic protection ensures that none of these other words has
value s_C. The erosion relation therefore loses no placement condition.

Equation (H) describes degree-five SUMSET residues, not multiplicities.
It does not detect a wrong quintic representation of s_B paired with the
original C. The usual hereditary validity of B must also be imposed when
using (H) as uniqueness of the entire q>=5 part. The experiment checks
this separately, rather than assuming cubic protection implies it.

Since 0 is not a hole, (H) implies

    |H_5| >= |3A|-1, or |5B|+|3A| <= N+1.               (C)

This is an actual quantitative restriction, but it CANNOT exclude N=245
or 247: for ANY five-block B and eight-set A, repetitions allowed,

    |5B| <= binomial(9,4)=126,
    |3A| <= binomial(10,3)=120,
    |5B|+|3A| <=246.

Thus (C) is automatically satisfied at both orders, even at the maximal
word counts. No sharpening of a lower bound on |5B| or |3A| can make this
single-block cardinality inequality contradict those orders. A successful
five-block argument needs PLACEMENT of the translated cubic shadow in
the holes, or coupling across different B's. This is the exact gap in
the second structural attempt, not a request for a larger search timeout.

## 6. Targeted pivot experiment and its limits

The same overlap-aware search was given a declared target of 32 different
sorted witnesses and a 45-second cap. It retained twelve cubic-protected
sets with overlap at most five, at N=239 and 247, before timing out during
N=239, restart 49, step 184. N=243 was not reached. There were 45384
batches / 10733888 distinct-point presentations, with 246 cubic-protected
visits; visits and presentations repeat sets. The twelve retained sets
fall into nine affine classes at their respective moduli, normalized by
the least ordered-unit-pair image. These are cohort classifications,
not a census of affine classes in either group.

For each saved set, all 56 five-block/triple splits were inspected. The
hole erosion and cubic-shadow identities above agree with the explicit
q=5,6,7,8 conditions. Primitive five-blocks are selected using their
DIFFERENCES, and their actual quintic validity is checked. No primitive,
valid five-block in this cohort satisfies the joint hole conditions.
All twelve sets have Q4 cardinality 69 and explicit eight-term rivals;
they illustrate that cubic protection and small overlap admit midpoint
failure. They do not prove that midpoint failure is forced. The minimum
shadow-placement deficits for eligible blocks range from 17 to 32 in
this cohort; those positive numbers exclude only these saved sets.

A distinct follow-up adds the penalty for a midpoint quartic collision.
There are 35 complementary four-subset pairs, represented by the
four-subsets containing index zero. Given cubic protection in odd order,
no midpoint collision is equivalent to 70 distinct squarefree quartics.
The objective is now

    cubic_loss + 4*max(maximum_overlap-5,0) + 4*midpoint_collision.

This specifically distinguishes the failed lemma from the hypothesis
that it can survive with the necessary 70-value condition. The 45-second
cap ended during N=239, restart 29, step 140, after 37340 batches /
8867680 distinct-point presentations. It found NO positive witness to
cubic protection + overlap<=5 + Q4=70. Its best saved candidates at
247 and 239 have cubic loss ONE, overlap two, and no midpoint collision.
They are not cubic-protected and prove nothing about the strengthened
hypothesis. They are independently checked snapshots, not exclusions.
Neither the incomplete schedule nor a nonzero minimum is certified.

The N=255 binary control {0,1,3,7,15,31,63,127} is valid and all 56
five-block splits satisfy the joint condition. This detects a sign or
erosion error that could otherwise falsely reject every example. It is
checked independently through all 6435 eight-term count vectors as well.

## 7. Precise unresolved target and stop assessment

The cubic--overlap alternative is now FALSE, with a reproducible,
positively checked counterexample. The five-block cardinality approach
falls short for a provable reason at the top of the interval. Its exact
placement formulation survives, but this round establishes no universal
placement theorem. The original Stage 37 exclusions and Stage 38 growth
bound retain their stated boundaries; discovery-only exclusions are not
upgraded. The target |4A|>=159 is neither proved nor refuted here.

One clearly distinguished, strictly stronger-than-necessary hypothesis
remains UNPROVED:

    No cubic-protected eight-set in odd 207<=N<248 has BOTH
    70 distinct squarefree quartics and maximum dilation overlap <=5.

The twelve examples and the midpoint-aware absence are weak, biased
discovery evidence. There is no claim that this hypothesis is likely true.
Its universal proof would combine with the existing necessary conditions
to finish the interval, retaining Stage 29's computational dependency.

The less demanding direct target is the following restricted-support
covering lemma, also UNPROVED:

    For every cubic-protected eight-set in odd 207<=N<248 with
    Q4=70 and overlap<=5, s belongs to union_(|B|=4) 8B.

That conclusion supplies an actual rival and need not forbid the input
sets themselves. It names the required cyclic placement fact; the support
cancellation reformulation is not evidence that this covering fact holds.
If full quartic protection is used as an additional hypothesis, it is
enough to cover s with the analogous union over THREE-point blocks.
Neither cover follows from word counts, the hole cardinality bound, or
the observed cohort. A proof must control where the restricted sumsets
lie relative to s. This is where the structural work remains unfinished.

This round meets the requested intermediate-lemma falsification outcome
and executes the requested structural pivot. It does not solve the
original conjecture. No historical exclusions were rerun, no process
remains running, and no earlier PR is merged.

## 8. Reproduction and verification boundary

Run from this directory, using Python with numpy installed:

```text
python -B stage39_cubic_overlap_probe.py
python -B stage39_cubic_overlap_probe.py --collect 32 --output stage39_cubic_cohort_results.json
python -B stage39_cubic_overlap_probe.py --avoid-midpoint --output stage39_midpoint_probe_results.json
python -B stage39_fiveblock_probe.py
python -B stage39_independent_check.py
```

The probe requires numpy. The five-block experiment and separate checker
use only the standard library and import no discovery/historical code.
The single-witness run has a deterministic positive stopping point. The
two capped runs are reproducible schedules whose stopping prefixes and
cohorts can vary with machine speed; their saved mathematical witnesses
are checked directly, without any claim of complete negative coverage.

Evidence is saved in the five correspondingly named Stage 39 JSON files.
The checker uses weak compositions to independently rebuild all primary
cubic, quartic and eight-term fibers, all dilation intersections, every
saved cohort's eight-term rivals, its quintic block validity, all 56 split
tests per set, and the saved near-witness diagnostics. It also checks the
disjoint-support property for EVERY alternative to each squarefree
quartic in the cohort, and the support-cancellation consequences. The
original witness is checked twice (once in detail and once in the cohort).
Together with the control this totals 90090 degree-eight count-vector
evaluations over thirteen distinct cyclic sets. Two deliberately
corrupted rivals, including a mass-preserving wrong-residue vector, are
rejected. The checker does not certify the heuristic search coverage.

The elementary proofs were challenged for padding, cancellation, the
odd-order midpoint step, the erosion sign, nonprimitive support blocks,
and the omitted quintic multiplicity issue. The computational challenges
use separate implementations by the same agent, not independent human
review or a proof assistant. No numerical absence here changes the
proved lower bound or certifies a new modulus exclusion.
