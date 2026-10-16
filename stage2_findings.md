# Research Stage 2: complementary sums and a quadratic improvement

## Results and status

The following bounds are proved below for arbitrary valid cyclic sets:

\[
 N\ge 2^{n-1}+n(n-1)\qquad(n\ge7).
\]

For n congruent to 3 modulo 4, the bound increases by one. Additional
equality obstructions give

\[
 N\ge109\quad(n=7),\qquad N\ge187\quad(n=8).
\]

For n=8, a set containing an antipodal pair must have N>=218; if 4 divides
N, that conditional bound is N>=220. Two successive antipodal reductions
give N>=240. Three reductions ending in an odd five-element quotient
give N>=248. These are lower bounds, not assertions that valid sets exist
at the stated endpoints. The conjectured minimum for n=8 remains 248.

The complementary-double claim is correct for n>=4, including equal
indices. A general family of short repeated sums leads to the quadratic
bound. A stronger four-term inequality was tested but is not proved.

No literature novelty is claimed. The bounds and proofs here were derived
in this run; targeted literature searches did not establish whether they
have appeared elsewhere. No Lean was written or run, no repository was
cloned, and no search over a range of candidate moduli was performed.

## 1. Independent audit of the previous stage

Let A={0,b_1,...,b_m} be valid in G=Z/NZ, with m=n-1. Write

\[
 s_T=\sum_{i\in T}b_i,\quad S=\{s_T:T\subseteq[m]\},
 \quad s=\sum_i b_i,\quad M=2^m.
\]

Translation preserves validity. Validity is equivalent to the absence of
a nonzero integer vector c on B={b_1,...,b_m} satisfying

\[
 c_i\ge-1,\qquad \sum_i c_i\le1,\qquad \sum_i c_i b_i=0.
\]

Indeed, set k_i=1+c_i for the nonzero coordinates and
k_0=1-sum c_i. These are exactly the competing multiplicities.

More particularly, if a subset T of size r has a multiset representation
h on B of length l<=r+1, set

\[
 k_i=1-1_{i\in T}+h_i,\qquad k_0=1+r-l.
\]

The resulting vector is nonnegative, has total n, and has sum s.
Validity forces h to be exactly T. This proves both dissociation, |S|=M,
and that nonzero doubles 2b_i are outside S. The condition l<=r+1 is the
exact condition for this replacement construction to have k_0>=0;
its failure does not assert that the original set is valid.

In a cyclic group, at most one antipodal pair can belong to A: two pairs
a,a+t and c,c+t, t=N/2, give the squarefree collision
a+(c+t)=(a+t)+c. Thus |2A|>=n-1, and odd N gives |2A|=n.
Counting nonzero doubles outside S gives the prior odd bound M+n-1.
For even N with a nonzero odd difference, exactly M/2 subset sums are
even; all doubles are even, giving N>=M+2n-4. If all differences are even,
N>=2M instead. For n>=3 this also proves the prior parity-free bound
N>=M+n-1. The previous proofs are correct.

The prior odd equality obstruction is also correct: if N=M+m is odd,
S and the m exterior doubles partition G, so
(2^{m-1}+2)s=0. An invertible coefficient contradicts dissociation.

The known background must be distinguished from these deductions. The
[paper](https://arxiv.org/html/2607.08366v2) proves the exact least modulus
for its fixed binary construction, and reports global certification through
n=7. The [repository](https://github.com/jarfo/min-modulus) records Inal's
general abelian minimum M and equality classification. Dissociation and
the exterior-double observation already underlie that classification.
The cyclic counting improvements here are not presented as literature-new
theorems. The numerical minima for n=4,5,6 recovered below were already
known; what is supplied here is an elementary argument for arbitrary sets.

## 2. Complementary doubles: all edge cases

Throughout, 2A denotes the dilation {2a:a in A}, not A+A. Define
D=(2A)\{0}. Its size is d=|2A|-1, not necessarily n-1. In particular,
zero doubles must be omitted, and an antipodal pair reduces the number of
distinct doubled values by one. We have d=n-1 for odd N, and d=n-2 or n-1
for even N according as an antipodal pair is present or absent.

Since S=s-S, both D and s-D are outside S. For n>=4 they are also disjoint:
an equality 2b_i=s-2b_j would give s=2b_i+2b_j. The multiset with two
copies of b_i, two copies of b_j, and n-4 zeros competes with the all-ones
multiset. If i=j it has four copies of b_i; it still competes. It cannot be
the baseline since it repeats a nonzero element. Thus

\[
 N\ge M+2d.
\]

The restriction n>=4 is necessary: for the valid A={0,1,3} modulo 6,
s=4 and D={2}=s-D.

For odd N, this gives the requested N>=M+2(n-1). Since N is odd, the
integer bound is actually N>=M+2n-1. Equivalently, the unique midpoint
s/2 is outside S and D union (s-D): S pairs complementary subsets without
a fixed point, and D and s-D are disjoint.

For even N with mixed parity and even s, S has M/2 even elements, and
D and s-D are both even. Hence

\[
 N\ge M+4d\ge M+4n-8.
\]

If s is odd, reflection switches parity and gives N>=M+2d. If every
element of A is even, the entire packing is in the even subgroup and gives
N>=2M+4d, an even stronger special-case bound.

Changing the base a changes the target to

\[
 s_a=\sum_{x\in A}x-na.
\]

For odd n and mixed parity, a base can always be chosen with even s_a.
For even n its parity is invariant. For n=8 its residue modulo 4 is also
invariant. Thus a base change cannot force the desired parity for n=8.
Complementary doubles alone already prove the proposed general bound 140
for n=8; when s is even and parity is mixed they give 152 instead.

## 3. A general packing of repeated sums

For k>=2 define the sumsets and their exterior portions by

\[
 C=2A,\qquad T_k=C+(k-2)A_{\mathrm{sum}},\qquad
 L_{k-2}=\{s_U:|U|\le k-2\},\qquad E_k=T_k\setminus L_{k-2}.
\]

Here rA_sum denotes all r-term multiset sums and 0A_sum={0}.

**Lemma.** T_k intersect S equals L_{k-2}. Consequently E_k is outside S.

Proof. The inclusion L_{k-2} subset T_k follows by using the repeated
element zero and padding with zeros. A representation in T_k has k terms
with some element repeated. If the repeated element is zero and all other
nonzero terms are squarefree, there are at most k-2 nonzero terms. Otherwise
a nonzero element is repeated. If its value equaled s_U with |U|>=k-1,
its representation on B would have length at most k<=|U|+1 and would have
to equal U by the replacement lemma. Both alternatives are impossible.
This proves the equality. QED.

Each element of E_k has a k-term representation with a nonzero element
repeated. Therefore, whenever j+k<=n,

\[
 E_j\cap(s-E_k)=\varnothing,
 \qquad N\ge M+|E_j|+|E_k|.                 \tag{1}
\]

Indeed, an intersection would represent s by j+k terms containing a
nonzero repetition; padding with zeros gives a competing size-n multiset.
No injectivity of the expressions used to generate E_k is assumed.

In particular, E_2=D, T_3=2A+A, T_3 intersect S=A, and

\[
 |E_3|=|2A+A|-n.
\]

For n>=5 we can pack E_3 and s-E_2; for n>=6 we can pack E_3 and s-E_3.

The proposed cubic residues are not all exterior. In the known valid
{0,1,3,7} modulo 12, 3*1=3 and 2*3+1=7 are in S. Also s-3*1=8 is in S.
For the directly verified valid {0,1,3,10} modulo 15, 3*10=0 is in S.
The general lemma identifies precisely the safe removal: T_3 loses A,
not an assumed empty intersection with S.

## 4. Cyclic differences control the size of 2A+A

**Difference lemma.** Every nonzero difference of A has at most one ordered
representation, except the involution t=N/2, which has two representations
if an antipodal pair exists and none if it does not.

Proof. From a-b=c-d obtain a+d=c+b. If either pair in this equality is
squarefree, validity, padded by the remaining elements of A, forces the
same unordered pair on both sides. For nonzero differences this yields
(a,b)=(c,d). Otherwise both pairs are doubles: a=d, c=b, and 2a=2b.
In a cyclic group the exceptional difference is t. Its two orientations
come from the unique antipodal pair. QED.

Let p be 1 if A has an antipodal pair and 0 otherwise. Set C=2A and
r=|C|=n-p. Let e be the number of unordered antipodal pairs in C.
Then e<=1, and e=0 unless 4 divides N. To prove this, a pair in C at
distance N/2 lifts to a pair in A at distance plus or minus N/4. The
difference lemma permits at most one such unordered pair.

The r translates u+A, u in C, each have n elements. A pair of these
translates intersects in at most one element unless their centers are
antipodal. In that exceptional case the intersection has size 2p.
The first inclusion-exclusion inequality therefore gives

\[
 |2A+A|\ge nr-\binom r2-(2p-1)e,
\]

or, equivalently,

\[
 |E_3|\ge \binom n2-p-(2p-1)e.             \tag{2}
\]

Notice the sign when p=0: an antipodal pair in 2A has *zero* intersection
between its translates, so it improves the estimate. It is not a loss of
two elements. Correctly accounting for this edge case is essential.

For n>=6, equations (1) and (2) give

\[
 \begin{array}{ll}
 p=0:& N\ge M+n(n-1)+2e,\\
 p=1:& N\ge M+n(n-1)-2-2e.
 \end{array}                              \tag{3}
\]

For odd N, p=e=0. In particular, the odd bound for n>=6 is
N>=M+n(n-1)+1 after parity rounding.

## 5. Subgroups, quotient validity, and the general quadratic bound

Validity is hereditary: a competitor for a subset can be padded with one
copy of every omitted element to contradict validity of A. Thus a parity
class of k elements yields a valid k-element set in Z/(N/2)Z, after
translation and division by 2.

**Antipodal reduction lemma.** If A contains 0,t with t=N/2, its image in
G/<t> is a valid (n-1)-element set.

Proof. There is only one antipodal pair, so precisely 0,t coalesce.
Write the other points as c_1,...,c_{n-2}. Suppose the quotient had a
competing size-(n-1) multiset h. Lift its nonzero multiplicities and add
one additional zero: the number of points available in the class {0,t}
is h_0+1>=1. The lifted sum differs from the original target by either
0 or t. Choosing either zero or one of these available copies to be t
adjusts that difference exactly. The resulting size-n multiset is a
competitor; because h was not the quotient baseline, it cannot equal the
original baseline. This contradiction proves the lemma. QED.

For clarity, the quotient in this lemma has order N/2, not 2A interpreted
as an automatically valid n-element tuple. Doubling can identify points.

The small base cases needed for induction follow from the same estimates:

- n=4: complementary doubles give odd N>=15 and even N>=12.
- n=5: packing E_3 with s-E_2 gives N>=30+e if p=0, and N>=28-e if p=1.
  When e=1, N is a multiple of 4, so the latter rounds up from 27 to 28.
  Thus N>=28; odd N>=31. A minimizer at 28 must have an antipodal pair.
- n=6: equation (3) gives N>=62+2e if p=0, and N>=60-2e if p=1.
  The latter rounds from 58 to 60 when e=1 because 4 divides N.
  Thus N>=60; odd N>=63. A minimizer at 60 must have an antipodal pair.
- n=7: if p=0, equation (3) gives N>=64+42=106. If p=1, reduction and
  the n=6 bound give N>=120. Hence the quadratic bound holds at n=7.

For n>=8, assume the quadratic bound at n-1. If p=0 use equation (3).
If p=1, antipodal reduction gives

\[
 N\ge2\bigl(2^{n-2}+(n-1)(n-2)\bigr)
   \ge2^{n-1}+n(n-1),
\]

since 2(n-2)>=n for n>=4. This completes the induction and proves
N>=2^{n-1}+n(n-1) for every n>=7.

There is a general parity rounding improvement when n=3 mod 4, n>=7.
The no-antipodal estimate has |E_3|>=binomial(n,2), an odd number.
For even N with mixed parity, choose a base with even s. Reflection
preserves parity, so the larger parity portion of E_3 has at least
ceil(binomial(n,2)/2) elements and its reflection has the same number.
Counting inside that subgroup yields

\[
 N\ge M+4\left\lceil\binom n2/2\right\rceil
   =M+n(n-1)+2.
\]

If all elements have one parity then N>=2M, which is stronger for n>=7.
The antipodal reduction bound is also stronger. Odd N rounds up to
M+n(n-1)+1. Thus the parity-free bound gains one for n=3 mod 4.
In particular every valid seven-element set has N>=107, and an even
seven-element modulus has N>=108.

## 6. Two useful equality and parity lemmas

Write Delta=(A-A)\{0}. If p=0 then |Delta|=n(n-1).

**Equality forces doubling closure.** If p=0 and |E_3|=binomial(n,2), then

\[
 2\Delta\subseteq\Delta.                  \tag{4}
\]

Proof. Equation (2) forces e=0. There are n translates of A, total
incidence n^2, with binomial(n,2) pairwise intersections available, each
of size at most one. Their union has size n+binomial(n,2), attaining the
first inclusion-exclusion lower bound. Therefore every pair intersects.
For every a!=c in A, this gives 2(a-c) in Delta. QED.

**Paired partition of an even group forces odd target.** If n>=6 and
N=M+2|E_3| is even, S, E_3, and s-E_3 partition G. Their sums give

\[
 N/2=(M/2+|E_3|)s=(N/2)s\pmod N,
\]

so s is odd. This applies separately for every choice of translated base.

**Parity energy estimate.** For even N, p=0, and parity class sizes a,b
in A, a+b=n,

\[
 |E_3|\ge\max\{\binom n2+e,\ 2ab\}.       \tag{5}
\]

Proof. A pair of centers in C=2A can intersect only using a same-parity
pair of columns in A. For each unordered column pair, its nonzero even
difference delta is not the involution (p=0). The equation 2(a-c)=delta
has at most two possible differences a-c, and each has at most one
ordered representation in A. Thus this column pair accounts for at most
two unordered center pairs. The total pair-intersection count is at most
2[binomial(a,2)+binomial(b,2)]. Inclusion-exclusion gives
|E_3|>=n^2-n-2[binomial(a,2)+binomial(b,2)]=2ab.
Combining with (2) proves (5). QED.

## 7. Strengthening the seven-element base case to 109

The general bound already gives N>=107. Antipodal sets have N>=120, so
only p=0 needs consideration at N=107 or 108.

At N=107, packing gives |E_3|<=21, while (2) gives |E_3|>=21. Equality
forces 2Delta subset Delta. Doubling is a permutation of Z/107Z, so Delta,
of size 42, would be invariant. But 2 has multiplicative order 106 modulo
the prime 107: 2^53=-1 and 2^2!=1. Its nonzero residues form one orbit
of length 106. No invariant subset of size 42 exists.

At N=108, the exterior size is 21 or 22. The case 22 is an exact paired
partition. A has mixed parity (otherwise N>=128), and n=7 is odd, so a
base can be chosen with even target. This contradicts the paired-partition
lemma, which would force the target to be odd for every base.

In the case 21, equation (4) again gives doubling closure. Parity sizes
1 and 6 are impossible because the six-element parity class would be
valid in Z/54Z, contradicting the n=6 bound 60. Sizes 3 and 4 are impossible
by (5), which would give |E_3|>=24. The only possibility is sizes 2 and 5.
Then Delta has 20 odd elements and 22 even elements. Doubling the 20 odd
elements produces at least 10 distinct elements congruent to 2 modulo 4,
all in Delta.

Some odd difference must be coprime to 3. Otherwise every cross-parity
difference would be divisible by 3, forcing all points of A into one
coset of the subgroup of order 36; dissociation would require 64 elements
in that subgroup. An odd difference not divisible by 3 has order 108.
After two doublings its orbit lies in 4G, has order 27, and has 18 distinct
elements under further doubling, since ord_27(2)=18. Closure puts all
18 into Delta. They are disjoint from the previous 10 elements congruent
to 2 modulo 4. This requires at least 28 even differences, contradicting
the count 22. Thus 108 is impossible as well.

We have proved N>=109 for n=7. In particular even N>=110. Antipodal
reduction now gives N>=218 for n=8, or N>=220 if N/2 is even.

## 8. The eight-element bound is 187

The quadratic theorem gives N>=184. An antipodal set already requires
N>=218, so the three endpoints 184,185,186 can be studied with p=0.

### Excluding 184

Packing forces |E_3|=28. The exact paired partition forces an odd target,
so the two parity class sizes in A are 1,7 or 3,5. Sizes 3,5 give |E_3|>=30
by (5), a contradiction. Sizes 1,7 give a valid seven-element set in
Z/92Z, contradicting the bound 109. Thus 184 is impossible.

### Excluding 185

Again |E_3|=28, so 2Delta subset Delta, and odd-order doubling makes Delta
invariant. Its size is 56. In Z/185Z there is one nonzero doubling orbit
of length 4 (the elements of order 5), and five orbits of length 36 (orders
37 and 185). Here ord_5(2)=4 and ord_37(2)=36; the latter follows from
2^18=-1 and 2^12=26 modulo 37. No integer of the form 36u+4v, with
0<=u<=5 and v in {0,1}, equals 56. Thus no such invariant Delta exists.

### Excluding 186

The exterior size is 28 or 29. Size 29 gives an exact paired partition,
forcing odd target. Parity sizes 3,5 contradict (5), and sizes 1,7 give
a valid seven-element set in Z/93Z, also impossible.

Suppose its size is 28. Doubling closure holds. By (5) the parity sizes
can only be 1,7 or 2,6 (one parity containing all eight points would give
N>=256). The first case is already excluded. Translate by a point in the
six-element class, so A has six even and two odd points. The target s is
even. Each parity of S has 64 elements. Counting E_3 and its reflected
copy inside each parity class of size 93 shows |(E_3)_even|<=14 and
|(E_3)_odd|<=14. Their total is 28, so both equal 14.

Now (2A+A)_odd has 2+14=16 elements, from exactly 8*2=16 pairs consisting
of a center in 2A and an odd point of A. Thus all these representations
must be unique. Let u,v be the two odd points. Their difference delta is
nonzero and even. The even difference set is closed under doubling by
(4). Doubling is a permutation of the even subgroup of order 93, so that
finite even difference set is invariant. Hence delta=2(a-c) for some
a,c in A. The equality 2a+v=2c+u gives two different representations in
the odd portion of 2A+A, contradicting its injectivity. This excludes 186.

Therefore every valid eight-element cyclic set satisfies N>=187.

The proof does not exclude 187, and does not assert existence there.

## 9. Modulo 4 and larger quotients

The quarter-pair parameter e is a concrete restriction modulo 4: it can
be nonzero only when 4 divides N. Without an antipodal pair it improves
the exterior-triple count by one, rather than worsening it. The original
complementary-double count and the parity energy estimate apply in every
even modulus; antipodal reduction applies to the subgroup of order two.

For n=8, iterating the antipodal reduction twice gives N>=4*60=240.
If three reductions end at an odd five-element quotient, its modulus is
at least 31 by Section 5, so N>=8*31=248. These are conditional bounds:
the required antipodal pairs in successive quotients are not forced by
the present arguments.

There is also an exact occupancy inequality for any divisor d of N.
Let c_r count S in residue class r modulo d, and e_{k,r} count E_k there.
Whenever j+k<=n, the disjoint packing gives

\[
 N/d\ge c_r+e_{j,r}+e_{k,s-r} \quad\text{for each }r\pmod d.       \tag{6}
\]

Unlike parity, higher quotient classes are not automatically balanced.
A sufficient condition for balance modulo 2^t, when 2^t divides N, is that the translated
differences contain distinct coordinates of 2-adic valuations 0,1,...,t-1.
Their 2^t subset sums are distinct modulo 2^t: in a putative difference,
the coordinate of lowest valuation cannot be canceled by the higher ones.
Thus they cover every residue, and including the other coordinates gives
c_r=M/2^t. Equation (6) then gives corresponding subgroup bounds.

This is a conditional structural statement, not an assumption about all
valid cyclic sets. Beyond the bounds above, no further unconditional
general estimate was proved from higher quotient occupancy in this stage.

## 10. A tested but unproved four-term extension

The proven packing theorem gives, for n>=8,

\[
 N\ge M+2|E_4|,\qquad E_4=T_4\setminus L_2,\quad T_4=C+(A+A).
\]

Thus T_4={2a+b+c:a,b,c in A}. The exact identity T_4 intersect S=L_2 is proved
in Section 3. What is missing is a general lower bound for its size.

One precise hypothesis tested was

\[
 |E_4|\stackrel{?}{\ge}\binom n3+n-1-3p \qquad(n\ge4).           \tag{7}
\]

This would give |E_4|>=60 at n=8 when p=1, and >=63 when p=0, hence
the conjectured lower bound 248 for n=8. It is NOT proved here.

In the known n=8 construction modulo 248, |E_4|=60; the binary construction
modulo 255 has |E_4|=63. No failure was found in the stated small tests.
Those observations are evidence only, particularly because most tested
sets belong to the same binary construction family.

The attempted proof via translated pair-sum sets stalls at their
intersections. For triples the translates are of A itself, whose nonzero
differences are controlled by validity. For four terms the translates
are of A+A, whose differences can have many representations. Validity
permits collisions between two representations that both repeat elements.
For example, in the known valid eight-element construction modulo 248,

\[
 2\cdot1+3+63=2\cdot15+31+7=68.
\]

The marked three-element supports on the two sides are disjoint, and
both sides are four-term repeated representations outside S. Thus a
naive injection of marked triples into E_4 is false. The uncorrected
claim |E_4|>=binomial(n,3)+n-1 also fails: 60<63 in this same construction.
Neither counterexample disproves the corrected hypothesis (7).

## 11. Computational verification

`stage2_experiments.py` contains the reproducible checks. It directly
verifies 28 explicit valid sets, including binary constructions for
n=4,...,9 at the known minimum, at odd modulus 2^n-1, and at 2^n.
Additional even-modulus cases include sets without antipodal pairs, both
with and without a quarter-distance pair. It checks all 171 translated
bases of these sets. It verifies the exact identities for
T_2,T_3,T_4, the allowable complementary packings, the triple-size bound,
cyclic difference multiplicities, and antipodal quotient validity.

It also checks 102 explicitly generated perturbation candidates, of which
three are valid, and tests (7) on those and the 171 known-set translations.
No counterexample to (7) was found; no absence of sampled counterexamples
is used in any proof. The group arithmetic checks compute the five
36-element and one 4-element doubling orbits modulo 185 and verify
ord_107(2)=106 and ord_27(2)=18. They enumerate residues of individual
small groups, not candidate sets across moduli.

All checks passed. The largest single direct validity check enumerates
binomial(17,9)=24310 multisets. All computations complete in seconds.

## 12. Bound comparison and remaining obstacles

| n | Previous-stage bound | Bound proved in Stage 2 | Conjectured minimum |
|---|---:|---:|---:|
| 4 | 12 | 12 | 12 |
| 5 | 21 | 28 | 28 |
| 6 | 39 | 60 | 60 |
| 7 | 71 | 109 | 124 |
| 8 | 135 | 187 | 248 |
| 9 | 265 | 328 | 504 |

The previous-stage n=9 entry is obtained from its parity-rounded formulas,
not claimed to have been listed in the original report. None of these
lower bounds certifies existence at the endpoint except where the known
construction matches it.

The principal unresolved step is proving a lower bound for E_4 or higher
E_k despite permitted repeated-versus-repeated collisions. The quadratic
result improves the additive term from O(n) to O(n^2), but still leaves
the exponential leading term M unchanged. For n=8, a proof of |E_4|>=60
would close the entire remaining gap; the tests do not prove it.

At N=187 the cubic counting argument would permit |E_3|=29 and one
missing center-pair intersection. The full doubling-closure obstruction
used at 185 is then unavailable. A stronger control on near-closure,
triple intersections, or four-term sumsets is required. This report does
not assert that a valid set at 187 exists.

Higher quotient occupancy helps when specific valuation patterns are
present, but forcing those patterns for arbitrary valid sets is another
unresolved structural problem. This completes Stage 2 without opening a
further research stage.
