# Review record and corrections

This package is ready for **focused mathematical review** as an AI-assisted,
computer-assisted proof proposal. No fatal mathematical gap was found in
this audit of the written reductions and retained finite contracts.
Independent external human review and proof-assistant certification remain
absent. The repository owner does not claim personal authorship of the proof.

## Baseline and evidence

The audit started at
[`888e5314b74bb26de60876d922cfaffcd92e117b`](https://github.com/hrfueinade-pixel/Cyclic-multiset-sum-proof-test/commit/888e5314b74bb26de60876d922cfaffcd92e117b).
No AGENTS.md or additional repository instructions were present. The
original research archive at `83892af4a9fa3aea516eb17af01bbb8b9c8467ba`
and all source certificate bytes were preserved. Work is on the separate
`audit/mathematical-review` branch.

| Evidence | Scope |
| --- | --- |
| [Earlier CI run](https://github.com/hrfueinade-pixel/Cyclic-multiset-sum-proof-test/actions/runs/39056481137) | GitHub reported success at the starting commit. This was read, not rerun or substituted for the baseline. |
| [Baseline bundle](../review/baseline.json.gz) | Personally ran Python 3.12.14, `python verify.py --seconds-per-order 300`, exit 0, 1,009.65 seconds, FULL_CHECKS_PASSED. All 150 required orders completed; no cache reuse. |
| [Pre-hardening full run](../review/pre-hardening.json.gz) | Personally completed all 150 orders again, exit 0, 1167.30 seconds. This predates the final integer-input guards and is not substituted for the submitted-source run. |
| [Interrupted runs](../review/editorial-interruption.json.gz) | Two early runs were explicitly stopped for final editorial corrections; exit 143, INCOMPLETE. Their captured logs are retained and supply no exclusion. |
| [Submitted-source bundle](../review/release.json.gz) | Fresh full run against the submitted source manifest. Contains its exact outcome, console, all checker logs/reports and 150 per-order records. The recorded exit status and completion counts are authoritative. |

Bundles retain complete output, not excerpts. Their source manifest digest
binds evidence to the corresponding files. The release manifest and release
evidence are submitted together; evidence is outside its own source hash
inventory. See [verification instructions](verification.md). Negative
controls deliberately produce incomplete records and reject altered
certificates; those are tests, not mathematical exclusions. No unsuccessful
search or historical timeout is used as a proof premise.

## Mathematical audit and repairs

The counting derivation was reconstructed from protected squarefree words:
complementary packing, the 36 distinct midpoints, private centers,
recoverable pair lifts, and all four triple correspondences. It separates
word pairs from value outputs and includes mixed-only quintic fibers.
The constant 496 and coefficients $(2,-5,0,5,-4,1)$ are derived in
[Lemma 6](../proof/counting.md), rather than asserted by a coefficient test.
The domain of $R_3=\sum_{y:m_y\ge1}\binom{m_y-1}{2}$ is explicit.
Sets $\mathcal T_d$ and their cardinalities $T_d$ have distinct notation.

The source audit covers all third centers and ten tail choices, surjective
unit-minor and torsion parameterizations, 901 first and 4,339 second total
cubic directions, and the independent six-pair forcing argument. Recoverable
source pairs are counted as E outputs only after exactly-two-ordinary
fibers are established. The 56 former cap-two triggers now have
[traceable identifiers](assignment-replacements.md). Stars use the
one-cubic-triple/one-split lemma; paths and triangles use positive rivals,
source contradictions, or at least 89 separated quartic values. No trigger
silently treats a quartic triple as forbidden under cap three.

The auxiliary graph uses open **center edges** as vertices, split outputs
as edges or marks, and source **fibers** as a separate inventory. Complete
local coverage handles repeated presentations, parallel edges, shared
physical labels, marks and paths. Componentwise orientation gives the
injection q<=h. Ownership removes the set of paired triangle vertices once,
giving q<=h-o. These distinctions are exposed in the expanded dependency
ledger and [certificate contracts](certificates.md).

The seven-point argument precedes the eight-point baseline. The subset
cube, at-most-one-antipodal-pair lemma, quotient validity, affine lift maps,
subgroup reductions and normalization, including explicit parity-preserving
affine lifts and their inverses, were checked against the actual
enumeration code. All 58 nonsaturated six-sets must be extended; every
required order and every nonunit preimage is retained. Partial brute force
is not a seven-point proof.

Cycle rivals and the graded quotient bounds were checked, as were all nine
forest incidence rows, the six large-forest exclusions, inter-class
interaction coverage and the entire two-triangle component. A useful hand
simplification moves the unconditional terminal-edge argument earlier:
terminal paired edges remain open under **arbitrary** additional equalities.
It shortens the nine-ordinary-pair proof and replaces obsolete pure-closure
case analysis. The final hypotheses are collected in [Closing](../proof/closing.md):
E-2q>=0, q<=h-o, t=1 and o>=2 imply 2N>=495>494.

## Computational changes

- Removed unused conditional quintic-credit machinery from the final
  checker. The retained archive has 31 P<=8 forcing nodes, 2,029 quartic
  growth leaves, five unconditional credit leaves and one shared-descent
  split guard. Forcing nodes require complete further ordinary branching;
  pure refinements remain allowed. Unsupported conditional rules now fail.
- Rejected fractional words and nonintegral matrices in the relevant
  certificate helpers and the independent validator. The old helper accepted
  a fractional rival from a relation that holds on the valid binary set at
  order 255; the new regression rejects it. Determinant one alone does not
  make a rational matrix unimodular. The supplied certificate vectors are
  integral, so this is checker hardening rather than an altered certificate.
- Bound multiplicity certificates to their actual model, degree and allowed
  canceled units. A quintic separation or a certificate requiring an
  unestablished unit cannot establish a quartic contradiction. The threshold
  is at least 89, with explicit failure controls for 87 and 88.
- Consolidated repeated parity sumset, extension and normalization code.
  Added direct exhaustive oracles for those shared helpers, all nonunit
  preimages, invariance, heredity, antipodal projection and lift coverage.
  Smaller binary examples test general pair lifts, not eight-specific caps
  or global minima 60 and 124.
- Added an implementation using ordered physical frames to recheck all
  29,466 refinement branches at 42 forcing nodes, plus small cyclic
  surjectivity checks retaining 3-, 5-, and 9-torsion. Failure controls reject
  missing/duplicate branches, invalid symmetries, odd cancellation, weakened
  thresholds and conditional-leaf misuse. Timeouts retain partial logs.

Markdown links, equation delimiters, and mathematical notation were inspected.
A dedicated renderer installation was not completed: automatic approval review
hit an account usage limit. No rendered-browser check is claimed.

## Limits and further simplification

The arbitrary-set lower bound still depends on computer-assisted lemmas;
only its final substitution and equality example are elementary. Shared
checker helpers are common sources of error. Another AI implementation is
not independent external human review. The mathematical bridges and leaf
premises deserve that review even when all software checks pass.

Focused attempts did not yield a complete shorter hand proof of the
seven-point minimum or the remaining two-triangle family. Neither finite
exclusion is replaced by an unsuccessful search or a conjecture. The
conceptual assignment is the path/cycle injection already given; its local
source obligations remain explicit. No exploratory conjecture is a premise.

Suitable Lean targets are the validity definition, squarefree protection,
heredity/invariance, complementary packing, common-tail lift inverses,
fiber counting identities, and the graph assignment injection. No Lean
runtime was installed or formalization checked in this audit. Adding
assumed computational lemmas would not certify the complete theorem.

The fixed-binary theorem is already in [Fonollosa and jarfo/min-modulus](references.md).
The proposed contribution here is its arbitrary-eight-set cyclic lower
bound. Novelty has not been established. Complete historical discovery
regeneration is unavailable for several certificate families; positive
certificate verification is reproducible without it. No license or new
human attribution was selected.

## Earlier corrections retained

- Quintic paths have a common tail; removing it gives the quartic path.
  Quintic splits have none.
- Quartic separation must reach at least 89 values to contradict T4<=88.
- The general assignment replaces every earlier cap-two inference.
- Seven-point and balanced parity searches require all orders to complete;
  historical timeouts are not exclusions.
- The two-triangle certificate closes only its stated component. The
  terminal-edge lemma closes the two remaining one-triangle forests.
