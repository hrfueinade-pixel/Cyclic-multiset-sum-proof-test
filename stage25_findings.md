# Eight-round continuation from PR #6

Research date: 2026-10-10. The universal N>=248 statement remains OPEN.
This report completes the requested bounded run, with one saved checkpoint
per round and an unmerged continuation PR. No novelty claim is made.

## Strongest proved result

**Computer-assisted classification:** validity, eight distinct points,
odd cyclic difference subgroup H and h=R3=0 force the affine binary
family, |H|=255 and |T4|=92. Thus N>=255 throughout this branch.
The proof in stage24_round7.md combines complete long-cycle and long-path
exclusions with the singleton-base trees and a numerical contradiction.
It does not assume MC or the external seven-point certification.

## Round checkpoints

|Round|Checkpoint|New outcome|
|---:|---|---|
|1|stage18_round1.md|Outside affine stability, at most 26 non-22 triangles; finite row-spectrum relaxation independently enumerated|
|2|stage19_round2.md|Every regular cycle is a triangle; 538 exact exclusions|
|3|stage20_round3.md|Every regular nontrivial path has two or three vertices; 498 exclusions; initially yields T4 size >=87|
|4|stage21_round4.md|FOP impossible without R3=0/MC; FOO retains four necessary roles after order-seven theorem|
|5|stage22_round5.md|Complete short-opponent inventories for singleton endpoint and isolated ordinary; new restrictions extend locally under MC|
|6|stage23_round6.md|All three singleton endpoint opponents excluded; 88 exact exclusions; only isolated-ordinary defects remain under MC|
|7|stage24_round7.md|Complete regular odd classification and T4 size 92, N>=255|
|8|stage25_round8.md|Odd h>0 forests with explicit deficits; even 1<=h<=4 forces parity split 1+7; final gaps and pivot rules|

## Evidence and independent verification

All new certificates are identities with integer coefficients and a
power-of-two multiplier, against a nonnegative eight-term rival distinct
from all ones. An odd denominator is never a cancellation premise.

|Family|Complete branches|Verified exclusion identities|Uncertified roles|
|---|---:|---:|---:|
|Long cycles|538|538|0|
|Long paths|498|498|0|
|Pure FOO/FOP layer|64|59|5 at arithmetic layer, 4 after elementary order-seven exclusion|
|PO endpoint opponents|88|88|0|

Total new integer exclusion identities: **1183**. Independent implementations
reconstruct the domains and coverage, and check every saved identity without
importing producer/search functions. They reject **2307** altered multiplier
or noninteger-coefficient certificates. These are separate implementations
by the same agent, not separate human reviews or proof-assistant verification.
The three later producers share the Round 2 certificate-search kernel;
the auditors do not. Independent checking accepts the saved identities,
not the producer's claimed rational rowspace or absence of further witnesses.

The optional Round 1 relaxation has 61 possible overlap spectra, 46
survivors and 15 excluded spectra; an independent enumeration of 125970
multisets of eight row partitions agrees on all 46 spectra and maximum 26.
Every spectrum and row witness is saved. The final regular theorem uses
the elementary weaker maximum 29 instead, removing that computation from
its required dependency chain.

Runtime limits and coverage were stated before each computation, and actual
times are preserved in results. No main research run timed out. Zero-budget control
runs are checked separately and labeled TIMEOUT/incomplete; they do not
overwrite the completed evidence. No random sampling, actual cyclic-set
enumeration, all-modulus search, live candidate witness, or novelty search
was performed. Arithmetic survivors remain symbolic necessary conditions.

## Required versus optional dependencies

|Claim|Required dependencies|
|---|---|
|Regular odd classification|Stage 4 validity/pair uniqueness; Stage 5 regular trees/degrees and affine classification; Stage 6 overlap lemma; Stage 8 local 31/31 and 22/31; Stage 9 no order-three difference; Stage 17 elementary cycle-type reduction; new Rounds 2/3 checked identities; Round 1 elementary incoming-pair bijection|
|No FOP configuration|Stage 8 local 4/31 closure; Round 4 checked identities; validity and odd h=0|
|No PO against isolatedO/FO/PO|New Round 6 identities; Stage 8 local closure/torsion; validity and odd h=0|
|No singleton defect in a fresh fiber|Historical MC and endpoint classification; Stage 15/16/17 two-ordinary opponent exclusions; Round 5 complete classification and Round 6 exclusions|
|Fresh-fiber short component inventory|MC gives pair-shadow; same elementary local h=0 lemmas and new Rounds 2/3 restrictions; Round 4 FOP exclusion|
|Odd h>0 forest/deficit identities|Elementary new Round 8 proof; odd doubling injectivity; validity/pair uniqueness|
|Even small-h parity restriction|Elementary Stage 6 DS/SS matching and signed-relation lemmas, extended DD treatment and parity argument in Round 8|

Historical MC and Stage 16 calculations retain their shared-kernel and
read-only-audit limitations; they were not rerun. Stage 10's four-way
exclusion is not a premise of MC. No claim of independent recertification
is added. The regular theorem does not need these local dependencies.

## Remaining sufficient budgets and next task

The original sufficient condition is |T4|>=89, or
Sigma-D>=53-8(h+R3), because |T4|=36+8h+8R3+Sigma-D
and N>=70+2|T4|. The stronger growth-lemma budget is separate.

The regular odd branch now has Sigma=56,D=0 and is finished. Historical
even h=0 gives subgroup order 254. Odd h=0,R3>0 still has isolated-ordinary
fresh fibers and its aggregate budget to cover. Every h>0 branch still
needs its own budget; Round 8 gives necessary restrictions only. The
antipodal reduction is conditional on the external reported n=7 result.

Choose a specifically classified isolated-ordinary opponent or a global
forest-deficit budget next. Retain the Q+O two-opponent allocation.
Do not rerun completed singleton/long-cycle/long-path exclusions.
Pivot after two rounds with no progress of the stipulated kinds. The
eight-round checkpoint is stage25_round8.md; the original theorem remains
open until all these cases and dependencies are covered.

## Reproduction

Use standard-library Python from this directory. Run a producer before
its independent checker; these overwrite only their designated results.

    python stage18_tree_spectra.py --seconds 30
    python stage18_tree_spectra_independent.py
    python stage19_cycle_roles.py --seconds 60
    python stage19_cycle_independent.py
    python stage20_path_roles.py --seconds 60
    python stage20_path_independent.py
    python stage21_pure_paths.py --seconds 30
    python stage21_pure_independent.py
    python stage23_endpoint_roles.py --seconds 60
    python stage23_endpoint_independent.py
    python stage24_arithmetic_check.py
    python stage25_completion_checks.py

Windows bundled Python:
python.
No historical computation is invoked by these commands.

## Delivery

The local folder is not a Git checkout. PR #6 was verified open/unmerged,
head archived-source. A new branch and PR
stacked on that head preserve historical and unrelated archive files.
All eight checkpoints, scripts, witnesses, independent results and the
updated README/resume are delivered. No PR is merged or retargeted here.
