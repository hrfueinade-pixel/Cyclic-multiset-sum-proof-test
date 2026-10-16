# Stage 41: four structural configurations excluded throughout odd N<248

2026-10-11. Continues Stage 40 / open PR #12. The full N>=248 theorem
remains OPEN. This stage gives complete computer-assisted proofs excluding
four configuration families in every odd group of order below 248. These
are uniform symbolic growth certificates, not searches over cyclic sets,
parameters or moduli. No earlier discovery-only exclusion is promoted.

The most useful consequence is new within this investigation:

> In a hypothetical valid eight-set of odd order N<248, no quartic value
> has four ordinary representations 2a+b+c with a,b,c distinct.

Two further exclusions imply that a repeated cubic value has at most three
ordinary representations. A cubic fiber with four or more representations
can only have exactly two pure cubes and two ordinary cubes. There is at
most one such exceptional fiber. The remaining aggregate growth estimate
is not proved. This is a structural advance toward 248, not its solution.

## 1. Definitions, packing, and the small-order proof strategy

A valid eight-set has its all-ones word as the unique degree-eight multiset
representing s=sum A. Consequently every squarefree sum of degree at most
eight is protected against every different same-degree multiset: append
its complement to obtain a rival otherwise.

Write kA for the k-fold sumset allowing repetition, Q_k for its squarefree
values, and T_k for its repeated values. Thus

    |Q_3|=|Q_5|=56,  |Q_4|=70,
    kA=Q_k disjoint-union T_k.

The same concatenation argument gives

    3A intersect(s-5A)=Q_3,
    N>=|3A|+|5A|-56.                                  (A)

Also 4A intersect(s-4A)=Q_4. In odd order the midpoint s/2 is absent
from 4A: otherwise doubling its four-term representation would give an
eight-term rival. It cannot be the original, whose eight counts are odd.
The union 4A union(s-4A) misses the midpoint, so

    N>=2|4A|-69 =71+2|T_4|.                            (B)

Odd pair protection gives 36 distinct two-term multiset sums and 56
distinct ordered nonzero differences. Of the 64 cubic marks 2a+b, a fixed
pair of different centers can contribute at most one coincident mark
pair, by difference uniqueness. There are at most 28 such pairs, so
|T_3|>=64-28=36 and |3A|>=92. This is an elementary bound; it uses no
previous modulus exclusion or external minimum.

The new strategy uses two different splits, rather than requiring 89
quartic values in every intermediate calculation. For two families we
first force 87 repeated quartics, obtaining N>=245 from (B). Under N<248,
the only odd possibilities are 245 and 247, both coprime to three. We can
THEN cancel powers of three as well as two in symbolic relations. A
quintic growth certificate yields 156 or 157 repeated quintics; (A) gives

    N>=92+(56+156)-56=248,

or the stronger 249. This excludes both remaining orders. The order of
these steps matters: cancellation by three is not assumed at the initial
odd orders divisible by three.

## 2. What a symbolic certificate proves

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

The six compressed JSON files contain the selected words and one rival
for every unordered pair, in combination order. The gzip format merely
keeps the certificates small; Python's standard library reads them.
Positive witnesses establish the growth bound even when their discovery
stops early or times out. Maximum clique size and search completeness
are not premises of any theorem here.

## 3. Four models and their uniform lower bounds

All displayed lists are labeled in the order used by the certificates.
They must have eight distinct points; validity itself requires this.
The parameters are arbitrary group elements, not integer intervals.

|Model|Eight labels|Certified growth|Consequence|
|---|---|---|---|
|leaf22|0,2u,2v,2w,z,z+u,z+2u-v,z+2u-w|T4>=87 in odd order; T5>=157 when 3 is invertible|N>=245 first, then N>=249|
|hub22|0,2u,2v,2w,z,z-u,z-v,z-w|T4>=90 in odd order|N>=251|
|fourO|0,2u,2v,2w,z-u,z-v,z-u-v,z-v-w|T4>=87 in odd order; T5>=156 when 3 is invertible|N>=245 first, then N>=248|
|purehub|0,2u,2v,2w,-u,-v,-w,z|T4>=89 in odd order|N>=249|

The respective original coefficient vectors b are

    leaf22:  (7,1,1,4),
    hub22:   (1,1,1,4),
    fourO:   (0,-1,1,4),
    purehub: (1,1,1,1).

Each row excludes its model throughout odd N<248. For leaf22 and fourO,
the argument in Section 1 supplies the required invertibility of three
only AFTER applying the quartic certificate. For hub22 and purehub, the
quartic certificate alone suffices.

These families are not empty or intrinsically contradictory at large N.
For example leaf22 with u=1,v=17,w=289,z=4913 in Z/39313 is valid and has
an eight-predecessor quartic fiber. Its labels are

    0,2,34,578,4913,4914,4898,4626.

There is no modular wrap in any eight-term sum. Equality with the target
forces equality of its four base-17 coefficients: the differences of the
u,v,w,z coefficients have absolute values at most 9,15,15,4 respectively,
all less than 17. If the counts on z+2u-v,z+2u-w are g,h, the v,w equations
give g,h positive odd integers. Their u contributions and target seven
exclude g>=3 or h>=3, so both are one. The total count on the four z-labels
is four; the u equation then forces the count on z+u to be one and on 2u
to be one. The other equations force all remaining counts to one.

The value 2z+4u has representations

    2(z+u)+0+2u,
    2(z+2u-v)+0+2v,
    2(z+2u-w)+0+2w,
    2z+2(2u).

Together their supports use all eight labels. Hence r_(3A,A) at that value
is eight. A universal local incidence cap seven would be false; the
small-order model exclusions, rather than such a cap, are what is proved.

## 4. Every fourfold ordinary quartic fiber is now excluded

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
in Section 3. Its uniform two-step growth proof excludes odd N<248.
Therefore every repeated quartic value in a remaining counterexample has
at most THREE ordinary representations. This is not just the old
F4<=R3 coexistence bound; it gives F4=0 in the entire conditional interval.

## 5. Consequences for cubic multiplicities

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

## 6. Two failed approaches before the successful pivot

First, a larger cube packing was tried: after choosing an origin and a
direction from A, take the 64 subset sums U of the other six normalized
points and union U,U+a,U+2a,U+3a. A universal claim that some such union
has size at least 248 is false. For the valid binary set in Z/255, all
56 origin/direction choices have maximum union size 224. The fixed control
script saves every size. This does not refute a conditional small-order
version, but the universal packing supplies no proof.

Second, the odd group character decomposition was considered in
characteristic two. Orthogonality gives a symmetric decomposition with
N summands of the permutation tensor, which equals the alternating
determinant tensor in characteristic two. Ordinary middle flattening has
rank binomial(8,4)=70 and is insufficient. The value 2^8-8=248 in the
[Houston--Goucher--Johnston formula](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/E33F5E0726A0691B250C3BB6CE3816F5/S0963548324000233a.pdf/a-new-formula-for-the-determinant-and-bounds-on-its-tensor-and-waring-ranks.pdf)
is an UPPER bound for ordinary tensor rank, not a usable lower bound or
a symmetric-rank theorem.

A proposed general symmetric-rank lower bound 2^n-1 in characteristic
two also fails. In F4, with omega^2=omega+1, the order-three alternating
tensor is omega times the sum of the cubes of these six vectors:

    e1,e2,e3,(1,omega,omega),(omega,1,omega),(omega,omega,1).

This is a tensor-power identity, not an ordinary cubic-polynomial identity.
For a repeated-index entry its value is zero; for three distinct indices
it is one. The script checks all 27 entries directly. It refutes that
general bound at n=3, not a possible n=8 theorem or a cyclic-modulus
claim. No applicable tensor-rank lower bound finishing 248 was established.

The pivot to full configuration closure then succeeded. Initial quartic
clique searches for leaf22 and fourO stalled at 87. Cancellation by three,
integer multiples of rival directions and a joined-odd-cycle lift were
investigated; none supplied the missing 89-value certificate in those
runs. A separate coefficient-closure test at modulus 245 also retained 87
within its ten-second cap; it did not enumerate parameter choices or
establish an exclusion. These failures do not assert maximum clique 87. Switching to the
3+5 packing produced the positive quintic certificates in about two
seconds, closing both families without a larger timeout.

## 7. What is still missing

No theorem here forces an arbitrary remaining valid eight-set to contain
one of the four excluded configurations. Quartic fibers with at most three
ordinary representations, mixed 31/22 fibers, and the unique possible
two-pure/two-ordinary cubic fiber remain. Even with F4=0, merely counting
168 ordinary words gives only 56 ordinary output values. Those outputs
may overlap the 36 doubled pair-sum outputs. Their union is not proved to
have 89 values. Assuming these sets disjoint would introduce a new gap.

The exact Stage 40 parity-covering target remains open. A next structural
branch is the order-three cubic exception, whose six forced labels are
0,delta,c,-2c,e,-2e with 3delta=0, plus two free points. The current
four-parameter checker does not cover its torsion coordinate. Excluding
that branch would simplify all cubic fibers to multiplicity at most three,
but would still require a global quartic or target-covering argument.

The main theorem is not marked complete. This stage removes four genuine
collision patterns over the entire interval, including all fourfold
ordinary quartics. It does not certify absence of arbitrary eight-sets at
any newly excluded order.

## 8. Reproduction, certificate checks, and publication boundary

The shipped certificates can be checked immediately, without discovery:

```text
python -B stage41_case_certificate_check.py
python -B stage41_pre_pivot_obstructions.py
```

The separate checker verifies 39,739 positive pair certificates across six
files. It rejects a wrong-mass rival and eight mass-preserving pure-word
corruptions at the first pair of each file. Its proof logic is expressed
using independent coordinate formulas and scalar equations, not graph
generation or search. Runtime is below one second apart from startup.
These are separate implementations by the same author, not an independent
human review or a formal proof assistant.

To regenerate suitable positive witnesses and repackage them:

```text
python -B stage41_saturated_fiber_closure.py --model leaf22 --target 87 --output stage41_saturated_fiber_closure_results.json
python -B stage41_saturated_fiber_closure.py --model leaf22 --degree 5 --target 156 --units 2,3 --integer-rays --output stage41_saturated_fiber_quintic_results.json
python -B stage41_saturated_fiber_closure.py --model hub22 --target 90 --integer-rays --output stage41_hub22_quartic_results.json
python -B stage41_saturated_fiber_closure.py --model fourO --target 87 --integer-rays --output stage41_fourO_quartic_results.json
python -B stage41_saturated_fiber_closure.py --model fourO --degree 5 --target 156 --units 2,3 --integer-rays --output stage41_fourO_quintic_results.json
python -B stage41_saturated_fiber_closure.py --model purehub --target 89 --integer-rays --output stage41_purehub_quartic_results.json
python -B stage41_pack_certificates.py
python -B stage41_case_certificate_check.py
```

The producer has a fixed ten-second search cap per run. The shipped
certificates establish the results regardless of later discovery success.
The original leaf22 quartic run reached its cap and retained a positive
87-clique. The other retained runs stopped on positive witnesses. No run
asserts optimality. The six positive sizes, degrees, unit hypotheses and
discovery status are saved in stage41_discovery_summary.json; compressed
certificates together occupy about 72KB.

No historical exclusion was rerun, no group parameter space was swept,
and no numerical timeout or absence supports a theorem. No process is
left running. The report, code and positive certificates are saved on a
new PR stacked on #12; earlier PRs remain unmerged. No novelty claim is made.
