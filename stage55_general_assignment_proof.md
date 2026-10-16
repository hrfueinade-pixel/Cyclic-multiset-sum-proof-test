# Stage55: general split assignment; the entire t=0 branch is closed

2026-10-12. The full N>=248 theorem remains OPEN. This proof extends q<=h from C4=0 to the GENERAL hypothetical odd N<248 setting and excludes every system with no ordinary quartic triangle. The remaining problem is the exact affine three-doubling-pair family.

## 1. Hypotheses and the general source budget

A has eight physically distinct labels in an odd cyclic group, full mass-eight validity, N<248, the established cubic/quartic/quintic multiplicity caps, and T4<=88. Let q count genuine quintic split outputs and h the unordered center edges uv for which 2(u-v) is absent from the ordered difference set. Write c=C3ordinary, t=C4triangle, w=C4split.

Stage54 proves every genuine split source has exactly two ordinary quartic representations, with a recoverable inverse and no source serving two different splits. Thus E>=2q generally and U=E-2q is an actual nonnegative inventory of unused two-ordinary disjoint-tail sources. Mixed words at those outputs are allowed.

The source theorem alone does not imply q<=h. The new argument below proves the separate global assignment and does not assume distinct center edges merely because word-pair sources are distinct.

## 2. One ordinary cubic triple supports at most one genuine split

Normalize an ordinary cubic triple as

    2x0+a0=2x1+a1=2x2+a2=V.

Privacy and protection give six distinct labels x0,x1,x2,a0,a1,a2. Name the other two p,r. A genuine split descending to one of the three cubic pairs chooses its third center z and middle tail b among the other four labels, with the last two added to that pair. There are exactly36 candidate fibers; no physical overlap is omitted.

Complete direct/source/growth exclusions remove30 candidates below248. The six necessary residuals have third center p or r and middle tail ak of the unused cubic word. Their added labels are xk and the other free label. For a fixed free center p, the third quintic word is

    2p+a0+a1+a2,

while its output is V+xk+r. Two choices of k would force equal distinct xk labels. Hence at most one output can use each free center.

The proof retains and checks all fifteen pairs of the six residuals, including the opposite-center cases. Six pairs give direct label collisions; nine have positive quartic-growth bounds108 or110. Three of those models retain genuine order-three torsion. Each model is surjective over all relevant odd-group solutions; no odd factor is divided out. Every selected quartic pair has a positively reconstructed mass-eight rival identity, proving T4>=89 and contradicting the budget.

Thus two genuine split outputs cannot descend to the same ordinary cubic triple in a putative small-order counterexample. This is a value-level restriction with an exact cubic descent, not an assumed allocation of c credits.

## 3. Replace every former cap-two inference

Stage53 proved a split assignment under C4=0. Its finite coverage contains56 local exclusions that ended in three ordinary quartic words. Those words are not contradictions under the general cap three. EVERY such inference is replaced here:

| Former inference | General replacement |
| --- | --- |
|28 paths in one-root/two-open coverage|Explicit rival or split-source contradiction, or positive growth to at least89 repeated quartic values.|
|14 paths in two-open sharing coverage|Positive growth to at least89 values.|
|Four paths in repeated-mark coverage|Split-source contradiction or positive growth.|
|Two triangles in repeated-mark coverage|A third ordinary word at an ACTUAL genuine-split source, contradicting Stage54. No t=0 assumption is used.|
|Eight stars: two one-root and six sharing cases|Removing the common tail gives an ordinary cubic triple containing BOTH split descents, contradicting Section2.|

The star inverse is literal common-tail removal. Its six cubic labels are distinct, and each of the two actual split descents is a pair from that triple. The two split fibers differ. The new verifier checks these facts and their integer identities; it never treats the star itself as forbidden generally.

Some path relation systems require more than a chosen dyadic pivot sequence. Solve a unit-minor subsystem and recover its free labels using a power-of-two scale. The remaining integer constraints, after an integer unimodular coordinate change, are n_i*delta=0. Bezout makes their combined condition gcd(n_i)*delta=0. Only the power of two is removed; the odd part remains torsion. The verifier checks the unit minor, coordinate recovery, every remaining constraint, unimodularity, and the retained odd gcd.

All other old exclusions were positive identities involving a label collision, closure of a declared open edge, a protected squarefree word, or a non-original mass-eight rival. They remain valid generally. The new verifier traverses the complete saved Stage53 coverage and intercepts all56 quartic-triple inferences instead of accepting the old C4=0 conclusion.

## 4. General auxiliary graph and injection

Use the h open center edges as vertices. A two-open split is an edge between its source vertices; a single-open split is a mark on its only open source. Include unused center edges as isolated vertices.

Every split has an open source: the complete closed-both-source model forces T4>=116. Its6,670 positive growth-pair identities and closure placements are checked in the new chain; this premise is independent of C4=0.

The general replacements restore all four local statements:

1. No vertex carries two marks.
2. The ends of one auxiliary edge cannot both carry marks.
3. A mark cannot be followed by a two-edge auxiliary path.
4. The graph has no parallel edges and has maximum degree two.

The unchanged complete coverage includes2,880 one-root presentations,100 end-mark residual pairs,7,190 path extensions,719 sharing presentations and962 degree-three residual pairs, and11,504 repeated-mark presentations. Identical-fiber skips and same-other-edge cases are explicitly checked. All physical labels are shared within the same eight positions.

A component cannot have two marks: adjacent ones violate Statement2, and more distant ones violate Statement3 along a shortest path. A marked cycle also violates Statement3. Thus components are unmarked paths, unmarked cycles, or paths with one mark, including isolated vertices.

Orient an unmarked path from a chosen root and assign each edge to its child. Orient an unmarked cycle consistently. Assign a marked path's mark to its vertex, then orient both sides away from that vertex and assign edges to children. These assignments cover EVERY split and use distinct incident open center edges across all components. Therefore

    q<=h                                               (GENERAL)

for any hypothetical odd N<248 counterexample, even with quartic stars, paths, splits or triangles elsewhere.

## 5. The whole no-triangle branch is excluded

The general Stage48/54 bound is

    2N>=496+2(h+R3+c)-5t+5w-2q+U.

For t=0, the assignment yields

    2N>=496+2(h-q+R3+c)+5w+U>=496,

contradicting N<248. This excludes ALL t=0 systems, not merely C4=0. Ordinary quartic stars, paths and splits are included.

Every remaining counterexample has a quartic triangle. Its equations are equivalent to

    2x-a=2y-b=2z-c=tau.

Translate every label by -tau. The triangle's six distinct labels become three doubling pairs, so the remaining full problem lies in

    A=(u,2u,v,2v,w,2w,p,r).

The normalization is surjective and uses no division by three or another odd integer. It does not exclude this family; generic examples and bounded discovery absence remain insufficient.

## 6. Sharper counting for the remaining family

A split has a unique cubic pair descent. Stage54 bounds four splits per ordinary cubic pair. Section2 bounds ONE per ordinary cubic triple, instead of four times its three pairs. The cubic-output inverse separates these classes. Hence

    q<=4(P3ordinary-3c)+c=4P3ordinary-11c,
    q<=min(h,4P3ordinary-11c).

Combined with the general count

    N>=288+h+R3+2c+2w-2(t+q+P3ordinary),

this forces further actual cubic equalities whenever the no-extra-cubic values violate N<248. Under that assumption, triangle counts are determined by three-edge matchings in alignment classes of directed edges x->a with fixed 2x-a. An added quartic triangle requires its cubic pair descents, so it cannot appear independently of those classes.

The final triangle allocation

    5t<=2(h-q+R3+c)+5w+U

is still UNPROVED. The general/even bounds, equality248, Stage45 residual558 and every historical discovery-only boundary are unchanged. No arbitrary odd207..247 modulus is newly excluded in full, and the full goal remains active.
