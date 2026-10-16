# Stage 48 proof track: every remaining compression requires a star or split

2026-10-11. Continues the Stage47 findings and no-triangle report. The
complete N>=248 theorem remains OPEN. This report proves new restrictions
under full validity in odd groups, then derives a budget-sensitive global
bound covering all configurations with NO ordinary quintic triples.

The hand arguments use cancellation by two only. In particular the new
results do not depend on the availability of three in orders245,247.
All degree-four squarefree protection is inherited from FULL validity.

## 1. Midpoint rigidity: an ordinary pair must be the complementary pair

Let s=sum(A), mu=s/2, and let a count word represent its group value.
At q=(s+c+d)/2 suppose two distinct ordinary quintic words O,O' occur.
Their doubled centers are private. Consequently EVERY coordinate of
O+O' is at most two: a center occurs twice in its own word and zero in
the other, and every other coordinate has at most one in either word.

The count vector

    r=2*allones+e_c+e_d-O-O'

is integer nonnegative, has mass16+2-10=8, and represents
2s+c+d-2q=s. Full validity therefore forces r=allones, or equivalently

    O+O'=allones+e_c+e_d.

If c=d, the right side has count three at c, impossible since every
coordinate of O+O' is at most two. Thus EACH DIAGONAL MIDPOINT mu+c
has at most ONE ordinary quintic representation.

If c!=d, the two doubled centers on the left force them to be precisely
c,d. The other six coordinates have count one, so the tails are disjoint.
Thus any ordinary pair at an off-diagonal midpoint must be the S5 pair
with that same center pair. This proves the recoverable inverse directly;
it is stronger than a support-omission test.

The diagonal midpoint words also omit c entirely: otherwise removing
one c from a quintic word at mu+c would give a quartic word at mu,
whose doubled mass-eight word would be a non-original representation of s.

## 2. Different diagonal ordinary words have different doubled centers

Suppose distinct diagonal outputs mu+a_i and mu+a_l have ordinary words

    M_i=2a_j+U_i,  M_l=2a_j+U_l

with the SAME doubled center j. Each tail is squarefree of degree three,
and the entire word omits its diagonal label. Subtracting their equations
gives

    value(U_i+e_l)=value(U_l+e_i).

These two degree-four count words differ: the first has count zero at i,
whereas the second has count at least one. If either were squarefree,
its full protection would contradict this equality. Hence both repeat,
so l occurs in U_i and i occurs in U_l.

Now M_i+M_l-e_i-e_l is nonnegative of mass eight and value
(mu+a_i)+(mu+a_l)-a_i-a_l=s. Validity forces it to be allones.
Its doubled centers would therefore have to be l and i respectively,
as both words omit their own diagonal label. This contradicts their
common center j. Therefore the center assignment on ordinary diagonal
outputs is INJECTIVE. Reused labels and overlapping tails are allowed
throughout; it is full protection that proves the injection.

## 3. Global counting without triangle cores

Assume no quintic output has three ordinary representations. Let n1,n2
count outputs with one,two ordinary words, let M count repeated outputs
with no ordinary word, and put k=h+R3. There are 280 ordinary words, so

    T5=140+n1/2+M.

Let delta=N-56-T3-T5>=0 be the exact packing slack. As T3=36+k,

    N=232+k+n1/2+M+delta.

All eight diagonal points mu+a_i are prescribed cubic holes after
reflection. At most delta of these points can be absent from T5:
the disjoint sets 3A and s-T5 leave exactly delta group elements.
Every present diagonal midpoint is either single-ordinary or mixed-only
by Section1. If g counts ordinary diagonal outputs, then

    g>=8-M-delta.

This immediately yields n1+M+delta>=8 and hence N>=236+k. Equality
forces all eight diagonals ordinary singles and every off-diagonal
midpoint an S5 pair. But the following parity allocation improves it.

Put m=M+delta and d=N-236-k, so n1=8+2d-2m.
Let u_c count all single-ordinary outputs with doubled center c. The g
diagonal words have DIFFERENT centers by Section2. The remaining n1-g
single-ordinary words can change the parity of at most n1-g center counts.
Thus at least

    2g-n1 >= 8-2d

vertices have odd u_c (a negative lower bound is harmless).

There are 28 off-diagonal midpoints. If an off-diagonal point belongs to
T5 and has two ordinary words, Section1 identifies its S5 edge uniquely.
All other off-diagonal points are single-ordinary, mixed-only, or packing
holes. At least 8-g of the M+delta nonordinary/absent slots are already
used by the diagonals. Consequently the graph E of MISSING S5 edges has

    |E| <= (n1-g)+(M+delta-(8-g))
         = n1+m-8 = 2d-m.

The Stage47 complementary-tail involution gives degree_S5(c)=35-u_c
modulo two. Since degree_S5(c)=7-degree_E(c), the vertices of E with odd
degree are EXACTLY those with odd u_c. The handshake bound therefore gives

    8-2d <= number_of_odd_degree_vertices(E) <= 2|E| <= 4d-2m.

Hence the global necessary inequality is

    3*(N-236-k) >= 4+M+delta.

In particular d>=2, and EVERY no-ordinary-triple configuration satisfies

    N>=238+k.

This was an intermediate global necessity. It uses all 280 ordinary words, the
36 protected midpoint locations, and a proved center injection; no
triangle core, disjoint output allocation, or distinct-witness assumption
is needed. Thus in odd N<248 the no-triple branch must have k<=9 and
N>=238+k. The k>=10 no-triple branches are excluded. This does not exclude
configurations with path/split/star/triangle ordinary quintic triples.
Section6 supersedes the remaining no-triple branch by closing it completely.

The necessity also identifies the remaining dense graph. In a no-triple
case the S5 graph is the complete eight-vertex graph with at most
2d-m edges removed. For d=2, m<=2. This is a specific simultaneous
compression obligation, rather than a claim that local triangle caps
cover an arbitrary counterexample.

## 4. Two failed approaches and the targeted experiment

First attempt: perfect ordinary pairing has even representation count
at each output. In the characteristic-two group algebra, if e_j denotes
the elementary squarefree sum polynomial, the ordinary quintic polynomial
is e1*e4+e5. Perfect pairing therefore gives e1*e4=e5. Reflecting
complements and multiplying gives further identities, but at protected
degree-eight coefficients the partition counts are all even. No period
of a sumset or quantitative growth follows from these identities alone.
This approach stops at a real missing inference, not a computed absence.

Second attempt: for two ordinary words with tails U,V on their other six
labels B, any accompanying words M,M' whose parity sum is U+V admit
r=1_B+(M+M'-U-V)/2. Coordinates U+V are at most two, so nonnegativity is
automatic; the word has mass eight and represents s. This bounds local
companion parities, but it does not allocate mixed-only output VALUES.
The resulting local cap does not finish global growth.

The pivot tested one diagonal midpoint with label0, two ordinary centers
1,2, and distinct three-label tails on the other five labels3..7. There
are exactly90 ordered assignments. The new script
stage48_saturation_diagonal_probe.py checks nonnegative mass-eight rivals
in the span of the ordinary equality and the diagonal-midpoint equation.
All90 have a saved positive rival with multiplier ONE. Its two rows are

    R1=O-O',     R2=2O-allones-2e0.

Every saved rival is allones+R1-R2, which simplifies to the hand formula
in Section1. Thus neither rational kernels nor the script's declared
availability of two/three are premises of the theorem; only the hand
formula is needed. No modulus, group parameter, or historical assignment
was swept. The saved positive identities are arithmetic support for a
universal count-vector proof.

Run the targeted new diagnostic with Python3:

    python -B stage48_saturation_diagonal_probe.py

## 5. Intermediate stopping point, superseded by Sections6-7

At this intermediate point the conditional dichotomy was still unproved.
The intermediate necessity was explicit: a no-triple counterexample
has k<=9 and N>=238+k, with an S5 graph missing only the stated number of
edges; or it has ordinary quintic triples, including path/split triples
on different center sets. The quartic budget T4<=88 has not yet been
turned into a contradiction for these compulsory dense systems at that
point. Section6 subsequently supplies exactly that missing coupling and
excludes EVERY no-triple case. Section7 gives the current sharper remaining
obligation, so the no-triple branch is not presented as still open.

The new diagonal and center-injection lemmas were challenged separately
against private-center use, repeated labels, midpoint placement,
nonnegativity, original-word exceptions and output reuse. Verification
is by AI agents and separate arithmetic implementations, not independent
human review or a formal proof assistant. No novelty claim is made.

## 6. Stronger coordinator coupling excludes the ENTIRE no-triple branch

The coordinator supplied a stronger combination using the quartic budget.
The exact pair lifts from Stage47 give

    P4=4*P3ordinary+S4,
    P5=6*P3ordinary+2*S4+S5=(3/2)*P4+(1/2)*S4+S5.

Let C4 count three-ordinary quartic outputs and n3 three-ordinary quintic
outputs. The number of ordinary quartic output values is
168-P4+C4. Since T4<=88, P4>=80+C4. Also

    P5=140-n1/2+(3/2)*n3.

Section1 implies that all 36 midpoint outputs are allocated among the S5
outputs, single-ordinary outputs, mixed-only outputs, or the delta unused
packing points. A midpoint can never have three ordinary words, since an
ordinary pair there is S5 and its six tail labels leave no third private
center. Therefore

    36<=S5+n1+M+delta.

Combining these four exact inequalities gives

    N>=248+k-2*n3+(3/2)*C4+(1/2)*S4.           (G)

In particular, if n3=0, then N>=248. Thus ALL no-ordinary-quintic-triple
cases below248 are excluded, superseding Section3's weaker bound.
This uses the small quartic budget and accounts for every midpoint and
ordinary pair. It does not assert injective charges from individual words.

## 7. Path triples also cancel from the global obstruction

There is a correction to the Stage44 prose: a path-type quintic triple
DOES have a common tail label. If its omitted edges in B are01,12,23,
then B label4 lies in all three tails. Removing it gives tail edges
23,03,01, an ordinary quartic PATH. Stage44's claim that both path and
split types have no common tail label was incorrect for the path type.
Its proved triangle/star correspondences remain valid.

The correction yields a new exact bijection:

    C5path=C4path.

Every quartic path uses four of its five noncenter labels; adding the
unique unused label gives its quintic path. Conversely the common
intersection of the quintic path tails is exactly one label; removing it
recovers the unique quartic path. These inverses handle label reuse and
output injectivity under the ordinary caps.

There is also an elementary exact cubic-star correspondence:

    C4star=2*C3ordinary.

A cubic ordinary triple uses three private centers and three distinct
tails, leaving two labels. Adding either label gives a quartic star,
at different outputs. Conversely a quartic star's unique common hub
label can be removed, recovering the cubic triple. The other unused label
forces its second lift. Again every output has a recoverable inverse.

Put c=C3ordinary, t=C4triangle, p=C4path, w=C4split, and q=C5split.
The complete three-edge classifications on five labels and the inherited
Stage44 correspondences now give

    C4=t+2c+p+w,
    n3=c+2t+p+q.

A quartic path triple has one pair of disjoint tails, while a quartic
split triple has two. These unordered word pairs occur in their own
fibers and are therefore different across outputs. Thus

    S4>=p+2w.

Set E4=S4-p-2w>=0. Substitution into (G) proves

    N>=248+k+c-(5/2)t+(5/2)w-2q+(1/2)E4.

Consequently every remaining counterexample must satisfy

    5*t+4*q > 2*k+2*c+5*w+E4.

In particular it must contain an ORDINARY QUARTIC TRIANGLE or a genuine
SPLIT-TYPE ordinary quintic triple. If both are absent, the global bound
already gives N>=248, including all path-only and mixed-only compression.

This is the required necessity argument for configurations with no useful
triangle core: if t=0, excessive compression MUST encounter a split-type
quintic triple, quantitatively 4q>2k+2c+5w+E4. No triangle core is assumed
to cover those split outputs, whose omitted edges use all five labels.

The full theorem remains open because simultaneous split fibers and the
budget-sensitive allocation around quartic triangles are not yet closed.
The concrete remaining obligation is now to contradict the strict last
inequality using the full-validity simultaneous relations, or produce an
eight-term rival. The path family is no longer an independent missing
compression channel in that inequality.

An equivalent sufficient missing lemma, stated without an output charge,
is the weighted inequality

    5*C4triangle+4*C5split
       <=2*(h+R3)+2*C3ordinary+5*C4split+S4double.

Here S4double=E4 is the number of disjoint-tail ordinary quartic collision
pairs not belonging to the unique disjoint pair of a path triple or the
two disjoint pairs of a split triple. Under ordinary cap three every
remaining such pair belongs to a two-ordinary quartic fiber, so this is
an actual nonnegative pair count, not a formal residual budget.

This weighted inequality is UNPROVED. If it held for full-valid eight-sets
in odd N<248 with T4<=88 and the inherited caps, the displayed global
bound would yield N>=248. A proof must constrain the star and split
systems jointly; it cannot infer this inequality merely from the new
necessity theorem. A count-only feasible diagnostic is not a cyclic set
and does not certify the realization of any proposed compressed system.

## 8. A scalar-feasible configuration fails simultaneous tail consistency

The coordinator's count-only diagnostic has N247,k6,h6,R3=0,
P3ordinary20,P480,C4=0,S4=0,P5135,S515,n1=22,n2=123,n3=4,M=delta=0.
All four quintic triples are assigned split type. Its ordinary cubic
center graph is K8 minus the eight-cycle012345670. These scalar values
satisfy the current counting inequalities. They are NOT a cyclic set,
group relation system, or evidence of an actual counterexample.

The targeted script stage48_fixed_cubic_graph_probe.py tests only this
fixed center graph for simultaneous cubic tails and ordinary quartic lifts.
Here is the complete necessity reduction, which does not use group values.

Each center c has five cubic partners, and R3=0 ensures five different
cubic words at c, hence five distinct active tail labels a. Each cubic
collision 2c+a=2d+b uses four distinct labels; adding any of the other
four labels e gives an ordinary quartic word 2c+a+e at c. If two different
cubic edges at c generated the same quartic word, their different opposite
centers would give THREE ordinary quartic words at one output. C4=0
forbids this. Thus the five four-edge stars on the seven possible tail
labels occupy twenty DIFFERENT two-label tail words out of21.

The two inactive tail labels p,q cannot generate their own edge, so pq is
the one missing quartic tail pair. Every active-to-inactive edge must be
present. The star owned by a is the only one able to cover ap or aq;
therefore it must contain both p,q. Its excluded labels d and b must be
active. Since the five partner labels d are exactly N(c), the active
tail set is N(c). Applying the same argument at the opposite center d
forces BOTH cubic tails a,b into N(c) intersect N(d).

For each of the twenty fixed graph edges the script chooses an ordered
pair of different common neighbors (a,b). It then generates the four
ordinary quartic tail pairs at either endpoint. A deterministic
minimum-options backtracking enumerates every consistent choice, rejecting
a choice exactly when one generated tail pair was already used at that
center. This is a necessary condition for the proposed FULL relation
system; not checking group values only enlarges the possible assignments.

The declared five-second run COMPLETEly exhausts the fixed graph in18
recursive nodes and finds NO assignment. No timeout enters the result.
The retained result includes all twenty edges and every option count.
It distinguishes the scalar-feasible explanation from actual simultaneous
quartic consistency; the tested scalar graph cannot realize the necessary
tail constraints. It is not coverage of all center graphs or all split
systems, and it does not prove the missing weighted lemma. In fact any
R3=0,C4=0 center graph with P3ordinary20 must be five-regular: degree at
most five follows from four distinct quartic lifts per partner and only21
ordinary quartic words at a center; the degree sum40 forces equality
everywhere. Its complement is a simple two-regular graph on eight
vertices, whose possible cycle types are C8,C5+C3,C4+C4. The retained
fixed experiment covers ONLY C8; the other two types are not closed here.

Run this new fixed diagnostic:

    python -B stage48_fixed_cubic_graph_probe.py

The additional stage48_graph_lift_check.py verifies all120 three-edge
graphs on five abstract labels and their recoverable common-tail removals,
with shape counts triangle10,star20,path60,split30. It also checks the
quartic disjoint-tail pair counts0,0,1,2 used in Section7. These are
finite count-vector/graph checks, not a cyclic-set or modulus search.

## 9. The new fixed graph test extends to three complete graph classes

After the fixed C8 test, the new targeted experiment was extended to
exactly the OTHER TWO necessary complement graph types C5+C3 and C4+C4,
each with the same new five-second cap. The original C8 record is reused
without rerunning it. The separate family script and JSON are
stage48_cubic_graph_family_probe.py and its results file.

All three complete tests have no assignment: C8 uses18 recursive nodes,
C5+C3 uses5, and C4+C4 uses5. None approaches its cap or leaves a timeout.
This closes the two graph types left open in the initial Section8 test.

The C5+C3 type also has a short hand contradiction. A vertex d in the
five-cycle part has three cubic partners in the three-cycle part. For
each such partner, its common neighbors with d are the same TWO vertices
of the five-cycle part. The three cubic tails at d must be different
because R3=0, but all must lie among those two labels, impossible.

Together with the necessary degree bound and full graph classification,
the completed three-class tail test proves the computer-assisted statement

    under R3=0 and C4=0, P3ordinary<=19.

This statement is conditional on full validity and the inherited ordinary
quartic cap. It is not the N>=248 theorem. It rejects the entire scalar
case P3ordinary20,R3=0,C4=0, not merely the coordinator's chosen C8 graph.
The fact that another count vector passes the scalar inequalities would
still not supply a cyclic example or simultaneous group realization.

The tests use complete option lists, deterministic propagation/backtracking,
and retained COMPLETE status. Their independent arithmetic/coverage review
is documented separately by the challenger; no failed discovery or
rational-kernel sample is an exclusion premise.

The challenger separately audited removal of the R3=0 hypothesis. C4=0
already forbids three ORDINARY cubic words at one value: their star
quartic lifts would give C4star=2*C3ordinary>0 under the quartic cap.
Thus an ordinary cubic word has at most one ordinary partner, even if a
pure companion makes R3 positive. Distinct partners at a center still
use distinct tails; pair/difference protection still makes the center
graph simple. Every degree and common-neighbor step above is unchanged.
The independently checked broader consequence is therefore

    full validity, odd order, ordinary quartic cap three, C4=0
       imply P3ordinary<=19.

Under T4<=88 this forces S4>=4 and, by (G),

    N>=250+k-2*n3.

The independent family checker reconstructs all three graphs, their
options and cycle-type coverage, with recursive node counts44,43,40.
It imports no producer. Its scope and result are recorded in
stage48_graph_family_independent.py and the companion JSON. This remains
a targeted computer-assisted symbolic result, not universal exclusion
of all simultaneous split systems or a modulus search.
