# Parity and the seven-point bound

All sets in this chapter are valid for their own size. The protection,
heredity, translation, and subset-cube arguments are defined in
[the proof](../PROOF.md). A normalized set containing zero has 2^(n-1)
distinct subset sums of its other points: replace a larger equal-valued
subset by the smaller and pad with zeros to contradict validity.

## Small non-antipodal bounds

Translate a non-antipodal n-set to contain zero, and let S be its subset
cube, s its full sum. Ordered nonzero differences are distinct: an equality
between two such differences gives an equality of protected pairs, except
that reversing a single pair would mean antipodes. The n translates 2a+A have total incidence n^2. A pair intersects at
most once; if their centers differ by the involution, their intersection
is empty because A has no antipodes. Inclusion-exclusion therefore gives
at least n(n+1)/2 repeated cubic values.

Let E be those repeated cubic values outside A. The replacement argument
shows T3 intersect S=A: a repeated cubic equal to a subset U of at least three nonzero points
would replace U, padding its three-term word by |U|-3 zeros. The resulting
word on the original set differs from the original and has the same
degree and target. For a two-point subset U, compare the cubic to the
protected squarefree word consisting of U and zero. Thus no such U can
have a repeated cubic value. Singletons and the empty subset give A,
and A is contained in 2A+A because zero is available. The sets S,E,s-E
are pairwise disjoint for n>=6: E misses S, S=s-S, and an intersection
of E with s-E represents s with six terms and a nonzero repetition.
Padding by n-6 zeros yields a rival. Thus the six-point bound used below is

    |<A-A>| >=32+2*(21-6)=62.

For clarity, for the eight-point bound the disjointness E intersect(s-E)
follows by padding their six-term union with two zeros. If this padding
were the original squarefree word, it would contain a repeated zero,
which is impossible. This also applies to any repeated representation.

## Seven points without antipodes

The normalizations used in the following enumerations are justified by the
lemma below. A set is **primitive** when its differences generate the whole
cyclic group. The pair-Sidon filter means that squarefree pair sums are
distinct and avoid doubles; the non-antipodal filter is imposed separately.

### Normalization lemma

If the order has at most two distinct prime divisors, a primitive set has
a unit difference. For a prime power this follows immediately: otherwise
all points agree modulo its prime. For two primes p,q, suppose every pair
has a nonunit difference. Pick two points disagreeing modulo p. They must
agree modulo q. Any third point disagreeing with them modulo q would have
to agree modulo p with both, which is impossible. Hence all points agree
modulo q, contradicting primitivity.

More generally, a nonzero difference t can be carried by multiplication by
a unit to g=gcd(t,M). Write t=g*t0 and M=g*M0, so t0 is invertible modulo
M0. Choose a multiplier inverse to t0 modulo M0, and choose its lift to
avoid zero modulo every prime dividing g but not M0. The Chinese remainder
theorem makes these choices simultaneous, and the resulting multiplier is
a unit modulo M. Thus translation and unit scaling give a root {0,g}.
Checking every proper-divisor root covers sets without unit differences.
The other points must range over all residues outside the root, including
points smaller than g. When a unit difference exists, g=1 suffices.

## Complete reduction

Let A be a valid non-antipodal seven-set in Z/M, M<=123. Its64 subset
sums force M>=64. Each six-subset B is valid and non-antipodal. The
elementary bound |<B-B>|>=62 is proved in the two-plus-six parity lemma:32 subset sums and
two disjoint exterior-cubic sets of size at least15. Every proper
subgroup of Z/M has size at most61, so B generates the whole group.

Translate B to contain0. If7B fills Z/M, a seven-term representation
of sum A using only B omits the seventh point and contradicts validity.
Therefore enumerate every primitive non-antipodal valid six-set with
7B not full. Normalization by unit pairs or by all gcd divisor roots
covers these sets, as in the two-plus-six parity lemma. Prefix validity is exact; a full
7-fold prefix sumset stays full for every extension because0 remains.
This is a NEW seven-fold family, not a rerun of the two-plus-six parity lemma's eight-fold
saturation result. The inherited producer output label 'full8' counts
the seven-fold pruning in this stage.

## Saturation is not universal: retain every survivor

The complete family has58 normalized six-point survivors:30 at121,
10 at122,18 at123, and none at64..120. Each has exactly one missing
seven-fold residue. Consequently the blanket intermediate assertion
7B=Z/M is FALSE; the witnesses and missing residues are all preserved.
For example B={0,1,3,7,15,31} in Z/121 misses120 in7B.

If x is the seventh point, sum B+x must be one of those missing
residues. Thus each survivor leaves exactly one possible x. The
58 resulting extensions are ALL invalid, with explicit nonnegative
seven-term count vectors saved. For the example, x=63 and the rival
counts (0,0,2,0,1,1,3) have the same target modulo121.
This final extension exclusion is essential; the six-point survivors
are not discarded or falsely labeled impossible.

The verifier freshly enumerates every order 64 through 123. It retains
all 58 six-point survivors, reconstructs every proposed seventh point,
and checks the explicit rival for each extension. The old saved survivor
list is a consistency control, not a substitute for fresh coverage.

## Antipodal projection and lifts
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
by the two-plus-six parity lemma's elementary bound. The six-set must therefore itself
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

[antipodal_lifts.py](../verification/checks/antipodal_lifts.py) enumerates all 139,503 five-subsets containing zero in
orders 16 through 30, checks their validity, and reconstructs the six affine
classes. It checks all 480 six-lifts, all 192 seven-lifts, and all 668
saved rival identities. Together these two cases prove the seven-point
minimum is at least 124. Neither case uses the eight-point baseline.

## The elementary eight-point baseline

An antipodal eight-set is already excluded below 248 by the seven-point
bound. Assume no antipodes and normalize zero into A. Its subset cube S
has 128 elements. There are at least 36 repeated cubic values, so E has
size at least 28. Disjointness of S,E,s-E gives N>=184.

Here are the boundary refinements needed to reach 187. The 64 cubic words
are eight translates 2a+A. Each pair of translates meets in at most one
point. If |E|=28, equality holds in the pair-union bound, so every center
pair has a collision; equivalently 2*Delta is contained in Delta.

For an even order, let a,b be the two parity counts of A. A pair of translates centered in 2A can intersect only through a
same-parity pair of tail labels. Fix one such unordered tail pair, whose
even nonzero difference is not the involution because A has no antipodes.
The equation 2(x-y)=that difference has at most two preimage differences;
each has at most one ordered representation in A. Thus this tail pair
accounts for at most two unordered center pairs. The total pair-intersection
count is at most 2[binom(a,2)+binom(b,2)]. Inclusion-exclusion gives
|E|>=64-8-2[binom(a,2)+binom(b,2)]=2ab.

If S,E,s-E partition an even cyclic group, its total sum is N/2. Pair
complementation makes sum S=64s, while sum E+sum(s-E)=|E|s.
Hence (64+|E|)s=(N/2)s=N/2, and s is odd. The parity split is therefore
1+7 or 3+5. The former is impossible below 248 by the seven-point bound
in the half-order group, while the latter has |E|>=30.

At N=184 the partition is exact and |E|=28, so this excludes 184.
At N=185, again |E|=28. Doubling permutes Delta, which has size 56.
The nonzero doubling orbits modulo 185 have sizes 4,36,36,36,36,36.
No union of these sizes is 56, excluding 185.

At N=186, |E| is 28 or 29. If it is 29 the partition is exact and the
preceding parity argument excludes it. If it is 28, the bound 2ab leaves
only 1+7 or 2+6, apart from 0+8 which cannot fit 128 subset sums into
93 residues. The seven-point bound excludes 1+7. Translate the 2+6 case
to make six labels even and two, u,v, odd. Then s is even, S has 64
elements in each parity, and E,s-E are disjoint within each parity of
size 93. Thus each parity of E has size at most 14, and both have size14.

The odd-output part of 2A+A consequently has 14+2=16 values. There are
exactly 8*2=16 odd-output words, so they are all distinct. But 2*Delta is contained in Delta because |E|=28. Its even part is
therefore invariant under doubling, which permutes the even subgroup of
order 93. The even nonzero difference v-u therefore
equals 2(a-c) for some distinct a,c in A. It follows that
2a+u=2c+v, a collision of two odd-output words, a contradiction.
This excludes 186 and proves N>=187.

## The three even parity families

Now write N=2M<248. The baseline restricts M to 94..123. Projection
excludes antipodes; the seven-point bound excludes 1+7 and subset sums
exclude 0+8. It remains to check the following three families.

## The two-plus-six case

Translate so that the two minority points are even. Write them as 2c,2d,
and the six odd points as 2b+1 for b in B. All quotient calculations in
this case are in Z/M, with M=94..123.

### Reduction to a six-point sumset

B is a VALID six-point set: any six-term rival modulo M lifts to a
six-term rival among the odd points modulo2M, and adding the two even
points gives an eight-term rival. B is non-antipodal, since antipodes
in B lift to antipodes in A.

Its difference subgroup J has order at least62. For completeness,
translate a six-point set to include0. Its subset sums S have size32.
The non-antipodal difference lemma and the union bound above give at least21 repeated cubic values. The replacement lemma gives T3 intersect
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

The fresh two-plus-six enumeration covers every required quotient order and leaves no primitive six-point survivor.

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
the exact number of copies of the newly added point, as in the two-plus-six parity lemma;
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

## Coverage contract

The current verifier runs each order in a fresh process, with a separate
completion record and a fingerprint of the enumeration code. It checks
all 30 orders in each parity case and all 60 in the seven-point case.
Every four-plus-four residue preimage is retained, including nonunits.
The resulting 51,168 opposing shapes are checked in full. The historical
timing and discovery reports in the source material have no role in the
completion decision. A timeout, missing order, or retained counterexample
fails the full command.
