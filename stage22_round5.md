# Round 5 of 8: complete opposing-shape inventory before local roles

Scope: valid eight distinct points, odd cyclic H, h=0, and a fresh
quartic fiber X. MC (the entire fiber of any multiway cubic cone is
connected) remains a Stage 13/14 computational dependency. MC implies
every cubic deletion at X has at most two marks. Thus the local graph
is pair-shadow, with degree at most two and no three vertices sharing
a point. Ordinary centers are private as always.

## Extension of new restrictions to this scope

Stage 17's cycle length/type proofs use regularity ONLY to obtain the
pair-shadow condition. Its geometric proofs and odd h=0 local lemmas
then apply verbatim to this fresh fiber. The new Round 2 long-cycle
identities therefore exclude every cycle longer than three here too.
The Round 3 path coverage uses only pair-shadow, pure pairing, absence
of order-three differences, disjoint 22/31 exclusion, and disjoint
31/31 order-five torsion. All hold here. Thus every nontrivial component
has two or three vertices. These extensions do not assert a global
path decomposition when R3>0: only fresh fibers are pair-shadow.
Round 4 FOP is excluded even without MC.

The following inventory is an elementary finite type analysis, with no
new numerical computation or role calculation. Symbols F,Q,P,O denote
4,22,31,211; path words are up to reversal, triangle words up to cyclic
rotation and reversal. A word is a necessary type shape, not a realization.

## All opponents to a 31/ordinary endpoint

Its component is exactly

    X=3a+b=2c+b+q, 3a=2c+q,

on four distinct points. Full-support separation leaves at most four
points for opponents. There cannot be two opposing components: each
needs at least two points, the only two-point component is isolated Q,
and distinct Qs cannot have the same value in odd H.

A component of support at most four is initially one of:

|Component|Support|
|---|---:|
|isolated Q|2|
|isolated O|3|
|FO path|3|
|PQ path|3|
|PO path|4|
|QO path|4|
|PQP path|4|
|PPO triangle|4|
|QPO triangle|4|

There is no isolated F or P: their pure cubic is paired by the
singleton-base forest/tree lemma at h=0. Two Qs or two Fs cannot
share a value; F/Q is forbidden; PP endpoints sharing a singleton
give order three; PPP cycles are excluded by Stage 15. FOP is the
new Round 4 exclusion. All other paths/triangles exceed four points.

Every shape containing Q is excluded because it is disjoint from
the main P, by Stage 8 Lemma 2.2. The PPO triangle has two P centers;
both are disjoint from the main P, so all three centers lie in one
order-five coset, violating unique ordered differences. Consequently
the COMPLETE remaining opponent list is:

    isolated O; FO path; PO endpoint path.

The next local calculation may target these three, not assume isolated O
is the only opponent. The PO/PO case uses all eight points, the others
leave unused points which must remain distinct in any presentation.

## All opponents to an isolated ordinary center defect

The main component is X=2a+b+c on three points. Its opponents use at
most five points in total. A single opposing component is necessarily:

|Component|Support|
|---|---:|
|isolated Q; isolated O|2; 3|
|FO; PQ; PO; QO; OO paths|3; 3; 4; 4; 5|
|FOO; POP; QPO; PQO; PQP; PPO paths|5; 5; 5; 5; 4; 5|
|POO; PPO; QOO; QPO triangles|5; 4; 5; 4|

PQP and PPO path have different incidences; QPO path and QPO triangle
are distinct cases. The table records types, with all admissible P
orientations still needing incidence roles before any calculation.
The OO opponent is already excluded by the Stage 17 theorem, whose
eight distinct labels are exactly its five points plus the main three.
No other entry is silently excluded here.

There could initially be TWO opponents on the five available points.
Exactly one must be isolated Q (two points); the other can initially
be isolated O, FO, or PQ (three points). A second Q is impossible;
FO and Q cannot share a value; PQ contains a second Q and is impossible.
Thus the only initial two-opponent allocation is isolated Q + isolated O.
Its two isolated Os, together with h=0 disjoint center closure, require
the six-point bridge's doubled tails; this allocation is NOT excluded
by merely naming it and remains explicitly listed. Total support is eight.

For coverage: components are paths of length <=3, triangles, or isolated
vertices. A nonpure endpoint adds one private point, an ordinary vertex
adds its private center, and a triangle has support 3+#O. At most one Q,
at most one F, no F with Q, all Ps adjacent to Q when Q occurs, at most
two Ps, and F only at an endpoint beside O exhaust the type restrictions.
Applying these rules at support <=4 and <=5 gives precisely the two tables.
No assumption about a global unpaired singleton permutation is used.

**New restriction/obstruction:** fresh pair-shadow fibers have only these
short-component opponents. The singleton endpoint has three cases left;
the isolated-ordinary branch retains a larger, explicitly separate list
and a possible two-opponent allocation. MC is a required dependency,
not independently recertified in this run. Round 5 checkpoint saved.
