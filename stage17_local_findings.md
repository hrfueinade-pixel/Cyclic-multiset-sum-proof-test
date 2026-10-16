# Stage 17 local researcher: exclusion of the eight-point ordinary opponent

Date: 2026-10-10. One focused local round, standard-library Python only.
No modulus sweep, random sampling, Lean, historical computation rerun,
or literature novelty claim. This file is written by the local researcher;
the independent challenger and coordinator have their own audit records.

## 1. Result, scope and dependency boundary

**Computer-assisted theorem with an elementary torsion finish.** Let A
be a valid set of eight distinct points in a cyclic group, and let its
difference-generated subgroup H have odd order. Suppose the 56 nonzero
ordered differences are closed under doubling (h=0). There cannot be
eight distinct points a,c,b,p,q,u,v,w of A satisfying

    X = 2a+b+p = 2c+b+q = 2u+v+w.                 (1)

The theorem does not need freshness, endpoint isolation, MC, R3=0,
Stage 9, or Stage 15's order-seven exclusion. The endpoint/isolated-
ordinary branch follows immediately as a corollary. It does not exclude
the separate 31/ordinary endpoint branch or all other center defects.
The full h=0 => D=0 and the original N>=248 bound remain open.

The proof consists of a complete elementary reduction, 615 saved dyadic
eight-term rival certificates in a new bounded role check, and elementary
torsion arguments for six full-rank presentations that survive those
certificates. Those six are preserved in the JSON as ARITHMETIC
SURVIVORS, not asserted valid counterexamples. The independent challenger
verifies the certificates separately; root independently verifies the
small determinant/signed-orbit arithmetic in its torsion audit.

## 2. Complete elementary partner coverage

Validity means the all-ones eight-term multiset has no different
eight-term multiset representation. Therefore a squarefree sum of up to
eight distinct A points cannot have a different equal-length multiset
representation: append the remaining points. In odd H this gives
uniqueness of all 56 nonzero ordered differences, and powers of two are
invertible.

Use h=0 and difference uniqueness to write

    2(a-u)=e-f.

Equation (1) gives e+b+p=v+w+f. The two triples cannot be literally equal:
their disjoint pairs {b,p} and {v,w} each would need to be supplied by the
single extra point on the other side. If either triple were squarefree,
validity would give a contradiction. Hence BOTH triples repeat, forcing

    e in {b,p},  f in {v,w}.

For c the complete domain is e in {b,q}, f in {v,w}. These are all
possible roles, not selected favorable partners: there are exactly 16
initial pairs of assignments. No forced multiway cubic is introduced.

The two negative labels cannot coincide. Subtract the two equations and
use 2(a-c)=q-p. For positives (b,b), (p,q), (b,q), (p,b), a shared
negative gives, respectively,

    a=c;  p=q;  2q=b+p;  2p=b+q.

Each violates distinctness or squarefree-pair uniqueness. If both positive
labels are b while the negatives differ, subtraction gives q-p=v-w or
w-v, contradicting uniqueness of ordered differences on disjoint pairs.

The remaining mixed positive assignments are also impossible. If a uses
(b,v) and c uses (q,w), the second equation substituted in (1) gives
2q+b=v+2w. Consequently

    2(a+q)=2u+b-v+2q=2u+2w,
    a+q=u+w.

That is a forbidden equality of disjoint squarefree pairs. If a uses
(p,v) and c uses (b,w), the first equation similarly gives 2p+b=2v+w
and c+p=u+v. Interchanging v,w proves the other two mixed cases.

Thus the ONLY two possibilities have own-tail positives p,q and
different negative labels. They are interchanged by swapping v,w, which
preserves the hypotheses. Assume the canonical one:

    2(a-u)=p-v,   2(c-u)=q-w.                     (2)

This covers all 16 initial assignments completely elementarily. Of
those, eight fail shared-negative, two fail common-positive b, four fail
mixed-positive, and two are the symmetric surviving assignments.

## 3. Exact integer coordinates and bounded role check

Translate w to zero. Let t=a-u and e=c-a. Equations (1),(2), using only
addition and invertibility of 2, imply the exact point formulas

    w=0, u=u, a=u+t, c=u+t+e,
    b=-4t, p=2t+4e, q=2t+2e, v=4e.              (3)

For example, substituting p=2u+v-2a-b into the first equation (2)
gives 4a=4u-b. Subtract the ordinary equalities to get p-q=2(c-a),
then subtract (2) to obtain v=4(c-a). Thus (3) holds in every actual
odd H; no odd denominator is divided out. Parameters are formal integer
coordinates (u,t,e), not sampled residues or assumed independent in H.

The new script `stage17_local_roles.py` imposes the two prescribed
closure equations

    2(v-w)=8e = point_i-point_j,
    2(b-w)=-8t = point_k-point_l.                 (4)

Each equation has all 56 ordered distinct-point roles, so coverage is
immediate. For each relation presentation, all 6434 distinct eight-term
multisets other than all ones are enumerated as possible forbidden rivals.
A rejection is accepted ONLY with a saved identity

    2^k (rival sum - all-ones sum) = sum_i z_i row_i,
    k>=0 and all z_i integers.                  (5)

Every (5) is checked coordinate by coordinate with integer arithmetic.
Rational elimination is a discovery tool only; odd denominators are not
cancelled. Rank-deficient free coefficients are set to zero, so missed
witnesses are possible; false positive exclusions are not accepted.

The first direction in (4) retains exactly six necessary role options:

    (w,u), (w,c), (u,v), (a,b), (a,v), (b,c).

The second retains exactly four:

    (u,b), (a,b), (a,v), (c,b).

There are 102 saved single-direction exclusions. Among their 24 combined
presentations, 15 further certificates leave nine rank-two presentations:

| 2(v-w) partner | 2(b-w) partner |
| --- | --- |
| w-u | a-b |
| w-u | c-b |
| w-c | u-b |
| w-c | a-b |
| u-v | a-b |
| u-v | c-b |
| a-v | c-b |
| b-c | u-b |
| b-c | a-b |

### One justified rank-forcing extension

For each of these nine presentations, take a primitive nonzero integer
functional F annihilating its two rows. Choose an ordered point
difference d maximizing F(d) over all 56 roles. Since the points in (3)
span rational coordinate space and their differences are symmetric,
F(d)>0. For every closure partner d', F(d')<=F(d), and therefore

    F(2d-d') >= F(d) > 0.

Thus every one of the 56 supplied partner roles adds an independent
third relation. This is a proof of full-rank coverage, not heuristic
selection of a likely partner. Exactly one such extension is performed;
there is no repeated closure expansion. Across 9*56=504 full-rank
presentations, 498 additional certificates (5) leave six presentations.

The endpoint/isolation condition was also checked diagnostically: the
eight support points would force the quartic fiber X to consist exactly
of the three displayed quartics, since every fourth representation shares
a support point and creates a propagation edge (a squarefree deletion
would itself contradict validity). The nine rank-two presentations force
no extra quartic among the 327 alternatives. This check eliminates ZERO
presentations, is unnecessary for the theorem, and is not used as an
assumption in the final rank-forcing coverage.

The complete run used a cooperative 60-second cap and finished in 1.390
seconds. Completion is COMPLETE; timed_out is false. Every witness and
every intermediate/final survivor is saved in `stage17_local_results.json`.
The 615 accepted certificates are 102+15+498, with no overlap in the
process counters. Deliberately changing a certificate coefficient,
using an odd multiplier, or using the all-ones rival is rejected.

## 4. Elementary torsion finish for the six arithmetic survivors

All six final source differences are u-p. Their presentation matrices are
the first two rows shown below and the row enforcing its doubled partner.
All are rank three. The absolute determinants are:

| 2(v-w) | 2(b-w) | 2(u-p) partner | determinant |
| --- | --- | --- | --- |
| w-u | c-b | p-a | 503 |
| w-u | c-b | v-a | 489=3*163 |
| w-c | u-b | p-a | 501=3*167 |
| w-c | u-b | v-a | 483=3*7*23 |
| w-c | a-b | p-u | 549=9*61 |
| w-c | a-b | v-u | 531=9*59 |

Here H is generated by u,t,e: each is an actual difference, and all
point differences in (3) are integer combinations of them. The relation
matrix presents a finite abelian group of order its absolute determinant,
mapping onto H. Consequently |H| divides the determinant. This preserves
odd torsion; it does not treat a nonzero determinant as invertible.

### A sufficient elementary packing lower bound

For self-containedness, |H|>=128. Translate 0 into A and take the 128
subset sums of the seven other points. If distinct subsets U,V have
equal sums, choose |U|>=|V| and replace U in the all-ones multiset by V,
adding |U|-|V| extra zeros. That gives a different eight-term rival.
Thus all 128 sums are distinct. This simple bound suffices for the
torsion finish; no exact cubic fiber count or R3=0 assumption is needed.

### Large prime factors cannot occur in H

The signed doubling orbits of a nonzero element modulo the listed primes
have the following sizes, obtained from the displayed multiplicative
orders of 2:

| prime | order of 2 | signed orbit size |
| --- | --- | --- |
| 503 | 251 | 502 |
| 163 | 162 | 162 |
| 167 | 83 | 166 |
| 61 | 60 | 60 |
| 59 | 58 | 58 |

Every size exceeds 56. If one of these primes divides |H|, projection
onto its prime quotient is nonzero on some A-difference, since differences
generate H. The h=0 difference set contains all signed powers of two of
that difference, and their projection already has more than 56 distinct
values, impossible. No unit-difference assumption is needed. Removing
that prime from the corresponding determinant leaves |H| dividing 1,3,
or9, contradicting |H|>=128. Root's separate torsion audit verifies the
determinants and small order arithmetic independently of this local kernel.

### The determinant 483 case

The only divisors of 483 at least128 are161 and483, so H has order
161 or483. Project A into Z/7 x Z/23. There must be
some actual difference nonzero in BOTH coordinates. Otherwise each pair
of projected points agrees in one coordinate, and the projected set lies
in a single row or a single column: take two points with distinct first
coordinate (same second coordinate); any point with different second
coordinate would have to share the first coordinate of both, impossible.
If no such pair exists, all first coordinates agree already. Either
case contradicts that A-differences generate both prime projections of H.

The identified difference has order161 or483. Modulo161, 2 has order
lcm(3,11)=33, and -1 is not a power of2 because that cyclic subgroup has
odd order. Its signed doubling orbit therefore has66 elements. A
difference of order483 has a projection of order161 and so its signed
orbit has at least66 elements as well. Both contradict |Delta|=56.
This excludes the last arithmetic survivor.

## 5. Verification and precise next checkpoint

Reproduce the bounded role check from this directory:

    python stage17_local_roles.py --seconds 60

The independent challenger reconstructs the coordinates, coverage,
functional choices and integer identities without importing this checker.
Its report records the independently completed audit and corruption
tests. Root separately checks all six determinants and signed doubling
orbit arithmetic. Those audits are supporting verification, not a
replacement for the coverage proofs above.

This completes the two-ordinary versus isolated-ordinary branch, along
with a stronger no-configuration-(1) theorem. Together with Stage16's
isolated-22 exclusion and Stage15's other opponent exclusions, it closes
the known two-ordinary endpoint defect branch, retaining the historical
MC dependency only when applying the endpoint classification.

The 31/ordinary endpoint defect and other isolated-ordinary center
defects remain separate and OPEN. Even excluding all h=0 defects would
still leave the regular shadow inequality Sigma>=53 and h>0 cases before
the original bound N>=248. No unrestricted proof or counterexample is
claimed. No same-center transport of the forced cubic was used.
