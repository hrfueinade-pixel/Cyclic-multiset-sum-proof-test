# Stage 53: the entire no-ordinary-quartic-triple branch is closed

2026-10-12. Continues the accepted full-modulus proof plan and open PR 22 at archived-source. The workspace remains an archive; delivery uses the GitHub connector. No PR is merged.

**New computer-assisted structural theorem:** in the hypothetical full-valid odd N<248 branch with C4=0, every genuine quintic split can be assigned to a distinct incident open doubled-center edge. Thus q<=h. Together with E>=2q and the Stage 48 packing inequality, this closes the ENTIRE C4=0 branch, rather than merely lowering a cubic-center bound.

**The full N>=248 theorem remains OPEN.** Remaining cases have ordinary quartic triples of some type; these need not be triangles. The inherited general N>=207 and even N>=248 conclusions are unchanged, and arbitrary odd207..247 are not newly excluded in full. Equality at248 remains allowed.

Read stage53_global_split_proof.md for all hypotheses, local coverage, the elementary component assignment and the final branch contradiction.

## What changed mathematically

Four new finite local lemmas rule out repeated root marks, marks at both ends of one auxiliary edge, a root followed by a longer auxiliary path, and three auxiliary edges at a vertex. Parallel auxiliary edges are also excluded. Therefore each auxiliary component is an unmarked path/cycle or a path with one mark, which supplies the global injection into h resources.

The previously proposed component compensation inequality is unnecessary in this branch: no deficient component exists. In particular, the proof does not assume unused bonuses are distinct or try to share R3 credits between components. It does not require P3<=17 or the pending all-single-open Stage51 assertion.

This is a proof of a full structural branch. Its local lemmas are computer-assisted, with integer certificates and complete symbolic coverage. It is not advertised as a wholly elementary proof or independent human/formal certification.

## Scope and evidence

The standalone checker imports no producer or historical checker. It constructs the split presentations independently from a shared quartic source and its unused labels, verifies every listed case and explicit skip, and checks 23,367 new integer identities. Only powers of two are canceled. A corrupted multiplier and nonunit cancellation are rejected.

The necessary closed-both-source exception is normalized completely, and the retained Stage49 positive growth certificate is included in the new archive: all6,670 pair identities separate116 repeated quartic values. The old discovery producer is not rerun. No unpublished Stage49 theorem needs to be accepted without its evidence.

No moduli, group elements or group parameters are enumerated. No historical modulus search, timeout enlargement, Lean conversion, or Stage45 residual reclassification is performed. Passing controls and incomplete witness searches are not used as exclusions; every final claimed local case has positive evidence.

## Reproduce

Python3, standard library only. To verify the shipped certificate archive:

    python -B stage53_certificate_check.py

To regenerate the NEW symbolic identities (the bounded timeout raises an error on incomplete coverage):

    python -B stage53_connected_split_probe.py --seconds 120 --full
    python -B stage53_connected_split_probe.py --seconds 120 --propagation
    python -B stage53_connected_split_probe.py --seconds 120 --three-open
    python -B stage53_connected_split_probe.py --seconds 120 --isolated-marks
    python -B stage53_certificate_pack.py
    python -B stage53_certificate_check.py

The packer retains the historical positive closed-split certificate from the shipped archive if its older local source JSON is absent. The checker uses the bundled identity data; it needs no optional libraries or external solver.

Artifacts: stage53_global_split_proof.md, stage53_connected_split_probe.py, stage53_certificate_pack.py, stage53_certificate_check.py, stage53_split_graph_certificates.json.gz, and stage53_independent_results.json.

## Next required proof

Extend the global accounting to C4>0. Quartic path/star outputs which were contradictions under cap two must be charged with their actual inverse maps; triangles and split triples must not consume the same witnesses twice. The full weighted inequality and the terminal T4>=89 or T3+T5>=192 dichotomy remain unproved. This is the next main mathematical objective, not another dense-center audit.
