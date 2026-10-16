# Eight-round checkpoint: progress on 248 and a structural pivot

Stages30-37, saved2026-10-10. The universal N>=248 theorem is OPEN.
All completed and incomplete records are retained; no PR is merged.

## Strongest proved results

1. EVERY valid cyclic seven-set has N>=124, now with a self-contained
   computer-assisted proof in Stages34-35. The prior external minimum
   is not a dependency of this new result.
2. EVERY valid cyclic eight-set with an EVEN modulus has N>=248.
   Stages30-32 close splits2+6,3+5,4+4. Stage35 closes1+7 and antipodes;
   subset-sum packing excludes the all-one-parity case below248.
3. EVERY valid cyclic eight-set has N>=207. The earlier elementary
   bound N>=187 and independent Stage3 certificate exclude smaller
   orders and187. Stages36-37 independently exclude each odd order
   189..205; the even cases are all closed below248. No exclusion
   from an interrupted or discovery-only order enters this bound.
4. For ANY valid eight-set in odd order N<285,4A has no nontrivial
   translation period. The elementary proof is in
   [stage37_aperiodicity.md](stage37_aperiodicity.md). It uses no
   computed minimum, MC, or external result.

The universal quartic target |T4|>=89, equivalently |4A|>=159, and
Sigma-D>=53-8(h+R3) remain UNPROVED. These stronger global statements
are not inferred from small-modulus exclusions.

## Focused rounds and saved outcomes

| Round | Stage | Outcome |
| --- | --- | --- |
|1|30|Complete independently checked exclusion of the entire even2+6 branch|
|2|31|Complete independently checked exclusion of the entire even3+5 branch; every opposing triple shape classified first|
|3|32|Complete independently checked exclusion of even4+4; all34 opposing quartic multisets and51168 symbolic shapes retained|
|4|33|Exact odd five-block/triple reduction; precise180-second duplication obstruction at191, with timeout preserved|
|5|34|Complete non-antipodal seven-point exclusion;58 verified counterexamples to blanket seven-fold saturation, then all58 seventh extensions excluded|
|6|35|Complete antipodal seven-point lift exclusion; all even eight-point cases now closed, including h>0|
|7|36|Coverage-preserving affine canonicalization; discovery completes189..227, times out at229; later orders remain uncertified|
|8|37|Independent odd exclusions189..205 raise general lower bound207; user-requested pivot produces a new elementary quartic-aperiodicity theorem|

## New computational claim and independent scope

Stage37's independent implementation uses explicit copy-count unions,
the complete opposing cubic-multiset list, scalar triple checks, and
direct ordinary base translations. Its normalized five-block canonical
form is computed from the full set of ordered unit-pair images. All
unitless divisor roots are included even when the two-prime lemma
could omit them. No producer is imported. A full8B immediately gives
an all-B rival and safely prunes the complementary-triple calculation;
therefore intermediate shape counts differ from discovery, as expected.
Actual Sidon eight-set survivors would receive all6435 multiset checks.

The stated600-second run completed189..205 and timed out DURING207.
Per-order primitive-block counts agree exactly with discovery; both
have zero necessary triple bases at all nine completed orders. The
independent records and interrupted207 state remain preserved. No
exclusion of207..221 follows from this incomplete global run.

The final five-second consistency check compares only the nine shared
COMPLETE orders and their block/base/Sidon/rival/survivor counts. It
does not repeat a search. The saved result is
stage37_final_crosscheck_results.json. All newly checked numerical
claims use different implementations by the same agent, not separate
human review or a formal proof assistant. Every runtime cap and coverage
argument was stated before its research computation. Timeouts remain
inconclusive for interrupted and unvisited orders.

## Remaining cases and reassessment

Only odd207,209,...,247 remain unexcluded in the final proved theorem.
Stage36 has discovery-only absence at207..227;229 is partial and
231..247 unvisited. None is promoted. The precise symbolic family,
completed versus interrupted scopes, and old h>0/overlap restrictions
are retained in stage37_symbolic_survivors.json. No actual valid
eight-set below248 has been found, which is not itself a proof.

The parity route made substantial progress: all even cases are closed
and the external seven-point dependency is removed. The canonical odd
route improved runtime but still leaves a broad computational obligation.
At the user's request, we stopped extending that route and pivoted to
structure rather than repeatedly increasing search caps or verifying
settled cases. No numerical process remains running at this checkpoint.

The new structural theorem removes EVERY periodic4A possibility below
285. The useful next question is whether aperiodicity, the special70-point
quartic intersection, and the existing cubic defect force enough growth
from3A to4A. Ordinary cardinality identities do not provide that step.
Investigate this growth question analytically before launching another
finite sweep. If it yields only bookkeeping twice, pivot again.
The theorem remains open until every odd case and dependency is covered.
