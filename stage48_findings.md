# Stage 48: global compression must encounter a quartic triangle or quintic split

2026-10-11. Continues open, unmerged PR19 at
`archived-source`, branch
`research/stage47-star-closure-global-necessity`, itself stacked on PR18.
The workspace is an archive, not a Git checkout. The 352 PR19 base blobs
were checked before delivery; historical research reports are preserved.
A late Stage47 local audit addition is saved separately in
`stage48_stage47_audit_addendum.md`.

**The complete theorem N>=248 remains OPEN. Equality is attainable.**
This stage closes entire configuration branches, rather than an arbitrary
new modulus. No earlier PR is merged, no historical search is restarted,
and the 558 Stage45 assignments remain unclosed. Three proof/challenge
agents and the coordinator continued the previously read checkpoint and
Stage37,40,41–47 material.

The main new result is a global necessity using actual quartic compression:
every hypothetical valid eight-set in odd N<248 must contain an ordinary
quartic triangle or a genuine split-type ordinary quintic triple. Systems
with no ordinary quintic triples are excluded in full. Triangle-type and
path-type quintic triples alone cannot account for the remaining compression.
This is not an assumption that triangle cores cover all systems: the split
branch is explicit and still open.

## 1. Hypotheses and counts

Full validity means allones is the unique nonnegative mass-eight word at
s=sum(A). Adding the complement of a squarefree word proves its protection
against EVERY different same-degree multiset. Use this full protection
throughout, never a weaker protected-set condition.

Suppose for contradiction that N is odd and below248. The inherited results
give ordinary cubic, quartic and quintic multiplicity at most three, total
cubic multiplicity at most three, and

    N>=56+T3+T5,     N>=71+2T4,     T4<=88,
    T3=36+k,        k=h+R3>=0.

Here Tj means |T_j|. Let n1,n2,n3 count quintic outputs with one,two,three
ordinary words; M counts repeated quintic outputs with no ordinary word.
Let C4 count ALL three-ordinary quartic outputs, not just triangles. Let Pj
count unordered pairs of different ordinary degree-j words at equal values.
Let Sj count such pairs whose tails are disjoint. The ordinary word counts
at degrees3,4,5 are56,168,280 respectively. Thus exactly

    P5=n2+3n3=140-n1/2+3n3/2,
    T5=140+(n1-n3)/2+M,
    O4=168-P4+C4<=T4<=88,
    delta=N-56-T3-T5>=0,
    N=232+k+(n1-n3)/2+M+delta.

O4 counts ordinary quartic VALUE outputs. The formulas count pairs and
outputs separately; mixed words at an ordinary output do not make a new value.

## 2. The universal midpoint rival supplies the missing placement constraint

For each unordered label pair c,d, allowing repetition, put
q=(s+c+d)/2. Its reflection (s-c-d)/2 cannot be a cubic multiset value:
a degree-three word W there would give the nonnegative mass-eight rival
2W+e_c+e_d at s. This word has at most two odd coordinates, so cannot
be allones. The 36 midpoint values are distinct: full protected pair sums
handle squarefree pairs and collisions with repeated pairs, while oddness
makes 2c=2d imply c=d.

Suppose q has two ordinary quintic words O,O'. Their doubled centers are
private in the whole fiber, so coordinatewise O+O'<=2. Then

    r=2*allones+e_c+e_d-O-O'

is integer, nonnegative, has mass eight and value s. Validity forces
O+O'=allones+e_c+e_d. If c=d this is impossible: its c coordinate is
three. If c!=d it forces the centers to be precisely c,d and the six
tail labels to occur once each. This is exactly an S5 pair. No third
ordinary word can occur: every other label already appears in those two
words and therefore cannot be a third private doubled center.

Consequently EVERY one of the 36 midpoints is either an S5 output, a
single-ordinary output, a mixed-only output, or outside T5. The disjoint
sets 3A and s-T5 leave exactly delta group elements uncovered. Since
every reflected midpoint is outside3A, at most delta midpoint values are
outside T5. Recovering the center pair from an S5 output proves uniqueness,
including when different pairs reuse labels. Therefore

    36<=S5+n1+M+delta.                            (A)

This is the new structural coverage step. It is not inferred from local
caps or a chosen allocation of distinct witnesses. Nonnegativity in the
rival is explicit; no factor three is canceled.

## 3. Quartic compression and midpoint coverage close the no-triple branch

Ordinary pairs have private centers. Removing their common tail labels
gives a recoverable inverse. At degree four, a pair either has one shared
tail label and descends to a cubic pair, or has disjoint tails. A cubic
pair uses four labels, leaving exactly four one-label lifts. At degree
five, intersection size2,1,0 gives respectively a cubic pair with six
two-label lifts, a disjoint-tail quartic pair with two one-label lifts,
or an S5 pair. Hence the exact inherited pair identities are

    P4=4P3+S4,
    P5=6P3+2S4+S5=(3/2)P4+(1/2)S4+S5.           (B)

Pairs in a triple fiber are counted separately; no pair is lost and no
distinct output is inferred from a lift. Since O4<=88, P4>=80+C4.
Combining (A),(B) with Section1 gives

    n1/2+3n3/2+M+delta>=16+3C4/2+S4/2,
    2N>=496+2k-4n3+3C4+S4.                       (G)

If n3=0, every term on the right after496 is nonnegative, contradicting
N<=247. **Thus the entire no-three-ordinary-quintic branch is closed.**
This handles systems with no useful triangle core, including mixed-only
outputs, without assuming that a mixed-only output must exist.

## 4. Paths cancel; the surviving weighted obstruction is precise

Classify a three-ordinary quartic fiber by its three tail edges on the
five noncenter labels. Classify a quintic fiber by its three omitted
edges there. The exhaustive graph types are triangle,star,path,split.
Write c=C3ordinary, t=C4triangle, p=C4path, w=C4split, q=C5split, and
E=S4double, the number of two-ordinary quartic fibers with disjoint tails.
Recoverable common-tail removal and unused-label addition prove

    n3=c+2t+p+q,     C4=t+2c+p+w,
    S4=p+2w+E.                                    (C)

The existing maps C5triangle=c and C5star=2t are retained. The additional
maps C4star=2c and C5path=p have explicit inverses. A cubic triple uses
six labels, leaving two distinct star-quartic lifts. A quartic path uses
seven labels, leaving exactly one quintic-path lift. Removing the common
hub or common tail recovers the originating fiber uniquely. Caps ensure
there are precisely three ordinary words at the lifted output.

**Stage44 erratum:** its statement that path and split quintic triples
both have no common tail label is wrong for paths. Omitted path edges
01,12,23 use four of the five labels; the unused label4 is in every tail.
Removing it yields quartic edges23,03,01, again a path. A split has no
common tail label. The Stage44 shared-center theorem and triangle/star
bijections are unaffected. Historical files are preserved with this explicit
correction at the current checkpoint.

Substitution of (C) into (G) yields

    2N>=496+2k+2c-5t+5w-4q+E.

In particular every remaining N<=247 counterexample requires

    5t+4q>=2+2k+2c+5w+E.                         (J)

If t=q=0 there is an immediate contradiction. Thus a remaining system
with NO quartic triangle must have genuine SPLIT quintic triples; path
triples cannot supply its compression deficit. Mixed-only fibers are
already included in (A) and in the exact packing slack, not omitted.

One sharply stated sufficient missing lemma is

    5t+4q<=2k+2c+5w+E                            (W48)

under full validity, odd N<248, T4<=88, and the inherited caps. **W48 is
UNPROVED.** It is a sufficient route to the original dichotomy, not an
equivalent restatement of the old quintic target. A proof must control
simultaneous triangle/split relations and output reuse using the actual
quartic budget. The quintic target T5>=156-h-R3 remains unproved in general.

## 5. Exact failed inferences and targeted evidence

The diagonal-only placement/center-parity argument gives N>=238+k when
n3=0, but leaves k<=9. It cannot close this gap without quartic information.
The stronger result (G) resolves it by counting cubic/quartic/quintic pairs.
The proof-track report records two earlier failed local/parity approaches
and the 90 fixed symbolic diagonal-pair cases that revealed the rival in
Section2. Every saved positive identity has multiplier ONE. No absence
search or cancellation by three is used as a premise.

An attempted triangle charge also fails: each triangle uses three ordinary
cubic pairs, but a cubic pair has four quartic lifts. Recoverability gives
only 3t<=4P3, not an injective compensation of the weight5 in (W48).
The paired-star cap seven bounds words at existing values, not fresh values.

The failure of a budget-free completion lemma is CONCRETE. The full-valid
set

    (0,101,303,707,1515,3131,6363,1) mod12827

has T3/T4/T5=43/127/260, h7,R3=0, c0,t7,w0,q0,E7 and all local caps.
W48 without its small-order/quartic-budget hypothesis becomes35<=21,
which is false. Modulo101 forces the last label's count to be one in any
mass-eight representation. The remaining seven labels are101 times the
binary seven-set in the group of order127. Translating that set by one
gives coins1,2,4,8,16,32,64. The only possible seven-coin target integers
are127,254,381; all have binary popcount7. A carry strictly reduces the
coin count, so there are no carries; only127 uses available binary digits.
This proves validity by hand. Separate implementations also checked all
6435 mass-eight words and the exact graph counts. T4=127>88, so the
conditional lemma and original248 target are NOT refuted.

A second diagnostic gives one scalar/center-graph record with N247,k6,
T3/T4/T5=42/88/149,P3/P4/P5=20/80/135,S4=0,S5=15,n1/n2/n3=22/123/4,
M=delta=C4=0. It satisfies the aggregate equations, midpoint coverage,
center incidence/parity, and (G). It assigns the four quintic triples split
type. **No group labels or tails are thereby supplied.** A new fixed
tail-consistency experiment rejects its chosen K8-minus-cycle cubic center
graph completely: all cubic pairs' four quartic lifts must be distinct at
each center or create a forbidden quartic triple. Producer and independent
checker exhaust this fixed symbolic graph in18 and44 recursive nodes.
Thus aggregate feasibility is not simultaneous feasibility. The supporting
proof track states the necessary common-neighbor reduction and exact scope;
this is not coverage of every compressed system.

The follow-up covers the entire equality case P3=20 when C4=0. No cubic
word can have two ordinary partners: that would be an ordinary cubic
triple and its star lifts would contradict C4=0. A center pair has at most
one ordinary cubic collision by protected pair/difference uniqueness.
Four distinct quartic lifts per cubic pair and only21 ordinary quartic
words per center give center degree at most five, so P3<=20. Equality
forces degree five at every center; the complement is a simple two-regular
graph on eight vertices, with exactly three possible cycle types:
C8,C5+C3,C4+C4. The common-neighbor tail reduction in the proof track
applies to all three. The two new classes exhaust in5 producer nodes each;
the independent fixed-order checker uses43 and40 nodes, independently
reconstructing the options, matching edge lists and option counts, and
checking the three-class coverage.

This supplies a targeted computer-assisted structural consequence:
**under the inherited ordinary quartic cap, C4=0 implies P3<=19.**
No assumption R3=0 is needed: a pure cubic companion cannot create a
second ORDINARY partner. With T4<=88, (B) then forces S4>=4 and
N>=250+k-2n3. The scalar pattern above is therefore rejected for every
possible center graph, not merely its first chosen graph. A different
scalar record has not been substituted as a putative realization. The
full weighted lemma remains open.

## 6. Reproduction, audit and boundaries

Read `stage48_no_triangle_notes.md`, `stage48_triangle_notes.md` and
`stage48_challenge.md` for the complete track arguments and challenges.
The standalone checks use Python's standard library:

    python -B stage48_saturation_diagonal_probe.py
    python -B stage48_independent_check.py
    python -B stage48_graph_lift_check.py
    python -B stage48_global_accounting_check.py
    python -B stage48_fixed_cubic_graph_probe.py
    python -B stage48_fixed_graph_independent.py
    python -B stage48_cubic_graph_family_probe.py
    python -B stage48_graph_family_independent.py
    python -B stage48_triangle_control.py

The independent overlap audit checks403200 midpoint presentations,
including89600 diagonal ones, and exactly560 allones exceptions, all S5.
It checks67200 shared-diagonal-center presentations and16800 nonnegative
cross-rivals, and all120 three-edge graphs and path-removal inverses.
The proof is the universal identities and inverses above; these finite
checks support it. Verification is by separate AI agents/implementations,
not a human review or formal proof assistant. No novelty claim is made.

The equality control A=(0,1,3,7,15,31,63,127) mod248 is independently checked
against6435 words. Translating by one gives eight binary coins through128;
possible targets255,503,751,999 all have popcount8, so no carries are
possible and only255 uses available digits. Thus strict N>248 is false.
The active goal's stale strict wording does not change the user's >=248
target. The goal is not marked achieved.

No modulus sweep, parameter sweep, timeout increase, Lean conversion,
historical search restart, or merge was performed. New fixed symbolic
diagnostics and declared positive controls are distinguished from the
still-open arbitrary odd207..247 exclusion and the Stage45 residual558.
