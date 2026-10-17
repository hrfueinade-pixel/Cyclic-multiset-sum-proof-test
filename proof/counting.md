# Lemma 6. The weighted counting inequality

Assume a valid eight-set in odd order $N<248$. The dependencies are [protection and
packing](../PROOF.md#lemma-2-complementary-packing-elementary) and [Lemma
5](multiplicity.md): total cubic multiplicity and ordinary quartic/quintic
multiplicity are at most three. The proof here is elementary. Write $T_d=|\mathcal T_d|$ for repeated **values**, not words.

## Cubic collisions and the open-edge count

The 64 repeated cubic words are $2a+b$, including $3a$ when $a=b$. The 56 nonzero
ordered differences have unique ordered representations. For a fixed unordered
center pair $\{u,v\}$, a collision $2u+a=2v+b$ exists exactly when
$2(u-v)=b-a\in\Delta$; if it exists, the tails are uniquely recovered. Let $h$ count
center pairs without such a collision. If $m_y$ is total repeated cubic word
multiplicity, then

$$
\sum_y\binom{m_y}{2}=28-h,
\qquad R_3=\sum_{y:m_y\ge1}\binom{m_y-1}{2}.
$$

Consequently,

$$
T_3=64-(28-h)+R_3=36+h+R_3.
$$

The last identity follows fiber by fiber from $1=m-\binom{m}{2}+\binom{m-1}2$ for
$m\ge1$. Pure cubes are included. Set $k=h+R_3$.

## Ordinary pairs and outputs

An ordinary word of degree $d$ has one doubled center and $d-2$ distinct tails. Its
center is absent from every other word of its fiber, by cancellation and squarefree
protection. There are 56, 168, and 280 ordinary words in degrees 3, 4, and 5.

Let $P_d$ count unordered equal-value ordinary **word pairs**, and $S_d$ those pairs
with disjoint tails. Let $C_4$ count three-ordinary quartic **outputs**. Let $n_i$
count quintic outputs with exactly $i$ ordinary words, and $M$ repeated quintic
outputs with none. Mixed words at an ordinary output do not produce another value.
Exact fiber counting gives

$$
P_5=n_2+3n_3=140-\tfrac{1}{2}n_1+\tfrac{3}{2}n_3,
\qquad T_5=140+\tfrac{1}{2}(n_1-n_3)+M.
$$

The ordinary quartic output count satisfies

$$
O_4=168-P_4+C_4\le T_4\le88.
$$

Let $\delta=N-56-T_3-T_5\ge0$ be the unused packing space. Then

$$
N=232+k+\tfrac{1}{2}(n_1-n_3)+M+\delta.
$$

## The 36 midpoint values

For unordered label pairs $c,d$, allowing $c=d$, set $z=(s+c+d)/2$. The reflected
value $s-z=(s-c-d)/2$ is outside $3A$: a cubic word $W$ there would give the
nonnegative mass-eight rival $2W+e_c+e_d$ at $s$. It has at most two odd
coordinates, so differs from all-ones. These 36 midpoint values are distinct.
Squarefree pair protection handles every comparison involving a squarefree pair;
oddness makes doubles distinct.

If $z$ has two ordinary quintic words $V,V'$, private centers imply $V+V'\le2\mathbf{1}$ coordinatewise. Thus $2\mathbf{1}+e_c+e_d-V-V'$ is a nonnegative mass-eight word
of value $s$. Validity forces

$$
V+V'=\mathbf{1}+e_c+e_d.
$$

This is impossible for $c=d$. Otherwise its doubled coordinates identify
the centers as $c,d$, and each other label occurs in exactly one tail.
It is an $S_5$ pair. A third ordinary center is impossible because every
label is already present. The pair recovers its midpoint uniquely.

The disjoint sets $3A$ and $s-\mathcal T_5$ leave exactly $\delta$ residues
uncovered. Hence at most $\delta$ reflected midpoints are outside
$s-\mathcal T_5$. The remaining midpoints are disjoint-tail double outputs,
single-ordinary outputs, or mixed-only outputs. Therefore

$$
36\le S_5+n_1+M+\delta. \tag{6.1}
$$

## Recoverable pair lifts

Delete all common tails from an ordinary word pair. At degree four, a pair either
has one common tail and descends to a cubic pair, or has disjoint tails. A cubic
pair uses four physical labels, leaving four possible lifts. At degree five,
common-tail sizes 2, 1, and 0 give respectively a cubic pair with $\binom{4}{2}=6$
lifts, a disjoint-tail quartic pair with two lifts, or an $S_5$ pair. Deleting the
common tails is the inverse, so

$$
\begin{aligned}
P_4&=4P_3+S_4,\\
P_5&=6P_3+2S_4+S_5
    =\tfrac{3}{2}P_4+\tfrac{1}{2}S_4+S_5.
\end{aligned}\tag{6.2}
$$

These are word-pair identities, including all three pairs in a triple fiber. They
make no assertion that arbitrary lifted pairs have different outputs.

Since $P_4\ge80+C_4$, substitution of (6.2) into (6.1) gives

$$
\tfrac{1}{2}n_1+\tfrac{3}{2}n_3+M+\delta
\ge16+\tfrac{3}{2}C_4+\tfrac{1}{2}S_4.
$$

Subtract $2n_3$ and use the exact formula for $N$ to obtain

$$
2N\ge496+2k-4n_3+3C_4+S_4. \tag{6.3}
$$

Thus the branch $n_3=0$ is already impossible.

## Triple correspondences and the coefficients

For a quartic triple, its three tails are distinct edges on the five noncenter
labels. For a quintic triple, use the three omitted edges on those labels. The only
three-edge graph types are triangle, star, path, and split (a two-edge path and a
disjoint edge).

Write $c$ for ordinary cubic triple outputs; $t,p,w$ for quartic triangle, path, and
split outputs; $q$ for quintic split outputs; and $E$ for quartic outputs with
exactly two ordinary words and disjoint tails.

| Target | Recoverable construction |
| --- | --- |
| Quintic triangles: $c$ | Omitted edges $ab,bc,ca$ give tails $cde,ade,bde$. Delete the two common tails $d,e$; the cubic triple has precisely those two unused labels. |
| Quintic stars: $2t$ | Omitted edges $ha,hb,hc$ give tails $bcd,acd,abd$. Delete the unique common tail $d$; a quartic triangle has two unused labels for the inverse lift. |
| Quartic stars: $2c$ | Delete the common hub of tails $ha,hb,hc$. A cubic triple has two unused labels for the inverse lift. |
| Quintic paths: $p$ | Omitted edges $01,12,23$ have common tail 4. Delete it, leaving quartic path edges $23,03,01$. That path uses seven labels and has exactly one unused label. |

Private centers justify each removal. The cap of three ensures the lifted triple is
the whole ordinary fiber. Within one source, different added labels give different
values; across sources, the recoverable inverse prevents overcounting. A quintic
split has no common tail.

A quartic path contains one disjoint edge pair, a split two, and a triangle or star
none. Consequently the exact output identities are

$$
n_3=c+2t+p+q,\qquad C_4=t+2c+p+w,\qquad S_4=p+2w+E.
$$

Substituting in (6.3), the coefficients of $(c,t,p,w,q,E)$ are
$(2,-5,0,5,-4,1)$. This proves

$$
\boxed{2N\ge496+2(h+R_3+c)-5t+5w-4q+E.} \tag{6.4}
$$

No fresh output is assumed. Ordinary and total multiplicities, pairs and outputs,
and mixed-only fibers have separate roles throughout.
