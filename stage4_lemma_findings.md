# Stage 4: the quartic growth lemma

## Status

The target remains UNPROVED:

    |T4| >= 2|T3| + 17,
    equivalently |E4| >= 2|E3| + 4,

for valid non-antipodal eight-element cyclic sets with 187 <= N < 248.
There is no counterexample to that statement here. The results below
are elementary proofs of restrictions on its collision mechanism and
a rigorously valid counterexample to two proposed local counting shortcuts.
No novelty claim is made. No Lean, random sampling, or modulus sweep was used.

## 1. Definitions and elementary prerequisites

Write A={a_0,...,a_7}, and use equality modulo N throughout. A is valid
when its all-ones multiset is the only size-eight multiset with sum sum A.
Assume no antipodal pair. Let Delta be the 56 nonzero ordered differences.

A squarefree multiset U cannot equal a different multiset V of the same
degree <=8: replace U by V in the all-ones multiset. More generally, for
two distinct equal-degree equal-sum vectors u,v, u-v must have both an
entry >=2 and an entry <=-2. Otherwise 1+u-v or 1+v-u is a rival.

All ordered differences are unique: a-b=c-d gives a+d=c+b. If either
pair is squarefree, validity identifies the pairs and hence the ordered
differences. If both are doubles, 2a=2b gives an antipodal pair. This
also proves uniqueness of all 36 two-term multiset sums.

After translating 0 into A, let S be the subset sums of A without 0.
Equal subsets give a rival by replacing the larger subset with the
smaller and filling with zeros, so |S|=128. The same replacement argument
shows that a subset of r nonzero points has no different representation
of length <=r+1, apart from padding that subset with at most one zero.
It follows that T3 intersects S in A, and T4 intersects S in L2, where

    T3={2a+b}, T4={2a+b+c}, |L2|=1+7+21=29.

Indeed T3 contains A and T4 contains L2 using repeated zeros; any subset
of at least two points in T3, or at least three in T4, would violate
the replacement restriction. Thus |E3|=|T3|-8 and |E4|=|T4|-29.

Two repeated quartic multisets cannot sum to sum A: their concatenation
would be a rival. Hence T4 and (sum A)-T4 are disjoint. Since
S=(sum A)-S, this proves the packing N>=128+2|E4|.

For cubic fibers let m_y be the number of marked representations 2a+b=y.
Define

    h = (1/2)|{delta in Delta : 2delta not in Delta}|,
    R3 = sum_y binomial(m_y-1,2),
    d = 64-|T3|.

A pair of equal cubics with different centers corresponds exactly to a
center difference delta whose double is in Delta. Difference uniqueness
gives exactly one pair for each such unordered center pair. Therefore

    sum_y binomial(m_y,2) = 28-h,
    d = 28-h-R3, and |T3| = 36+h+R3.                 (1)

The second equality uses binomial(m,2)-(m-1)=binomial(m-1,2).
In particular |E3|>=28, so the target implies |E4|>=60 and N>=248.
None of these arguments uses the paper's n=7 computational certification.

## 2. Cubic propagation and full support separation

Use the 260 DISTINCT repeated degree-four multisets as vertices:
8 of type 4, 56 of type 31, 28 of type 22, and 168 of type 211.
Join vertices when their equality comes from adding one point of A to
an equality of repeated degree-three multisets. Call this the propagation
graph. Its edges stay within quartic sum fibers. Let K be its number of
components, and D=K-|T4| the number of further identifications required.
This is equivalent to the 288-marking implementation after identifying
the two markings of each type-22 multiset.

**Proposition 1.** In any quartic fiber, different propagation components
have disjoint FULL supports, including their repeated centers.

Proof. Suppose distinct equal-sum quartic multisets share a point a.
Delete one a from both. The resulting distinct degree-three multisets
are equal in sum. Neither can be squarefree, by the replacement argument.
Thus their equality is a repeated cubic equality, and adding a back is
a propagation edge. Conversely every propagation edge shares its added
point. The propagation graph is therefore exactly the support-overlap
graph within each quartic fiber. If two component support unions met,
some vertices from the two components would share a point and be joined.
This proves the proposition. QED.

**Proposition 2.** A quartic fiber with four ordinary representations
2a+b+c, where a,b,c are distinct, contributes zero to D.

Proof. An ordinary repeated center a cannot occur in any other distinct
representation: deleting it would leave the squarefree triple a+b+c.
Thus the four centers are distinct and none occurs in another tail.
Their four distinct tail edges lie on the other four points. A simple
graph with four edges on at most four vertices is connected and uses
all four vertices: a disconnected such graph has at most three edges.
Adjacent tail edges share a point, so Proposition 1 joins all four
representations into one component. That component uses all eight
points. Any additional representation shares a point with it and hence
belongs to the same component. The fiber has one component and D_x=0.
QED. In particular, the previously bounded fourfold ordinary fibers
are not themselves a source of fresh collision loss.

## 3. A restricted center-pair counting lemma

**Proposition 3.** Fix distinct centers a,d and put delta=a-d. If
2delta belongs to Delta, there is at most one quartic value at which
ordinary representations centered at a and d lie in different
propagation components. Such a collision determines six distinct points
in three ordered pairs with differences delta, 2delta, 4delta.

Proof. Write the two ordinary representations as

    2a+b+c = 2d+e+f.

Their full supports are disjoint by Proposition 1. Difference uniqueness
determines unique u,v with v-u=2delta, so 2a+u=2d+v. Subtracting gives

    b+c+v = e+f+u.

If v were outside {b,c}, the left triple would be squarefree and would
force equality of the multisets. Since b,c are absent from {e,f}, a
single occurrence of u cannot supply both of them; equality is impossible.
Thus v belongs to {b,c}. Similarly u belongs to {e,f}. Write the tails
as {v,b'} and {u,e'}. Then

    2(v-u)=e'-b'=4delta.

All of a,d,v,u,e',b' are distinct by full support separation and
ordinariness. The unique ordered difference representations of 2delta
and 4delta determine both tails, hence determine the quartic value.
This proves both assertions. QED.

This is NOT a bound for all center pairs, or for mixed 31/211 fibers.
The following example shows why missing doubled differences must be
handled by a global argument rather than a unit local charge.

## 4. Three fresh collisions for one center pair

Take

    N=78337,
    A={0,4609,4610,4626,4898,9248,9522,9792}.

There are three equalities with the same repeated centers 4609,4610:

    2*4609+4626+4898 = 2*4610+0+9522    = 18742,
    2*4609+4626+9522 = 2*4610+4898+9248 = 23366,
    2*4609+4898+9522 = 2*4610+4626+9792 = 23638.

These are three fresh, independent identifications in the propagation
graph, not merely three markings of one multiset. They disprove both
universal local charges of at most one and at most two per center pair.
They do NOT refute the target growth lemma or its sub-248 version.

### Complete validity proof

Before translation by 4609, label the points

    d=0, a=1, x=17, y=17^2, z=17^3,
    w=x+y-z-2=-4609,
    p=x-y+z-2=4639,
    q=-x+y+z-2=5183.

For a rival write c_i=k_i-1, k_i>=0, sum k_i=8. Translation does not
change equality of size-eight sums. In the translated model all sums
lie between 0 and 8*9792=N-1, so equality modulo N is integer equality.
That equality has the base-17 form

    F0+17Fx+17^2 Fy+17^3 Fz=0,
    F0=c_a-2(c_w+c_p+c_q),
    Fx=c_x+c_w+c_p-c_q,
    Fy=c_y+c_w-c_p+c_q,
    Fz=c_z-c_w+c_p+c_q.

From sum k_i=8, F0 is in [-11,13] and Fx,Fy,Fz are in [-10,6].
Every absolute value is <17. Successive reduction modulo 17 therefore
forces each F to be zero. Put u=c_w,v=c_p,t=c_q and U=u+v+t. Then

    c_a=2U, c_d=-2U,
    c_x=-U+2t, c_y=-U+2v, c_z=-U+2u.

The two even coefficients c_a,c_d are both >=-1, so U=0. Then
c_x=2t,c_y=2v,c_z=2u>=-1 imply u,v,t>=0, and their zero sum forces
u=v=t=0. Every c_i is zero. This proves validity. N is odd, so there
is no antipodal pair. QED.

### Why the three identifications are fresh

For a difference c of two degree-three multisets there is again no wrap:
each translated sum is in [0,3*9792], below N. The same digit equations
apply: |F0|<=9 and |Fx|,|Fy|,|Fz|<=6. Thus the displayed formulas for c
again hold. Its positive mass is at most three.

If |U|>=2, |c_a|+|c_d|=4|U| and the other six coefficients have total
absolute value at least 2|U| (their two triples sum to -U and U).
The positive mass is therefore at least 3|U|>3. If |U|=1, each of
c_x,c_y,c_z is odd, so the other six coefficients have absolute mass
at least 3+1=4; the total positive mass is at least four. Consequently
every cubic relation has U=0 and hence c_a=c_d=0.

It follows that no repeated cubic containing a or d can equal another
distinct cubic: a cubic relation cannot change its multiplicity of that
point, and canceling the shared point would give a pair-sum collision.
Each of the six ordinary quartic representations displayed above is
therefore isolated in the propagation graph. Deleting a tail point
would leave a repeated cubic containing its center; deleting its center
would leave a squarefree cubic. Neither admits a different equal cubic.
The two vertices at each of the three distinct values are isolated and
their merger contributes one independently to D. QED.

The only cubic equalities in this model form the triple
2x+q=2y+p=2z+w: with U=0 the positive mass is
3(|u|+|v|+|t|)/2, so nonzero cubic relations have (u,v,t) a permutation
of (1,-1,0). Hence |T3|=62 and R3=1, also without enumeration.
In particular 2(a-d) is missing from Delta: its presence would give a
cubic equality with different repeated centers a,d, which was excluded.
The direct quartic count |T4|=241, K=244, D=3 is separately checked
computationally; the counterexample proof does not require that count.

## 5. Exact global budget and remaining proof obligation

Let I be the kernel of the homogeneous map from C[X_0,...,X_7] to
C[Z/NZ][t] sending X_i to t*g^(a_i). Validity excludes every collision
involving a squarefree degree-three or degree-four monomial. Thus

    dim I_3=d, dim I_4=260-|T4|,
    dim (span_i X_i I_3)=260-K.

For the last identity, multiplying cubic binomials by variables gives
exactly propagation edges; edge differences span a space of dimension
number of vertices minus number of components. Therefore

    D = dim (I_4 / span_i X_i I_3).                 (2)

This identifies the fresh loss with the number of degree-four minimal
generators, since I_1=I_2=0. It does not bound that number.

Define the nonnegative shadow credit

    Sigma = 8d-(260-K).

Nonnegativity follows because the eight products of each of d basis
vectors span the propagated space. Equations (1) and (2) give exactly

    |T4|-2|T3| = 132-6d+Sigma-D.

The SINGLE unresolved global counting lemma that would finish this
route is therefore

    Sigma-D >= 53-6h-6R3                          (3)

under validity, no antipodes, and 187<=N<248. This is an equivalent
collision-budget formulation of the growth target, not a theorem or
a numerical estimate proved here. Propositions 1-3 restrict its terms
but do not yet sum to (3).

One stronger, potentially workable split is

    D<=h, and K>=2|T3|+h+17.                       (4)

BOTH inequalities in (4) remain unproved. The first cannot follow by
charging one new collision to its own missing-doubling center pair:
Section 4 uses that same pair three times. The second cannot be assumed
as a generic shadow-growth fact. The elementary estimate
K>=260-8d=36+8h+8R3 proves the second only when 5h+6R3>=53.
Thus, even after proving D<=h, a sharper shadow estimate is still needed
for the small-defect cases 5h+6R3<=52.

The ordinary internal-pair bound leaves mixed fibers, repeated tails,
and missing-doubling pairs untreated. A successful argument must couple
their aggregate contribution to shadow credit or to small cyclic modulus.
Maximal ordinary fibers, local support size, and passing tests do not
provide that coupling. Minimal-rank Waring decomposition classifications
do not supply it either: no hypothesis here forces a minimal decomposition.

## 6. Bounded experiments and corrections

Run, with standard-library Python 3 in this directory:

    python stage4_lemma_experiments.py
    python stage4_independent_check.py

The first script imports stage3_growth_probe.py for eight existing
nonbinary fixtures and stage3_search.py for direct_valid_count; the
latter imports research_experiments.py. No new random draws occur.
The independent checker imports NO project verification functions.
It enumerates unmarked multisets and reconstructs propagation components
as connected components of support-overlap graphs, rather than using
the original marked union-find implementation.

The fixed batch has 129 candidate records, four exact duplicate (A,N)
pairs, and 125 distinct pairs. All 125 are valid, each checked through
all 6435 eight-term multisets: 804375 checks total. It consists of 13
prior non-antipodal fixtures, three prior root models, two CRT models,
the two- and three-collision constructions, one four-binary-pairs model,
and 108 mixed-radix rotation representatives for alphabets {2,3}, {2,4},
{3,4}. The 125 pairs have 45 distinct recorded collision signatures
(T3,T4,K,h,R3,maximum local rank), NOT 45 proved affine classes.

The 30-second cap did not fire; the batch took about 0.72 seconds.
All tested examples satisfy the growth target and both proposed bounds
in (4). Six pairs lie outside the naive-shadow range. Only the explicit
four-binary-pairs model exercises Proposition 3 nonvacuously, with two
internal ordinary collision pairs. Its counts are T3=61,T4=234,K=236,D=2.
The separate seven-fixture checker reproduced every expected count and
checked 45045 eight-term multisets, within its 10-second cap.

These are deliberately constructed or previously accepted examples;
the valid fraction has no statistical meaning. The smallest modulus
tested is 255. There are NO valid examples in the conditional range
N<248, and the batch is NOT a search of all valid sets. Passing it does
not establish either (3), (4), or the conditional target.

**Correction to stage 3.** For A={0,2,8,26,80,242,728,2186}, all-three
radix at N=6560 has T3=64,T4=232,K=260,D=28, not D=21. D=21 belongs
to the SAME residue list at mixed terminal radix two, N=4373, where
T4=239. Both counts were independently reconstructed here. The old
report and checkpoint have been repaired without altering their proofs.

## Dependencies and delivery

All propositions and validity proofs in this note are elementary and
independent of published computational results. Existing stage-3 exact
endpoint exclusions, and the antipodal case conditional on the paper's
reported n=7 minimum 124, are not used in these proofs. See
stage3_findings.md for that separate dependency boundary.

A limited primary-source check of the relevant algebraic reformulation
found no applicable bound on the degree-four generator budget. The
minimal-rank scope of https://arxiv.org/abs/1201.2922 does not justify
(4); general binomial-ideal theory at
https://arxiv.org/abs/alg-geom/9401001 was not used to assert such a bound.
This is not an exhaustive literature audit or a claim of novelty.

The workspace is not a Git repository (verified again with git
rev-parse), so no configured GitHub repository or PR is available.
Nothing has been published externally. All verification runs finished.
