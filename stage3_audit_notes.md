# Stage 3 independent audit

Audit date: 2026-10-09. Original reports and scripts are preserved.
This audit reconstructs claims from the definition, rather than treating
passing assertions as a universal proof. No Lean was run.

## 1. Literature baseline and its limits

Sources inspected in this session:

- [Fonollosa v2](https://arxiv.org/html/2607.08366v2), especially Sections 2,
  7, and 8. The all-n theorem fixes the set `{2^i-1}`. Section 7 explicitly
  reports free-set CP-SAT infeasibility for every subthreshold modulus
  through n=7. Thus 124 is a reported global seven-element minimum, not
  merely a minimum for the binary family. Beyond seven the text reports
  search, not exhaustive exclusion. No CP encoding, certificate artifact,
  or independent checker was obtained or run in this session.
- The current [author README](https://github.com/jarfo/min-modulus) states
  that the arbitrary cyclic-set conjecture remains open. Its additional
  all-finite-abelian minimum and equality classification are separate.
  The linked Inal preprint is [OSF C58Q9](https://doi.org/10.17605/OSF.IO/C58Q9).
  The README's current layout lists only the axiom audit under `scripts`.
  Direct GitHub API requests failed; no independent claim about the latest
  commit date is made.
- The current [formal-conjectures source](https://raw.githubusercontent.com/google-deepmind/formal-conjectures/main/FormalConjectures/Arxiv/2607.08366/MinModulus.lean)
  still labels the arbitrary cyclic-set statement open. Reading this source
  is not running a formal checker.
- [Cambie--Gao--Kim--Liu](https://arxiv.org/html/2308.03748v1) proves modular
  subset-sum results and exact classification at cube-size excess at most
  three. Here the seven-point normalized cube has excess 59 through 119;
  that classification does not apply. Its asymptotic maximum-element result
  does not supply the desired finite repeated-sum count.
- [On Unique Sums in Abelian Groups](https://link.springer.com/article/10.1007/s00493-023-00069-w)
  concerns existence of a unique two-term target, not uniqueness of the
  full squarefree eight-term target. Its rectification and asymptotic
  results do not directly establish the finite bound here.

Targeted searches under unique multiset sums, modular subset sums, unique
representations, and cyclic groups found no existing proof of the proposed
quartic bound. This is a bounded literature check, not an exhaustive
novelty review. Some sentences in the paper's open-problem discussion
overstate the fixed-family theorem; its formal definitions and Section 7
make the applicable scopes clear.

## 2. Reconstruction of the essential elementary lemmas

Let A={0} union B be valid, |A|=n, s=sum B. All equalities below are in
Z/NZ. Translation preserves validity because both competing sums use n
terms. For U subset B of size r, suppose a multiset h on B of size
l<=r+1 has sum equal to sum U. Assign each b in B multiplicity
1-1_U(b)+h(b), and zero multiplicity 1+r-l. These are nonnegative,
total n, and have sum s. Validity makes them all one, hence h=1_U.
Orienting an equality of two subset sums toward the larger subset proves
|S|=2^(n-1). Complementation proves S=s-S.

For T_k={2a+a_1+...+a_(k-2)}, and L_(k-2) the subset sums of B using at
most k-2 points, T_k intersect S=L_(k-2). The forward low-set inclusion
uses doubled zero and padding zero. For a subset target with at least
k-1 points, a k-term repeated representation, after deleting zeros,
has length at most k<=r+1. The preceding lemma forces the exact
squarefree target. A designated nonzero repeated element makes this
impossible; a designated doubled zero leaves at most k-2 nonzero terms.
This proves the reverse inclusion without assuming every short repeated
sum is exterior.

For n=8, T_4 and s-T_4 are disjoint: two four-term repeated multisets
would combine into an eight-term competitor, which contains a repetition
even when the repeated point is zero. Therefore S, E_4, s-E_4 are
pairwise disjoint, |L_2|=29, and N>=128+2|E_4|=70+2|T_4|.
Changing the translated base shifts T_4 by -4a and preserves its size;
it does not produce another independent quartic cardinality test.

If a-b=c-d is nonzero, then a+d=c+b. A squarefree pair cannot equal a
different two-term multiset: replacing that pair in the baseline would
give a rival. Thus either the ordered differences are identical, or
both pairs are doubles, with a=d, c=b and 2a=2b. The only exceptional
nonzero difference is the involution N/2. Two antipodal pairs would give
a squarefree cross-pair collision, so at most one is possible. Without
antipodes the 36 unordered two-term multiset sums and 56 nonzero ordered
differences are all distinct.

Validity is hereditary: pad a rival for a subset with one copy of every
omitted point. If A contains 0,t with t=N/2, its quotient identifies only
that pair. A rival quotient multiset has h(0)+1>=1 slots available for
the pair upstairs. Assigning zero or one of them to t corrects either
kernel error in the target sum. If the lifted multiset were baseline,
its projected multiplicities after removing the extra collapsed slot
would be the quotient baseline. Hence the quotient rival lifts to a
rival, a contradiction. The quotient is valid of size n-1.

Consequently, accepting the external seven-element minimum 124 settles
the eight-element antipodal case at N>=248. Without that external
dependency the elementary seven-point bound below gives only 218
(or 220 if N/2 is even).

## 3. Reconstruction of the quadratic and endpoint proofs

Put C=2A, p=0 or 1 according as antipodes are absent or present, r=n-p,
and let e be the number of antipodal pairs in C. A quarter-difference
in A supplies such a pair. Difference uniqueness implies e<=1; e=0
unless 4 divides N. Each of the r translates c+A has n points. Their
pairwise intersections have size at most one, except an antipodal
center pair has 2p points. First inclusion-exclusion gives

    |E_3| >= binomial(n,2)-p-(2p-1)e.

For n>=6, E_3 and s-E_3 can be packed outside S. The n=5 packing of
E_3 with s-E_2 gives 30+e for p=0 and 28-e for p=1; e=1 rounds the
latter to 28 because 4 divides N. The n=6 bound is 62+2e for p=0,
60-2e for p=1, with the latter rounding to 60. At n=7 the no-antipodal
bound is 106; the antipodal quotient gives 120. Induction via that
quotient proves N>=2^(n-1)+n(n-1) for all n>=7.

Three auxiliary facts used at the endpoints are justified as follows.

1. Equality |E_3|=binomial(n,2), p=0 forces e=0 and equality in first
   inclusion-exclusion. All center pairs must intersect and triple
   intersections must be absent. In particular 2Delta subset Delta,
   where Delta=(A-A) minus {0}.
2. An exact partition S,E_3,s-E_3 of an even group has residue sum
   N/2=(2^(n-2)+|E_3|)s=(N/2)s modulo N. Thus s is odd. This argument
   applies separately at every translated base.
3. For even N and no antipodes, if the parity class sizes are a,b,
   then |E_3|>=2ab. Every intersecting center pair uses a same-parity
   column pair. For a fixed oriented column difference delta, the
   equation 2(a-c)=delta has at most two solutions for the difference
   a-c, each with one ordered realization. Thus at most two unordered
   center pairs use each unordered column pair. Inclusion-exclusion
   gives n^2-n-2[binomial(a,2)+binomial(b,2)]=2ab.

For n=7, odd rounding gives 107. At even modulus, mixed parity permits
a base with even target because n is odd. Since binomial(7,2)=21,
one parity of E_3 has at least 11 points, so packing in that parity
requires N>=64+44=108. A single parity requires N>=128.

At 107, |E_3|=21 and Delta (size 42) is invariant under doubling.
The nonzero residues of the prime 107 form one doubling orbit of size
106, impossible. The elementary order test is 2^53=-1 modulo 107,
2^2!=1; the divisors of 106 are 1,2,53,106.

At 108, |E_3| is 21 or 22. Size 22 gives an exact partition and odd
target for every base, contradicting the mixed-parity base change.
Size 21 gives doubling closure. Parity sizes 1,6 are impossible by
the valid six-point class in modulus 54<60; sizes 3,4 are impossible
because 2ab=24. Sizes 2,5 give 20 odd and 22 even differences. Their
odd differences double to at least ten class-2-mod-4 differences.
Some odd difference is coprime to 3: otherwise all cross-parity
differences are divisible by 3, putting A into one coset of size 36,
where its 64 subset sums cannot fit. Such a difference has order 108.
After two doublings its further orbit has size 18 in 4G (order 27).
This follows from 2^9=-1 and 2^6=10 modulo 27. Those 18 even
differences are disjoint from the previous ten, contradicting 22.
Thus every valid seven-point set has N>=109.

For n=8, the quadratic bound gives 184. Antipodes need at least 218,
so assume none at 184,185,186. At 184, |E_3|=28 and the partition
forces odd target, hence parity sizes 1,7 or 3,5. The first supplies
a valid seven-point class in modulus 92<109; the second needs E_3>=30.
At 185, |E_3|=28 forces invariant Delta of size 56. Doubling has one
orbit of size four and five of size 36: ord_5(2)=4, ord_37(2)=36,
and lcm(4,36)=36. No sum 4v+36u, v in {0,1}, is 56.

At 186, size 29 again gives a partition, and the same odd-target
parity cases contradict modulus 93<109 or E_3>=30. Size 28 gives
doubling closure; parity energy leaves 1,7 or 2,6. The former is
excluded as before. Translate into the class of size six; then six
points are even, two odd, and s is even. Each parity of S has 64
points. Packing inside a parity class of size 93 leaves at most 14
points of E_3 of each parity, hence exactly 14 each. The odd portion
of T_3 has 16 points from 8*2 center-column representations, so these
representations are injective. Let u,v be the odd points and
delta=u-v. Delta_even is closed under doubling, which is bijective
on the even subgroup of order 93; it is therefore invariant. Thus
delta=2(a-c) for some a,c in A, and 2a+v=2c+u contradicts the odd
representation injectivity. This proves the elementary N>=187 bound.

No gap was found in these endpoint proofs. They do not exclude 187.

## 4. Quartic audit and experimental scope

For distinct equal-length vectors u,v giving the same residue,
c=u-v has sum zero. If every c_i>=-1, 1+c is an eight-term rival;
if every c_i<=1, 1-c is a rival. Thus c has both a positive entry
at least two and a negative entry at most minus two. This is a
necessary restriction, not a converse to validity.

In a fiber of ordinary expressions 2a+b+c with three distinct points,
the centers are distinct by pair-sum uniqueness. A center cannot be
a singleton in another expression, since its surplus after cancellation
would then be at most one at every coordinate on its side. With q
centers, all distinct singleton pairs lie on the remaining 8-q points,
so q<=binomial(8-q,2) and q<=4. The four-ordinary construction in the
previous report attains four; its base-19 coefficient proof checks.
The negative-three construction's polynomial factorization proof also
checks: P(-3)=k(3^8-1) makes P-k(x^8-1) divisible by x+3 over Z;
cyclic coefficients give c_i=3r_i+r_(i-1) and sum r_i=0. A negative
r_i forces a distinct positive predecessor of at least twice its
magnitude, contradicting zero total mass. The quotient by four and
the non-antipodal claim are valid. The eightfold fiber is in L_2,
not E_4; that distinction matters.

The 288 marked representations count 28 type-22 multisets twice.
Since each center has a unique tail pair, marked multiplicity is at
most eight. For the eight distinct translates X_a=2a+(A+A), Q and R
as defined in the previous report satisfy |E_4|=259-Q+R exactly.
The inequality Q-R<=199 is only an equivalent restatement of the
desired sufficient bound. No universal energy or global-loss bound
was established by that identity or the local fiber lemmas.

Code audits: `collision` enumerates all multisets, not ordered tuples.
The independent degree-eight DP uses ascending degree within each
value, correctly accounting for unbounded repetitions. Saturation at
two preserves the yes/no uniqueness test. `cube` correctly tests subset
injectivity. `affine_key` ranges over units only and all translated
bases, so it does not use invalid nonunit scaling. Some assertions
in `structure` assume the numeric bounds being tested; their successful
execution is therefore corroboration, not an independent proof.

Both original scripts were rerun unchanged: stage2's 28 cases/171
bases and 102 perturbations passed; obstruction's 640 draws, 15
distinct valid pairs, and 120 bases reproduced exactly. The prior
eight-point perturbation batch has only the binary survivor at 255.
The only sampled subthreshold batches (239 and 247) have zero valid
sets, so they provide no positive test of the conditional quartic
claim at a subthreshold valid set. None is an exhaustive search.

## 5. Scope of this audit

The essential lemmas, endpoint proof, exact counting identities, and
explicit constructions are independently reconstructed here. The
seven-point minimum 124 remains an external reported computation.
No new bound or novelty claim is made by this audit. New stage-3
arguments require their own independent checks before incorporation.

## 6. Independent check of the root near-equality template lemma

This lemma was supplied during the session and reconstructed independently.
Assume a valid non-antipodal eight-point set at N=187, write
Delta=(A-A) minus {0}, and let m_x be the multiplicities of 2a+b.
Set |E_3|=28+k and R_3=sum_(m_x>0) binomial(m_x-1,2).
An unordered center pair {2a,2c} intersects exactly when 2(a-c) belongs
to Delta, and it then intersects in one point. Because all 56 ordered
differences occur once, the number of missing center pairs is

    h=(1/2)*|{delta in Delta: 2delta not in Delta}|.

The exact incidence identity |T_3|=64-Q_3+R_3, with Q_3=28-h, gives
k=h+R_3. Packing gives 187>=128+2(28+k), hence k<=1.

Doubling orbits in Z/187Z minus {0} have lengths 10 (one order-11
orbit), 8 (two order-17 orbits), and 40 (four unit orbits). Negation
preserves each nonunit orbit: -1=2^5 modulo 11 and -1=2^4 modulo 17.
It exchanges unit orbits in pairs, since an exponent equal to 5
modulo 10 and 4 modulo 8 cannot exist. If h=0, Delta is invariant
under doubling. Its symmetric unit component is either empty or has
at least 80 points. Empty units leave at most 10+8+8=26 points,
contradicting |Delta|=56; nonempty units are also impossible. Thus
h=1, k=1, R_3=0. There are exactly two outgoing doubling boundaries.

On any doubling cycle, a nonempty proper chosen portion has as many
outgoing boundaries as intervals. On a negation-self nonunit cycle,
negation pairs the outgoing boundaries without fixed points, so a
partial selected portion consumes at least two boundaries. If that
occurred here, every unit cycle would be fully selected or empty.
Symmetry would again require either at least 80 unit points or none,
and neither can yield total 56. Therefore the two boundaries must
lie on exchanged unit cycles, one on each. Each chosen portion is
one interval, and the two intervals are negatives of one another.
Every nonunit orbit is fully selected or empty; no other full unit
orbit pair can be present.

Let a in {0,1} indicate the selected order-11 orbit, and b in {0,1,2}
count selected order-17 orbits. The two unit intervals have the same
length t, so 56=2t+10a+8b and t=28-5a-4b. Their terminal outgoing
differences are units. Unit scaling by the inverse of one terminal
difference is valid; translating its realized ordered pair makes
that pair 0,1 if desired. The normalized unit portion is exactly

    {+/-2^(-j): 0<=j<t} modulo 187.

The order-11 orbit has one choice, while the two order-17 orbits may
be selected in zero, one (two choices), or two ways. Together with
a=0 or 1 this gives eight normalized templates. The templates may
overcount equivalent sets, which is harmless for an exclusion; none
is omitted by the normalization. In particular one must not assume
an arbitrary difference is a unit, but this proof forces the selected
terminal difference to be a unit before scaling it.

This is a proved necessary structural restriction at 187, not yet an
exclusion of 187 and not a template theorem for the whole interval
187<=N<248. The remaining task is deciding whether any template can
be the complete difference set of an eight-point valid set.

## 7. Independent check of new quartic links

The collision-structure agent supplied the lemmas in this section.

### Antipodal pairs in the pair-sum set

For a valid non-antipodal eight-point set at even N, let P=A+A (36
distinct two-term multisets), t=N/2. Then P has at most seven
antipodal pairs, and its dilation {2p:p in P} has at least 29 values.

Classify a P antipodal pair by its two representing multisets:
squarefree-squarefree (SS), double-double (DD), or double-squarefree
(DS). There is at most one SS pair. Indeed, its two squarefree supports
must be disjoint, else cancellation produces an antipodal pair in A.
If two different SS pairs have signed relations r,r' with value t,
the nonzero zero-sum vectors r+r' and r-r' must each have coefficients
at least two and at most minus two. Therefore all four intersections
of their positive and negative two-element supports are nonempty.
Each support of r' takes one point from each support of r, uses the
same four points, and subtraction of the aligned relations gives
2(v-w)=0 for distinct points v,w. This contradicts absence of antipodes
in A. The vectors r+r',r-r' cannot vanish since that would mean the
same antipodal pair with the same or reversed orientation.

There is at most one DD pair, by unique differences at plus or minus
N/4. For DS, write 2a-b-c=t. The center a is distinct from b,c, each
center occurs in at most one such relation, and tail edges {b,c}
are distinct. Any two tail edges intersect: otherwise adding their
relations gives a nonzero zero-sum vector whose negative coefficients
are all at least minus one, forbidden by validity. Center coefficients
can only increase those negative coordinates; the resulting vector
cannot be zero, since two doubled centers cannot equal the squarefree
multiset of four distinct tail points. A pairwise-intersecting family
of simple edges is a star or a triangle. In a star its hub is never
a center, so there are at most seven DS pairs. A triangle has at most
three. If a DD pair exists, its two centers cannot also be DS centers,
so DS<=6 and DD+DS<=7.

Finally if an SS pair with supports U,V exists, comparison of any DS
relation with each orientation of its relation forces the DS tail
to intersect both U and V. This follows by applying the negative-entry
part of the cancellation restriction: the only possible coefficient
minus two occurs on the tail's intersection with the negatively
oriented SS pair. The comparison vector is nonzero because its DS
center has coefficient two. Thus all DS tails are cross edges of
K_(2,2). Their pairwise intersection permits at most two edges.
In this case SS+DS+DD<=1+2+1=4. The maximum over all cases is seven.
Doubling identifies exactly the antipodal pairs of P, proving 36-7=29.

The cap seven is sharp for the valid binary set modulo 256. Its six
DS antipodes are `(0,0)` against `(1,127)`, `(1,1)` against `(3,127)`,
`(3,3)` against `(7,127)`, `(7,7)` against `(15,127)`, `(15,15)` against
`(31,127)`, and `(31,31)` against `(63,127)`. The DD antipode is
`(63,63)` against `(127,127)`. There is no SS antipode. Each pair's
sums differ by 128. The previously audited binary carry proof establishes
validity here; this example invalidates any unrestricted cap of six.

### A fourfold ordinary quartic fiber forces triple overlap

Let four ordinary expressions 2c_i+d_i+e_i have a common value x.
Their four centers are distinct and occur in no singleton tail.
The four distinct tail pairs form four simple edges on the other
four points. Such a graph is either a four-cycle or a triangle with
one pendant edge. In the cycle case, adding equations for opposite
edges gives 2(c_i+c_j)=2(c_k+c_l). Pair-Sidon makes the difference
nonzero; hence this case requires even N and an SS antipodal pair
in P. In the triangle-pendant case the degree-three hub h belongs
to three tails. Subtracting h yields three equal ordinary triple
representations 2c_i+d_i=y=x-h. Therefore R_3>=1.

At odd N, the cycle case is impossible. Moreover the correspondence
from fourfold ordinary quartic fibers to these triple values is
injective, and each associated triple fiber has exactly three
representations. Here is a complete check, including pure triples.

The three centers c_1,c_2,c_3 and three singleton columns d_1,d_2,d_3
are distinct and disjoint, leaving only h,z. The quartic's fourth
center is z with tail {d_i,d_j}, i!=j:

    2z+d_i+d_j=y+h.

No extra triple center is one of c_1,c_2,c_3, because a fixed center
has a unique singleton column. An extra center h or z cannot use a
column d_l: it would give 2h=2c_l or 2z=2c_l. Nor can its column be
one of the other triple centers, by the cancellation restriction.
The remaining four cases are these:

- y=2z+h gives 2z+d_i+d_j=2z+2h, forbidden by pair-Sidon.
- y=2h+z gives z+d_i+d_j=3h, a squarefree-three versus repeated-three
  equality, forbidden by replacing that subset in the baseline.
- y=3z gives d_i+d_j=z+h, forbidden by pair-Sidon.
- y=3h, combined with 2c_i+d_i=y and 2c_j+d_j=y, gives
  2(z+h-c_i-c_j)=0. At odd N this is a forbidden pair-Sidon equality.

Thus the triple fiber is exactly the three ordinary expressions.
The last case is precisely where an unrestricted even-N version
would need repair: it can instead yield an SS antipodal pair in P.

For injectivity, the same triple value could lift at most at the two
leftover hubs h,z. Suppose both lifts exist, with respective fourth
tail pairs {d_i,d_j} and {d_k,d_l}. Adding their equations gives

    h+z+d_i+d_j+d_k+d_l=2y.

If the pairs agree, use 2y=2c_i+2c_j+d_i+d_j to obtain the forbidden
squarefree-four equality h+z+d_i+d_j=2c_i+2c_j. If they differ, they
share one of the three d's; label them {d_i,d_j},{d_i,d_k}. Then,
with s the full eight-point sum,

    s=c_1+c_2+c_3+2y-d_i=5c_i+c_j+c_k+d_i.

This is an eight-term rival, again forbidden. Hence only one lift
exists. Consequently at odd N the number of ordinary quartic fibers
of multiplicity four is at most the number of triple fibers of
multiplicity exactly three, and therefore at most R_3. This controls
the coexistence of separate quartic collisions, rather than merely
bounding a single fiber. It does not itself establish |E_4|>=60.

## 8. Independent audit of the exact hereditary extension search

The exact-search agent supplied `stage3_search.py`. Its mathematical
encoding reconstructs as follows. For an already valid p-point prefix
with sum s, an enlarged (p+1)-term rival uses q copies of the new
point x. For q=0 it requires x in H_(p+1)-s; for q>=2 it requires
(q-1)x in s-H_(p+1-q). The q=1 case is exactly the valid-prefix
baseline and hence cannot be a rival. These are necessary and
sufficient conditions; no rival multiplicity is omitted.

The code maintains H_0 through H_n as exact modular bitsets. Its
ascending-degree update H'_r=H_r union (x+H'_(r-1)) correctly permits
arbitrarily many copies of the newly added point up to the degree
cap. It solves each kx=y with every gcd(k,N) lift; the unit path's
byte-table dilation computes the same inverse image exactly. The
sorted extension recursion covers every valid prefix, and heredity
ensures invalid-prefix pruning loses no valid full set. Root branches
are recorded as completed only after recursive completion, so
continuation that repeats the incomplete branch and skips completed
branches is sound. The controlled initial=(0,1) runs stay within
the recursion's sorted-coordinate bounds.

At 187, a valid eight-point set must have a unit difference. Otherwise
translate one point to zero: all other points are multiples of 11 or
17. A point divisible by 11 but not 17 and a point divisible by 17
but not 11 have a unit difference. In their absence all points lie
in a single subgroup of order 11 or 17, impossible for 128 distinct
normalized subset sums. A forced unit difference may legitimately
be scaled to one; an arbitrary difference may not. The same proof
works below 256 with at most two distinct prime divisors, with the
subgroup order at most N/2<128. It does not prove the corresponding
normalization at moduli with three distinct prime divisors.

`stage3_triple_templates.py` was also statically audited. Its candidate
vertices are exactly the common neighbors of 0 and 1 in each symmetric
Delta graph. The bitset recursion enumerates every sorted clique
containing those two points. Sidon pruning requires every new forward
and reverse difference to be distinct from each other and from all
existing differences; thus it is exact. A completed empty output
excludes compatible eight-point difference sets in that template.
Its `largest_visited_clique` field is not a maximum-clique certificate,
since target-eight cardinality pruning can skip smaller cliques.
No unproved unit scaling is hidden in the enumeration.

This static audit establishes encoding correctness, not the outcome
of a still-running process. Final complete/timeout outcomes must be
read from the corresponding terminal result and current artifact.

## 9. Completed independent finite certificate at 187

`stage3_certificate_check.py` uses only standard-library imports and
imports none of the template generator, clique search, hereditary
search, or original validators. It reconstructs each Delta directly
from the formula in Section 6, with the order-11 subgroup represented
by the nonzero multiples of 17, and the two order-17 doubling orbits
represented by `11*2^j` and `33*2^j`, 0<=j<8. It checks exact agreement
with the saved template file and every supplied coloring certificate.

It then enumerates every six-subset of the common neighbors of 0,1,
without pruning or Sidon assumptions, checking all 15 pair differences.
An eight-point set containing 0,1 would require one such six-clique.

| a | mask | Vertices | Edges | Verified coloring colors | Six-subsets checked | Six-cliques |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 13 | 0 | 1 | 1716 | 0 |
| 0 | 1 | 11 | 6 | 2 | 462 | 0 |
| 0 | 2 | 11 | 0 | 1 | 462 | 0 |
| 0 | 3 | 13 | 12 | 3 | 1716 | 0 |
| 1 | 0 | 17 | 71 | 5 | 12376 | 0 |
| 1 | 1 | 17 | 42 | 4 | 12376 | 0 |
| 1 | 2 | 17 | 79 | - | 12376 | 0 |
| 1 | 3 | 15 | 44 | 4 | 5005 | 0 |

All 46,489 six-subsets were checked. The exceptional template has no
saved five-coloring certificate, but this chromatic failure is not
used as a clique claim: its 12,376 six-subsets were checked directly.
The other seven proper colorings were independently verified on
arithmetically reconstructed graphs. The output is saved in
`stage3_independent_certificate_result.json`. Together with Section 6
this is an independently checkable finite exclusion of N=187.

The current full hereditary-search outcomes were also inspected:

- N=187: COMPLETE, elapsed 44.219 seconds; valid-prefix counts at sizes
  2,...,8 are 1,178,14801,589958,3493404,1124,0; all 178 legal
  third-coordinate branches complete; no accepted eight-point set.
- N=188: COMPLETE, elapsed 68.828 seconds; counts are
  1,180,15153,616625,4127034,20542,0; all 180 legal third-coordinate
  branches complete; no accepted eight-point set.

Both full runs use initial (0,1), no branch restriction, and the
previously audited unit-difference normalization (187=11*17,
188=4*47). Their full searches were not independently rerun by this
checker. The distinction is that 187 additionally has the small
standalone finite certificate above, whereas the 188 result currently
rests on the completed exhaustive program with an audited encoding.

## 10. Full-parity aggregate quartic link

The root's strengthening of Section 7 checks. Let q_4 be the number
of quartic values with four ordinary representations. Let epsilon=1
if P=A+A contains an SS antipodal pair, otherwise zero. Then

    q_4 <= R_3 + epsilon.

For a four-cycle ordinary fiber, the two opposite-edge pairs of
centers form the unique SS antipodal pair in P. Hence every cycle
fiber has the same four centers, and the same complementary four
tail points. If p,q are those pair sums, p-q=t=N/2, adding opposite
quartic equations gives 2x=2p+sum(tails). The full target is
s=p+q+sum(tails)=2x-t. Two different cycle-fiber values would differ
by t, and would therefore be x,s-x. Both cannot lie in T_4, by
T_4 intersect (s-T_4) empty. Thus there is at most one cycle fiber,
and its existence requires epsilon=1.

For a triangle-pendant fiber, Section 7's case split excludes every
fourth ordinary triple representation. It also excludes pure triples
at the remaining fourth quartic center. Only the pure triple at the
hub can survive in even N. Thus the associated triple value has
exactly three ordinary representations, plus possibly that one pure
representation. Its ordinary core is uniquely defined. The two-lift
contradiction in Section 7 uses no oddness assumption, so distinct
triangle-pendant quartic fibers have distinct associated triple
values. Each such triple fiber contributes at least one to R_3.
Combining the cycle and triangle counts proves the displayed bound.

This statement does not assume that two repeated representations
cannot coincide. It links the total number of maximally overlapping
ordinary quartic fibers to cubic overlap, across the full parity range.

## 11. Valid even example showing the pure-hub exception

The root supplied A={0,1,33,1089,20034,37822,39934,39998} modulo 40000.
Use labels a=1,b=33,c=1089,d_a=39998,d_b=39934,d_c=37822,z=20034.
For a candidate write c_i=k_i-1, so c_i>=-1 and sum c_i=0. Define

    F_a=c_a-2c_(d_a)+c_z,
    F_b=c_b-2c_(d_b)+c_z,
    F_c=c_c-2c_(d_c),
    F=F_a+33F_b+1089F_c.

The weighted collision is F+20000c_z=0 modulo 40000. Since all
multiplicities are nonnegative and total eight, |F_i|<=16, giving
|F|<=16(1+33+1089)=17968<20000. Therefore F=0 and c_z is even.
Successive reduction modulo 33, using |F_i|<=16, gives F_i=0.
Write c_z=2k; its lower bound implies k>=0. Put
u=c_(d_a),v=c_(d_b),w=c_(d_c). The equations give
c_a=2u-2k,c_b=2v-2k,c_c=2w. Their lower bounds force u,v>=k,w>=0.
Now c_0=2k-3(u+v+w)>=-1. If k>=1 this is at most -4k, impossible.
Thus k=0, and nonnegative u,v,w with -3(u+v+w)>=-1 must all vanish.
Every coefficient is zero. This proves validity, not merely a test.

The displayed set has no antipodal pair. Direct enumeration of all
6435 eight-term multisets also found no rival. Its cubic zero fiber is
`(0;0),(1;39998),(33;39934),(1089;37822)`. Its four ordinary quartic
zero representations have centers/tails `(1;0,39998)`, `(33;0,39934)`,
`(1089;0,37822)`, and `(20034;39934,39998)`. The three ordinary cubic
representations coexist with pure `3*0`, exactly the even case that
must not be omitted from a proof of the aggregate link.

## 12. Independent audit of the targeted q_4 search at 247

The exact-search agent supplied `stage3_four_fiber_search.py`.
An ordinary fiber of size four at odd modulus cannot be a four-cycle.
Label its triangle-pendant tails as 0,2u,2v,2w, with hub 2v and
pendant leaf 2w. Writing the common value 2H gives the full set

    {0,2u,2v,2w,H-u,H-v,H-u-v,H-v-w}.

This parameterization loses no case: two is a unit at odd modulus,
and the only graph automorphism swaps the two nonhub triangle vertices.

At 247=13*19 some tail difference must be a unit. Otherwise translate
one tail to zero and use the two-prime argument: all four tails lie
in one mod-13 or mod-19 coset. Their four centers all have the same
residue r modulo that prime, since each is half the common value
minus two tail values. Selecting two of the four centers and any
subset of the other three tails yields 6*8=48 distinct subset sums
in the same prime coset, whose capacity is at most 19. This violates
the normalized subset-sum injectivity. The argument also covers r=0.

The six tail pairs have four orbits under the graph automorphism:
the two nonhub triangle vertices (difference 2u), triangle-hub edges
(2v or 2(v-u)), missing edges from nonhub vertices to the leaf
(2w or 2(w-u)), and the pendant edge (2(w-v)). Reorienting and unit
scaling therefore makes u=1,v=1,w=1, or w-v=1. These are precisely
the four normalization cases in the code.

The point coefficient sum is (4,0,-1,1), as in `BASELINE`. All 6434
indexed rivals are expanded exactly. The H coefficient is between
-4 and 4; every nonzero such coefficient is a unit at 247. Thus each
rival either forbids a tail linear equation independent of H, or
forbids exactly one affine H value. Deduplicating equations and
identifying a balanced equation with its negative does not change
its zero set. All modular roots in the tail pruning are included.
The substitutions for the four normalizations reconstruct exactly.

Point distinctness need not be an extra pruning hypothesis: if two
indexed points coincide, moving one baseline copy from one coordinate
to the other is one of the enumerated rivals. Hence no surviving
parameter quadruple can have repeated points. The final explicit
distinctness assertion and full eight-term checker provide additional
verification. The encoding and normalization have no gap for N=247.
Current-state inspection confirms `stage3_four_fiber_247.json` is complete,
with all 247 outer parameter rows completed in each of the four
normalizations, no accepted set, and elapsed time 9.25 seconds under
the 180-second cap. The four pair counts are respectively
5564,5557,5551,5462 balanced-passing cases (22134 total), and
55445,55452,55458,55547 rejected cases. Each passing case had every
one of its 247 H values excluded: the stored counts are exactly its
passing count times 247. This establishes q_x<=3 at N=247 with the
audited complete computational dependency. It does not independently
exclude valid sets at 247 or establish |E_4|>=60.

The optional fixed-form difference graph probe is not a replacement
for this arithmetic cover. Its `stage3_four_fiber_cover_247.json`
records 2423 forms, 665224 graph edges, a proper coloring with 174
colors, and a found clique of size 95. The coloring proves that a
single injective family certified by that edge rule has size at most
174<247, so that proposed shortcut cannot cover all H values. The
95 is only a found clique, not a proved maximum. Neither number is
the maximum number of distinct evaluated forms at a particular valid
tail parameter tuple; extra inequalities can create distinct values
not certified by this restricted edge rule.

## 13. Independent audit of full non-type22 fibers at odd subthreshold N

The collision-structure agent's classification checks after its correction
of the order-189 loop/path attachment case. Precisely, no valid eight-point
set at odd 187<=N<248 has a quartic fiber containing a non-type22 marking
at every one of the eight centers. This restriction concerns f_x, not
the full marked multiplicity r_x; type22 markings must not be silently
included. Its final finite center-completion checks are explicit
computational dependencies, independently reproduced below.

Assume such a fiber has value x and q ordinary representations. Each
center has at most one tail pair by pair-Sidon, so all eight centers
occur once. If an ordinary center a appeared in any other fiber
representation, comparison with 2a+b+c would have surplus at most one
on the ordinary side after cancellation, forbidden by validity. This
also covers another 31 or 4 representation; a shared doubled center
would already violate fixed-center tail uniqueness. Thus no ordinary
center appears in any other row's support. The remaining k=8-q
centers H have representations 3h+F(h)=x, with F:H->H; a loop is 4h=x.
The coefficient matrix has block form

    M = [2I_q  * ; 0  3I_k+F].

All rows sum to four. In the integral column basis consisting of
the all-ones vector followed by e_1,...,e_7, subtract row zero from
the other rows. The resulting matrix has first column (4,0,...,0),
so det M=4 det L, where L is the seven-by-seven row-difference matrix.
If B=(a_i-a_0)_(i=1..7), then LB=0 modulo N. The coordinates of B
generate Z/NZ: otherwise its 128 distinct subset sums lie in a proper
subgroup, of size at most N/2<=123. Multiplication by adj(L) shows
det(L) annihilates every B coordinate, hence annihilates their generated
group. Therefore N divides det(L)=det(M)/4. No unproved inverse of L
or stronger invariant-factor assertion is used.

The determinant of a functional graph with t tree vertices and cycle
lengths ell is

    det(M)=2^q * 3^t * product(3^ell-(-1)^ell).

This follows by removing tree vertices in triangular order and evaluating
each cycle block 3I+permutation. A two-cycle would give 2(h-h')=0,
forbidden; at odd N there is at most one loop because 4h=x has one
solution. The ordinary bound gives 0<=q<=4. Enumeration of cycle
partitions with total at most 8-q yields only these candidate rows:

| q | Cycles | Trees | det(M)/4 | Odd N in [187,247] dividing it |
|---:|---|---:|---:|---|
| 0 | 1 | 7 | 2187 | 243 |
| 0 | 3 | 5 | 1701 | 189,243 |
| 0 | 1,3 | 4 | 2268 | 189 |
| 0 | 8 | 0 | 1640 | 205 |
| 1 | 1 | 6 | 1458 | 243 |
| 1 | 3 | 4 | 1134 | 189 |
| 1 | 1,3 | 3 | 1512 | 189 |
| 2 | 1 | 5 | 972 | 243 |
| 2 | 3 | 3 | 756 | 189 |

`stage3_full_fiber_check.py` independently reconstructs this finite
arithmetic table without imports from earlier research modules.

Translate by -x/4, making the fiber value zero, so F(h)=-3h.
If F(h)=F(h') for distinct h,h', then 3(h-h')=0. Unique ordered
differences permit at most one unordered such pair globally, since
the kernel of multiplication by three has at most three elements.
In particular no vertex has indegree three. Any nonempty tree attaches
to a cycle at an indegree-two vertex, using the unique possible branch;
there can therefore be only one attached path and no internal branch.
Its length is at most v_3(N), because after that many iterations of
-3 the 3-primary component has vanished and the remaining component
is periodic. This eliminates all rows with too many tree vertices.

At 205 the sole remaining row is an eight-cycle with q=0. Summing all
eight equations 3h+F(h)=x, with F a permutation, gives 4s=8x and thus
s=2x. This contradicts T_4 intersect (s-T_4) empty.

At 243 the only periodic point of -3 is zero, so a three-cycle is
impossible. The only remaining row has q=2, one loop, and a path of
length five. Its leaf has order 243 and is a unit. Unit normalization
of that leaf to one makes

    H={0,1,9,81,216,240} modulo 243.

At 189=27*7, periodic points lie in the order-seven subgroup; the
nonzero points form three-cycles under -3. The q=1 row has both the
zero loop and such a three-cycle. Whether the path attaches to the
loop or the other cycle is irrelevant: the cycle contains a,2a,4a,
and together with zero repeats the difference a-0=2a-a, impossible.
It would be incorrect to assume the path always attaches to the
three-cycle, but this argument excludes both attachments. The remaining
q=2 row has one three-cycle and a path of length three. Its leaf has
order 27 in the 3-primary component and a nonzero order-seven component,
so it is a unit. Normalize it to one, yielding

    H={1,9,81,135,162,186} modulo 189.

The two ordinary centers must belong to
`{-(d+e)/2: d,e in H, d!=e}` minus H. These are nine possible centers
at 189 and ten at 243. The independent standalone checker enumerates
all 36 and 45 unordered two-center choices, respectively. It scans
all 6435 eight-term multisets for each, without relying on the older
validator. At 189 none of the 36 completions is Sidon or valid. At
243 five of the 45 are Sidon, but none has an injective normalized
subset cube and none is valid. All 81 have explicit stored rivals.
The complete result is `stage3_independent_full_fiber_result.json`:
231660+289575=521235 multisets scanned.

These finite checks close every remaining classified case, establishing
the stated odd-subthreshold non-type22 restriction with a small,
independently reproducible computational component. They do not exclude
all quartic marked fibers of size eight, since type22 rows are outside
this classification; nor do they by themselves imply |E_4|>=60.

## 14. Independently reproduced even full non-type22 exclusion

The determinant and functional-graph argument of Section 13 applies
at even modulus, with two changes. First, 4h=x can have four solutions,
but those solutions occur in antipodal pairs, so at most two belong to
a set with no antipodal pair. Second, translating every point by a changes
x by 4a. Thus x=0,...,gcd(4,N)-1 represents every translation class of
the common value. These are necessary restrictions, not a claim that
four is invertible. Two-cycles remain forbidden by the antipodal condition.

Enumerating cycle partitions for 0<=q<=4, at most two loops, no two-cycle,
and total 8-q vertices gives exactly the following even divisors of
det(M)/4 in [187,247]:

    192,196,200,208,210,216,224,234,240,244.

For each common-value representative define F(h)=x-3h. The unique
ordered-difference argument still permits at most one pair of vertices
with equal image. Therefore every admissible closed H is a union of
cycles, possibly with one unbranched path attached to one cycle. A
complete superset of these H is obtained by taking any union of short
cycles together with the full forward orbit of a possible leaf. Every
actual H occurs in this enumeration. Invalid extra configurations do
not affect exclusion completeness.

For each H, every ordinary center must solve 2c=x-d-e for two distinct
tails d,e in H. Both solutions modulo an even N must be included when
they exist. The independent implementation instead checks all c in
Z/NZ directly against this equation, avoiding any division ambiguity.
It chooses every q-element collection of centers outside H, then tests
unique ordered differences, the 128 normalized subset sums, and finally
all 6435 eight-term multisets. All filters are necessary for validity.

`stage3_even_full_fiber_check.py` reconstructs the arithmetic partitions,
closed sets, center choices, and validity checker without importing
the agent's search code. Its complete result is
`stage3_independent_even_full_fiber_result.json`, independently matching
the original counts:

| N | Closed H | Sidon H | Determinant Passing | Completions | Sidon A | Cube Passing | Valid |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 192 | 420 | 0 | 0 | 0 | 0 | 0 | 0 |
| 196 | 435 | 40 | 0 | 0 | 0 | 0 | 0 |
| 200 | 222 | 8 | 0 | 0 | 0 | 0 | 0 |
| 208 | 212 | 0 | 0 | 0 | 0 | 0 | 0 |
| 210 | 674 | 60 | 0 | 0 | 0 | 0 | 0 |
| 216 | 990 | 264 | 216 | 106992 | 6336 | 507 | 0 |
| 224 | 588 | 40 | 40 | 13904 | 0 | 0 | 0 |
| 234 | 528 | 0 | 0 | 0 | 0 | 0 | 0 |
| 240 | 3652 | 840 | 768 | 64320 | 4864 | 0 | 0 |
| 244 | 723 | 432 | 432 | 65520 | 7200 | 0 | 0 |

The 90-second capped checker completed in 6.641 seconds. In total it
considered 250736 completions, of which 18400 were Sidon and 507 had
injective subset cubes; all 507 failed full validity. This is a complete
targeted configuration exclusion, not a search over all sets or moduli.
Together with Section 13 it establishes, with the stated finite
computational dependencies, f_x<=7 for every non-type22 quartic fiber
of a valid no-antipodal eight-point set in 187<=N<248. It does not
establish r_x<=7, since a type22 multiset contributes two markings.

## 15. Counterexample to an unrestricted exterior marked-fiber cap

The root agent supplied the odd-modulus example

    N=5833, A={0,243,351,363,365,369,405,729}.

It is valid and has no antipodal pair. Its exterior quartic value 1458
has eight markings:

    (0;729,729), (243;243,729), (351;351,405),
    (363;363,369), (365;363,365), (369;351,369),
    (405;243,405), (729;0,0).

The first and last mark the same type22 multiset. The other six are
type31. Thus r_1458=8 but f_1458=6. Every low subset sum is at most
729+405=1134<1458, so this value lies in E_4 by the exterior identity.
This defeats a universal exterior cap seven, including at odd modulus,
but does not refute the subthreshold non-type22 restriction.

Here is a complete independent validity proof. Order the points by
q_i=(-3)^i for i=0,...,6 and q_7=-729, putting a_i=(q_i+729)/2.
Because N=8*729+1, equality of eight-term sums modulo N is equality
of their integer sums: every such sum lies in [0,5832]. Let a rival
have c_i=k_i-1>=-1 and sum c_i=0. Integer equality is
sum c_i*q_i=0. Set

    P(X)=sum_(i=0..5) c_i*X^i + (c_6-c_7)*X^6.

Then P(-3)=0. Monic integer division gives P=(X+3)R with integral
R=sum_(i=0..5) r_i*X^i. With r_-1=0, coefficient comparison yields
c_i=3r_i+r_(i-1) for i=0,...,5 and c_6-c_7=r_5. Summing gives

    4*sum r_i + 2c_7=0.

Hence c_7 is even. Since c_7>=-1, it is nonnegative, and sum r_i<=0.
If any r_i=-m<0, c_i>=-1 forces its preceding coefficient to be
r_(i-1)>=3m-1>=2m>0. The case i=0 cannot occur. Distinct negative
coefficients have distinct positive predecessors, so the total positive
mass is at least twice the total negative mass. Consequently sum r_i>0
whenever any negative coefficient exists, a contradiction. If none is
negative, sum r_i<=0 forces every r_i=0. The sum identity then gives
c_7=0, and all c_i vanish. This proves uniqueness.

Independent direct enumeration of all 6435 eight-term multisets found
only the baseline at target sum 2825 and independently reconstructed
exactly the eight displayed markings. No novelty assertion is made.

## 16. Odd mixed marked-eight fibers cannot have four ordinary markings

Assume odd N and a valid no-antipodal set with a quartic fiber marked
at all eight centers and with a type22 multiset 2u+2v. At odd modulus
there is at most one such multiset, since multiplication by two is
injective and pair sums are Sidon. There is no type4 representation:
4a=2u+2v would imply 2a=u+v, forbidden by pair-Sidon.

Suppose four markings are ordinary. Their centers C cannot appear in
any other representation, by the ordinary-center cancellation lemma.
The other four vertices D are their tails, and the tail graph is a
triangle with a pendant edge; the four-cycle is excluded at odd N.
Its hub h belongs to three edges and gives a common cubic value
y=x-h with three representations 2c_i+d_i, where the three d_i are
exactly D minus h. The type22 core u,v lies in D, since neither can
be an ordinary center.

The full-marked hypothesis gives h a marking. If it is type31,
3h+d=x, then d cannot be in C. If d=h the marking is the already
excluded type4; otherwise d is one of the d_i. Subtracting h from
the two quartic equalities gives 2h+d_i=2c_i+d_i, hence h=c_i at
odd modulus, impossible. Therefore h is a type22 center, so h is
one of u,v. But every pair in D containing the hub is an edge of
the triangle-pendant graph. If u,v is that edge, its ordinary marking
2c+u+v=2u+2v again gives 2c=u+v, violating pair-Sidon. This contradiction
proves q_x<=3 in this mixed full-marked case. It does not yet exclude
the case itself.
