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

## Independent controls and evidence

The full command also runs `python -m verification.independent` and the
small exhaustive oracles in `tests/test_mathematics.py`. See the
[certificate contracts](certificates.md) for their scope and shared-code
boundaries. Six- and seven-point examples test general protection and pair
lifts; they do not rerun the eight-point proof at another n or prove minima
60 and 124.

The [review record](review-status.md) links complete baseline and release
logs, reports, and all per-order records. Evidence is JSON compressed with
gzip in `review/`; extract it with Python's `gzip` and `json` modules. Each
bundle records its command, exit code, Python version, and the digest of
`certificates/manifest.json`. The release bundle and source manifest belong
to the same submitted tree. Evidence is outside the manifest's source
inventory to avoid a self-referential hash; its recorded source digest must
match the checkout. The source certificates have not been changed.

A process timeout now retains its partial stdout/stderr log. It is always
`INCOMPLETE`, including when some earlier obligations passed. Prior CI
results are separately identified and do not replace a personal fresh run.

## Regeneration and the historical archive

The original research material is preserved in this repository's Git
history at
[`83892af4a9fa3aea516eb17af01bbb8b9c8467ba`](https://github.com/hrfueinade-pixel/Cyclic-multiset-sum-proof-test/tree/83892af4a9fa3aea516eb17af01bbb8b9c8467ba).
Inspect it in a separate checkout:

```sh
git worktree add --detach ../cyclic-research 83892af4a9fa3aea516eb17af01bbb8b9c8467ba
```

The [source map](source-map.json) gives the exact original certificate names
and concatenation order. For example, concatenate `stage60` numbered parts
in increasing order to reconstruct `large-forests.json.gz`; the resulting
bytes must match the source map's SHA-256. A hash is an integrity check,
not certificate verification.

| Published family | Exact historical generator/packager references |
| --- | --- |
| Initial multiplicity | [stage41_saturated_fiber_closure.py](https://github.com/hrfueinade-pixel/Cyclic-multiset-sum-proof-test/blob/83892af4a9fa3aea516eb17af01bbb8b9c8467ba/stage41_saturated_fiber_closure.py), [stage41_pack_certificates.py](https://github.com/hrfueinade-pixel/Cyclic-multiset-sum-proof-test/blob/83892af4a9fa3aea516eb17af01bbb8b9c8467ba/stage41_pack_certificates.py) |
| Cubic exception and four-pair/chain growth | [stage42_symbolic_probe.py](https://github.com/hrfueinade-pixel/Cyclic-multiset-sum-proof-test/blob/83892af4a9fa3aea516eb17af01bbb8b9c8467ba/stage42_symbolic_probe.py) (`--model`, `--degree`, `--target`) |
| Quintic cap | [stage43_fourpair_inventory.py](https://github.com/hrfueinade-pixel/Cyclic-multiset-sum-proof-test/blob/83892af4a9fa3aea516eb17af01bbb8b9c8467ba/stage43_fourpair_inventory.py), [stage43_joint_relations.py](https://github.com/hrfueinade-pixel/Cyclic-multiset-sum-proof-test/blob/83892af4a9fa3aea516eb17af01bbb8b9c8467ba/stage43_joint_relations.py), [stage43_relation_growth.py](https://github.com/hrfueinade-pixel/Cyclic-multiset-sum-proof-test/blob/83892af4a9fa3aea516eb17af01bbb8b9c8467ba/stage43_relation_growth.py), [stage43_pack_certificates.py](https://github.com/hrfueinade-pixel/Cyclic-multiset-sum-proof-test/blob/83892af4a9fa3aea516eb17af01bbb8b9c8467ba/stage43_pack_certificates.py) |
| Base assignment | [stage53_connected_split_probe.py](https://github.com/hrfueinade-pixel/Cyclic-multiset-sum-proof-test/blob/83892af4a9fa3aea516eb17af01bbb8b9c8467ba/stage53_connected_split_probe.py), [stage53_certificate_pack.py](https://github.com/hrfueinade-pixel/Cyclic-multiset-sum-proof-test/blob/83892af4a9fa3aea516eb17af01bbb8b9c8467ba/stage53_certificate_pack.py) |
| Source fibers | [stage54_source_triple_probe.py](https://github.com/hrfueinade-pixel/Cyclic-multiset-sum-proof-test/blob/83892af4a9fa3aea516eb17af01bbb8b9c8467ba/stage54_source_triple_probe.py), [stage54_source_path_cubic_inventory.py](https://github.com/hrfueinade-pixel/Cyclic-multiset-sum-proof-test/blob/83892af4a9fa3aea516eb17af01bbb8b9c8467ba/stage54_source_path_cubic_inventory.py), [stage54_source_path_second_cubic.py](https://github.com/hrfueinade-pixel/Cyclic-multiset-sum-proof-test/blob/83892af4a9fa3aea516eb17af01bbb8b9c8467ba/stage54_source_path_second_cubic.py), [stage54_certificate_pack.py](https://github.com/hrfueinade-pixel/Cyclic-multiset-sum-proof-test/blob/83892af4a9fa3aea516eb17af01bbb8b9c8467ba/stage54_certificate_pack.py) |
| General assignment | [stage55_split_exception_probe.py](https://github.com/hrfueinade-pixel/Cyclic-multiset-sum-proof-test/blob/83892af4a9fa3aea516eb17af01bbb8b9c8467ba/stage55_split_exception_probe.py), [stage55_certificate_pack.py](https://github.com/hrfueinade-pixel/Cyclic-multiset-sum-proof-test/blob/83892af4a9fa3aea516eb17af01bbb8b9c8467ba/stage55_certificate_pack.py) |
| Ownership, triangle splits, forests, interactions, two-triangle closure | Certificate archives and standalone checkers are preserved; complete discovery generators are not present in the pinned archive. |

The working recovery and discovery commands are:

```sh
python -m verification.regeneration recover --programs
python -m verification.regeneration generate --recipe all
```

Recovery restores all 24 retained certificate inputs, including the exact
ordered concatenation of split archives and the union of **completed**
4+4 reference rows. It checks every resulting hash before writing files.
`--programs` also restores 29 historical programs, each pinned by SHA-256.
Generated files go under ignored `.verification/`, never over the proof's
certificate inputs. A full Git clone containing the archive commit is needed
for recovery; a shallow checkout is insufficient.

Fresh discovery runs the four Stage 41 recipes and three Stage 42 recipes
in new isolated directories, then validates each result using the current
checker, without importing the discovery program. The seven resulting JSON
payloads reproduce the published witnesses. Gzip container headers may differ
across platforms; byte identity is reported separately from JSON equality.
A process failure, timeout or insufficient positive bound returns INCOMPLETE,
with its complete log retained. It never establishes a mathematical exclusion.
Use `--recipe NAME` for one of the seven names in [generation.json](generation.json).

The recovered `stage43_fourpair_inventory.py` also regenerates the fixed
cubic-direction inventory. Its output is not a growth certificate. The
current quintic-cap checker independently reconstructs all its directions.

Several later packagers need discovery outputs that were not retained, and
complete later-family discovery programs are absent from all repository
history. The catalog records these limits per input. Therefore **complete
proof discovery regeneration remains unavailable**. Archive restoration is
not fresh discovery; fresh discovery is not certificate verification. The
positive certificate bytes are sufficient for `verify.py`, which trusts
neither discovery nor old success reports. The release bundle includes the
recovered programs for offline execution of the seven complete recipes; see
[publication instructions](publication.md).

Finite parity evidence is regenerated fully by `python verify.py`; saved
references supplement that fresh enumeration. `verification/seal.py`
regenerates only integrity metadata after intentional edits, never missing
mathematical evidence.

To export a complete captured run, retain its console and use the exact exit
code (including a nonzero code for an incomplete run):

```sh
python -m verification.evidence --console /path/to/console.log --exit-code 0 --output review/release.json.gz
```

The exporter checks the run's manifest digest before attaching its artifacts.
It does not turn an incomplete run into a success.
