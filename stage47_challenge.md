# Stage 47 independent challenge and positive controls

2026-10-11. This is the challenger track within the current four-agent
continuation. The complete cyclic N>=248 theorem remains OPEN. These are
separate implementations by another agent in this session, not independent
human review or formal verification. No historical search was rerun.

## 1. A genuine mixed-only fiber with eight predecessors and no triangles

The following proposed universal shortcut is false:

> Every mixed-only repeated quintic fiber has at most seven repeated-quartic
> predecessors, or must encounter an ordinary quartic triangle.

Put B=53, N=B^4=7,890,481 and take the eight signed labels

    A=(2,-3,2B,-3B,2B^2,-3B^2,2B^3,-3B^3) modulo N.

This is a full-valid cyclic eight-set. For counts p_i,q_i on the two labels
of pair i, the target is -sum_i B^i. The difference of an eight-term integer
sum from the target has absolute value less than 25B^3<N. Its coefficients
are 2p_i-3q_i+1, lying between -23 and17. Congruence modulo N therefore
implies integer equality; successive reduction modulo B makes each
coefficient zero. Thus 2p_i-3q_i=-1. Its nonnegative solutions are

    p_i=1+3t_i, q_i=1+2t_i, t_i>=0.

The total mass is 8+5sum_i t_i. Mass eight forces every t_i=0, proving
full validity without enumeration or cancellation of a group parameter.

All quartic words have different values. Indeed equal formal values require
the difference on each pair to be (3t_i,2t_i), and equal total degree gives
sum_i t_i=0. A nonzero difference has a positive t_i, requiring at least
five terms in one of the quartic words, impossible. Balanced base-B descent
and no modular wrap justify formal equality for the actual cyclic control.
Consequently T4=260 and there are no ordinary quartic triangle cores.

The quintic value zero has exactly these four mixed32 words:

    3(2B^i)+2(-3B^i)=0, i=0,1,2,3.

Removing either used label leaves a repeated quartic. Their four disjoint
two-label supports therefore provide ALL EIGHT repeated-quartic
predecessors at this mixed-only output. There are no ordinary words there.
The same coefficient argument shows these four zero words are the only
quintic collision, giving T5=733. The cubic repeated outputs are all64,
with h=28,R3=0. All three inherited local multiplicity caps hold, and the
ordinary quintic cap is even one throughout this control.

The standalone `stage47_independent_control.py` checks the declared set,
all6435 mass-eight multisets and the stated degree counts. This is ONE
actual positive control, not a search over parameters or moduli. Its
T4=260>88 and large N are essential boundaries: it does not refute the
conditional small-quartic-budget target or produce a sub248 set.

## 2. Independent audit of the141-fiber quintic relaxation

`stage47_independent_partition_check.py` independently reconstructs all736
repeated quintic words with stars and bars and checks the saved partition
without importing its producer. It verifies exact word coverage,2258
pairwise primitive-dyadic rival exclusions,1190 ordinary-center privacy
checks, fixed-parity injectivity, and at most TWO ordinary words per fiber.
Thus every three-ordinary restriction, including all triangle and
shared-center rules, is vacuous in this relaxation.

The same checker independently found the following simultaneous failure:

    2a0+a1+a2+a3 = 2a1+a2+2a5,
    2a0+2a1+a6   = 3a1+2a5.

Subtracting the relation rows gives a3-a6=0. Equivalently the all-ones word
plus their difference is the explicit nonnegative mass-eight rival

    (1,1,1,2,1,1,0,1).

No factor is canceled. The abstract partition is therefore impossible
under full validity in ANY group. It is positive evidence that the stated
local constraints do not imply the global growth bound, while simultaneous
closure rejects this particular relaxation. It does NOT show every141-fiber
partition has such a witness, does not enforce the quartic budget, and does
not certify a hypothetical cyclic counterexample.

## 3. Audit of the new proof-agent claims

The independent new-claims checker imports no producer. It reconstructs
the52 avoiding-label companion words and their exact odd-group models,
checks all six individual221 rivals and all726 positive simultaneous-star
pair identities. Each pair verifies the MULTIPLIED integer equation

    factor*(M(rival)-M(allones))
      = multiplier*2*(second_word-first_word),

where factor is a positive power of two, multiplier is nonzero, and the
rival is nonnegative of mass eight and differs from allones. Original-word,
wrong-mass, zero-multiplier and undeclared factor-three corruptions are
rejected. The309 pairs with no shipped positive witness remain UNEXCLUDED;
absence of an identical formal rival is not a universal group theorem.

The two hand221 rivals pass independent algebraic checking. In normalized
triangle notation x+y+3z=-2a-2b-c. If u=2a+2b+c, then
2u+v+x+y+3z=s. If u=2a+2b+v, then c+2u+x+y+3z=s. Both words are
nonnegative mass eight. These cover exactly the six avoiding-u221
assignments whose two doubled labels both lie in X={a,b,c}. Surviving
221 shapes or the other mixed types are not declared realizable.

The ordinary pair-lift identities

    P4=4P3O+S4,
    P5=6P3O+2S4+S5=2P4-2P3O+S5

also pass the coverage audit. Here pairs are counted with multiplicity at
an output; Sk counts ordinary pairs with disjoint tails. Tail intersection
sizes2,1,0 uniquely specify the cubic lift, disjoint-quartic lift, or fresh
quintic pair, so no pair is reused. A cubic pair occupies four labels,
leaving four possible one-label and six possible two-label lifts; a
disjoint-tail quartic pair occupies six labels, leaving two possible lifts.

S5<=28 is justified per unordered center pair: disjoint quintic tails
partition the six other labels, and two candidate partitions imply equal
squarefree triples after canceling TWO. A third ordinary representation is
impossible because its private center would occur in those disjoint tails.
For two B-only companions of this fiber, complementary parities give
(M+M'+1_B)/2, a nonnegative mass-eight rival. Integrality, mass and omitted
centers are all checked; no odd prime is canceled.

## 4. Actual no-triangle and avoiding-star controls

`stage47_independent_newclaims_check.py` independently checks all6435
mass-eight words for each of the following declared cyclic controls, their
ordinary caps, quartic triangles and pair-lift identities:

|Control|N|T3,T4,T5|Ordinary caps at3,4,5|Quartic triangle cores|
|---|---:|---|---|---:|
|path|(670617)|62,244,664|2,3,3|0|
|split|(709785)|63,250,685|2,2,3|0|
|star avoiding|(245633)|60,228,592|2,3,3|1|

The path and split controls demonstrate that ordinary quintic triples
without triangle cores are genuinely realizable under full validity and
the local caps. The star control has exactly two mixed words avoiding the
added label at a three-ordinary star output, refuting a universal cap ONE
there. All three controls have T4>88; none refutes a conditional sub248
lemma. Their explicit sets are retained in the checker and its results.

## 5. Remaining global coverage

If there are no three-ordinary quintic fibers, ordinary cap TWO gives
T5>=140. Hence k=h+R3>=16 would already force T3+T5>=192. Any failure of
the target in this no-triple branch must have k<=15. When k>=13 in this
same branch, packing first gives N>=245; only245 and247 remain below248,
so cancellation by three is then legitimate. It is not legitimate outside
that independently established branch.

At k=15 and T5<156-k, complete saturation would require exactly140 fibers,
all with two ordinary words, no one-ordinary fiber and no mixed-only output.
Current results do not exclude that coupled scenario. In particular no
proof establishes the tempting statement that every no-triple set must
have a mixed-only output. A single pure5 word can share an ordinary output
without violating the pairwise rival or private-center test. None of the
audited local restrictions supplies the global necessity or injective
allocation needed to eliminate every compressed system.

The sharply remaining problem is simultaneous additive closure under
T4<=88, including the no-triple branch k<=15 and path/split or mixed-only
fibers without triangle cores. No arbitrary odd207..247 order is newly
excluded, the558 Stage45 assignments are unchanged, and no completion or
literature-novelty claim is made.

Reproduce the new independent checks with:

    python -B stage47_independent_control.py
    python -B stage47_independent_partition_check.py
    python -B stage47_independent_newclaims_check.py
