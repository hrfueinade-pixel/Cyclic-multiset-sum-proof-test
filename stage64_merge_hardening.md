# Verifier hardening before merging the proof chain

The independent AI audit of PR28 at archived-source
found the argument sound within its audited scope and reported no fatal
sign error. It identified two operational verifier weaknesses. This
checkpoint corrects both, without changing the mathematical search logic
or any positive proof certificate.

1. Stage42 now requires at least89 distinct repeated quartic values for
   the exception3 exclusion. The bound N>=71+2*T4 then excludes N<248.
   The original94-value certificate is unchanged and remains sufficient.
   Genuine87- and88-value truncated certificates are now rejected;
   the valid89- and94-value controls are accepted.
2. Stage32 and Stage34 still save their explicit incomplete evidence
   after timeout, but now exit with status2. Complete runs keep status0.
   Consumers must inspect completeness and expected coverage as well.

Run python -B stage64_verifier_hardening_check.py. The quartic controls
check genuine certificate identities. The parity controls replace only
the run function in temporary copies to exercise complete/timeout exit
paths; their synthetic successful reports are NOT parity-proof evidence.
The original independent audit reproduced the actual parity mathematics.
No time limit was enlarged and no incomplete run was promoted to a proof.

The audit report is preserved in proof_audit_pr28.md. It describes the
pinned pre-hardening version; these fixes are additional tested changes,
not an alteration of that historical audit. The complete proof remains
computer-assisted, with AI audits rather than external human review or
proof-assistant certification. The manifest is an integrity check, not
an independent proof of all earlier dependencies.

All existing proof PRs are a dependency chain. They are merged oldest
first into main using merge commits so descendants retain their ancestry.
The final PR carries these fixes; no extra PR is needed.
