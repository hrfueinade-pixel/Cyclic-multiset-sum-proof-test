# Cyclic multiset sums: the eight-point minimum

A computer-assisted proof that eight distinct residues whose total has a
unique eight-term multiset representation require a cyclic group of order
at least **248**. The bound is attained by

$$
\lbrace 0,1,3,7,15,31,63,127\rbrace\subset\mathbb Z/248\mathbb Z.
$$

Start with the [proof](PROOF.md). It defines the problem, explains the
counting argument, and identifies each finite lemma. The supporting chapters
contain the detailed reductions and the interpretation of the certificates.

| Read or do | Location |
| --- | --- |
| Understand the complete argument | [Proof and notation](PROOF.md) |
| Check the even-order reduction | [Parity and small sets](proof/parity.md) |
| Understand the multiplicity caps | [Multiplicity](proof/multiplicity.md) |
| Derive the weighted inequality | [Counting](proof/counting.md) |
| Follow the source allocation | [Assignment](proof/assignment.md) |
| Follow the remaining triangle cases | [Alignment](proof/alignment.md) |
| Check the final contradiction and equality | [Closing argument](proof/closing.md) |
| Run or inspect the computations | [Verification guide](docs/verification.md) |
| Trace the retained research material | [Provenance](docs/provenance.md) |

## Verify

Use Python 3.12 or later, with its standard library:

```sh
python verify.py
```

This checks the symbolic certificates, freshly enumerates all 150 required
case/order combinations, checks the equality example, and runs failure and
privacy controls. Success ends with `FULL_CHECKS_PASSED`. Incomplete runs
fail. See the [guide](docs/verification.md) for outputs and explicit resumption.

## Review status

The package presents a computer-assisted proof. Automated verification checks
the supplied identities and finite coverage; the written mathematical
reductions still require human review. This work has not received independent
external mathematical review or proof-assistant certification. No claim of
novelty is made. The [corrections and review boundary](docs/review-status.md)
record the relevant limits.

The research history and experiments remain in the original archive. This
repository is the reading and verification edition.
