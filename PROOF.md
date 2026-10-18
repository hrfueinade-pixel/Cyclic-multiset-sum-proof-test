# The eight-point cyclic minimum

## Statement

Let $A=\lbrace a_0,\ldots,a_7\rbrace\subset\mathbb Z/N\mathbb Z$ have eight
distinct elements. Call it **valid** if the only nonnegative integers
$m_0,\ldots,m_7$ satisfying

$$
\sum_i m_i=8,\qquad \sum_i m_i a_i=\sum_i a_i
$$

are $m_i=1$ for all $i$. Equality in a cyclic group is always modulo its
order. The theorem is that a valid set requires $N\ge248$, and that
$\lbrace 0,1,3,7,15,31,63,127\rbrace$ is valid at order 248.

This is the proposed arbitrary-set lower bound, extending the fixed-binary
construction result of [Fonollosa](docs/references.md). It has not received
independent external mathematical review or proof-assistant certification.

The argument below is a proof with finite computational lemmas. Each such
lemma is identified at its point of use. Its mathematical reduction is in a
supporting chapter, and its exact input files are listed in the
[dependency ledger](certificates/dependencies.json).

## Lemma 1. Protection and invariance (elementary)

A **word** is a nonnegative integer count vector; its degree is the sum of
its counts. It is **squarefree** if every count is zero or one. A word that
differs from the original and has degree eight and value $s=\sum A$ is a
**rival**. Every squarefree word on a valid set is protected against a
different word of the same degree: append its squarefree complement to get
a rival. In particular, every subset of a valid set is valid for its own
degree. Translation and multiplication by a unit preserve validity.

## Lemma 2. Complementary packing (elementary)

Assume validity. Write $dA$ for degree-$d$ values, $Q_d$ for the
squarefree values, and $\mathcal T_d$ for the values of words with a repeated
label. Set $T_d=|\mathcal T_d|$. Protection makes $Q_d$ and $\mathcal T_d$
disjoint. No multiplicity cap is used in this lemma.
For eight points, $|Q_3|=|Q_5|=56$ and $|Q_4|=70$.
Complementation gives

$3A\cap(s-5A)=Q_3$: a concatenated degree-eight word at the target
must be the original squarefree word. Taking the union therefore gives

$$
N\ge56+T_3+T_5.                                      \tag{1}
$$

For odd $N$, independently of multiplicity caps, the 64 repeated cubic words form eight
translates $2a+A$. Each pair of translates intersects at most once, by
ordered-difference uniqueness. Thus $T_3\ge64-28=36$.

Also $4A\cap(s-4A)=Q_4$. For odd $N$, the midpoint $s/2$ is outside $4A$: doubling a
four-term representation would give a rival with all counts even. Hence

$$
N\ge71+2T_4.                                        \tag{2}
$$

Thus a hypothetical odd counterexample has $T_4\le88$ and
$T_3+T_5\le191$. These two bounds drive the finite symbolic lemmas;
none requires searching over all cyclic moduli.

## Lemmas 3–4. Seven points and even orders (computer-assisted)

The [parity chapter](proof/parity.md) proves the seven-point bound 124 first,
using a complete six-point enumeration and all its surviving extensions,
plus all necessary antipodal lifts. It then establishes the elementary
eight-point baseline $N\ge187$. This ordering avoids using the
eight-point theorem as a premise of the seven-point computation.

An antipodal pair means two points differing by half the group order.
Identifying such a pair projects a valid $n$-set to a valid
$(n-1)$-set in the half-order group. Thus an antipodal eight-set already
requires $N\ge2\cdot124$.

For a non-antipodal eight-set in order $2M<248$, translate to choose the
smaller parity block. A $0+8$ split contradicts the 128 distinct subset
sums in a half-order coset; a $1+7$ split contradicts the seven-point
bound in $\mathbb Z/M\mathbb Z$. The other splits are $2+6$,
$3+5$, and $4+4$. The baseline leaves exactly $94\le M\le123$.
The three complete finite exclusions in the parity chapter eliminate them.
All even orders below 248 are therefore excluded.

## Lemmas 5–6. Multiplicity and the weighted count

Assume now that $N<248$ is odd. An **ordinary degree d word** has
one doubled point, its **center**, and $d-2$ distinct other points, its
**tails**. A **fiber** consists of all words with one value. A center of an
ordinary word cannot occur in another word of its fiber: canceling it
would violate squarefree protection.

The [multiplicity chapter](proof/multiplicity.md) proves, with symbolic
certificates, that total repeated cubic multiplicity and ordinary quartic
and quintic multiplicity are all at most three. These are statements
under the present small-order hypothesis.

Let $\Delta$ be the set of nonzero differences of distinct points. It has
56 elements: an equality of two ordered differences either contradicts
squarefree pair protection or reverses an antipodal pair; odd order excludes
the latter.
An unordered center edge $\lbrace u,v\rbrace$ is **open** when
$2(u-v)\notin\Delta$. Let $h$ count these edges. Put
$R_3=\sum_{y:m_y\ge1}\binom{m_y-1}{2}$, where $m_y$ is the number of the
64 repeated cubic words at $y$. Pair uniqueness gives

$$
\sum_y\binom{m_y}{2}=28-h,\qquad T_3=36+h+R_3.       \tag{3}
$$

The three-tail-edge graph of a quartic triple, or the three-omitted-edge
graph of a quintic triple, has one of four types: triangle, star, path,
or split (a two-edge path and a disjoint edge).

For a quartic triangle written
$2x+b+c=2y+a+c=2z+a+b$, its **paired edges** are
$\{x,a\},\{y,b\},\{z,c\}$. These are six distinct labels, with common
alignment $2x-a=2y-b=2z-c$. The paired edges differ from pairs of its
ordinary word centers.

| Symbol | Count |
| --- | --- |
| $c$ | Ordinary cubic triple outputs |
| $t$ | Ordinary quartic triangle outputs |
| $w$ | Ordinary quartic split outputs |
| $q$ | Ordinary quintic split outputs, called genuine splits |
| $E$ | Quartic outputs with exactly two ordinary words and disjoint tails |
| $o$ | Distinct open paired center edges belonging to quartic triangles |

The [counting chapter](proof/counting.md) derives, without assigning any
fresh outputs by assumption,

$$
2N\ge496+2(h+R_3+c)-5t+5w-4q+E.                    \tag{4}
$$

Its key steps are exact cubic-to-quartic-to-quintic pair lifts, the
quartic budget $T_4\le88$, and coverage of 36 protected midpoint
values. Path contributions cancel. The common-tail correspondence for
quintic paths is stated explicitly to correct the historical error.

## Lemmas 7–9. Sources, assignment, and ownership

Each genuine split has two recoverable quartic sources. The
[assignment chapter](proof/assignment.md) proves that both are counted
in $E$, that a source cannot be used twice, and that the splits admit
an injective assignment to incident open center edges. The proof combines
complete finite local configurations with an elementary argument on paths
and cycles in an auxiliary graph. The general version replaces every
inference that had previously assumed ordinary quartic cap two.

The [triangle ownership lemma](proof/alignment.md#lemma-9-triangle-edge-ownership-computer-assisted)
excludes paired triangle edges from the source assignment. Thus

$$
E\ge2q,\quad q\le h-o,\quad U:=E-2q\ge0.
$$

Equation (4) becomes

$$
2N\ge496+2(h-q+R_3+c)-5t+5w+U.                    \tag{5}
$$

If $t=0$, its right side is at least 496. Every remaining hypothetical
counterexample must therefore contain a quartic triangle.

## Lemmas 11–16. Alignment exclusions

The edges of a triangle have common alignment $\tau=2x-a$. Translate
all labels by $-\tau$, with no division. Its three disjoint edges then
have the form $u\to2u,v\to2v,w\to2w$.

The [alignment chapter](proof/alignment.md) supplies the following chain.

1. A hand proof excludes cycles in a triangle-bearing alignment class.
   The alignment graph is a union of paths with maximum matching three.
   There are exactly nine partitions of the eight vertices.
2. A complete certificate excludes the six large forests. Only
   $(2,2,2,1,1),(4,2,1,1),(3,2,2,1)$ remain; every alignment class has
   at most four edges.
3. A complete interaction certificate permits only one triangle-bearing
   alignment class globally.
4. A complete certificate excludes $(3,2,2,1)$, including all required
   extra ordinary and pure relations. Its separate incomplete research
   trees are not premises of this proof.

The supporting source-count, low-collision, and one-split lemmas used in
those certificates are included in that chapter. Consequently $t=1$,
and only the first two forests remain.

## Lemma 10 and the final contradiction

Lemma 10, proved independently of the forest exclusions, says that a terminal
paired edge stays open even if other relations are added. In a set containing three disjoint doubling pairs, there is
no equality $x+y=z$ with distinct physical labels $x,y$. Choose a
doubling pair $b,2b$ disjoint from them. Replace
$x,y,b,2b$ by $z,b,b,b$ in the original word. This gives a rival,
since only one of the two removed labels $x,y$ can be restored by $z$.

For an aligned edge $a\to b=2a$, closure would mean
$2(a-b)=x-y=-b$, hence $y=x+b$. The preceding lemma forces $x=b$
and $y=2b$. Closure is therefore equivalent to an outgoing edge from
$b$. Every terminal edge is open.

In $(2,2,2,1,1)$ all three triangle edges are terminal. In
$(4,2,1,1)$, the last edge of the four-vertex path and the separate
two-vertex path are terminal. Thus $o\ge2$. Since $q\le h-o$ and
all other credits are nonnegative, (5) gives

$$
2N\ge496+4-5=495>494,
$$

contradicting $N<248$. Together with the even case this proves the bound.

## Equality

Put $a_i=2^i-1$. A degree-eight word at the original target modulo 248
would have $S=\sum_i m_i2^i\equiv255\pmod{248}$, with
$8\le S\le1024$. Thus $S\in\lbrace 255,503,751,999\rbrace$.
For coins $1,2,\ldots,128$, the minimum coin count at $S$ is
$\lfloor S/128\rfloor+b(S\bmod128)$, where b(r) is the number of 1-bits
in r. To obtain this formula, carry every pair of smaller equal coins
upward. The four minima are 8, 9, 11, 12.
Only 255 can use eight coins, and its unique minimal representation uses
every denomination once. This proves the stated equality example.

The [closing chapter](proof/closing.md) assembles the hypotheses and final substitution. The verifier also checks all 6,435 degree-eight words of the
equality example as a consistency control. This direct check supplements
the coin proof.
