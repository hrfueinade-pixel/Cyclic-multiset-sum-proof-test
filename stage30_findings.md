# Stage 30: even parity split 2+6 is impossible below 248

Checkpoint, 2026-10-10. New computer-assisted exclusion of an entire
remaining h>0 branch. The universal N>=248 theorem remains OPEN.

## Theorem

A valid non-antipodal eight-point set in an even cyclic difference
subgroup H of order less than248 cannot have parity split2+6.
This theorem does not use MC, an h=0 assumption, or external n=7
certification. The finite new dependency is described below.

Write |H|=2M. The earlier elementary eight-point lower bound gives
|H|>=187, hence M=94,95,...,123. Take the minority parity to be even
by translating if necessary. Write its two points as2c,2d, and its
six odd points as2b+1 with b in B subset Z/M.

## Elementary reduction to a six-point sumset

B is a VALID six-point set: any six-term rival modulo M lifts to a
six-term rival among the odd points modulo2M, and adding the two even
points gives an eight-term rival. B is non-antipodal, since antipodes
in B lift to antipodes in A.

Its difference subgroup J has order at least62. For completeness,
translate a six-point set to include0. Its subset sums S have size32.
Pair uniqueness gives at most15 pairs of equal repeated cubics among
36 marks, hence |T3|>=21. The replacement lemma gives T3 intersect
S=B, so E3=T3 minus B has size at least15. Both S and its complement
reflection about s=sum B agree; T3 and s-T3 are disjoint because their
repeated three-term representations would concatenate into a rival
six-term multiset. Consequently S,E3,s-E3 are pairwise disjoint and

    |J|>=32+2*15=62.

As M<=123, every proper subgroup of Z/M has order at most61. Thus B
generates the ENTIRE quotient group. No external six-point bound is
used in this deduction.

Every eight-term sum using only odd points has the form2r+8, r in8B.
The original target is2(sum B+c+d)+6. Thus if8B=Z/M, it contains
r=sum B+c+d-1 and gives an eight-term rival omitting both even points.
Therefore any putative counterexample requires

    B valid, non-antipodal, primitive, |B|=6, and8B not equal Z/M.

## Complete new finite exclusion

The discovery program enumerates exactly these necessary conditions
at ALL30 values M=94..123. Translation puts0 into B. Unit scaling can
normalize any selected nonzero point to its gcd with M, a proper
divisor g. The root is{0,g}; the four remaining points range over all
increasing choices outside the root, including points smaller than g.
For M having at most two prime factors, the elementary two-prime
unit-difference lemma gives a pair that normalizes to0,1. For the
other M, all proper-divisor roots are checked. This reduction discards
no primitive B. No assumption that B contains a unit difference is
made at the three-prime orders.

Each prefix must be pair-Sidon, non-antipodal and hereditary valid.
If P is valid and a new point x occurs q times in a competing multiset,
q=1 reduces to validity of P. For q=0 or2..|P|+1, the required old sum
is sum P+(1-q)x and uses |P|+1-q terms. Exact old sumsets therefore
decide extension validity. Sumsets up to degree8 are updated by the
unbounded-coin recurrence. If8P is already the whole group, every
extension has full8B because0 remains available for padding, so that
entire branch is excluded.

All6,316,572 visited valid prefixes were covered in the main run.
Every modulus completed, with ZERO primitive six-point survivors.
The global60-second cap was stated before execution; the main run
completed in about58.687seconds. Per-order roots, prefix counts and
pruning counts are saved in stage30_even_two_six_results.json.
This is a complete necessary-family exclusion, not a claim based on
passing examples or a timeout.

## Independent check limited to this new promising claim

A separate implementation imports no producer or historical kernel.
It uses a different coverage partition: every set having a unit
difference is affine-normalized to0,1; for all other sets every
difference is nonunit, and every proper-divisor root is considered
while retaining only unitless prefixes. At orders with at most two
prime factors, primitivity excludes the unitless branch by the
elementary lemma. Its sumset update explicitly unions all possible
counts of the new point, rather than using the coin recurrence.

Every order94..123 completed again with zero survivors. The stated
120-second capped main run completed in about70.016seconds. Its
different prefix counts and complete coverage are preserved in
stage30_even_independent_results.json. Separate implementations are
by the same agent, not separate human reviews or a formal proof check.
The finite absence result and its elementary reductions prove the
stated2+6 theorem.

## Connection to 248 and next work

An entire even h>0 parity branch is now closed without the external
seven-point result. The even1+7 branch and antipodes retain that
external dependency; the even3+5 and4+4 branches remain required.
Odd h>0 still needs the quartic collision budget or another direct
small-modulus contradiction. The universal theorem is not proved.

The next direct candidate is3+5. With odd block B of size5 and even
block C of size3, a seven-odd/one-even rival exists if

    sum B+sum C-1 belongs to7B+C.

Its absence forces every two-point sum of C into

    F=(Z/M minus7B)-sum B+1.

This gives a concrete enumeration of C from three pair sums in F,
followed by the remaining one/three/five-odd rival tests. B may have a
proper difference subgroup in this branch; do NOT import the six-point
primitivity proof. Save all such survivors and preserve scope.

## Reproduction

    python stage30_even_two_six.py
    python stage30_even_independent.py

Both main runs are COMPLETE. No process is running. This new research
checkpoint is to be delivered through a new unmerged PR based on PR#8.
