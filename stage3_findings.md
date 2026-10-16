# Stage 3: collision coexistence and the remaining 248 obstruction

Research date: 2026-10-09. Earlier reports are preserved. No Lean,
external package installation, repository clone, researcher contact,
or external publication was used. A platform usage limit interrupted
the sustained session; elapsed wall time is not claimed as active work.

## 1. What changed, and what did not

The sufficient statement `|E4| >= 60` for valid non-antipodal eight-point
sets below 248 remains unproved. No counterexample to it was found.
The stronger statement `|E4| >= 63` also remains unproved.

Substantive additions, independently reconstructed by a separate checker:

1. An exact cubic-defect formula `k = h + R3`, measuring both failure of
   doubling closure of the difference set and cubic multiway overlap.
2. A sharp bound of seven antipodal pairs in `P=A+A`, with at most one
   squarefree--squarefree antipodal pair.
3. A global coexistence bound `F4 <= R3 + epsilon`: fourfold ordinary
   quartic fibers inject into cubic fibers, except for at most one
   four-cycle fiber. This is not merely a local multiplicity cap.
4. Throughout `187 <= N < 248`, eight non-type-22 representations in
   one quartic fiber are excluded. The odd case has an elementary finite
   classification with explicit witnesses; the even case has a stated,
   independently reproduced finite computational dependency.
5. Complete custom searches exclude 187 and 188. Modulus 187 also has
   a much smaller independent difference-template certificate.
   Together with the reconstructed elementary baseline, these give
   the computationally strengthened bound `N >= 189`.
6. Rigorous counterexamples distinguish marked from unmarked fibers
   and show why the cubic injection needs an even-modulus caveat.

These are contributions of this session relative to the earlier notes,
not assertions of literature novelty. The bounded literature check did
not establish that these lemmas have never appeared elsewhere.

## 2. Baseline and external dependencies

[Fonollosa v2](https://arxiv.org/html/2607.08366v2), Section 7, reports
free-set CP-SAT certification through n=7, including global minimum 124
for seven elements. This is not just certification of the fixed binary
family. We checked the text's scope, but did not obtain or reproduce the
CP encoding or an independently checkable certificate.

The all-n fixed-family theorem and the arbitrary cyclic-set conjecture
must be distinguished. The current
[author repository](https://github.com/jarfo/min-modulus) and
[formal conjecture source](https://raw.githubusercontent.com/google-deepmind/formal-conjectures/main/FormalConjectures/Arxiv/2607.08366/MinModulus.lean)
still present the arbitrary cyclic problem as open. Reading the latter
is not a formal proof check. The repository's additional abelian-group
minimum does not settle the cyclic conjecture.

Accepting the reported minimum 124, the antipodal quotient lemma proves
the eight-element antipodal case at 248. Our elementary baseline
`N >= 187`, new collision lemmas, and searches at 187/188 do not use
that external certification. Complete reconstruction of the foundations
and the elementary endpoint arguments is in Sections 2--4 of
[stage3_audit_notes.md](stage3_audit_notes.md).

Related modular subset-sum classifications, including
[Cambie--Gao--Kim--Liu](https://arxiv.org/html/2308.03748v1), do not cover
the cube excess here. The classification of
[minimal Waring decompositions of monomials](https://arxiv.org/abs/1201.2922)
assumes minimum rank; applying it to a nonminimal cyclic decomposition
would be an unjustified extension. Neither route supplied the missing
finite quartic bound. This was a bounded literature check.

## 3. Definitions and audited foundations

Translate a valid set to `A={0} union B`, with `|B|=7`, and put `s=sum B`.
Let S be its 128 subset sums, L2 its 29 subset sums of sizes at most two,
`Tj={2a+a1+...+a_(j-2)}`, and `Ej=Tj minus L_(j-2)`.

The replacement lemma is the foundation. If U is a subset of B of
size r and a multiset h on B of length l <= r+1 has its sum, assign
multiplicities `1-1_U+h` on B and `1+r-l` at zero. This is an eight-term
competitor. Validity forces h to be exactly U. Orienting equal subset
sums toward the larger subset proves injectivity; complementing gives
`S=s-S`.

Consequently `T4 intersect S=L2`. Low sums use doubled zero and padding
zero. A subset target of size at least three cannot have a repeated
four-term representation: deleting zeros leaves at most four terms,
so replacement forces the squarefree target, whereas a nonzero doubled
center repeats and a doubled zero leaves at most two nonzero terms.
Moreover `T4 intersect (s-T4)` is empty: two repeated four-term
multisets would concatenate into a rival eight-term multiset. Thus

    N >= 128 + 2|E4| = 70 + 2|T4|.

The target 60 is exactly `|T4| >= 89`; the stronger 63 is `|T4| >= 92`.
No inference from passing tests is needed for these identities.

If two different equal-length multisets u,v have the same sum, then
`u-v` must have coefficients at least two and at most minus two.
Otherwise baseline plus or minus this difference is a rival. Applied
to pair sums, this proves unique nonzero ordered differences unless
there is an antipodal pair. In the non-antipodal case, `|Delta|=56`
and all 36 unordered pair-multiset sums are distinct.

Two antipodal pairs would create a squarefree cross-pair collision.
For the one possible pair, translate it to 0,t with t=N/2 and project
to N/2. A quotient rival has h(0)+1 slots for the collapsed pair; using
zero or one copy of t corrects either lift error. A baseline lift
would have projected to the quotient baseline, so a rival remains a
rival. This proves valid quotient size seven and the stated conditional
antipodal result.

## 4. Exact cubic defect and the 187 certificate

For a non-antipodal A, let m_y count representations `2a+b=y`, and define

    |E3|=28+k,
    h=(1/2)|{delta in Delta: 2delta not in Delta}|,
    R3=sum_(m_y>0) binomial(m_y-1,2).

**Proved identity:** `k=h+R3`. Each of the eight sets `2a+A` has eight
points. Distinct sets intersect in at most one point by difference
uniqueness; the pair with centers a,d intersects exactly when
`2(a-d) in Delta`. Thus its pair-incidence count is `Q3=28-h`.
For every nonempty fiber, `m-binomial(m,2)+binomial(m-1,2)=1`, so
`|T3|=64-Q3+R3=36+h+R3`. Since `T3 intersect S=A`, subtract eight
to obtain the identity. Cubic complementary packing gives
`k <= floor((N-184)/2)`.

At 187=11*17, doubling has one nonunit orbit of length ten, two of
length eight, and four unit orbits of length forty. Negation preserves
the nonunit orbits and exchanges unit orbits in pairs: its required
exponent is five modulo ten and four modulo eight, which is impossible.
A symmetric 56-point doubling-invariant Delta therefore cannot exist:
nonunits supply at most 26 points, whereas any full unit-orbit pair
already supplies 80. Hence h>=1; packing forces `h=k=1` and `R3=0`.

There are only two outgoing doubling boundaries. A partial nonunit
orbit consumes both by negation symmetry, leaving unit orbits full or
empty, again impossible. The unit portion must therefore be one interval
and its negative on two exchanged cycles; nonunit cycles are full or
empty. If a in {0,1} selects the ten-cycle and b counts selected
eight-cycles, their interval length is `t=28-5a-4b`. Its terminal
difference is a unit, so scaling that realized difference to one and
translating its start to zero are justified. The unit portion is exactly
`{+/-2^(-j):0<=j<t}`. The two eight-cycles have four selection masks;
together with a this leaves eight templates, none omitted.

For each template, additional vertices beside 0,1 must belong to
`Delta intersect (1+Delta)`, and six of them must form a clique under
the allowed-difference relation. The standalone
[stage3_certificate_check.py](stage3_certificate_check.py) reconstructs
all eight templates without importing the search code. It verifies seven
proper five-colorings and independently checks **all 46,489 six-subsets**
across the eight candidate graphs. There are zero six-cliques. The
exceptional non-five-colorable graph has 17 vertices; all its 12,376
six-subsets are checked. Failed coloring is not used as a proof.

This is a small finite computational certificate for exclusion of 187,
not a theorem inferred from random sampling. Full structural proof and
auditor reconstruction are also in Section 6 of the audit notes.

## 5. Two aggregate collision restrictions

The following complete elementary proofs are in Sections 2--3 of
[stage3_collision_notes.md](stage3_collision_notes.md), independently
reconstructed in Sections 7 and 10 of the audit notes.

**Pair-sum theorem.** P has at most seven antipodal pairs, at most one
squarefree--squarefree (SS) pair, and at most four pairs total if SS exists.
Thus `|{2p:p in P}| >=29`. Double--squarefree tail edges must pairwise
intersect, hence form a star or triangle. A double--double pair removes
two possible star centers. An SS pair forces the edges to cross its
two-by-two partition, leaving at most two such edges. Two different SS
pairs, compared in both orientations, force a forbidden antipodal A pair.
The notes supply every cancellation case, not an assumed injection.
The bound seven is attained by binary A at N=256, so six is false.

**Coexistence theorem.** Let F4 count values with four ordinary
`2a+b+c` representations, where a,b,c are distinct. Let epsilon be one
if P has an SS pair and zero otherwise. Then `F4 <= R3+epsilon`.

An ordinary center cannot occur in any other representation at the
same value, by the positive-coefficient cancellation restriction.
Four centers leave four distinct tail edges on the other four points:
either a cycle or a triangle with a pendant edge. A cycle forces an
SS antipodal pair of center sums. Uniqueness of SS fixes the centers;
adding opposite-edge equations fixes 2x, leaving at most x and x+t.
Their full target is s=2x+t, so complementary disjointness permits
at most one cycle value globally.

A triangle-pendant hub h cancels to a cubic core
`y=2c_i+d_i` for i=1,2,3, using six distinct points. With the other
points h,z, its fourth equation is `2z+d_i+d_j=y+h`. Additional cubic
representations can only be `2z+h`, `2h+z`, `3z`, or `3h`.
The first three contradict pair uniqueness or squarefree triple
replacement; the last implies `2(z+h-c_i-c_j)=0`. It is impossible
at odd N, but a pure-hub representation may occur at even N. In either
case the ordinary core is unique.

If both remaining hubs lifted the same core, adding their fourth
equations gives `h+z+d_i+d_j+d_k+d_l=2y`. Equal tail pairs imply the
forbidden squarefree equality `h+z+d_i+d_j=2c_i+2c_j`. Different pairs
share one singleton d_i and give the rival
`s=5c_i+c_j+c_k+d_i`. Hence at most one triangle-pendant value charges
each cubic core, which contributes at least one to R3. This proves the
aggregate bound in both parities. For odd N the associated total cubic
multiplicity is exactly three.

## 6. A small-modulus restriction that is not a marked-fiber cap

Let f_x count distinct repeated quartic multisets of types 4,31,211,
excluding type22. For valid no-antipodal A and `187 <= N <248`,
`f_x <=7`. It is essential not to replace f_x by marked multiplicity r_x.

Complete proof, nine odd determinant rows, explicit repeated-difference
or subset-collision witnesses, and even enumeration specification are
in Sections 4--5 of the collision notes and Sections 13--14 of the
audit notes. The proof uses a genuinely cyclic restriction: if f_x=8,
the coefficient matrix is `[2I_q,*;0,3I+F]`, where F is the function
`h -> x-3h`. Its row-difference determinant satisfies

    N divides det(M)/4,
    det(M)=2^q 3^t product_cycles(3^ell-(-1)^ell).

Here q<=4, two-cycles are forbidden, and unique differences allow only
one incoming path. Differences generate the entire cyclic group because
the subset cube has 128 points and a proper subgroup below248 has at
most123; the adjugate identity therefore proves the divisibility.

Odd determinant exceptions are 189,205,243. The 205 permutation case
gives s=2x, forbidden. The remaining canonical completions at189/243
have explicit elementary difference/subset witnesses, independently
checked over all81 completions and 521,235 eight-term multisets.
The ten even determinant exceptions have250,736 completions,18,400
Sidon completions,507 injective-cube completions, and zero valid ones.
The latter507 are checked through all6435 multisets each. The separate
even checker includes both modular half-solutions and all common-value
translation classes; it reproduces every count without importing the
original configuration code. This is an explicit finite computational
dependency, not a certificate excluding all valid sets below248.

## 7. Concrete failed shortcuts, with validity proofs

### Exact-three cubic attachment fails at even modulus

Take `N=40000` and
`A={0,1,33,1089,20034,37822,39934,39998}`.
Cubic value zero has three ordinary representations and pure `3*0`;
quartic zero has four ordinary representations. At translated bases
37822,39934,39998 that quartic value is exterior. Thus restricting the
claim to exterior fibers does not rescue its even extension.

Proof of validity: label a=1,b=33,c=1089, d_a=-2a,d_b=-2b,d_c=-2c,
z=20000+a+b. A rival has coefficients c_i>=-1, <=7, with sum zero.
Its weighted condition is `F+20000*c_z=0 mod40000`, where
`F=F_a+33F_b+1089F_c`, `F_a=c_a-2c_d_a+c_z`, similarly F_b, and
`F_c=c_c-2c_d_c`. Each |F_i|<=16, so |F|<=17968<20000. Thus F=0
and c_z is even. Reduction successively modulo33 makes all F_i zero.
Write c_z=2k>=0 and u=c_d_a,v=c_d_b,w=c_d_c. The coefficient lower
bounds imply u,v>=k and w>=0, while
`c_0=2k-3(u+v+w)>=-1`. This forces k=0 and u=v=w=0, hence every
coefficient zero. This is a proof, supplemented by all6435 multiset checks.

### An exterior marked-fiber cap seven is false, even at odd modulus

Take `N=5833` and `A={0,243,351,363,365,369,405,729}`.
At exterior value1458 the markings `(center;tail)` are

    (0;729,729), (243;243,729), (351;351,405),
    (363;363,369), (365;363,365), (369;351,369),
    (405;243,405), (729;0,0).

The first and last are the same type22 multiset. There are seven
distinct multisets, eight markings, and six non-type22 representations.
All low subset sums are at most1134, proving exterior status.

For a complete validity proof, order `q_i=(-3)^i` for i=0,...,6 and
q_7=-729, with `a_i=(q_i+729)/2`. Every eight-term sum is between0
and5832, so there is no modular wrap. For rival coefficients, set
`P(X)=sum_(i=0..5)c_i X^i+(c_6-c_7)X^6`. Integer equality gives
P(-3)=0, hence P=(X+3)R with integral coefficients r_0,...,r_5.
Then `c_i=3r_i+r_(i-1)` (r_-1=0), `c_6-c_7=r_5`, and
`4 sum r_i+2c_7=0`. Thus c_7 is even and nonnegative, so sum r_i<=0.
Any negative r_i=-m requires a distinct positive predecessor at least
3m-1>=2m; r_0 cannot be negative. Positive mass would exceed negative
mass, contradicting that sum. Otherwise all r_i>=0 and the sum forces
all zero, then all c_i zero. This proves validity. Independent full
enumeration confirms it. This is not a counterexample below248.

Other concrete failures: binary N256 has T3=37,T4=93, refuting
`T4>=2T3+20` even without antipodes. The known collision at68 and the
shared-singleton collisions remain valid and rule out naive injection.
At all-three mixed radix, N6560, there are no cubic collisions but28
quartic identifications unexplained by cubic propagation/type22 marking.
The21-identification example instead has terminal radix two and N4373;
stage4_independent_check.py independently verifies both counts.
Thus controlling only propagated cubic collisions is insufficient.

## 8. Exact experiments and reproducibility

All accepted examples were checked through the6435 eight-term multisets.
No random candidates were generated in stage3. Counts below describe
their stated spaces, not hypothetical exhaustive searches elsewhere.

| Experiment | Candidate scope | Valid outcomes / status |
|---|---|---|
| Full187 search | all sorted normalized(0,1) extensions;3,493,404 valid six-prefixes;1124 seven-prefixes |0;COMPLETE,44.219s |
| Full188 search | same proved normalization;4,127,034 six-prefixes;20,542 seven-prefixes |0;COMPLETE,68.828s |
| Independent187 certificate |8 templates;46,489 six-subsets |0 cliques;COMPLETE |
| Ordinary q4 at247 |4*247^3 labelled parameter triples;22,134 balanced-passing tail pairs |0;COMPLETE,9.250s |
| Ordinary q4 at241 |4*241^3 labelled parameter triples |0;COMPLETE,7.922s |
| Fixed q4 range239/247/255 |25,095/25,935/26,775 parameter tuples |0;complete only within restricted ranges |
| Conditional255 prefix(0,1,3,7) |216 fifth branches;11,190 six-prefixes;4197 seven-prefixes |1 binary set;COMPLETE within this class,1.078s |
| Existing fixtures |15 distinct valid(set,modulus) pairs;no new draws |+17 growth passes; +20 fails at256 |
| Mixed radix |36 cyclic-rotation representatives with bases2 or3 |36 valid;not an affine-class census |
| New root models |3 specified sets at40000,60000,5833 |3 valid;T4-2T3 gaps102,108,96 |

The ordinary-q4 exclusions at241/247 do not exclude sets with smaller
ordinary fibers. The conditional255 search contains only one affine
class and is not a full search at255. Earlier fixture affine analysis
found ten nonbinary classes; repeated bases and unit scalings add none.
The new families have distinct collision signatures, but we do not
pretend the36 rotation representatives establish36 affine classes.

The initial120-second187 run timed out, then was superseded by a
completed continuation and a fresh complete run. Its TIMEOUT record
remains preserved. No timeout or empty restricted sample is called
infeasibility. No ongoing research process remains.

Run with standard Python3 in this directory:

```text
python stage3_search.py --N 187 --n 8 --seconds 120 --initial 0 1 --validate --checkpoint stage3_search_187_complete.json
python stage3_search.py --N 188 --n 8 --seconds 180 --initial 0 1 --checkpoint stage3_search_188.json
python stage3_triple_templates.py
python stage3_certificate_check.py
python stage3_full_fiber_check.py
python stage3_even_full_fiber_check.py
python stage3_four_fiber_search.py --N 247 --seconds 180 --validate
python stage3_growth_probe.py
python stage3_growth_probe.py --mixed-radix
python stage3_root_models.py
```

The full extension criterion, modular-root encoding, and normalization
proofs are in [stage3_search_notes.md](stage3_search_notes.md). The
independent template and full-fiber checkers do not import the original
search modules. Machine-readable outputs are the matching stage3 JSONs.

## 9. Single most useful unresolved lemma

The sharply testable candidate is, for valid non-antipodal eight-point
sets in the gap,

    |T4| >= 2|T3| + 17,
    equivalently |E4| >= 2|E3| + 4.

This is **unproved**, not a restatement of the desired quartic loss bound.
Since |E3|>=28, it would give |E4|>=60 and close the gap. The nearby
stronger constant20 is false as shown above; constant17 passes only
the explicitly bounded fixtures and constructions. There are no valid
subthreshold examples testing its conditional hypothesis.

The missing mechanism is control of **independent disjoint-tail quartic
identifications**, including mixed type31/type211 fibers and type22
markings. Cubic propagation plus the heavy-fiber coexistence theorem
does not bound this loss: all-three radix supplies28 such identifications
with zero cubic collisions. A proof must couple that loss to small
cyclic modulus, rather than merely impose a local multiplicity cap.
The failed fixed-form cover at247 also does not supply the coupling:
its verified174-coloring prevents a247-form clique certificate using
only the tested proportional balanced-relation rule.

The next concrete step is to classify these cross-component relations
and derive a charging inequality incorporating h,R3 and pair-sum
antipodes, or produce a counterexample to the growth lemma. The initial
CRT unit-difference derivation for three-prime moduli was not independently
audited or used; it must be completed before broadening normalization.

No PR could be created: the workspace is not a Git repository and has
no configured GitHub remote. No files were published externally.
