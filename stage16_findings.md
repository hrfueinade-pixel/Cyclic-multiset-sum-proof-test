# Stage 16: exclusion of the two-ordinary / isolated-22 branch

Date: 2026-10-10. One bounded continuation from Stage 15. No novelty
claim, Lean, sampling, all-modulus sweep, or historical computation rerun.
The full h=0 => D=0 and original 248 targets remain OPEN.

## 1. Result and precise scope

**Computer-assisted exclusion.** Let A have eight distinct points in a
cyclic group whose difference-generated subgroup H is odd. Assume A is
valid and its nonzero differences are closed under doubling (h=0).
There cannot be SEVEN DISTINCT points a,c,b,p,q,r,s of A satisfying

    2a+b+p = 2c+b+q = 2r+2s.                         (1)

This excludes the isolated-22 opponent of a fresh two-ordinary endpoint
component. In fact, the statement does not require freshness, isolation,
MC, or any of the Stage 10/13/14 finite computations. The reduction below
is elementary; its final 228-case exclusion is a NEW finite-computation
dependency. It is not presented as a complete elementary exclusion.

There is no actual candidate-set or modulus enumeration. Candidate counts
below count formal role assignments, not valid sets or affine classes.

## 2. Elementary foundations

Validity forbids a different equal-length representation of any squarefree
sum of at most eight points: add its complementary points to obtain a
rival for the eight-term all-ones target. In particular, a squarefree pair
cannot have any different pair representation. In odd H this implies
uniqueness of all nonzero ordered differences: x-y=u-v gives x+v=u+y;
if this is not a literal pair identity, either a side is squarefree or
both repeat, the latter giving 2x=2u and then x=u by oddness.
Doubling and every power of two are automorphisms of H.

We need one short local consequence of h=0 (Stage 8, Lemma 2.2), recorded
here to make the mathematical dependencies self-contained.

**Disjoint 22/31 lemma.** If u,v,z,w are four distinct points of A, then

    2u+2v=3z+w

is impossible under the stated hypotheses. Write 2(u-z)=e-f by h=0.
Then 2v+e=z+w+f. The right side cannot be squarefree: it would equal a
repeated triple, not the same literal multiset. Thus f=z or w. If f=z,
then 2u=z+e; e=z would force u=z, otherwise this is a forbidden
squarefree-pair replacement. Consequently f=w and e=2u-2z+w belongs
to A. Likewise g=2v-2z+w belongs to A. The quartic equality gives

    e+g+z=3w.

Its left side is squarefree. Indeed e=g would give u=v; e=z would give
2v=2w, and g=z would give 2u=2w. All are impossible. This is the desired
squarefree contradiction. No division by an odd integer is used.

## 3. Seven local choices for each doubled difference

Fix x in {r,s}, and let y be the other core point. Write the UNIQUE
ordered representation supplied by h=0 as

    2(a-x)=e-v.

Using (1), we have e+b+p=2y+v. If e is outside {b,p}, the left triple
is squarefree and the right triple repeats, a contradiction. Therefore
e is b or p. We now exhaust the eight possible roles of v:

* v=e would give a=x. If v is the OTHER tail, substitution in (1)
  gives 2y=2e and hence y=e. Thus neither b nor p is possible.
* v=x gives 2a=x+e, a forbidden squarefree-pair replacement.
* v=q,e=p gives 2(a-x)=p-q=2(c-a), hence 2a=x+c, forbidden.
* v=q,e=b gives 2b+p=2y+q. Subtracting this from
  2c+b+q=2x+2y and using 2(a-x)=b-q gives a+y=b+c,
  another forbidden pair equality. Equivalently solve q=2x+b-2a
  directly in the second ordinary equality.
* v=c,e=p gives 2p+b=2y+c. Combining with the second ordinary
  equality gives 3c+q=2x+2p, impossible by the disjoint 22/31 lemma.

Writing f for the eighth, unused point, the exact remaining domain is

    e=b, v in {a,c,y,f};  OR  e=p, v in {a,y,f}.       (2)

Interchange a,c and p,q for the other ordinary center. There are SEVEN
choices for each of the FOUR comparisons (a,r),(a,s),(c,r),(c,s).
No unspecified partner is chosen: difference uniqueness makes each
comparison's ordered representation unique, and every permitted role
is included.

## 4. All four negative labels must be distinct

These are complete elementary restrictions, independent of the numerical
check. They are stronger than merely prohibiting free-point reuse.

### 4.1 No reuse within one ordinary center

Suppose both comparisons for a have the same negative label v:

    2(a-r)=e_r-v,  2(a-s)=e_s-v,  e_r,e_s in {b,p}.

If e_r=e_s, oddness gives r=s. Otherwise {e_r,e_s}={b,p}; add the
equations and use 2r+2s=2a+b+p to get

    a+v=b+p.

The distinct pair b,p cannot equal this other literal pair, because v
is neither b nor p and a is outside {b,p}. Contradiction. The same
argument applies to c. The earlier suggestion that such reuse might
merely create a harmless cubic triple was INCOMPLETE: it omitted this
pair contradiction. It is not retained as an unresolved possibility.

### 4.2 No reuse across the two ordinary centers

Suppose 2(a-x)=e-v and 2(c-y)=g-v, with x,y in {r,s},
e in {b,p}, g in {b,q}. Use 2(a-c)=q-p. All eight cases give:

| x,y | e,g | Consequence |
| --- | --- | --- |
| x=y | b,b | a=c |
| x=y | p,q | p=q |
| x=y | b,q | 2q=b+p |
| x=y | p,b | 2p=b+q |
| x!=y | b,b | a-c=x-y |
| x!=y | p,q | x-y=q-p |
| x!=y | b,q | a+q=2x |
| x!=y | p,b | c+p=2y |

For equal cores, subtracting the two doubling equations immediately gives
the first four entries. For different cores their subtraction gives
2(a-c)-2(x-y)=e-g. The first two entries then follow by oddness.
For e=b,g=q this gives 2(x-y)=2q-p-b; combine with
2a=2x+2y-b-p to obtain a+q=2x. The last entry is symmetric.
The difference equalities contradict ordered-difference uniqueness on
seven distinct points. The remaining entries violate distinctness or
squarefree-pair uniqueness. Thus reuse across rows is impossible.

### 4.3 Two common-positive labels at one core are impossible

If both comparisons at the same core x use positive b, write
2(a-x)=b-v_a and 2(c-x)=b-v_c. Then

    q-p=2(a-c)=v_c-v_a.

Difference uniqueness forces v_c=q and v_a=p, excluded already by (2).
This is an additional necessary role filter, not an assumption about
which negative labels are available.

## 5. Finite arithmetic check and why it is sound

Normalize s=0. Use a formal Z^5 presentation with coordinate order
(r,a,c,b,f). The eight point vectors are

    s=0, r=(1,0,0,0,0), a=(0,1,0,0,0), c=(0,0,1,0,0),
    b=(0,0,0,1,0), p=2r-2a-b, q=2r-2c-b, f=(0,0,0,0,1).

This imposes (1) exactly in every target group. Each role assignment
imposes four integer rows

    2(center-core)-positive+negative=0.               (3)

For each allowed assignment the check lists ALL 6434 distinct eight-term
multisets other than the all-ones multiset: C(15,7)-1=6434. Their count
vectors are nonnegative, sum to eight, and differ literally from all ones.
For each, form the integer vector v equal to rival sum minus target sum.
Exact rational row reduction is only used to FIND a certificate. An
exclusion is accepted only after constructing and checking an identity

    2^k v = sum_i z_i row_i,  with integer z_i and k>=0.    (4)

In any actual odd H, (3) and (4) imply 2^k v=0 and then v=0. That rival
contradicts validity. NO odd denominator is inverted or discarded. Every
accepted certificate is rechecked coordinate by coordinate using integer
arithmetic. Rational row-space membership alone is NOT an exclusion.

The script would set free elimination coefficients to zero at deficient
rank, potentially missing witnesses but never accepting a false one.
In this run EVERY eligible presentation had rank four, so that limitation
does not arise. It does not infer a theorem from passing sample tests:
the elementary reduction covers every possible local role assignment,
and the completed enumeration produces a forbidden-sum certificate for
each remaining assignment.

Reproduce from this directory, with standard-library Python only:

    python stage16_isolated22_roles.py --seconds 90

The defined scope was at most 7^4=2401 assignments and 6434 target rivals
per retained assignment, with a cooperative 90-second deadline checked
between assignments. No modular realizations, factorizations, random sets,
or historical solver calls are used. The check completed, not timed out:

    completion: COMPLETE
    elapsed_seconds: 1.735
    raw assignments: 2401
    excluded negative-label reuse: 1913
    excluded common-positive b at a core: 260
    eligible presentations: 228
    rank-four presentations: 228
    certified forbidden rivals: 228
    surviving local presentations: 0

These exclusions are counted in order; the filter counts are disjoint
process counters, not claims that the underlying obstructions never
overlap. They sum to 2401. No valid-set count or structural-diversity
census of actual A is asserted: no residue set was instantiated.

Root performed the arithmetic run. The alternative-route researcher
independently READ the code and audited coordinate coverage, filters,
transpose/row-operation orientation, and the dyadic certificate rule.
That audit passed, but was NOT an independent execution or independent
implementation. The challenger remained unavailable after its prior
usage-limit failure; no replacement agent was spawned to bypass it.
The new script does not import or share the Stage 10/13/14 kernels.

## 6. Dependency ledger and exact next checkpoint

| Statement | Status / dependencies |
| --- | --- |
| Seven choices per comparison | Complete elementary proof, validity + oddness + h=0 |
| Four distinct negative labels | Complete elementary proof above |
| Common-positive b core filter | Complete elementary proof above |
| No configuration (1) on seven distinct points | Complete bounded COMPUTER-ASSISTED exclusion of 228 presentations after the elementary coverage proof |
| A fresh two-ordinary endpoint cannot oppose isolated22 | Corollary of (1); does not need MC for this local exclusion |
| Classification of ALL remaining fresh fibers | Historical Stage 14/15 reduction; retains MC's Stage 13/14 computational dependency |
| Two-ordinary endpoint opposed by isolatedordinary | OPEN; now the ONLY opposite type for this endpoint shape |
| 31/ordinary endpoint defect | OPEN and separate |
| Other isolatedordinary center defects | OPEN |
| h=0 => D=0 | OPEN |
| Original E4>=60 / N>=248 goal | OPEN; regular Sigma>=53 and h>0 still remain |

**Next most useful targeted lemma.** Exclude a fresh two-ordinary endpoint
component opposite an isolated ordinary vertex. Its full eight-point
support splits as

    X=2a+b+p=2c+b+q=2u+v+w,
    {a,c,b,p,q} disjoint from {u,v,w}, all eight distinct.

There is now NO free point in this shape. Its isolatedordinary component
also has a center defect: both repeated cubic deletions 2u+v and 2u+w
are unpaired and force a multiway fiber elsewhere. Do not assume that
forced fiber cones back at X: Stage 15 proves same-center transport is
impossible. A successful argument must combine local closure constraints
or change roles in the multiway bridge. The isolated22 check is complete
and must not be rerun merely as a resumption step.

One focused round is complete. Work is saved locally only, per the latest
request to reserve GitHub checkpoints for necessary saves. The folder is
not a Git checkout; no GitHub branch/PR, merge, or unrelated repository
was created in this round. No process remains running.
