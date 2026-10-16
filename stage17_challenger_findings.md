# Stage 17 independent challenger: role coverage and arithmetic audit

Date: 2026-10-10. This note is agent-written. One bounded research round;
no historical computation rerun, modulus/set sweep, sampling, or novelty claim.

## 1. Independent coverage of the first two doubled differences

Assume all eight labels are distinct, A is valid in odd H, h=0, and

    X=2a+b+p=2c+b+q=2u+v+w.

Validity forbids a different equal-length replacement of a squarefree
subset: adding its complement gives an eight-term rival. Pair uniqueness
and oddness consequently imply nonzero ordered-difference uniqueness.

Write 2(a-u)=e-f, using h=0. Substitution gives

    e+b+p=f+v+w.

Literal multiset equality is impossible: two distinct left tails b,p are
disjoint from the two right tails v,w; the single point f cannot supply
both b,p. Thus neither side may be squarefree. Necessarily

    e in {b,p}, f in {v,w}.

For c the exact domain is e in {b,q}, f in {v,w}. These statements
cover all supplied partners, without assumptions about where partners
are preferred or available. There are 16 assignments. This derivation
was made before reading the local-proof agent's code or its derivation.
No freshness, isolation, MC, or Stage16 arithmetic enters this step.

## 2. Elementary reduction from 16 assignments to two

Let the negative labels of the a,c comparisons be f,g.

If f=g, subtracting 2(a-c)=q-p from the partner equations gives:

| positives for a,c | consequence |
| --- | --- |
| b,b | a=c |
| p,q | p=q |
| b,q | 2q=b+p |
| p,b | 2p=b+q |

Every row violates distinctness or squarefree-pair uniqueness. Hence
f!=g. If both positives are b, subtraction gives q-p=g-f. Difference
uniqueness contradicts four distinct p,q,f,g.

For a:(b,v), c:(q,w), translate u=0 temporarily. The equations are
2a=b-v and 4c=v-b, so a=-2c. Since
q=v+w-2c-b=w+2c, we obtain a+q=w, or before translation

    a+q=u+w.

Both pairs are squarefree and different, a contradiction. The other
three mixed-positive cases give a+q=u+v, c+p=u+v, or c+p=u+w.

Therefore only two assignments survive, related by swapping v,w:

    2(a-u)=p-v, 2(c-u)=q-w,

or their simultaneous v,w swap. For the displayed orientation they
force 2p+b=2v+w and 2q+b=v+2w. In particular the cubic u-marks
2u+p and 2u+q are already paired with centers a and c, respectively.
They may still be multiway; being paired does not exclude that.

This is a complete elementary restriction, not a complete exclusion.

## 3. Independent finite arithmetic cross-check of the initial domains

The separate implementation stage17_independent_check.py normalizes u=0
and uses coordinates (a,c,b,v,w), with
p=v+w-2a-b and q=v+w-2c-b. Thus it imposes all three base quartic
equalities identically. It imports no local-proof or historical kernel.

For each of the 16 covered partner assignments it adds its two integer
relation rows. It lists all 6434 distinct eight-term rival multisets and
solves row membership through a 2x2 minor, validating every coordinate.
An exclusion is accepted only if a positive power-of-two scale times
the rival-minus-target vector equals an INTEGER linear combination of
the rows. Odd denominators are never discarded or inverted in H.

The run completed in 0.75 seconds: 16 cases, 14 integer-certified
exclusions, and exactly the two elementary surviving assignments above.
The elementary reduction does not depend on this calculation; this
calculation supplies an independently implemented cross-check.

For each of the 14 accepted certificates, verification rejected a
coefficient changed by one, an odd scale of 3, the all-ones multiset,
and malformed eight-term counts. All 56 deliberate negative checks
passed. Every witness and both surviving necessary presentations are
preserved in stage17_independent_results.json. This is COMPLETE within
its 16-case scope, not a timeout and not a counterexample search.

## 4. Three forced-cubic branches and the transport obstruction

Isolation at X makes 2u+v and 2u+w unpaired. The elementary center
incidence identity therefore forces a multiway cubic Y=2u+ell at some
other singleton ell. Stage9's at-most-one-pure-mark result leaves THREE
branches: no pure mark; pure at u (ell=u); pure at z!=u.

If a different center d of Y is doubled in an opposing quartic
X=2d+R, with R a literal pair outside {u,v,w}, then write
Y=2d+s. Subtraction gives s+v+w=ell+R. If s avoided v,w, the left
would be squarefree and could not equal the right literally. Thus
s is v or w. If the opposite vertex is ordinary, R is squarefree,
forcing ell in R as well. These are restrictions on every possible
other center, not a choice of one partner.

The two ordinary opposing centers a,c cannot both occur in Y.
Otherwise their singleton labels must be v,w (a fixed singleton
cannot accompany two different centers at odd order), and subtracting
the quartic equalities gives q-p=w-v (or its swapped version), a
forbidden equality of ordered differences on four distinct points.
This is also a special case of the stronger Stage15
at-most-one-opposing-center result across all quartic types.

If the pure mark is at u, ell=u. Support separation then forbids
both a,c from Y because an ordinary opponent would require ell in its
tail pair. If the pure mark is at z!=u, z cannot be a or c: its
singleton s=z would have to be v or w, contrary to support separation.
It may still be an ordinary tail such as b,p,q. No-pure and pure-elsewhere
must not be conflated with pure-at-u.

Same-center transport cannot work in any branch. If X=Y+t, cancelling
2u yields v+w=ell+t. Pair uniqueness forces the literal pair {ell,t}
to be {v,w}; hence ell is v or w and the u-mark is unpaired, contradicting
the chosen multiway Y. This is an impossibility proof for that route,
not a proof that the entire target configuration is impossible.

## 5. Independent audit of the bounded two-direction closure check

Normalize w=0, write t=a-u and e=c-a, and use the surviving orientation.
The equations give b=-4t, v=4e, p=2t+4e and q=2t+2e. Thus the point
coordinates (u,t,e) are exactly

    w=0, u=(1,0,0), a=(1,1,0), c=(1,1,1),
    b=(0,-4,0), p=(0,2,4), q=(0,2,2), v=(0,0,4).

These were reconstructed independently from the elementary equations.
The checked directions are 2(v-w)=(0,0,8) and 2(b-w)=(0,-8,0).
Each is a nonzero doubled difference in odd H and must have one of
ALL 56 ordered distinct-point partners. Therefore the complete 56-role
domain per direction is proved; no local preferred-partner assumption
or cyclic modulus realization is needed.

The producer checks each single direction, leaving six and four roles;
it then checks every combination in the retained 6x4 domain. Every
excluded role has an eight-term forbidden-rival certificate. The
independent implementation reconstructs each row from the direction
and named partner, validates the saved point coordinates, and verifies
all 117 certificates using coordinatewise integer arithmetic. It also
checks the exact partition of each 56-role domain and all 24 retained
combined assignments. All checks passed. Changing one nonzero-row
coefficient, changing the scale to odd 3, supplying all ones, or using
malformed counts was rejected for EACH certificate: 468 negative checks.

Nine symbolic two-direction presentations remain. The computation is
complete within this necessary-condition scope, not a full h=0 check.
They are not valid counterexamples. The extra check of 327 unexpected
quartics at X found no dyadic certificate in these nine presentations;
that absence does not prove their exact quartic fibers in odd groups.
The independent arithmetic and coverage audit is recorded under
local_certificate_audit in stage17_independent_results.json.

## 6. Independent audit of the global all-ordinary cycle restriction

In the regular R3=0 branch, three distinct quartic vertices cannot share
a point: deleting that point gives three distinct repeated cubic marks.
If a deletion were squarefree, validity already forbids its equality.
Two distinct vertices cannot share two points, because cancelling both
would give a different pair representation.

An ordinary center appears in no other distinct vertex. Cancelling its
one copy from such a vertex and its own ordinary representation gives
a squarefree triple on the latter side; equality to a different repeated
triple contradicts validity. Two ordinary vertices with the same center
would instead violate tail-pair uniqueness.

An all-ordinary cycle of length L therefore has L distinct center points
and L distinct shared tail points. Its two distinct tail deletions give
the two incident edges. Reusing one edge point, whether on adjacent or
disjoint edges, would put it in at least three vertices. Hence support
has exactly 2L points and L<=4. The graph is simple, so L>=3.

For L=4, support is all eight points. The sum of the four literal count
vectors is twice the all-ones vector. If their common value is X, this
says 4X=2sum(A), so oddness gives 2X=sum(A). Twice any one of these
quartic vertices is a different eight-term representation of sum(A),
contradicting validity. All-ordinary cycles must therefore be triangles.

This is a complete new elementary structural restriction conditional
on R3=0. It does not assert Sigma>=53 or remove mixed-type cycles.
The independent challenger found no gap in the global agent's proof.
No finite computation, MC, or extra assumption on cycle supports is used.

The global agent's stronger restriction also passes independent audit:
an EVEN cycle without any 22 vertex is impossible. Pure vertices have
degree at most one, so such cycle vertices are ordinary or 31. Write
them as 2y_i+x_(i-1)+x_i, where x_i is the shared deletion point on
edge i; for a 31 vertex its center is one of these edge points.
The repeated centers y_i are distinct. An ordinary center is private,
and two 31 vertices at a fixed value with the same center would be
identical. Alternating the quartic equalities cancels every edge point,
giving twice one squarefree subset of centers equal to twice the
disjoint complementary subset. Oddness cancels 2, contradicting validity.

Further global deductions independently accepted during this round:

* Three consecutive 31 vertices in a cycle of length at least four
  are impossible. Stage9's no-order-three-difference theorem excludes
  adjacent 31 vertices sharing their singleton; sharing their center
  would make them identical. Their orientation is therefore coherent.
  Translate the first edge point to zero to get centers/tails
  0,Y,-2Y,7Y. The first and third supports are disjoint. Stage8
  Lemma2.1 forces their center difference 2Y to have order five, hence
  5Y=0 by oddness. But 0+(-2Y)=Y+7Y is then a different squarefree-pair
  equality, contradicting validity.
* There is at most one 22 vertex at a quartic value by pair uniqueness
  and oddness. Stage8 Lemma2.2 makes every 31 vertex in a cycle
  containing it one of its two neighbors; thus there are at most two
  31 vertices. A cycle with L vertices and n_O ordinary vertices uses
  exactly L+n_O points, since every edge point is distinct and ordinary
  centers are private. With a 22, n_O>=L-3, so L<=5.
* Without a 22, even lengths are excluded above. A length-seven cycle
  would have at most one ordinary vertex by L+n_O<=8, leaving a run
  of at least six 31s; the preceding three-run exclusion forbids it.
  There can be no length above eight. Hence every regular quartic
  cycle has length 3, 4, or 5; every length-four cycle contains a 22.
* A length-five cycle without a 22 has exactly three ordinary and
  two 31 vertices. Support gives n_O<=3. A case with three 31s and
  two ordinaries, avoiding a three-run, has cyclic word 31,31,O,31,O.
  Its isolated 31 is disjoint from both other 31s; Stage8 Lemma2.1
  puts all three distinct centers in one coset of the unique order-five
  subgroup. Six distinct ordered differences cannot fit its four
  nonzero elements. Fewer ordinary vertices force a three-run; more
  ordinary vertices require at least nine support points.

These deductions retain their explicit Stage8/9 elementary dependencies.
The initially suggested exclusion of ALL even cycles had a gap for a
cycle containing a 22. The independent challenger identified this and
the global report was corrected. Such a length-four cycle remains an
unexcluded necessary type. No claim Sigma>=53 follows from these results.

One further length-four type was then excluded and independently audited:
22,31,O,31. A 31 adjacent to a 22 cannot share its center with the 22,
because cancellation would give a different squarefree-pair equality.
Thus write the two disjoint 31s as 3a+p=3b+q, with p,q the two 22 points.
Stage8 Lemma2.1 gives a-b order five. Translate b=0, put a=delta,q=t.
Then X=t,p=t-3delta; X=2p+2q gives 3t=6delta=delta, hence 15t=0.
The opposite ordinary center d has 2d+delta=t, so d=-t by oddness.
Since a=3t,d=-t,q=t, there is already the forbidden squarefree-pair
equality a+d=2q. The final global report uses this simpler direct proof.
Its explicit identity was independently checked coordinate by coordinate:
with r1=(3a+p)-(3b+q), r2=(2p+2q)-(3b+q),
r3=(2d+a+b)-(3b+q), and T=5(a-b),

    2(a+d-2q)=2r1-r2+r3-T.

The three-31 chain identity likewise checks exactly:
2(3x0-2x1-x2)+(3x1-2x2-x3)-5(x0-x2)=x0+x2-x1-x3.
These rows are genuine relations by the preceding elementary lemmas,
and no odd divisor is cancelled in either witness.

The final type-word ledger is independently accepted. Up to rotation
and reversal, length four leaves QOOO and QPOO, with support sizes
seven and six. Length five leaves PPOOO, POPOO, QPOOP and QPOOO,
with support sizes eight, eight, seven and eight, respectively.
Here Q=22,P=31,O=ordinary. These are necessary types, not realizations.
Stage5 degree bookkeeping then gives
3C=188+c2-I-t4-2t5, so C>=53 is equivalent to
I+t4+2t5<=29+c2. That inequality remains OPEN.

## 7. Final rank-forcing closure: independently verified complete coverage

For each of the nine rank-two presentations, take the primitive integer
cross product F of its two relation rows. This nonzero functional
annihilates both rows. The eight formal points span the three coordinate
directions over Q, so some point difference has nonzero F-value; signed
symmetry gives a difference d maximizing F(d)>0.

h=0 supplies 2d=d' for one of all 56 ordered distinct-point differences.
For every such partner,

    F(2d-d') >= F(d) > 0.

Thus the additional relation has rank three. This is a proved structural
reason for the final bounded extension, not an arbitrary extra search.
The implementation enumerated exactly 9x56=504 branches. The independent
checker reconstructed every functional, source maximizer (including its
deterministic tie rule), relation row, and branch partition. All 504 were
covered; all are rank three. No domain was removed by a mere rational
rank assertion.

498 branches carry integer dyadic eight-term forbidden-rival certificates.
Combined with the earlier 117, all 615 producer certificates were checked
independently; all 2460 deliberate corruption tests were rejected.
The six remaining full-rank determinants, independently calculated, are

    503, 489, 501, 483, 549, 531.

No odd denominator is cancelled to exclude these six branches. They
are handled by the elementary cyclic torsion argument below instead.

## 8. Independent audit of the elementary final-six torsion exclusion

Let M be the three-by-three relation matrix in a remaining branch.
Its adjugate implies det(M) annihilates u,t,e. Since w=0 and
t=a-u,e=c-a, these differences generate the actual difference subgroup
H. Cyclicity therefore gives |H| dividing |det(M)|. This does not
claim that an arbitrary relation matrix has a faithful cyclic realization.

Validity gives |H|>=128 directly: the subset sums of the seven points
other than w=0 are all distinct. An equality between different subsets
can be cancelled to disjoint subsets, oriented so the larger is on the
left, and padded on the shorter side with copies of w. This is a
different equal-length replacement of a squarefree subset and violates
validity. No R3 packing formula is needed for this lower bound.

Delta is closed under both doubling (h=0) and negation. If a prime p
divides |H|, projection of A to the cyclic quotient of order p is not
constant, because its differences generate that quotient. A nonzero
projected difference has a signed-doubling orbit of size at most
|Delta|=56. The independently calculated orbit sizes are:

| modulus p | order of 2 | signed orbit size |
| --- | --- | --- |
| 503 | 251 | 502 |
| 163 | 162 | 162 |
| 167 | 83 | 166 |
| 61 | 60 | 60 |
| 59 | 58 | 58 |

All exceed 56, so these primes cannot divide |H|. The factorizations
503, 489=3*163, 501=3*167, 549=9*61, 531=9*59 then leave |H|<=9,
contradicting |H|>=128. These elementary residue calculations are
independently reproduced in the audit output, not residue-set searches.

For determinant 483=3*7*23, omitting either factor 7 or 23 leaves
|H|<=69. Thus both occur, and H surjects to Z/7 x Z/23. Its projected
point differences generate both factors. There must be two points
differing in BOTH coordinates: otherwise every pair agrees in one
coordinate. Pick a pair with differing first coordinates; they share
their second coordinate. Any point with a different second coordinate
would need the first coordinate of both, impossible. Hence every point
would share one second coordinate, contrary to generation of the second
factor. This is the complete elementary rook-clique argument.

The resulting difference has order 161 in the quotient. The order of
2 modulo 7 is 3 and modulo 23 is 11, hence its order modulo 161 is
33. Negation is outside that orbit (already modulo 7), so the signed
orbit has 66 elements. This exceeds 56 and contradicts closure of Delta.
No assumption that a difference generates the whole group H is used.

Verdict: the final-six torsion exclusion is sound, independently audited,
and uses elementary cyclicity, validity, and h=0. It completes the local
exclusion when combined with the new finite certificates.

## 9. Final accepted claims and precise limitations

The displayed eight-distinct-point configuration is excluded. Its NEW
finite-computation dependency consists of the saved 615 dyadic witnesses
and complete role coverage, independently checked by a separate
implementation. Its six final torsion branches are excluded elementarily.
The exclusion itself needs no freshness, isolation, MC, Stage15/16
arithmetic, or forced-multiway argument; those are context for its use.

The global regular-cycle restrictions are complete elementary results
under R3=0. They do not establish Sigma>=53. The 31/ordinary endpoint
and other isolated-ordinary center defects remain separate open targets.
The full h=0=>D=0 and original N>=248 goals remain OPEN. No novelty
claim or valid counterexample is made. The bounded local calculation
completed, with no timeout and no further expansion after 504 branches.

Reproduce the independent check with standard-library Python:

    python stage17_independent_check.py

It checks the initial 16-role cross-check and, when the producer artifact
stage17_local_results.json is present, all producer witness identities,
all three coverage stages, and the final signed orbit calculations.
