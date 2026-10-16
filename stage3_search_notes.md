# Stage 3 exact-search notes

This file records the exact-search subtask separately from the structural
research. No solver or external package was installed. Bundled Python 3.12
has no OR-Tools, Z3, SCIP, or SciPy; the implementation uses the standard
library and the pre-existing `research_experiments.py` validator.

## Exact extension lemma

Let P be a valid p-element set modulo N, let s=sum(P), and let H_r be the
set of all r-term multiset sums from P, with H_0={0}. For x outside P,
the extended set P union {x} is invalid exactly when at least one of
the following conditions holds:

1. x belongs to H_(p+1)-s.
2. For some q in {2,...,p+1}, (q-1)x belongs to s-H_(p+1-q).

Proof. A competing (p+1)-term multiset uses q copies of x. Its remaining
terms have sum h in H_(p+1-q), and its sum condition is
(q-1)x=s-h. For q=0 this is condition 1. For q>=2 it is condition 2.
For q=1 the remaining p-term multiset has sum s; validity of P forces
the baseline, so the enlarged multiset is not a rival. Conversely every
instance of conditions 1 or 2 explicitly gives a rival with q different
from one. This exhausts the possibilities. QED.

Validity is hereditary: a rival for a subset is padded by one copy of
every omitted point. Consequently a search of sorted valid prefixes
using this lemma loses no valid complete set.

The search maintains H_0,...,H_n as integer bitsets. Adding a new point
uses the exact recurrence H'_r=H_r union (x+H'_(r-1)). Modular equations
kx=y are solved with all gcd(k,N) lifts, not with an unjustified inverse.
When k is a unit, byte lookup tables compute precisely the dilation of
the bitset; this changes runtime only. Once every residue is forbidden,
returning early is exact.

## Complete normalization at N=187

Translation preserves validity: both sums in the defining equality have
eight terms. Unit scaling also preserves it.

Every valid eight-element set at N=187=11*17 has a unit difference.
Suppose otherwise and translate a point to zero. Every nonzero point is
divisible by 11 or 17. A nonzero multiple of 11 and a nonzero multiple
of 17 have a difference divisible by neither prime, hence a unit.
Thus all points must lie in the subgroup of multiples of one prime,
of order 17 or 11. The 128 subset sums of the seven translated nonzero
points are distinct by validity, impossible in either subgroup. QED.

Choosing a unit difference a-b and applying (x-b)/(a-b) therefore makes
the set contain 0 and 1. Searching every sorted extension of (0,1)
covers every valid eight-element affine class at this modulus. No
assumption that an arbitrary difference is a unit has been made.

The same argument works when N<256 has at most two distinct prime
factors: if no difference is a unit, all points lie in one residue class
modulo one of those primes, whose subgroup has order at most N/2<128.
With two prime factors, points divisible by both primes belong to either
class; a p-only and a q-only point would have a unit difference. This
generalization is not an assertion about moduli with three prime factors.

## Validation

`validate_encoding()` compares the extension lemma with direct multiset
validity for every valid sorted prefix in the specified small tests:
(N,n)=(5,3),(6,3),(7,3),(11,4),(12,4),(15,4). All 766 extension comparisons
passed. For each binary set at N=248,255,256, all seven extension steps
passed, followed by independent enumeration of all 6435 eight-term
multisets. Exactly one target representation was found in every case.

Separate complete searches starting from (0,), without unit scaling,
gave the following counts of valid sets containing zero:

| N | n | Valid sets | Search status |
|---:|---:|---:|---|
| 5 | 3 | 0 | COMPLETE |
| 6 | 3 | 6 | COMPLETE |
| 11 | 4 | 0 | COMPLETE |
| 12 | 4 | 16 | COMPLETE |

These checks recover the known small threshold cases but do not prove
the eight-element search correct by themselves. Its completeness instead
rests on the extension lemma and the explicit normalization proof.

## N=187 bounded search checkpoint

The first run used a 120-second search deadline with initial tuple (0,1).
It terminated normally with status TIMEOUT at elapsed time 120.0 seconds.
The machine-readable result is `stage3_search_initial_timeout.json`.

- Fully completed third-coordinate branches: 3,4,5,6,7,8,9.
- Visited valid prefix counts at sizes 2,...,8:
  1,8,1209,73586,588885,289,0.
- Active incomplete prefix at timeout: (0,1,10,58,144,156).
- Accepted complete sets: none.
- This first run is incomplete and is not an exclusion of modulus 187.

Values below 3 cannot start a valid extension: 2 collides with 0+2=1+1.
The 300-second continuation begins with third coordinate at least 10,
so it does not redo the fully completed first-run branches. It saves to
`stage3_search_187_remaining.json`; its final outcome will be recorded
below. A TIMEOUT record is not a solver infeasibility certificate.

The continuation completed in 35.531 seconds with no accepted set.
A fresh full run then completed in 44.219 seconds, producing the single
clean record `stage3_search_187_complete.json`. It visited 3,493,404 valid
six-element prefixes and 1124 valid seven-element prefixes, with no
eight-element extension. A separate full N=188 run completed in 68.828
seconds, producing `stage3_search_188.json`; it visited 4,127,034 valid
six-element prefixes and 20,542 seven-element prefixes, again with no
eight-element extension. The initial tuple was (0,1), and normalization
is complete at both moduli by the proved two-prime lemma.

These are completed custom exhaustive computations, not random tests,
SAT-solver infeasibility messages, or portable proof certificates. They
do not depend on the published seven-element certification. In particular
the N=188 search includes antipodal candidates and still excludes them.
The separate independent checker reconstructed the extension criterion,
bitset update, both modular-root branches, and the normalization proof.

## Reproduction

Use Python 3 in this directory:

```text
python stage3_search.py --N 187 --n 8 --seconds 120 --initial 0 1 --validate
python stage3_search.py --N 187 --n 8 --seconds 300 --initial 0 1 --first-min 10 --checkpoint stage3_search_187_remaining.json
python stage3_search.py --N 187 --n 8 --seconds 120 --initial 0 1 --checkpoint stage3_search_187_complete.json
python stage3_search.py --N 188 --n 8 --seconds 180 --initial 0 1 --checkpoint stage3_search_188.json
```

Each run has an explicit deadline. Checkpoint files record the exact
initial tuple, any first-extension restriction, all fully completed
first-extension branches, and the active prefix at timeout. On timeout,
continuation can safely skip completed branches and repeat the incomplete
branch. The implementation does not claim fine-grained resumption inside
that branch. Every accepted set is independently checked by complete
multiset enumeration before it is recorded.

## Targeted ordinary-four-fiber structure in odd groups

Suppose four ordinary representations 2a_i+b_i+c_i have one value,
where each representation has three distinct points, and A has no
antipodal pair. The four centers are distinct: a fixed center has a
unique tail pair by the Sidon property. No center can occur as a singleton
in another representation, because cancellation would leave every surplus
on that side at most one, producing a rival to the all-ones multiset.
Thus all tail pairs lie on the other four points. The pairs are distinct,
or equality of their sums would identify two doubled centers.

The resulting graph on four tail points has four edges. It is either a
four-cycle or a triangle with a pendant edge. If the modulus is odd,
the four-cycle is impossible: alternating tail-edge sums are equal, so
alternating center-pair sums are equal after canceling the invertible
factor two. This is a forbidden squarefree two-term collision. The odd
modulus assumption is essential to this argument.

Label the tail points as 0,2u,2v,2w, with triangle 0,2u,2v and pendant
edge 2v,2w. Solving the four center equations gives, for some H,

    A = {0,2u,2v,2w,H-u,H-v,H-u-v,H-v-w}.

Conversely this configuration has the indicated four ordinary
representations at value 2H whenever its points are distinct. No claim
that every parameter choice is valid is made.

At N=247 the four tails must contain a unit difference. Otherwise the
two-prime lemma for their pairwise differences puts them in one prime
coset. Translate a tail to zero. All three other tails are zero modulo
that prime; the four centers all have one quotient residue r. Selecting
two centers and an arbitrary subset of the three nonzero tails gives
6*8=48 distinct subset sums, all in residue 2r. Each coset has capacity
247/13=19 or 247/19=13, contradiction. This includes r=0.

Under the graph automorphism swapping the two nonhub triangle vertices,
the six tail-pair types fall into four classes: the triangle base, a
central triangle edge, a missing edge, and the pendant edge. Translation
and unit scaling make the corresponding parameters satisfy respectively
u=1, v=1, w=1, or w-v=1. A chosen unit difference can be scaled to two
rather than one because the modulus is odd. Thus these four cases cover
every valid ordinary-four-fiber configuration at 247. At the prime
modulus 241, every nonzero tail difference is a unit, so the same four
cases are automatically complete. No such normalization is assumed at
an arbitrary composite modulus.

## Exact linear encoding of that configuration

The eight points have coefficient vectors on (H,u,v,w)

    (0,0,0,0), (0,2,0,0), (0,0,2,0), (0,0,0,2),
    (1,-1,0,0), (1,0,-1,0), (1,-1,-1,0), (1,0,-1,-1).

Their sum has coefficient vector (4,0,-1,1). Enumerating the 6434 indexed
rival eight-term multisets gives 3815 distinct nonzero difference vectors
(c_H,c_u,c_v,c_w), with c_H in [-4,4]. If c_H=0, the equation is a
forbidden balanced tail relation. If c_H is nonzero, its inverse exists
at 247 and 241, so exactly one H is forbidden for the chosen tails.
Both implications are equivalences, not merely necessary filters.
The resulting sets have 409 balanced constraints (up to sign) and 2423
forbidden linear forms for H at each tested modulus.

`stage3_four_fiber_search.py` checks all parameter pairs for each of the
four normalizations. It first solves every balanced equation for the
second free parameter, retaining every gcd lift. Then it unions all
forbidden H values. This covers all H without testing them individually.
If any H survives, all 6435 eight-term multisets are independently
enumerated before accepting the set.

Validation compared this encoding with direct eight-term enumeration for
all 88 distinct-point configurations in the specified small N=19,23
parameter box. It also accepts the proved sharp four-fiber construction
at N=54865 with (u,v,w,H)=(1,19,361,6859), independently checked through
all 6435 multisets. An independent checker reconstructed the coefficient
generation and all four normalization cases without finding a gap.

## Completed targeted outcomes

At N=247, the targeted search completed in 9.250 seconds under a
180-second cap. It covered 4*247^3=60,276,892 labelled parameter triples,
not that many distinct sets. The exact per-normalization counts are:

| Case | Balanced-rejected tail pairs | Passing tail pairs | Forbidden H values |
|---|---:|---:|---:|
| Triangle base | 55445 | 5564 | 1374308 |
| Central edge | 55452 | 5557 | 1372579 |
| Missing edge | 55458 | 5551 | 1371097 |
| Pendant edge | 55547 | 5462 | 1349114 |

Every passing pair forbids all 247 values of H. Thus no valid set at 247
can contain an ordinary fiber of size four. This is a targeted exhaustive
computational restriction, not an elementary proof for all moduli below
248, and not an exclusion of valid sets whose ordinary fibers are smaller.
The full record is `stage3_four_fiber_247.json`.

The selected prime modulus 241 was checked separately, completing in
7.922 seconds under a 60-second cap, again with no accepted configuration.
Its record is `stage3_four_fiber_241.json`. These two selected high-fiber
experiments are not an exhaustive sweep over moduli. The initial files
and results from earlier stages were preserved.

```text
python stage3_four_fiber_search.py --N 247 --seconds 180 --validate
python stage3_four_fiber_search.py --N 241 --seconds 60 --checkpoint stage3_four_fiber_241.json
```

## Current continuation direction

The next structural question is whether the balanced constraints and the
forbidden H forms admit a small arithmetic covering certificate, or a
pigeonhole argument independent of the particular modulus. Simply
repeating the finite searches at every modulus is not the intended next
step. No global four-term collision-loss inequality has been proved by
these computations.
