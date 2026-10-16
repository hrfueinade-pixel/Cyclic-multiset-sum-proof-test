# OpenMath: cyclic unique multiset sums

This archive contains a computer-assisted proof argument for the sharp
minimum cyclic modulus of a full-valid eight-point set: **N_min=248**.
A={0,1,3,7,15,31,63,127} attains the bound modulo248.

Start with [the assembled proof](stage63_full_bound_proof.md) and
[the current frontier](proof_frontier.md). The proof combines the earlier
parity/counting results, checked symbolic exclusions, and an elementary
terminal-edge argument giving2N>=495 when a hypothetical N<=247 would
require2N<=494.

An [independent AI audit](proof_audit_pr28.md) reports no fatal mathematical
or sign error within its audited scope. It is not human peer review or
formal certification. Its two verifier weaknesses are corrected by
[the merge hardening checkpoint](stage64_merge_hardening.md).

## Reproduction

Use Python with assertions enabled (no -O or PYTHONOPTIMIZE):

```text
python -B stage60_certificate_check.py
python -B stage61_certificate_check.py
python -B stage62_certificate_check.py
python -B stage63_finishing_check.py
python -B stage63_dependency_check.py
python -B stage64_verifier_hardening_check.py
```

Stage60/61 archives are delivered as contiguous numbered .part files;
the standard-library readers concatenate them automatically. The manifest
checks the unchanged logical archive hashes. The Stage63 dependency check
certifies package integrity, not the entire mathematical dependency chain.
The audit report traces and checks the inherited claims as well.

Bounded parity checkers save partial output and exit2 on timeout. A status0
is not by itself a substitute for checking complete coverage. The Stage42
exception requires at least89 quartic values; its original94-value evidence
is retained. Regression controls distinguish real certificate checking
from synthetic tests of the process exit paths.

## Privacy checks

The upload uses fresh history and neutral commit metadata. Personal
paths, account references and obsolete source-history identifiers have
been removed from the release contents. See [PRIVACY.md](PRIVACY.md) for
the review scope and the separate visibility of the hosting account.

Run the content scanner and its negative controls with:

```text
python -B privacy_check.py
python -B -m unittest -v test_privacy
```

The content scanner includes decompressed certificate archives and
reconstructed multipart archives. It reports locations and categories
without printing any detected secrets. It supplements the private
identity-specific review; it does not certify anonymity or mathematics.

## Historical records

Earlier stage reports are retained as historical research records. Their
then-current OPEN labels and withdrawn claims are superseded by the active
proof chain and explicit later corrections. In particular, Stage48 repairs
the Stage44 common-tail statement; the corrected Stage53/55 arguments do
not depend on the abandoned Stage50 orientation table.

The incomplete discovery trees, timeouts and weak witness bounds are not
premises of the final argument. Independent human review and Lean
formalization remain future validation work.
