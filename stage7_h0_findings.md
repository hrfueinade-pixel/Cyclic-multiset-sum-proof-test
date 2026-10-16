# Stage 7: counting fresh triple-single collisions

Follow-up: stage8_regular_bridge_findings.md proves D=0 in the ENTIRE
odd h=R3=0 branch, using the 31/31 result below as a dependency. The
odd R3>0 branch and full goal remain open. This report is preserved as
the earlier stage, not the latest boundary of proved results.

The goal h=0 => D=0 for all valid non-antipodal eight-point cyclic sets
is STILL OPEN. Stage 6 settled the even difference-subgroup branch.
This stage proves a collision-type bound in the remaining odd branch:

    D_(31/31) <= 2R3.

Here D_(31/31) counts the fresh loss of fibers having type-31 quartics
in different propagation components. Thus this collision type vanishes
at R3=0. Other contributions to D are NOT bounded by this statement.
No novelty claim is made; there is no Lean or modulus sweep.

## 1. Audited prerequisites

Translate A into its difference-generated cyclic subgroup H. Validity
prohibits a different equal-length representation of any squarefree sum
of degree <=8. A nonzero zero-sum relation of total coefficient sum zero
must have both a coefficient >=2 and one <=-2; otherwise 1+c or 1-c
is a rival. No antipodes then implies unique pair sums and all 56 ordered
nonzero differences. In odd H, h=0 means 2Delta=Delta.

Different quartic propagation components at a common value have disjoint
ENTIRE supports. An ordinary quartic 2p+q+b has its repeated center p
absent from every other distinct representation of that value: deleting
p would otherwise equate its squarefree triple to a different triple.

Every pure cubic 3a is paired in the odd h=0 case. Indeed, for base a the
seven label pairs {a,r} correspond via 2d+a=2e+r to a spanning tree of
center edges. A cycle would yield a forbidden relation with distinct
signed labels and only one possible coefficient outside {-1,0,1}.
No edge enters a, since that would give 2d=a+r. Connectivity therefore
forces an edge leaving a, hence a different representation of 3a.

If R3=0 all cubic fibers have size at most two. Doubling permutes
differences, so each label b participates in exactly seven paired marks.
Precisely ONE of the eight marks 2a+b is unpaired. This uniqueness, not
an assumed absence of repeated-representation collisions, is used below.

## 2. Two local lemmas

**Lemma 1.** If 3a+b=3c+d, the pairs {a,b},{c,d} are disjoint with
a!=b,c!=d, and 2(a-c) is in Delta, then a-c has order five.

Proof. Write 2(a-c)=e-f. Then a+b+e=c+d+f. These are different triples,
since the fixed support pairs are disjoint, and neither can be squarefree.
Thus e is a or b and f is c or d. The choices (a,c),(a,d),(b,c) imply
respectively a=c, 2c=a+d, or 2a=b+c, all impossible. The last choice
(b,d) gives 2(a-c)=b-d=-3(a-c), hence order five. QED.

The four nonzero differences of the unique order-five subgroup are now
exhausted by {a,c} and {b,d}. These pairs occupy different cosets; four
points in one order-five coset would repeat differences. No other A
points can share such a coset. The coset-size pattern is 2,2,1,1,1,1.
Under h=0 there are at most TWO disjoint type-31 collision pairs globally:

    3a+b=3c+d,   3b+c=3d+a.

Their center pairs must be the two existing order-five pairs, with the
other pair as singletons. The alternative singleton assignments are
unequal since the nonzero center difference has order five.

**Lemma 2.** A disjoint-support equality 2a+2b=3c+d, with a!=b,c!=d,
is impossible if both 2(a-c) and 2(b-c) belong to Delta.

Proof. Write 2(a-c)=u-v. Then 2b+u=c+d+v. The right side cannot be
squarefree, so v is c or d. If v=c, 2a=c+u is a forbidden pair-sum
equality. Thus v=d, and u=2a-2c+d. Similarly write 2(b-c)=w-d,
where w=2b-2c+d. Adding gives u+w+c=3d. This triple is squarefree:
u=w would give 2a=2b; u=c would give 2b=2d; w=c would give 2a=2d.
No antipodes excludes these cases. Since c!=d it is a different
representation of 3d, contradicting validity. QED.

Both lemmas hold in any cyclic group under their stated conditions.
In h=0 the difference conditions hold automatically. At odd modulus,
4/4,4/22, and 22/22 disjoint equalities are also impossible by doubling
injectivity and pair-sum uniqueness. Other collision types remain.

## 3. Four-point components and the R3=0 proof

Assume H odd and h=0. Suppose 3a+b and 3c+d lie in different components
U,V at value x. Let W be the four other points. A partner 2p+q of 3a,
coned by b, belongs to U. It cannot use c or d, which would join V,
or a, by fixed-center uniqueness and pair-sum uniqueness.

If p=b, its coned vertex is type 31 centered at b, and Lemma 1 against
3c+d would force b,c into one order-five coset. If q=b, the vertex is
type 22, excluded by Lemma 2. If p=q, Lemma 1 would put p in c's coset,
whose only A points are a,c. All are impossible. Thus p,q are distinct
points of W. Similarly a partner 2t+u of 3c uses two distinct W points.
Disjoint supports force all four distinct. Hence

    support(U)={a,b,p,q}, support(V)={c,d,t,u},
    3a=2p+q, 3c=2t+u.

The components exhaust A, so no third component can have this value.
Each such fresh fiber contributes exactly ONE to D.

Now 2a+b must be unpaired. Otherwise cone its partner by a. The new
vertex is in U and cannot contain the ordinary center p. Its center
and singleton thus lie in {a,b,q}, with center different from a.
A type-22 result is excluded by Lemma 2 against 3c+d. A type-31 result
is excluded by Lemma 1, since its center b or q is outside c's coset.
An ordinary result centered at b would contain a center occurring in
3a+b; one centered at q would contain a center occurring in 2p+q+b.
Both violate the ordinary-center restriction. No pure quartic is
possible since the coned point a would have to be its center. Therefore
there is no partner for 2a+b.

Assume R3=0. Since only one mark with singleton b is unpaired, 2p+b
MUST be paired. Cone its partner by q. The new vertex cannot contain p,
and its remaining points lie in {a,b,q}. Ordinary results centered at a
or b are excluded by 3a+b. A type-22 result is excluded by Lemma 2.
A type-31 result centered at b or q is excluded by Lemma 1; one centered
at a would be 3a+q=x=3a+b, forcing q=b. The ONLY remaining case is 4q,
from the cubic equality 2p+b=3q. Thus 4q=x belongs to U.

The mirrored argument gives 4u=x in V. Multiplication by four is
injective in odd H, so q=u, contradicting disjoint supports. No fresh
31/31 collision is possible at R3=0. QED.

This repairs a tempting shortcut: it is WRONG to assert that 2p+b
must be unpaired too. It may equal 3q. The correct proof retains this
pure-quartic case and compares both components.

Since at most two such fibers exist, each contributes one, and none
exists at R3=0, their total satisfies D_(31/31)<=2R3. The stronger
D_(31/31)<=R3 has NOT been proved. Other losses in D remain uncontrolled.

## 4. A counterexample to local closure alone

This valid example is NOT h=0 and does NOT refute the objective:

    N=262445,
    A=(0,209956,52490,209957,209965,52570,210685,59050).

It has h=26,R3=0,D=2. Its two fresh fibers are

    3*209956+209957 = 3*0+52490 = 52490 mod N,
    3*209957+0 = 3*52490+209956 = 104981 mod N.

All four vertices are isolated in the cubic-propagation graph. Their
center differences have order five, with their whole doubling/negation
orbit inside Delta. Thus even this stronger LOCAL closure does not
give connectivity. Global h=0 is essential to Section 3.

Validity has a complete construction proof. In Z/5 x Z/Q, Q=52489,
the points are c=(0,0),a=(1,0),d=(0,1),b=(2,1), plus
(0,9),(0,81),(0,729),(0,6561). Every eight-term second-coordinate sum
is <=8*6561<Q, so equality with the all-ones target is integer equality.
Base-nine digits cannot carry, since coefficients are <=8. Each high
point occurs once, b,d together occur twice, and a,c together occur
twice. Writing r=#a,s=#b, the first-coordinate condition is
r+2s=3 mod 5 with 0<=r,s<=2. Its sole solution is r=s=1.

The four relevant cubic deletions cannot use a high point and have
unique representations in the low four-point block, proving isolation.
For exact D=2 bookkeeping, classify repeated low-block quartics by
k=#b+#d:

|k|Vertices|Fibers|Components|
|---:|---:|---:|---:|
|0|5|5|5|
|1|8|5|6|
|2|8|4|4|
|3|8|5|6|
|4|5|5|5|

At k=2 the squarefree quartic is excluded; all other paired vertices
share a point. At k=1,3 only the displayed pairs are disjoint. Any
fiber involving a high point shares that high point, since its base-nine
multiplicities are fixed, so it is connected. The direct independent
check finds T3=62,T4=242,K=244 after all 6435 validity checks.

## 5. Additional reductions

### Reflection alternative

A valid eight-point set in odd H cannot satisfy 2A=-A+t.
First |H|>=184: its translated subset cube has 128 points; 64 repeated
cubic marks have at most 28 pairwise center intersections, so T3>=36.
Since T3 intersects the cube in A, E3>=28. The sets S,E3,s-E3 are
disjoint; two repeated triples summing to s, padded with two zeros,
would be an eight-term rival. Hence |H|>=128+56=184.

If phi(a)=t-2a permutes A, translate 0 into A, so t=phi(0) is in H.
For a cycle of length k, q_k=(1-(-2)^k)/3 satisfies q_k(3a-t)=0.
A single eight-cycle, started at zero, generates H by t with 85t=0,
giving |H|<=85. Otherwise the cycle-length partition of eight has
parts <=7. The subgroup generated by 3a-t contains 3H and has order
dividing L=lcm(|q_k|). The values for k=1..7 are 1,1,3,5,11,21,43.
A 7 leaves a 1; a 6 leaves at most a 2; a 5 leaves at most a 3,
giving L<=33; largest part 4 gives L<=15; smaller parts give L<=3.
Thus always L<=43, |H|<=3L<=129, contradicting 184. QED.

Consequently if A and 2A are congruent, the only valid alternative is
positive affine doubling stability, already the binary order-255 case
with D=0. An unresolved odd instance must have genuinely NONCONGRUENT
homometric A and 2A, not merely a reflected doubling orbit.

### Prime powers

The audited tree bound gives 128<=|H|<=2187; Stage 6 excluded prime
order. For |H|=p^e,e>=2, generation of H forces a unit difference.
Its joint doubling/negation orbit must fit in Delta, of size 56.
Necessarily p<=43. For the smallest power p^e>=128 with e>=2:

|p|p^e|Joint orbit size|
|---:|---:|---:|
|3|243|162|
|5|625|500|
|7|343|294|
|11|1331|1210|
|13|169|156|
|17|289|136|
|19|361|342|
|23|529|506|
|29|841|812|
|31|961|310|
|37|1369|1332|
|41|1681|820|
|43|1849|602|

All exceed 56; larger powers cannot have smaller orbits than their
reductions. These are exact fixed-integer certificates, not sampled
configurations. The checker iterates each orbit and verifies the
lifted order formula: if k=ord_p(2), it checks 2^k!=1 mod p^2;
binomial expansion gives v_p((2^k)^(p^j)-1)=1+j, hence lifted order
k*p^(e-1). Its even-order halfway power is -1, since an odd prime
power has only two square roots of one. If k is odd, adjoining -1
doubles the orbit. Thus odd prime-power H is impossible.

## 6. Experiments, dependencies, and remaining lemma

Two fixed order-five probes used the previously audited hereditary
search, with 15-second caps each. No modulus sweep was performed.

|N|Orbit-mask candidates|Normalized masks completed|Visited valid prefixes, sizes 6/7/8|Valid 8-sets|
|---:|---:|---:|---|---:|
|315|450|210|0/0/0|0|
|585|965|382|0/0/0|0|

Both completed, in about 6.33 and 7.86 seconds. Unit-free candidates
retain translation only; no unit-difference assumption is used in these
three-prime-factor groups. These exclude h=0 sets at just TWO orders,
not all valid sets there or the remaining orders. Prefix counts are
counts visited after pruning, not a census. No accepted examples means
no additional valid-set structural diversity from these probes.

The project-import-free collision checker independently enumerates
all 6435 multisets for six fixed VALID fixtures, including the order-five
construction, binary 255/256, the even 254 family, and previous multi-loss
examples. Binary 255 has eight disjoint 211/31 vertex pairs and twelve
disjoint 211/211 pairs, all connected by propagation. Disjoint vertices
must not be conflated with different components. A separate arithmetic
checker verifies 13 prime-power certificates, 21 multi-cycle partitions,
and three INVALID negative-doubling controls with explicit rivals.

Reproduce with standard-library Python 3:

    python stage7_collision_mechanisms.py
    python stage7_arithmetic_checks.py
    python stage7_torsion_probe.py

Counts, arithmetic certificates, deadlines and scope are in the JSON
outputs. Computations test bookkeeping; the collision proofs do not
depend on passing experiments. No claim uses the paper's n<=7
computational certification. The tree bound and even classification
are explicitly proved dependencies in stages 5 and 6.

The main unresolved lemma is still the GLOBAL cubic bridge:

    In an odd h=0 instance, a quartic fiber cannot have two
    disjoint-support propagation components.

An unresolved instance now has odd subgroup order 184..2187 with
at least two distinct prime factors, and noncongruent homometric A,2A.
The surviving disjoint type pairs include 4/31,4/211,22/211,31/211,
211/211, and the controlled 31/31 case when R3>0. In particular ordinary
type-211 collisions and the full R3>0 branch remain open. Even D=0
would leave the separate Sigma>=53 budget at h=R3=0 for the 248 bound.

The primary paper [The beltway problem over orthogonal groups](https://arxiv.org/abs/2402.03787)
discusses failure of uniqueness for collision-free binary supports;
[the cyclic five-point classification](https://www.sciencedirect.com/science/article/abs/pii/S0012365X26004243)
distinguishes cyclic homometry from real-line reconstruction. Neither
provides the needed eight-point validity-sensitive bridge. No novelty
assertion or exhaustive literature claim is made.

The goal remains active. No PR is possible: this workspace has no Git
repository or configured GitHub remote.
