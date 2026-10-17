# Verification guide

Run `python verify.py` from the repository root with Python 3.12 or later.
No third-party packages, network connection, or solver are required.
A fresh run can take tens of minutes; enumeration speed depends on the computer.

The command checks release hashes, eleven symbolic certificate families,
150 freshly enumerated case/order combinations, the seven-point extensions
and antipodal lifts, elementary identities and sharpness, failure controls,
and the public privacy scanner. It requires assertions and refuses Python
optimization mode. Symbolic checkers use exact integer identities and retain
odd torsion; finite parity checkers reconstruct their domains.

Results go into ignored `.verification/`: `summary.json`, per-check logs,
and per-order completion records. Source certificates are immutable; checkers
run on isolated generated copies. The success status is
`FULL_CHECKS_PASSED`. Any failed, missing, or incomplete obligation returns
a nonzero exit code and `INCOMPLETE`. A hash match establishes package
integrity, not the mathematics of a certificate.

The default is a fresh run. If an enumeration deadline is too short on a
slower computer, increase it explicitly:

```sh
python verify.py --seconds-per-order 300
```

CI uses this longer per-order deadline to allow for shared-runner speed.
Every order must still complete; a larger deadline never accepts a partial run.

To continue a previous local run, use `python verify.py --resume`.
Only completed records with the same enumeration-code fingerprint are reused;
coverage is checked again and the reused count is reported. Local cache files
are trusted inputs in this mode: edit or delete them only if you intend to
rerun the affected cases. Fresh verification is the release/CI standard.

For development, `--only symbolic`, `--only parity`, and `--only elementary`
run limited phases. They can report only `LIMITED_PHASE_PASSED`. They never
claim a full verification. Changes to published inputs require regenerating
`certificates/manifest.json`; see the maintenance script below.

The checks test mathematical certificates, not their discovery algorithms.
The finite parity enumerations are rerun because an old success report or
saved list of survivors alone would not prove domain coverage. Unit tests
also demonstrate that truncated quartic separation at 87 or 88 is rejected,
89 is sufficient, corrupted signs and units are rejected, and incomplete,
duplicate, missing, and changed-code enumeration records fail.

Human review should establish the reductions, completeness of the symbolic
models, and interpretation of every leaf. The checked counts are controls
against accidental truncation. They do not replace those arguments.
