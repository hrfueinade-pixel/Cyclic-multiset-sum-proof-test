# Stage56: triangle alignment classes are forests

The full N>=248 theorem remains open. This hand argument applies to a
full-valid eight-point set in an odd cyclic group with N<248 and the
established ordinary quintic cap three. It makes no parameter or modulus
search and cancels no odd integer.

For a fixed alignment value tau, draw x->a when 2x-a=tau. Physical
distinctness and oddness give indegree and outdegree at most one. Translate
all labels by -tau; the edges become x->2x. A quartic triangle is exactly
a matching of three such edges, on six distinct labels.

## A block saturation lemma

Suppose a directed cycle has r distinct vertices. Its block is
B={delta,2delta,...,2^(r-1)delta}, where d=ord(delta) divides 2^r-1 and
the doubling orbit has length r. If d=2^r-1, then rB=H=<delta>.

Indeed every nonzero residue modulo d has a binary representation using
at most r block terms. Split any term into two copies of its predecessor
along the cycle until there are exactly r terms. Each split preserves its
value, including the wrap delta=2*2^(r-1)delta. The zero residue is the
sum of all r block terms. Thus kB=H for every k>=r.

Let C be the other m=8-r labelled positions and project to G/H. Any word
on C of degree at most m at the projected original sum can be completed
by at least r block terms to a mass-eight word at sum(A). Full validity
therefore forces that word to be exactly the original C word.

This graded property makes the 2^m subset sums distinct: equal different
subsets U,V, oriented so |V|<=|U|, would give the non-original word
V+(C\U) of degree at most m at the original sum. For m>0 the midpoint
of the original sum is outside the subset cube, by complementation and
oddness. Hence the quotient order M=N/d is at least 2^m+1.

## Exclude cycles of length at least three

The possible block orders follow by factoring 2^r-1 and retaining only
orders with doubling orbit length exactly r. The proper-order rivals below
have r nonnegative terms at the block's original sum, which is zero.
Appending every other original label once gives a non-original mass-eight
word. Every listed rival repeats a label, so differs from the original.

|Cycle length r|Possible d|Exclusion|
|---|---|---|
|3|7|The graded-five quotient lemma below gives M>=37, so N>=259.|
|4|5,15|For d=5 use 3*delta+2delta=0. For d=15 use M>=17, so N>=255.|
|5|31|M>=9, so N>=279.|
|6|9,21,63|For d=9 use 3*delta+3*(2delta)=0. For d=21 use 5*delta+16delta=0. For d=63 use M>=5, so N>=315.|
|7|127|M>=3, so N>=381.|
|8|17,51,85,255|For d=17 use 6*delta+2delta+128delta=136delta=0. For d=51 use 6*delta+32delta+64delta=102delta=0. For d=85 use 5*delta+16delta+2*(32delta)=85delta=0. The order d=255 itself gives N>=255.|

The cycles have length at most eight because there are eight labels. Thus
no alignment class contains a cycle of length at least three below248.

For completeness, here is the order-seven quotient lemma. A graded-valid
five-position set has 32 distinct subset sums S. Complementation gives
s-S=S and leaves the unique midpoint mu=s/2 outside S, so odd M>=33.
If 2c belongs to S, its subset must be a singleton: a subset U with at
least two terms gives the forbidden word 2c+(C\U) of degree at most five,
and the empty subset would give c=0. Thus draw c->2c whenever the double
belongs to C. Doubling is injective, and a cycle would have its labels
sum to zero, contradicting the subset cube. These arrows form paths.
The double of each terminal vertex is a distinct hole of S, and cannot
be mu, since 4c=s is a forbidden degree-four word. This excludes M=33.
For M=35 the only two holes apart from mu form a complementary pair. Two
different path exits would give 2c+2d=s, another forbidden degree-four
word. Hence there is one five-vertex path C={t,2t,4t,8t,16t}, with s=31t.
But 4*(16t)+2t=66t=31t in order35 is a non-original degree-five word.
Therefore odd M>=37, and an order-seven block forces N>=7*37=259.

## Exclude a two-cycle in a triangle-bearing class

A two-cycle is {delta,2delta}, where 3delta=0. A class with a three-edge
matching has two further mutually disjoint edges u->2u and v->2v,
disjoint from this cycle. If its matching avoids the cycle, choose any two
of its edges; otherwise use its other two. Let p,r be the remaining two
labels. The original sum is 3u+3v+p+r. The non-original mass-eight word
with three copies each of u and v and one each of p,r has that same sum.
Thus a triangle-bearing class contains no two-cycle either.

Four disjoint aligned edges are excluded by the ordinary quintic cap:
writing their labels as xi,2xi for i=1..4, the four distinct ordinary
quintic words 2xi+sum(j!=i)2xj have the same value. Consequently the
alignment graph of a triangle-bearing class is a disjoint union of paths
whose maximum matching has size exactly three.

## Complete primary forest shapes

Include isolated labels as paths with one vertex. The possible partitions
of eight vertices are exactly

    (2,2,2,1,1), (4,2,1,1), (3,2,2,1),
    (6,1,1), (5,2,1), (4,3,1), (3,3,2), (7,1), (5,3).

The six shapes with at least five edges have only the three- or two-root
models of successive powers of two. This classification covers a chosen
triangle-bearing alignment class. Other alignment classes and additional
cubic relations remain possible; the classification alone does not prove
the full bound or assume their absence.
