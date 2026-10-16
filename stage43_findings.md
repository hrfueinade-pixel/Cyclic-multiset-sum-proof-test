# Stage 43: the entire four-doubling-pair quintic family is excluded

2026-10-11. Continues Stage 42 / open PR #14, whose live head was checked
at archived-source. Earlier PRs remain unmerged.
The workspace remains an archive without a local Git checkout.

**The full N>=248 theorem remains OPEN.** This stage proves Stage 42's M1,
not M2. No new arbitrary odd modulus is excluded. All odd 207..247 remain
open in the general theorem, and historical discovery-only exclusions are
not promoted. The target is N>=248; equality is possible.

## 1. New theorem and consequence

**Theorem.** No valid eight-element set in an odd group of order N<248
can be translated to

    A={c0,c1,c2,c3,2c0,2c1,2c2,2c3},                (F)

with eight distinct labels. This is a complete computer-assisted exclusion
of this symbolic family, uniform in its group parameters. It is not a
residue-set search. The proof even works for odd finite abelian groups;
the cyclic case requested here is included.

**Corollary.** In every hypothetical valid eight-set in odd N<248, each
quintic fiber has at most THREE ordinary representations 2a+b+c+d with
four distinct labels.

Stage 42 proved that an ordinary quintic center is private: its occurrence
in another representation would, after cancellation, violate squarefree
quartic protection. Four such centers force the other four labels to be
their four complementary three-subsets. The equations yield 2ci-bi=z;
translation by z gives bi'=2ci', exactly (F). Five ordinary representations
are impossible because their five private centers leave only three tail
labels and one available triple. The new theorem therefore proves the
corollary. Translating preserves validity and every same-degree value count.

This closes the general family left unresolved in Stage 42, rather than
assuming it is a chain. It does not imply ordinary quintic cap two or the
global cubic--quintic bound.

## 2. Packing forces simultaneous cubic collisions

Full validity gives protected squarefree sums and exact complementary
packing. In odd N<248,

    |T4|<=88,
    |T3|+|T5|<=191.

These follow respectively from N>=71+2|T4| and N>=56+|T3|+|T5|.
They do not use a discovery-only exclusion, a prior minimum, or cancellation
by three.

For (F), let p=(p0,...,p7) be a count vector and define its formal four
coefficients by

    M(p)=(p0+2p4,p1+2p5,p2+2p6,p3+2p7).

The target coefficient vector is b=(3,3,3,3). The 64 repeated cubic words
have 58 distinct formal vectors. Six pairs coincide identically because
2ci+(2cj)=2cj+(2ci). The inherited Stage 42 positive quintic certificate
proves |T5|>=135 for (F), using only odd cancellation by two. Thus a
hypothetical counterexample requires |T3|<=56: at least one additional
cubic equality is forced. Formal values are not presumed distinct in G.

## 3. Complete first-relation inventory

Take every pair of different formal cubic vectors. Their 1653 differences
are classified up to sign and permutation of the FOUR PAIRS, canceling only
their common powers of two. There are exactly 50 direction types.

For 34 types, an explicit non-original nonnegative eight-term word p gives

    M(p)-b=k*d

for a nonzero signed integer k and the safely normalized difference d.
If d vanished, p would be a rival. The saved inventory supplies each word
and k. No absence claim from a search establishes these exclusions.

The other 16 types have complete group parameterizations. For 13, positive
certificates force at least 89 repeated quartics, contradicting |T4|<=88.
The quartic bounds, in inventory order r00..r15, are

    102,92,92,91,94,89,90,85,89,95,93,89,95,89,87,85.

Only r07,r14,r15 survive this quartic argument. Up to pair permutation
and sign, their equations are precisely

    I:   4ca=cb,                 a!=b;
    II:  5ca=cb+4cc,             a,b,c distinct;
    III: 4ca+cb=cc+4cd,          a,b,c,d distinct.

The other 13 are genuinely excluded by positive growth witnesses; these
three are not inferred impossible from small discovered cliques.

### Why parameterization loses no nonunit branch

If a relation coefficient is a signed power of two, choose it as pivot.
Writing the other centers as that power times arbitrary parameters gives
an integer formula for the pivot center. In an odd group this parameter
change is surjective because those powers are units.

Three types need special handling:

    3(c3-2c0)=0: c3=2c0+delta, 3delta=0;
    5(c3-c0)=0:  c3=c0+delta, 5delta=0;
    5c3=6c0:    t=c3-c0 gives c0=5t and c3=6t.

The first two retain an explicit torsion coordinate; they do not cancel
three or five. The last uses the two displayed integer identities, with
no division by five or six. All three receive quartic bounds >=89.

## 4. One independent extra equality is insufficient

Consider the rational span of ALL actual equalities between different
formal repeated cubic vectors. This is a classification of the equalities
that occur, not an assertion that G embeds in a rational vector space.

If the span has dimension zero, |T3|=58 and 58+135>191.
If its dimension is one, its direction is I, II, or III, by Section 3.

For II or III, the one-relation integer model has exactly 57 formal cubic
values. If two of those different values coincided in G, their original
coefficient difference would be independent of the first relation, contrary
to the dimension-one assumption. Thus |T3|=57, and 57+135=192 contradicts
the small-order packing.

For I, the corresponding one-chain model has exactly 54 formal cubic
values. The same independence argument makes |T3|=54 in the dimension-one
case. The inherited Stage 42 one-chain certificate gives |T5|>=142, so
54+142=196>191. It uses only powers of two, even when 3 divides N.

Consequently at least TWO rationally independent cubic relations of types
I, II, III must occur. This is the new simultaneous-collision mechanism.
It does not assign separate quintic outputs to different cubic fibers.
All six reused-output configurations from Stage 42 remain accounted for
as identical formal vectors and cannot be double-counted as fresh values.

## 5. Complete two-relation closure

Types I, II, III have 12,24,12 distinct directions after identifying signs:
48 total. Every two different directions are rationally independent.
Their 1128 unordered pairs have 57 orbits under joint permutation of the
four pairs, sign changes of the two equations, and swapping the equations.

The checker independently reconstructs EVERY direction and pair orbit.
It verifies that each supplied model has exactly its stated two relations
and that the matching certificate was made for that exact model.

For the first equation, a unit pivot gives three free parameters. Substitute
into the second, obtaining a row v of three integers. An explicitly saved
integer matrix U with determinant +/-1 gives

    vU=(g,0,0), where g=gcd(v).

The inverse of U is integer, so this coordinate change is valid over every
abelian group. The two zero coordinates are free and the first satisfies
g*delta=0. Only the common powers of two in g are canceled. Its odd part
is retained as torsion, including orders 3,5,9,15,17,21. No odd prime is
inverted. Every actual solution of both equations has this form.

All 57 models are closed by positive evidence:

- 27 have an explicit non-original eight-term word whose formal value
  equals b identically, including the torsion coordinate.
- 30 have selected sets of at least 89 repeated quartic words. For every
  selected pair, an explicit eight-term rival would follow from equality.

The direct rivals contradict validity. The growth cases contradict |T4|<=88.
Combined with the forced rank-two step, this proves the theorem for (F).
No maximum-clique calculation or timeout is a premise of the proof.

## 6. Verification and independent challenges

All positive witnesses are packed in stage43_certificates.json.gz. The
standalone checker imports NONE of the inventory, parameter construction,
or discovery modules. It independently uses count compositions to rebuild
the 58 cubic values, all 50 first-direction classes, the 48 allowed final
directions, and all 57 joint orbits.

For each growth pair it checks a mass-eight nonnegative rival different
from allones and the multiplied equation

    r*(M(p)-b)=k*(M(left)-M(right)),

with integer equality in the free coordinates and congruence in the torsion
coordinate. Here r is a product of the declared unit primes and k is a
nonzero signed integer. The MAIN proof uses only r=2^j. Oddness cancels r;
k is multiplied, never inverted.

Across the 83 retained files, including the exploratory cases below, it
checked 282437 new pair records and rechecked 19056 inherited pair records.
It also checks every direct rival. Wrong mass, original words, a zero
multiplier, and an undeclared factor seven are rejected by corruption
controls. Parameterizations, unimodularity, gcd reduction, and the equality
between each coverage model and its actual certificate are checked.

Manual deductive challenges: formal distinctness is invoked only in the
explicit rank-at-most-one case; relation signs and permutations act on
centers AND doubles together; torsion is kept when unit pivots fail; the
gcd matrix is invertible over the group, not merely over Q; packing needs
FULL validity; and model coverage is exact rather than sampled. No distinct
witness, disjoint output, or injective charge is assumed.

Two retained quintic diagnostics for r07/r14 gave 143/144 rather than 156.
The r14 diagnostic declares units {2,3}; its quartic87 bound first forces
odd N>=245, making three invertible under N<248. Neither diagnostic enters
the proof above. Their incomplete discovery cannot exclude a configuration.

This is computer-assisted proof with a separate implementation by the same
author, not independent human review or formal proof-assistant verification.
No novelty claim is made. No earlier search was restarted.

## 7. Attempt at the remaining global case: three ordinary quintics

After closing (F), a hypothetical counterexample has ordinary quintic cap
three, total cubic cap three, and ordinary quartic cap three. These local
caps do NOT establish |T3|+|T5|>=192.

A fiber with three ordinary quintics has three private centers and five
other labels B. Its tails are three different three-subsets of B. Their
complements in B are three distinct edges on five vertices. There are four
graph types: triangle, star, path of length three, and a two-edge path plus
a disjoint edge. This includes reused labels and unused tail vertices.

Normalize B to (0,2u,2v,2w,2t). Writing the common quintic value minus sum B
as 2z makes each center z plus the half-sum of its omitted edge. This gives
four five-parameter models, with no nonunit normalization.

| Tail-complement graph | Formal cubic values | Positive T4 bound | Positive T5 bound |
| --- | ---: | ---: | ---: |
| triangle | 62 | 68 | 121 |
| star | 61 | 67 | 119 |
| path | 62 | 67 | 120 |
| two-edge path plus edge | 63 | 73 | 126 |

Each discovery retained its fixed two-second cap, without increasing an
earlier timeout. All positive pair witnesses are checked, but NONE of
these bounds closes its model. Even granting no additional cubic collision,
the cubic-plus-quintic sums are only 183,180,182,189. In contrast to (F),
these certificates do not force a new cubic equality. That is the exact
failure of extending the rank-two argument directly to these four shapes.

The classification accounts for all three-ordinary fibers, not all possible
quintic fibers: fibers with fewer ordinary words and nonordinary 5/41/32/
311/221 words remain. Merely counting 280 ordinary words with cap three
gives 94 output values; the 456 nonordinary words can reuse those values.
No fresh contribution or disjointness has been proved.

## 8. Current missing step and continuation

M1 is now CLOSED. The remaining objective is M2: for a full-valid eight-set
in odd 207<=N<248 with |T4|<=88 and the three proved multiplicity caps,
prove |T5|>=156-h-R3, or directly construct an eight-term rival.

The immediate unresolved structural restriction is a coupled closure
condition across different quintic fibers, or between the three-ordinary
models and their extra quartic equalities. The four local five-parameter
models above are not excluded, and their formal cubic counts cannot force
that extra relation from current quintic bounds. A successful next step
must use actual quartic/quintic compression jointly, including mixed-word
fibers; repeating the single-fiber clique run with a larger cap would not
establish this coupling.

The full goal remains ACTIVE and unachieved. No claim is made that the
problem is reduced to a few numerical moduli. Discovery-only historical
orders remain open, no processes remain running, and no PR is merged.

## 9. Reproduction

Check the shipped bundle without discovery:

```text
python -B stage43_certificate_check.py
```

Regenerate the fixed symbolic inventory and positive witnesses:

```text
python -B stage43_fourpair_inventory.py
python -B stage43_relation_growth.py
python -B stage43_joint_relations.py
python -B stage43_relation_growth.py --model r07 --degree 5 --target 156
python -B stage43_relation_growth.py --model r14 --degree 5 --target 156 --units 2,3
python -B stage43_three_quintics.py
python -B stage43_three_quintics.py --degree 5 --target 156
python -B stage43_pack_certificates.py
python -B stage43_certificate_check.py
```

Each clique discovery has a fixed two-second cap. Joint discovery reuses
an existing positive certificate for the SAME exact model when present;
it does not restart that search. The proof depends on the shipped positive
witnesses, not on later reproducibility of a capped search's stopping point.
Scripts use the standard library; only the generic clique helper is imported
from Stage 41. No group parameters, cyclic sets, or moduli are swept.

Delivery continues the existing stack on a new PR based on PR #14's head.
