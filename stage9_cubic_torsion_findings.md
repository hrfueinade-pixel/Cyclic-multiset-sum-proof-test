# Stage 9: no order-three difference in the odd h=0 branch

Research date: 2026-10-10. The full goal h=0 => D=0 remains OPEN.
Follow-up: stage10_fourway_findings.md gives a computer-assisted
four-way exclusion with independent modular audits. The latest resume
point is stage11_threeway_findings.md; three-way fibers remain open.
Stage 8 proved the regular odd branch h=R3=0. This stage addresses an
actual obstruction in the remaining multiway-cubic branch, without
assuming R3=0 and without searching sets across moduli.

## 1. Precisely proved results

**Theorem 9.1.** If A is a valid eight-element set with odd
difference-generated subgroup H and h=0, then Delta contains NO
element of order three.

**Corollary 9.2.** Every cubic fiber has at most four representations
2a+b, and at most one is a pure cubic 3a. A fiber of size m>=3 has
either disjoint center and singleton sets (using 2m points), or one
common point which is its own pure center (using 2m-1 points).

Thus the remaining multiway shapes are exactly the following necessary
support possibilities, not an assertion that any h=0 realization exists:

|Fiber size|Pure representations|Core support|Other A-points|
|---:|---:|---:|---:|
|3|0|6|2|
|3|1|5|3|
|4|0|8|0|
|4|1|7|1|

The proof of Theorem 9.1 is algebraic. Small exact checks verify its
arithmetic, but are NOT its logical basis. There is no n<=7 computational
dependency, Lean use, modulus sweep, or claim of literature novelty.

## 2. Basic facts, valid also when R3>0

Translate A into H. Odd order makes doubling invertible. Validity
forbids a different equal-length multiset representation of every
squarefree subset sum of degree <=8: pad a replacement by its complement.
In particular all pair sums and all 56 ordered nonzero differences
are unique. The condition h=0 is exactly 2Delta=Delta.

We use |H|>=184, independently of the seven-point computation in the
paper. Here is its counting proof. The 64 cubic marks have pair-incidence
count 28: each pair of centers collides once because its doubled
difference lies in Delta. For a fiber of size m,

    m-binomial(m,2)+binomial(m-1,2)=1.

Hence |T3|=36+R3. Translate 0 into A; the 128 subset sums S of
A\{0} are distinct, s-S=S, and validity gives T3 intersect S=A.
Thus E3=T3\A has size 28+R3. The sets S,E3,s-E3 are disjoint:
two exterior cubics summing to s would, padded by two zeros, be a
rival eight-term multiset. Therefore |H|>=184+2R3>=184. These are
the audited elementary packing identities in stages 3 and 8, not a
consequence of passing tests.

Suppose for contradiction that an ordered difference has order three.
Translate its pair to 0,t, with t of order three. Write J=<t>.
The differences t,-t are already exhausted by this pair, so the six
remaining A-points occupy six distinct nonzero J-cosets. There is no
third point in the coset J. Write M=|H|/3, and C for these six points
in H/J, a cyclic group of order M.

C has no opposite pair. Otherwise four distinct ordered differences,
from each opposite outside point to the two base points, would project
to the same quotient difference. Its three lifts cannot accommodate
four distinct differences. This contradicts difference uniqueness.

## 3. Complete doubled-spoke classification

Fix an outside point c. Write the unique doubled differences as

    2c=p-q,     2(c-t)=r-s.

Since 3t=0, their difference is -t, giving

    p+s+t=q+r+0.                                      (1)

If the multisets in (1) differ, neither triple can be squarefree.
The left repetition is p=s, p=t, or s=t; the right repetition is
q=r, q=0, or r=0. This gives the following COMPLETE nine-case table:

| |q=r|q=0|r=0|
|---|---|---|---|
|p=s|4c in J|p=2c, forbidden pair|N2|
|p=t|N1|2c=t|q-s=-t, another J-pair|
|s=t|r=2c-t, forbidden pair|p-r=t, another J-pair|2(c-t)=-t|

The entries involving a multiple of c in J would put c in J, since
2 and 4 are invertible. The pair entries respectively give 2c=0+p
or 2c=t+r. Another J-pair must be the original 0,t pair, again
putting c in J. Thus only N1,N2 survive.

If the multisets in (1) are identical, p or s must be 0. Matching
the other two points gives either P or N0 below; the other matching
would again put c in J. The resulting four possibilities are

|Type|Outside points|Images of 2c and 2(c-t)|
|---|---|---|
|P|x=2c+t|(x,t), (x,0)|
|N0|x=-2c|(0,x), (t,x)|
|N1|x=-2c+t, y=2x+t|(t,x), (x,y)|
|N2|x=-2c+2t, y=2x+t|(x,y), (0,x)|

Each ordered pair (u,v) in the last column means the difference u-v.
All displayed outside points are in A, by construction. This derivation
uses squarefree replacements, not any restriction on cubic fiber size.

Since C contains no opposite pair, the signed doubling map sends each
q in C to a unique point F(q) in C with

    F(q)=+2q or -2q.

It is injective (otherwise two C-points are equal or opposite), hence
a permutation of its six points. A positive transition lifts precisely
to x=2c+t. A negative transition lifts to x=-2c+j*t, j=0,1,2.
The nonzero j cases N1,N2 FORCE the next transition to be positive,
because y=2x+t is in A and C contains no opposite pair.

## 4. Only five subgroup orders can occur

On a cycle of F of length k and sign product epsilon, iterating the
lift equations yields

    (1-epsilon*2^k)c in J,
    3(1-epsilon*2^k)c=0.

All points of that cycle are generated by c,t. Thus |H| divides

    3*lcm_i |1-epsilon_i*2^(k_i)|,    sum_i k_i=6.       (2)

This is an exponent argument in a cyclic group, not a determinant or
an assumed unit difference. The eleven partitions give the following
elementary finite arithmetic table:

|Cycle lengths|Maximum in (2)|Values in (2) at least 184|
|---|---:|---|
|6|195|189,195|
|5+1|279|279|
|4+2|255|255|
|4+1+1|153|none|
|3+3|189|189|
|3+2+1|315|315|
|3+1+1+1|63|none|
|2+2+2|45|none|
|2+2+1+1|45|none|
|2+1+1+1+1|45|none|
|1+1+1+1+1+1|9|none|

Since every bound is odd and at most 315, each proper divisor is at
most 105. Combining (2) with |H|>=184 therefore forces

    |H| in {189,195,255,279,315}.

For U=C union (-C), its twelve points form a signed-doubling invariant
set generating the quotient group of order M. Listing element-order
orbits gives the following COMPLETE possibilities, up to unit scaling:

|M|Possible generating U|
|---:|---|
|63|one twelve-point unit orbit, or the order-nine and order-seven orbits|
|65|one twelve-point unit orbit|
|85|an eight-point order-seventeen orbit and the four order-five points|
|93|a ten-point order-thirty-one orbit and the two order-three points|
|105|the six order-seven, four order-five, and two order-three points|

For completeness, the signed orbit sizes by element order are

    M=63: 3->2, 7->6, 9->6, 21->12, 63->12;
    M=65: 5->4, 13->12, 65->12;
    M=85: 5->4, 17->8, 85->16;
    M=93: 3->2, 31->10, 93->20;
    M=105: 3->2,5->4,7->6,15->8,21->12,35->24,105->24.

These sizes follow by iterating 2 and including negation. They imply
the displayed twelve-point possibilities by generation and cardinality.
Different unit orbits of one order are equivalent by a unit scaling;
mixed coprime-order components can be normalized independently by CRT.

For M=93 or 105, C contains a point q of order three. Its F-cycle
has length one and negative sign. N1,N2 cannot occur, since they would
force the next sign to be positive. Hence its lift satisfies c=-2c,
giving c in J and q=0, contradiction. Orders 279,315 are excluded.

## 5. The autocorrelation square and cyclotomic sign rigidity

Use the rational group algebra of the quotient cyclic group. Put

    f=sum_(c in C) X^c,     u=f+f^-,     v=f-f^-,
    P=2+f,

where minus superscript replaces c by -c. The coefficients of PP^-
are exactly the projected ordered-difference counts of A, including
diagonals. Since 2Delta=Delta and doubling is bijective in H,
PP^- is doubling-invariant. The twelve-point support u is also
doubling-invariant. Expanding gives

    PP^- =4+2u+(u^2-v^2)/4.

Consequently v^2 is doubling-invariant.

Evaluate at any primitive d-th root zeta, d dividing M, and let
sigma send zeta to zeta^2. Then for w=v(zeta),

    sigma(w)^2=w^2,

so sigma(w)=epsilon*w, epsilon in {+1,-1}, whenever w!=0. The sign
is a rational constant: sigma^r(w)=epsilon^r*w. This last conclusion
would NOT hold for general complex evaluations without a field
automorphism; the cyclotomic field is essential.

We use only classical cyclotomic facts, with proofs of the needed
basis statements in Section 6: degrees phi(d), the automorphism
zeta->zeta^2, and irreducibility of the cyclotomic polynomial. No
computer-certified set exclusion is needed.

### 5.1 M=65

U is a unit orbit. The primitive 65-th roots are rationally independent
because 65=5*13 is squarefree, so w=v(zeta_65) is nonzero. But
2^6=-1 mod 65, hence sigma^6(w)=-w by antisymmetry. The sign equation
instead gives sigma^6(w)=w, contradiction.

### 5.2 M=85

Write w=w5+w17 for its order-five and order-seventeen contributions
at a primitive 85-th root. The order-seventeen contribution is nonzero:
its eight signed powers are a subset of the rationally independent
nontrivial seventeenth roots. Since 2^4=1 mod 5 and -1 mod 17,

    sigma^4(w)=w5-w17.

If w were zero, this equality and w5+w17=0 would force w17=0.
Thus w is nonzero; the sign equation gives sigma^4(w)=w and again
forces w17=0, contradiction.

### 5.3 M=63 with order-nine and order-seven support

Evaluate at a primitive TWENTY-FIRST root, not a primitive 63rd root.
Write w=w3+w7. The order-nine points project to three signed
third-root pairs, so

    w3=k*(zeta_3-zeta_3^2),   k in {-3,-1,1,3},

and w3 is nonzero. The order-seven contribution w7 is nonzero by
prime-root independence. Since 2^3=-1 mod 3 and 1 mod 7,

    sigma^3(w)=-w3+w7.

If w=0 both contributions would be zero. For nonzero w, epsilon=+1
would force w3=0, and epsilon=-1 would force w7=0. Both are impossible.

This is why primitive-63 evaluation ALONE is insufficient: an
antisymmetric combination of primitive ninth roots can vanish there.
The lower-order character prevents that cancellation.

### 5.4 M=63 with a unit orbit

Normalize U={+/-2^i:0<=i<6} modulo 63. These twelve exponents are
distinct modulo 21. Section 6 proves that their primitive-63 root
evaluations are linearly independent. Thus w=v(zeta_63) is nonzero,
and sigma(w)=epsilon*w forces the COEFFICIENT identity

    doubled(v)=epsilon*v.

It follows that the six choices for C have either constant signs
along the 2-orbit (epsilon=+1), or alternating signs (epsilon=-1).
In the first case all six F-transitions are positive. Iterating their
lifts x->2x+t gives 63c=0, since 63t=0. In the second case every
transition is negative; the forced-positive rule excludes N1,N2,
so every lift is x->-2x and again gives 63c=0 after six steps.

But H has order 189. This equation requires c to be divisible by
three in Z/189, whereas its image in Z/63 is a unit. Contradiction.
All five subgroup orders have been excluded, proving Theorem 9.1.

## 6. Classical basis facts used above, with proofs

For a prime p, {zeta_p^i:1<=i<p} is a rational basis: a relation
with zero constant term and degree <=p-1 cannot be a nonzero multiple
of Phi_p=1+X+...+X^(p-1).

For coprime prime conductors p,q, Q(zeta_p,zeta_q)=Q(zeta_(pq))
has degree (p-1)(q-1). The product of their nontrivial prime-root
bases is therefore a basis. By CRT these products are precisely the
primitive pq-th roots, proving the squarefree-65 fact used here.
This standard normal-basis statement is also recorded in
[Keith Conrad, Linear Independence of Characters](https://kconrad.math.uconn.edu/blurbs/galoistheory/linearchar.pdf),
Example 3.2 and its footnote. The specialized proof above is supplied
to make the dependency transparent, not as a novelty assertion.

For 63=9*7, write zeta_63=zeta_9^4*zeta_7^(-3).
The nontrivial seventh roots form a basis over Q(zeta_9), since
[Q(zeta_63):Q(zeta_9)]=6. Grouping a rational relation between
primitive 63rd roots by its seventh-root component reduces each group
to a relation between primitive ninth roots. Since

    Phi_9=X^6+X^3+1,

the ONLY relations supported on the six unit exponents modulo nine
have constant coefficients on {1,4,7} and separately on {2,5,8}.
Equivalently, the coefficients in a relation among primitive 63rd
roots are constant on each triple {a,a+21,a+42} of unit exponents.

A support with at most one exponent per such triple is therefore
independent: the two missing coefficients are zero, forcing the
third to be zero. Our twelve exponents +/-2^i have distinct residues
modulo 21, explicitly

    {1,2,4,8,16,11,20,19,17,13,5,10}.

This proves the specialized independence used in Section 5.4.

## 7. Proof of the cubic-fiber corollary

Let a_i be the centers and b_i the singleton labels in a cubic fiber.
They are separately distinct, since doubling is injective. If
b_i=a_j with i!=j, canceling a_j from
2a_i+a_j=2a_j+b_j gives the forbidden pair equality
2a_i=a_j+b_j. Thus a common center/label can only be its own pure
representation a_i=b_i.

Two distinct pure representations would satisfy 3a_i=3a_j and yield
an order-three difference, excluded by Theorem 9.1. There is therefore
at most one such common point. If the fiber size is m, its union of
centers and labels has size 2m or 2m-1, at most eight. Hence m<=4,
with exactly the support cases in Section 1. QED.

## 8. A concrete failure of a tempting stronger reduction

The implication "a multiway cubic fiber must contain an order-three
difference" is FALSE without global h=0. For example, modulo 39305,

    A=(0,1,17,289,4913,4911,4879,4335)

is valid and has

    4913=2*0+4913=2*1+4911=2*17+4879=2*289+4335.

It has h=22,R3=3, and no order-three difference (3 does not divide
39305). Thus no-order-three alone does NOT imply R3=0. This is not
a counterexample to either h=0=>D=0 or the 248 bound.

Here is a complete validity proof. Put R=17,Y=R^3=4913 and
C={0,1,R,R^2}; A=C union {Y-2c:c in C}. Every eight-term sum is
between 0 and 8Y=39304, so equality modulo 39305 is integer equality.
The target is 4Y-(1+R+R^2). If k_c counts the C-point c and l_c its
partner Y-2c, reducing successively modulo R forces

    k_c-2l_c=-1   for c=1,R,R^2.

Indeed each difference from -1 lies in [-15,9], so zero is the only
multiple of 17. The top coefficient then forces sum l_c=4. From
sum k_c=4 follows k_0=2l_0-1 as well. Thus all four l_c>=1, whence
all l_c=1 and all k_c=1. This is the unique all-ones multiset.

## 9. Exact checks, limitations, and remaining lemma

Reproduce using standard-library Python 3:

    python stage9_cubic_torsion_checks.py

The checker has no project imports. Its fully bounded work is:

* Eleven partitions of six with 166 cycle-sign choices, checking the
  annihilator bound and the exact five possible large subgroup orders.
* Orbit unions in FIVE fixed relation-derived quotient groups, all
  of order <=105: 704 masks total, at most 256 in one group. These are arithmetic
  supports, not an enumeration of all valid sets or all moduli.
* Exactly 256 signed quotient orientations. Only four pass the
  projected autocorrelation test, all in the unit-63 family, with
  masks 0,21,42,63; Section 5.4 excludes their lifts algebraically.
* Exact polynomial reduction and rational ranks: the 48 primitive
  65th roots are independent, the twelve chosen 63rd roots are
  independent, and all 36 primitive 63rd roots have rank 24 with
  the twelve explicitly checked triple relations.
* Three fixed valid eight-point fixtures, each tested through all
  6435 multisets. The binary-255 control has h=R3=0 and no order-three
  difference; the reused stage8 CRT control has h=27,R3=0 and an
  order-three pair; the constructed four-way control has h=22,R3=3.

There are three fixture candidates and three valid fixtures, with one
new non-h0 multiway construction. NO new h=0 structural diversity
was found or sampled. The orbit enumeration is complete for its five
fixed quotient arithmetic problems; it is not a search certification
of the general goal. The proof instead uses the complete spoke table,
the small cycle arithmetic table, and the cyclotomic arguments.

The most useful unresolved lemma is now:

    Under odd h=0 and validity, exclude a three-way cubic fiber
    2a_1+b_1=2a_2+b_2=2a_3+b_3 whose centers and singleton
    labels are disjoint or share only one own pure point.

This is a proposed sufficient lemma, not proved. Every larger cubic
fiber contains such a triple; proving its exclusion would give R3=0
and, by stage8, finish h=0=>D=0. A counterexample would require a
direct multiway quartic bridge rather than exclusion of R3.

The original 248 target also retains its separate shadow-credit
obstruction: even at h=R3=D=0, Sigma>=53 is not proved. Neither
Theorem 9.1 nor the cubic-size bound should be mistaken for |E4|>=60.

No PR can be created from this workspace: it has no Git repository
or configured remote. The active full goal remains unproved.
