# Round 3 of 8: regular paths have at most three vertices

Hypotheses: validity, eight points, odd cyclic H, h=R3=0.
New result: every nontrivial quartic propagation path has length two
or three. This is a computer-assisted restriction with independently
reconstructed complete finite coverage, not a set census.

First, any path contains at most two 31 vertices. Three consecutive
31s are excluded by Stage 17's integer identity and order-five lemma.
For any other placement of three, one is nonadjacent to each of the
other two. Their centers then all lie in one order-five coset, by
Stage 8 Lemma 2.1. Six distinct ordered differences of these three
centers cannot fit its four nonzero elements. This also uses that
distinct 31 vertices at a value have different centers.

There is at most one 22 vertex. Every 31 is adjacent to it, since
disjoint 22/31 equalities are excluded by Stage 8 Lemma 2.2.
There is at most one pure quartic in a fiber, by odd doubling and
pair uniqueness. It is an endpoint, its neighbor is ordinary, and
there is no 22 at its value. A shared 31 neighbor would give either
identical points or an order-three difference (Stage 9).

For a path of L vertices, the L-1 shared edge-points are distinct.
Every ordinary center is private. A nonpure endpoint contributes
one additional private point: for ordinary this is its other tail
(as well as its already counted center), for 31 its center, and for
22 its second point. A 31 endpoint shares its singleton, since
deletion of the singleton leaves its paired pure cubic. Thus support
size is exactly

    L-1 + number_of_ordinary_vertices + number_of_nonpure_endpoints.

No L>=9 is possible: eight edge-points leave no space for a nonpure
endpoint, and two pure endpoints are impossible. All L=4,...,8 type
words are scanned, up to reversal, after just the restrictions above
and the eight-point support bound. Every internal 31 orientation is
checked, with precisely the path's consecutive support intersections.
Endpoint private points remain distinct symbols; unused A-points are
also separate symbols. No group realization is pruned by assuming a
minimal presentation or by inverting an odd denominator.

All necessary disjoint O/O, P/O, P/P roles are attached just as in
Round 2, including all combinations. Each of the 498 resulting
branches has a saved exact dyadic eight-term rival certificate.
There are zero symbolic survivors. Producer completed in 1.172 seconds
under 60 seconds. A separate path construction, with no producer
import, reconstructed all 498 branches and verified every identity,
rejecting 996 altered/noninteger certificates under 30 seconds.
The certificate search shares the Round 2 producer's linear algebra;
the independent integer audit does not. Completion proves only the
stated path exclusion and retains the historical elementary premises.

**New numerical consequence.** There are 36-c2 nontrivial paths,
each with at most one internal vertex. Hence I<=36-c2. Round 2 gives
only triangles, so

    C >= ceil((152+2c2)/3),
    |T4| >= 36+ceil((152+2c2)/3) >=87,
    N >=70+2|T4| >=244.

In this regular odd branch c2>=3 already suffices for N>=248.
The even h=0 branch historically has N>=254. Neither result treats
odd h=0,R3>0 or h>0 in full. The remaining regular obligation is
at least 7-2c2 two-vertex paths. Round 3 checkpoint saved.
