# Full proof milestone: cyclic minimum for n=8 is248

The odd branch is now closed by the elementary terminal-edge lemma in
stage63_full_bound_proof.md. Combined with the earlier even-order proof,
this establishes N>=248 for every full-valid eight-point cyclic set.
The same document proves attainment at248 by the binary coin argument.

The new global finish has three steps. A normalized triangle supplies
three disjoint doubling pairs. Any distinct-pair sum x+y=z inside A can
be converted into a forbidden eight-term word with a disjoint pair.
Therefore a paired center edge is closed exactly when its tail has an
outgoing doubling edge. After the complete large-class, multi-class and
two-triangle exclusions, the remaining one-triangle shapes have at least
two OPEN paired edges. The source injection leaves them unused, giving
h-q>=2, and the weighted count yields2N>=495 instead of2N<=494.

New completed symbolic dependencies preserve every odd torsion factor:
Stage60 checks1,723,040 positive mass-eight identities, Stage61 checks
1,570,316, and Stage62 checks7,945,564. Their total is11,238,920. The
Stage63 standard-library checker separately checks224 literal rival
identities, the forest counts, the integer contradiction and sharpness.
The completed Stage62 two-triangle graph has no unresolved leaf. Every
refinement requiring another ordinary equality has P<=8 and invokes
the proved P>=9 theorem. Arbitrary pure refinements are permitted.

This is a complete COMPUTER-ASSISTED proof argument assembled from the
proved parity/counting chain and explicit symbolic certificates. The
checkers were separately implemented by the same assistant. It is not
external mathematical review or proof-assistant formalization. A future
review should audit the complete dependency chain, not rerun modulus
sweeps or improve unrelated lower bounds.

The unfinished Stage62 one-triangle discovery tree is terminal and is
NOT a premise. The elementary finish replaces it. Historical Stage56/57
trees and weak/timeout results also remain outside the proof. New
certificate archives are immutable, content-hashed evidence; seven
overwritten discovery filenames were repaired before the Stage62 check
passed. No unverified archive pointers are used in delivery.

The proof and required local dependency archives are preserved together
in one major PR stacked on Stage59, left unmerged for review.
