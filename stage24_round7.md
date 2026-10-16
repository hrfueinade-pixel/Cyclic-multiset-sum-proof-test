# Round 7 of 8: complete classification of the regular odd branch

**Computer-assisted theorem.** If A is valid, has eight distinct points,
has odd cyclic difference subgroup H, and h=R3=0, then 2A=A+t for
some t. Consequently |H|=255 and A is affine equivalent in H to
the binary orbit {1,2,4,8,16,32,64,128}. In particular |T4|=92 and
N>=255 in this branch. This exceeds the requested 248 target here.

This theorem uses the complete checked cycle and path exclusions in
Rounds 2/3, and the elementary Stage 5 singleton-tree and Stage 6
homometric-overlap lemmas. It does NOT use MC, the local endpoint
work, external n=7 computation, a modulus search, or Round 1's finite
spectrum enumeration. It is not claimed as a wholly elementary proof.

## Numerical contradiction, with all dependencies explicit

Suppose A is not affine doubling-stable. The Stage 6 overlap lemma
then bounds each tree indegree by five. Each of the eight trees has
seven directed edges, so its incoming degrees sum to seven. Convexity
gives sum binomial(indeg,2)<=binomial(5,2)+binomial(2,2)=11:
moving one unit from a smaller positive part to a larger part cannot
decrease this sum, until the largest part is five.

The incoming-pair/triangle bijection proved in Round 1 therefore gives

    u3 <= floor(8*11/3) =29,

where u3 counts triangles WITHOUT 22. This elementary version is
weaker than the independently computed u3<=26 and is already sufficient.

Rounds 2 and 3 show every cycle is a triangle and every nontrivial
path has two or three vertices. The fixed-point-free unpaired
permutation has c2 two-cycles, 0<=c2<=4. The 28 type-22 vertices
split into c2 isolated, 8-2c2 endpoints, and 20+c2 degree-two vertices.
Each triangle containing a 22 uses one DIFFERENT degree-two 22, since
components are disjoint and no fiber has two distinct 22 representations.
Thus, with q3 the number of such triangles,

    q3 <=20+c2,
    C=u3+q3 <=49+c2.

There are 36-c2 nontrivial paths and at most one internal vertex each:
I<=36-c2. The exact degree-two count is

    3C=188+c2-I >=152+2c2.

Combining gives

    152+2c2 <=3C<=147+3c2,
    hence c2>=5,

contrary to c2<=4. Therefore the affine-stable case is forced.
Stage 5's elementary carry/classification theorem gives |H|=255.
For its binary orbit, repeated quartics carry to unique squarefree
multisets of sizes one, two, or three. Each is reachable by expansions
to length four. Their 8+28+56=92 sums are distinct, giving |T4|=92.

The budget in this entire branch is now proved: Sigma=C=56, D=0,
and |T4|=36+56=92>=89. Equivalently I+t4+2t5<=29+c2 follows.
The stronger structural classification, not just passing examples,
establishes the result.

## Verification and remaining theorem boundary

Before the arithmetic check: coverage is all c2=0,...,4 and all
partitions of seven with parts <=5; scope is the displayed finite
inequalities; runtime cap 10 seconds; completion verifies the numerical
contradiction only. The standalone checker imports no project code,
reconstructs the maximum 11 and the five incompatible upper/lower bounds,
and saves them. The structural proof above is the coverage argument;
the arithmetic is not a classification search.

Odd h=0,R3>0 still needs control of isolated-ordinary fresh fibers
AND its Sigma-D budget. Even h=0 was historically classified at 254.
The h>0 branch remains required and is addressed separately in Round 8.
The antipodal route's reported n=7 certification remains external,
not independently recertified. The original theorem is OPEN.
Round 7 checkpoint saved.
