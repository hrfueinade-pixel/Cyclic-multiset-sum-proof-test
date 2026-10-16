# A new structural restriction: quartic aperiodicity below 285

This is an elementary proof. It uses no enumeration, MC, previously
computed minimum, or external seven-point certification.

## Theorem

Let A be a valid eight-element set in a cyclic group G of odd order
N<285. Then4A has trivial translation stabilizer. Consequently kA
has trivial stabilizer for each k=1,2,3,4.

Here kA allows repetitions. Valid means the all-ones eight-term
multiset is the unique eight-term representation of s=sum A.

## 1. The quartic intersection has exactly70 elements

Let Q be the set of sums of four DISTINCT elements of A. Hereditary
validity makes its70 sums distinct: another four-term representation
of any such sum, when joined to its four-point complement, would
give an eight-term rival. In particular no repeated quartic multiset
has a Q sum.

If x is in4A intersect(s-4A), choose four-term representations for
x and s-x. Their concatenation represents s in eight terms, so
validity forces each to be a complementary squarefree four-subset.
Conversely every such subset qualifies. Hence

    4A intersect(s-4A)=Q, with |Q|=70.

Let H={h in G:4A+h=4A}. Both4A and s-4A are H-invariant, so Q is
a union of H-cosets. Thus |H| divides70 and N. If H is nontrivial,
odd order forces |H| to be5,7,or35; in particular |H|>=5.

## 2. Every four-subset remains valid in the quotient

Fix a four-subset C of A and its complementary four-subset E.
Suppose a non-original four-term multiset M supported on C satisfies

    sum M=sum C modulo H.

Put e=sum M-sum C in H. Since sum E is in4A and4A is H-invariant,
there exists a four-term multiset L supported on A with
sum L=sum E-e. Then M followed by L is an eight-term representation
of s. It cannot be the original multiset: M uses only C and differs
from C; if the eight counts were all ones, L would have to contain
the four outside points E once each, using every available term,
and could not repair the wrong counts on C. This contradicts validity.

Therefore all four-position subsets remain hereditary valid after
projection to G/H. In particular projected points are distinct:
if two coincide, replace one by the other in a four-subset containing
both and apply the preceding argument.

## 3. The projected eight points have56 distinct nonzero differences

Any equality between two different squarefree pair sums in G/H, or
between a squarefree pair and a doubled point, involves at most four
points of A. Include all involved points in some four-subset C.
Replacing the first pair by the second and retaining C's other two
terms gives a non-original four-term multiset supported on C with
the same quotient sum. Section2 forbids it. Thus every squarefree
pair has a unique two-term representation among the projected points.

For completeness, equality of ordered differences

    a-b=c-d, with a!=b and c!=d,

gives a+d=c+b. If an endpoint repeats, either this is the same ordered
pair, or it equates a squarefree pair with a doubled point, which
was just excluded. If both sides are doubles, odd quotient order
makes doubling injective and again forces the same ordered pair.
Otherwise it is an equality of different squarefree pair sums and
is excluded. Projected points are already distinct. Thus all8*7=56
ordered differences are distinct and nonzero, so

    |G/H|>=57.

If H were nontrivial, N=|H|*|G/H|>=5*57=285, contradiction.
Therefore H is trivial. A period of kA for k<=4 is also a period
of4A=kA+(4-k)A, which proves the final assertion.

## Separate logical check and connection to 248

The proof was checked in two equivalent forms: quotient validity of
each four-subset, and directly correcting the H-error of a pair
replacement by a four-term multiset. Both require the replacement
to be supported on the selected C. The argument does NOT assert
that the entire projected eight-set is valid, which would be stronger
and is not justified. It needs only the pair restriction. No computational
check, separate human review, or formal proof assistant is claimed.

Every remaining odd N<248 counterexample therefore has APERIODIC4A.
This removes the periodic alternative from a sumset-growth approach.
It is a new proved restriction, not a relabeling of the quartic-loss
identity. It alone does not establish |4A|>=159, equivalently
|T4|>=89, nor Sigma-D>=53-8(h+R3). Those remain required if the
general quartic-growth route is used. No novelty claim is made.
