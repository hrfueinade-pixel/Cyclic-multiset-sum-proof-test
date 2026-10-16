# Stage 48 triangle contribution: the global inequality needs the quartic budget

2026-10-11. Independent paired-star track. The target remains N>=248, with
equality allowed. No historical exclusion or Stage 45 assignment is changed.

## Proposed conditional allocation

Write k=h+R3, C4tri for ordinary quartic triangle values, C5split for ordinary
quintic split-triple values, C3ord for ordinary cubic triples, C4split for
ordinary quartic split-triple values, and F4 for quartic values having exactly
two ordinary representations whose tails are disjoint. The proposed bound is

    5*C4tri+4*C5split <= 2k+2*C3ord+5*C4split+F4.       (TARGET)

This report does NOT prove it under T4<=88. It exhibits a concrete full-valid
counterexample when that budget is omitted, even retaining the three local
multiplicity caps. Thus a proof from local caps and paired-star inverses
alone is impossible.

## First triangle-only attempt: charge its cubic collisions

A triangle

    2x+b+c=2y+a+c=2z+a+b

is equivalent to the alignment 2x-a=2y-b=2z-c. Its three pairs, after
removing their shared tail labels, give three ordinary cubic collision pairs:

    2x+b=2y+a,  2x+c=2z+a,  2y+c=2z+b.

Those are genuine pair incidences. Each ordinary cubic pair has four unused
labels and therefore four ordinary quartic lifts, with a recoverable inverse.
This gives only 3*C4tri<=4*P3ord. It does not justify a weight-five charge,
since the same cubic pair can feed several different quartic triangle values.
Neither k nor C3ord directly counts distinct unused lift slots. The precise
gap is an allocation controlling the reused cubic-pair lifts, with explicit
compensation from C4split or F4; no such injection follows from the inverse.

## Second attempt: use paired-star mixed caps as compensation

Stage 47 gives two different star outputs for each triangle, each with at
most four mixed words. Its inverse proves that these output pairs are disjoint.
This is an UPPER bound on representations at the already existing ordinary
outputs. It is not a LOWER bound on new mixed-only values. All remaining
nonordinary words may also use path/split or two-ordinary outputs; there is
no proved allocation showing that each triangle consumes five globally
distinct units of slack in TARGET. Assuming that allocation would beg the
main compression question.

## Targeted positive counterexample

To distinguish "the local data imply TARGET" from "the small quartic budget
must enter a further global argument", inspect the ONE fixed cyclic set

    A=(0,101,303,707,1515,3131,6363,1) modulo 12827=101*127.

The first seven labels are the binary seven-set
101*(0,1,3,7,15,31,63) in a subgroup of order 127. Projection modulo 101
forces the eighth label's count to be one in any mass-eight representation
of the original sum, since its count is between zero and eight. Dividing
the remaining subgroup equality by its explicit coordinate identification
leaves the original binary seven-set problem modulo 127. This is not
cancellation of 101 as a unit in the ambient group; it is the isomorphism
Z/127 -> subgroup, t ->101t.

For that seven-set, add one to every label: the weights are 1,2,4,...,64.
Seven power-of-two coins at the original target have positive sum divisible
by 127, bounded by 448. The possible multiples are 127,254,381, each with
seven binary ones. Any carry decreases the coin count. Therefore equality
of seven coins and seven binary ones forbids all carries. Of the three
multiples only 127 uses available powers without a carry, and uses each once.
This proves the full eight-set valid, with no numerical absence search.

The separate fixed arithmetic check yields

    T3=43, T4=127, T5=260; h=7, R3=0;
    total cubic cap=2; ordinary quartic/quintic caps=3;
    C4tri=7, C5split=C3ord=C4split=0, F4=7.

Thus TARGET becomes 35<=21, which is FALSE. All seven quartic triangle
fibers and all seven disjoint-tail two-ordinary quartic fibers are saved as
positive records. The check exhausts all 6435 degree-eight count words and
independently reconstructs ordinary tail graph shapes and output counts.

This example is NOT below248 and has T4>88. It does not refute the intended
conditional bound. It shows concretely that full validity, all local caps,
the cubic defect identity and exact paired-star inverses do not by themselves
pay for the triangle contribution. The subgroup-based cyclic doubling
structure produces genuine repeated charge reuse; it simultaneously forces
too many quartic outputs to survive the small-order problem.

## Exact remaining gap

The necessary extra statement is budget-sensitive: when T4<=88, exclude or
quantify families of negative-doubling alignments whose cubic-pair lifts are
reused across quartic triangles, enough to obtain the weight-five term after
accounting for C4split and F4. It must also establish compensation for the
quintic split term, rather than treating all triple outputs as stars. The
fixed counterexample shows that this cannot be a lemma merely about local
multiplicity caps. No missing witness is declared realizable, and no
conditional conclusion is inferred from the counterexample's large order.

Reproduce only the new fixed control:

    python -B stage48_triangle_control.py

No modulus/set/parameter sweep, historical entry point or increased timeout
is used. The script is standalone standard-library code. Independent
challenger audit checks the hand validity proof and the declared counts.
