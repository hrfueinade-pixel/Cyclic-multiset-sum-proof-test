# Stage 47 paired-star track: avoidance is a genuine compression mechanism

2026-10-11. Companion report for the coordinator's Stage 47 work. The full
N>=248 proof remains OPEN. The main new theorem is a sharp cap TWO on paired
star companions avoiding the added label. This report does not exclude any
new arbitrary modulus, reclassify the Stage 45 558 assignments, or claim a
global allocation.

## 1. Two attempted proof routes and their exact gaps

Normalize an ordinary quartic triangle in an odd group to

    2x+b+c=2y+a+c=2z+a+b=0,
    A={a,b,c,u,v,x,y,z},  s=u+v.

All eight labels are distinct. Its paired star values are u and v. By
private centers every extra star word lies on B={a,b,c,u,v}. Under the
inherited conditional ordinary cap these extra words are nonordinary.

First attempt: remove the added label from a star companion and use the
quartic core's cap. This exactly handles companions CONTAINING u at value u.
It has no operation on a word avoiding u: its support is {a,b,c,v}, and
subtracting u produces a negative coefficient. Thus it supplies no cap on
the missing family and no global necessity statement.

Second attempt: use Stage 46's three-word parity relation on avoiding words.
The three ordinary star tails are u+b+c, u+a+c, u+a+b. Their sum D has
parity e_u. Any triple of words avoiding u has u-coordinate zero in its
parity sum. Consequently the stated parity obstruction is vacuous on ALL
triples drawn only from avoidance words. The cross-fiber obstruction also
requires a B-only quartic word L. If the triangle has no 31 companion there
is no such L: Stage 46 excludes 4/22, and the ordinary cap excludes a fourth
ordinary quartic. One cannot assume excessive compression creates that L.

These two failures motivated a small fixed symbolic experiment, never a
search over moduli or group elements.

## 2. Sharp cap two: a short simultaneous-collision proof

Consider two distinct quintic words M,M' at value u, both supported on
{a,b,c,v}, and suppose their v counts have the same parity. If all their
count parities agree, fixed-parity injectivity forbids equality: cancel
two from their difference to obtain a protected degree-at-most-two
collision. Otherwise their parity difference on the three coordinates
a,b,c has even weight, since both masses are five. Thus it consists of
exactly two coordinates; relabel them a,b. Use 2z+a+b=0 to form

    r=(M+M'+2e_v+e_a+e_b+2e_z)/2.                    (1)

The numerator has even counts at every coordinate. Every count is
nonnegative and its mass is (5+5+2+1+1+2)/2=8. Its doubled value is
2u+2v+(a+b+2z)=2s, so oddness gives value(r)=s. It omits x,y and u,
hence is not original. Reused labels and arbitrary overlaps cause no issue.

Therefore at most one avoiding companion has even v-count and at most
one has odd v-count: there are at most TWO avoiding companions. The
proof applies to ALL quintic words on {a,b,c,v}; its conditional application
calls them mixed because the ordinary quintic cap already accounts for the
three center words. It cancels only two, never three.

Together with Stage 46's at-most-two containing companions, each paired
star has at most FOUR mixed words, hence at most SEVEN words altogether
under the inherited ordinary cap. Stage 44's unique inverse gives distinct
star outputs, so the mixed representation-incidence sum over paired stars
is at most 4*C5star=8*C4triangle. This counts WORDS at existing outputs;
it is not a charge to newly distinct quintic values. Section 5's control
attains two avoiding words, so the avoidance bound is sharp.

## 3. A new hand restriction on avoiding 221 words

Odd cancellation of two gives

    x+y+3z=-2a-2b-c.                                  (2)

If a 221 companion avoiding u doubles two triangle labels, relabel them a,b.
Its singleton must be c or v. The two possibilities produce explicit rivals:

    u=2a+2b+c:   2u+v+x+y+3z = u+v;
    u=2a+2b+v:   c+2u+x+y+3z = u+v.

Both words have mass eight, nonnegative counts, and omit original labels.
No factor of three is canceled. Thus any surviving 221 companion avoiding u
must double v and one of a,b,c; its singleton is another triangle label.
This leaves six possible words, not six proven distinct outputs or six
simultaneously realizable words. The same assertion holds with u,v swapped.
The challenger independently checked the identity, nonnegativity and coverage.

## 4. Fixed symbolic inventory and simultaneous-pair experiment

There are exactly 52 nonordinary quintic words on {a,b,c,v}: shapes 5,41,32,
311,221 have counts 4,12,12,12,12. S3 on a,b,c leaves 14 orbits. Set
(a,b,c,v)=(2p,2q,2r,2t) and u=value(M). Then the triangle centers are
x=-q-r,y=-p-r,z=-p-q. This four-parameter model is SURJECTIVE for every
actual odd-group solution containing M: no odd unit or torsion-free premise
is used, since u occurs with coefficient one in its own equation.

All 6435 mass-eight count vectors are tested for formal equality to the
original coefficient vector. Exactly six assignments have direct rivals,
precisely those in Section 2. The other 46 have no identically equal rival in
this formal model. That absence is a DIAGNOSTIC, not a proof that any actual
group realization is valid, or that the entire small-order family survives.

For each of the 1035 pairs among those 46 words, keep the second relation
as an integer vector. The targeted test finds 726 positive rival identities

    2^j*(value(c)-value(allones))
      = k*(value(M_second)-u),   k nonzero integer.

Every supplied c is nonnegative, mass eight and non-original. Thus the 726
pairs cannot coexist with the core in a full-valid odd-group set. The 309
pairs without a retained witness remain UNEXCLUDED. A positive TWO-clique
cover partitions all 46 words by parity of the v exponent (sizes 30 and 16);
every pair within a block has a supplied rival certificate. This suggested
Section 2's much shorter hand proof. No maximum-clique, minimum-cover,
absence, or coverage-of-all-compression claim is inferred. Integer k is
multiplied, never canceled. The standalone checker verifies every identity
and the whole positive cover without importing either producer.
It additionally checks the short hand construction directly on ALL 56
quintic words on four labels: 588 unequal-parity pairs receive the stated
nonnegative rival and 204 same-parity pairs reduce to distinct words of
degree at most two. Thus the theorem does not depend on a maximum graph
calculation or on exclusion of the six individual assignments.

## 5. Counterexample to two tempting avoidance shortcuts

The unrestricted claims "a paired star has at most one avoiding companion"
and "two avoiding companions force a 31 word in their quartic core" are
BOTH FALSE, even under full validity and the three local multiplicity caps.

Take the raw ordered labels

    (a,b,c,u,v,x,y,z)
      =(2,202,20402,10,-598,-10302,-10202,-102).

After translating by 10302 use the eight distinct nonnegative points

    (10304,10504,30704,10312,9704,0,100,10200)
    modulo N=245633.

The raw quartic zero fiber consists of exactly the three ordinary triangle
words. It has NO 31 companion. The raw star at u=10 has those three lifts
and two additional words

    5a=u,       a+3b+v=u,

both avoiding u. The full 6435-word check finds the original word uniquely.
Counts are T3=60,T4=228,T5=592,h=24,R3=0. Total cubic multiplicity is at
most two; ordinary quartic and ordinary quintic multiplicities are at most
three. This is OUTSIDE the desired interval, has T4>88, and refutes neither
N>=248 nor the conditional global growth target.

### Elementary validity proof for the fixed example

Its coefficient model is

    a=2p,b=2q,c=2r,u=10p,v=8p-6q,
    x=-q-r,y=-p-r,z=-p-q,
    (p,q,r)=(1,101,101^2).

Mass-eight coefficient differences from the original lie respectively in
[-26,62],[-42,22],[-8,16]. If a raw sum equals the original integer sum,
successive reductions modulo 101 force each coefficient difference to zero.
The translated degree-eight sums and the target lie between zero and N-1,
so equality modulo N first gives equality as integers.

Write a candidate's counts as A,B,C,U,V,X,Y,Z. Coefficient equality gives

    A=9+(Y+Z)/2-5U-4V,
    B=(X+Z)/2+3V-3,       C=(X+Y)/2.

It also forces X,Y,Z to have the same parity. Using total mass eight yields
W=X+Y+Z=1+2U, so all three center counts are odd and positive.

* U=0 would give W=1, impossible.
* U=1 gives X=Y=Z=1. Then A=5-4V and B=3V-2 force V=1;
  all other counts equal one.
* U=2 gives W=5. Since Y+Z<=4, A>=0 forces V=0. But then
  B=(5-Y)/2-3<0.
* U>=3 gives A<=9+U-5U=9-4U<0, since X>=1.

Thus the original word is unique. This proof uses no numerical absence
search. The challenger independently audited the coefficient bounds and cases.

## 6. Global implication and missing necessity statement

The evidence distinguishes two explanations. Avoidance is NOT an artifact
that full validity or the local caps automatically remove: two avoiding
mixed words can coexist with a clean triangle core. The small quartic budget
must enter any proposed exclusion or allocation. The sharp cap two and
726 new simultaneous
pair restrictions are real but LOCAL. They do not show that compressed
quintic systems must encounter one of these pairs, do not handle fibers
without triangle cores, and do not count fresh quintic outputs.

The precise missing statement for this track is a budget-sensitive necessity
or allocation: under T4<=88, relate star avoidance incidences (including cores
with no 31 word) to globally distinct additional outputs or a nonnegative
eight-term rival. It must then combine with an argument for path/split and
mixed-only fibers. Neither part follows by assigning distinct charges to
individual companion words. The requested global inequality
T5>=156-h-R3 remains UNPROVED.

## 7. Reproduction and evidence boundary

    python -B stage47_star_avoid_probe.py
    python -B stage47_star_pairs.py
    python -B stage47_star_check.py

All three new runs complete in seconds. Producers enumerate only a fixed
52-word symbolic inventory, fixed same-star pairs and count words. No old
entry point, modulus sweep, historical timeout or longer search is used.
The checker imports no producer or historical helper. Checking is separate
code by the same agent plus a mathematical audit by the challenger, not an
independent human review or a formal proof-assistant certificate. Earlier
PRs remain unmerged; the coordinator incorporates this track in the new PR.
