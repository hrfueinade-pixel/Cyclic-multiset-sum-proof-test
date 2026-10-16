# Stage61: all quartic triangles belong to a single alignment class

LOCAL PROOF CHECKPOINT. Full N>=248 remains OPEN. No new PR has been created.

Under the full-valid odd N<248 hypotheses, there is at most ONE alignment value supporting a quartic triangle. Together with the checked Stage60 four-edge theorem, the total number of quartic triangles is at most TWO. Every paired edge from any triangle lies in one of the three small forests (2,2,2,1,1),(4,2,1,1),(3,2,2,1).

## Complete interaction coverage

Normalize one triangle to A=(u,2u,v,2v,w,2w,p,r). A second triangle consists of three disjoint directed edges on these same eight physical labels, with a common alignment gamma. There are3,360 literal presentations: choose three centers, three tails among the remaining five labels, and a bijection. For edges (xi,ai), impose the two equations2Axi-Aai=2Ax0-Aa0. No odd integer is divided out.

Exactly one presentation has gamma=0 formally. Another603 force gamma=0 through their integer relation modules. These are rejected only under the selected hypothesis that the second class is DIFFERENT; they are not full-model exclusions. The remaining2,756 presentations use unconditional model exclusions or a complete residual proof.

The initial residual modules give14 types under permutation of the three primary doubling pairs and of p,r. By explicit relabeling and translation using an actual triangle, they reduce to nine affine families. Each has six formal ordinary cubic collision pairs. A counterexample needs at least nine by Stage58, so every family must acquire a new PRIVATE ordinary collision.

The alternating seven-vertex-path family is represented by

    u+4v=5w,    20v+r=21w.

Its complete first refinement leaves one system with eight ordinary pairs, so another ordinary equality is compulsory. All next cases close positively. This excludes the entire alternating family, allowing all additional relations and retaining all odd torsion.

For the other eight affine families, complete first-private-pair coverage leaves precisely two unresolved modules. They have seven and eight ordinary pairs, respectively. Another ordinary equality is compulsory in both, and all of those next cases close positively. No further branch is needed. Weak quartic-growth bounds in the first residuals are never used as exclusions.

All accepted closures are direct protected/label/multiplicity contradictions, explicit mass-eight rivals, checked alignment-cycle/source premises, applications of Stage60's four-edge bound, an explicit affine map to the already excluded alternating family, or positive separation of89 repeated quartic words. Every affine map is a permutation of all eight physical positions followed by translation; it preserves full validity and cancels no odd factor.

## Complete checker

Run `python -B stage61_certificate_check.py` with `stage61_interaction_certificates.json.gz`. The separate implementation imports the existing Stage60 checker helpers, but no producer or elimination code. It reconstructs second-triangle coverage from all ordered eight-label frames, rebuilds private-pair coverage from the56 ordinary cubic words, verifies every unimodular reduction and retained odd factor, and checks the physical permutation or affine frame for every reused model.

The check passed3,360 second-triangle presentations;5,605 private direction cases;6,667 literal private cases;803 alternating proof nodes and2,857 needed coupling proof nodes; and1,570,316 positive mass-eight pair identities. The archive SHA256 is333c4cbd58bf769ae7d9e2f2ffc7f3cc8fbc6115a0da9ac7662eec694dc6d753. This is same-assistant separate-implementation checking, not formal or external certification.

The proof is acyclic: the alternating family closes using Stage60 and P>=9; the remaining affine families can then reuse that completed result. The interaction theorem itself is not a premise of its own finite closures. All producer and checker sessions for this interaction proof are terminal.

## Remaining full-proof target

A hypothetical counterexample therefore has one triangle-bearing class, with one or two triangles. Stage59 requires at least six, five, or five ordinary cubic pairs outside that class for the respective three shapes. Those external classes have no quartic triangles.

The next proof must exclude these single-class external-collision systems, or show that they satisfy

    5t<=2(h-q+R3+c)+5w+U,    U=E-2q,

or |T3|+|T5|>=192. The interaction theorem is a new global restriction; it does not by itself establish full N>=248 or exclude every remaining odd modulus.
