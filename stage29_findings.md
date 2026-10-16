# Stage 29: overlap at most five in every odd counterexample

Checkpoint, 2026-10-10. The universal N>=248 theorem remains OPEN.
This completes the new two-path family from Stage28 and supplies a
numerical restriction for the remaining odd h>0 forest budget.

## Strongest new result

**Computer-assisted theorem.** Every valid eight-point set with odd
cyclic difference subgroup H and |H|<248 satisfies

    |2A intersect(A+t)|<=5 for every shift t.

Stage27 excludes overlap seven/eight. Stage28 excludes any cycle in
an overlap-six partial doubling graph. This stage excludes all its
remaining two-path shapes. No h=0, R3=0, MC or external n=7 premise
is used. The theorem is necessary for a counterexample, not a proof
that no counterexample exists. Even groups remain outside its scope.

## Complete family and normalization

Translate B=A-t so an overlap-six map is b->2b. Stage28 leaves exactly
two paths of total eight vertices, with lengths L and8-L, L=1,2,3,4.
Thus for starts x,y it has the form

    B={2^i*x:0<=i<L} union {2^j*y:0<=j<8-L}.

The starts are nonzero and generate H, because the two paths contain
x,2x or y,2y, and their within-path differences include the respective
start whenever that path has length at least two. If L=1, the long
path gives y as a difference, and x-y together with y generates x.
Thus gcd(|H|,x,y)=1 in every case. Conversely the difference subgroup
of every distinct constructed set with this gcd is all of H.

Cubic packing gives |H|>=184, so odd H lies in185,187,...,247.
All starts x with gcd(x,n)=g can be multiplied by a UNIT modulo n
to obtain g. To see this prime-power by prime-power, write x=p^v*a
with a a unit when v is below the exponent of p in n, and choose a
unit multiplier congruent to (g/p^v)*a^(-1) modulo p^(e-v), where
p^e is that prime-power factor; it lifts to a unit modulo p^e.
If x=0 in a prime-power factor any unit works. The Chinese remainder
theorem combines these choices.
Equivalently units act transitively on elements of any fixed order.
Multiplication preserves validity and the partial graph.

Hence normalize x to a proper positive divisor g of n and let y range
over ALL residues with gcd(n,g,y)=1. This covers every possible pair;
the remaining unit stabilizer need not be factored out. We include
parameter sets with extra doubling edges as well: checking a superset
cannot omit an actual overlap-six case.

## Completed exclusion and saved identities

The producer checks all32 odd orders, all four path-length pairs,
all normalized first starts and every generating second start:71512
parameter cases. It discards constructed sets with fewer than eight
distinct points or fewer than56 distinct ordered differences; validity
already forces both conditions. It deduplicates by exact modulus and
sorted residue set, without an unproved affine reduction.

There are30204 distinct Sidon sets left. EVERY one has a checked
eight-term rival. The search omits each labeled point in turn and
uses eight layers of cyclic residue reachability to find eight terms
from the other seven points with the all-ones target. An eight-term
rival must omit some point: otherwise eight positive multiplicities
would all be one. Thus this search is exact for the validity target.
For exclusion, its saved positive witness alone is sufficient.

All30204 rival vectors are saved in stage29_two_path_results.json.
Each compact record is [n,L,x,y,count_string], with eight digits giving
multiplicities in the SORTED constructed set. The format is explicitly
recorded in the JSON. The starts reconstruct the full set exactly;
no candidate residue data or symbolic survivor was discarded. There
are zero survivors. The 30-second main run completed in about1.203s.
The evidence was compacted after execution without rerunning search.

A separate auditor imports no producer or historical code. It rebuilds
the coverage using divisors as point orders and iterative doubling,
lists all ordered differences, reconstructs every saved candidate from
its starts, and checks each rival using ordinary integer arithmetic:

    counts are nonnegative integers, sum counts=8,
    at least one count=0,
    sum_i (counts_i-1)*B_i =0 modulo n.

The independently rebuilt candidate set equals the saved set exactly;
per-modulus parameter and candidate counts also agree. All71512
parameters and30204 identities pass. Its 30-second main run completed
in about1.297s. It does not trust or replicate reachability search.
Separate implementations are by the same agent, not separate human
reviews or formal proof-assistant verification. No timeout is treated
as an exclusion, and this is not a sweep of arbitrary eight-point sets.

## Numerical consequence for the odd h>0 milestone

In Stage25's singleton-base forest T_b, the indegree at d equals
m_(2d-b)-1, where m_t=|2A intersect(A+t)|. Thus every indegree in
an odd counterexample is at most FOUR. Its row sum is7-s_b and
sum_b s_b=2h. Let P=sum_(b,d) binomial(indeg_Tb(d),2).

For a row with r edges, convexity gives the following upper bound by
putting at most four into a part before filling the next part:

|r|0|1|2|3|4|5|6|7|
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|Maximum incoming pairs|0|0|1|3|6|6|7|9|

Each entry is at most r+2, hence

    P <= sum_b ((7-s_b)+2) =72-2h.

The incidence identity counting overlap entries gives

    P=3 sum_t binomial(m_t,3),
    sum_t binomial(m_t,2)=28-h.

Indeed an overlap of size m gives m entries of indegree m-1, and
m*binomial(m-1,2)=3*binomial(m,3). These identities use only present
labels and odd difference uniqueness, not h=0 or R3=0. Therefore

    sum_t binomial(m_t,3) <= floor((72-2h)/3).

When R3=0, Stage18's incoming-pair/triangle bijection extends to the
present edges of the forests: the three quartic vertices still have
degree two and distinct shared labels. No missing direction is needed
in that construction. Thus the number u3 of triangles without22 is
at most floor((72-2h)/3). For h>=1 this is at most23. With R3>0, do
not identify incoming pairs with whole graph components or with Sigma.

This is a proved upper bound on incoming branching/short triangles.
It does NOT bound D or establish Sigma-D>=53-8(h+R3). In particular
long quartic components under missing doubling directions remain
uncontrolled. This is the precise remaining obstruction on this route.

## Reassessment and required next work

Stage26 settles h=0 below248. Stages27-29 sharpen the odd h>0 branch:
no overlap above five, forest indegree at most four, and P<=72-2h.
The high-overlap route is now finished at this threshold; rerunning
these exclusions is not the next research step. Seek an aggregate
restriction coupling missing-label deficits and fresh loss, or a new
small-modulus contradiction for lower-overlap sets. A four-overlap
classification alone is not justified without a clearer global payoff.

Even h>0 stays a separate required milestone. Stage27's parity1+7
quotient is elementary, but its numerical248 consequence and the
antipodal route retain the reported external seven-point certification.
Neither external dependency was recertified in this continuation.
No claim of novelty or of the original theorem being proved is made.

## Reproduction and delivery

    python stage29_two_paths.py
    python stage29_two_path_independent.py

These overwrite only their own Stage29 evidence. Both main runs are
COMPLETE; no process is running. Reports and all witnesses from
Stages26-29 are delivered on a new PR stacked on open PR#7, unmerged.
