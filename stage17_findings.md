# Stage 17: closing the two-ordinary endpoint obstruction

Date: 2026-10-10. One focused round with a local proof researcher, an
independent challenger, a global-bound researcher, and the coordinator.
The full h=0 => D=0 and N>=248 goals remain OPEN. No novelty claim.

## 1. New result and its meaning

**Computer-assisted theorem.** Let A be a valid eight-point set in a cyclic
group, with odd difference-generated subgroup H and h=0 (doubling closure
of its nonzero differences). Eight DISTINCT points of A cannot satisfy

    X=2a+b+p=2c+b+q=2u+v+w.

Validity means that the eight-term all-ones sum of A has no other
eight-term multiset representation. The theorem does not require freshness,
endpoint conditions, isolation, MC, or R3=0. It uses a new complete finite
certificate calculation after elementary coverage and an elementary
cyclic torsion finish. It is not claimed as a wholly elementary theorem.

In plain language, the last opposing shape of the two-ordinary endpoint
branch is impossible: two overlapping repeated sums cannot share their
value with the separate ordinary sum on the other three points.

Combined with the Stage 15 opponent exclusions and Stage 16 isolated22
exclusion, this closes the known TWO-ORDINARY singleton-defect branch.
That classification corollary retains the Stage 13/14 MC computational
dependencies. The new local theorem itself has none of those dependencies.

## 2. Proof coverage and finite certificates

The full proof is in stage17_local_findings.md; its independent coverage
and arithmetic audit is in stage17_challenger_findings.md.

* h=0 supplies 2(a-u)=e-f. Substitution gives e+b+p=v+w+f.
  A squarefree side would violate validity, and literal equality is
  impossible by disjoint tails. Hence e is b or p and f is v or w.
  The corresponding c-domain has e in {b,q}, f in {v,w}.
* Complete elementary case analysis reduces all 16 assignments to two
  symmetric own-tail cases. After swapping v,w if needed, they are
  2(a-u)=p-v and 2(c-u)=q-w.
* With w=0, t=a-u, e=c-a, the eight points are the integer vectors
  (0,u,u+t,u+t+e,-4t,2t+4e,2t+2e,4e), in label order
  (w,u,a,c,b,p,q,v). No odd denominator is inverted.
* Check every one of the 56 ordered roles for each of 2(v-w)=8e and
  2(b-w)=-8t. Of 112 single roles, 102 have forbidden-rival certificates.
  The retained 6-by-4 domain has 24 combinations; 15 have certificates,
  leaving nine necessary symbolic presentations.
* For each rank-two survivor choose an integer functional F annihilating
  its rows and an actual point difference d maximizing F(d)>0. All 56
  possible partners d' of 2d satisfy F(2d-d')>=F(d)>0. Thus the last
  relation has rank three. All 9*56=504 branches are covered; 498 have
  forbidden-rival certificates and six remain for the torsion argument.

Every one of the 615 main exclusions preserves an eight-term rival and
an exact identity 2^k*(rival-target)=sum(z_i*row_i), with integer z_i.
The six final determinants are 503,489,501,483,549,531. The adjugate
annihilates u,t,e, which generate H; cyclicity gives |H| dividing the
determinant. Validity gives |H|>=128 by distinct subset sums.

The signed doubling orbits modulo primes 503,163,167,61,59 have sizes
502,162,166,60,58 respectively, all exceeding the 56 actual differences.
Excluding these prime factors leaves |H|<=9 in five cases. In the 483
case, H must contain factors 7 and 23. A complete rook-clique argument
forces a difference nonzero in both projected coordinates. Its signed
doubling orbit modulo 161 has 66 elements, again impossible. This treats
odd torsion explicitly instead of discarding odd denominators.

An optional endpoint diagnostic excluded zero cases and is NOT a premise
of the stronger theorem. All intermediate and final arithmetic survivors
are preserved; none is a valid counterexample.

## 3. Independent verification and global restriction

The challenger imported no producer or historical kernel. Its separate
implementation cross-checked the initial 16 roles (14 certificates, two
survivors), reconstructed the canonical coordinates and all later role
partitions, and verified all 615 main integer certificates. It rejected
2460 deliberate corruptions, checked every maximizing functional and
all 504 final branches, and independently checked the torsion arithmetic.
The coordinator additionally checked all six adjugate identities and
rejected six altered adjugates using a third small implementation.
That same separate checker verifies all 194 global arithmetic certificates
and rejects 388 deliberately incorrect or noninteger coefficient variants.
The producer's zero-budget path was checked: it reports TIMEOUT/incomplete
and does not claim an exclusion. The final producer run was COMPLETE
in 1.390 seconds under a cooperative 60-second cap.

The global-bound agent proved new regular-branch restrictions, audited
independently: all-ordinary cycles are triangles; even cycles without a
22 vertex are impossible; three consecutive 31 vertices in a longer
cycle are impossible. The resulting admissible cycle lengths are 3,4,5,
with every four-cycle containing a 22. The full proofs and precise type
restrictions are in stage17_global_findings.md. These are elementary
restrictions, not a proof that there are at least 53 cycles.
The remaining four-cycle type words are QOOO and QPOO; the five-cycle
words are PPOOO, POPOO, QPOOP, QPOOO, with O=ordinary, P=31, Q=22.
They are necessary type patterns, not certified realizations.

Writing c2 for isolated22 vertices, I for internal vertices of nontrivial
paths, and t_j for the number of j-cycles, the existing degree count and
new length restriction give

    3C=188+c2-I-t4-2t5.

Thus the regular shadow target C>=53 is exactly

    I+t4+2t5 <= 29+c2.

This is a precise remaining counting obligation, NOT a proved inequality.
The global proof audit caught and corrected an omitted four-cycle case
containing a 22; that case is not silently excluded.

## 4. Remaining work and reproducibility

The singleton-defect case still needing work is the 31/ordinary endpoint.
Other isolated-ordinary center defects remain separate. Same-center and
same-singleton forced-cubic transport are already proved impossible.
All three forced-cubic branches (no pure, pure at u, pure elsewhere)
remain distinct; paired u-marks p,q may still be multiway.

The next focused local step is to classify opponents of the remaining
31/ordinary endpoint before another finite role calculation. The global
alternative is to prove the displayed path/cycle budget. Do not extend
the completed two-ordinary search without a new structural reason.

Even proving h=0=>D=0 would leave the shadow inequality and h>0 for
N>=248. The exact sufficient target is |T4|>=89, or
Sigma-D>=53-8(h+R3); the stronger growth-lemma budget is a different goal.

Run from this directory with standard-library Python:

    python stage17_local_roles.py --seconds 60
    python stage17_independent_check.py
    python stage17_global_checks.py
    python stage17_coordinator_check.py

Run both producers before their respective audits, which read saved results. These
commands overwrite only their designated Stage 17 output files. On this
Windows machine use the bundled Python executable if the Python alias
is unavailable. Historical Stage 10/13/14/16 checks were NOT rerun.
No Lean, sampling, actual candidate-set enumeration, or modulus sweep
was performed. No literature novelty was investigated.

The round finished its targeted proof before the 45-minute maximum; it
did not begin another defect branch. Stage 15/16 and the new results are
delivered together in one PR against current main, without a merge.
