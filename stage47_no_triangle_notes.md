# Stage 47 proof track: the branch without quartic triangle cores

2026-10-11. This is a separate proof-track report continuing Stage 46.
The complete N>=248 theorem is OPEN. All claims below assume FULL validity,
not merely protected cubic sums. Only cancellation by two is used.

## 1. Exact ordinary-pair lift counts, with recoverable inverses

Let P_d be the number of unordered pairs of different ordinary degree-d
words at equal values. Ordinary means 2c followed by d-2 distinct labels
different from c. Let S_d count such pairs with DISJOINT tails, for d=4,5.

For any equal ordinary pair, its two centers are different and neither
center occurs anywhere in the opposing word: canceling one occurrence
would contradict a protected squarefree degree-(d-1) sum.

An ordinary cubic pair therefore uses four distinct labels. Adding one
of the four unused labels gives four different ordinary quartic pairs.
Conversely, an equal ordinary quartic pair with intersecting tails has
exactly one common tail label; removal uniquely recovers that cubic pair
and the added label. Equal tail sets are impossible by odd cancellation.
Thus no output, pair, or removed label is counted without an inverse:

    P4 = 4*P3 + S4.

For ordinary quintic pairs, the intersection of the two tails has size
zero, one, or two. Intersection two uniquely removes the two common
labels, recovering an ordinary cubic pair; exactly binomial(4,2)=6
additions are available. Intersection one uniquely removes that label,
recovering a disjoint-tail quartic pair; its six used labels leave exactly
two possible additions. Intersection zero is S5 itself. Consequently

    P5 = 6*P3 + 2*S4 + S5 = 2*P4 - 2*P3 + S5.

These are counts of WORD PAIRS, not distinct values. Different lifted
pairs may lie in the same fiber; the formulas do not require disjoint
outputs. The deletion inverse is what controls reuse.

There are at most 28 disjoint-tail ordinary quintic pairs. For fixed
unordered centers c,d, their six other labels form B. Orient the pair as
2c+U=2d+(B-U), where U is a three-subset of B. This gives

    2*sum(U) = 2d-2c+sum(B).

Two such partitions for the same centers have equal squarefree triple
sums after canceling two, hence are identical by protection. Therefore
S5<=binomial(8,2)=28. Each S5 output has EXACTLY two ordinary words:
its two disjoint tails use all six noncenters, leaving no possible private
center for a third ordinary word.

## 2. A no-triple branch that is already sufficient at k>=16

Put k=h+R3. The desired conditional quintic bound is T5>=156-k.
There are 280 ordinary quintic words. If no output has three ordinary
words, their multiplicity is at most two, so T5>=140. Hence the desired
bound follows immediately when k>=16 in this NO-ORDINARY-TRIPLE branch.

For k<16, forcing 16-k mixed-only quintic VALUES suffices. Here mixed-only
means an output represented by at least one repeated nonordinary word
and by no ordinary word; the word count 456 is not a value count.

More exactly, let n1,n2,n3 count fibers with respectively one,two,three
ordinary quintic words, and M5 count mixed-only repeated output values.
Then

    280=n1+2*n2+3*n3,
    T5=140+(n1-n3)/2+M5.

The target is therefore exactly

    M5 >= 16-k+(n3-n1)/2.                 (UNPROVED in general)

This includes the configurations without triangle cores: path/split
triples contribute to n3, and mixed-only fibers contribute to M5.
Stage 44's shared-center theorem bounds reuse on one center triple,
but gives no lower bound for M5 across DIFFERENT center triples.

## 3. Two structural attempts and their exact gaps

First attempt: use the lift count to force an ordinary quintic triple.
In the no-triple branch P5<=140, hence P3<=23 from six cubic lifts.
The total cubic collision-pair count is 28-h. In every fiber of cubic
multiplicity at most three, the number of pairs involving pure words
is at most the number of pure words there plus its contribution to R3.
(For one pure and two ordinary words this is 2<=1+1; for two pure and
one ordinary it is 3<=2+1; all double fibers satisfy the claim.) There
are eight pure words, so P3>=20-h-R3=20-k. The bounds

    20-k <= P3 <= 23

are compatible for every nonnegative k. Thus cubic compression alone
does not force a triple, even after retaining every lift overlap.

Second attempt: exploit S5 fibers' complementary mixed parities.
An S5 pair has q=2c+U=2d+V, B=U disjoint-union V and

    2s=2q+sum(B).

Any other word in the fiber avoids c,d. If two such quintic words M,M'
on B have complementary parity, M+M'=1_B modulo two, then

    r=(M+M'+1_B)/2

is an integer nonnegative mass-eight rival, of value s, omitting c,d.
Thus complementary parities are forbidden. Fixed-parity injectivity
holds because a degree-five word with fixed parity is epsilon+2v,
with v of degree at most two; equal values cancel two and violate pair
protection. The odd-parity space on six labels has 32 elements, in 16
complementary pairs. This gives at most 16 accompanying B-only words,
which is too weak to force 16-k NEW output values. It controls words at
an existing output and supplies no injection into M5.

Both attempts stop at quantified gaps. Neither is a proof of global
growth, and neither assumes cancellation by three or disjoint outputs.

## 4. Targeted two-control experiment: triangle-free path and split exist

The experiment in stage47_no_triangle_probe.py examines only TWO fixed
free-abelian coefficient models. It does not sweep cyclic sets, moduli,
parameters or historical search assignments. Its purpose is to distinguish
"all valid compression has useful triangle cores" from "triangle-free
compression is valid but must be excluded using the small quartic budget."

In both models let

    B=(0,2u,2v,2w,2t).

For the path use centers (z+u,z+u+v,z+v+w); for the split use centers
(z+u,z+u+v,z+w+t). Both have three ordinary quintic words of equal value
2z+2u+2v+2w+2t, with omitted edges respectively
(01,12,23) and (01,12,34). These are the path and split types.

Both generic models are fully valid, by an elementary coefficient proof.
Let alpha,beta,gamma be center counts in a mass-eight rival. Its z
coefficient gives alpha+beta+gamma=3. For the path the w equation makes
gamma odd, the v equation then makes beta odd, and the u equation makes
alpha odd. For the split the v,w equations make beta,gamma odd and
the u equation makes alpha odd. Nonnegative odd counts summing to three
are all one. The other coefficient equations and mass force every B
count to one. This proves validity in the coefficient model without
a numerical search.

Set (u,v,w,t,z)=(1,17,289,4913,83521). The two declared cyclic controls are:

| Model | A | N | T3/T4/T5 |
|---|---|---:|---|
|path|0,2,34,578,9826,83522,83539,83827|670617|62/244/664|
|split|0,2,34,578,9826,83522,83539,88723|709785|63/250/685|

There is no modular wrap since N=8*max(A)+1. All degree-at-most-eight
parameter coefficients are between zero and 16, so distinct coefficient
vectors give distinct base-17 integers. Thus the coefficient validity
proof applies to each cyclic control. The script additionally checks all
6435 mass-eight words directly as arithmetic support.

Both controls have NO ordinary quartic TRIANGLE cores. The path has one
ordinary quartic PATH triple; the split has no ordinary quartic triples.
Each has one ordinary quintic triple. Cubic total multiplicity is two,
ordinary quartic multiplicity at most three and ordinary quintic
multiplicity three. These controls refute the UNRESTRICTED claim that
full validity and the inherited local caps force useful quartic triangles.
They are not counterexamples below248: their T4 values greatly exceed88.
The budget T4<=88 must enter any triangle-necessity argument.

The saved JSON includes coefficient rows, all ordinary triple words,
pair-count decompositions, output counts and fixed cyclic controls. It
checks the exact lift formulas in these models. Formal absence of other
triangle cores is checked in the finite coefficient-word list; it is not
a classification of all group solutions of a relation system.

Run with Python3:

    python -B stage47_no_triangle_probe.py

This proof track leaves the sharp global missing lemma from Section2
open. The independently challenged pair-count and parity arguments do
not close distinct-center path/split coupling. No earlier PR or historical
verification boundary is altered.

## 5. A global necessity in the saturated no-triple branch

For fixed centers c,d and B the other six labels, an equal ordinary
quintic pair with tails U,V has the complementary pair

    (2c+(B-V), 2d+(B-U)).

The same difference equation is preserved by subtracting the tails from
sum(B). Complementing again recovers U,V, so this is an involution on
the pairs with these fixed centers. Its fixed points have U=B-V,
which is EXACTLY disjointness of the three-label tails. Thus all non-S5
pairs occur in twos, even when their output values coincide elsewhere.

In a perfect pairing of all 280 ordinary words into 140 fibers, each
center's 35 ordinary words participates once. Its incident ordinary-pair
count is 35, hence odd. Nonfixed complementary pairs contribute two
incidences at that center. Therefore the graph with centers as vertices
and S5 pairs as edges has all eight vertex degrees ODD. It is simple by
the S5<=28 proof above. In particular it has AT LEAST FOUR edges.

More generally in the no-triple branch, let u_c count single-ordinary
fibers with center c. The degree parity in the S5 graph is 1-u_c modulo
two. Since sum(u_c)=n1, at least 8-n1 vertices have odd degree when
n1<=8, forcing S5>=ceil((8-n1)/2). This is a simultaneous global
necessity, not another local multiplicity cap.

Packing localizes three near-saturated cases. In this no-triple branch
N>=232+k. For k=13,14,15 under odd N<248, N is at least245, so ONLY
after this deduction is three invertible (remaining orders245,247).

| k | possible N | T5 upper bound | compulsory S5 edges |
|---:|---:|---:|---:|
|15|247|140|at least4; perfect ordinary pairing, no mixed-only outputs|
|14|247|141|at least3 since n1<=2|
|13|245|140|at least4; perfect ordinary pairing|
|13|247|142|at least2 since n1<=4|

No all-odd-degree graph is assumed to contain a perfect matching: K1,7
is an explicit counterexample to that graph inference. Consequently a
proof must handle graphs with reused centers as well as four disjoint
center pairs.

## 6. Small targeted symbolic test of the nonnegativity obstruction

The script stage47_no_triangle_matching.py fixes four DISJOINT center
pairs (01,23,45,67) and fixes the first relation to

    R0=(2,-2,1,1,1,-1,-1,-1).

For each of the other pairs it chooses one of the 20 three-tail
partitions on the remaining six labels. This is a declared 8000-assignment
symbolic slice, NOT coverage of every compulsory graph, and no cyclic
group, modulus, or group parameter is enumerated.

It tests the proposed immediate rival

    r=1+sum_i sign_i*R_i,   sign_i in {-1,1}.

Each success has integer nonnegative counts, mass eight, is non-original,
and differs from all-ones by a sum of actual collision rows. It therefore
is a valid direct rival in ANY group admitting those equalities.

The formula succeeds for 2340 assignments and fails for 5660. The first
saved positive example gives r=(0,4,0,0,0,0,4,0) using signs(-1,-1,1,1).
The saved failure examples retain all four relation rows. A failed test
means only that all 16 unit-coefficient signed sums have a negative
coordinate or are original; it does NOT mean the equations permit a
valid set, or that other integer/dyadic combinations fail. No new local
cap or exclusion is inferred from these failures.

This experiment distinguishes the two competing explanations: compulsory
cross-fiber parity exists, but parity alone does not repair nonnegativity
in the simplest sum formula. The sharpened missing saturated lemma is:

> Under full validity, T4<=88, and the compulsory all-odd-degree S5 graph
> arising from perfect ordinary pairing, either produce a nonnegative
> mass-eight rival from simultaneous collision equations or force a
> mixed-only quintic output. Handle reused centers and all graph shapes.

That lemma is unproved. Solving it would close k=15 and the N=245,k=13
saturation branches without assuming any triangle core. It would not by
itself close the entire odd207..247 interval.

## 7. Midpoint placement in the two saturated branches

For every S5 pair with centers c,d at value q, summing its equations gives
2q=s+c+d. Thus q=(s+c+d)/2. Protected pair sums make the output recover
the center pair uniquely. Its reflection s-q=(s-c-d)/2 is exactly one
of Stage40's prescribed cubic holes. The two complementary ordinary pairs
at fixed centers have values q,q' with q+q'=s+c+d.

In the saturated no-triple branches (k,N)=(15,247) and (13,245), packing
is equality: 56+|T3|+|T5|=N. Since 3A and s-T5 are disjoint, their sizes
exhaust the group, so G\3A=s-T5. Stage40's full-validity parity reduction
places all 36 points (s-c-d)/2, c,d in A with repetition, outside3A.
Reflecting them therefore forces all 36 distinct midpoints

    (s+c+d)/2 in T5.

Every such output is perfectly ordinary-paired in these branches. No word
M at this midpoint can contain both c,d: otherwise 2M-e_c-e_d is a
nonnegative mass-eight rival, and has at most two odd coordinates, so
cannot be original. For a diagonal pair c=d, every word must avoid c
altogether, since 2M-2e_c would otherwise be an even-count rival.

This strengthens the missing saturated lemma to a concrete placement
problem: explain why perfect ordinary pairing of all 36 midpoint outputs,
their omission restrictions, the odd-degree S5 graph, and T4<=88 cannot
coexist. Placement alone does not yet provide that contradiction. These
deductions use only cancellation by two and exact packing, not a modulus
search or an assumption that different words use distinct witnesses.
