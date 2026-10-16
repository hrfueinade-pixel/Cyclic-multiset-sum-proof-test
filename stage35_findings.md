# Stage 35: antipodal seven-sets and the whole even eight-point branch

Saved checkpoint, 2026-10-10. Together with Stage34 this gives a
self-contained computer-assisted proof: every valid cyclic seven-set
has modulus at least124. It removes the earlier external seven-point
premise. The universal eight-point248 theorem still needs the odd branch.

## Quotient and lift coverage

A valid set contains at most one antipodal pair; two give an equal
sum of distinct squarefree pairs. Project a valid n-set in Z/(2M) with
its antipodal pair identified to Z/M. The resulting n-1 points form a
valid set. A rival downstairs lifts to n-1 points upstairs; adding
one of the two antipodes corrects either possible M-error in its sum.
It remains a rival for the original n-set. Projected coincidences
beyond the one pair would similarly contradict validity.

Thus an antipodal seven-set at modulus<=123 projects to a valid
six-set at order<=61. A non-antipodal six-set requires order>=62
by Stage30's elementary bound. The six-set must therefore itself
have antipodes and project to a valid five-set at order<=30.
The latter has16 distinct subset sums, so its order lies in16..30
and it generates its whole group (proper groups have size<=15).

Every valid five-set at those orders is enumerated INCLUDING antipodal
ones. Applying the non-antipodal ordered-difference filter here would
be incorrect and is deliberately avoided. The producer uses exact
hereditary validity and normalized unit-pair or all unitless divisor
roots. It finds22 normalized rows in six affine classes:

    Z/28: {0,1,3,7,15};
    Z/30: {0,1,3,7,15}, {0,1,3,15,25}, {0,1,4,6,16},
          {0,1,4,16,24}, {0,1,9,15,19}.

For every quotient representative, duplicate each possible fiber in
turn and choose either lift of every other point. This exhausts all
antipodal lifts:5*16=80 six-point lifts per class,480 in total. Four
are valid, all in ONE affine class, represented by

    Z/60: {0,1,3,7,15,31}.

All6*32=192 antipodal seven-lifts of that class in Z/120 are invalid.
Each has a saved explicit seven-term rival. Quotient affine maps lift
to affine maps upstairs: a unit modulo M has an odd unit lift modulo
2M (choose the odd representative when M is odd). The free fiber
choices cover every resulting representative. Thus taking one affine
class per quotient discards no relevant lift.

## Independent completion

The producer30-second capped run completed in0.032seconds. The separate
60-second checker completed in0.625seconds. It enumerates ALL139503
five-subsets containing0 in cyclic orders16..30. Necessary squarefree
pair sums must be distinct and disjoint from doubles; duplicated
doubles, which antipodes permit, are NOT forbidden. Every remaining
five-set is checked against all126 five-term multisets. Its affine
classes agree exactly with the six classes above.

The checker reconstructs all480 six-lifts and192 seven-lifts, checks
their complete multiset validity, verifies all668 integer rival
identities (476 six-term and192 seven-term), and positively certifies
the four valid six-lifts. It imports no producer. Both complete outputs
and every witness are saved in stage35_antipodal_seven_results.json and
stage35_antipodal_independent_results.json. Independent implementation
does not mean separate human review or formal proof verification.
Scopes, coverage arguments and caps preceded both runs.

## Proved consequence for 248

Stage34 excludes every non-antipodal seven-set below124. This stage
excludes all antipodal ones. Hence EVERY valid cyclic seven-set has
N>=124, with the finite dependencies reconstructed in this archive.

An antipodal eight-set projects to a valid seven-set, forcing N>=248.
For a non-antipodal eight-set in even order2M<248, a1+7 parity split
gives a valid seven-set in Z/M, impossible for M<=123. Translation
interchanges the two parities. A0+8 split lies in a coset of a proper
subgroup, impossible because128 subset sums cannot fit when N<248.
Stages30,31,32 exclude the remaining splits2+6,3+5,4+4 for M=94..123.
The earlier elementary baseline excludes smaller moduli. Therefore:

    No valid eight-element cyclic set has an EVEN modulus below248.
    Every antipodal eight-element cyclic set has modulus at least248.

These results cover even h>0 as a separate required milestone and
use neither MC nor an h=0 hypothesis nor published external n=7 data.
Only the odd non-antipodal h>0 branch remains for the universal theorem.
The global quartic inequality and Sigma-D budget have not been proved.
