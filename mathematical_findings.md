# Cyclic unique multiset sums: one bounded research stage

## Status and scope

The arguments below are rigorous elementary deductions developed in this run.
Their novelty in the wider literature has not been established. They do not
prove the general conjecture. No Lean was written or executed; no repository
was cloned; computations used explicitly selected small moduli.

The paper proves that the fixed set `{2^i - 1 : 0 <= i < n}` first becomes
valid at `2^n - 2^floor(log2(n))`. Global optimality over arbitrary cyclic
sets remains open. The paper reports certification through n=7 and search
evidence through n=13; these are reported results, not computations repeated
here. The later repository update records Inal's result: the minimum over all
finite abelian groups is `2^(n-1)`, with equality only in an elementary
abelian 2-group, up to translation and isomorphism. Thus the older paper's
abelian-group open problem has been settled, while its cyclic conjecture and
classification of cyclic minimizers remain open.

Sources:

- https://arxiv.org/html/2607.08366v2
- https://github.com/jarfo/min-modulus
- https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/Arxiv/2607.08366/MinModulus.lean

## Definitions

Let A={a_0,...,a_m} be valid in Z/NZ, where m=n-1. Validity means that
the only nonnegative integer vector k with sum k_i=n and sum k_i*a_i=sum a_i
is the all-ones vector. Translation preserves validity. Write

    b_i = a_i-a_0  (1 <= i <= m),
    s_T = sum_{i in T} b_i,
    S = {s_T : T subset {1,...,m}},
    s = sum_{i=1}^m b_i.

## Lemma 1: representations with one extra term

For any T of size r, the only multiset of the nonzero b_i with sum s_T
and length at most r+1 is T itself.

Proof. Suppose the other representation has multiplicities h_i and length l.
Set k_i=1-1_{i in T}+h_i for i>=1, and k_0=1+r-l. All these numbers are
nonnegative, their sum is m+1=n, and their weighted sum in the translated
tuple (0,b_1,...,b_m) is s-s_T+sum h_i*b_i=s. Validity forces every k_i=1.
Consequently h_i=1_{i in T} and l=r. QED.

This proves dissociation: if s_T=s_U, orient the equality so that |U|<=|T|,
then apply the lemma to the representation U of s_T. In particular |S|=2^m.

It also proves the exterior-doubling property:

    2*b_i != 0  ==>  2*b_i not in S.

Indeed, a nonzero double represented by a subset T must have |T|>=1;
the representation consisting of two copies of b_i has length 2<=|T|+1
and cannot be the squarefree representation T.

This condition is stronger than dissociation alone. For example, {1,2} in
Z/5Z has distinct subset sums 0,1,2,3, but {0,1,2} is invalid because the
multiset {1,1,1} has the same size and sum as {0,1,2}.

## Lemma 2: at most one doubled collision in a cyclic group

Write 2A={2*a : a in A}. Then |2A|>=n-1. If N is odd, |2A|=n.

Proof. Doubling has trivial kernel for odd N. For even N its kernel is
{0,t}, where t=N/2, so each doubled class has at most two elements.
If two different doubled classes each contained a pair, A would contain
four distinct elements a,a+t,c,c+t. But

    a+(c+t) = (a+t)+c.

Starting with the all-ones multiset, add one copy of a and c+t and remove
the copies of a+t and c. This is a different size-n multiset of the same
sum, contradicting validity. Therefore at most one doubled class has two
elements. QED.

The possibility of one pair is real: {0,1,3} in Z/6Z is valid and 2*0=2*3.
Thus an injectivity claim for doubling on A would be false.

## Proposition 3: stronger cyclic lower bounds

For a valid n-element cyclic set with n>=3,

    N odd:   N >= 2^(n-1) + n - 1,
    N even:  N >= 2^(n-1) + 2*n - 4.

Consequently, without a parity assumption,

    N >= 2^(n-1) + n - 1.

Proof. The set D=(2A-2a_0)\{0} has |2A|-1 elements. Lemma 1 says that
D is disjoint from S. For odd N, Lemma 2 gives |D|=n-1, proving the first
inequality by counting S union D.

Now suppose N is even. If some b_i is odd, pairing each subset T with
T symmetric-difference {i} shows that exactly half the 2^m distinct subset
sums are even. Every element of D is even. The even subgroup has N/2
elements, so

    N/2 >= 2^(m-1) + |2A|-1 >= 2^(m-1) + n-2.

This gives the second inequality. If every b_i is even, S lies entirely
in that subgroup and instead N>=2^(m+1)=2^n. This implies the claimed
even bound because 2^(n-1)>=2*n-4 for n>=3 (immediate by induction).
Finally 2*n-4>=n-1 for n>=3, yielding the parity-free bound. QED.

The same counting argument works in any finite abelian group G with a
surjective homomorphism G->Z/2Z on which at least one translated difference
is nonzero: |G|>=2^(n-1)+2*(|2A|-1). The restriction on |2A| in Lemma 2
uses the cyclic group's unique nonzero involution.

## Proposition 4: an odd equality obstruction

Suppose N is odd and N=2^m+m. A valid tuple would necessarily satisfy

    (2^(m-1)+2)*s = 0 mod N.

Therefore equality in the odd bound is impossible whenever

    gcd(2^m+m, 2^(m-1)+2)=1.

Proof. In an odd cyclic group the m nonzero doubles are distinct. Equality
in Proposition 3 means S and D partition the entire group. Each b_i appears
in 2^(m-1) subset sums, so sum_{x in S} x=2^(m-1)*s. Also sum_{x in D} x=2*s.
The sum of all residues of an odd cyclic group is zero. Adding gives the
displayed congruence. If the coefficient is invertible, s=0, contradicting
the distinctness of the empty and full subset sums. QED.

Two consequences:

- n=4: even N>=12; odd N>=11, but N=11 is excluded since gcd(11,6)=1.
  Thus every valid set has N>=12. The known construction at N=12 matches
  this, providing an elementary set-independent proof of the known minimum.
- n=6: even N>=40; odd N>=37, but N=37 is excluded since gcd(37,18)=1.
  Since N is odd, this gives N>=39 in the odd case, hence N>=39 overall.

Including parity rounding and this obstruction gives the following proved
lower bounds, compared with the conjectured minimum:

| n | Dissociation bound | Bound from these arguments | Conjectured minimum |
|---|---:|---:|---:|
| 2 | 2 | 2 | 2 |
| 3 | 4 | 6 | 6 |
| 4 | 8 | 12 | 12 |
| 5 | 16 | 21 | 28 |
| 6 | 32 | 39 | 60 |
| 7 | 64 | 71 | 124 |
| 8 | 128 | 135 | 248 |

The table does not assert the existence of valid sets at its lower bounds.
For n=8 the equality obstruction has gcd(135,66)=3, so its invertibility
argument does not exclude 135.

## Failed stronger lemma: almost disjoint translates

A tempting route was to prove that some translate S+g satisfies

    |S intersect (S+g)| <= 2^floor(log2(n)).

Counting the union would immediately prove the conjectured lower bound.
This proposed lemma is false even for a known optimal construction.

Take n=5, N=28, A={0,1,3,7,15}, valid by the paper's theorem. Its cube is

    S={0,1,3,4,7,8,10,11,15,16,18,19,22,23,25,26}.

For shifts g=1,...,14 the exact overlap sizes are

    8,5,12,10,6,9,12,9,8,10,8,9,10,8.

The overlap for -g equals that for g, and the overlap for g=0 is 16.
Thus every translate has overlap at least 5, exceeding the proposed
threshold 2^floor(log2(5))=4. This is an explicit counterexample, not a
failure to find a favorable shift.

A related naive claim that the repeated-coordinate face
2*b_i+S_{others} is always disjoint from S also fails: for the valid
A={0,1,3,7} modulo 12, 2*1+3+7=0, which is in S.

## Bounded experiments and limitations

`research_experiments.py` checks validity directly by enumerating size-n
multisets for each individual candidate; it does not search over a range of
moduli. It checks the canonical constructions for n=2,...,9, two explicit
additional examples, the dissociated-but-invalid example, the shift-overlap
counterexample, and the arithmetic equality obstruction. Its assertions
check the proved exterior and parity bounds on all valid inspected examples.
The largest direct candidate check has C(17,9)=24310 multisets.

As a limited screen, it inspects at most 350 normalized sets per explicitly
chosen pair (n,N) in {(3,5),(3,7),(4,13),(4,15),(5,29),(5,31)}, stopping
after three valid examples. The actual counts are 6,6,220,25,350,350,
respectively. No sampled valid set was found at (5,29) or (5,31), but the
separately checked canonical set at N=31 is valid: the sample's negative
result is not an infeasibility certificate. No general conclusion is drawn
from these sampled negative results.

All assertions passed. Experiments corroborate the proofs; the proofs do
not depend on random sampling or on the absence of sampled counterexamples.

## Precise remaining obstacles

1. The proved improvement is additive O(n), while the conjecture requires
   approximately another 2^(n-1) residues. Single doubled elements alone
   cannot provide that many exterior residues.
2. Multiplying exterior doubles by arbitrary subset sums does not preserve
   exteriority. Lemma 1 only excludes an alternative representation of
   length l at a subset target of size r when l<=r+1. Collisions against
   smaller-cardinality targets remain possible and occur in optimal sets.
3. Distinct repeated-coordinate representations can share a residue: in
   the valid four-element example modulo 12, 2*1=2*7. A successful larger
   packing argument must control these overlaps rather than count all
   repeated representations separately.
4. When the coefficient in Proposition 4 is not invertible, the first
   moment can permit a nonzero target of small order. Even when it is
   invertible, the argument only excludes equality, not a whole interval
   of moduli above the improved bound.
5. The two-translate approach cannot establish the full conjecture in
   general: its desired overlap estimate is explicitly false. A proof
   would need a larger or different family of representations, or a
   structural argument exploiting the length restriction globally.

This completes the requested research stage. The global cyclic conjecture
and any stronger unproved hypotheses remain unresolved.
