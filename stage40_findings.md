# Stage 40: proof work aimed specifically at 248

2026-10-11. Continues Stage 39 / open PR #11. The lower-bound theorem
N>=248 remains OPEN. This stage proves two period restrictions and an
exact parity reduction of the remaining contradiction. It does not exclude
a new modulus. Earlier PRs and historical exclusion boundaries are preserved.

The principal missing step is now stated without an overlap hypothesis or
a stronger universal quartic-growth claim:

> In odd 207<=N<248, for an eight-set with full squarefree quartic
> protection, prove that s belongs to 2-dot(3A)+(A+A).

Here full protection means that every squarefree four-term multiset has
exactly one representation among ALL four-term multisets. The doubled
sumset 2-dot(3A) is dilation, not the six-fold sumset. The statement is a
target, not a theorem. Section 3 proves why it would finish the odd interval.

## 1. A quotient descent lemma, with complete elementary proof

Let A have n distinct points in a finite abelian group. For r>=3, let Q_r
be the squarefree r-sums and T_r the repeated r-sums. Suppose every
squarefree r-sum has a unique representation among all r-term multisets.
Let H be any subgroup preserving T_r, and pi:G->G/H the projection.
Assume r<=n.

**Lemma.** The projected n labeled points are distinct, and every projected
squarefree (r-1)-sum has a unique representation among all (r-1)-multisets.

First, pi(Q_r) and pi(T_r) are disjoint. If q-t belongs to H with q in Q_r
and t in T_r, periodicity gives q=t+(q-t) in T_r, contradicting protection.
If two projected labeled points i,j coincide, choose an r-subset containing
both. Replacing i by another j produces a repeated r-word with the same
projected value as that squarefree word. This contradicts disjointness.

Now let U be a squarefree (r-1)-word and M a different (r-1)-word of the
same projected sum. If M contains a label b outside U, append b to both:
U+b is squarefree of degree r, whereas M+b repeats b. If M is supported
on U, it must be repeated: otherwise its degree and support would force
M=U. Append any b outside U; U+b is squarefree and M+b remains repeated.
In either case pi(Q_r) meets pi(T_r), a contradiction. QED.

This proves protection one degree lower in the quotient. It does NOT prove
full eight-term validity in that quotient, or protection of its squarefree
r-sums against other squarefree r-sums.

### A useful elementary cubic bound

In an odd group, eight pair-protected points have 36 distinct two-term
multiset sums and 56 distinct nonzero ordered differences. Squarefree pair
protection handles an equality a+d=c+b whenever one side is squarefree;
injectivity of doubling handles two doubled sides. Thus every nonzero
ordered difference has exactly one representation.

There are 64 marks 2a+b in T_3. Two marks with the same center cannot
coincide. For a fixed unordered pair of different centers a,c, an equality
2a+b=2c+d determines b-d=2(c-a). Ordered-difference uniqueness allows
at most one unordered pair of coincident marks for those centers. Therefore
the total number of coincident mark pairs is at most binomial(8,2)=28.
For mark multiplicities m_y,

    64-|T_3| = sum_y(m_y-1) <= sum_y binomial(m_y,2) <=28.

Consequently |T_3|>=36. Cubic protection additionally gives 56 distinct
squarefree cubic values disjoint from T_3, so |3A|>=92.

### Theorem A: T_3 is aperiodic in every odd group

Let the eight-set be cubic-protected. If T_3 had a nontrivial stabilizer H,
the descent lemma would make its eight projected points pair-protected.
The quotient remains odd. Its T_3 has at least 36 values, by the preceding
bound. Since T_3 is a union of H-cosets,

    |T_3|=|H|*|pi(T_3)| >=3*36=108.

But T_3 has only 64 marked words. Contradiction. Thus T_3 is aperiodic.
Full eight-term validity is more than this theorem needs.

### Theorem B: T_4 is aperiodic below odd order 315

Let the eight-set be quartic-protected. If T_4 had a nontrivial stabilizer H,
the descent lemma would make the quotient eight-set cubic-protected.
In an odd group a cubic-protected eight-set has at least 69 distinct
squarefree quartic values: a collision between different squarefree quartics
must have disjoint supports, since canceling a common point would violate
cubic protection. Such subsets are complementary. Their common residue
is s/2, and doubling is injective. At most one complementary pair can
collide, so 70 words give at least 69 values.

The quotient repeated quartics contain the dilation of all 36 two-term
multiset sums, hence at least 36 values. These are disjoint from the quotient
squarefree quartics by pi(Q_4) disjoint from pi(T_4), proved above. Hence

    |G/H| >=69+36=105,
    |G|=|H|*|G/H| >=3*105=315.

This proves the theorem. In particular T_4 is aperiodic throughout the
remaining odd interval. This resolves the specific stabilizer gap left in
Stage 38 for applying Kneser to T_3+A.

### Deductive challenges to these proofs

The proof uses a period of T_r itself; a period of its larger parent sumset
is not substituted. Quotient points are shown distinct before counting
marks. The appended label can already occur on the opposing side; that is
exactly what creates a repeated word. The quotient r-sums need not be
distinct; the 69-value bound, rather than an unjustified 70, accounts for
this. Cardinalities of H-periodic sets multiply by |H| exactly. Quotient
oddness and |H|>=3 are both necessary. These are separate deductive
challenges by the same author, not independent human review or a formal
proof-assistant check.

## 2. First quantitative attempt: remove periods, then calculate growth

For finite nonempty X,Y in an abelian group, Kneser gives

    |X+Y| >= |X+H|+|Y+H|-|H|,

where H is the stabilizer of X+Y. Aperiodicity gives |X+Y|>=|X|+|Y|-1.
See the primary-source formulation in
[Lev, Section 1](https://www.numdam.org/item/10.5802/jtnb.485.pdf).

The inherited cubic identity is |T_3|=36+k and |3A|=92+k, where
k=h+R3 and 0<=k<=28. The new theorem permits the previously unjustified
application to T_3+A=T_4. Its ACTUAL result is

    |T_4| >= |T_3|+8-1 =43+k.

This is at most 71, so does not reach 89. No implication from aperiodicity
to faster growth is assumed.

For a generating Sidon A containing zero, |X|>=2 and |X+A|<=N-2, the
second isoperimetric bound is |X+A|-|X|>=2|A|-3=13; see
[Hamidoune--Serra--Zemor, Lemma 11](https://arxiv.org/pdf/math/0603478v2).
In a hypothetical odd sub-248 valid set, the normalized A generates G:
it has 128 distinct subset sums in its difference subgroup, whereas a
proper subgroup of an odd group here has size at most N/3<128. The quartic
packing gives |T_4|<=88, so its complement has more than two points. Taking
X=T_3 therefore yields |T_4|>=49+k, still at most 77.

The stronger protected-output incidence bound from Stage 38 remains

    |T_4|>=57+k, or |4A|>=127+k.

Indeed 3A+A has 8|3A| incidences; the 70 squarefree quartic outputs each
have exactly four, and a repeated output has at most eight. This yields
|T_4|>=|3A|-35. Even k=28 gives only 85 repeated values. The new period
proof closes a logical gap but does not improve this best numerical bound.
The exact quantitative gap is still 32-k repeated values. This attempt
fails at that estimate, not at an unverified stabilizer premise.

## 3. An exact 248-specific target: a two-parity covering statement

Assume full quartic protection. It implies protection of every squarefree
sum of degree at most four by padding the original side with distinct
outside labels. Let c be a non-original eight-term representation of s,
and J its support. A word using all eight labels is necessarily original,
so |J|<=7. Cancel one copy of each present label from both sides:

    sum_(i not in J) a_i = sum_(i in J)(c_i-1)a_i.

Both degrees are 8-|J|. If |J|>=4, this is a different representation of
a squarefree sum of degree at most four, impossible. Thus |J|<=3.

An eight-term word on at most three labels has either zero or two odd
counts, since its total is even. If two counts are odd, write it as

    c=2v+e_i+e_j,  i!=j,  sum(v)=3.

If all counts are even, c=2w with sum(w)=4. Select one occurrence e_i in w
and write c=2(w-e_i)+e_i+e_i. Thus EVERY possible remaining rival has value
in

    P(A) = 2-dot(3A)+(A+A).

Conversely every word defining P(A) has zero or two odd counts, whereas
the original eight-point word has eight odd counts. If s is in P(A), its
defining word is therefore a genuine rival, without further support checks.
We have proved the exact equivalence

    under full quartic protection:
    A is valid  <=>  s NOT in P(A).                         (1)

In odd order let mu=s/2. Dividing (1) by two gives the equivalent hole
placement condition

    3A intersect (mu - (A+A)/2) = empty.                    (2)

The 36 pair sums are distinct, so (2) forces an affine dilate of the entire
pair sumset into the complement of 3A. Separating the doubled pairs from
the squarefree pairs, this says both

    mu not in 4A,
    (s-a-b)/2 not in 3A for every distinct pair a,b in A.

The first condition uses the eight doubled-pair holes mu-a; the other 28
holes come from squarefree pairs. This is stronger than checking only the
midpoint, and has no Stage 29 computational dependency.

**Precisely what remains unproved.** For every eight-set in odd
207<=N<248 with full quartic protection, prove s in P(A), equivalently
prove that the affine pair-sum shadow in (2) cannot entirely fit into the
cubic holes. This only asks to cover the particular s; proving P(A)=G or
a universal |4A|>=159 is unnecessary.

Counting does not establish it. Condition (2) gives merely

    N >= |3A|+|A+A| =128+k.

Even its largest value is 156. For prime orders, Cauchy--Davenport applied
directly to P(A) gives |P(A)|>=min(N,127+k), also far from forcing coverage.
At composite orders Kneser would require P(A)'s own stabilizer; neither
new period theorem supplies that. Even granting it trivial gives the same
insufficient bound. What is missing is placement of the specified target
relative to the coupled, dilated summands.

The supporting word script checks all 1380 support-at-most-three words:
260 have no odd count and 1120 have two. It reconstructs each as 2v+e_i+e_j.
This is arithmetic evidence for the reduction, not evidence for the cover.

## 4. Second structural attempt: force 89 pairwise separated quartic words

For any equal-degree equal-sum count vectors u!=v, validity requires both
a coefficient of u-v at least two and another at most minus two: otherwise
allones+(u-v), or its opposite, is a rival. In odd order, common powers of
two in the difference can first be canceled. The resulting integer vector
still has sum zero. If one of its signs has magnitude at most one, adding
it to allones is again a non-original nonnegative eight-term vector.

Construct a graph on the 260 repeated quartic words, with an edge whenever
this test FORBIDS equal values. A clique of 89 would force |T_4|>=89 and
finish the problem without knowing the actual values of A.

The fixed word experiment completes in about 0.13 seconds. Its maximum
clique is 36. More decisively, it produces and saves an explicit proper
65-coloring of the ENTIRE graph. Checking that every edge has differently
colored endpoints is a positive certificate. Thus these pairwise
restrictions alone admit an abstract assignment to 65 repeated values;
they cannot force 89. This is not an assignment realized by a cyclic set.
No conclusion about actual valid sets follows from the coloring.

The missing restriction is concrete: individually allowed equalities can
combine into a forbidden relation. For example four ordinary words with
distinct centers a1,...,a4 and distinct tails b1,...,b4 could individually
pass the pairwise test while all sharing one value:

    2a1+b1+b2 = 2a2+b2+b3 = 2a3+b3+b4 = 2a4+b4+b1.

Adding the first and third and subtracting the second and fourth yields
2(a1+a3-a2-a4)=0. Oddness then forces a1+a3=a2+a4, a forbidden squarefree
pair collision. This illustrates exactly why the graph's coloring is not
a counterexample to validity. A successful word-packing proof must control
closure of the simultaneous relations, rather than only individual pairs.
No larger timeout, residue-set sweep or collision-budget rewrite was used.

## 5. Third structural attempt: pack the subset cube against its dilation

Translate zero into A and let U be the 128 distinct subset sums of the other
seven points. Oddness makes 2-dot U another 128-point set. If their
intersection had size at most eight, their union would give N>=248.

That proposed universal intersection lemma is FALSE. The historical valid
binary eight-set {0,1,3,7,15,31,63,127} in Z/255 has

    |U intersect 2-dot U|=54,  |U union 2-dot U|=202.

This is a counterexample outside the conditional sub-248 interval, not
a counterexample to the original problem. Its validity has a short binary
carry proof: replace the eight set entries by weights 1,2,4,...,128. The
target becomes 255 modulo 255. Eight positive power-of-two coins have sum
at most 1024. The possible positive multiples are 255,510,765,1020; each
has eight binary ones. Any carry reduces the number of coins, so eight
coins cannot reach those targets using a carry. Only 255 can be expressed
without a carry from the available powers, and it uses each once.

Validity DOES restrict a nontrivial overlap 2*sigma(T)=sigma(S). In the
normalized eight-coordinate relation its nonzero coordinates are
2*1_T-1_S and its zero coordinate is |S|-2|T|. All nonzero negative
coordinates are at least minus one. To avoid a rival it is therefore
necessary that

    |S|<=2|T|-2, and T is not a subset of S.

These rank restrictions permit substantial overlap, as the binary example
demonstrates. A conditional bound of eight below 248 would need a NEW
small-order argument coupling the overlaps. It does not follow from
oddness, the distinct subset sums, or this single-overlap replacement.

The saved control also has |3A|=92, |4A|=162, |P(A)|=218 and s absent
from P(A). Thus the parity-covering statement in Section 3 genuinely
needs its small-order hypothesis; it is not a universal consequence of
protection or of the new period restrictions.

## 6. Outcome and reproduction boundary

The new proved progress is quotient descent, unconditional odd T_3
aperiodicity under cubic protection, odd T_4 aperiodicity below 315 under
quartic protection, and the exact two-parity equivalence (1). None is the
248 theorem. The three substantive attacks stop at specified gaps:
insufficient calculated growth after removing periods; a positive abstract
65-coloring defeating the pairwise-word approach; and an actual valid
binary counterexample to the unrestricted cube-overlap shortcut.

The next proof target is the conditional placement/cover in Section 3.
It retains the full quartic restriction missing from the false cubic lemma
and directly produces a rival. The equivalence localizes the problem but
does not supply a quantitative covering proof. No evidence here upgrades
that target from an unproved lemma.

Supporting code uses only Python's standard library:

```text
python -B stage40_odd_collision_graph.py
python -B stage40_parity_reduction.py
```

The first examines one fixed graph of count vectors. The second examines
word parity and one historical N=255 control. They save the correspondingly
named results JSON files. Neither enumerates arbitrary cyclic eight-sets,
checks old exclusion coverage, or searches moduli below 248. The coloring
and the overlap are positive artifacts; the maximum-clique result is a
completed graph calculation, not a certified cyclic exclusion. No process
is left running. No historical discovery-only exclusion is recertified or
promoted. No claim of independent human review, formal verification, or
literature novelty is made.
