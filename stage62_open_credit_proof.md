# Stage62: open paired-edge credit under all pure refinements

The full N>=248 theorem remains OPEN. This hand lemma is for the remaining single-class problem after the checked Stage60 and Stage61 theorems. It requires no new search or odd cancellation.

Fix an exact relation model of A=(u,2u,v,2v,w,2w,p,r), retaining all odd torsion. Its primary triangle alignment is zero. Assume an actual full-valid odd N<248 realization adds NO ordinary cubic equality beyond the model; arbitrary pure refinements are permitted. Let F be the distinct paired edges of the model's quartic triangles, and o0 their formally open count.

## The primary alignment graph cannot acquire another edge

Any new aligned edge has two endpoints, so among the primary triangle's three disjoint edges there is an edge disjoint from it. These two edges give an ordinary cubic collision pair. If that pair were already formal, the formal alignment of the existing edge would force the new edge to be formal as well. Thus a newly aligned edge forces a new ordinary equality, contrary to the hypothesis. The primary path forest is therefore fixed under pure-only refinements.

## Long terminal edges cannot close purely

Translate the alignment to zero. A terminal edge a->b=2a on a path of at least three vertices has a predecessor c with a=2c and b=4c. Pure-involving cubic closure of its center edge has one of the forms

    3a=2b+f,    3b=2a+g,    3a=3b.

The first gives f=-a, so the protected squarefree triple c+b+f equals3c. The three labels are distinct: coincidence of f with c forces a two-cycle, and coincidence with b forces a collision in an odd group. The second gives g=2b, extending the path, contrary to terminality and the fixed graph. The third gives3a=0 and a reverse edge b->a, a forbidden two-cycle in a triangle-bearing class. Thus a formally open long terminal remains open when no new ordinary equality is added.

An internal paired edge a->b with b->2b is already formally closed through3b=2a+2b. Hence the formally open edges of F are terminal edges.

## A new pure closure of a short terminal uses an isolated label

For a two-vertex component a->2a, the only possible pure closure is f=-a; the other two closure forms extend the path or create a two-cycle. If f has an outgoing edge f->2f, then either that edge is disjoint from a->2a or the two edges create a forbidden two-cycle/collision. In the disjoint case a=-f gives a literal mass-eight rival: replace the four original labels a,2a,f,2f by two copies each of a and f, leaving every other label once. Both block sums are zero.

If f is a non-isolated terminal label, write f=2b for its predecessor. The short component is disjoint from that path, so a,2a,b,f are four different labels. From a=-2b we get the private ordinary cubic equality

    2[f]+[2a] = 2[b]+[a].

Brackets denote one occurrence of a physical label, so [2a] is the
terminal label, not two occurrences of the center a. Both sides have
degree three. Their common value is zero when f=2b=-a.

Conversely its difference, using f=2b, is2b+a. If the equality were already formal, a=-f would be formal and the paired edge would not be formally open. Therefore a NEW pure closure through such f adds an ordinary equality, contrary to the hypothesis.

Only an isolated vertex can supply a new pure closure of a formally open short terminal. Each isolated vertex can supply at most one, because distinct terminal centers have distinct negatives in the actual group.

## Count which isolated labels are still available

An isolated label f is unavailable if its negative already equals ANY formal point of A. Then it cannot newly equal the negative of another physical label in a full-valid realization without a label collision; if it equals the relevant center formally, the edge was already closed. This includes f=0 and formal opposite pairs of isolated labels.

Let b0 count isolated labels whose negative is absent from the formal point set. Let ell0 count formally open paired terminal edges on paths of at least three vertices. Pure-only refinements can close at most b0 of the o0 edges, and none of the ell0 long terminals. Therefore

    o_actual >= o_lower := max(ell0,o0-b0).               (1)

The remaining shapes have respectively two, two and one isolated vertices. This does not assume independent fresh credits per triangle: F is a set, and every potential pure closure is charged to an actual isolated label once.

## A stronger proof-forcing quintic target

P=P3ordinary, t and c=C3ordinary are fixed if no new ordinary equality is added. R3_actual>=R0, where R0 is the formal repeated-cubic excess: merging formal cubic fibers cannot decrease sum binom(size-1,2). Use the general count and q<=h-o:

    N>=288+h+R3+2c+2w-2(t+q+P)
      >=288-h+R3+2c+2w+2o-2t-2P.

Since a counterexample has N<=247, and T3=36+h+R3,

    T3 >= 77+2R0+2c+2o_lower-2t-2P.                    (2)

Consequently a positive quintic separation certificate at

    T5 >= 115-2R0-2c-2o_lower+2t+2P                    (3)

contradicts N>=56+T3+T5 and N<=247, under the no-new-ordinary hypothesis. It therefore forces another ORDINARY equality. It is not an unconditional whole-model exclusion unless the independent T5>=156-R0 bound also holds.

Equation(3) gives a smaller rigorous target than the universal quintic156 bound. The lemma supplies a way to complete required residual couplings while allowing every pure refinement; weak discovery bounds still prove nothing.

## Persistent quartic and quintic credits

Let E0 be the number of formal quartic fibers consisting of exactly two
ordinary words with private centers and disjoint two-label tails. Under
the no-new-ordinary hypothesis, each remains an E fiber. A third ordinary
word would have a new private center outside the four old tail labels
and the two old centers. Its two tails must intersect the union of those
four old tails. Subtract a common tail from it and an old word: this gives
a new ordinary cubic equality. If this equality had already been formal,
the third quartic word would already have been in the formal fiber.
Two formal E fibers cannot merge because that would give four ordinary
quartic words, forbidden by the established cap. Therefore E>=E0.

Let U0 count those E0 outputs whose center edge belongs to F, once per
output. Stage58 forbids their consumption by genuine splits. Thus
U=E-2q>=U0 under the same hypothesis. Formal quartic split triples w0
and formal genuine quintic split triples q0 persist even when new
ordinary equalities are allowed: adding another ordinary word or merging
their fibers violates the cap of three. Consequently w>=w0, q>=q0 and
T3=36+h+R3>=36+q0+R0.

The necessary counterexample ledger is

    5t >= 2+2(o+R3+c)+5w+U.

With P,t,c fixed under pure refinements, its formal lower credits force
another ordinary equality whenever

    2+2(o_lower+R0+c)+5w0+U0 > 5t.                    (4)

The quartic budget also gives E>=80+t+2c-w-4P. From the exact weighted
count 2N>=496+2(h+R3+c)-5t+5w+E-4q and q<=h-o,

    2T3 >= 74+4R0+2c-5t+4o_lower
           +max(E0+5w0,80+t+2c-4P+4w0).             (5)

Take the integer ceiling of half the right side, and the maximum with
(2) and 36+R0+q0. A positive quintic certificate at 192 minus this
lower bound forces another ordinary equality. At 156-R0-q0 it excludes
the whole model. These two conclusions must remain separate.

For the robust N bound, let h0 and o0 be the formal open-center and
paired-edge counts. Every paired edge that becomes closed adds a
different repeated-cubic collision pair, recoverable from its two
centers. Thus h0-h_actual >= o0-o_actual, even if one cubic fiber gains
several pure words. Consequently

    q <= h_actual-o_actual <= h0-o0.

Combining this with the single-class split theorem gives

    q <= min(h0-o0,4(P-|D|)+1,4P-11c).

Under no new ordinary equality this yields the robust bound

    N >= 288-q_max+R0+2c+2w0-2t-2P.                  (6)

With four primary aligned edges, the actual triangle count is already
fixed even when new ordinary equalities are allowed: Stage60 forbids a
fifth edge, and Stage61 forbids another triangle-bearing class. Otherwise
the unconditional maximum is two. These facts justify the unconditional
credit exclusion 2+2(R0+c)+5w0>5*t_max.
