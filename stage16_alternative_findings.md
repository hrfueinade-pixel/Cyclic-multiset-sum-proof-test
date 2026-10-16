# Stage 16 alternative audit: the isolated-22 local roles

Research date: 2026-10-10. One focused round. This agent performed no
computation, random sampling, modulus search, or historical rerun. The
new finite check described below was run by the main researcher and
independently read here; this is not an independent-generator rerun.
No novelty claim is made. The original 248 target and h=0 => D=0 remain
open.

## 1. Scope and hypotheses

Let A be valid, have eight distinct points, and lie, after translation,
in its odd cyclic difference-generated subgroup H. Assume h=0:
doubling sends every nonzero ordered A-difference into the difference
set Delta. Multiplication by every power of two is injective in H.

Study seven DISTINCT points satisfying

    X = 2a+b+p = 2c+b+q = 2r+2s.                 (1)

Write f for the eighth point. Validity implies squarefree replacement
uniqueness through degree eight: a squarefree sum cannot equal another
same-length multiset sum. In particular ordered nonzero differences
are unique, and all multiset pair sums are unique.

The elementary restrictions below require neither freshness of X nor
MC nor R3=0. Freshness motivated this shape, but is not a hypothesis
needed in the local algebra. No assumption concerning uniqueness of
available cubic partners is used.

## 2. Complete elementary role restriction

For t in {a,c} and x in {r,s}, h=0 supplies the unique labels e,v in A
such that

    2(t-x) = e-v.                               (2)

Let y be the other core point. Let k=p when t=a and k=q when t=c.
Then the possible roles are exactly restricted to the following list
of NECESSARY options; membership in this list does not establish
realizability:

    e in {b,k};
    v in {t,other ordinary center,y,f};
    v = other ordinary center implies e=b.      (3)

Thus there are seven options per comparison. Here and below f is the
actual eighth point, not a freely renamed negative label.

Proof for t=a; exchange a,c and p,q for the other row. Substituting
(2) into (1) gives

    e+b+p = 2y+v.                               (4)

If e is outside {b,p}, the left side is squarefree, whereas the right
side repeats y, a forbidden replacement. Hence e is b or p.

The negative label v cannot equal e because a!=x. Nor can it be the
other member of {b,p}: if e=b,v=p, (4) gives b=y; if e=p,v=b, it gives
p=y, in each case by doubling injectivity. Therefore neither own tail
is possible as a negative label.

If v=x, equation (2) gives 2a=x+e, a forbidden squarefree-pair
replacement, since x and e are distinct.

If v=q and e=b, combining (2) with the c representation in (1) gives

    a+y=c+b,

a forbidden equality of distinct squarefree pairs. If v=q and e=p,
use p-q=2(c-a) to obtain 2a=x+c, again forbidden.

Finally suppose v=c and e=p. Equations (1),(2) give

    2p+b=2y+c,
    3c+q=2x+2p.                                 (5)

The last equality is a disjoint 31/22 collision, excluded by the
elementary Lemma 2.2 of stage8_regular_bridge_findings.md under h=0.
For completeness, its proof is reproduced next. This excludes the
only remaining option missing from (3). All eight label possibilities
have been covered. QED.

### Local 31/22 exclusion, without the global Stage 8 hypotheses

Suppose 2u+2w=3z+d with four distinct points, and both doubled
differences 2(u-z),2(w-z) are in Delta. Write 2(u-z)=i-j. Substitution
gives 2w+i=z+d+j. Its right side must repeat, so j=z or d. The first
choice gives 2u=z+i, a forbidden pair equality. Thus j=d and
i=2u-2z+d is in A. Similarly k=2w-2z+d is in A. The original quartic
equality now gives

    i+k+z=3d.

The left side is squarefree: i=k would give u=w, i=z would give w=d,
and k=z would give u=d. This is a forbidden replacement. QED.

## 3. All four negative labels are distinct

**Elementary proposition.** In the four comparisons (2), all four
negative labels v are pairwise distinct.

### 3.1 Within one ordinary-center row

Suppose

    2(a-r)=e_r-v,  2(a-s)=e_s-v.

If e_r=e_s, then r=s. Otherwise {e_r,e_s}={b,p}. Add these equations
and use (1); the result is

    2(a+v)=2(b+p), hence a+v=b+p.

This is a forbidden squarefree-pair replacement: a is distinct from
b,p, so the pair multisets cannot be identical, irrespective of v.
The c row has the same proof.

**Correction of the preliminary interpretation.** Reusing f at both
core comparisons of one center does force the three-way cubic
2a+f=2r+e_r=2s+e_s. However, adding the equations ALSO forces
3a+f=X, or equivalently a+f=b+p. Therefore this is not a surviving
local configuration. The earlier preliminary suggestion that this
three-way cubic alone might be harmless omitted its direct cone to X.

### 3.2 Between the two ordinary-center rows

Suppose

    2(a-x)=e-v,  2(c-y)=h-v,
    e in {b,p}, h in {b,q}, x,y in {r,s}.         (6)

The negative label v can be ANY point of A; no free-point hypothesis
is needed. Equation (1) gives 2(a-c)=q-p.

If x=y, subtraction in (6) gives q-p=e-h. The four positive choices
give respectively

    e=b,h=b: q=p;
    e=p,h=q: 2(q-p)=0, hence q=p;
    e=b,h=q: b+p=2q;
    e=p,h=b: 2p=b+q.

Each is a duplicate point or forbidden pair replacement.

If x!=y, they are the two distinct core points, and subtraction gives

    2(x-y)=q-p-e+h.                              (7)

For e=h=b, (7) and (1) imply x-y=a-c, violating ordered-difference
uniqueness between disjoint point pairs. For e=p,h=q they imply
x-y=q-p, with the same contradiction.

For e=b,h=q, use the c equality in (1) and its image equation in (6):

    b+2q=2x+v.

Add 2a-2x=b-v to this identity. It gives a+q=2x, a forbidden pair
replacement. For e=p,h=b the symmetric argument gives c+p=2y.
Every positive choice and both core allocations have been covered.
This proves cross-row nonreuse and hence the proposition. QED.

## 4. One additional elementary filter

At the SAME core point x, the two comparisons cannot both have
positive label b. Otherwise

    2(a-x)=b-v_a,  2(c-x)=b-v_c

imply q-p=v_c-v_a. Difference uniqueness forces v_c=q,v_a=p, but
(3) excludes those negative labels. This argument uses no MC or
global partner selection.

There remain four pairwise distinct negative labels chosen from
{a,c,r,s,f}, with r available only in the s comparisons and s only in
the r comparisons. Four-label distinctness alone is not an exclusion;
one must use the actual relation equations and validity.

## 5. Audit of the bounded new check

The main researcher wrote stage16_isolated22_roles.py and reported:

    scope: 7^4=2401 local role assignments, not valid sets or moduli;
    negative-reuse filter: 1913 assignments;
    same-core common-positive filter: 260 assignments;
    remaining presentations: 228, all rank four;
    certified eight-term rivals: 228;
    survivors: zero;
    status: COMPLETE, 1.735 seconds with a 90-second cap.

This agent read the script and audited its mathematical translation
without rerunning it. The points are normalized as s=0, with formal
coordinates (r,a,c,b,f), and

    p=2r-2a-b, q=2r-2c-b.

The four generated rows are precisely

    2(center-core)-positive+negative=0,

with the seven options (3) per row. The two prefilters are exactly
Sections 3 and 4 above, so no valid local role assignment is discarded
without an elementary justification.

For each remaining presentation the script enumerates the 6434
non-all-ones eight-term count vectors. It obtains an exact identity

    2^k * (rival_sum - all_ones_sum)
        = sum_i integer_coefficient_i * relation_row_i.     (8)

The final assertion checks (8) coordinate by coordinate as an INTEGER
identity and checks that its positive multiplier is a power of two.
Thus in any odd group the rival sum equals the all-ones sum, violating
validity. No odd torsion is divided out. The row reduction can miss
certificates (especially with rank deficiency), but every returned
certificate is sound because of this final exact check. All actual
remaining presentations were reported rank four.

This supports the computer-assisted local exclusion:

    Under odd h=0 and validity, seven distinct points cannot satisfy
    2a+b+p=2c+b+q=2r+2s in an eight-point A.

It does NOT require MC, R3=0, freshness, or a modulus bound. The
computational statement remains dependent on completion of the new
228-presentation check. A read-only code audit is not a second run,
not a separate implementation, and not an elementary exclusion of
all presentations. No individual numerical configuration was tested
for validity by this agent.

## 6. Dependency ledger and stopping boundary

Elementary, with complete proofs here: the seven-option domains;
nonreuse within and between ordinary-center rows; the equal-core
common-positive filter; the local disjoint 31/22 exclusion.

Finite computation: the main researcher's exhaustive completion over
the 228 surviving formal presentations, using exact dyadic integer
certificates. This note records a read-only coverage/algebra audit.
Reproduce with `python stage16_isolated22_roles.py --seconds 90`.
This agent did not execute that command.

Conjectural/unresolved: h=0 => D=0; the original |E4|>=60 at N<248;
transport for remaining singleton-defect opponents and isolated
ordinary defects. No proof about those residual shapes follows merely
from this isolated-22 exclusion.

The next focused obstruction is the two-ordinary endpoint component
opposite an isolated ordinary component. This round stops after the
isolated-22 role audit, without expanding to that next shape.
