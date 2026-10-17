# The final contradiction and equality

The lower bound depends on the computer-assisted seven-point/even-order lemmas,
multiplicity caps, split-source and assignment lemmas, ownership, and alignment
exclusions. The final substitution and equality proof are elementary. This chapter
assembles the hypotheses in one place.

## The odd-order conclusion

Assume a valid eight-set in odd order $N\le247$. Use the notation of [Lemma
6](counting.md), so all counts $h,R_3,c,t,w,q,E,o$ are nonnegative. The established
statements are

$$
\begin{gathered}
2N\ge496+2(h+R_3+c)-5t+5w-4q+E,\\
E-2q\ge0\quad\text{(Lemma 7)},\qquad
q\le h-o\quad\text{(Lemmas 8–9)}.
\end{gathered}
$$

If $t=0$, these already imply $2N\ge496$. Therefore there is a triangle. Lemmas 11
and 14 leave only the forests $(2,2,2,1,1)$, $(4,2,1,1)$, and $(3,2,2,1)$ in each
triangle-bearing class. Lemma 15 permits just one such class, and Lemma 16 excludes
the last forest. Thus $t=1$.

By [Lemma 10](alignment.md#lemma-10-terminal-paired-edges-are-open-elementary), a
paired edge is open exactly when it is terminal. In $(2,2,2,1,1)$ the three paired
edges are terminal, giving $o=3$. In $(4,2,1,1)$ the unique triangle uses the first
and last edges of the four-vertex path and the separate two-vertex path; the latter
two are terminal, giving $o=2$. No no-new-equality hypothesis is imposed.

Set $U=E-2q$. The four final inputs are therefore

$$\boxed{U\ge0,\qquad q\le h-o,\qquad t=1,\qquad o\ge2.}$$

Substitution, retaining the other nonnegative terms, gives

$$
2N\ge496+2(h-q+R_3+c)-5t+5w+U \ge496+4-5=495>494.
$$

This contradicts $N\le247$. [Lemma 4](parity.md) excludes all even orders
below 248, completing the proposed lower bound.

## Equality at 248

Let $a_i=2^i-1$ for $0\le i<8$. A nonnegative degree-eight word at the
original target modulo 248 would have

$$S=\sum_i m_i2^i\equiv 255\pmod{248},\qquad 8\le S\le1024.$$

Thus $S$ is 255, 503, 751, or 999. For coins $1,2,\ldots,128$, the minimum number
needed to represent $S$ is

$$\left\lfloor S/128\right\rfloor+\operatorname{popcount}(S\bmod 128).$$

Carry pairs of equal smaller coins upward. Each carry reduces the count;
the unique carry-free representation has the displayed count. The four
minima are respectively 8, 9, 11, and 12. Only 255 uses eight terms, and
its unique minimum representation uses every denomination once. Hence
$\{0,1,3,7,15,31,63,127\}$ is valid modulo 248.

This is also the $n=8$ case of [Fonollosa's fixed-construction theorem](../docs/references.md).
The verifier separately enumerates all 6,435 degree-eight words here; that
check supplements the hand proof and does not establish the arbitrary-set bound.
