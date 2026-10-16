# Stage 38: audit, failed growth routes, and counterexamples to weaker lemmas

Research dates: 2026-10-10--11 (America/New_York). Continues open, unmerged PR #9
at commit archived-source. Earlier reports are preserved.

**The odd-modulus theorem is still OPEN.** No valid eight-point counterexample
was found, and no new modulus is excluded. The Stage 37 verification boundary
is unchanged: the proved general lower bound is 207; odd 207,209,...,247 remain
unexcluded. Discovery-only absence and timeouts are not certificates.

This round delivers counterexamples to two investigated intermediate claims,
an audit of the Stage 37 proof, numerical calculations for applicable growth
theorems, two substantive structural dead ends, and a sharply stated remaining
coupling problem. It does not claim |4A|>=159 or a complete proof of N>=248.

## 1. Definitions and the precise standard-theorem comparison

Write kA for the k-fold sumset ALLOWING repetitions. Write 2.A={2a:a in A}
for dilation; older reports sometimes call this latter set "2A". The two
notations must not be confused. Let s=sum(A), Q the squarefree quartic sums,
T3=(2.A)+A, and T4=(2.A)+(A+A). Validity means that the all-ones count vector
is the unique nonnegative count vector of total eight representing s.

Translate 0 into A. Its difference-generated subgroup contains the 128
distinct subset sums of A minus 0. In odd N<248 any proper subgroup has order
at most N/3<128. Therefore A generates the full group after translation.
This uses elementary validity, not the numerical exclusions in Stage 37.

For a valid set, every squarefree cubic has a unique representation among
ALL cubic multisets. Odd order gives 36 distinct unordered pair sums and
56 distinct nonzero ordered differences Delta. Put

    h = |{d in Delta:2d not in Delta}|/2,
    R3 = sum_y binomial(m_y-1,2),  m_y=#{(a,b):2a+b=y},
    k = h+R3.

The previously proved cubic formula yields

    |T3|=36+k,    |3A|=56+|T3|=92+k,    0<=k<=28.

The upper limit follows from the 64 marks, not a conjectural fiber cap.
Stage 26 additionally supplies h>=1 for an actual sub-248 counterexample;
using that result retains its recorded computer-assisted dependencies.

**Kneser.** For finite nonempty X,Y in an abelian group, with stabilizer
H of X+Y, |X+Y|>=|X+H|+|Y+H|-|H|. Thus an aperiodic sum has size at least
|X|+|Y|-1. See [Lev, Section 1](https://www.numdam.org/item/10.5802/jtnb.485.pdf).
Stage 37 makes 2A,3A,4A aperiodic in the remaining odd interval. Substituting
the actual known cardinalities gives:

|Application|Lower bound obtained|
|---|---:|
|A+A|15, superseded by exact size 36|
|2A+A|43, superseded by exact size 92+k|
|2A+2A=4A|71|
|3A+A=4A|99+k, between 100 and 127 when 1<=k<=28|

Applying Kneser to T3+A would require its OWN stabilizer: aperiodicity of
4A does not imply aperiodicity of its subset T4. That shortcut is unavailable.

**Sidon isoperimetry, a stronger applicable bound.** A generating Sidon set
S containing 0 with |S|>=3 has second isoperimetric number 2|S|-3. Equivalently,
for |X|>=2 and |X+S|<=|G|-2, the boundary |X+S|-|X| is at least 2|S|-3.
See [Hamidoune--Serra--Zemor, Lemma 11](https://arxiv.org/pdf/math/0603478v2).
Here S=A and X=3A. The packing proved below gives |4A|<=158, so at least
49 group elements are outside 4A. All hypotheses hold. Consequently

    |4A|>=|3A|+13=105+k.

This ranges from 106 to 133, still below 159 for EVERY possible k.
Also 2.(A+A) has 36 values, all in T4 and disjoint from Q by validity;
hence |4A|>=70+36=106. The combined bound is max(106,105+k).

**Kemperman--Scherk representation bound.** For finite nonempty X,Y and
c in X+Y, let r(c) count ordered pairs (x,y) with x+y=c. Then
|X+Y|>=|X|+|Y|-r(c); see
[Hamidoune's formulation](https://arxiv.org/abs/0909.5664). For q in Q,
r_(3A,A)(q)=4 and r_(2A,2A)(q)=6. Those applications give 96+k and 66,
respectively, weaker than the above. For X=Y=4A, validity gives r(s)=70;
the theorem gives |8A|>=2|4A|-70, again only the packing bound.
"Unique eight-term multiset" is NOT a unique ordered pair of quartic residues.

For prime N, Cauchy--Davenport gives the same basic unrestricted bounds.
The prime-group restricted-sum theorem gives |4^A|>=min(N,4*(8-4)+1)=17,
where 4^A is the squarefree sumset. We already have |4^A|=70. It supplies
no count for T4. The prime-only hypotheses cannot be silently used at
composite orders; see the discussion in
[Bajnok](https://arxiv.org/abs/1305.2141).

## 2. Audit of the exact intersection and the aperiodicity proof

Validity first implies hereditary squarefree protection: replacing a subset
U of A by a different equal-length multiset and appending its complement
would be a rival for s. In particular all 70 squarefree quartics are distinct
and no repeated quartic represents one of their values.

If x belongs to 4A intersect(s-4A), concatenate any quartic representations
of x and s-x. Validity forces the all-ones vector. Both quartics are therefore
complementary four-subsets. Conversely complementary four-subsets provide
every Q value. Thus

    4A intersect(s-4A)=Q,    |Q|=70.

**Converse, with a necessary hypothesis.** If every squarefree quartic has
a unique representation among all quartics, and the displayed intersection
equals Q, then A is valid: split any eight-term representation of s into
two quartics. Their values lie in Q; unique quartic representations force
complementary squarefree subsets. Merely requiring 70 distinct Q values is
not sufficient for this converse (Section 5 gives a checked counterexample).

The proof in [stage37_aperiodicity.md](stage37_aperiodicity.md) passes the audit:

1. A period subgroup H of 4A also preserves s-4A and Q. Hence |H| divides
   gcd(N,70). In odd order a nontrivial H has size 5,7,or35.
2. For a four-subset C with complement E, a different multiset M supported
   ON C representing sum(C) modulo H has error e in H. Periodicity supplies
   a quartic L with sum(L)=sum(E)-e. M+L is a rival: if its counts were all
   ones, L would need all four points of E and could not repair M on C.
3. This forces projected points to be distinct and forbids every different
   squarefree pair replacement, including replacements by doubled points.
   All involved points fit into a four-subset C, so Step 2 applies.
4. An equality a-b=c-d gives a+d=c+b. Squarefree pair protection handles
   every nontrivial case except two doubled pairs; injectivity of doubling
   in the ODD quotient handles that case. Thus its 56 ordered nonzero
   differences are distinct and |G/H|>=57.
5. Nontrivial H would imply N>=5*57=285. Finally a period of kA, k<=4,
   would preserve kA+(4-k)A=4A.

The critical challenge was whether quotient validity had been overclaimed.
It had not: the argument proves the required validity of four-position
subsets, not validity of the full projected eight-set. Another critical
point is support containment of M in C; the proof explicitly requires it.
No repair or new assumption is needed.

In odd order the midpoint s/2 cannot lie in 4A: membership would place it
in Q and equate two complementary squarefree quartics. The union therefore
misses that point and

    N>=2|4A|-69.

This is the odd rounding of the packing bound; it excludes no new order.
For example N=247 still allows |4A|=158. A proof of |4A|>=159 would actually
force odd N>=249, and would finish the requested interval.

## 3. Structural attempt I: grow 3A using its protected outputs

The specific extra restriction is not just absence of periods. Every
squarefree quartic has exactly four representations in 3A+A, one for each
choice of the last point, and every distinct quartic equality u=v must have
both an entry of u-v at least 2 and an entry at most -2. Otherwise the
all-ones vector plus or minus u-v is an eight-term rival.

More generally that sign restriction holds for every equal-degree relation,
not just cubics or quartics. Collections of individually permissible
relations must remain compatible with it after cancellation and addition.
This compatibility is what the single-sumset growth theorems discard.

Set X=3A. Counting the eight translates X+a gives 8|X| incidences; each
protected Q output accounts for exactly four. At a repeated quartic value
t, the number of incident translates is exactly the union of supports of
its quartic representations, and can be as large as eight. Thus simply
using the protected outputs gives only

    8|3A| <= 4*70+8|T4|,
    |T4|>=|3A|-35=57+k,
    |4A|>=|3A|+35=127+k.

This elementary protected-output bound IMPROVES the standard Sidon bound,
but it still ranges only from 128 to 155 when 1<=k<=28. It holds for every
valid eight-set in any finite abelian group: odd order and aperiodicity are
not needed for the 35-point increment. Applying the representation theorem
at a Q output gives only |3A|+4. To finish, the increment needs to be 67-k,
leaving 32-k additional values beyond the proved 35, at least four even
at k=28. In odd order its packing consequence N>=185+2k recovers the
earlier cubic packing bound and supplies no new modulus exclusion.

The 35-point increment is sharp over general abelian groups. Take 0 and
the seven coordinate basis vectors in (Z/2)^7. An eight-term target rival
would need odd counts at each of the seven basis vectors; with only eight
slots this forces their counts all to be one and the zero count to be one.
Thus the set is valid, |3A|=sum_(j=0)^3 binomial(7,j)=64 and |4A|=99.
The independent checker verifies this model too. It is outside the odd
cyclic scope, but rules out strengthening this incidence argument using
validity alone without an additional restriction.

**Exact gap:** these arguments count supports or use the minimum boundary
over arbitrary X. They never prove that the repeated-output incidence
patterns can be simultaneously realized without a forbidden higher-degree
relation. No estimate for that compatibility has been proved here. This
route was stopped at this gap, not recast as a new collision-budget bound.

## 4. Structural attempt II: complementary pairing and apolarity

Work over R in the group algebra with basis e_x, and define

    B(e_x,e_y)=1 if x+y=s, and 0 otherwise.

This is a nondegenerate bilinear form on the N-dimensional group algebra.
Let V be the span of the basis vectors for 4A. Its restricted matrix has
nonzero rows precisely at the 70 Q values. On those values it is the
permutation pairing complementary subsets; the other rows are zero.
Therefore its rank is 70 and its radical is the repeated-quartic span,
of dimension |T4|=|4A|-70. Since the radical lies in V-perp,

    |4A|-70 <= N-|4A|.

This recovers the packing bound, not a lower bound for the radical. In odd
order the 70-dimensional piece comprises 35 complementary pairs with no
fixed point; the missing midpoint supplies the one-element rounding above.

The limitation is concrete. In Z/247 with reflection x->-x, set

    Q0={1,...,35} union {212,...,246},
    V0=Q0 union {36,...,123}.

Then |Q0|=70, |V0|=158, V0 intersect(-V0)=Q0, and the union is all nonzero
residues. V0 is aperiodic because gcd(158,247)=1. The pairing has rank 70
and radical dimension 88. This is an abstract reflection countermodel,
NOT a sumset generated by an eight-set and NOT a counterexample to validity.
It shows exactly why the pairing and aperiodicity alone cannot supply 89.

The polynomial version has the same gap: degree-eight coefficient extraction
is the squarefree monomial, so its middle catalecticant has rank 70, but this
does not bound the extra repeated-quartic dimensions. Classifications of
[minimal Waring decompositions](https://arxiv.org/abs/1201.2922) require minimum
rank. Our character decomposition has N summands and has not been shown
minimal; imposing such a hypothesis would be an invalid extension.

## 5. Targeted pivot: competing hypotheses and actual counterexamples

### 5.1 Sidon, small dilation overlap, and aperiodicity do not force growth

The tested weaker lemma was: these three properties, in the remaining odd
interval, force |4A|>=159. It is FALSE. Take

    N=245, A={0,1,7,21,49,84,99,140}.

The separate count-composition checker confirms:

|Property|Value|
|---|---:|
|Distinct unordered pair sums|36|
|Distinct ordered nonzero differences|56|
|h, R3|13, 1|
|Maximum dilation overlap|3|
|Periods of 4A|{0}|
|Sizes of 3A and 4A|86, 130|
|Distinct squarefree cubics, quartics|52, 61|

Aperiodicity also has a short arithmetic check: a period order divides
gcd(245,130)=5, so the only nontrivial candidate is the subgroup generated
by 49. But 16 is in 4A and 65=16+49 is not. The set generates the group
because it contains 0 and 1.

It is NOT valid. For example 0+1+7+21=29 is a squarefree quartic, but
99+3*140=519=29 modulo 245. Appending 49,84,99,140 gives an eight-term
rival with counts (0,0,0,0,1,1,2,4). Its integer sum is 891, congruent to
the all-ones sum 401. Cubic and quartic protection are precisely missing.

### 5.2 Cubic protection alone cannot exclude the interval

A different possible shortcut was the stronger claim that no eight-set
in odd 207<=N<248 can have all its squarefree cubics uniquely represented.
It too is FALSE. The targeted extension experiment finds

    N=247, A={0,1,3,7,15,31,63,165}.

All 56 squarefree cubics are distinct and are singleton fibers among all
120 cubic multisets. All 36 pair sums and 56 differences are distinct.
Here h=12, R3=0, |T3|=48, |3A|=104, |4A|=199, and 4A is aperiodic.
But the original target is 285=38 modulo 247, also represented by
six zeros, 7, and 31. In particular this is NOT a valid set.

The independent checker finds the sharper quartic obstruction

    0+1+3+7=11=3*31+165 modulo 247.

Its maximum dilation overlap is SIX, at shift 246. Thus it does not refute
a strengthened approach using the Stage 29 overlap-at-most-five theorem.
The two-coordinate follow-up finds a second cubic-protected set,
{0,1,3,7,15,31,82,123} modulo 247. It has the same cardinality diagnostics,
also overlap six, and the rival consisting of seven zeros and 15.
No affine-equivalence classification is claimed for these two sets.

### 5.3 Bare intersection equality is not full validity

For A={0,1,3,7,15,31,63,127} modulo 251, the 70 squarefree quartic values
are distinct, 4A is aperiodic, and 4A intersect(s-4A)=Q EXACTLY.
Nevertheless

    0+1+3+7=11=1+7+127+127 modulo 251.

Appending the four-point complement gives a rival with counts
(0,1,0,1,1,1,1,3). This example lies OUTSIDE the requested interval and
fails Sidon uniqueness; its role is to disprove the general converse that
omits protection of Q. Section 2's converse includes that hypothesis.

## 6. Sharply stated remaining lemma and why these methods do not prove it

The growth route still lacks a theorem coupling protected quartic outputs
and the allowable repeated-output supports across ALL eight coordinates.
The elementary incidence argument improves the boundary from 13 to 35,
leaving exactly 32-k values to prove. The pairing cannot supply them, as
its abstract dimension-88 model
shows. The N=245 witness refutes a route using only Sidon, aperiodicity,
and low overlap; the N=247 witness refutes cubic separation alone.

An alternative, strictly stronger hypothesis worth distinguishing is:

**Cubic--overlap alternative (UNPROVED).** For every eight-element A in
an odd cyclic group of order 207<=N<248, if every squarefree cubic has a
unique representation among all cubic multisets, then some shift t has

    |(2.A) intersect(A+t)|>=6.

This is a different missing lemma, not a quartic-loss identity. It imposes
no eight-term validity, no quartic protection, and no aperiodicity. If it
were proved, hereditary cubic protection and Stage 29 would directly
contradict any remaining valid set. Its use would retain Stage 29's finite
computer-assisted dependency; it is not an independent replacement for it.

The two cubic-protected N=247 examples satisfy its conclusion, so the bare
cubic shortcut fails exactly where the low-overlap restriction enters.
The experiments below produce no cubic-protected low-overlap example in
the requested interval. This is limited discovery evidence, not proof or
a probability estimate. Standard Sidon isoperimetry contains no dilation
overlap hypothesis, and the rank calculation only pairs quartic values;
neither method controls this cubic--doubling coupling. A proof of the
alternative, or a verified counterexample to it, is a precise next test.
No additional search cap was increased to hide this gap.

## 7. Declared experiment scopes, reproduction, and verification boundary

1. `stage38_growth_experiment.py`: 3264 single-coordinate binary
   presentations and 9801 two-coordinate presentations, exactly 13065.
   Cap 45 seconds; completed in about 2.83 seconds. After 537 nondistinct
   presentations, 606 duplicates, and 7228 non-Sidon candidates, 4694
   distinct Sidon pairs were evaluated. Only the known N=255 binary set
   has protected cubics in this family. No arbitrary-set coverage follows.
2. `stage38_coset_experiment.py`: six-point Sidon subsets containing 0,1
   in kernels of orders 33,35,45,49, with two points in a second coset
   using a missing signed difference. This is a declared structural family,
   not a full affine census. A 30-second cap interrupted the order-49 branch
   at prefix [0,1,12,27,45]. It evaluated 55388 candidates and retained the
   positive N=245 counterexample. The partial state and counters are saved.
   No absence, exclusion, or complete kernel-49 coverage is inferred.
3. `stage38_cubic_probe.py`: all 6232 nonduplicate-point extensions of the
   fixed seven-point binary set at the named 27 orders; 12*5000 seeded
   annealing steps at each of 239,247,255 (180000 attempted, 174229 evaluated);
   then all 182286 two-coordinate presentations about the N=247 witness
   with the first four points frozen (173520 have eight distinct points).
   The follow-up domain was fixed after discovering the first cubic witness.
   Final code reruns the declared phases in one 30-second budget and completed
   in about 5.03 seconds. Seeded heuristic minima exclude nothing. All
   zero-score witnesses are saved, including controls outside the interval.
4. `stage38_independent_check.py`: no producer, historical verifier, or
   numpy imports. It generates weak compositions instead of sorted word
   lists, rebuilds the residue fibers, checks every saved diagnostic value,
   and checks all 6435 eight-term count vectors for each of 15 distinct
   retained cyclic witnesses (96525 total), plus 6435 for the exponent-two
   sharpness model. Eight corrupted-rival checks reject count vectors
   with wrong mass or wrong residue, including mass-preserving changes.
   Cap 30 seconds; completed in about 0.25 seconds.
   This validates positive witnesses, not negative searches or their coverage.

Run from this directory:

```text
python -B stage38_growth_experiment.py
python -B stage38_coset_experiment.py
python -B stage38_cubic_probe.py
python -B stage38_independent_check.py
```

The growth, coset, and independent scripts use standard-library Python;
the cubic heuristic requires numpy. The coset script imports only the new
growth diagnostic, and the independent checker imports none of them.
JSON evidence has matching filenames ending `_results.json`; the independent
output is `stage38_independent_results.json`. Runtime-limited coset counts
may change between runs. Its selected witnesses are explicitly recorded;
the independent checker validates their mathematical properties directly.

Separate implementations and proof challenges in this round are by the
same agent, not independent human review or a formal proof assistant.
No historical certificate was rerun, no earlier PR was merged, and no process
remains running. No literature novelty claim is made.
