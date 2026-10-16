# Stage 10: a bounded computational exclusion of four-way cubic fibers

Research date: 2026-10-10. The full objective h=0 => D=0 is STILL OPEN.
This stage closes the four-way branch, with an explicit computational
dependency. It does not prove the three-way exclusion, the full objective,
or |E4|>=60. No literature novelty is asserted.
Follow-up: stage11_threeway_findings.md proves a free-point restriction
for the no-pure three-way case and records the exact stopping point.

## 1. Statement and dependencies

**Computer-assisted proposition.** A valid eight-point set in an odd
cyclic difference-generated subgroup H, satisfying h=0, has no cubic
fiber with four representations. Consequently every cubic fiber has at
most three representations.

The proof consists of the coverage argument below and two complete finite
template checks. The check is not a self-contained elementary proof.
Independent modular calculations audit the quotient solver, but share the
structural generators. Structural coverage is therefore proved separately.
No statement relies on the paper's n<=7 computational certification.

Elementary prerequisites, proved in the indicated reports:

* Validity forbids a nonzero balanced zero relation having all coefficients
  >=-1: adding it to the all-ones vector gives an eight-term rival.
  It also forbids a replacement of a squarefree sum of degree <=8.
* In odd H all 36 pair sums and 56 ordered differences are distinct.
  At h=0 doubling permutes the differences.
* Stage5, Proposition 1b and Corollary 2a: for a fixed singleton base a,
  the equations 2d+a=2e+r, one for each r!=a, form an oriented spanning
  tree. No edge enters a. Its odd presentation determinant has absolute
  value <=2187 and is divisible by |H|. These facts do not assume R3=0.
* Stage7, Lemma 2: disjoint 22/31 quartic equalities are impossible at h=0.
* Stage9, Theorem 9.1 and Corollary 9.2: no difference has order three;
  cubic fibers have at most four marks and at most one pure mark.
  A singleton label cannot be a foreign center in the same fiber.
* The cubic exterior packing gives |H|>=184+2R3>=184.

In particular a four-way fiber has exactly one of the following forms:

    (I)  A=C union B, C={c0=0,c1,c2,c3}, bi=Y-2ci;
         all eight points distinct, and the common cubic value is Y.
    (II) A={0,c1,c2,c3,-2c1,-2c2,-2c3,X};
         all eight points distinct, and the common cubic value is 0.

The normalization in (II) translates the pure cubic center to zero.
There is no assertion that either form is realizable at h=0.

## 2. The internal B-edge restriction

This is the key validity-sensitive reduction; internal B collisions are
not dismissed merely because internal C cubics might be unique.

### Case I: no pure cubic

Use the tree with singleton base b0=Y. The fiber gives the three fixed
edges c0 -> cj with labels bj, j=1,2,3. The remaining four edge labels
are c0,c1,c2,c3. No additional edge can join two C-points: the fixed
C-star already contains their tree path. No additional edge leaves c0,
since that would create a fifth mark at value Y. No edge enters b0.

Suppose an additional B-edge has equation

    q = 2bj+b0-2bk-cl = 0,    j!=k.

Put Ri=2ci+bi-b0=0. If j!=0 and l is neither 0 nor j, then

    -q+Rj-Rl = 2cj-cl-bj-b0+2bk-bl = 0.                 (1)

All negative coefficients in (1) are >=-1, since bj,b0,bl are distinct
and C is disjoint from B. The coefficient of cj is 2. Thus (1) is a
nonzero balanced relation giving a rival, a contradiction.

If j!=0 and l=j, the same equations give

    3bj+cj = 2bk+2c0.

Its support pairs are disjoint, contradicting the 22/31 lemma. If l=0,
substitute b0=2ck+bk (as residues) to obtain

    2bj+2ck = 3c0+bk.

For k=0 this is the forbidden pair equality 2bj=b0+c0. For k!=0
the support pairs are disjoint, again contradicting 22/31. This last
argument also rules out l=0 when j=0.

Therefore every B-edge points from b0 to some bj, j!=0, and has a
nonzero C-label. In particular the B-edge subgraph is a star based at b0.

### Case II: one pure cubic

Write Bi=-2ci, i=1,2,3, and use the tree with singleton base c0=0.
The fixed edges are c0 -> ci with labels Bi. The four remaining
labels are c1,c2,c3,X. There is no extra edge out of c0, no edge into
c0, and no extra C-C edge.

An internal B-edge with label cl has

    q=2Bi+c0-2Bj-cl=0,    i!=j,  l in {1,2,3}.

With Ri=2ci+Bi-3c0=0, when l!=i the balanced relation

    -q+Ri-Rl = 2ci-cl-c0-Bi+2Bj-Bl = 0                 (2)

has every negative coefficient >=-1 and the coefficient of ci equal
to 2. It contradicts validity. When l=i, q+Ri gives

    3Bi+ci = 2Bj+2c0,

a disjoint 31/22 equality. Thus every B-B edge must have label X.
Labels are distinct, so there is at most one such edge.

These arguments are complete also when positive and negative B-terms
cancel: cancellation cannot create a negative coefficient below -1,
and the doubled C coefficient cannot cancel.

## 3. Complete structural coverage

Contract the three fixed C-star edges. In both cases this leaves a tree
on five vertices, with four remaining edges and four distinct labels.

In case I, choose the subset J of the three B-leaves joined directly
to b0. The connected B-cluster {b0} union {bj:j in J} attaches to the
C-block by exactly one cross edge; each remaining B-point is a separate
leaf attached to the C-block. Two cross edges into one cluster would
form a cycle, while no cross edge would disconnect it. Choose its
attachment point anywhere in the cluster. Each cross edge can attach
to any ci. Its orientation is free except that no edge enters b0
and no additional edge leaves c0. Assign the four C-labels bijectively,
rejecting label c0 on a B-edge. This is exactly structural_templates().

In case II, enumerate all 5^(5-2)=125 labeled trees by their Pruefer
words. Keep only trees with at most one B-B edge; such an edge must
have label X. Lift each C-block attachment to any of c1,c2,c3;
c0 cannot be an endpoint of an additional edge. Enumerate both
orientations and all bijective label assignments. This is exactly
pure_structural_templates(). All 125 tree words are checked distinct.

Additional local filters are necessary, never assumptions of validity:
the cubic marks 2source+base and 2destination+label on edges with a
common source must contain at most four marks, at most one pure mark,
and no label equal to a foreign center. These follow from stage9.
Different destinations follow from the tree property. Rejecting these
violations cannot discard a valid h=0 instance.

## 4. Exhaustive quotients of each presentation, not all moduli

After eliminating the three fixed equations, the unknowns are
(Y,c1,c2,c3) in case I, and (c1,c2,c3,X) in case II. Each additional
edge contributes

    2point(source)+base-2point(destination)-point(label)=0.

Rows are ordered by their four labels. Modulo two they are Y-ci in
case I (c0=0), and the four separate coordinates in case II. Both
matrices are invertible modulo two, hence have nonzero odd determinant.

The eliminated B-variables have unit coefficients. In case I, translating
the base b0 to zero changes the remaining variables to
(-Y,c1-Y,c2-Y,c3-Y), an integral unimodular change. Thus the four-variable
determinant equals the full seven-tree determinant up to sign. In
case II no further change is needed. Hence

    184 <= |H| divides |det M| <= 2187.

The remaining variables generate H because the C-points and Y or X
belong to A. Therefore all possible realizations are primitive kernel
vectors Mv=0 modulo a determinant-divisor order, up to multiplication
by a unit. There is NO assumption of an individual unit difference.

The primary solver gives integer unimodular L,V with LMV diagonal,
verifying this identity and unimodularity for every large matrix. It
enumerates all primitive cyclic quotient vectors, including noncyclic
presentations. This uses stage6_path_quotients.py and its dependencies.

The independent solver factors det M, solves directly modulo prime
powers, and combines by CRT. If a cofactor is nonzero modulo p, M has
rank three there; its primitive kernel is a single unit orbit at each
requested p^e dividing det M, represented by an adjugate column with
its first unit coordinate normalized to one. Integer elimination with
three unit pivots proves this statement. Otherwise it enumerates the
projective kernel over Fp and lifts x to x+p^e z by solving

    Mz = -Mx/p^e modulo p.

Fixing z at the normalized coordinate to zero preserves its value one.
Every normalized lift is included exactly once. Earlier coordinates
remain divisible by p, not necessarily zero modulo p^e. CRT combines
these local unit normalizations; every primitive global unit orbit has
exactly one such representative. The solver checks Mv=0 explicitly.
This proves solver coverage, not merely equality of output counts.

Both solvers finally reject repeated points, nonunique pair sums, and
failure of 2Delta=Delta. No full eight-term validity check was reached:
every Sidon output already failed doubling closure. The earlier validity
lemmas are used to restrict the template family, not replaced by Sidon.

## 5. Reproducible bounded results

Run using standard-library Python 3:

    python stage10_fourway_templates.py
    python stage10_fourway_templates.py --pure
    python stage10_modular_audit.py
    python stage10_modular_audit.py --pure
    python stage10_kernel_controls.py

|Count|Case I|Case II|
|---|---:|---:|
|Labeled structural templates|81408|177408|
|Locally admissible distinct matrices|38808|87786|
|Matrices with determinant at least 184|19638|49062|
|Primitive cyclic quotient maps up to units|18747|46965|
|Distinct eight-point outputs, primary solver|10896|10475|
|Sidon outputs, primary solver|8660|8056|
|Sidon outputs passing doubling closure|0|0|
|Valid sets found|0|0|

All four runs have complete flags. Primary deadlines were 12 and 15
seconds, with recorded times 3.70 and 8.61 seconds. Independent deadlines
were 20 and 30 seconds, with times 4.06 and 29.00 seconds. Template hard
caps were 116640 and 395136. A slower rerun that hits a deadline must
be labeled incomplete, not silently treated as certification.

The independent solver matched all five template/matrix/map counters.
Without output-set deduplication it saw 14805 and 36729 Sidon maps;
all failed doubling closure. Output sets are deduplicated by identical
sorted residues, NOT classified up to affine equivalence. These counts
do not demonstrate diversity of valid examples; there were no survivors.

Sixteen fixed positive kernel controls, including noncyclic presentations,
checked 53136 vectors modulo 3 or 9 by direct enumeration. Orbit counts
matched exactly, including multiple orbits and empty primitive kernels.
An initial control requested p^e not dividing det M, outside the solver's
contract; controls were corrected and that precondition is now asserted.
The large runs only requested determinant divisors. No audit failure was
repaired by weakening a mathematical condition.

The independent audit shares structural generators and is not a formal
proof verifier. Its role is to reduce the risk of an integer-diagonalization
or kernel-enumeration error. The finite exclusion remains a computational
dependency with the explicit mathematical coverage proof above.

## 6. Remaining obstruction

Every remaining multiway cubic fiber has exactly three marks:

    no pure: C={0,c1,c2}, B={Y,Y-2c1,Y-2c2}, plus two free points;
    one pure: {0,c1,c2,-2c1,-2c2}, plus three free points.

The compensation arguments (1),(2) still apply to internal B-edges
whose labels are in C. They do NOT exclude B-edges labeled by a free
point. In the four-way case there were no free labels (case I), or only
one (case II). The additional free labels are precisely the obstacle
to recycling that complete template coverage as a three-way proof.

The single useful sufficient lemma remains: these three-way fibers are
impossible under odd h=0 and validity. This would give R3=0 and allow
stage8 to prove D=0. It is not proved by this stage. Alternatively a
realization would force a direct multiway quartic bridge.

Even that diagnostic lemma would not finish the original 248 bound:
at h=R3=D=0, Sigma>=53 remains open, as do the relevant h>0 cases.
The active goal is not marked complete. This workspace is not a Git
repository and has no configured remote, so no PR can be created.
