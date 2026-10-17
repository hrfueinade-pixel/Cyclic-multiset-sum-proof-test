# Multiplicity caps

This chapter works throughout under full validity, odd order, and N<248.
The packing inequalities and notation are in [the proof](../PROOF.md).
The local models are exclusions under these hypotheses. A growth certificate
contains positive separation witnesses, whose meaning is explained below.

## What a symbolic certificate proves

Each family below expresses the eight labels as integer combinations of
four group parameters u,v,w,z. Let M send a count vector to its four
integer coefficients, and let b=M(allones). For two selected repeated
degree-d words p,q, set D=M(p)-M(q).

Every pair in each certificate supplies a non-original nonnegative count
vector c of mass eight. The checker verifies

    M(c)-b = k*(D/r),                                 (C)

where k is a nonzero signed integer and r is the product of the common
powers of the declared invertible primes removed from D. For the first
certificate in a family those primes are just {2}. Quintic certificates
for the two-step argument use {2,3}.

If p and q had the same actual group value, then D would vanish in the
group. Since multiplication by r is invertible, D/r would vanish too.
Equation (C) then forces the explicitly supplied c to represent s, a
rival. Thus every selected pair has different values. This proof works
for ALL choices of the group parameters and needs no normalization by a
unit parameter, no primitivity assumption, and no parameter coverage.

An arbitrary integer multiplier k is safe: it is not divided out. Only
the declared units are canceled. This distinguishes the certificate from
an unjustified division by a nonunit. The checker verifies every count
word, all pairs, every scalar equation and its degree. It imports no
discovery code or historical kernel.

The retained compressed JSON files contain the selected words and one rival
for every unordered pair, in combination order. The gzip format merely
keeps the certificates small; Python's standard library reads them.
Positive witnesses establish the growth bound even when their discovery
stops early or times out. Maximum clique size and search completeness
are not premises of any theorem here.

## Required initial models

The labels below are ordered as in their certificate coordinates. Parameters
are arbitrary group elements. Four retained certificates establish:

| Model | Labels | Bound |
| --- | --- | --- |
| hub22 | 0,2u,2v,2w,z,z-u,z-v,z-w | T4>=90 |
| fourO | 0,2u,2v,2w,z-u,z-v,z-u-v,z-v-w | T4>=87, then T5>=156 |
| purehub | 0,2u,2v,2w,-u,-v,-w,z | T4>=89 |

For fourO, (2) first forces N>=245. The only remaining odd orders below
248 are 245 and 247, so three is now invertible. Only at this point may
the quintic certificate cancel powers of three. Since T3>=36, (1) gives
N>=56+36+156=248. The other two models are excluded directly by (2).
The four certificates are checked by [multiplicity_models.py](../verification/checks/multiplicity_models.py).


## Every fourfold ordinary quartic fiber is now excluded

An ordinary quartic is 2c+d+e with c,d,e distinct. If two different
representations at its value shared its center c, canceling one c from
both would equate its squarefree cubic c+d+e to another cubic. Protection
forbids this. Thus its center is absent from every other representation.

Four ordinary representations consequently have four distinct private
centers and four tail edges on the other at most four labels. The edges
are distinct: equal tails would give equal doubled centers in odd order.
A simple graph with four edges on at most four vertices is connected and
uses four vertices. It is a four-cycle or a triangle with a pendant edge.

In the four-cycle, adding the opposite quartic equations and subtracting
the other opposite pair gives twice an equality of two different
squarefree center-pair sums. Odd cancellation contradicts pair protection.

In the triangle/pendant case, translate one nonhub triangle vertex to zero.
Label the other triangle vertex 2u, the hub 2v and the pendant vertex 2w.
Write the common quartic value as 2z, possible in odd order. Its four
centers are exactly

    z-u, z-v, z-u-v, z-v-w.

All eight labels are accounted for, so this is precisely the fourO model
in the initial-model table. Its uniform two-step growth proof excludes odd N<248.
Therefore every repeated quartic value in a remaining counterexample has
at most THREE ordinary representations.

## Consequences for cubic multiplicities

An ordinary repeated cubic is 2c+d with c!=d. Its center cannot occur in
another distinct representation of its value: if it occurs as another
tail, canceling c equates a squarefree pair to a doubled point; if it is
another center, odd doubling and pair uniqueness identify the words.
Tails of two different ordinary marks are distinct by odd doubling.
A pure cubic's label likewise cannot occur in another mark: 3a=2c+a
would force a=c.

Four ordinary cubic marks therefore use four centers and four tails,
all eight labels. Pick one mark 2z+h and add its tail h to the other
three. They become three ordinary quartics with common hub h, and the
chosen mark becomes 2z+2h. After translating h to zero and halving the
other three tails, the eight-set is the hub22 model. Its 90-value quartic
certificate excludes it below 248. Hence at most three ordinary cubic
marks occur at any value in the remaining odd interval.

If three ordinary cubic marks share a value with a pure cubic 3h,
translate h to zero. Their equations become 2c_i+d_i=0. Write d_i=2u_i,
so c_i=-u_i. These seven distinct labels plus the eighth free label form
the purehub model, also excluded below 248.

At most two pure cubes share one value. Indeed three distinct points with
3a=3b=3c lie in one coset of the order-three kernel. Their squarefree sum
equals 3a, violating cubic protection. If a cubic fiber had at least four
marks, the previous two exclusions therefore leave only two pure and
two ordinary marks. Any larger fiber would contain a forbidden subpattern.

For the cyclic groups of the original problem, there is at most one such
exceptional fiber: two pure cubes require an
ordered difference of order three. A cyclic group's order-three subgroup
has only two nonzero elements; uniqueness of the 56 ordered differences
allows at most one unordered A-pair in it. The pair determines its pure
cubic value. At orders coprime to three there is no exceptional fiber.

Let Delta be the 56 ordered nonzero differences, put
h=|{d in Delta:2d not in Delta}|/2, and put
R3=sum_y binomial(m_y-1,2), where m_y is the total cubic mark multiplicity.
Each center pair whose doubled difference occurs contributes exactly one
coincident cubic pair, so sum_y binomial(m_y,2)=28-h. The new restrictions yield

    R3 <= floor((28-h)/3)+1,

and without the +1 when 3 does not divide N. To check this, let t3,t4 count
fibers with three and four marks. All others have at most two, t4<=1,
R3=t3+3t4 and 3t3+6t4<=28-h. Therefore
R3<=floor((28-h)/3)+t4. This bound still does not prove T4>=89 globally.

## Second serious approach: classify a saturated ordinary quintic fiber

Call a quintic ordinary when it is 2c+b+d+e with four distinct labels.
Its center c is absent from EVERY other representation of its value.
If another word contained c, subtracting one c from both words would
equate its squarefree quartic c+b+d+e to a different quartic. Full validity
forbids that. This holds for nonordinary opposing words too.

For r ordinary representations, their r centers are distinct and private.
Their three-label tails are different: equal tails would imply equality
of doubled centers, and odd order cancels two. The tails lie on at most
8-r labels. For r>=5 there is at most one available triple and at least
five required ones. Thus EVERY valid odd eight-set has at most FOUR
ordinary quintic representations per fiber.

If there are four, the remaining four labels B={b_1,...,b_4} provide
exactly their four three-subsets. Relabel so the tail of center c_i is
B minus b_i. If their common value is t, set z=t-sum(B). Then

    2c_i-b_i=z for i=1,2,3,4.

Translate every label by z. For c_i'=c_i-z and b_i'=b_i-z we get
2c_i'=b_i'. Consequently the eight-set has the form

    A={u,v,w,z,2u,2v,2w,2z},                         (F)

with all eight labels distinct. Here the new parameter z is unrelated to
the preceding translation symbol. No parameter is assumed a unit. No
factor of three was canceled. This is an exact classification, not a
sampled configuration inventory.

The complete quintic-cap argument below excludes this four-pair family. Its first growth bound alone is insufficient; additional cubic relations are forced and covered explicitly.

## Secondary branch closed: no exceptional cubic fiber below 248

If two pure and two ordinary cubes share a value, translate one pure label
to zero. The second is delta with 3delta=0. The ordinary equations give
the six distinct forced labels

    0,delta,c,-2c,e,-2e,

and two remaining free labels u,v. Their distinctness follows from the
private-label and odd-tail arguments of the multiplicity-model lemma. In a cyclic group the
nonzero delta has order three. The model does not require canceling three.

The separate certificate selects 94 repeated quartic words for this model
and supplies an eight-term rival for each of their 4371 unordered pairs.
It works uniformly for all choices of c,e,u,v,delta satisfying 3delta=0.
Therefore, under full validity in odd order,

    |T_4|>=94, and N>=71+2*94=259.

This excludes the exception in EVERY hypothetical odd sub-248 set. Combined
with the multiplicity-model lemma, every remaining repeated cubic fiber now has at most THREE
total representations, and

    R3 <= floor((28-h)/3).

Indeed all fibers have multiplicity at most three, so if t3 is the number
of three-mark fibers, R3=t3 and 3t3<=sum binomial(m_y,2)=28-h.
Two pure cubes alone may still coincide at orders divisible by three.
The result does not make multiplication by three invertible.

### Certificate logic and independent challenge

The exception uses four unrestricted integer coordinates for c,e,u,v and
one coordinate modulo three for delta. If D is the coordinate difference
of selected words, each record supplies c!=allones with nonnegative counts
of mass eight, a nonzero signed integer k, and r=2^j such that

    r*(M(c)-M(allones)) = k*D

in the four integer coordinates and modulo three in the torsion coordinate.
If the selected words had equal actual values, D would vanish. Oddness
then cancels r and the supplied c is an explicit eight-term rival.
The checker verifies this MULTIPLIED equation, avoiding the discovery
code's coordinate normalization. Signed k is multiplied, never canceled.
Modulo-three arithmetic encodes 3delta=0; it does not invert three.

The same witness format checks the doubling-chain models. The independent
implementation imports neither the producer nor the multiplicity-model lemma search code.
It checks all 23,427 pair records across the three required files, including
wrong mass, original-word, zero-multiplier, and wrong-coordinate corruption
controls. This is separate code by the same author, not independent human
review or formal verification. All selected words are repeated, all are
distinct, and all pair equations are checked. No maximum-clique claim is
needed for any theorem.

Deductive checks: private centers use full quartic protection; the six
exception labels are proved distinct before modeling them; no division
by a parameter or by three occurs; the midpoint bound uses full validity;
the four-pair classification covers only a four-ordinary-quintic fiber;
and two disjoint chains are not inferred from arbitrary cubic collisions.

## New theorem and consequence

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

the cubic-exception lemma proved that an ordinary quintic center is private: its occurrence
in another representation would, after cancellation, violate squarefree
quartic protection. Four such centers force the other four labels to be
their four complementary three-subsets. The equations yield 2ci-bi=z;
translation by z gives bi'=2ci', exactly (F). Five ordinary representations
are impossible because their five private centers leave only three tail
labels and one available triple. The new theorem therefore proves the
corollary. Translating preserves validity and every same-degree value count.

This closes the general family left unresolved in the cubic-exception lemma, rather than
assuming it is a chain. It does not imply ordinary quintic cap two or the
global cubic--quintic bound.

## Packing forces simultaneous cubic collisions

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
2ci+(2cj)=2cj+(2ci). The inherited the cubic-exception lemma positive quintic certificate
proves |T5|>=135 for (F), using only odd cancellation by two. Thus a
hypothetical counterexample requires |T3|<=56: at least one additional
cubic equality is forced. Formal values are not presumed distinct in G.

## Complete first-relation inventory

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

## One independent extra equality is insufficient

Consider the rational span of ALL actual equalities between different
formal repeated cubic vectors. This is a classification of the equalities
that occur, not an assertion that G embeds in a rational vector space.

If the span has dimension zero, |T3|=58 and 58+135>191.
If its dimension is one, its direction is I, II, or III, by the first-relation inventory.

For II or III, the one-relation integer model has exactly 57 formal cubic
values. If two of those different values coincided in G, their original
coefficient difference would be independent of the first relation, contrary
to the dimension-one assumption. Thus |T3|=57, and 57+135=192 contradicts
the small-order packing.

For I, the corresponding one-chain model has exactly 54 formal cubic
values. The same independence argument makes |T3|=54 in the dimension-one
case. The inherited the cubic-exception lemma one-chain certificate gives |T5|>=142, so
54+142=196>191. It uses only powers of two, even when 3 divides N.

Consequently at least TWO rationally independent cubic relations of types
I, II, III must occur. This is the new simultaneous-collision mechanism.
It does not assign separate quintic outputs to different cubic fibers.
All six reused-output configurations from the cubic-exception lemma remain accounted for
as identical formal vectors and cannot be double-counted as fresh values.

## Complete two-relation closure

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
