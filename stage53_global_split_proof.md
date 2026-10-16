# Stage 53: a global assignment for all genuine splits when C4=0

2026-10-12. This closes the entire no-ordinary-quartic-triple branch of the hypothetical odd N<248 problem. The full N>=248 theorem remains open in the branch C4>0. The proof has finite computer-assisted local lemmas and an elementary global graph argument. It does not enumerate group elements or cyclic moduli.

## 1. Statement and inherited hypotheses

Let A be eight distinct points in an odd cyclic group. Full validity means the all-ones word is the unique nonnegative mass-eight representation of s=sum(A). Consequently every squarefree word is protected against any different equal-degree multiset word.

Work in the inherited hypothetical odd N<248 setting. Ordinary cubic, quartic and quintic multiplicities are at most three, and the repeated quartic count satisfies T4<=88. Assume C4=0: no value has three ordinary quartic representations of ANY type. Thus every ordinary quartic fiber has at most two words. By the corrected Stage 48 lift correspondences, all ordinary quintic triples are genuine splits. Let q be their number, E=S4 the number of disjoint-tail ordinary quartic word pairs, and h the number of unordered center edges uv with 2(u-v) outside the ordered difference set Delta.

**Theorem. Under these hypotheses, genuine split outputs admit an injective assignment to incident open center edges. In particular q<=h. Therefore this entire branch contradicts N<248.**

This is stronger than the proposed compensation lemma in this branch. No bonuses, component deficits, cubic-excess allocation, P3<=17 theorem, or pending Stage 51 coverage assertion are needed.

## 2. Canonical splits and the exact closure rule

A split has the form

    2x+c+d+e = 2y+a+d+e = 2z+a+b+c,

where all eight displayed labels are distinct. Its cubic relation is

    2x+c = 2y+a.

Its two disjoint-tail quartic sources are

    2x+d+e = 2z+a+b,
    2y+d+e = 2z+b+c.

Deleting the shared tail label recovers these sources uniquely. A source supports at most one genuine split: if Q=2u+A=2v+B has unused labels i,j and both Q+i and Q+j were split triples, their third words would be 2j+A+B-r and 2i+A+B-r'. Adding the equations gives s=3u+3v+r+r', a nonnegative mass-eight rival omitting i,j. Hence 2q<=E.

For a source 2u+l1+l2=2v+r1+r2 with disjoint tails, suppose 2(u-v)=f-g belongs to Delta. Then

    l1+l2+f = r1+r2+g.

The two count vectors differ. Full protection requires BOTH sides to repeat, so f is one of the LEFT tails and g one of the RIGHT tails. Thus the four possible closures are exact, with their sign fixed:

    2(u-v)=left_tail-right_tail.

This rule introduces no missing ambient labels or extra closure assumption.

## 3. Every split has an open source edge under the quartic budget

If both source-center edges are closed, compare the two closures with 2(x-y)=a-c. Of sixteen tail placements, twelve give a protected cubic collision, two give 2a=2c, and only two d/e-mirror placements survive:

    2(x-z)=d-a,  2(y-z)=e-c.

Translate z=0 and set u=x-y, v=y, r=c. The equations force, without dividing by an odd integer,

    (x,y,z,a,b,c,d,e)
      =(u+v,v,0,r+2u,r+4u+6v,r,r+4u+2v,r+2v).

The retained positive Stage 49 certificate separates 116 repeated quartic words for EVERY full-valid odd realization of this complete model. Every selected pair has an explicit identity

    2^j (value(rival)-s) = m (value(left)-value(right)),

where the rival is nonnegative, has mass eight, and differs from all-ones. Equality of the two quartic values would therefore contradict full validity. The 6,670 identities cover every pair of the 116 words and give T4>=116, contrary to T4<=88.

This certificate is included in the Stage 53 bundle, rather than relying on an unpublished report. Its sixteen closure placements, words and all 6,670 pair identities are checked by the new standalone verifier. Thus every split has at least one open source-center edge.

## 4. Four complete local lemmas

Call a split with two open sources a two-open split. Call one with exactly one open source a root mark at that source-center edge. Under full validity, oddness and ordinary quartic cap two, the following statements hold:

1. **One open center edge cannot carry two distinct root marks.**
2. **The two open source edges of a two-open split cannot both carry root marks.**
3. **A root mark cannot be followed by a two-edge auxiliary path.** More explicitly: if a two-open split joins open center edges U,V and U carries a root mark, no distinct two-open split can join V to an edge W different from U.
4. **No open center edge is incident to three distinct two-open splits with different other source edges.** Also, two different two-open splits cannot have the same two open source-center edges.

Here "different" refers to genuine word fibers/outputs, not alternate presentations of the same fiber. These lemmas allow every physical label overlap among different splits: each split uses the same eight positions.

### Finite coverage and positive proof identities

Fix a canonical two-open split on labels 0,...,7 with open source edges 02 and 12. A split using a specified source edge is recovered by choosing its third center (six choices), the added label (five choices), a two-tail partition (six choices), and the omitted label of its third word (four choices). There are exactly 720 fibers. A root mark also chooses one of the four possible closures of its other source, giving 2,880 presentations.

No repeated-center configuration is removed by assumption. Choices using the central split's same center triple are included. Presentations of the identical fiber are omitted only when the statement explicitly requires a DISTINCT additional split.

| Local statement | Complete positive coverage |
| --- | --- |
| Root on 02 beside a canonical two-open split | 2,870 of 2,880 presentations excluded; ten remain as necessary relation systems. |
| Root marks at both ends of that split | All 100 pairs of the ten surviving left/right relation systems excluded. |
| Root followed by a second auxiliary edge | All 7,190 distinct extensions excluded; the ten identical-central presentations are explicitly skipped. |
| Two distinct two-open splits sharing 02 | 685 of 719 additional fibers excluded; 34 necessary systems remain. Cases with the same other edge as the central split are all excluded, proving no parallel auxiliary edges. |
| Three two-open splits incident to 02 | All 962 pairs with different other source edges excluded. The 194 same-other-edge pairs do not describe three distinct incident auxiliary edges. |
| Two distinct root marks at 02 | All 11,504 presentations excluded, covering four first-mark closures and every second mark. The sixteen identical-first-fiber presentations are explicitly skipped. |

Each exclusion supplies an integer combination of its ORIGINAL cubic/quintic/closure relations equal to a power of two times one of:

- a label difference, contradicting distinctness;
- an open doubled-center difference minus an actual label difference;
- a protected squarefree word minus another word;
- a non-original nonnegative mass-eight word minus all-ones; or
- both differences between three ordinary quartic words.

The last type contradicts cap two; it is not used as a universal validity contradiction. All factors canceled are powers of two. Rational elimination is only a discovery aid, never a proof premise. The checker reconstructs coverage by a different source-and-unused-label enumeration and checks all identities by integer multiplication.

One instructive degree-three residual has the three cubic descents

    2x+c=2y+a,
    2x+y=2d+e,
    2x+d=2c+e,

and two quartic source equations

    2x+a+c=2z+e+b,
    2x+y+a=2z+e+b.

Subtracting the last two directly gives c=y. No cancellation of three, rational-rank inference, or torsion argument is needed. Its d/e mirror has the same direct label collision. Explicit original-row identities retain these cases even when a chosen rational basis would suggest unnecessary odd denominators.

## 5. The global graph argument

Use the h open source-center edges as vertices of an auxiliary graph, including unused ones as isolated vertices. A two-open split is an edge between its two sources; a root mark is a mark at its sole open source. The split outputs are precisely its edges and marks. No source is assumed unique merely because its center edge is unique.

The local lemmas imply:

- the graph has no loops or parallel edges and has maximum degree two;
- each vertex has at most one mark;
- no connected component contains two marks: if their distance is one, Lemma 2 applies; if it is at least two, Lemma 3 applies to the first two edges of a shortest path;
- a marked component cannot contain a cycle. With maximum degree two, a component containing a cycle is that cycle, and a mark on it would have a two-edge path prohibited by Lemma 3.

Every component is therefore an unmarked path, an unmarked cycle, or a path with one mark. Isolated vertices are included in the path convention.

Assign each unmarked path edge to its child after choosing a root. Assign the edges of an unmarked cycle consistently around that cycle. For a marked path, assign the mark to its vertex, then orient the path away from that vertex and assign each edge to its child. These constructions assign EVERY split to a distinct incident open center edge. Therefore q<=h globally.

This pays the full demand in all components simultaneously. There is no hypothesis of disjoint bonus pairs, no separate R3 credit that might be reused, and no induction which stops at the smallest core.

## 6. Finish the entire C4=0 branch

The established Stage 48 packing and midpoint bound specializes here to

    N >= 248+h+R3-2q+E/2.

The source inverse gives E>=2q, and the global assignment gives q<=h. Hence

    N >= 248+h+R3-q >= 248+R3 >=248,

contradicting N<248. The entire no-ordinary-quartic-triple branch is closed.

No new arbitrary odd modulus is individually claimed excluded: the remaining putative counterexamples must have C4>0. This still includes quartic stars, paths and splits with t=0, as well as quartic triangles. It is not valid to say the remaining branch consists only of triangles.

## 7. Exact remaining global obligation

Keep the Stage 48 variables c,t,p,w,q,E, with E now counting only two-ordinary disjoint-tail quartic fibers and S4=p+2w+E. The general sufficient inequality

    5t+4q <= 2(h+R3)+2c+5w+E

is still unproved. The cap-two local contradictions above often produce quartic PATHS or STARS; in the general branch those are configurations to account for, not contradictions. Two isolated-root cases produce triangles. A correct extension must retain their exact fibers, prove ownership of their incidences, and combine them with triangle doubling-path reuse.

The next proof task is this joint accounting for C4>0, retaining the original quartic/cubic-quintic finishing target and available slack. The P3<=17 audit, Stage 45 residual558, historical modulus discovery, and equality at248 are unchanged. The goal is not marked complete.
