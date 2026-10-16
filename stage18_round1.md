# Round 1 of 8: singleton trees give a numerical restriction

Scope: valid eight-point sets in odd cyclic H, h=R3=0. The regular
path budget remains open. No historical calculation was rerun.

Let m_t=|2A intersect (A+t)|. Each overlap pair is b=2d-t. In the
singleton-base tree T_b, the indegree of d is m_(2d-b)-1: each other
overlap point supplies exactly the edge a->d with label 2a-t.
The case d=b has indegree zero by squarefree-pair validity.
Every row of this eight-by-eight indegree matrix sums to seven.

If m_t>=7, Stage 6's homometric one-point-difference lemma gives
2A=A+t. Stage 5 then proves |H|=255 and |T4|=92. Otherwise all
m_t<=6. Counting all matrix entries gives

    sum_t binomial(m_t,2)=28.

Pairs of incoming edges a->d, c->d in T_b, with different labels r,s,
give the triangle

    2a+b+s = 2d+r+s = 2c+b+r.

The three quartics are distinct: each two share a point and their
deletions are the distinct cubic marks defining the edges. Their tails
are distinct, so none is 22. They have degree two and form an entire
triangle. Conversely a triangle without 22 has three distinct shared
edge-points; each vertex is uniquely 2d+r+s on its incident points.
Its two neighboring vertices therefore reconstruct an incoming pair
at d in the tree based at the opposite edge-point. This is a bijection
between incoming pairs and triangle vertices, even when a vertex is 31.
Thus, writing u3 for triangles without 22,

    3u3 = sum_(b,d) binomial(indeg_Tb(d),2)
        = 3 sum_t binomial(m_t,3).

Let a_m count overlaps of size m, m=2,...,6. Necessarily
sum binomial(m,2)*a_m=28. The m*a_m entries of weight m-1 must pack
into eight rows of capacity seven. This is a relaxation: it discards
column constraints, diagonal positions, distinct shifts per row, and
group realizability. Discarding constraints cannot exclude a real set.

**New computer-assisted restriction:** outside the affine binary case,
u3<=26. Producer completely checked all 61 spectra allowed by the
pair budget, retaining 46 row-packable spectra and excluding 15.
The maximum is 26. All row witnesses and excluded spectra are saved.
A separate program independently enumerates the multisets of eight
integer row partitions of seven with parts at most five and reconstructs
the spectra from divisibility of part counts. It imports no producer.

Before execution: coverage was all those spectra/row partitions; scope
was this finite relaxation; both runtime limits were 30 seconds;
completion establishes only its extremum. Both executions completed.
See their JSON records for actual elapsed times and independent counts.
No random examples or cyclic-set enumeration are involved.

This is an UPPER triangle restriction, not a lower bound on cycles.
It sharpens the alternative to the binary case but does not prove
I+t4+2t5<=29+c2. In particular it identifies how much work a global
compatibility argument would still have to do. Round 1 checkpoint saved.
