# Relationship to existing work

José A. R. Fonollosa, *Minimum modulus for the unique multiset-sum problem*,
[arXiv:2607.08366v2](https://arxiv.org/html/2607.08366v2), 14 July 2026,
proves that the **fixed** construction

$$A_n=\{2^i-1:0\le i<n\}$$

first becomes valid at $2^n-2^{\lfloor\log_2 n\rfloor}$. Theorems A and B
concern that construction. Conjecture 1 asks for the same lower bound over
**arbitrary** $n$-element sets in cyclic groups. Section 7 reports CP
certification through $n=7$ and search evidence through $n=13$; those
computations were not repeated in this review.

The associated [jarfo/min-modulus](https://github.com/jarfo/min-modulus)
repository was inspected at commit
[`e7c78dd63955092b5f8d8a5fa826476337c0f4be`](https://github.com/jarfo/min-modulus/tree/e7c78dd63955092b5f8d8a5fa826476337c0f4be).
Its `MinModulus/UniqueSums.lean` defines `a i = 2^i-1`; `Valid n N` uses
that fixed `a`, and `nmin_eq` proves its least valid modulus. It does not
quantify over arbitrary eight-element sets. The source and README were
read; its Lean build and axiom audit were **not** rerun here.

The same repository also reports Michael Inal's all-finite-abelian-group
result, $2^{n-1}$, and supplies a separate formalization. That minimum is
over a different class of groups and does not establish the cyclic bound
248. This review does not independently assess that result.

The proposed contribution of the present repository is the $n=8$ case of
Conjecture 1: an arbitrary valid cyclic eight-set requires order at least
248. The equality example and its binary-coin argument are already covered
by Fonollosa's theorem. No classification of cyclic equality cases is
claimed, and no novelty claim follows from this limited literature check.

AI assistance, arithmetic certificate checking, independent external human
review, and proof-assistant certification are distinct. This repository has
the first two; it does not claim the latter two. No license is selected or
borrowed from the cited repositories.
