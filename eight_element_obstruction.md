# Eight-element cyclic modulus: collision obstruction audit

## Outcome and external baseline

The sufficient claim **has not been proved or disproved**:
for valid non-antipodal eight-element sets with N < 248, |E4| >= 60.
The stronger unrestricted non-antipodal bound |E4| >= 63 is also unresolved
here. Neither follows from the experiments. No novelty claim is made.

Sources checked on 2026-10-08:

- [Fonollosa, v2, Section 7](https://arxiv.org/html/2607.08366v2#S7)
  reports exact CP-SAT infeasibility certification for arbitrary residue
  sets, for every subthreshold modulus, through n = 7. Thus its reported
  global seven-element minimum is 124. Beyond seven, it reports searches,
  not exhaustive certification. The all-n main theorem concerns the fixed
  binary set, not arbitrary sets. I verified the scope of the statement,
  but did not obtain/check the CP certificates or rerun that computation.
- The current [author repository](https://github.com/jarfo/min-modulus)
  records Inal's all-finite-abelian minimum 2^(n-1) and equality
  classification, separately from the still-open cyclic conjecture.
  The inspected [scripts directory](https://github.com/jarfo/min-modulus/tree/master/scripts)
  contains the axiom audit, not the reported CP certificate files.
- The [formal-conjectures entry](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/Arxiv/2607.08366/MinModulus.lean)
  still labels the general cyclic statement open. No Lean was run.
- [Cambie--Gao--Kim--Liu](https://arxiv.org/abs/2308.03748) studies modular
  distinct subset sums near the cube-size threshold. Its stated
  asymptotic/near-threshold results do not directly supply the finite
  repeated-four-term estimate needed here. No later proof of the
  eight-element claim was located in these sources or targeted searches.

**Conditional on the paper's reported seven-element certification, the
antipodal eight-element case already has N >= 248**, by the elementary
quotient proof below. This is an external computational dependency, not
a self-contained elementary proof of that case. The older report's
218/220 estimates are weaker and are not the correct best baseline when
this dependency is allowed. Its endpoint exclusions are not used here.

## Audited elementary proofs

Work in Z/NZ with A = {0} union B, |B| = 7, and s = sum B.
Translation preserves validity because every candidate has eight terms.

**Replacement lemma.** If a subset U of B has size r and a nonnegative
multiplicity vector h on B, of length l <= r+1, has sum equal to sum U,
then h is exactly the indicator of U. Indeed, give each b in B
multiplicity 1 - 1_U(b) + h(b), and give zero multiplicity 1+r-l.
These are nonnegative, total eight, and sum to s. Validity forces the
all-ones vector, proving the assertion. For two equal subset sums, take
the larger subset as U and the smaller as h. Thus subset sums are
injective, |S| = 128, and complementation gives S = s-S.

**Exterior identity.** Define T4 = {2a+b+c : a,b,c in A} and let L2
consist of the subset sums of B using at most two elements.
Then T4 intersect S = L2 and |L2| = 1+7+21 = 29.
The inclusion L2 subset T4 follows by using doubled zero and padding the
two remaining slots with zeros. Conversely, suppose a four-term repeated
representation equals a subset sum using r >= 3 elements of B.
Remove its zeros, obtaining h of length at most 4 <= r+1. The replacement
lemma makes h squarefree and equal to that subset. If the designated
doubled element was nonzero, this is impossible; if it was zero, h has
at most two terms, also impossible. Hence E4 = T4 minus L2 is exterior
to S and |E4| = |T4|-29.

**Complementary disjointness, in a stronger form.** T4 and s-T4 are
disjoint: a common point would combine two repeated four-term multisets
into an eight-term multiset with sum s. It contains a repetition, so
cannot be the all-ones multiset. Since S = s-S, the sets S, E4, s-E4
are pairwise disjoint. Consequently

    N >= 128 + 2|E4| = 70 + 2|T4|.

In particular, the desired sufficient bound is exactly |T4| >= 89.
The stronger 63 bound is |T4| >= 92. For each translated base a,
T4(A-a) = T4(A)-4a and |L2| remains 29, so |E4| is base-independent.
Unit scaling also preserves these cardinalities. Testing many bases
does not add structural diversity to this particular cardinality test.

**Difference uniqueness.** A squarefree two-term sum cannot equal a
different two-term multiset sum: replace those two elements in the
all-ones multiset by the rival pair. If a-b = c-d is nonzero, then
a+d = c+b. If either side is squarefree, the two multisets must agree,
forcing a=c, b=d (the alternative would give zero difference).
Otherwise a=d, c=b, and 2a=2c: the difference is N/2. Two distinct
antipodal pairs would give equal different squarefree cross-pair sums,
so there is at most one antipodal pair. It follows that without an
antipodal pair all nonzero ordered differences are unique, and all 36
unordered two-term multiset sums, including doubles, are distinct.

**Antipodal reduction.** Translate a pair to 0,t, t=N/2. Projection to
Z/(N/2)Z identifies only this pair, yielding a seven-element set C.
Suppose h were a rival seven-term multiset for C. Lift its nonzero
coordinates to the corresponding elements of A. Allocate the h(0)+1
remaining slots between 0 and t. Choosing zero or one copy of t
corrects either possible kernel error in the lifted target sum; there
is always at least one slot. This produces an eight-term multiset for A
with the required sum. It cannot be all-ones, because its projection
after removing the extra collapsed slot would make h all-ones.
Contradiction. Thus C is valid. Using the externally reported minimum
124 gives N/2 >= 124, hence N >= 248.

## Collision lemmas and exact counting

Assume from now on that A has no antipodal pair.

**Cancellation restriction.** If distinct equal-length multiplicity
vectors u,v have the same sum, then u-v must have an entry >= 2 and an
entry <= -2. Otherwise either 1+u-v or 1+v-u is a nonnegative eight-term
rival to the all-ones vector. This restriction applies after
cancellation; it does NOT forbid repeated-versus-repeated collisions,
and it is necessary, not a sufficient description of validity.

**Ordinary-fiber bound.** Call 2a+b+c ordinary when a,b,c are distinct.
At most four ordinary representations have any one value.
For a fixed center a the tail pair is unique, by the Sidon property.
In a fiber of q ordinary representations the q centers are distinct.
No center can occur as a singleton in another representation: after
cancellation that center would have surplus at most one, as would
every other coordinate on its side, violating the preceding restriction.
All singleton pairs therefore lie on the remaining 8-q elements.
Those pairs are distinct, since a shared pair would imply 2a=2d.
Hence q <= binomial(8-q,2), which forces q <= 4.

For all marked representations (a,{b,c}), the elementary bound is
r_x <= 8: each of the eight centers has at most one tail pair.
A multiset 2a+2b is marked twice, once at each center; this is not a
collision of distinct multisets and must not be discarded incorrectly.

There are 288 marked representations and 260 distinct repeated
four-term multisets. The latter consist of 8 of type 4, 56 of type 31,
28 of type 22, and 168 of type 211. The 28 type-22 double markings
explain the difference between 288 and 260.

Put P = A+A, X_a = 2a+P, and r_x = number of X_a containing x. The Sidon
property makes this precisely the marked multiplicity. Set

    Q = sum_x binomial(r_x,2)
      = sum_{a<d} |X_a intersect X_d|,
    R = sum_{x:r_x>0} binomial(r_x-1,2).

The following are exact identities, not independence assumptions:

    sum_x r_x = 288,
    |T4| = 288 - (Q-R),
    |E4| = 259 - (Q-R).

Proof: binomial(r,2)-binomial(r-1,2)=r-1 for each nonempty fiber;
sum the identities. Equivalently, the unmarked collision excess is
260-|T4|, exactly 28 less than Q-R. Thus the sufficient bound asks for
Q-R <= 199; the stronger 63 bound asks for Q-R <= 196.

Cauchy--Schwarz supplies a justified but weaker counting inequality:

    |T4| >= ceil(288^2 / (288+2Q)).

Indeed sum r_x^2 = 288+2Q. In particular Q <= 327 would suffice for
|T4| >= 89. No such subthreshold energy bound was proved. A uniform
version without N < 248 is false: the valid binary set at N=256 has
Q=353. Multiway overlap matters: it has R=158 and Q-R=195, so it
satisfies the desired exterior bound despite failing this energy bound.

For comparison, the previous elementary cubic count still gives only
|E4| >= 28 here. The eight translates 2a+A each have size eight and
pairwise intersections at most one, so their union T3 has size at least
64-28=36. The replacement argument gives T3 intersect S = A. Padding
with zero shows E3 subset E4. Thus |E4| >= |E3| >= 28.
The sharp local four-per-fiber bound alone does not close this gap.

## Concrete failures, with validity proofs

The binary sets below are valid at N=255 and N=256 by a short carry
argument. Write a_i=2^i-1. An eight-term target collision gives a sum of
eight coins from 1,2,...,128 congruent to 255 modulo N, lying in [8,1024].
At N=255 the possible sums are 255,510,765,1020, whose minimum coin counts
are 8,9,11,12. At N=256 they are 255,511,767,1023, with counts 8,10,12,14.
These counts follow by taking as many 128-coins as possible and the
binary expansion of the remainder. Carrying strictly lowers coin count,
so the minimum representation is unique. Only 255 is possible with
eight coins, and its representation is all-ones.

- **Naive marked-triple injection fails without antipodes too:** at
  N=255, 2*1+3+63 = 2*15+31+7 = 68, outside S, with disjoint supports.
  Overlap is also possible: 2*3+0+0 = 2*1+1+3 = 6, outside S, with a
  shared nonzero element. Both exteriority assertions are directly
  checked by the subset-sum enumeration.
- **An exterior marked cap of four is false:** at N=256 the exterior
  value 12 has centers/tail pairs (1;3,7), (3;3,3), (7;127,127),
  (63;15,127), (127;7,7). These are five markings of four multisets.

**Four ordinary exterior representations are possible.** Let b=19 and

    A = {0,2,38,722,6479,6839,6840,6858}, N=54865.

It is valid by the following elementary proof, not just a computer test.
Order the coordinates as displayed and put c_i=k_i-1 for a candidate.
Since N=8*max(A)+1, congruence of eight-term sums implies integer equality.
That equality is

    0 = H*b^3 + D2*b^2 + D1*b + D0,
    H = c4+c5+c6+c7,
    D2 = 2c3-c4,
    D1 = 2c2-c4-c5-c6,
    D0 = 2c1-c5-c7.

Using k_i>=0 and sum k_i=8 gives D0 in [-8,16], D1 in [-7,17],
D2 in [-9,15], H in [-4,4]. Successive reduction modulo 19 therefore
forces D0=D1=D2=H=0. D2 makes c4 even; D0 and D1 make c5,c6,c7 have
the same parity. H=0 forces these three to be even too. All four center
coefficients are even and >=-1, hence nonnegative, so H=0 makes them
zero. Then c1,c2,c3 vanish, and sum c_i=0 gives c0=0. This proves validity.
The modulus is odd, so no antipodal pair exists. The value 13718 has
ordinary representations with centers/tails
(6479;38,722), (6839;2,38), (6840;0,38), (6858;0,2).
It exceeds every two-element subset sum, so lies in E4. This disproves
an ordinary exterior-fiber cap of three, and shows the proved cap four
is sharp. Its computed exterior cardinality is 200, not a failure of 60.

**The total marked cap eight is sharp, but this example is in L2.**
Let q_i=(-3)^i and first work modulo 6560=3^8-1. Suppose c_i>=-1,
sum c_i=0 and P(-3)=0 modulo 6560, where P(x)=sum c_i*x^i.
Integer division by x+3, also applied to x^8-1, shows that modulo x^8-1

    P(x) = (x+3) sum_{i=0}^7 r_i*x^i

for integers r_i. Hence c_i=3r_i+r_{i-1}, with cyclic subscripts, and
0=sum c_i=4 sum r_i. If r_i=-m_i<0, c_i>=-1 forces
r_{i-1}>=3m_i-1>=2m_i>0. The predecessors of negative indices are
distinct positive indices, so total positive mass is at least twice
total negative mass. This contradicts sum r_i=0. Thus r_i=0 and c_i=0,
proving validity of the q_i.

All q_i are 1 modulo four. Equality of eight-term sums transfers exactly
under a_i=(q_i-1)/4 to modulus 1640. The resulting valid set is

    A = {0,2,20,182,1093,1579,1633,1639} modulo 1640.

There is no antipodal pair: the original integer q_i lie in
[-2187,729], an interval of length 2916 < 3280; an antipodal pair in the
quotient would give a difference 3280 modulo 6560 upstairs.
The cyclic recurrence gives 3a_i+a_{i+1}=-1 modulo 1640 for all eight
indices. Thus r_1639=8. Importantly, 1639 belongs to A, so this is a
low-set fiber, not an eightfold exterior example. It disproves a small
cap for the full T4 accounting, not an exterior cap of eight.
The computed |E4| is 168.

## Reproducible bounded experiments

Run `python obstruction_experiments.py` in this directory. It imports
`research_experiments.py` and `stage2_experiments.py`; both were read
before this investigation. The earlier stage2 script was rerun unchanged.
Its assertions passed, but passing assertions are not mathematical proofs.

Every accepted eight-element set is checked both by enumerating all
binomial(15,8)=6435 eight-term multisets and by an independently written
saturated-coefficient dynamic program. Every normalized base is checked
for the exterior identities, complementary packing, differences and
collision cancellation. The maximum DP array is 9*54865 entries.

The earlier 102 perturbations split into 52 five-element candidates with
two valid sets, and 50 eight-element candidates with just one valid set:
the binary set at N=255. They supplied **no nonbinary eight-element case**.

New batches have fixed seeds and 64 draws each, with no success-based stop:

| Batch | N | Draws | Distinct candidates | Cube-passing draws | Distinct valid sets | Affine classes outside binary | E4 range |
|---|---:|---:|---:|---:|---:|---:|---|
| Local | 239 | 64 | 63 | 7 | 0 | 0 | - |
| Local | 247 | 64 | 63 | 26 | 0 | 0 | - |
| Local | 255 | 64 | 64 | 36 | 1 | 0 | 63 |
| Local | 257 | 64 | 62 | 44 | 0 | 0 | - |
| Local | 509 | 64 | 63 | 44 | 0 | 0 | - |
| Local | 1021 | 64 | 61 | 46 | 0 | 0 | - |
| Random | 257 | 64 | 64 | 1 | 0 | 0 | - |
| Random | 509 | 64 | 64 | 7 | 0 | 0 | - |
| Random | 1021 | 64 | 64 | 16 | 0 | 0 | - |
| Random | 4093 | 64 | 64 | 42 | 8 | 8 | 221--230 |

Local candidates perturb the final three coordinates of the binary set.
Random candidates contain zero and seven uniformly sampled distinct
nonzero residues. Seeds and ranges are specified in the script.
Affine classes are computed exactly by canonicalizing under all unit
scalings and choices of translated base, separately at each modulus.
For example, {0,380,2226,2296,2421,3225,3549,3966} at N=4093 is valid
and has |E4|=229. The eight random classes are pairwise inequivalent.

There are 640 sampled draws, nine distinct accepted (A,N) pairs. Combining
these with five reference pairs and the two proved constructions gives
15 distinct valid pairs, checked at 120 bases. Ten are nonbinary affine
classes: eight at 4093 and the two constructions at their respective
moduli. The constructions are not affine binary sets, since their T4
cardinalities differ from the binary T4 cardinality 127 at those moduli.

Selected computed counts, including multiway-overlap compensation:

| A family | N | Antipodal | E4 | Marked excess Q-R | Q | R |
|---|---:|---|---:|---:|---:|---:|
| Binary | 248 | Yes | 60 | 199 | 395 | 196 |
| Binary | 254 | Yes | 62 | 197 | 376 | 179 |
| Binary | 255 | No | 63 | 196 | 320 | 124 |
| Binary | 256 | No | 64 | 195 | 353 | 158 |
| Binary | 1022 | No | 98 | 161 | 242 | 81 |
| Four-ordinary-fiber construction | 54865 | No | 200 | 59 | 79 | 20 |
| Negative-three construction | 1640 | No | 168 | 91 | 120 | 29 |

For antipodal rows, Q is the collision count of indexed markings, not
the eight-distinct-translates interpretation used in the non-antipodal
proof. No accepted non-antipodal set failed either bound 60 or 63.
However, the subthreshold sample consists of only 128 local draws at
239 and 247 and has **zero valid sets**. It cannot test the conditional
E4 claim on a subthreshold valid set, much less certify nonexistence.
All searches are incomplete. The diverse valid examples occur far above
248 and provide only weak evidence for near-boundary cardinality bounds.

## The single most useful unresolved lemma

**Global collision-loss bound:** for a valid non-antipodal eight-element
set modulo N < 248, with the eight translates X_a defined above,

    sum_{a<d} |X_a intersect X_d|
      - sum_{x:r_x>0} binomial(r_x-1,2) <= 199.

This is an exact counting reformulation of the sufficient claim, not a
separately proved advance. It specifies precisely what must be controlled:
pairwise collision counts WITH the credit from multiple overlaps. The
proved cancellation restriction, the sharp local ordinary cap four and
the full marked cap eight do not yet bound this global quantity. The
energy-only shortcut is unnecessarily strong and fails just above the
boundary. A successful proof must charge global collision loss using
additional cyclic/small-modulus structure or exploit complementary
packing beyond its present cardinality use. No proof of that charging
step, and no counterexample to the sufficient claim, is supplied here.

This completes the requested investigation. Existing stage2 files were
preserved. This directory and its parents are not a configured Git
repository, so no PR can be created here.
