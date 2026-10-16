# Stage 48: independent midpoint and boundary challenge

2026-10-11. The full N>=248 theorem remains OPEN. Equality at248 is allowed.
This challenger track independently checked the new midpoint identities,
the support-graph argument and the complement-involution boundary proof.
No cyclic set, modulus or historical search is enumerated here.

## 1. Midpoint ordinary-pair lemma: accepted, including nonnegativity

Let s=sum A and mu=s/2 in an odd group. Suppose a quintic midpoint

    q=(s+c+d)/2

has two different ordinary words O,O'. Their two doubled centers are
private under full validity. Consequently EVERY coordinate of O+O' is at
most two: each center contributes two and is absent from the other word;
all other coordinates are the sum of two zero-or-one tails.

Thus the explicit count vector

    r=2*allones+e_c+e_d-O-O'

is integer, nonnegative, and has mass16+2-10=8. Its value is
2s+c+d-2q=s. Validity therefore forces r=allones.

For a diagonal midpoint c=d, r_c>=2, so it cannot be original. Hence every
diagonal value mu+c has AT MOST ONE ordinary quintic representation.
No division by three or five, no disjointness assumption, and no unused
labels are needed. This statement is universal for full-valid odd eight-sets.

For c!=d, originalness requires O+O'=allones+e_c+e_d. The two private
centers have count two, so they must be c,d; the other six labels must each
occur once in the two tails. Thus a midpoint with an ordinary pair must
be exactly a disjoint-tail S5 pair with centers c,d. These original
exceptions must NOT be falsely declared rivals.

The standalone `stage48_independent_check.py` checks all90 saved diagonal
models with explicit unit multiplier ONE. It independently checks403200
finite count-vector overlap presentations, including89600 diagonals,
and classifies precisely560 original offdiagonal exceptions. This arithmetic
supports the hand lemma, not any residue search or new modulus exclusion.

## 2. Global midpoint coverage: accepted

Use the conditional small-order ordinary cap three. Let n_i be the number
of repeated quintic outputs with exactly i ordinary words, i=1,2,3, and
let M count outputs with none. There are280 ordinary quintic words, so

    T5=140+(n1-n3)/2+M.

Put k=h+R3 and delta=N-56-T3-T5=N-92-k-T5. Exact complementary packing
gives delta>=0 and describes the complement of3A as s-T5 together with
exactly delta additional residues.

Stage40 puts each mu-c outside3A. Reflection about s therefore puts the
eight DISTINCT values mu+c either in T5 or in these delta additional
residues. A squarefree quintic output cannot occur here: reflecting it
would give a squarefree cubic value inside3A. By Section1 each diagonal
in T5 belongs to a one-ordinary or mixed-only fiber. The output counts
are therefore genuine residue counts, with no reused charge:

    8 <= n1+M+delta.

Substituting the exact T5 identity and using delta>=0 gives the new GLOBAL
necessary condition

    2*(N-236-k)+n3-M >=0.

In particular every hypothetical odd N<=247 counterexample must satisfy

    n3-M >= 2k-22.

This is a necessary relation across ALL quintic outputs, not merely a
cap at a chosen star. It does not yet prove T5>=156-k.

If there are no three-ordinary quintic fibers, n3=0, then N>=236+k.
This already excludes that entire branch for k>=12 below248. All statements
retain the inherited cap-three hypothesis; they are not transferred to
weaker protected sets.

## 3. Equality in the no-triple bound is impossible: accepted

Suppose n3=0 and N=236+k. The global inequality forces M=0. The diagonal
coverage and packing identities then force

    T5=144, n1=8, delta=0.

Every diagonal midpoint is a distinct one-ordinary output, using all eight
such outputs. All28 other pair midpoints must be two-ordinary outputs,
because the36 pair midpoints are distinct, delta=0, M=0, and all one-ordinary
outputs have already been used by the diagonals. By Section1 each is S5.
Thus the simple S5 graph on the eight labels is COMPLETE, of degree seven
at every vertex.

Normalize s=mu=0 by translation by -s/8; eight is a unit in every odd
group. Let M_i be the unique ordinary quintic at diagonal value a_i.
Every quintic word at a_i omits i: otherwise removal of that label gives
a quartic representation of0=mu, whose doubling would be an eight-term
rival. Each M_i has support four, so the directed support graph has
exactly32 arcs i->j, with no loops.

For mutual arcs i->j,j->i, the word

    M_i+M_j-e_i-e_j

is nonnegative, has mass eight and value zero. Validity forces it to be
allones. Since M_i omits i and M_j omits j, this requires M_i to double j
and M_j to double i, with the remaining six tails disjoint. Each vertex
can consequently have at most ONE mutual neighbor.

There are28 unordered vertex pairs. At most four can be mutual, hence at
most28+4=32 arcs. Equality is attained, so all vertices have one mutual
neighbor and these four pairs form a matching. Each diagonal word's center
is its matching partner. Every label therefore centers exactly ONE of the
eight one-ordinary quintic words. Write this count as u_c=1.

Now apply complement duality to ordinary collision pairs with fixed
centers c,d and six other labels B. An equal pair with tails U,V dualizes to

    (U,V) -> (B\V, B\U).

This preserves equality and is an involution. Its fixed points are exactly
the disjoint-tail S5 pairs. Nonfixed paired outputs are distinct by
protected squarefree triple sums, and contribute two to the number of
ordinary paired outputs incident to c. There are35 ordinary words centered
at c, of which u_c are single outputs; hence

    35-u_c == degree_S5(c) modulo2.

At the claimed boundary this says34==7 modulo2, a contradiction.
This closes equality and proves, in the no-three-ordinary branch,

    N>=237+k.

Consequently that entire branch is impossible for k>=11 and N<248.
The proof does not assume every odd-degree graph has a perfect matching:
the matching above follows from equality in an explicit arc count.

## 4. Stronger quantified result: accepted

The proof agent subsequently derived a stronger inequality, which also
passes the challenger audit and supersedes the preceding no-triple bound.

First, ordinary words at DIFFERENT diagonal values have different centers.
Suppose M_i=2a_j+U_i and M_l=2a_j+U_l represented mu+a_i and mu+a_l.
Neither uses its own diagonal label. The equality

    U_i+a_l=U_l+a_i

is between different degree-four words: its left coordinate i is zero and
its right coordinate i is at least one. Full quartic protection forces
both words to be repeated, hence a_l occurs in U_i and a_i occurs in U_l.
Then M_i+M_l-e_i-e_l is nonnegative, has mass eight and value2mu=s, but its
coordinates i,l are zero. It is a rival. The shared center is impossible.
The independent checker covers67200 finite overlap presentations, including
16800 direct cross-support rivals; the other cases have a protected
squarefree quartic on at least one side. No parameter or prime is canceled.

Put d=N-236-k and m=M+delta. Exact counting gives

    n1=8+2d+n3-2m.

There are at least g=8-m ordinary diagonal words. Their centers are
different by the preceding injection. If u_c counts one-ordinary quintic
outputs centered at c, these g words initially give g odd center counts.
The remaining n1-g words can change the parity of at most n1-g centers.
Thus the number of centers with odd u_c is at least

    2g-n1 >=8-2d-n3.

Let v_c count three-ordinary outputs incident to center c, so sum_c v_c=3n3.
The number of ordinary collision pairs incident to c is35-u_c+v_c: a
two-ordinary word supplies one pair, a three-ordinary word supplies two.
Complement duality still acts on PAIRS, even inside triple outputs; its
fixed points remain exactly S5. Hence

    degree_S5(c) ==35-u_c+v_c modulo2.

Let E be the missing edges from the complete S5 graph. Then degree_E(c)
has parity u_c-v_c. At most3n3 center parities can be affected by the
triple incidences, so E has at least8-2d-4n3 odd-degree vertices.

Among36 distinct midpoint residues, every output with an ordinary pair is
S5 by Section1. All others lie among n1 single outputs, M mixed-only
outputs and delta slack residues. Therefore

    |E|=28-S5 <=n1+m-8=2d+n3-m.

A graph with |E| edges has at most2|E| odd-degree vertices. Combining the
last bounds gives the new GLOBAL necessary inequality

    3*(N-236-k+n3) >=4+M+delta.                    (G)

There is no matching assumption here. Negative intermediate lower bounds
remain safe lower bounds; no positivity is inferred from them. The
center injection concerns only the actual diagonal words, and the
parity-changing upper bounds explicitly allow all other words to reuse
those centers.

When n3=0, integer d satisfies3d>=4, so d>=2. Thus

    N>=238+k in the no-three-ordinary branch.

That entire branch is excluded for k>=10 under N<248. General inequality
(G) retains ALL three-ordinary fibers, including path/split types, and
all mixed-only outputs. It does not claim those counts are independent.

## 5. Quartic/quintic global coupling closes the whole no-triple branch

The coordinator's subsequent coupling is stronger than Sections2--4 and
passes the independent challenge. Let P4,P5 count ordinary equal-word
pairs at degree4,5, with pairs inside triple outputs counted three times;
let C4 count ALL ordinary quartic triple outputs, and let S4,S5 count
ordinary pairs with disjoint tails. These are not just triangle counts.

The audited pair-lift identities give

    P4=4P3ordinary+S4,
    P5=6P3ordinary+2S4+S5=3P4/2+S4/2+S5.

The number O4 of outputs carrying ordinary quartics is exactly
168-P4+C4. Thus T4<=88 forces P4>=80+C4, and consequently

    P5>=120+3C4/2+S4/2+S5.

At degree5 the exact ordinary-word count gives
P5=140-n1/2+3n3/2. ALL36 distinct pair midpoints, not merely the8
diagonals, reflect the Stage40 holes. Each midpoint in T5 either has at
most one ordinary word or is an S5 output by Section1; an S5 output has
exactly two ordinary words, because its complementary tails use all
remaining labels and cannot permit a third private center. Therefore

    36<=S5+n1+M+delta.

Combining these three inequalities yields

    n1/2+3n3/2+M+delta>=16+3C4/2+S4/2.

Since N=232+k+n1/2-n3/2+M+delta, the final global consequence is

    2N>=496+2k-4n3+3C4+S4.                         (H)

Every step counts actual outputs or complete ordinary pair inventories.
No disjointness of the mixed outputs, fresh lift allocation, distinct
witnesses or independent fibers is assumed. Tail intersections uniquely
specify the pair-lift inverse, which is why reused labels do not cause
overcounting. Ordinary cap three and the small quartic budget are used
at their stated places.

If n3=0, (H) gives N>=248+k+3C4/2+S4/2>=248. Thus the ENTIRE
no-three-ordinary-quintic branch is now excluded under odd N<248, for
every k. This genuinely resolves a global no-core branch, rather than
presuming that every counterexample contains a quartic triangle.

The general theorem still needs a restriction on the surviving n3 outputs.
One sufficient sharp missing lemma is

    4n3<=2k+3C4+S4,

which would finish N>=248 through (H). It is currently UNPROVED; it must
account for triangle/star, path/split triple outputs and all simultaneous
compression. Equation(H) itself only establishes a necessary tradeoff,
not that missing upper bound.

## 6. Path-lift correction and refined global necessity

The proof agent found a real error in Stage44's explanatory classification:
an omitted-edge PATH on four of the five noncenter labels does have a
common quintic tail label, namely the unused fifth label. Only the SPLIT
type uses all five labels and has no common tail label. The shared-center
rigidity theorem and the two already proved bijections are not invalidated,
but the statement that path/split both have no common label must be corrected.

Deleting the unique common label of a path quintic triple gives three
ordinary quartics whose tails are complementary two-subsets on four labels,
again a path. Conversely a quartic path uses seven labels; adding its unique
unused label recovers the quintic path. These inverse maps prove

    C5path=C4path.

A quartic star has a unique common tail hub. Deleting it yields an ordinary
cubic triple, which uses six labels and has two possible distinct hub lifts.
The inverse common-hub removal proves C4star=2*C3ordinary. These are
recoverable-output bijections, not unproved fresh-output allocations.

Put c=C3ordinary,t=C4triangle,p=C4path,w=C4split,q=C5split. Together with
Stage44's retained triangle/star maps, complete graph classification gives

    n3=c+2t+p+q,
    C4=t+2c+p+w,
    S4=p+2w+S4double.

The last identity counts zero disjoint edge pairs in triangle/star quartic
triples, one in a path, and two in a split; S4double counts the remaining
two-ordinary quartic fibers with disjoint tails. The independent checker
covers all120 three-edge graphs on five labels (10 triangle,20 star,
60 path,30 split), common-tail intersections and inverse path removal.

Substitution in (H) gives

    2N>=496+2k+2c-5t+5w-4q+S4double.

Thus every hypothetical odd N<=247 counterexample must satisfy

    5*C4triangle+4*C5split
      >=2+2k+2*C3ordinary+5*C4split+S4double.        (J)

In particular it MUST contain an ordinary quartic triangle or a genuine
split-type ordinary quintic triple. Path-only compression, and configurations
with neither type, cannot evade the global growth argument. This accounts
explicitly for a broad no-triangle branch: if quartic triangles are absent,
the surviving quintic triple must be the split type, not a path.

The remaining missing lemma can now be localized: rule out enough simultaneous
triangle/split compression to contradict (J), or prove directly that
2k+2c-5t+5w-4q+S4double>=0. This is UNPROVED. The local star cap seven
does not supply that aggregate inequality or an injection among other outputs.

## 7. Actual counterexample to an unconditional weighted finish

The proposed sufficient weighted inequality in Section6 is FALSE if the
small quartic budget is omitted, even under full validity and all local caps.
The proof-agent control

    A=(0,101,303,707,1515,3131,6363,1) modulo12827

has independently checked counts

    T3=43,T4=127,T5=260,h=7,R3=0,
    C4triangle=7,C5split=C3ordinary=C4split=0,S4double=7.

Its weighted triangle/split side is35, while2k+2c+5w+S4double=21. The
total cubic cap is two and ordinary quartic/quintic caps are three. Thus
the missing weighted lemma must USE T4<=88 or the small-order hypothesis;
full validity and the multiplicity caps alone cannot prove it.

Its hand validity proof also passes independent challenge. Projection
modulo101 forces the count on the added label1 to be one, since all other
labels are divisible by101 and the count lies between zero and eight.
The seven remaining labels divide to0,1,3,7,15,31,63 modulo127. Adding one
to each seven-term coin gives powers1,2,4,...,64 and target127 modulo127.
The possible positive multiples127,254,381 each have seven binary ones.
Any binary carry reduces coin count, so seven initial coins must use no
carry. Only127 is possible without unavailable higher powers, and it
uses each available power once. This proves full eight-set validity.

The standalone independent checker verifies all6435 mass-eight words and
all stated actual output and graph counts. This is ONE declared positive
cyclic control. T4=127>88 and N12827 are explicit boundaries; it does not
refute the conditional target or give a sub248 counterexample.

The proof agent also tested one fixed symbolic center graph K8 minus the
cycle012345670 under R3=0,C4=0,P4=4P3ordinary. Under those hypotheses, five
distinct cubic tails at a center produce five disjoint four-edge quartic
lift stars, covering20 of the21 tail pairs on the other seven labels.
The only uncovered pair joins the two inactive tails, forcing each active
star to include both inactive labels. This forces active tails to equal
the center's five graph neighbors; both ends' tails must therefore lie
among common graph neighbors. The necessity argument passes the audit.

`stage48_fixed_graph_independent.py` independently rebuilds the finite
options and checks that ONE graph with functional fixed-order bit-mask
recursion, obtaining COMPLETE_NO_ASSIGNMENT in44 nodes under a five-second
cap (the producer used MRV and18 nodes). This does not cover arbitrary
twenty-edge graphs, does not enumerate cyclic sets or moduli, and does not
finish the weighted conditional lemma. Only this declared graph is excluded.

## 8. Complete three-graph closure and its broader scope

The subsequent authorized targeted extension closes the entire cubic
twenty-pair scenario with no quartic ordinary triples. At a fixed center,
each ordinary cubic partner yields four distinct ordinary quartic tail
words. With C4=0, lifts from different partners cannot reuse one such word:
the original center and the two different opposing centers would otherwise
form three ordinary quartics. There are only21 two-label quartic tails per
center, so its ordinary cubic graph degree is at most five.

If P3ordinary=20, the degree sum is40 and all eight degrees must be five.
The simple graph's complement is two-regular. Its complete possible cycle
types are C8,C5+C3,C4+C4; no length-two cycle is possible in a simple graph.
The common-neighbor tail reduction from Section7 applies at every center.

`stage48_graph_family_independent.py` reuses the independently completed
C8 record, then checks exactly the other two classes with independent
functional fixed-edge-order bit-mask recursion. All three classes are
COMPLETE_NO_ASSIGNMENT: C8 took44 independent nodes, C5+C3 took43,
C4+C4 took40. Both new checks use five-second caps and complete almost
immediately. The separate producer's MRV node counts differ, as expected.
The checker verifies cycle-type coverage, independently reconstructs the
options, and matches the edge lists and per-edge option counts.

R3=0 is NOT needed for this consequence. C4=0 under ordinary quartic cap
three already forbids three ordinary cubics: their quartic star lifts
would give C4>0. Thus any ordinary cubic mark has at most one ordinary
partner, even if a pure cubic accompanies that pair. Different partners
at a center consequently have different active tails, and all preceding
degree and common-neighbor reductions still hold. Ordered-difference
uniqueness gives at most one ordinary pair per center pair.

The independently accepted computer-assisted statement is therefore

    under full validity, odd order, ordinary quartic cap3 and C4=0:
    P3ordinary<=19.

The cap-three hypothesis is essential to the statement's meaning: C4 counts
exactly-three-ordinary outputs, so C4=0 alone must not be exported to an
arbitrary setting that permits four ordinary words at an output.

Under the actual small quartic budget, P4>=80. The exact identity
P4=4P3ordinary+S4 then gives S4>=4. Substitution in the global bound (H)
proves the stronger conditional result

    when C4=0, N>=250+k-2n3.

This excludes the coordinator's earlier scalar-feasible N247,k6,n3=4,
C4=0 point by GLOBAL necessary relation: the bound gives N>=248. It does
not exclude all split systems or certify a cyclic realization of any
other scalar-feasible point. No residues, group parameters or historical
searches were swept. The proof is computer-assisted over exactly the
complete three graph classes forced by the new extremal assumption.

## 9. Rejected shortcut and remaining coverage

The proposed parity shortcut that equal parity of two diagonal tail shadows
always creates a rival is insufficient without checking originalness.
Swapped-center ordinary pairs M_a=2b+U,M_b=2a+V with complementary tails
can make the constructed word exactly allones. Section3 treats precisely
that case and derives a matching only when all arc counts are saturated.
An analogous four-shadow parity sum also requires a separate originalness
argument before it can be accepted.

The no-triple result is genuine global progress, but it does not handle
all possible counterexamples: simultaneous quartic-triangle or genuine
quintic-split systems remain. Triangle, path, split and mixed-only
outputs must all remain in the global bookkeeping. The Stage45 residual558
assignments remain unclosed. No historical discovery-only absence is promoted.

Only cancellation by two is needed for these midpoint and duality arguments,
and normalization uses the unit eight. Cancellation by three is legitimate
only after an independent N>=245 deduction; five remains a nonunit at245.

This is an independent agent's deductive challenge and separate arithmetic
implementation within this session, not a human or formal proof-assistant
review. It establishes the stated conditional branches, not the full248
theorem or literature novelty.
