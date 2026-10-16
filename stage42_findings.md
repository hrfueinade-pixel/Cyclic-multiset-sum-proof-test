# Stage 42: simultaneous quintic collisions and the order-three exception

2026-10-11. Continues Stage 41 / open PR #13, whose head was checked at
archived-source. Its base is the Stage 40 branch;
neither it nor an earlier PR was merged. The workspace is an archive, not
a Git checkout. All 264 remote blobs matched the local files byte for byte.

**The universal conclusion N>=248 remains OPEN.** No new arbitrary modulus
is excluded, and no valid set below 248 is produced. The general proved
bound remains N>=207, with all odd 207,209,...,247 still requiring closure.
Discovery-only and timed-out historical exclusions retain their boundaries.

This stage delivers three new structural results, two counterexamples to
proposed intermediate shortcuts, separate positive certificates, and two
precise remaining obligations. The primary global cubic--quintic tradeoff
is not proved. The strongest new exclusion is secondary: the order-three
exception cannot occur in a hypothetical odd sub-248 valid eight-set.

## 1. Exact target and inherited hypotheses

For full validity, every squarefree word of degree at most eight has its
unique same-degree representation: append its complement to any replacement
to get an eight-term rival. Therefore Q_k and T_k are disjoint, with the
squarefree words distinct. All sums here allow repetitions unless stated.

The exact complementary packing and odd midpoint argument give

    3A intersect(s-5A)=Q_3,
    N >= 56+|T_3|+|T_5|,
    N >= 71+2|T_4|.

Thus the desired dichotomy is

    |T_4|>=89 OR |T_3|+|T_5|>=192.                 (D)

In a hypothetical odd N<248 counterexample, |T_4|<=88. The cubic identity
|T_3|=36+h+R3 makes the remaining target |T_5|>=156-h-R3. This inequality
is a TARGET, not a lemma used in the calculations below. The conclusion
is N>=248, not N>248. A quartic route yields N>=249 in odd order, whereas
the cubic--quintic route need only yield 248 before oddness is applied.

Stage 41's exclusions and full-validity restrictions are used as stated:
quartic and cubic fibers have at most three ordinary representations, and
the only possible four-mark cubic fiber has two pure and two ordinary
words. These are not transferred to merely cubic-protected sets.

## 2. First serious approach: propagate protected outputs to degree five

Every repeated degree-five word can lose one occurrence while retaining a
repeat; conversely adding a point to a repeated quartic retains a repeat.
Hence T_5=T_4+A. Likewise T_4=T_3+A. For the unrestricted sums 4A+A,
count RESIDUE pairs (x,a), not multiset representations.

A protected squarefree quintic has exactly five such incidences, one for
each possible last label. Every repeated quintic has at most eight, since
there are eight possible last labels. Therefore

    8(70+|T_4|) <= 5*56+8|T_5|,
    |T_5| >= |T_4|+35.

The analogous protected quartic calculation gives |T_4|>=|T_3|+21.
Writing k=h+R3 and combining these bounds gives

    |T_5| >=92+k,
    |T_3|+|T_5| >=128+2k.

Even k=28 gives only 184. The remaining numerical gap is 64-2k, at least
eight values. Removing the order-three exception does not remove it.

**Exact failure:** these inequalities allow the same output to receive
many incoming translates. They prove no injectivity of a proposed charge,
and |T_4|<=88 does not reverse either lower bound to create additional
growth. Every overlap has been accounted for by the incidence cap; no
outputs or witnesses are assumed disjoint. Merely iterating these
inequalities cannot prove (D). No additional collision budget is claimed.

## 3. Second serious approach: classify a saturated ordinary quintic fiber

Call a quintic ordinary when it is 2c+b+d+e with four distinct labels.
Its center c is absent from EVERY other representation of its value.
If another word contained c, subtracting one c from both words would
equate its squarefree quartic c+b+d+e to a different quartic. Full validity
forbids that. This holds for nonordinary opposing words too.

For r ordinary representations, their r centers are distinct and private.
Their three-label tails are different: equal tails would imply equality
of doubled centers, and odd order cancels two. The tails lie on at most
8-r labels. For r>=5 there is at most one available triple and at least
five required ones. Thus EVERY valid odd eight-set has at most FOUR
ordinary quintic representations per fiber.

If there are four, the remaining four labels B={b_1,...,b_4} provide
exactly their four three-subsets. Relabel so the tail of center c_i is
B minus b_i. If their common value is t, set z=t-sum(B). Then

    2c_i-b_i=z for i=1,2,3,4.

Translate every label by z. For c_i'=c_i-z and b_i'=b_i-z we get
2c_i'=b_i'. Consequently the eight-set has the form

    A={u,v,w,z,2u,2v,2w,2z},                         (F)

with all eight labels distinct. Here the new parameter z is unrelated to
the preceding translation symbol. No parameter is assumed a unit. No
factor of three was canceled. This is an exact classification, not a
sampled configuration inventory.

This makes a local saturation question concrete, but it does not itself
exclude (F). The fixed symbolic experiment below certifies T_4>=78 and
T_5>=135 for this family. Together with the general T_3>=36 it gives only
171 in the cubic--quintic packing. A bound T_3>=57 for (F) would have
finished that particular calculation, but that proposed lemma is FALSE.

### Two explicit failures of the local shortcut

Take N=255 and the ordered set

    A=(1,4,16,64,2,8,32,128).

This is a translate and reordering of the binary control. All 6435
eight-term count vectors are checked directly: the all-ones vector is
the only one summing to its target 0. Independently, a sum of eight
powers-of-two coins congruent to 0 has sum 255,510,765,or1020. Each has
eight binary ones. A carry reduces the number of coins, so equality of
coin count and binary population count forces no carry. Only 255 can be
formed without a carry from the available powers, each used once.

Its exact counts are

    |T_3|=36, |T_4|=92, |T_5|=162, h=R3=0.

It has at most two total cubic marks per repeated fiber and at most three
ordinary quartics, yet FOUR ordinary quintics at 170. Thus it refutes
both unrestricted claims: (F) forces T_3>=57; and the Stage 41 local
multiplicity caps plus full validity force at most three ordinary quintics.
It is OUTSIDE the target interval and has |T_4|>88. It does not refute
either conditional small-order version or the requested theorem.

It also exhibits the precise label reuse problem. Write its centers as
c_i=(1,4,16,64), and b_i=2c_i. For each of the six unordered center pairs
{i,j}, with remaining indices {k,l},

    (2c_i+b_j)+(b_k+b_l)
      = (2c_j+b_i)+(b_k+b_l) = 170.

The six cubic residues 2c_i+b_j are DISTINCT, by doubled pair-sum
uniqueness, yet their six lifts all have the SAME quintic output. Inside
each cubic fiber there are already two words. Word decompositions and
residue incidences cannot be counted interchangeably. A charge assigning
a fresh quintic value to each cubic fiber therefore needs a separate
overlap theorem. The saved control records all six witnesses explicitly.

## 4. Targeted pivot: competing simultaneous-collision explanations

After the two approaches above stalled, the experiment compares four
fixed presentations of (F). It distinguishes the claim that saturated
quintic fibers are intrinsically forbidden from the claim that extra
cubic compression forces growth elsewhere. It is NOT an enumeration of
all additional cubic equalities or of all possible symbolic quotients.

| Presentation of the four centers | Positive quartic bound | Positive quintic bound |
| --- | ---: | ---: |
| u,v,w,z | 78 | 135 |
| u,4u,v,w | 85 | 142 |
| u,4u,v,4v | 89 | not needed |
| u,4u,16u,64u | 92 | not needed |

Each eight-set consists of these centers and their doubles. For the last
two rows, the certified quartic bounds exclude the family throughout odd
N<248: respectively N>=249 and N>=255. They are new positive symbolic
exclusions. The first two rows are INCONCLUSIVE, not counterexamples.
For the one-chain model, 85 quartics give N>=241, which still permits 243.
Cancellation by three is therefore NOT justified by this bound.

The quintic discoveries used the SAME fixed ten-second clique cap, and
retained 135 and 142 respectively. No cap was increased. Their negative
search outcome proves neither optimality nor existence of a compressed
cyclic realization. A cubic diagnostic retained a 30-clique for (F), weaker
than the general proved bound 36; it has no role in any exclusion.

Five declared cyclic controls were also checked directly, without searching
for them. Besides the binary example, these include full-validity witnesses
for the generic four-pair model, the one-chain and two-chain models, and
the order-three exception, all at large moduli. Their exact counts and
6435-word checks are saved. They demonstrate that the configurations are
not inherently contradictory: the small-order growth restriction matters.
The controls are not evidence for a universal classification of compression.

## 5. Secondary branch closed: no exceptional cubic fiber below 248

If two pure and two ordinary cubes share a value, translate one pure label
to zero. The second is delta with 3delta=0. The ordinary equations give
the six distinct forced labels

    0,delta,c,-2c,e,-2e,

and two remaining free labels u,v. Their distinctness follows from the
private-label and odd-tail arguments of Stage 41. In a cyclic group the
nonzero delta has order three. The model does not require canceling three.

The separate certificate selects 94 repeated quartic words for this model
and supplies an eight-term rival for each of their 4371 unordered pairs.
It works uniformly for all choices of c,e,u,v,delta satisfying 3delta=0.
Therefore, under full validity in odd order,

    |T_4|>=94, and N>=71+2*94=259.

This excludes the exception in EVERY hypothetical odd sub-248 set. Combined
with Stage 41, every remaining repeated cubic fiber now has at most THREE
total representations, and

    R3 <= floor((28-h)/3).

Indeed all fibers have multiplicity at most three, so if t3 is the number
of three-mark fibers, R3=t3 and 3t3<=sum binomial(m_y,2)=28-h.
Two pure cubes alone may still coincide at orders divisible by three.
The result does not make multiplication by three invertible.

### Certificate logic and independent challenge

The exception uses four unrestricted integer coordinates for c,e,u,v and
one coordinate modulo three for delta. If D is the coordinate difference
of selected words, each record supplies c!=allones with nonnegative counts
of mass eight, a nonzero signed integer k, and r=2^j such that

    r*(M(c)-M(allones)) = k*D

in the four integer coordinates and modulo three in the torsion coordinate.
If the selected words had equal actual values, D would vanish. Oddness
then cancels r and the supplied c is an explicit eight-term rival.
The checker verifies this MULTIPLIED equation, avoiding the discovery
code's coordinate normalization. Signed k is multiplied, never canceled.
Modulo-three arithmetic encodes 3delta=0; it does not invert three.

The same witness format checks the doubling-chain models. The independent
implementation imports neither the producer nor the Stage 41 search code.
It checked every one of 38537 pair records across eight files, including
wrong mass, original-word, zero-multiplier, and wrong-coordinate corruption
controls. This is separate code by the same author, not independent human
review or formal verification. All selected words are repeated, all are
distinct, and all pair equations are checked. No maximum-clique claim is
needed for any theorem.

Deductive checks: private centers use full quartic protection; the six
exception labels are proved distinct before modeling them; no division
by a parameter or by three occurs; the midpoint bound uses full validity;
the four-pair classification covers only a four-ordinary-quintic fiber;
and two disjoint chains are not inferred from arbitrary cubic collisions.

## 6. Sharply stated remaining obligations

**M1, saturated-quintic closure (UNPROVED).** In odd 207<=N<248, no full-valid
eight-set of the four-pair form (F) has |T_4|<=88. It is enough to prove
the conditional cubic--quintic target for this family, or directly exhibit
an eight-term rival. The two-chain and full-chain subfamilies are closed;
the generic and one-chain positive bounds do not close it. In particular,
extra cubic collisions have NOT been classified as disjoint chains.

Proving M1 would reduce every remaining ordinary quintic fiber to at most
three representations. It would simplify, but still not solve, the global
problem: 280 ordinary quintic words then give only 94 ordinary output
values. These can meet outputs of the 456 nonordinary repeated words.
Their union is not proved to reach 156-h-R3.

**M2, global simultaneous completion (UNPROVED).** Under full validity,
odd 207<=N<248, |T_4|<=88, the now-proved cubic cap three and inherited
quartic ordinary cap three, establish |T_5|>=156-h-R3. If M1 is first
proved, add ordinary quintic cap three. A proof must handle overlapping
fibers and reused labels across BOTH ordinary and nonordinary words;
the fixed six-to-one lift witness shows why an unqualified fresh-output
charge is false. No assumption of distinct witnesses, disjoint image
sets, or injective charging is available.

A concrete certificate route for either obligation is to combine several
actual equal-value word differences D_i into

    sum k_i*D_i = 2^j*(c-allones),

with nonnegative c of mass eight and c!=allones. Oddness would then give
the rival. This is a sufficient format, not a proved closure theorem or
a claim that every possible rival is generated by degrees three to five.
The current bounds use the imposed model relations plus one challenged
collision; they do not establish that all compressed fiber systems admit
such a combination. A direct rival outside this format is equally useful.

This is the exact missing structural step. The new restrictions and the
positive controls do not settle it, do not establish a universal growth
theorem, and do not change the verified odd-modulus exclusion interval.

## 7. Reproduction and saved stopping point

Check the retained positive evidence without discovery:

```text
python -B stage42_certificate_check.py
python -B stage42_fixed_controls.py
```

Regenerate the small fixed symbolic experiments, each with a ten-second
clique cap (no residue-set, parameter, or modulus enumeration):

```text
python -B stage42_symbolic_probe.py --model doubling4 --degree 3 --target 58
python -B stage42_symbolic_probe.py --model doubling4 --degree 4 --target 89
python -B stage42_symbolic_probe.py --model doubling4 --degree 5 --target 156
python -B stage42_symbolic_probe.py --model pairchain --degree 4 --target 89
python -B stage42_symbolic_probe.py --model pairchain --degree 5 --target 156
python -B stage42_symbolic_probe.py --model twochains --degree 4 --target 89
python -B stage42_symbolic_probe.py --model chain3 --degree 4 --target 89
python -B stage42_symbolic_probe.py --model exception3 --degree 4 --target 87
```

The producer reuses only the Stage 41 clique search helper. It does not run
an earlier search. New scripts otherwise use the standard library. Positive
sizes can vary on a later capped discovery run; the shipped certificates
are the evidence for the reported bounds. Search caps apply to discovery,
not startup, graph construction or witness packaging.

Stop at M1/M2 without increasing timeouts or resuming old modulus sweeps.
A useful next experiment must select explicit additional cubic relations
not already covered by the two-chain model and track their joint closure;
its parameter coverage cannot be assumed. The main theorem remains open.
No process remains running and no literature-novelty claim is made.

Delivery is a new PR stacked on PR #13's Stage 41 head, preserving its
entire tree and every earlier unmerged PR.
