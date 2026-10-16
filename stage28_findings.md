# Stage 28: six-point overlaps have no cycles below 248

Checkpoint, 2026-10-10. The universal theorem remains OPEN.
This is a new restriction on odd h>0 counterexamples, not a restart
of the completed regular path/cycle argument.

## Theorem and scope

Let A be a valid eight-point set with odd cyclic difference subgroup
H of order below248. If |2A intersect(A+t)|=6, then after translating
B=A-t its partial doubling graph consists of exactly TWO paths and
NO cycles. Their vertex counts are 1+7,2+6,3+5,or4+4.

Stage27 excludes larger overlap; cubic packing gives 185<=|H|<=247.
This theorem does not assume h=0 or R3=0, use MC, or rely on external
n=7 certification. Its new finite dependency is a 360-case quotient
replacement lemma, independently checked below.

## Partial-map reduction

Odd doubling is injective, so six edges on eight vertices with indegree
and outdegree at most one give exactly two path components, plus any
cycles. A fixed point would be0; a nonzero doubling edge together with0
gives the forbidden pair equality 2*b=0+(2b), so0 cannot occur.
All cycles have length at least two and sum zero.

With at least two cycles, take both whole paths and one cycle. The
omitted cycles sum zero. This gives fewer than eight terms with the
target sum; repeatedly replace a cycle point by two predecessors to
reach eight terms, still omitting a whole cycle. Validity forbids this.

Suppose exactly one cycle of length c remains, with path lengths L,M.
The sum of the paths is the target. Expanding all path terms into their
first points gives (2^L-1)+(2^M-1) terms with the same sum. If this is
at least eight, stop expansion at exactly eight terms, omitting the
cycle, to obtain a rival. Thus:

|Cycle length c|Path lengths not immediately excluded|
|---:|---|
|2|None (L+M=6; minimum capacity14)|
|3|None (L+M=5; minimum capacity10)|
|4|2+2 only (1+3 has capacity8)|
|5|1+2|
|6|1+1|

The cases below cover every survivor.

## Six-cycle

Six Sidon points have30 distinct nonzero differences. A six-cycle
point has order dividing63, hence its order is63 (all other divisors
are below31). Write J for this order63 subgroup. The only odd multiple
of63 in the contradiction range is189, so H/J has order3.

The two singleton path points x,z generate H/J. At least one of them
is nonzero there; zero,one,or two copies of that point realize any
quotient residue, including the projection of x+z. Use that many path
terms, omitting the other path point. The remaining kernel target is
represented by at most six points of the binary cycle in J (zero by
all six). At least six term slots remain. Cycle expansion reaches
exactly eight terms and produces a rival.

## Five-cycle

Its subgroup J has order31. The only odd multiple in range is217;
H/J has order7. Write the paths as {x} and {z,2z}, with target x+3z.
If z is nonzero in the quotient, it generates that quotient, and
zero through six copies of z represent every residue. Every integer
0..6 is a sum of at most three terms from {1,2}, so at most three
terms from {z,2z} realize the target quotient while omitting x.
If z is zero in the quotient, use just x; the target difference3z
lies in J and both points of the other path are omitted.

The binary five-cycle represents every residue of J with at most
five terms (zero by all five). There are at least five slots left;
expand cyclically to eight. Both cases give a rival.

## Four-cycle and complete finite lemma

Its point order divides15. Four Sidon points have12 distinct nonzero
differences, forcing order15. Thus J has order15 and the only odd H
in range are195 and225. The quotient has order q=13 or15.
The two paths are {x,2x},{z,2z}. Their projected first points generate
the quotient, so gcd(q,x,z)=1. The target projects to3x+3z.

**Checked finite lemma.** For every generating pair x,z modulo q=13
or15, there are nonnegative integers u,v, different from (3,3), with

    ceil(u/2)+ceil(v/2)<=4,
    ux+vz=3x+3z modulo q.

Hence at most four terms from the four path points match the target
quotient with a different path multiplicity pattern. The four-cycle
represents every kernel residue using at most four terms (zero by
the whole cycle). Fill the remaining slots by cycle expansion. This
eight-term multiset differs from the original on the path points.

The producer checks ALL x,z in both quotients with gcd(q,x,z)=1,
and ALL u,v in0..8 satisfying the term bound. The box is exhaustive:
at most four terms of weights1or2 have total weight at most8.
There are168 generating pairs modulo13 and192 modulo15, total360.
Every pair has a witness; every witness is saved. Runtime cap5seconds;
the main run completed (coarse timer0.0seconds).

A separate implementation imports no producer. It enumerates actual
multisets of zero through four terms from four labeled path points,
independently finds an alternative for every one of the360 pairs,
and verifies every saved count vector against the target residue.
Its five-second capped main run completed in about0.016seconds.
Separate implementations are by the same agent, not separate human
reviews or proof-assistant verification. Neither program enumerates
valid eight-point sets or makes a conclusion from passing examples.

## Result and next step

All cycle-containing six-overlap configurations are excluded. Together
with Stage27, every degree-five singleton-tree incidence in an odd
counterexample now comes from a translate whose doubling graph is
exactly two paths. This is a complete structural restriction, not a
proved aggregate Sigma-D budget. The four path-length pairs above
remain necessary symbolic survivors; they have not been certified as
valid sets.

The next focused route is to exploit those two paths and |H|<248.
If they too can be excluded, maximum overlap falls to five and
singleton-forest indegree to four. That stronger cap still needs a
connection to quartic loss; do not infer the target budget from it.
Even h>0 and the antipodal external-dependency milestone remain separate.

## Evidence

    python stage28_cycle_quotients.py
    python stage28_cycle_independent.py

Results: stage28_cycle_quotient_results.json and
stage28_cycle_independent_results.json. Both main runs are COMPLETE,
no numerical process is running, and no historical check was rerun.
This checkpoint will be delivered with Stages26-27 in an unmerged PR.
