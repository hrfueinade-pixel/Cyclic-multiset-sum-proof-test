# Stage62: one genuine split attached to the entire remaining class

Assume a full-valid eight-point set in an odd cyclic group of order
N<248. Stage60 restricts a triangle-bearing alignment class to one of
(2,2,2,1,1), (4,2,1,1), (3,2,2,1), and Stage61 proves that there is
at most one such class globally. These are already checked premises.

**Theorem.** At most one genuine quintic split has its unique ordinary
cubic descent in any quartic triangle of A. Hence, with D the set of
ordinary cubic pairs contained in triangles,

    q <= 4(P-|D|)+1.

For the first two shapes there is one triangle, so Stage59 proves the
claim. For the last shape, translate the alignment to zero and label

    A=(u,2u,v,2v,w,2w,p=4u,r).

There are exactly two triangles:

    L=(u->2u,v->2v,w->2w),
    H=(2u->p,v->2v,w->2w).

First, a cubic pair in two distinct triangles supports no genuine split.
The pair fixes two directed edges, since its ordinary centers and cross
tails are physical labels. Stage59 proves that the two labels added in
the quintic lift must be exactly the two labels on the third edge of
the supporting triangle. Two different third edges cannot give the
same added-label pair. The only other possibility is opposite directions
on the same pair, a two-cycle in the triangle-bearing class, already
excluded. This uses label sets, without cancelling by an odd integer.
In particular H's v/w descent supports no split.

Consider H's 2u/v descent, omitting the w->2w edge. Relative to H the
two free labels are u and r. Stage59's complete normal-form theorem
leaves only

    3w=2u+r, or 3w=u+2r.

In the first case the third quintic center is u. One source has centers
u and 2u, the paired edge of L. Stage58 forbids a genuine split with
that source. In the second case the original sum is

    sum(A)=7u+3v+3w+r=8u+3v+3r.

It equals the eight-term word consisting of two copies of p=4u, three
copies of v, and three copies of r. This is a different nonnegative
mass-eight word and contradicts full validity. The 2u/w descent is
identical after interchanging v and w. Thus H supports no split at all.

Every surviving split descending inside D must therefore be attached
to L, which supports at most one by Stage59. Splits descending outside
D are bounded by four per ordinary cubic pair, proving the displayed
inequality. This theorem alone does not prove N>=248.
