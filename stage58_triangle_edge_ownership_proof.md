# Stage58: unused triangle edges and the global low-collision exclusion

The full N>=248 theorem remains OPEN. Assume a full-valid eight-point
set in an odd cyclic group with N<248. Retain the established cubic,
ordinary quartic/quintic caps and T4<=88. Stage55 proves general q<=h
by assigning every genuine quintic split to a distinct incident open
source center edge.

## 1. A paired triangle edge cannot be a genuine split source

Choose any edge in a quartic triangle. Translate its common alignment
value to zero, giving the exact surjective family

    A=(u,2u,v,2v,w,2w,p,r).

Take the paired center edge (u,2u). The complete genuine-split normal
form, with all eight physical positions shared, has720 source presentations
on this edge. A presentation has three distinct centers and omitted-tail
edges forming a two-edge path plus a disjoint edge. It includes every
possible third center, source tails, free lift label and omitted tail.

Every presentation is excluded below248. There are190 exact relation
models after parameter symmetries that FIX the chosen pair. In184 models
a physical label collision or an equality between a protected squarefree
word and a different word is forced. In the remaining six models,
89 repeated quartic words have pairwise positive mass-eight separation
identities. Their23,496 pair identities contradict T4<=88.

The standalone checker reconstructs720 presentations from all ordered
eight-label canonical frames, independently of the producer's shared-source
construction. It verifies integer unimodular row/column reductions, keeps
every odd diagonal factor as torsion, and checks both directions of each
reused model implication. Only the four parameter permutations that fix
(u,2u) may reuse a conditional edge proof. It imports no producer,
eliminator or earlier checker. No witness-search absence or timeout is a
premise. Every accepted model in this archive is excluded outright; edge
closure alone is not used as an exclusion.

The same theorem applies to every paired center edge occurring in any
quartic triangle, by physical label symmetry and translation.

## 2. Count the unused edges once

Let F be the SET of unordered paired center edges occurring in at least
one actual quartic triangle, and let o be the number of its open members.
An edge reused by several triangles is counted once. Section1 says no
genuine split has a source on any edge in F. The o open vertices are
therefore unused by every assignment in Stage55's auxiliary graph.
Applying that injection to the remaining vertices gives the GENERAL bound

    q<=h-o.                                             (6)

Also, every two-ordinary disjoint-tail source counted in E whose center
edge lies in F is unused by genuine splits. These sources give a literal
subset of U=E-2q, without requiring their values to be fresh per triangle.
Their distinct outputs and center pairs must still be counted explicitly.

Write P=P3ordinary and J=P3total-P. The global count now gives

    N>=260-P+J+R3+2c+2w-2t+2o.                      (7)

This is stronger than an assumed separate credit per triangle: o counts
actual unused edges, including all reuse.

## 3. Complete forest incidence table

By stage56_alignment_cycle_hand_proof.md, each triangle-bearing alignment
class is a path forest on eight labels with maximum matching three.
For a class with m edges, each pair of disjoint edges gives an ordinary
cubic pair. Adjacent edges give a pair involving a pure cubic word.
These cubic pairs have a unique alignment value, so classes contribute
disjoint sets of pairs. A triangle is a matching of three edges.

|Path vertex sizes|Ordinary pairs Pclass|Pure-involving pairs Jclass|Triangles|
|---|---:|---:|---:|
|(2,2,2,1,1)|3|0|1|
|(4,2,1,1)|4|2|1|
|(3,2,2,1)|5|1|2|
|(6,1,1)|6|4|1|
|(5,2,1)|7|3|3|
|(4,3,1)|7|3|2|
|(3,3,2)|8|2|4|
|(7,1)|10|5|4|
|(5,3)|11|4|6|

For example, Pclass=binom(m,2)-sum(max(s-2,0)) and
Jclass=sum(max(s-2,0)), where s runs over path vertex sizes.
The nine partitions are exhaustive: a matching of size four is forbidden
by the ordinary quintic cap, and smaller matching numbers have no triangle.

## 4. Every counterexample has at least nine ordinary cubic pairs

Suppose P<=8. If t<=2, (7) immediately gives N>=260-8-4=248.
The incidence table leaves only these cases with t>=3:

* One class with three triangles: its shape is(5,2,1), contributes at
  least seven ordinary pairs and at least three pure-involving pairs.
  Thus N>=260-8+3-6=249.
* A two-triangle class and a one-triangle class: their minimum ordinary
  counts are5+3=8. Both minima must hold, so the first shape is(3,2,2,1),
  the second is(2,2,2,1,1), and there are no other ordinary pairs.
* One four-triangle class: with P<=8 its shape must be(3,3,2), accounts
  for all eight ordinary pairs, and has at least two pure-involving pairs.

Three triangle-bearing classes already require P>=9. Two classes with
at least two triangles each require P>=10. Larger single-class triangle
counts require P>=11. No other t>=3 case occurs with P<=8.

For the second case, the(3,2,2,1) class has three terminal paired edges
forming a matching on six labels. All three occur in triangles, and none
can be closed by an ordinary pair from that same alignment class: their
terminal labels have no outgoing edge in it. The other class's three
ordinary pairs have center edges forming a triangle on its three centers.
Such a triangle can contain at most ONE edge from the terminal matching.
At least two of the terminal paired edges are therefore either open or
closed by new pure-involving cubic pairs. Each such pure closure uses a
distinct center edge and contributes a distinct pair to J, beyond the
primary class's one adjacent-edge pair. Consequently J+2o>=1+2=3.
Equation(7) gives N>=260-8-6+3=249.

For the third case, the(3,3,2) class likewise has three terminal paired
edges forming a matching. All its ordinary pairs are already used, so
none of these terminal edges can be closed by an ordinary pair outside
the class. If r terminal edges are closed, they contribute r additional
pure-involving pairs, while the others contribute3-r to o. The two
adjacent-edge pairs are distinct from these closures. Hence

    J+2o>=2+r+2(3-r)>=5.

Equation(7) gives N>=260-8-8+5=249. These exclusions cover P<=8,
proving the global necessary condition

    P3ordinary>=9                                      (COUNTEREXAMPLE).

This excludes a whole structural branch. It does not exclude arbitrary
odd207..247 moduli in full. The remaining task is a coupled allocation
argument or complete positive closure for systems with at least nine
ordinary pairs; no unresolved finite-inventory branch is a theorem.

## 5. Robust ordinary-only branching with the new credit

Fix a relation model and suppose an actual counterexample adds no ordinary
cubic equality. Let h0 be its formal open-edge count and o0 the number of
formally open paired edges occurring in its formal triangles. A new
closure of one of those o0 edges must involve a pure cubic word; otherwise
it is a new ordinary equality. Distinct closures use distinct center-edge
marks. If s new pure-involving pairs occur, actual h=h0-s and
o>=max(0,o0-s). Equation(6) therefore gives q<=h0-o0.

Combining it with q<=4P-11c, and allowing ALL pure refinements, improves
the conditional bound to

    N>=288-min(h0-o0,4P-11c)+R0+2c-2t-2P.

This can force a new ordinary equality without enumerating irrelevant
pure-only relations. A global T5>=156-R0 positive proof still excludes
the whole model directly. The full tree remains incomplete discovery.
