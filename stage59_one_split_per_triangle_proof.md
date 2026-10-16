# Stage59: one genuine quintic split per quartic triangle

Assume a full-valid eight-point set A in an odd cyclic group of order N<248. Retain the established ordinary multiplicity caps, T4<=88, the general source budget, and the split assignment q<=h. The full N>=248 theorem remains open.

**Theorem.** At most one genuine quintic split output can have its unique cubic-pair descent among the three descents of a fixed quartic triangle.

The proof has elementary complete local coverage and pairwise exclusions, with one positive quartic-growth certificate. It does not enumerate moduli or group parameters. The certificate is checked by a separate implementation written by the same assistant; it is not external review or formal certification.

## 1. Exact triangle normalization and split coverage

A quartic triangle is equivalent to three disjoint aligned edges with common value tau=2x-a. Translate every label by -tau. Its six labels become three doubling pairs, and all eight physical positions are

    A=(u,2u,v,2v,w,2w,p,r).

This normalization uses no division. Full validity and protected equal-degree identities are invariant under translation.

Fix the triangle's ordinary cubic descent

    2u+2v = 2v+2u.

The genuine-split normal form from Stage54 gives

    2u+2v+d+e = 2v+2u+d+e = 2z+2u+b+2v,

where z,b,d,e are exactly the remaining four labels w,2w,p,r, all distinct. Thus the only remaining equation is

    d+e=2z+b.                                             (1)

There are exactly12 ordered choices of z,b; d,e are the unordered complement. This covers every genuine split descending to this cubic pair, with no assumptions about additional cubic relations. Once z,b are specified, all three quintic words and the output are determined.

## 2. Eliminate ten of the twelve choices

The following table is literal coverage of (1). The p/r alternatives are displayed together; the checker reconstructs all12 presentations from ordered physical frames.

|z|b|Necessary equation|Exclusion or residual|
|---|---|---|---|
|w|2w|p+r=4w|The protected squarefree pair p+r equals the repeated pair 2(2w).|
|w|p or r|r=p or p=r|Physical labels collide.|
|2w|w|p+r=5w|The protected squarefree triple w+p+r equals 3(2w).|
|2w|p or r|r=p+3w or p=r+3w|A non-original mass-eight word is 3u+3v+2r, or 3u+3v+2p, respectively.|
|p or r|w|w+r=2p or w+p=2r|A protected squarefree pair equals a repeated pair.|
|p or r|2w|r=2p+w or p=2r+w|Positive quartic growth to89 values, below.|
|p|r|3w=2p+r|Necessary residual.|
|r|p|3w=p+2r|Necessary residual.|

For the mass-eight rival row, the original sum is 3u+3v+3w+p+r. Substituting r=p+3w changes its last three summands to2r. The proposed rival has exactly eight terms; it repeats u,v,r and differs from the original word. The swapped case is identical.

For the growth row, it suffices to exclude p=w+2r. This equation has the exact, surjective parameterization

    A=(u,2u,v,2v,w,2w,w+2r,r)

over any abelian group. The coefficient of p is one, so no odd torsion is discarded. The saved certificate selects89 repeated quartic words. For every pair Wi,Wj it supplies a nonnegative mass-eight word R different from the original, an integer k, and a positive power of two f, with the exact integer identity

    f*(value(R)-sum(A)) = k*(value(Wi)-value(Wj)).          (2)

There are89*88/2=3,916 such identities, checked directly in the four free coordinates u,v,w,r. If Wi and Wj coincided in an odd group, (2) would force value(R)=sum(A), since f is invertible. Full validity forbids this. Therefore all89 quartic values are distinct, contradicting T4<=88. Swapping p and r excludes r=w+2p with the same certificate.

The only necessary residuals for this fixed cubic descent are therefore

    3w=2p+r, or 3w=p+2r.                                 (3)

No bound obtained by the absence of witnesses or by a timeout is used.

## 3. Six residual presentations, at most one compatible

Apply Section2 to each of the triangle's three cubic descents. The six necessary presentations are

    3xi=2p+r or 3xi=p+2r,    xi in {u,v,w}.                (4)

Each presentation determines its quintic fiber uniquely. All15 pairs of distinct presentations are incompatible:

1. **Different xi, same orientation.** The two equations give 3xi=3xj. This equates the distinct protected squarefree pairs xi+2xi and xj+2xj. There are six such pairs of presentations.
2. **Same xi, opposite orientation.** Subtraction gives p=r, a physical label collision. There are three such pairs.
3. **Different xi, opposite orientation.** Name them so 3xi=2p+r and 3xj=p+2r, and let xk be the other triangle center. The original sum is

       3xk+3xi+3xj+p+r = 3xk+4p+4r.

   Take xk and2xk once each, xi and2xi twice each, and r twice. This non-original eight-term word has value

       3xk+6xi+2r = 3xk+4p+4r.

   It is a forbidden mass-eight rival. There are six such pairs.

These identities use no cancellation by three. The checker verifies all15 pairs in the exact five-coordinate triangle family. Two distinct genuine split outputs supported by the triangle would give two distinct presentations in (4), which is impossible. This proves the theorem.

## 4. Global split compression

Let P=P3ordinary. Let D be the SET of ordinary cubic pairs that occur in at least one actual quartic triangle, counted once even when reused. Every split has a unique cubic descent.

- At most4(P-|D|) splits descend outside D, by the Stage54 four-splits-per-pair lemma.
- At most t splits descend inside D: assign each such split to any triangle containing its descent. No triangle can receive two splits by the theorem just proved, so this assignment is injective.

Consequently

    q <= 4(P-|D|)+t.                                    (5)

The established triangle-incidence bound says each cubic pair feeds at most two triangles, so3t<=2|D|. Hence also

    q <= 4P-5t.                                         (6)

The set-level form (5) is often stronger and is needed for the forest corollary. Neither (5) nor (6) alone proves the full bound.

## 5. Verification and exact boundary

Run `python -B stage59_certificate_check.py` with the adjacent archive `stage59_one_split_certificates.json.gz`. The checker imports no producer or prior checker. It reconstructs12 local cases, checks eight direct exclusions and the two symmetry uses of one growth prototype, verifies all3,916 positive quartic identities, and constructs all15 residual-pair exclusions. Its forest calculation independently lists integer partitions of eight and all path matchings.

The archive SHA256 is2f10f531380a470f3b73d586610b4a2136dcc32fecd087c1576814ca5b6798a2. Larger local discovery files and the incomplete Stage57 tree are not premises. The next section of the proof is in stage59_forest_residual_proof.md. General N>=207, the even-order exclusions, equality248, and the historical discovery boundaries are unchanged.
