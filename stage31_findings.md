# Stage 31: even parity split 3+5 is impossible below 248

Checkpoint, 2026-10-10. A second entire remaining h>0 parity branch
is now excluded. The universal theorem remains OPEN; the result uses
no MC, h=0 premise, or external seven-point certification.

## Theorem and exact necessary conditions

A valid non-antipodal eight-point set in an even difference subgroup
H with |H|<248 cannot have parity split3+5. Write |H|=2M, so the
elementary eight-point bound puts M in94..123. Translate so the five
points are odd and write A=(2B+1) union2C with |B|=5,|C|=3.
Both blocks are hereditary valid and non-antipodal modulo M.

Let s=sum B and t=sum C modulo M. The target is2(s+t)+5. Rivals with
q odd points, q=1,3,5,7, require respectively

    s+t+2 in B+7C,
    s+t+1 in3B+5C,
    s+t   in5B+3C,
    s+t-1 in7B+C.

For q=5, the unique permitted factor sums are s in5B and t in3C.
Any other three-term C multiset with sum z must satisfy s+t-z
NOT in5B. Thus all nine repeated three-term deviations z-t lie in

    G={s-r:r not in5B}.

Write C=c0+{0,u,v}, 0<u<v and c0+v<M, using the least ordinary
residue of C as c0. Its six differences and three pure-cube deviations
must all belong to G:

    +u,-u,+v,-v,+(v-u),-(v-u),
    -u-v, 2u-v, 2v-u.

These exactly enumerate its nine repeated cubic multisets. They also
ensure validity of C's all-ones target, since0 is not in G.

For q=7, all three two-point sums of C must belong to

    F=(Z/M minus7B)-s+1.

Equivalently 2c0 belongs to the intersection

    (F-u-v) intersect(F-u) intersect(F-v).

These are necessary conditions for EVERY counterexample. The full
completed result actually eliminates C using only q=5 and q=7;
the q=1/3 calculations are never needed in the final exclusion.

## Proper-subgroup restriction obtained during discovery

The odd five-block B need not generate Z/M. Its difference subgroup
J has order at least30. Normalize0 into B. Its subset sums S have
size16. Pair uniqueness and at most10 cubic pairs give |T3|>=15,
so E3=T3 minus B has size at least10. The four nonzero doubled
points form E2 outside S. S,E3,s-E2 are pairwise disjoint: the last
two cannot meet because repeated three-term and two-term multisets
would concatenate into a rival for the five-point target. Hence

    |J|>=16+10+4=30.

If5B fills its J-coset, any competing three-term C multiset in (Z/M)/J
can be corrected by five B terms. Thus C projects to a VALID
three-point set in (Z/M)/J. Projected repetitions are impossible
for the same reason. For M<=123 and proper J, its index is at most4.
There is no valid three-point cyclic set in order1..4: repetitions
give a replacement, the whole Z/3 has a pure-cube rival, and each
three-subset of Z/4 is a three-term arithmetic progression whose
middle point taken three times is a rival. Therefore every proper
block with5B filling J is excluded without enumerating C.

## Complete normalized block coverage

Translation and unit scaling put any block with a unit difference
into the root{0,1}. A block with no unit difference can put any
selected nonzero point into its gcd g with M, a proper divisor.
All these roots are included, retaining only unitless prefixes when
g>1. This partition covers proper and primitive blocks alike. No
six-point primitivity argument is imported into this stage.

The three other points range over every increasing choice outside
the root, including points below g. Prefix validity is decided by
the exact number of copies of the newly added point, as in Stage30;
all pair differences must be distinct and non-antipodal. If7P fills
the group, every extension fills7B and gives a q=7 rival, so that
prefix is safely pruned.

For every surviving five-block, all normalized even-triple shapes
are checked. A bitset implementation intersects the linear residue
conditions above; it makes no probabilistic claim and does not omit
shapes for having no preferred orientation. The doubled-base equation
is solved with every preimage when M is even; c0+v<M makes every
ordinary C triple have a unique selected base point.

All30 half-orders94..123 completed with ZERO candidate even triples
after the q=5/q=7 conditions. The180-second main cap was stated before
execution; this complete run took about114.734seconds. Per-modulus
block, proper-subgroup and shape counts are saved. There is no actual
counterexample or unresolved final symbolic C survivor.

## Independent verification of the new claim

The separate program imports no producer. It builds sumsets by an
explicit union over counts of the new point, enumerates graph triangles
in the allowed difference set, checks pure-cube deviations scalarly,
and verifies all nine actual repeated cubic multisets. For each shape
it loops directly over EVERY possible c0 with c0+v<M and checks all
three pair sums against F. It uses neither doubled-base intersection
nor modular division.

All30 orders completed again in about94.578seconds under the stated
240-second cap. Block counts, proper-subgroup exclusions and shape
counts agree at each order. Every one of the7,986 shapes surviving
q=5 is preserved explicitly in stage31_even_independent_results.json,
with its B, normalized C shape and empty compatible-translation list.
Separate implementations are by the same agent, not separate human
reviews or a proof-assistant check.

## Timeouts, pivot and remaining obligations

The first90-second run completed NO order: it explored8,705,104 pair
sum triples in the top order before timing out. Every actual Sidon
candidate it reached already had a q=5 rival. That timeout is saved
as stage31_initial_timeout.json and is INCONCLUSIVE.

The next90-second shape-based run completed orders123,122,121 before
timing out. Its partial state is saved as stage31_shape_timeout.json.
It is not used to claim exclusions of its unfinished orders. The
final bitset-intersection run has new complete coverage of every order,
and its first three counts match the saved scalar shape computation.
Both earlier scripts are retained with their evidence.

This route progressed by deriving the proper-subgroup and full nine-
deviation restrictions, then eliminating the expensive translation
enumeration. No historical certificate was rerun. It closes3+5 rather
than merely tightening an overlap statistic.

Together with Stage30, the even2+6 and3+5 branches below248 are now
closed without external n=7 certification. The even4+4 branch remains
required; even1+7 and antipodes retain their separate external boundary.
Odd h>0 still needs its own proof. The universal248 theorem remains open.

## Reproduction

    python stage31_even_three_five.py
    python stage31_even_independent.py

The current discovery cap is180seconds and independent cap240seconds.
Both main results are COMPLETE. Intermediate timeouts are archived
separately. Deliver this checkpoint in a new unmerged PR based on PR#8.
