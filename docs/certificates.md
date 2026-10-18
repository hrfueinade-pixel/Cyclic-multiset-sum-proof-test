# Certificate contracts and mathematical coverage

A certificate verifies a finite implication. A separate mathematical
reduction must put every hypothetical counterexample into its domain.
The [dependency ledger](../certificates/dependencies.json) records those
reductions, including source injection, assignment, ownership, and forcing.
All claims in this document assume full eight-term validity, distinct
physical labels, odd order below 248, and the already established caps
when a leaf invokes them. The parity computations have their own domains.

## Worked integer identity

In the cubic-exception model the labels, in order, are

$$
A=(0,\delta,c,-2c,e,-2e,g,h),\qquad3\delta=0.
$$

The first quartic word `00001201` has value $-3e+h$ and `00201001` has
value $2c+e+h$. The saved rival is `41001011`, namely
$4[0]+[\delta]+[e]+[g]+[h]$, with eight nonnegative terms. Since
$s=\delta-c-e+g+h$, its value differs from $s$ by $c+2e$. The record gives

$$
2(\operatorname{val}(R)-s)
=-\bigl(\operatorname{val}(W)-\operatorname{val}(W')\bigr).
$$

If the two quartic values coincided, oddness would force
$\operatorname{val}(R)=s$. The rival differs from all-ones, contradicting
validity. Three is never canceled. The record is in
[`cap-cubic-exception-quartic.json.gz`](../certificates/multiplicity/cap-cubic-exception-quartic.json.gz).
Repeating this argument for **every** selected pair separates at least 89
repeated quartic values, contradicting $T_4\le88$. Bounds 87 or 88 do not
contradict that budget.

## Coordinates, reductions, and symmetry

A word is an eight-entry nonnegative integer vector; fractional entries are
rejected even if clearing a denominator gives a valid integer identity. Checkers verify its
length, degree, repetition, and inequality to all-ones when it is a rival.
A growth proof verifies all unordered selected pairs, not merely formal
inequality of coefficient vectors. An integer multiplier is multiplied,
never canceled. Among bounds used in the proof, only powers of two may be canceled under oddness, except
in the fourO quintic step: its preceding quartic bound first restricts the
order to 245 or 247, where three is a unit.

For relation matrices K, archives give integer unimodular L,V and diagonal
D with LKV=D. Entries must be integers and determinants must be +/-1. A determinant-one
rational matrix is not a valid unimodular coordinate change. Writing parameters as Vz is
invertible over every cyclic group. Each diagonal imposes d*z=0; removing
its power of two retains its entire odd part as a torsion constraint.
Free coordinates remain unrestricted. Multiple odd factors are independent
constraints on elements of the actual cyclic group, not an assumption that
the group contains a direct product of those orders.

The source checkers also use unit-minor parameterizations. A power-of-two
minor and recovery of the designated free labels establish surjectivity;
satisfying the equations alone would establish only one direction. The
remaining constraints are retained via unimodular changes and Bezout gcds.
No parameter is assumed to be a unit.

Symmetries are actual physical relabelings, pair permutations, or affine
maps obtained by relabeling and translation along an actual triangle.
They have inverse maps. Ownership permits only the four parameter
permutations fixing the chosen source edge and checks both relation-module
implications. Graph refinements need only the forward implication into an
already excluded child; the checker verifies it while preserving all odd
torsion. A child proved impossible under broader hypotheses remains safe.

## From a counterexample to the finite domain

| Family | Completeness bridge |
| --- | --- |
| Multiplicity | Private centers reduce four ordinary quartics to two simple tail graphs and four ordinary quintics to four doubling pairs. Every new total cubic direction is enumerated up to sign, powers of two, and an explicitly invertible pair permutation. All 57 joint orbits retain nonunit cases. |
| Split sources | Every split has the canonical eight-label form. A third source center is one of two unused labels; protection excludes one, leaving exactly ten tail choices. The remaining path forces a new total cubic relation by the six-pair count, then a second relation in each of six residuals. Inventories contain 901 and 4,339 directions, including pure cubics. |
| Assignment | A specified source edge has 720 fibers and 2,880 closure presentations. Enumerations include all eight shared physical positions, repeated presentations, distinct-output skips, and parallel-edge cases. All 56 quartic-triple leaves are replaced under cap three; their [stable identifiers](assignment-replacements.md) are emitted by the checker. |
| Ownership | All 720 source presentations on a paired triangle edge are covered. An edge-closure conclusion alone is not an accepted exclusion. Distinct paired open edges are unused vertices of the assignment graph, proving q<=h-o. |
| Forests | Cycle exclusion and matching number three give nine partitions. Each chosen class forces a new ordinary collision unless an unconditional growth certificate already excludes it. Every private four-label pair is included. The six large shapes and all further required nodes close. |
| Interactions | All 3,360 second-triangle presentations on the same physical labels are covered. The 604 same-class conclusions are conditional on the selected second class being different; they are not contradictions for the whole model. Every distinct-class residual is excluded, with complete further ordinary branching. |
| Two triangles | The root is exactly p=4u. Its 31 forcing nodes have at most eight formal ordinary pairs. Lemma 12 requires another ordinary pair. Every new private pair is covered, modulo sign and powers of two only. All 13,333 nodes are reached in an acyclic proof graph. |
| Seven points/parity | Heredity, the subset cube, antipodal projection, and subgroup bounds precede normalization. Every required order is freshly enumerated. Unitless divisor roots include points below the root. Every nonunit preimage is kept. All 58 six-set survivors are extended; quotient affine classes lift surjectively. |

## Accepted leaves in the final proof graphs

| Leaf | Mathematical conclusion and required premise |
| --- | --- |
| Label or protected collision | Unconditional contradiction to distinctness or squarefree protection. |
| Non-original mass-eight word | Unconditional contradiction to validity. |
| Four ordinary words, or four total cubics | Contradiction using the corresponding established cap three. Ordinary and total caps are not interchangeable. |
| Source with a third ordinary quartic word | Contradiction only after Lemma 7; the checker recovers an actual genuine split and its source. |
| Separated repeated quartics | At least 89 distinct repeated **values**, hence contradiction to T4<=88. Every pair has a checked rival identity. |
| Alignment cycle or five aligned edges | Uses the already proved cycle/forest theorem with the actual physical edges checked. |
| Distinct-class interaction | Two triangle matchings in the same class share at most one of four available edges; a union of at least five edges therefore invokes Lemma 15. |
| Global credit | Unconditional: formal R0=c0=w0=1 persists under all further ordinary and pure equalities; 11>10 contradicts t<=2. Exactly five final leaves use this. |
| Shared-descent split guard | Unconditional: a genuine split descends to a pair in two triangles, forbidden by Lemma 13 and the cycle lemma. Exactly one final leaf uses this. |
| Forced ordinary refinement | A **conditional** statement: if no new ordinary equality occurred, P<=8 would contradict Lemma 12. It forces another ordinary equality; it is accepted only with complete further branching. Pure refinements remain allowed. |

There are no conditional quintic-growth credit leaves in the retained final
archive. The checker now rejects their unused rule names rather than
accepting them as unconditional exclusions. The full run independently
reconstructs all 29,466 branches at the 42 ordinary-forcing nodes across
forests, interactions, and the two-triangle component.

## Implementation independence

Discovery is not imported by the retained checkers. Several checkers are
separately written, but later graph checkers **share** `alignment_forests`
integer arithmetic and coverage helpers; assignment shares earlier checker
helpers. The parity enumerators share `verification/parity.py`.
These are common sources of implementation error.

`verification/independent.py` reconstructs refinement coverage from ordered
physical labels without those helpers. It also compares actual cyclic
solutions with retained parameterizations at orders 3, 5, and 9, using
straightforward exhaustive enumeration and separate rational determinant
arithmetic. Small-case tests compare shared parity routines with direct
multiset enumeration, affine normalization, and all residue preimages.
These checks can reveal errors; small-case success is not a universal
surjectivity proof. The unimodular identities supply that proof. All new
code is AI-assisted, not independent external human review.
