# Stage 15 alternative route: singleton defects are two-vertex endpoints

Research date: 2026-10-10. One focused elementary round; no computation.
The diagnostic theorem h=0 => D=0 and the original 248 target remain
open. No novelty or valid counterexample is claimed.

Later root consolidation: Section 3.1 of stage15_findings.md supplies
a complete elementary four-case exclusion of the 22--31 opponent.
The THREE residual shapes recorded below were the boundary when this
alternative note finished; after that root proof only isolated22 and
isolatedordinary remain as opponents to a two-ordinary endpoint component.
That later proof was not independently audited by this agent.

## 1. Hypotheses and precise proved results

Assume A has eight distinct points, is valid in its odd cyclic
difference-generated subgroup H, and h=0. Use the elementary Stage9
absence of order-three differences, and the current (MC) theorem:

    Every entire quartic fiber coning a multiway cubic is connected.

MC has the Stage13/14 computational dependencies recorded separately.
It implies that a fresh quartic fiber X is pair-shadow: each repeated
cubic deletion has at most two marks in its fiber, and each quartic
propagation component is a path, cycle, or isolated vertex.

**Proposition 1 (exact singleton-defect shape).** If two distinct
unpaired literal deletion marks 2a+b,2c+b occur at X, their quartic
vertices are adjacent degree-one vertices. Their component contains
exactly these two vertices and is either:

    31--ordinary: 3a+b=2c+b+q, 3a=2c+q;
    ordinary--ordinary: 2a+b+p=2c+b+q, 2a+p=2c+q.

The supports have respectively four or five distinct points.
Conversely each such two-vertex component exhibits the singleton
defect. There is no 31--31 singleton-defect case.

**Proposition 2 (same-singleton transport is impossible).** The
multiway fiber forced by the singleton incidence identity cannot
cone X through a mark having that same singleton b. Transport,
if it exists, must change the singleton label. This is a proved
obstruction to the naive transport route, not to D=0 itself.

**Proposition 3 (one opposite type excluded).** A fresh two-ordinary
component cannot be opposite a three-point pure-plus-ordinary
component. A complete sixteen-case elementary proof is below.

After Proposition 3, an opposite component to a two-ordinary
component has only four support/type possibilities before using
the companion Stage15 order-seven theorem: isolated 22, 22--31,
isolated ordinary, or a three-31 cycle on an order-seven block.
The elementary order-seven-block exclusion in stage15_findings.md
removes the last case, leaving THREE residual shapes. None is
asserted to be realizable.

## 2. Exact endpoint proof: all literal deletions are handled

Write the two quartic representations producing the unpaired marks as

    X=(2a+b)+t_a=(2c+b)+t_c.

The centers a,c are distinct, since doubling is invertible. Neither
is b: a pure cubic 3b is paired by the singleton-base spanning tree.
The two quartic multisets are distinct. If they were identical,
cancel b; the resulting literal cubic multisets 2a+t_a and 2c+t_c
would be identical despite different repeated centers, impossible.

The quartics share b. Deleting b supplies a propagation edge:

    2a+t_a=2c+t_c.                                    (1)

Their different cubic multisets are repeated, as required. Neither
t_a nor t_c can equal b. Otherwise one side of (1) would be one of
the assumed unpaired marks, contradicting its new partner.

Thus the quartic vertices are 31 or ordinary, not 22. Deletion of
t_a yields the unpaired mark 2a+b, while deletion of b yields
the paired mark in (1). These are the only relevant repeated
cubic deletions. By MC that paired mark has exactly one partner.
Hence the first vertex has degree one; so does the second. Their
component is precisely this one edge.

If both vertices were 31, they would be 3a+b and 3c+b, giving
3(a-c)=0, forbidden by Stage9. If one is 31, the other is an
ordinary 2c+b+q. Its center c avoids the first vertex's points;
q cannot be a, since 3a=2c+a would give a=c. Thus a,b,c,q are
four distinct points. If both are ordinary, center exclusion
and (1) ensure a,c,b,p,q are five distinct points.

Conversely, in a two-vertex component of either displayed type,
their paired deletions give its one edge; their other repeated
deletions are distinct unpaired marks with singleton b. No global
unpaired permutation or unique available pure partner is assumed.

## 3. The forced same-singleton multiway fiber cannot cone X

For singleton b the incidence identity is

    k_b=1+sum_(paired b-marks)(m_Y-2).

Two unpaired b-marks give k_b>=2, so some cubic fiber Y has at
least three marks and contains a mark 2p+b. The identity does not
determine Y. Suppose that this fiber could cone X, so X=Y+t
for a point t in A. Then

    X-b=2p+t=2a+t_a=2c+t_c.

The last two marks form the paired fiber in (1). Because X is
fresh, MC allows exactly these two literal representations.
Therefore 2p+t must be literally one of them. Its center is a
or c, and Y is respectively 2a+b or 2c+b. Both those marks
are unpaired, contradicting the chosen multiway Y.

Thus every multiway cubic containing singleton b is harmless at
X. This matches the earlier center-defect obstruction: the
multiway forced at an isolated ordinary's own center cannot
directly cone the fresh value either. A successful global argument
must transport through a different center or singleton, not merely
invoke the incidence identity again.

## 4. Two ordinary endpoints versus a pure three-point component

Suppose the two ordinary endpoints have value X=4z. An opposite
component with at most three points containing a pure vertex is
exactly pure-plus-ordinary. Translate z to zero and write it as

    0=4*0=2r+0+s, s=-2r.

Write the main endpoints as

    0=2a+b+p=2c+b+q,
    p=-2a-b, q=-2c-b.

The eight points 0,r,s,a,c,b,p,q are distinct by support separation
and ordinary-center exclusion.

For disjoint ordinary equalities, doubled-center uniqueness forces
2(r-a) to be a tail of the r-vertex minus a tail of the a-vertex.
This is Stage8's elementary six-point bridge precursor: subtract
the associated cubic equality from the quartic equality; a
squarefree triple would be forbidden unless both labels are tails.
Thus there are exactly four alternatives:

    A1: 2a=2r+b;
    A2: 4a=2r-b;
    A3: 2a=4r+b;
    A4: 4a=4r-b.

For center c the alternatives C1--C4 are the same four equations
with a replaced by c. No uniqueness of a pure-cubic partner is used.

Every pair of alternatives has the following elementary contradiction:

| |C1|C2|C3|C4|
|---|---|---|---|---|
|A1|a=c|a+q=0|c=a+r|r+a+q=0|
|A2|c+p=0|a=c|c+p=r|p=q+r|
|A3|a=c+r|a+q=r|a=c|a+q=0|
|A4|r+c+p=0|q=p+r|c+p=0|a=c|

All calculations use only division by 2 or 4 in odd H. For example:

* A1,C2 give a=r+b/2 and q=-r-b/2, hence a+q=0.
* A1,C4 give a=r+b/2 and q=-2r-b/2, hence r+a+q=0.
* A2,C3 give p=-r-b/2 and c=2r+b/2, hence c+p=r.
* A2,C4 give p=-r-b/2 and q=-2r-b/2, hence p=q+r.

The diagonal entries repeat points. Entries a+q=0 and c+p=0
replace a squarefree pair by two copies of 0. Entries c=a+r,
p=q+r, c+p=r, and their reversals give different pair multisets
after inserting 0 on the one-point side. The two triple entries
replace three distinct points by three copies of 0. Every entry
contradicts validity. This completely excludes this opposite type.

An audit correction is explicit: A2,C3 gives c+p=r, not the
incorrect triple identity r+c+p=0 initially suggested while
deriving the table. The saved proof uses the correct pair identity.

## 5. Complete remaining opposite-type classification

A two-ordinary component uses five points. Any opposite component
therefore has at most three support points; there can be no third
component, since every possible remaining component needs at least
two points, and a pure component needs at least three.

If the opposite component contains a pure vertex, pure pairing and
Stage9 make its partner an ordinary on three points. No other
vertex is possible on those points by center exclusion and pair
uniqueness. Proposition 3 excludes this case.

If it contains a 22 vertex 2r+2s, no different pure or 22 vertex
has that value by odd doubling and pair uniqueness. An ordinary
on at most three points would have its center t outside {r,s}
and tails r,s, giving 2t=r+s, forbidden. A 31 centered at r
or s would likewise give a squarefree-pair replacement. Thus
there can only be one 31, centered at a third point t with
singleton r or s. A fixed center cannot have two different
singleton representations at one value. The opposite component
is therefore either an isolated 22 on two points, or a 22--31
pair on three points.

If it contains ordinary vertices but neither pure nor 22, there
is at most one ordinary on three support points. Its center
cannot occur in a 31, leaving only its two tail points; a 31
on those points would force its doubled center equal the
ordinary doubled center. Thus it is an isolated ordinary.

The final possibility is a 31-only component on three points.
Each 31 must have a propagation neighbor because its pure
cubic is paired. It cannot have only two vertices: each one's
pure-cubic edge would have to delete its singleton; the shared
point would then be their common singleton, forcing an
order-three difference. It must have three vertices with
different centers. Their singleton labels are different from
their own centers. A two-cycle would give 3r+s=3s+r and
2(r-s)=0, so their orientation is a three-cycle:

    X=3r+s=3s+t=3t+r.

Translate r=0 and put s=delta. Then

    t=-2delta, 7delta=0, X=delta.

Because delta!=0, its order is exactly seven. This finishes
the four-way classification of residual opposite shapes.

## 6. Elementary restriction on the order-seven cycle case

### 6.1 General small 31-only components

The three-point classification extends to EVERY 31-only component
of a fresh fiber with at most five support points. Such a component
must be the same three-point order-seven triangle.

For a vertex 3a+b, its pure-cubic partner is unique by MC. Cone
that partner by b. A 31-only component forces the partner's doubled
center to be b, giving its successor 3b+q, where q=3a-2b.
The predecessor is unique as well: fixed b,q determine 3a=2b+q,
and Stage9 excludes two different pure centers with that value.
Different vertices have different centers at one quartic value.
Every propagation edge is a successor or its reverse; a shared
singleton would instead give an excluded order-three difference.
Therefore the component is one directed cycle, and all its
singleton labels are the next centers on that cycle. Its support
size equals its cycle length k.

Put delta_i=a_(i+1)-a_i. The successor formula gives
delta_(i+1)=-3delta_i. Summing around the cycle gives

    (1-3+9-...+(-3)^(k-1))*delta_0=0.

For k=2 this implies 2delta_0=0, impossible in odd H. For
k=3 it gives order seven. For k=4 it gives order five, but
four distinct points in that subgroup coset require twelve
distinct ordered differences where only four exist. For
k=5 it gives order61, because the alternating sum is61.
The multiplicative order of2 modulo61 is60: 2^30=-1,
2^20=47, and2^12=9 modulo61 exclude the three maximal
proper divisors30,20,12 of60. Doubling closure would then
put60 distinct multiples of delta_0 in the56-point Delta,
impossible. A one-vertex component is excluded by pure
cubic pairing. Thus only k=3 remains for support<=5.

This cycle-classification lemma alone does NOT exclude the
order-seven triangle. The separate elementary order-seven-block
exclusion in stage15_findings.md does so. That proof uses
validity and odd h=0, not MC, Stage9, or a computation. Thus,
after that companion theorem, no 31-only component of a fresh
fiber has support size at most five.

### 6.2 Projected five-point restriction

The three-point block J0={0,delta,-2delta} has six distinct
ordered differences, exhausting every nonzero element of
J=<delta>, an order-seven subgroup. Therefore each of the
other five A-points lies in a different nonzero J-coset.

Their five projected points form a VALID five-point set in H/J.
Indeed the three-term multisets drawn from J0 realize every
residue in J. In units of delta, examples for residues 0--6 are

    (0,0,0), (0,0,1), (0,1,1), (1,1,1),
    (1,5,5), (0,0,5), (0,1,5).

If a different five-term multiset of the projected outside points
had the projected all-ones sum, lift it using the corresponding
actual A-points. Its sum differs from the actual outside sum by
an element of J. One of the displayed three-term block multisets
corrects this difference to the eight-term target. Its outside
multiplicities differ, producing a rival eight-term multiset.
This contradicts validity and proves the projected-five assertion.

This is a structural restriction only. No published minimum,
finite search, or unsupported quotient-six validity claim is
used to exclude the case. In particular two-term block sums
miss one J residue, so a stronger collapse to a valid six-point
quotient would need a separate argument.

## 7. Dependency ledger and exact next obstacle

The elementary proofs use validity, odd doubling, global h=0,
pure-cubic pairing, Stage9, support separation, and the six-point
ordinary bridge. MC is the additional current computer-assisted
theorem needed to keep every fresh fiber pair-shadow. No new
computation, historical rerun, random sampling, or modulus sweep
was performed for this note.

The singleton-defect obstruction is now concrete, not merely an
incidence count. It is a 31--ordinary or ordinary--ordinary
two-vertex component. The pure-opposite type of the latter is
excluded completely here; its 31-only opposite is excluded by
the companion elementary order-seven theorem. Its remaining
THREE opposite shapes (isolated 22, 22--31, isolated ordinary),
and the opposite types for 31--ordinary, are still unresolved.

The incidence-forced multiway fiber at the SAME singleton cannot
transport directly to the fresh quartic value. This shows exactly
why the initial transport shortcut fails. It does not refute a
different-singleton transport theorem, D=0, or the 248 conjecture.
The most useful next lemma is to exclude the residual two-vertex
endpoint components using all singleton-base trees, or force
another coned multiway at their value with a different singleton.
