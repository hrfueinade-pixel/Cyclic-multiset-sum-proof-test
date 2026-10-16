# Stage 3: coexistence of heavy four-term fibers

## Scope and status

This note studies valid eight-element sets A in Z/NZ without an antipodal
pair. It preserves the earlier reports and does not claim literature
novelty. The elementary lemmas below use validity and cyclic-group
structure, not the paper's seven-element computational certification.
They do not prove N >= 248 or |E4| >= 60.

Three changes are substantive:

1. P=A+A has at most seven antipodal pairs, with a sharp example.
2. Fourfold ordinary quartic fibers are globally controlled by cubic
   multiway overlap: their number is at most R3+epsilon, defined below.
3. A full fiber of eight non-type-22 quartic multisets is impossible at
   odd 187 <= N < 248 by an elementary finite classification. An additional
   exact, bounded configuration enumeration excludes the corresponding
   even cases, but its status is explicitly computational.

The third restriction concerns NON-type-22 multisets, not all marked
representations. It must not be confused with a marked multiplicity cap
seven: a type-22 multiset has two markings.

## 1. Elementary prerequisites

For any two distinct equal-length multiplicity vectors u,v with equal
sum, u-v has an entry >=2 and an entry <=-2. Otherwise one of
1+u-v or 1+v-u is a nonnegative, size-eight competitor for the all-ones
multiset. This applies after cancellation.

A squarefree sum cannot equal a different multiset of the same length
at most eight: replacing that squarefree part in the baseline gives a
competitor. In particular, every nonzero ordered difference of A is
unique unless it is the involution. With no antipodal pair, all 56
nonzero ordered differences are distinct and all 36 unordered pair sums
P=A+A, including doubles, are distinct.

For completeness, if a-b=c-d, then a+d=c+b. If one side is squarefree,
validity forces equal multisets, giving the same ordered difference.
Otherwise a=d,c=b and 2a=2b, yielding an antipodal pair.

T4={2a+b+c} and s-T4 are disjoint, where s=sum A: their intersection
would concatenate two repeated four-term multisets to a forbidden
eight-term competitor. Translating A changes T4 by four times the
translation, so this statement is independent of choosing a base.

For any base a, subset sums of A-a with zero omitted are injective and
number 128. This follows by replacing the larger of two equal subsets
in the all-ones multiset by the smaller and padding with zeros. Therefore
when N<248, the differences of A generate all of Z/NZ: otherwise its
translated subset-sum cube would lie in a proper subgroup of size at
most N/2 <=123.

## 2. Antipodal pairs in the pair-sum set

**Theorem.** P=A+A has at most seven unordered antipodal pairs. There
is at most one squarefree--squarefree pair. If such a pair exists, P has
at most four antipodal pairs in total. Consequently |2P| >=29.

Proof. Write t=N/2; the theorem is vacuous when N is odd. Pair sums in P
have unique two-multiset representations. Classify their antipodal pairs
as squarefree--squarefree (SS), double--squarefree (DS), or double--double
(DD).

An SS relation has the form u+v-w-z=t on four distinct points; sharing a
point would give an antipodal pair in A. Suppose two different SS pairs
had signed vectors r,r'. Both r+r' and r-r' are nonzero zero-sum
relations. The cancellation restriction forces each of the four
intersections between their positive and negative support pairs to be
nonempty. Thus r' uses the same four points, with each of its pairs
crossing the partition {u,v}|{w,z}. After orienting r', subtracting the
relations gives 2(v-w)=0 or 2(v-z)=0, forbidden by the absence of
antipodes in A. Hence SS <=1.

A DD pair satisfies 2a-2d=t, so a-d=+/-N/4. Unique ordered differences
give DD <=1.

A DS pair has 2a-b-c=t, with a,b,c distinct. Each double 2a participates
in at most one such pair, and its tail edge {b,c} is unique. Two DS tail
edges must intersect: if they were disjoint, adding their equations
would give a nonzero zero-sum vector with every negative coefficient
at least -1. Center occurrences among the tails only improve this
inequality. This contradicts validity.

A family of distinct pairwise-intersecting edges is a star or a triangle.
For a star its hub cannot be a DS center, because each center is disjoint
from its own tail. Therefore a star has at most seven edges; a triangle
has at most three. If DD exists, its two doubled points cannot be DS
centers, so DS <=6 and DD+DS <=7.

If an SS relation u+v-w-z=t exists, compare a DS signed relation with
both signs of this SS relation. To have a negative coefficient <=-2 in
both resulting zero-sum relations, the DS tail must meet both {u,v}
and {w,z}. Thus DS tails are cross edges of K2,2. A pairwise-intersecting
cross-edge family has at most two edges. Hence in this case
SS+DS+DD <=1+2+1=4. This proves both bounds. Dilation identifies exactly
the antipodal pairs of P, so |2P|=36-(number of these pairs)>=29. QED.

The bound seven is sharp. For the valid binary set
A={0,1,3,7,15,31,63,127} at N=256, the DS pairs are
2a versus next(a)+127 for a=0,1,3,7,15,31, and the DD pair is
2*63 versus 2*127. There are exactly seven. Thus a cap six is false.
Validity at N=256 has the carry proof in eight_element_obstruction.md
and is independently checked here by all 6435 eight-term multisets.

## 3. Ordinary quartic fibers propagate to cubic fibers

Call 2a+b+c ordinary when a,b,c are distinct, with {b,c} unordered.
Let F4 be the number of residues having four ordinary representations.
Let m_y count marked cubic representations 2a+b=y, and put

    R3 = sum over y with m_y>0 of binomial(m_y-1,2).

Let epsilon=1 if P has an SS antipodal pair, and zero otherwise.

**Theorem.** F4 <=R3+epsilon. For odd N, F4 <=R3. Each odd-N
fourfold ordinary quartic fiber is attached injectively to a cubic
fiber consisting of exactly three ordinary representations.

Proof. A fixed ordinary center has a unique tail, by pair-sum uniqueness.
Furthermore, an ordinary center cannot occur in ANY other multiset
representation of the same quartic value: canceling it would leave all
positive coefficients of its ordinary vector at most one. Thus the
centers in a fiber are distinct and all tail edges lie outside them.
For q ordinary representations, their q distinct tail edges lie on
8-q vertices, so q<=binomial(8-q,2), and q<=4.

For q=4 there are four tail edges on four vertices. Their graph is
either a four-cycle or a triangle with one pendant edge.

In the four-cycle case, adding the equations for opposite tail edges
gives 2(c1+c3)=2(c2+c4) for four distinct centers. Their squarefree pair
sums are different, so they are antipodal in P; N is even. The SS pair
is unique by Section 2, so every cycle fiber has the same four centers,
with the same antipodal partition. If D is the sum of the four tail
vertices and U is one of the two center-pair sums, every such quartic
value x satisfies 2x=2U+D. Thus there are at most two candidate values,
differing by t. The full target is s=2x+t, so the two values are x and
s-x. Complementary disjointness of T4 forbids both. Hence cycle fibers
number at most epsilon.

In the triangle-pendant case, cancel its degree-three hub h from the
three incident tail edges. This produces a cubic value y=x-h with
three ordinary representations

    y=2c_i+d_i, i=1,2,3,

where the three centers and three singletons are disjoint triples.
Let h,z be the two remaining points. The fourth quartic center is z,
and its tail is a pair {d_i,d_j}. Thus

    2z+d_i+d_j=y+h.                                      (1)

Any further cubic representation at y must have center h or z and
singleton h or z. A reused singleton d_i would imply a reused doubled
center. An ordinary center c_i cannot be a singleton in another cubic
representation, by cancellation. The possibilities are:

- y=2z+h forces d_i+d_j=2h in (1), contrary to pair uniqueness;
- y=2h+z forces z+d_i+d_j=3h, a squarefree triple collision;
- y=3z forces d_i+d_j=z+h, contrary to pair uniqueness;
- y=3h implies 2(z+h-c_i-c_j)=0.

The last case is impossible at odd N. At even N it may occur and gives
an SS antipodal pair; it is the only possible extra representation.
In either parity, the three ordinary cubic representations form a
unique core; the cubic fiber has multiplicity three or four.

It remains to prove that one core cannot support two different
triangle-pendant fibers. The two possible hubs are h,z. If both occur,
their fourth representations have tails {d_i,d_j} and {d_k,d_l}, and
adding their equations gives

    h+z+d_i+d_j+d_k+d_l=2y.

If the pairs agree, comparing the two corresponding cubic equations
gives h+z+d_i+d_j=2c_i+2c_j, a forbidden squarefree-four collision.
If they differ, they share exactly one singleton, say d_i. Then

    h+z+2d_i+d_j+d_k=2y,
    s=c1+c2+c3+d1+d2+d3+h+z
     =c1+c2+c3+2y-d_i=5c_i+c_j+c_k+d_i.

The right side is an eight-term multiset distinct from the baseline,
contradicting validity. Thus each cubic core supports at most one
triangle-pendant fiber. A multiplicity-three or multiplicity-four
cubic fiber contributes at least one to R3. Combining this injection
with the cycle-fiber bound proves the theorem. QED.

**Failed even extension.** It is false that the associated cubic fiber
must always have multiplicity exactly three. The valid set

    A={0,1,33,1089,20034,37822,39934,39998}, N=40000

has cubic value zero with 2*1+39998, 2*33+39934, 2*1089+37822,
and pure 3*0. Its quartic value zero has four ordinary representations.
It has one SS pair in P: 1+33 versus 0+20034. At bases 37822,39934,39998,
this quartic value becomes exterior, at 8712,264,8 respectively; it is
low at the other five bases. Full enumeration confirms validity and
the E4 cardinality is 191. Root's separate report gives a self-contained
validity proof for this construction; this note does not use it as an
unproved universal lemma.

## 4. Eight non-type-22 multisets in one fiber

Let f_x count the distinct quartic multisets of types 4,31,211 at value x.
Because each has one repeated center and a fixed center has a unique
tail, f_x<=8. A type-22 multiset is deliberately excluded from f_x.

**Theorem.** For odd 187<=N<248, f_x<=7 for every x.

Proof setup. Suppose f_x=8. Every point of A is a repeated center.
Let C be the q ordinary centers, with 0<=q<=4, and H the other k=8-q
points. Ordinary centers are absent from all other representations,
as proved in Section 3. Consequently the coefficient matrix of these
eight four-term representations has the block form

    M=[2I_q, *; 0, 3I_k+F],

where F has one 1 per row and represents the function
h |-> x-3h from H to H. A pure 4h representation is a loop of F.
Two-cycles would give an antipodal pair in A. At odd N there is at
most one loop, since 4h=x has a unique solution.

Let the directed cycles have lengths ell_1,...,ell_r and let t be the
number of noncycle vertices. Then

    det M = 2^q 3^t product_j (3^ell_j-(-1)^ell_j).

Indeed tree vertices contribute factors 3, and a directed cycle gives
the indicated determinant of 3I plus its permutation matrix.

Subtract the first row from all other rows and add the other columns
to the first. The determinant is 4 det L, where L is the seven-by-seven
row-difference matrix on translated coordinates b_i=a_i-a_0. We have
L b=0 modulo N. The differences generate the whole group by Section 1;
the adjugate identity therefore gives N|det L=det M/4.

Here the possible cycle lengths are 1,3,4,5,6,7,8, with at most one
length-one cycle and total length at most 8-q. Their cycle factors are
4,28,80,244,728,2188,6560 respectively. Factoring these small integers
and allowing the tree factor 3^t shows that the only odd divisors in
[187,247] are 189,205,243. The complete surviving determinant rows are:

| q | Cycle lengths | t | det M/4 | Remaining odd N |
|---:|---|---:|---:|---|
|0|1|7|2187|243|
|0|3|5|1701|189,243|
|0|1,3|4|2268|189|
|0|8|0|1640|205|
|1|1|6|1458|243|
|1|3|4|1134|189|
|1|1,3|3|1512|189|
|2|1|5|972|243|
|2|3|3|756|189|

No other rows survive. This finite arithmetic is reproduced by
full_fiber_determinants() in the companion script; it is not a search
over arbitrary residue sets.

If two points of H have the same F image, their difference has order
three. Unique ordered differences permit at most one such unordered
pair in the whole A. Thus F has at most one indegree-two vertex, no
indegree-three vertex, and its noncycle part is a single path feeding
a cycle. Translate by x/4, which is legal for odd N; F becomes -3h.
On the 3-primary component its path depth is at most v_3(N).

For N=205, F is a permutation and the table has q=0. Summing the
eight equations gives 4s=8x, hence s=2x. Since x belongs to T4, this
contradicts complementary disjointness.

For N=189 the path has at most three vertices. All rows except
q=1, cycles 1+3, t=3 and q=2, cycle 3, t=3 are eliminated. A 3-cycle
of -3 lies in the order-seven subgroup and has form {a,2a,4a}.
The q=1 case also contains its zero loop, immediately giving the
repeated difference a-0=2a-a.

In the q=2 case the deepest path leaf has nonzero 3-primary and
7-primary components, so it is a unit. Unit scaling is therefore
justified, rather than assumed. Normalize that leaf to 1. Then

    H={1,9,81,135,162,186} modulo 189.

Every ordinary center equals -(d+e)/2 for distinct d,e in H and lies
outside H. The complete possible-center list is
{13,15,117,121,123,144,148,150,184}. Individual difference uniqueness
removes the following five, with explicit witnesses:

| Center | Equal nonzero differences modulo 189 |
|---:|---|
|13|1-186=13-9|
|117|9-162=117-81|
|123|9-135=186-123|
|144|9-135=144-81|
|150|9-162=186-150|

The remaining centers are {15,121,148,184}. Every pair fails:

| Centers | Equal nonzero differences modulo 189 |
|---|---|
|15,121|1-15=121-135|
|15,148|1-15=148-162|
|15,184|1-15=184-9|
|121,148|121-135=148-162|
|121,184|9-135=184-121|
|148,184|9-162=184-148|

For N=243, -3 has only its zero cycle and path depth at most five.
The table therefore leaves only q=2, cycle 1, t=5. Its deepest leaf
is a unit; normalize it to 1. Then

    H={0,1,9,81,216,240} modulo 243.

The complete potential-center list is
{13,15,117,121,123,135,198,202,204,238}. Individually, four fail:

| Center | Equal nonzero differences modulo 243 |
|---:|---|
|13|1-240=13-9|
|117|9-216=117-81|
|135|0-81=135-216|
|204|9-216=240-204|

The remaining six centers are {15,121,123,198,202,238}; all fifteen
pairs are excluded by this complete table. Subset sums in its last
column are squarefree and different, so violate dissociation.

| Centers | Repeated difference or equal subset sums modulo 243 |
|---|---|
|15,121|15+81+121=1+216|
|15,123|15-123=216-81|
|15,198|15-216=240-198|
|15,202|1-15=202-216|
|15,238|1-15=238-9|
|121,123|0-121=123-1|
|121,198|9=81+198+216|
|121,202|0-81=121-202|
|121,238|9+81=1+121+216+238|
|123,198|81-123=198-240|
|123,202|1-123=202-81|
|123,238|1+9+81=123+216+238|
|198,202|1-202=240-198|
|198,238|9=81+198+216|
|202,238|9-216=238-202|

These exhaust all three exceptional odd moduli, proving the theorem.
QED. The independent checker reconstructed the determinant argument
and all 81 canonical q=2 completions in stage3_full_fiber_check.py.

## 5. Even full-fiber configuration exclusion: computational status

At even N, at most two loops of F can belong to H: three of the four
solutions of 4h=x would contain an antipodal pair. The same determinant
argument leaves only ten even moduli in [187,247]:

    192,196,200,208,210,216,224,234,240,244.

The companion script enumerates this derived exception list, not all
eight-element sets or all moduli. For each N, translating A changes x
by 4a, so x in {0,...,gcd(4,N)-1} represents every value class; no unit
scaling assumption is made. H is a union of short cycles of the actual
affine map F(h)=x-3h and at most one incoming path. These closed sets
are generated directly. Only sets H with unique ordered differences
and the correct determinant divisibility are completed.

Every ordinary center is chosen from ALL solutions of
2c=x-d-e with distinct d,e in H. For even N both half-solutions are
included. All q-subsets of these candidate centers are tested. Every
complete candidate is checked for unique differences, its normalized
128-element subset-sum cube, and, if it survives, all 6435 size-eight
multisets. This encoding is complete within the full f_x=8 scope.

The fixed 30-second cap did not fire. Total runtime was approximately
2.6 seconds on this host. Outcomes:

| N | Closed H sets | Sidon H | Determinant-passing H | A completions | Sidon A | Cube-passing A | Valid A |
|---:|---:|---:|---:|---:|---:|---:|---:|
|192|420|0|0|0|0|0|0|
|196|435|40|0|0|0|0|0|
|200|222|8|0|0|0|0|0|
|208|212|0|0|0|0|0|0|
|210|674|60|0|0|0|0|0|
|216|990|264|216|106992|6336|507|0|
|224|588|40|40|13904|0|0|0|
|234|528|0|0|0|0|0|0|
|240|3652|840|768|64320|4864|0|0|
|244|723|432|432|65520|7200|0|0|

The independent reconstruction is now complete. The standalone
stage3_even_full_fiber_check.py uses a different closed-set construction,
direct membership testing of the half-equation, direct subset enumeration,
and complete multiset enumeration. It reproduces every count above;
the parent reran it at final consolidation. Thus f_x<=7 throughout the
even gap has this explicit finite computational dependency. This is not
an elementary proof of all ten exclusions and not a certificate excluding
all valid sets throughout the gap. See audit-notes Section 14 and
stage3_independent_even_full_fiber_result.json.

## 6. Other bounded experiments and their limitations

Run `python stage3_collision_experiments.py`. It imports only
research_experiments.py for collision and subset-cube verification.
Reference examples also check the P antipodal theorem and quartic-to-
cubic coexistence theorem. Counts are invariant under translated base
changes, and bases are not counted as new structural examples.

The relation-template batch fixes

    A={0,2,2q,2r,h-1,h-q,h-1-q,h-r},
    q=2,...,8; r=q+1,...,20; h=0,...,N-1.

This directly forces four ordinary quartic representations, when the
eight residues are distinct. Fixing the first tail parameter to 1 is
a restriction, NOT a complete symmetry reduction. A 20-second cap per
modulus did not fire.

| N | Parameter tuples | Distinct size-eight sets | Sidon | Cube-passing | Valid |
|---:|---:|---:|---:|---:|---:|
|239|25095|21893|2981|34|0|
|247|25935|22677|3189|45|0|
|255|26775|23461|3397|58|0|

These limited tests are not full exclusions even of all fourfold
ordinary fibers. The separate exact-search agent has stronger complete
configuration exclusions at selected moduli; those do not follow from
this batch. No random candidates were generated in this stage.

## Remaining obstacle and next step

The global inequality F4<=R3+epsilon excludes coexistence of many
fourfold ordinary values when cubic overlap credit is small. The full
non-type-22 fiber classification also shows that small modulus prevents
one maximally heavy pattern seen at N=1640. Neither controls all
ordinary double/triple fibers, type-22 markings, or mixtures of 31 and
211 representations well enough to prove |T4|>=89.

The most useful next lemma is a charging inequality for total quartic
collision loss using the cubic defect together with the now-classified
exceptional pair-sum antipodes. It must accommodate mixed fibers and
disjoint-tail collisions; a bound on F4 alone cannot do that. The binary
set at N=255 has F4=0 but already substantial quartic overlap, so excluding
fourfold fibers does not by itself establish the sufficient bound.

Checkpoint: all runs above finished, no process remains live. Preserve
the exact-three even counterexample, the q=1 branching-attachment
correction, and the distinction between f_x and marked multiplicity.
The independent audit of the even closed-set enumerator is complete.
The next concrete action is to classify disjoint-tail ordinary double/triple fibers
that are not charged by the cubic propagation theorem.
