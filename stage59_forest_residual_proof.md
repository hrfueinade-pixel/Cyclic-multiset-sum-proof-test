# Stage59: the residual problem requires collisions outside each triangle class

The full N>=248 theorem remains open. This argument uses the one-split-per-triangle theorem in stage59_one_split_per_triangle_proof.md to exclude an entire structural family and quantify what a remaining counterexample must add.

## 1. A counting bound that allows all pure refinements

For a hypothetical full-valid eight-set in odd N<248, retain the general count

    N >= 288+h+R3+2c+2w-2(t+q+P).                       (1)

Here P=P3ordinary. The general assignment q<=h gives h-2q>=-q. All other displayed correction terms are nonnegative. Thus

    N >= 288-q-2t-2P.                                  (2)

This inequality does not fix the pure cubic partition or forbid new pure collisions. It uses no assumption that formally different outputs remain different.

## 2. All nine ordinary-collision-exhausted forest families are excluded

Choose an ACTUAL triangle-bearing alignment class. By the published cycle exclusion, its graph is a path forest on eight physical labels, with maximum matching exactly three. Let P0 be its number of disjoint edge pairs, t0 its number of three-edge matchings, and D0 the set of its edge pairs occurring in at least one such matching.

Every disjoint edge pair gives an ordinary cubic collision pair with the class's alignment value. That value is uniquely recoverable from the pair. Distinct classes therefore have disjoint cubic-pair inventories. Different matchings produce different quartic triangle outputs under the ordinary cap; otherwise the union of their representations would contain more than three ordinary words, and the three-word fiber recovers its matching uniquely.

Suppose EVERY ordinary cubic pair in the set belongs to the chosen class. Then P=P0. Another triangle-bearing class would contribute ordinary cubic pairs of its own alignment value, so no such class exists; t=t0 and |D|=|D0|. Section4 of the split theorem gives

    q <= Q0 := 4(P0-|D0|)+t0.

Combining with (2) proves N>=B0:=288-Q0-2t0-2P0.

|Path vertex sizes|P0|t0|D0 count|Q0|B0|
|---|---:|---:|---:|---:|---:|
|(2,2,2,1,1)|3|1|3|1|279|
|(4,2,1,1)|4|1|3|5|273|
|(3,2,2,1)|5|2|5|2|272|
|(6,1,1)|6|1|3|13|261|
|(5,2,1)|7|3|7|3|265|
|(4,3,1)|7|2|5|10|260|
|(3,3,2)|8|4|8|4|260|
|(7,1)|10|4|9|8|252|
|(5,3)|11|6|11|6|248|

The nine shapes are exhaustive. Their counts are obtained by selecting disjoint edge pairs and triples in literal paths; the checker independently reconstructs this table from all integer partitions of eight. In particular, D0 is not assumed equal to P0. For example, the six-vertex path has six disjoint edge pairs but only three of them occur in its unique matching of size three.

Every B0 is at least248. Thus the whole family in which ordinary collisions are exhausted by one triangle class is excluded. Equivalently, EVERY chosen triangle-bearing class of a remaining counterexample must have at least one ordinary cubic pair outside it. Pure-only refinements cannot evade this conclusion.

## 3. Quantify the additional structure rather than branch blindly

Keep the chosen class, but now allow r ordinary cubic pairs outside it and t_out triangles in other classes. Then P=P0+r and t=t0+t_out. Let D_out be the ordinary pairs in those other triangles. Alignment uniqueness makes D_out disjoint from the chosen class, and the two-triangles-per-pair bound gives |D_out|>=3t_out/2.

The set-level split bound consequently gives

    q <= Q0+4(r-|D_out|)+t_out
      <= Q0+4r-5t_out.

Use this in (2) to obtain the GENERAL bound

    N >= B0-6r+3t_out.                                  (3)

Therefore a counterexample, with integer N<=247, must satisfy

    6r-3t_out >= B0-247.                                (4)

This is an additional structural necessity, not a claim that satisfying it realizes a cyclic set. It implies the following minimum external ordinary-pair counts, and extra triangle classes can raise the requirement further:

|Chosen shape|Minimum r|
|---|---:|
|(2,2,2,1,1)|6|
|(4,2,1,1)|5|
|(3,2,2,1)|5|
|(6,1,1)|3|
|(5,2,1)|3|
|(4,3,1)|3|
|(3,3,2)|3|
|(7,1)|1|
|(5,3)|1|

All these inequalities hold while allowing arbitrary additional pure cubic collisions. Additional ordinary triples and quartic splits only contribute nonnegative terms omitted in (2).

## 4. What remains for the full theorem

The residual configurations have either one triangle-bearing class plus ordinary collisions in other, non-triangle classes, or multiple triangle-bearing classes. They must satisfy (4) for EVERY chosen primary class, the general q<=h-o assignment, the cubic-triple bound q<=4P-11c, the source budget U>=0, and the quartic budget.

The next proof task is to show that the required external collisions produce actual unused edges/sources or exceed the quartic or cubic/quintic budgets. The sufficient global target remains

    5t <= 2(h-q+R3+c)+5w+U.

No per-triangle source freshness is assumed here. The reversal and terminal-edge lemmas described in the local next-target note are promising tools for coupling classes, but the saved reversal probe has not been promoted to a premise of this proof. The incomplete broad cubic trees remain discovery only. This result does not exclude every arbitrary odd order207..247 in full.
