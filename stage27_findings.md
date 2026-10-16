# Stage 27: no seven-point doubling overlap below 248

Meaningful continuation checkpoint after Stage 26. The universal theorem
and active research goal remain OPEN. This stage makes a new elementary
restriction on h>0 counterexamples; it does not restart regular cases.

## 1. Odd-subgroup theorem

**Theorem.** If A is valid, has eight points, and has odd cyclic
difference-generated subgroup H with |H|<248, then

    |2A intersect (A+t)|<=6 for EVERY t in H.

Oddness already rules out antipodes. The existing cubic packing gives
|H|>=184, hence |H|>=185. Overlap eight is affine doubling stability,
whose historical elementary classification gives |H|=255, impossible.
It remains to exclude overlap seven. The proof below uses no MC,
external seven-point certification, or assumption h=0/R3=0.

Translate A first into H. An overlap shift t is in H because t=2a-b
for one overlap pair. Put B=A-t, so |2B intersect B|=7. Translating
preserves validity and the difference subgroup. Oddness makes doubling
injective, so the directed partial map b->2b on B has seven edges on
eight vertices, indegree/outdegree at most one. Its components are
exactly ONE path, with L vertices, and zero or more directed cycles.
An isolated vertex is a path of length L=1.

There is no fixed point: a fixed point is 0, and if 0 is in B then
every nonzero doubling edge b->2b would give the forbidden pair equality
2*b=0+(2b). Overlap seven includes nonzero edges, so 0 cannot be in B.
Every cycle therefore has at least two vertices. Its sum is zero:
doubling permutes its points, so 2 sum C=sum C.

An expansion on a cycle replaces a point by two copies of its predecessor.
It preserves the sum and raises the number of terms by one, indefinitely.
Expanding a path point other than its first point does the same, until
all path terms are copies of its first point.

### At least two cycles

Take the whole path and just one cycle. Its sum equals sum B because
all omitted cycles sum to zero. It starts with fewer than eight terms.
Expand points in the selected cycle until it has eight terms. This gives
a rival supported on a proper subset of B. Thus there is at most one cycle.

### One cycle and L>=4

The path is {x,2x,...,2^(L-1)x}; its sum is (2^L-1)x=sum B.
Its L terms can expand, one term at a time, to 2^L-1 copies of x.
Since 2^L-1>=15, it can reach exactly eight terms. The resulting multiset
uses only the path, omits the cycle, and is a rival. Thus L<=3.

### One cycle and L=1

The cycle has seven vertices. Its first point y has order dividing
2^7-1=127, and exact doubling-cycle length seven makes that order 127.
Thus 127 divides |H|, impossible for odd 185<=|H|<=247.

### One cycle and L=2

The cycle has six vertices. Its point order divides 63. Six Sidon points
have 30 distinct nonzero differences inside that subgroup, so its order
is at least 31. The only divisor of 63 of that size is 63. Thus its
generated subgroup J has order63, and the only odd multiple in the
range is |H|=189. The quotient H/J has order three.

The path sum 3x lies in J; every residue in J is a sum of at most six
cycle points, except zero which is represented by all six. This follows
from the binary residues 1,2,4,8,16,32 in Z/63. Any such representation
can expand cyclically to exactly eight terms. A rival entirely within
the cycle therefore realizes the target sum, omitting both path points.

### One cycle and L=3

The five-cycle generates J of order31, since its point order divides
the prime 2^5-1=31. The only odd multiple in the range is |H|=217.
The quotient H/J has order seven, so the path sum 7x lies in J.
The binary five-cycle represents every residue of J with at most five
terms (zero by all five). Cyclic expansion again gives an eight-term
rival supported entirely on the cycle.

### No cycle

All eight points form the path {x,2x,...,128x}. Differences include x,
so x generates H, and the target is 255x. Let r=255-|H|, which is an
integer in [8,70]. Its ordinary binary expansion uses at most seven
of the allowed powers 1,2,...,128. Splitting powers into equal halves
raises the number of terms one at a time, up to r copies of one.
Hence r is a sum of EXACTLY eight allowed powers. This represents
255x modulo H with an eight-term multiset different from all ones,
whose integer power sum is 255 rather than r. Contradiction.

These cases exhaust the partial-map decomposition and prove the theorem.
No finite numerical search is a premise of the new odd theorem.

## 2. Quantitative connection to the remaining budget

In the odd singleton-base forest at b, the indegree of d equals

    |2A intersect (A+(2d-b))|-1.

Each other overlap point a contributes precisely the edge a->d labeled
2a-(2d-b); the excluded point d itself gives the base label b. Thus every
indegree is now at most FIVE for any putative odd counterexample N<248,
including h>0 and R3>0. The forest has 7-s_b edges, and sum s_b=2h.

This supplies the same local degree cap that powered the completed
regular argument, but with extra roots and without importing its cycle
or path exclusions. The remaining quantitative step is to couple those
forest deficits to Sigma-D, or to further constrain the small modulus.
The theorem does not provide that coupling by itself.

For any such forest, sum binomial(indeg,2)<=11 by distributing at most
seven edges into parts of size at most five. The aggregate bound is
at most88 incoming pairs. Identifying these with a particular graph
cycle budget when multiway cubes or missing directions occur requires
additional proof. No conjectural inequality for Sigma-D is asserted.

## 3. Even small-h branch: explicit conditional reduction

If seven A-points lie in one parity coset of even H, their affine
division by two is a VALID seven-point set in H/2. Any competing
seven-term multiset there lifts to the seven original points; adding
the eighth A-point creates a rival eight-term multiset. This elementary
implication needs no doubling-closure assumption.

Consequently, USING the historical external n=7 lower bound124,
the parity split1+7 forces |H|>=248. Stage25 proves that every even
non-antipodal set with 1<=h<=4 has precisely that split. Conditional
on the external certification, any remaining even counterexample below
248 must therefore have h>=5 and a 2+6,3+5,or4+4 split.

This does not independently recertify the seven-point result or upgrade
its source boundary. Without that dependency, the new proved implication
is the valid seven-point quotient, not the numerical124 bound. Odd
overlap restriction in Section1 has no such external dependency.

## Stopping state and next promising step

Stage26 finishes h=0 for the 248 modulus target. Stage27 removes every
odd seven/eight-overlap configuration from a putative smaller modulus,
and makes the even small-h quotient dependency explicit. The active
goal remains the full universal theorem. Its weakest current step is
a quantitative bound for the remaining h>0 forests/fresh loss, or a
direct contradiction for those small-group configurations.

Do not infer D=0, regular unpaired permutations, short global paths,
or the required Sigma-D budget from the indegree cap. Substantive
findings are delivered with Stage26 in a new unmerged PR based on PR#7.
