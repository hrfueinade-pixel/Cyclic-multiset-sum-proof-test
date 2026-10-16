# Stage57: force ordinary cubic relations in the remaining full problem

The full N>=248 theorem remains open. Use the proved general Stage55
assignment q<=h and Stage54 source budget. This argument does not assume
absence of pure cubic collisions.

Write P=P3ordinary, J=P3total-P, c=C3ordinary, t=C4triangle. The general
count and q<=h give

    N>=288+h+R3+2c+2w-2(t+q+P)
     >=260-P+J+R3+2c+2w-2t.                       (1)

Here h=28-P3total. The signs of J and R3 are positive. Adding only pure
cubic collisions therefore cannot lower the right side when the ordinary
cubic partition is fixed.

## Each ordinary cubic pair feeds at most two quartic triangles

An ordinary cubic pair uses four distinct labels. Its two corresponding
alignment edges have a common value 2x-a. Completing it to a triangle
chooses an aligned edge on the other four labels.

By stage56_alignment_cycle_hand_proof.md, an alignment class bearing a
triangle is a path forest, and cannot contain a matching of size four.
Three edges on the remaining four labels would therefore form a directed
path with four vertices. Its first and last edges are disjoint. Together
with the two fixed edges they would give the forbidden four-edge matching.
Thus there are at most two completion edges. Each triangle contributes
exactly three ordinary cubic pairs, so

    3t<=2P.                                             (2)

Combining (1) and (2), if P<=5 then N>=260-7P/3>=248+1/3.
Therefore every hypothetical odd N<248 counterexample has P>=6. This
requires at least six ORDINARY collision pairs, not merely six total ones.

## A robust bound when only the ordinary partition is fixed

Take any exact odd-group relation model. Assume an actual valid small-order
realization adds no equality between different FORMAL ORDINARY cubic
classes. Then P,c,t remain exactly their formal values. Every triangle
requires three ordinary pair descents, so pure collisions cannot create
an additional triangle without an additional ordinary equality. Let
h0=28-P3total(formal) and R0=R3(formal). Actual h<=h0 and R3>=R0.

Using q<=min(h,4P-11c), the least possible value of h-2q over
0<=h<=h0 is -min(h0,4P-11c). Consequently

    N>=288-min(h0,4P-11c)+R0+2c-2t-2P.             (3)

If this exceeds247, an actual counterexample must add an ordinary cubic
equality. Pure-only refinements are insufficient. This justifies branching
on the56 ordinary cubic words instead of all64 repeated cubic words.

## Quintic finishing without a no-pure-collision assumption

From (1) and N<=247,

    J+R3<=P+2t-2c-13.

Since T3=64-P-J+R3, every hypothetical counterexample satisfies

    T3>=77-2P-2t+2c.                                   (4)

This is a GLOBAL inequality. In a fixed ordinary-partition model, a
positive quintic growth proof of

    T5>=115+2P+2t-2c                                  (5)

contradicts T3+T5<=191, even if new pure cubic collisions occur. Thus (5)
also forces an additional ORDINARY cubic equality. A weak quintic bound
proves nothing; no search absence is used.

There is also an unconditional terminal rule. The established identity
T3=36+h+R3 and monotonicity under additional cubic equalities give
T3>=36+R0 for every realization of a model, even when ordinary classes
merge. Therefore a positive T5>=156-R0 proves T3+T5>=192 and excludes
the ENTIRE model. It must be treated as a terminal proof, rather than
merely a reason to add another relation.

For the primary alignment forests (3,3,2) and (7,1), the exact values
(P,t,c) are (8,4,0) and (10,4,0). The new thresholds are139 and143.
The existing positive selected-word certificates give139 and149. Once
their identities are checked, each forest requires a further ordinary
cubic relation, not just a further total cubic relation.

The first triangle inventory has785 ordinary coefficient directions,
closed under the twelve pair/free-label permutations. Its existing positive
closures leave36 ordinary root orbits, rather than63 total-cubic orbits.
That coverage is discovery until a standalone checker validates it. No
entire arbitrary odd modulus or the full triangle family is yet claimed
excluded.
