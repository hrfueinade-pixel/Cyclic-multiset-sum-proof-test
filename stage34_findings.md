# Stage 34: all non-antipodal seven-sets below 124 are excluded

Saved checkpoint, 2026-10-10. This is a complete computer-assisted
exclusion. The antipodal case is a separate required Stage35 milestone.
No published seven-point computation is assumed.

## Complete reduction

Let A be a valid non-antipodal seven-set in Z/M, M<=123. Its64 subset
sums force M>=64. Each six-subset B is valid and non-antipodal. The
elementary bound |<B-B>|>=62 is proved in Stage30:32 subset sums and
two disjoint exterior-cubic sets of size at least15. Every proper
subgroup of Z/M has size at most61, so B generates the whole group.

Translate B to contain0. If7B fills Z/M, a seven-term representation
of sum A using only B omits the seventh point and contradicts validity.
Therefore enumerate every primitive non-antipodal valid six-set with
7B not full. Normalization by unit pairs or by all gcd divisor roots
covers these sets, as in Stage30. Prefix validity is exact; a full
7-fold prefix sumset stays full for every extension because0 remains.
This is a NEW seven-fold family, not a rerun of Stage30's eight-fold
saturation result. The inherited producer output label 'full8' counts
the seven-fold pruning in this stage.

## Saturation is not universal: retain every survivor

The complete family has58 normalized six-point survivors:30 at121,
10 at122,18 at123, and none at64..120. Each has exactly one missing
seven-fold residue. Consequently the blanket intermediate assertion
7B=Z/M is FALSE; the witnesses and missing residues are all preserved.
For example B={0,1,3,7,15,31} in Z/121 misses120 in7B.

If x is the seventh point, sum B+x must be one of those missing
residues. Thus each survivor leaves exactly one possible x. The
58 resulting extensions are ALL invalid, with explicit nonnegative
seven-term count vectors saved. For the example, x=63 and the rival
counts (0,0,2,0,1,1,3) have the same target modulo121.
This final extension exclusion is essential; the six-point survivors
are not discarded or falsely labeled impossible.

## Completion and independent checks

The first120-second producer run completed64..119 and timed out
during120. Its record is preserved as stage34_initial_timeout.json
and stage34_seven_sum_results.json. A90-second run covered ONLY
120..123 and completed in66.031seconds. The assembled report
stage34_combined_results.json records all60 completed orders, the
source runs, and all58 survivors. The timeout's partial120 state is
never treated as an exclusion.

The independent180-second enumeration completed64..123 in175.5seconds.
It uses the different unit-pair/unitless partition and explicit unions
by new-point copy count instead of the producer coin recurrence. It
reconstructs EXACTLY all58 B sets and their missing seven-fold residues;
no producer code is imported.

The five-second extension search completed in0.016seconds and saved
all58 rival identities in stage34_seventh_extension_results.json.
A further separate five-second checker completed in0.047seconds. It
directly enumerates degree-six multisets to confirm validity of every
B, degree-seven multisets to reconstruct each missing residue, all
possible seventh points, and every actual seven-term target and rival.
All58 rivals check; zero valid seven-set extensions remain. Its result
is stage34_extension_independent_results.json. This verifier imports
no producer kernel. Independent implementations are by the same agent,
not a separate human review or formal verification.

Coverage, scope, cap and completion implications were stated before
each research run. Passing fixtures and timeouts remain inconclusive.
This round closes the non-antipodal dependency; Stage35 must cover
antipodes before concluding the full seven-point lower bound124.
