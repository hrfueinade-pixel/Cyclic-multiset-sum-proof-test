# Round 8 of 8: h>0 milestone and final reassessment

The bounded eight-round run is complete. The original universal N>=248
theorem remains OPEN. No search is active, no PR is merged, and no
literature novelty or formal proof-assistant certification is claimed.

## New elementary restriction for odd H with arbitrary h

Assume a valid non-antipodal eight-point set and odd cyclic difference
subgroup H. Doubling is injective on the 56 ordered differences, even
when h>0. The 28-h available unordered center pairs map injectively to
28-h singleton-label pairs. Let s_b be the number of missing label pairs
incident to b. Then 0<=s_b<=7 and sum_b s_b=2h.

For each present singleton pair {b,r}, orient its unique center edge
d->e by 2d+b=2e+r. The edges based at b are labeled by the distinct
r!=b. They form a FOREST, with exactly 7-s_b edges and 1+s_b components.

Proof of acyclicity: traverse an undirected cycle, with signs eta_i
on its orientations. Summing gives sum eta_i*(r_i-b)=0. Every label
r_i is different, so the balanced coefficient vector is nonzero and
every coordinate except b is 0,+1,-1. If its b-coordinate is <=1,
subtract it from all ones; otherwise add it to all ones. The chosen
rival is nonnegative, has eight terms, and has the same sum. Validity
forbids it. Also no edge has destination b: that would give a double
equal to a different squarefree pair. This proof does not require h=0
or R3=0, but needs odd H for the label-pair uniqueness used above.

Let k_b be the number of unpaired cubic marks with singleton b. A paired
mark in a fiber of size m contributes m-1 outgoing tree edges. Hence
the complete incidence identity becomes

    k_b = 1+s_b + sum_(paired b-marks)(m-2).

When R3=0, each forest has outdegree <=1 and exactly 1+s_b roots;
sum k_b=8+2h. Thus for h>0 the regular unpaired permutation cannot
exist: there are strictly more than eight unpaired marks. This is a
proved numerical obstruction to extending Round 7's eight rooted trees
unchanged. For R3>0 the extra summand records the further defect.

At R3=0 the global quartic graph still has degree <=2. It has exactly
8(28-h) edges: each cubic pair has eight distinct cones, and two cones
cannot produce the same quartic edge because that would share two
occurrences and violate pair uniqueness. Therefore K=36+8h+C and
Sigma=C, where C counts graph cycles, but isolated pure vertices and
unpaired 31 vertices now occur. The budget is C-D>=53-8h. Short-cycle
and short-path exclusions from h=0 cannot be used unless every required
doubled-center direction remains present. No bound on C-D is proved here.

## New parity restriction for even H with arbitrary h

Translate 0 into A and suppose A generates even H. Let p,q be its
positive numbers of even and odd points, p+q=8. There are 2pq odd
ordered differences. Classify antipodal pairs of the 36 pair sums as
DS (double/squarefree), SS, DD, with counts d,e,j. The Stage 6 matching
argument, independent of h=0, gives

    |2Delta|=56-L,  L=2d+4e+j.

The elementary signed-relation arguments in Stage 6 still give d<=7,
e<=1, and d<=2 when e=1. For arbitrary h the additional DD case needs
treatment: j<=1, since a DD pair forces a unique order-four difference
between its centers. If j=1, neither of its two centers can be a DS
center: adding/subtracting the DD and DS antipodal equations would
equate a double to the DS squarefree tail. In a DS star, excluding
those two centers leaves at most six distinct centers (at most five
if the hub is neither); a DS triangle has at most three. Thus d<=6
when j=1. These cases give L<=14 WITHOUT assuming h=0:
e=j=0 gives 14; e=1 gives at most 9; e=0,j=1 gives at most 13.

All doubled differences are even. Only 56-2pq differences of Delta
are even, so at least 2pq-L distinct doubled images are outside Delta.
Each has at least one missing-doubling preimage. Consequently

    h >= pq-L/2 >= pq-7.

In particular, **if 1<=h<=4, the parity split MUST be 1+7**.
Splits 2+6, 3+5, 4+4 require h>=5,8,9 respectively.
This treats even h>0 separately; it does not apply the odd forest
argument when doubling is noninjective. It does not settle the budget.

## Strongest result and remaining obligations

The strongest new proved result is Round 7's COMPLETE regular odd
classification: h=R3=0 implies the affine binary family, |H|=255,
|T4|=92 and N>=255. It is computer-assisted via the independently
checked long-cycle and long-path exclusions. Round 1's tighter triangle
enumeration is optional, not a dependency of that theorem.

Round 6 closes the remaining singleton endpoint defect. Conditional
on historical MC, any fresh fiber in odd h=0 must now contain an
isolated ordinary center defect. Its complete short-opponent inventory
was saved BEFORE new roles, in Round 5, with OO and PO opponents
subsequently removed by Stage 17 and Round 6 respectively.

The unsolved requirements are:

1. Odd h=0,R3>0: exclude or control every isolated-ordinary fresh fiber,
   including the surviving opponent table and Q+O allocation. Then still
   prove Sigma-D>=53-8R3; do not infer it merely from D=0.
2. h>0: obtain a global C-D or Sigma-D bound that accounts for missing
   closure directions and forest deficits. The new forest and parity
   restrictions narrow the structural problem but do not satisfy the budget.
3. Antipodal cases: retain the external reported n=7 certification unless
   independently recertified or replaced by a self-contained argument.
4. Historical MC and Stage 16 exclusions retain their recorded computation
   and audit limits when used. They were not rerun or upgraded here.

The required sufficient target throughout is |T4|>=89, equivalently
Sigma-D>=53-8(h+R3). The stronger growth lemma remains a separate goal.

## Reassessment and stopping rule

The path/cycle route succeeded in its full regular scope and is now
finished; do not continue searching its surviving long types (none).
The pure FOO layer left four necessary roles, but regular classification
now makes that diagnostic unnecessary for the regular target. It may
still help the isolated-ordinary local inventory. It is NOT a valid
counterexample or an exhausted full-closure presentation.

The next bounded round should choose one explicitly classified
isolated-ordinary opponent family or a global forest-deficit budget,
not restart the closed singleton endpoints. For a local family, state
all P orientations and role domains first, and preserve every surviving
torsion presentation. For a global family, seek a restriction coupling
fresh loss to missing labels rather than assuming one fresh loss per
missing center pair (historically false). Pivot after two rounds with
no new restriction, checked exclusion, verified intermediate counterexample,
or precise obstruction. No such consecutive stalled route occurred in
these eight rounds: each saved a new restriction/exclusion or explicit
scope obstruction, and the regular route was stopped on completion.

Reproduction and new verification totals are in stage25_findings.md.
The final checkpoint is this report and research_resume.md. Deliver via
a separate unmerged PR stacked on PR #6. Round 8 checkpoint saved.
