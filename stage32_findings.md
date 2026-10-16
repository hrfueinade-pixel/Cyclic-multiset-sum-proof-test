# Stage 32: the even 4+4 branch is impossible below 248

Saved checkpoint, 2026-10-10. This is a complete computer-assisted
exclusion, independent of h, MC, and external seven-point certification.
The universal eight-point theorem is not established by this checkpoint.

## Reduction and opposing shapes

Write an eight-set as A=(2B+1) union 2C in Z/(2M), with |B|=|C|=4.
The audited elementary N>=187 bound restricts M to94..123. Both blocks
are hereditary valid and non-antipodal if A is non-antipodal. Put
s=sum B and t=sum C. The original target is2(s+t)+4. For q=0,2,4,6,8
odd terms, the relevant quotient sums respectively are

    s+t+2 in8C; s+t+1 in2B+6C; s+t in4B+4C;
    s+t-1 in6B+2C; s+t-2 in8B.

Define G={s-r:r NOT in4B}. Write C=c+D where D={0,u,v,w},
0<u<v<w and c+w<M. Every NON-original quartic multiset from D must
have deviation sum(multiset)-sum D in G. This classifies all34 opposing
multisets before the base calculation. Zero is not in G.

The triple {0,u,v} must have all nine repeated cubic deviations in G:
the six differences and -u-v,2u-v,2v-u. For the fourth point w, the
multisets classified by its multiplicity q impose:

    q=0: w in4{0,u,v}-u-v-G;
    q=1: the nine triple conditions already checked;
    q=2: w in G+u+v-2{0,u,v};
    q=3: 2w in G+u+v-d, for each d in{0,u,v};
    q=4: 3w in G+u+v.

Every residue preimage is retained when multiplication by2 or3 is
not invertible. No division assuming odd M or coprimality is used.
The independent checker instead generates the34 multiplicity vectors
automatically and intersects their linear constraints.

Let K_j be the complement of jB. Necessary q=6 and q=8 conditions are

    2c in intersection over r in2D of (K_6-s-sum D+1+r),
    4c in K_8-s-sum D+2.

The completed independent check finds NO c satisfying these two
conditions for ANY of the51168 surviving quartic shapes. Thus q=0/2
and the remaining whole-set tests are not needed for the exclusion.

## Proper blocks and coverage

A valid non-antipodal four-block has difference subgroup J of order
at least14: its eight subset sums, its three exterior doubles, and
their reflections are disjoint. If4B fills its J-coset, any rival for
C in (Z/M)/J can be corrected using four B terms. C therefore would
project to a valid four-set in a cyclic group of index at most8.
Such a set is impossible: a non-antipodal four-set requires order14;
an antipodal four-set projects to a valid three-set in order at most4,
also impossible. This excludes the proper saturated blocks.

All other B blocks are covered by a normalized unit pair{0,1}, or,
when every difference is nonunit, all proper-divisor roots{0,g}.
The other two points range over all increasing choices outside the
root, including points below g. No primitivity hypothesis is imposed.
Prefix validity uses the exact number of copies of the newly added
point. A full8-fold prefix sumset prunes extensions because0 remains
available for padding and supplies an all-odd eight-term rival.

Every C has its least ordinary residue c and a unique increasing D.
All triple and quartic constraints above are necessary. Therefore
complete absence in this finite family excludes every 4+4 eight-set
at the stated half-orders; it is not a passing-example argument.

## Completed runs and retained evidence

Before computation the scope, coverage, cap and intended exclusion
were stated. The first180-second producer run completed M=123..115
and timed out during114. Its incomplete record is preserved in both
stage32_even_four_four_results.json and stage32_high_orders_results.json.
It establishes no result for the interrupted order. A second180-second
run covered ONLY M=114..94 and completed in148.594seconds. Together
these completed per-order reports cover all30 half-orders.

The independent480-second run completed all30 in453.359seconds. It
imports no producer, updates sumsets by explicit copy counts, derives
the quartic conditions from every multiplicity vector, and checks
ordinary base translations directly. Per-order block, proper-block
and quartic-shape counts agree. All51168 symbolic shapes and empty
base-survivor lists are preserved losslessly in
stage32_symbolic_shapes.json.gz. The independent result is
stage32_even_independent_results.json. Separate implementations are
by the same agent; no formal proof-assistant or separate human audit
is claimed. Neither timeout alone is used as an exclusion.

## Result and next milestone

Stages30,31,32 exclude all balanced parity splits2+6,3+5,4+4, including
the remaining even h>0 branch. To close EVERY even eight-set still
requires a seven-point lower bound for split1+7 and for antipodes.
The next route reconstructs that dependency rather than repeating
settled balanced searches. Quartic loss Sigma-D remains uncontrolled
outside these contradiction ranges.
