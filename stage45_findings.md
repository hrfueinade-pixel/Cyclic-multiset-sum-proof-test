# Stage 45: mixed-quintic counterexample and a complete coupled exclusion

2026-10-11. Continues Stage 44 / open PR #16 at
archived-source. Earlier PRs remain unmerged.
The complete N>=248 theorem remains OPEN and the goal remains ACTIVE.
No arbitrary new odd modulus is excluded by this stage.

This round tests the mixed 311 quintics, meaning 3a+b+c with three distinct
labels. It finds an actual full-valid counterexample to a local compression
lemma, then proves that its entire coupled configuration is excluded under
the small quartic budget. The global cubic--quintic tradeoff remains open.

## 1. Two structural approaches and the targeted pivot

An ordinary quintic has a private doubled center. A fiber with three such
words confines every additional representation beyond those three to the
five remaining labels B.
There are 168 mixed 311 words on the eight-set. Controlling their possible
compression on B would be a plausible ingredient in the global quintic
growth estimate, if accompanied by a proved overlap argument.

**Attempt one:** bound the number of 311 words in a fiber on any protected
five-label set by two. This is false: the full-valid set {1,2,4,8,16} in
Z/31 has three such words at value 15:

    3*1+4+8 = 3*2+1+8 = 3*4+1+2 = 15.

**Attempt two:** weaken the cap to three, using full five-label protection
and the existing cubic/quartic/quintic multiplicity restrictions. The fixed
symbolic experiment below produces a stronger counterexample: FOUR 311
words on five labels, extendable to a full-valid eight-set satisfying all
the existing local multiplicity caps. Thus those hypotheses alone cannot
justify this local bound. An additional small-order or coupled hypothesis
is necessary.

The actual proposed bound WHEN THREE ORDINARY WORDS COEXIST in that same
fiber is NOT refuted by our counterexample: its fourfold mixed fiber has
no ordinary words. Nor is a bound under |T4|<=88 refuted. These stronger
conditional questions remain open; no conclusion is transferred between
their different premises.

## 2. Complete fixed symbolic inventory, with exact boundary

Two 311 words with the same tripled center cannot coincide: cancellation
of that center three times would equate two different squarefree pair sums.
Thus four 311 representations on five labels have four different centers.
Normalize these labeled centers to 0,1,2,3. Each center has six possible
tail pairs on the other four labels, giving exactly 6^4=1296 assignments.
These are label configurations, not residues, moduli, or group parameters.

Subtract the first of the four degree-five words from the other three,
obtaining three integer relation rows R1,R2,R3. For 714 assignments the
saved positive evidence gives a non-original nonnegative degree-five word p
with

    2^j*(p-1_B) = u1*R1+u2*R2+u3*R3.

If the four words shared a value, these rows would vanish. Oddness cancels
only 2^j and makes p a rival for the squarefree five-subset B. Appending
the three outside labels gives an eight-term rival. Each word's mass and
nonnegativity and every integer equation are checked independently.

The remaining 582 assignments all have rational relation rank three. They
are NOT exclusions, and rational rank alone does not remove odd torsion.
A fixed integer-kernel embedding diagnostic examined only three of them,
stopping at its first full-valid counterexample. Its first two embeddings
had coincident labels. No cyclic parameter or modulus search was performed.

## 3. Explicit counterexample to the local cap three

Let

    B={0,14,15,17,21} in Z/107,
    A={0,14,15,17,21,1000,10000,100000} in Z/800001.

B is full-valid in degree five. A is full-valid in degree eight. Both
moduli are odd. The four mixed quintics at value 80 are

    3*17+14+15 = 3*14+17+21
               = 3*15+14+21 = 3*21+17+0 = 80.

### Elementary validity proof, independent of enumeration

The sum of B is 67. No modular wrap is possible in five terms, since
5*21=105<107. Five nonzero coins are already at least 70. If the number
of 21's is at least four the sum exceeds 67; with three the remainder is
4; with two it is 25, neither representable by 14,15,17. With one 21 the
remainder 46 must use three coins and its only decomposition is 14+15+17.
With no 21, three coins total at most 51 and five at least 70; four 17's
give 68, while any replacement drops the total by at least two, never one.
Thus the only nonzero-coin representation of 67 is 14+15+17+21. In degree
five exactly one zero pads it, giving the all-ones word.

For A, every eight-term sum is at most 800000, so again there is no modular
wrap. The contribution from B is at most 168<1000. The target is 111067.
Modulo 1000 the B contribution must therefore be exactly 67. The three
large coin counts are between zero and eight; their base-ten digits in
the remaining value 111000 consequently force each count to be one.
Only five terms remain for B, whose unique representation was just proved.
Thus all eight counts are one.

Independent complete enumeration checks all 126 five-term B multisets and
all 6435 eight-term A multisets. For A it also finds

    |T3|=60, |T4|=229, |T5|=601;
    maximum total cubic multiplicity =2;
    maximum ordinary quartic multiplicity =2;
    maximum ordinary quintic multiplicity =2.

The fiber at 80 consists of exactly the four displayed 311 words. It has
no ordinary quintics. The shared-center triple restrictions are vacuous
because there are no three-ordinary quintic fibers.

This is NOT a counterexample to N>=248 or the intended conditional growth
bound: N is large, |T4|=229>88, and |T3|+|T5|=661>192. Its purpose is to
refute the unrestricted local mixed-word lemma even under full validity
and all three multiplicity caps. The small quartic budget cannot be omitted.

## 4. Complete coupled-pattern exclusion below 248

The counterexample comes from the abstract equalities

    3a+b+c = 3b+a+d = 3c+b+d = 3d+a+e.                (F)

**Theorem.** No full-valid eight-set in an odd group with N<248 contains
five distinct labels satisfying (F).

### Group coverage without any division

In label order a,b,c,d,e, the three relation rows are

    R1=(-2,2,-1,1,0),
    R2=(-3,0,2,1,0),
    R3=(-2,-1,-1,3,1).

Set t=c-b. The following exact INTEGER combinations prove

    a-e-17t = 8R1-5R2-R3,
    b-e-14t = 7R1-4R2-R3,
    c-e-15t = 7R1-4R2-R3,
    d-e-21t =10R1-6R2-R3.

Here a row means its corresponding linear combination of the five labels.
As R1,R2,R3 vanish, translating e to zero yields the COMPLETE model

    {0,14t,15t,17t,21t,u,v,w},                         (M)

with the other three points arbitrary. No parameter is assumed a unit.
No rational argument or cancellation of three, five, seven, or any odd
integer is used. Every actual group solution of (F), including a possible
nonunit or torsion solution, has this form. Conversely these five multiples
satisfy (F) identically, so the coverage is exact.

### Positive quartic growth

For (M), a saved positive certificate selects 92 repeated quartic words.
Each of its 4186 selected pairs has an explicit non-original mass-eight
word c and a multiplied identity

    2^j*(M(c)-M(1)) = k*(M(left)-M(right)),  k!=0.

If that selected pair shared an actual group value, oddness would cancel
2^j and make c a rival. Thus all 92 outputs are distinct, with no assumption
of disjoint witnesses or unused labels. Full validity gives |T4|>=92, and
the exact odd packing inequality gives N>=71+2*92=255, contradicting N<248.

The theorem therefore excludes the WHOLE coupled equality pattern (F), not
just the integer example or a torsion-free sample. Its S4 orbit has 24
different assignments in the original residual inventory; all 24 are closed
by the same relabeled coverage proof. There remain 558 unexcluded symbolic
assignments in this fixed four-311-on-five-label experiment.

## 5. Verification and scope

The standalone checker imports no discovery, Gaussian elimination, kernel
embedding, or earlier research modules. It independently reconstructs every
one of the 1296 assignments and checks all 714 positive rival identities,
the residual ranks by integer minors, the explicit integer parameterization
of (F), its full 24-element symmetry orbit, and all 4186 growth-pair records.
It rechecks the full-valid numerical sets with a different weak-composition
implementation, and verifies their actual multiplicity caps and output
counts. Wrong mass, an original word, and a factor-three cancellation are
rejected by corruption controls.

All arithmetic and coverage claims above passed. This is a same-author
separate implementation, not independent human or formal review. No
novelty claim is made. The generic positive search retained the existing
two-second cap and its first certificate was reused during metadata updates;
no failed or interrupted search supplies an exclusion. No historical search
entry point was called and no earlier PR was merged.

## 6. Missing global step and next bounded question

The remaining goal is still the conditional dichotomy

    |T4|>=89  OR  |T3|+|T5|>=192

for full-valid eight-sets in odd 207<=N<248. Equivalently, under |T4|<=88,
the unproved target remains |T5|>=156-h-R3. Neither the local counterexample
nor exclusion of its single coupled pattern establishes this global result.

What changed is the next action: a cap on mixed 311 fibers cannot follow
from full protection and local multiplicity caps alone. It must exploit
the quartic budget or coexisting ordinary words. Pattern (F) demonstrates
exactly how a genuine permitted collision can have too much quartic growth
to survive below 248.

A bounded next structural question is whether the OTHER 558 assignments
of four 311 words on five labels similarly force |T4|>=89 or an eight-term
rival, retaining every odd-torsion branch. The fixed inventory is already
complete; it must not be replaced by a residue search or a torsion-free
embedding sweep. Even a complete conditional cap three on five labels
would NOT finish 248: collisions among types 5,41,32,221 and across different
center triples would remain, and fresh-output charges still need proof.

## 7. Reproduction and delivery

The shipped bundle contains the complete inventory, retained growth
certificate, counterexample audits, and the three-case embedding diagnostic.
Check it without discovery:

```text
python -B stage45_certificate_check.py
```

To reproduce the fixed experiment and its saved evidence:

```text
python -B stage45_five_label_311.py
python -B stage45_residual_embeddings.py
python -B stage45_counterexample.py
python -B stage45_pack_certificates.py
python -B stage45_certificate_check.py
```

The positive producer uses the existing Stage 43 generic growth engine.
Its loose certificate retains that helper's stage43_s45_* prefix; the
Stage 45 bundle includes it, so the checker needs no loose files.
The current report, reproducible scripts, bundle and checked results continue
the stack in a new PR based on Stage 44 / PR #16. Earlier PRs remain unmerged.
The full N>=248 goal remains active and incomplete.
