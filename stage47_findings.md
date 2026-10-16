# Stage 47: sharp star closure and a triangle-free global necessity

2026-10-11. Continues open, unmerged PR #18 at
archived-source, branch
research/stage46-proof-first-mixed-triangles. The local workspace is an
archive, not a Git checkout. All 328 base-PR blobs matched local bytes
before this round's edits. Earlier PRs are neither merged nor retargeted.

**The complete theorem N>=248 remains OPEN.** Equality at 248 is attainable.
No new arbitrary odd modulus is excluded. Discovery-only absence and old
timeouts retain their previous boundaries; the 558 Stage 45 assignments
have NOT been closed or reclassified.

Three proof/challenge agents and the coordinator read the required checkpoint
and Stage 37, 40, 41-46 reports before proposing new claims. This round proves
a sharp missing paired-star cap and a global necessity for nearly saturated
configurations WITHOUT ordinary quintic triples. It also gives actual
counterexamples to proposed intermediate shortcuts. Neither result is a
necessity theorem covering every excessively compressed system.

## 1. Target and hypotheses

Full validity means the all-ones count vector uniquely represents s=sum A
in nonnegative mass eight. Appending a squarefree word's complement proves
full same-degree protection against every other multiset, not just ordinary
opponents. Q_k and T_k denote squarefree and repeated values respectively.

The inherited exact packing is

    N>=56+|T3|+|T5|,       N>=71+2|T4| in odd order.

The remaining cases are odd 207<=N<248. In a hypothetical counterexample
|T4|<=88, and the target is |T5|>=156-k, k=h+R3, where |T3|=36+k.
The cubic total and quartic/quintic ordinary multiplicity caps are three.
None is transferred to weaker protected sets. Oddness permits cancellation
by two; cancellation by three is used nowhere in the new proofs below.

## 2. The added-label-avoidance gap is closed locally

Normalize an ordinary quartic triangle by translating its value to zero:

    2x+b+c=2y+a+c=2z+a+b=0,
    A={a,b,c,u,v,x,y,z},       s=u+v.

All eight labels are distinct. The paired star values are u and v.
Privacy of the ordinary centers x,y,z confines any other word at u to
{a,b,c,u,v}. A word avoiding u is consequently on {a,b,c,v}.

**Theorem (unconditional odd-group avoidance cap).** At most two distinct
quintic representations at u avoid u and all three private centers. At
most one has even count on v and at most one has odd count on v.

Proof. Take two distinct such words M,M' with the same v-count parity.
If their whole parities agree, fixed-parity injectivity forbids equality:
write each word as epsilon+2w, with w of degree at most two, cancel two
and use protected pair sums or point distinctness.

Otherwise their parity difference is an even nonzero vector on three
labels a,b,c. It is therefore e_a+e_b after relabeling. The count vector

    r=(M+M'+2e_v+e_a+e_b+2e_z)/2

is integer and nonnegative. Its mass is (5+5+2+1+1+2)/2=8.
Its doubled value is 2u+2v+a+b+2z=2s. Oddness gives value(r)=s.
It omits x,y and u, so is not the original word. Contradiction. This
proof allows every word shape and arbitrary overlaps. QED.

Stage 46 already bounds the companions CONTAINING u by two, through an
exact removal/addition inverse with the 31 words at the quartic core.
Under the conditional ordinary cap there are exactly three ordinary
lifts at u, so the WHOLE paired-star fiber has at most SEVEN words.
The same holds at v. This consequence retains the inherited small-order
caps; the avoidance theorem itself only needs full validity and oddness.

Across all paired-star outputs there are at most

    4*C5star = 8*C4triangle

nonordinary representation incidences. Stage 44's recoverable core and
added-label inverse proves output pairs disjoint. This counts words at
existing outputs, not fresh values, and does not assume distinct charges.

A second new hand restriction excludes avoiding 221 words that double
two of a,b,c. If u=2a+2b+c, then 2u+v+x+y+3z is a mass-eight rival;
if u=2a+2b+v, then c+2u+x+y+3z is a rival. Both use
x+y+3z=-2a-2b-c, obtained by cancellation of two. A surviving avoiding
221 must double v and one triangle label. No three is canceled.

The separate [paired-star report](stage47_star_notes.md) gives both proofs,
the exact hypotheses, and all supporting identities.

## 3. The cap two is sharp; useful triangle cores are not automatic

These are actual large-order full-valid controls, NOT sub-248 examples:

| Control | Odd N | |T3| / |T4| / |T5| | What it disproves |
|---|---:|---|---|
|Star with two avoiding words|245633|60 / 228 / 592|Avoidance cap one; two avoiding words necessarily create a 31 core companion|
|Path quintic triple|670617|62 / 244 / 664|Full validity plus all local caps necessarily creates a quartic triangle core|
|Split quintic triple|709785|63 / 250 / 685|The same triangle-necessity shortcut|
|Four mixed 32 words|7890481|64 / 260 / 733|Every mixed-only quintic output has at most seven repeated-quartic predecessors|

The sharp star control, in the displayed label order, is

    (10304,10504,30704,10312,9704,0,100,10200) mod 245633.

Before translation by 10302 it is
(2,202,20402,10,-598,-10302,-10202,-102).
Its quartic zero core has exactly the three ordinary triangle words and
NO 31 companion. At u=10 the two avoiding words are 5a and a+3b+v.
The companion report supplies an elementary coefficient and count proof
of validity, independently challenged against every case and nonnegativity.

The path and split controls have no quartic triangle cores, although the
path has a quartic PATH triple. Their generic coefficient models are
fully valid by a short parity/mass argument, detailed in the
[no-triangle report](stage47_no_triangle_notes.md). Thus useful triangles
are not a consequence of protection and the local caps alone. A proposed
necessity theorem must use the small quartic budget or other global data.

For the mixed-only control use four pairs
(2*53^i,-3*53^i), 0<=i<=3, modulo 53^4. Its target is the sum of the
eight labels. Equality with the target successively modulo 53 forces
2p_i-3q_i=-1 in each digit: the coefficient differences lie in [-23,17].
Thus p_i=1+3t_i,q_i=1+2t_i with t_i>=0. Total mass is
8+5*sum(t_i), so all t_i=0. This is an elementary validity proof.
Its zero quintic fiber consists exactly of the four words 3(2*53^i)+
2(-3*53^i). Removing either of each pair's labels leaves a repeated
quartic, so all eight labels are predecessors at this mixed-only output.
All quartic words have distinct values, hence there are no triangle cores.

Every control has |T4|>88. None refutes the conditional target. Separate
enumeration of all 6435 mass-eight words per control supplies arithmetic
support; it is not the proof or a search over moduli.

## 4. A global necessity that covers a no-core branch

There are 280 ordinary quintic words. If there are no three-ordinary
quintic fibers, at least 140 values represent these words. Therefore the
desired bound follows in this branch whenever k>=16. A remaining
counterexample WITHOUT ordinary quintic triples must have k<=15.

Let n1,n2,n3 count outputs with respectively one, two, three ordinary
words; let M5 count repeated outputs with NO ordinary word. Exactly

    280=n1+2n2+3n3,
    |T5|=140+(n1-n3)/2+M5.

Thus the general allocation obligation is

    M5+(n1-n3)/2 >= 16-k.                       (UNPROVED)

This exposes what the star cap does not cover: path/split triples on
different center triples and mixed-only outputs. It is an exact target,
not a growth bound inferred from the identity. For the no-triple branch,
16-k mixed-only VALUES suffice; a single-ordinary surplus can also help.

There is new NECESSITY beyond this bookkeeping. Let S5 be the ordinary
quintic collision pairs with disjoint three-label tails. Their two centers
are private. For fixed centers c,d and the other six labels B, the
complement operation

    (2c+U,2d+V) -> (2c+(B-V),2d+(B-U))

is an involution on equal-value ordinary pairs. Its fixed points are
EXACTLY the disjoint-tail pairs; all others occur in twos. Protected triple
sums and oddness permit at most one S5 pair for each unordered center pair.
Its output is q=(s+c+d)/2, recovering the center pair uniquely by protected
pair sums. Different S5 pairs therefore have distinct output values.
The complementary point s-q=(s-c-d)/2 is exactly a prescribed cubic hole
from Stage 40. This is a proved bridge to the earlier covering target.

In a perfect pairing of the 280 ordinary words, each center has 35 words,
each participating once. Nonfixed complementary pairs contribute even
incidences; hence the simple S5 graph on eight centers has ALL EIGHT
DEGREES ODD and at least four edges. More generally, if u_c counts
single-ordinary outputs centered at c, its S5 degree has parity 1-u_c.
Since sum u_c=n1, at least 8-n1 vertices have odd degree for n1<=8.

Packing in the no-triple branch gives N>=232+k, and yields:

| k | Possible N<248 | Quintic upper bound | Compulsory S5 structure |
|---:|---|---:|---|
|15|247|140|Perfect ordinary pairing; all degrees odd; at least four edges; M5=0|
|14|247|141|n1<=2; at least three edges|
|13|245|140|Perfect ordinary pairing; at least four edges|
|13|247|142|n1<=4; at least two edges|

Only in these k>=13 no-triple cases does N>=245 independently justify
cancellation by three. Availability of that unit is recorded, not used to
claim a completed exclusion. An all-odd-degree graph need not have a
perfect matching: K1,7 is a counterexample. Reused centers remain covered.

The two perfect-pairing branches also saturate the 3+5 packing, so
G\3A=s-T5. Reflecting Stage 40's 36 prescribed cubic holes forces

    (s+c+d)/2 in T5 for every c,d in A, with repetition.

These 36 midpoints are distinct. Every output must have two ordinary words
in the saturation branch. A representing word M cannot contain both c,d,
since 2M-e_c-e_d would be a nonnegative mass-eight rival with at most two
odd coordinates. At a diagonal midpoint c=d it must avoid c altogether.
The stronger saturated placement problem is therefore explicit; no
contradiction from these conditions is claimed.

The no-triangle report proves the complement inverse, the ordinary-pair
lift counts P4=4P3ordinary+S4 and P5=6P3ordinary+2S4+S5, and all overlap
conditions. These count WORD PAIRS, not separate fresh output values.

## 5. Failed global attacks and targeted experiments

First attack: ordinary-pair lift multiplicities force a triple. The exact
counts only give 20-k<=P3ordinary<=23 in the no-triple branch, compatible
with all k>=0. They do not force any useful core.

Second attack: local rival tests and ordinary-center privacy alone prevent
the required compression. A fixed new diagnostic partitions all 736
repeated quintic words into 141 abstract fibers, each with at most TWO
ordinary words. Every word appears once. All 2258 internal word pairs pass
the primitive-dyadic pairwise test; center privacy and fixed-parity
injectivity hold. Every fiber has an ordinary word, so M5=0 in this
relaxation. There are no triple fibers at all, making every Stage 44/46
triple-core restriction vacuous. This is NOT a cyclic set, nor does it
certify any value of k or the quartic budget.

Two saved cross-fiber equations show exactly why it is unrealizable:

    2a0+a1+a2+a3 = 2a1+a2+2a5,
    2a0+2a1+a6 = 3a1+2a5.

Their difference forces a3=a6. Equivalently the nonnegative mass-eight
rival is (1,1,1,2,1,1,0,1), whose difference from all-ones is the first
relation minus the second. No prime is canceled. Both equalities separately
pass the local test. The missing restriction is simultaneous cross-fiber
and cross-degree consistency, not another triangle-only local cap.

Third attack: the compulsory S5 parity pattern automatically yields a
nonnegative rival by signing its relation rows. A targeted 8000-assignment
slice fixes four disjoint center pairs and one first relation, then tests
only r=allones+sum sign_i*R_i, sign_i=+/-1. It succeeds for 2340 assignments
and fails for 5660. Three explicit failures and a positive rival are saved.
These failures refute this RESTRICTED FORMULA, not the existence of other
integer/dyadic rivals or full validity. The slice does not cover graphs with
reused centers and does not assume every compulsory graph is a matching.

The separate star experiment has 52 avoidance words, 14 S3 orbits, six
direct 221 exclusions, and 726 positive pair rival identities. A positive
two-clique cover by v-count parity suggested the short proof in Section 2.
The 309 pairs without a saved pair witness are not exclusions or valid
group models. No old search was rerun or historical timeout increased.

## 6. Sharply stated remaining lemma and delivery boundary

The full missing lemma is still the budget-sensitive GLOBAL allocation:

> For a full-valid eight-set in odd 207<=N<248 with |T4|<=88 and the
> inherited caps, prove M5+(n1-n3)/2>=16-(h+R3), or construct an explicit
> nonnegative mass-eight rival. Handle path/split triples with different
> centers, ordinary pairs with reused centers, and mixed-only fibers.

No distinct witnesses, disjoint image sets, or injective charges may be
assumed. Stage 44 proves such inverse statements only for its stated lifts.
The new star cap seven does not make all other quintic fibers star fibers.

A sharper next sublemma, supported by the new global necessity, is:

> In the perfect ordinary pairing branches (k,N)=(15,247) or (13,245),
> the compulsory all-odd-degree S5 graph, perfect ordinary pairing of all
> 36 midpoints (s+c+d)/2 with their omission restrictions, and |T4|<=88
> force either a nonnegative eight-term rival or one mixed-only quintic
> output.

That sublemma is UNPROVED. It would close those branches, not every odd
case. The explicit signed-sum failures show why parity is not enough;
nonnegativity and arbitrary graph shapes need an additional argument.

Standalone challengers import no producers. They check new star identities,
the abstract partition and its positive rejection, the fixed controls, and
the saved matching experiment. Wrong mass, original rivals, undeclared
factor-three cancellation and zero multipliers are rejected. Mathematical
claims were also challenged by a separate agent. This is AI-agent review
and separate implementations, not independent human review or a formal
proof assistant, and no novelty claim is made.

Check the shipped evidence without discovery:

    python -B stage47_independent_partition_check.py
    python -B stage47_independent_newclaims_check.py
    python -B stage47_star_check.py
    python -B stage47_independent_control.py
    python -B stage47_structural_check.py

Regenerate the NEW fixed diagnostics if desired:

    python -B stage47_local_partition.py
    python -B stage47_star_avoid_probe.py
    python -B stage47_star_pairs.py
    python -B stage47_no_triangle_probe.py
    python -B stage47_no_triangle_matching.py

No cyclic-set or modulus sweep, historical entry point, increased search
cap, merge or discovery-only promotion occurred. All processes terminate.
This separate report, proof-track notes and reproducible supporting files
are delivered in a new PR stacked on PR #18, with the full goal still open.
