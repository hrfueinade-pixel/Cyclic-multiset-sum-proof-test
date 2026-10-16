# Skeptical audit of the cyclic eight-point minimum proof

Audit date: October 12, 2026, America/New_York. Auditor: an independent execution of an AI assistant, not human peer review or formal certification.

Target: `the source research archive`, PR #28, pinned head `archived-source`; parent `archived-source`.

## Verdict

**Sound within the audited scope, with nonfatal verification weaknesses found.** I found no failing mathematical identity, lost hypothesis, missing required leaf, circular dependency, or fatal sign error in the proof actually used at this commit. The lower-bound argument and the sharp modulo-248 example survive this audit. This conclusion combines reconstructed mathematical arguments with verified finite evidence; it does not follow merely from successful script exits.

Two verifier weaknesses deserve attention: the Stage42 exception threshold is weaker than its exclusion requires, and bounded parity checkers return exit code zero after an incomplete run. Both were demonstrated. The pinned Stage42 evidence itself is sufficient. Timed-out portions of the parity reproduction were checked separately with unchanged algorithms and original time limits. No canonical proof file was repaired.

Scope excludes novelty, external literature claims, Lean verification, historical discovery completeness, and files not needed by the active dependency chain. The original, withdrawn Stage50 intermediate messages/table are not in the pinned repository; the local historical files describe their withdrawal. I verified the corrected orientation and its replacement in the active code, rather than claiming to have inspected every withdrawn cell.

## 1. Provenance and reference convention

All file/line references below refer to the pinned versions in `snapshot/`, unless explicitly labelled **local historical context**. Repository-relative references can be opened at:

`<file>#L<line>`.

The GitHub connection confirmed the head, its parent, and PR28's current head/base. The complete remote tree was not truncated: 458 blobs. Local bytes matched 456 immediately. `README.md` and `research_resume.md` differed; their exact pinned versions were fetched and verified by Git blob SHA. Thus all 458 source blobs were acquired and verified. Comparing the parent tree gives 418 unchanged inherited blobs and 40 added/changed blobs. The proof is not limited to those 40 files.

Evidence: `pinned_commit.json`, `remote_tree.json`, `parent_tree.json`, `pr_metadata.json`, `snapshot_verification.json`, and `audit_scope.json`. The main source artifacts remain unchanged in the user's workspace. Checkers wrote regenerated result files only inside the audit copy; those fresh outputs must not be confused with the original hashed result blobs. Manifest verification preceded those writes.

The Stage50 files requested by the objective are absent from both pinned head and parent. Their local copies and SHA256 hashes are preserved in `historical_context/` and `audit_scope.json`. They are contextual evidence, not pinned premises.

## 2. Ranked findings and smallest repairs

### 1. Stage42 accepts a growth bound insufficient for its published exclusion

Reference: `stage42_certificate_check.py:87–95`, especially line 91; compare `stage42_findings.md:198–215`.

The final assertion accepts an exceptional quartic certificate with **87** distinct repeated values. In odd order, this yields only `N >= 71+2*87 = 245`; it leaves 245 and 247. The exceptional-cubic exclusion needs at least 89 quartic values, or another supplied exclusion of the remaining orders.

Concrete control: retain only the first 87 of the original 94 quartic words and precisely their valid pair witnesses. Run the unmodified Stage42 checker in a separate directory. It accepts this weakened package. See `stage42_threshold_control.py` and `stage42_threshold_control_results.json`.

Effect: **no defect in the pinned mathematical exclusion**. The original certificate has 94 distinct values, all 4,371 pair witnesses check, and the actual implication is `N >= 259`. The weakness is that a future regression can lose the necessary strength without this checker failing. The checker describes itself as checking positive model bounds, so its successful exit alone must never be read as certification of the exclusion.

Smallest repair: require at least 89 for that exception when checking the theorem implication, or exactly 94 when enforcing the published numerical certificate. Add the demonstrated truncation as a negative control. No repair was applied here.

### 2. An exit code of zero can accompany incomplete parity coverage

References: `stage34_seven_sum_independent.py:67–89`; `stage32_even_independent.py:120–145`. They catch `TimeoutError`, save an incomplete status, and finish normally.

Fresh Stage34 reproduction returned zero after completing only 64–120 and timing out at 121. Fresh Stage32 returned zero after completing only half-orders 123–100 and timing out at 99. Neither exit proves the whole exclusion. These are operational defects if a caller treats zero as proof completion; their saved status labels correctly say incomplete.

Effect: the partial runs did not refute any theorem and were not promoted to complete. Separate audit copies checked only Stage34's 121–123 and Stage32's 99–94, keeping the original limits and all mathematical pruning/coverage logic. Complete per-order reports, not interrupted partial states, are combined. See `replay_stage34_remaining.py`, `replay_stage32_remaining.py`, their generated scope-limited copies, and logs.

Smallest repair: a theorem-reproduction wrapper must require complete per-order coverage and compare expected order sets, or the scripts must return a nonzero exit after timeout. No original script was changed.

### 3. The final manifest does not certify the earlier mathematical chain

References: `stage63_dependency_check.py:1–36`; `stage63_proof_manifest.json`, keys `files`, `prior_dependency_head`, and `earlier_chain`.

The manifest verifies 20 selected package files, archive parts, and saved outputs. It records an earlier parent but does not itself prove that parent's caps, allocation theorems, or parity exclusions. Its docstring explicitly limits it to integrity. A successful manifest check is not a full proof audit.

Effect: no theorem defect; this audit independently pinned the whole tree, traced the inherited statements, and ran the relevant earlier checks. Minimal improvement: maintain a machine-readable dependency ledger with exact hypotheses and verifier requirements for the inherited claims, rather than relying on a prose `earlier_chain`.

### 4. Two historical corrections must remain explicit

References: local historical `stage50_findings.md:174–183`, `stage50_split_proof_notes.md:23–34`; pinned `stage44_findings.md:160`, corrected by `stage48_findings.md:135–141`.

Stage50 withdrew reversed closure placements and an invalid root-mark inference. The corrected analysis uses the left tails minus right tails and the actual source edges `xf`, `zb`, not the cubic edge `xb`. The active Stage53/55 replacement checks these equations directly. Separately, Stage44's claim that quintic paths have no common tail was false: omitted edges 01,12,23 leave label 4 in all tails. Stage48 correctly removes that common label and recovers a quartic path.

Effect: neither withdrawn inference is needed downstream. Historical documents remain historical; their false sentences must not be used in isolation. Minimal improvement: attach explicit errata or current dependency links to old archived claims. The missing original Stage50 message/table prevents a cell-by-cell audit of the abandoned version, not of the replacement proof.

## 3. Dependency map and exact hypotheses

Let V mean eight physically distinct labels and full degree-eight validity. For the odd contradiction branch, O means cyclic group of odd order `N<248`. Symbols `Tj` count repeated VALUE outputs, not words. An ordinary degree-j word has one doubled center and j-2 distinct other labels.

|Claim|Hypotheses|Source and audit status|
|---|---|---|
|Every squarefree word is protected from every other same-degree word|V|Append its squarefree complement. Reconstructed directly; `stage41_findings.md:23–43`.|
|Unique ordered nonzero differences; 36 distinct unordered pair sums in odd order|V, oddness|Protected pair sum plus invertibility of 2. Reconstructed; `stage2_findings.md:188–203`, `stage41_findings.md:45–50`.|
|Elementary baseline N>=187|V, cyclicity|Exterior-sum packing gives 184, then excludes 184–186; `stage2_findings.md:145–230,235–298,302–422`. Rechecked deductions, including the signs of antipodal translate intersections and endpoint doubling arguments.|
|All even N<248 excluded|V, cyclicity|Antipodal reduction plus complete seven-point proof; parity 0+8,1+7,2+6,3+5,4+4. Stage30–35 proofs and independent checkers inspected/reproduced; see §4.|
|N>=56+T3+T5 and N>=71+2T4|V; oddness for the second bound|Complementary degree packing; absent midpoint adds one in odd order. Reconstructed; `stage41_findings.md:29–43`. Hence T4<=88.|
|T3=36+h+R3 and Ptotal=28-h|V, oddness|64 repeated cubic words, each center pair permits at most one collision. Summing m-binomial(m,2)+binomial(m-1,2)=1 over fibers. R3>=0; reconstructed.|
|Ordinary quartic cap three|V,O|Four private centers leave a cycle or pendant-triangle tail graph; cycle contradicts protected pairs, pendant is fourO. `stage41_findings.md:153–180`; six certificate files checked.|
|Total cubic cap three|V,O, quartic budget|Stage41 excludes ordinary-four and purehub; cyclic kernel allows at most two pure cubes. Stage42 excludes the only 2-pure/2-ordinary exception with 94 values. `stage41_findings.md:183–217`, `stage42_findings.md:198–215`; checked.|
|Ordinary quintic cap three|V,O, quartic/cubic packing|Four private centers force four disjoint doubling pairs. Complete Stage43 one/two-relation closure; `stage43_findings.md:15–168`; checked.|
|Shared-center rigidity, cross-degree bijections|V,O, caps and budget|Stage44 has complete 2,880 presentations and all 15 residuals; certificates checked. Path erratum replaced in Stage48.|
|General weighted inequality|V,O, preceding caps|Stage48 midpoint coverage and exact pair-lift/bijection ledger; `stage48_findings.md:33–145`. Re-derived in §5.|
|Four splits per ordinary cubic pair|V, oddness, split normal form|Coefficient of middle tail is 2, so fixed third center determines it uniquely. `stage54_split_count_hand_proof.md:7–24`; re-derived, no division by 3.|
|Every genuine split source is an E-output; E>=2q|V,O, caps, budget|Stage54 full source-path exclusion with forced total cubic collisions. `stage54_source_triple_proof.md:19–134`; checker reproduced. Forcing precedes E>=2q, so no circular allocation.|
|General injection q<=h|V,O, Stage54 source theorem|Stage55 replaces all 56 C4=0-only quartic-triple inferences from Stage53. Written auxiliary component argument rechecked; both checkers reproduced. `stage55_general_assignment_proof.md:33–68`.|
|t>=1|V,O, q<=h, U>=0|General weighted count with t=0 gives 2N>=496. This is the whole no-triangle branch, not just C4=0.|
|Triangle normalization and cycle-free nine forests|V,O, quintic cap|Stage56 hand cycle/quotient proof and four-edge matching cap. Rechecked; see §6. No Stage56 discovery status used.|
|q<=h-o, o counts distinct open paired edges|V,O, general injection|Stage58 excludes all 720 split-source presentations on one chosen paired edge. 190 models, 184 direct and six growth89; checker reproduced. `stage58_triangle_edge_ownership_proof.md:9–55`.|
|Pordinary>=9|V,O, Stage58 bound, Stage56 forest classification|Low-P forest incidence and distinct center-edge accounting, including pure closures; `stage58_triangle_edge_ownership_proof.md:59–133`. Reconstructed.|
|One split per triangle and external ordinary collision required|V,O, earlier caps/injection|Stage59 covers 12 local presentations and all 15 residual pairs, then all nine forests. Checker reproduced.|
|Every alignment class has at most four edges|V,O, previous claims|Stage60 complete six-family exclusion, with forced extra ordinary equality when P<=8. All reachable leaves checked; `stage60_large_forest_proof.md:15–109`.|
|At most one triangle-bearing class|V,O, Stage60 and P>=9|Stage61 3,360 second-triangle presentations, affine reuse and complete refinements. Checked; no interaction theorem used as its own premise.|
|Two-triangle class (3,2,2,1) excluded|V,O, Stage60/61, P>=9, Stage59 split theorem|Stage62 component `3221`, all 13,333 nodes checked. Only P9 forcing is used in this pinned component. Global credit and split guard audited below.|
|Final o>=2,t=1 and contradiction|V,O, above exclusions|Stage63 rival/terminal lemmas reconstructed and independently checked with every eligible disjoint-pair choice.|
|Attainment at 248|Eight displayed labels in Z/248|Coin proof reconstructed; all 6,435 words independently enumerated; dynamic programming independently confirms minima and uniqueness.|

Not essential: the general N>=207 numerical exclusions, Stage37 aperiodicity, the Stage45 unfinished 558 assignments, Stage50/51 compensation inventory, Stage52 center-graph refinement, unfinished Stage56/57 trees, and the Stage62 one-triangle discovery tree. No theorem is inferred from their incompleteness or zero-survivor reports.

## 4. Even-order coverage audit

Antipodal projection identifies only one pair. A rival downstairs lifts, and an extra available slot in the collapsed pair corrects the kernel error. A non-original projected word cannot lift to allones. Thus a valid eight-set with antipodes would imply a valid seven-set in order N/2.

For non-antipodal sets, heredity gives valid parity blocks. Translation interchanges parity. The all-one-parity branch would place 128 distinct subset sums in a group of order at most 123. The 1+7 branch uses the seven-point bound. The remaining splits are precisely 2+6,3+5,4+4 with half-order 94–123 after the elementary baseline.

I re-derived their quotient targets: with A=(2B+1) union 2C, |B|=b, the target is 2(sB+sC)+b. A mass-eight word with q odd terms requires quotient sum `sB+sC+(b-q)/2`. This produces the q=5/7 conditions in Stage31 and q=0/2/4/6/8 conditions in Stage32 with the recorded signs.

Coverage normalizes a unit difference to 0,1. If all differences are nonunit, all relevant gcd roots are retained; remaining points can be smaller than the selected root. For primitive sets at orders with at most two prime factors, the unit-difference reduction is valid: if a pair differs mod p, it must agree mod q; any point differing from them mod q would have to agree mod p with both, impossible. Therefore all points agree mod q, contradicting primitivity. Proper saturated blocks are separately excluded using quotient validity, not silently omitted.

Prefix validity checks every possible copy count of the new point. Full-prefix sumsets only prune when they already give the required all-block rival. Stage32's nonunit linear constraints retain every preimage under multiplication by 2 or 3; its independent checker generates all 34 opposing multiplicity vectors. No cancellation of 3 is assumed there.

Stage34's six-point necessary inventory retains exactly 58 sevenfold-saturation failures, rather than incorrectly asserting universal saturation. Its complete seventh-extension check verifies their explicit rivals. Stage35 enumerates quotient five-sets including antipodal sets, all 480 six-lifts, and 192 seven-lifts. Quotient units have odd unit lifts, and all fiber choices are included. Thus the final parity proof no longer relies on an external seven-point certificate.

Fresh reproduction results and split completion are in the logs and `parity_validation.json`. The two timeouts remain labelled incomplete; they are not used for interrupted orders.

## 5. Dedicated sign, orientation, and inequality audit

### Convention

For every word equation I use **left value minus right value**. For equalities `2x+a=2y+b`, the zero row is `2x+a-2y-b`; consequently `2(x-y)=b-a`. For a disjoint-tail source `2u+l1+l2=2v+r1+r2`, the source itself gives `2(u-v)=r1+r2-l1-l2`. A permitted closing DIFFERENCE has the other placement rule, `left_tail-right_tail`; these are distinct statements, not conflicting conventions.

To justify that rule, if `2(u-v)=f-g`, then `l1+l2+f=r1+r2+g`. Both sides must repeat or full protection contradicts them; thus f is a left tail and g a right tail. The corresponding cubic is `2u+g=2v+f`. `stage53_certificate_check.py:94–98` constructs precisely this row. Reversing the whole zero row is legitimate; changing only f/g while retaining centers reverses the placement and is invalid.

### Stage50 withdrawal and replacement

The local historical notes explicitly withdraw negatives of those permitted placements. They also correct `xb` to the actual other S4 sources `xf` and `zb`, and correct swapped parameter consequences. In the corrected CaseB form,

`(x,z,a,b,c,d,e,f)=(u,0,r,v+3u,u-v,r+2v+4u,r+2v-6u,v-3u)`.

Independent substitution gives `2(x-f)=8u-2v` and `2(z-b)=-2v-6u`. The four X placements give, in order, `3u=2v`, `r=-9u+v`, `r=15u-5v`, `v=9u`; the four Z placements give `r=-9u-5v`, `v=-8u`, `u=-2v`, `r=9u+v`. These are the corrected table, with only cancellation of 2. For example using the wrong sign in X2 changes `r=-9u+v` to `r=7u-3v`, showing why one cannot reuse a placement after changing orientation.

The active Stage53 proof reconstructs closure coverage from the canonical split. Stage55 intercepts every old C4=0-only exclusion rather than accepting the old theorem universally. Neither imports the local Stage50 files or its abandoned table. The bundled closed-split normal form is independently recoverable: set z=0, y=v, x=u+v, c=r; the cubic gives a=r+2u; closures give d=r+4u+2v, e=r+2v; the source gives b=r+4u+6v. This is the exact surjective model used for the 116-word certificate.

References for the replacement are `stage53_global_split_proof.md:17–64`, `stage53_certificate_check.py:94–111,158–199`, and `stage55_certificate_check.py:133–168,221–223`. The last file verifies that all 56 former restricted inferences have replacements. It is not silently reusing the historical C4=0 conclusion.

### Translation and final closure

If `2x-a=tau`, define x'=x-tau, a'=a-tau. Then `2x'-a'=2x-a-tau=0`, so `a'=2x'`. A degree-d word changes value by -d*tau; all equal-degree equations and the degree-eight validity condition are preserved. Translating by +tau would generally give `2x''-a''=2tau`, and is not the normalization used.

For b=2a, `2(a-b)=2a-4a=-2a=-b`. Thus closure `2(a-b)=x-y` is `x-y=-b`, or **y=x+b**. Conversely an outgoing edge b->2b supplies `x=b,y=2b`, and `b-2b=-b=2(a-b)`. Both directions have the same orientation; there is no lost minus sign.

### Certificate identity

The active growth check requires `f*(value(R)-sum(A))=k*(value(Wi)-value(Wj))`, with R nonnegative, mass eight, and R!=allones, and f a positive power of two. Free coordinates use literal integer equality; torsion coordinates use congruence with the same subtraction and multiplier signs (`stage60_certificate_check.py:95–103`, Stage61 lines 37–49, Stage62 lines 123–137). k is multiplied, never canceled. It need not be a unit. If a word pair coincides, f alone is inverted, forcing the rival. Flipping k alone was rejected by a fresh corruption control.

### Weighted ledger independently recalculated

The midpoint argument gives `36<=S5+n1+M+delta`. Exact ordinary pair lifts give `P5=(3/2)P4+(1/2)S4+S5`; quartic compression gives `P4>=80+C4`. Together with `P5=140-n1/2+3n3/2`, this yields

`n1/2+3n3/2+M+delta >=16+3C4/2+S4/2`.

Since `N=232+(h+R3)+(n1-n3)/2+M+delta`, independently substituting yields

`2N >=496+2(h+R3)-4n3+3C4+S4`.

The exact inverse maps give `n3=c+2t+p+q`, `C4=t+2c+p+w`, `S4=p+2w+E`. Therefore

`-4(c+2t+p+q)+3(t+2c+p+w)+(p+2w+E)=2c-5t+5w-4q+E`.

The path coefficient is zero, not negative or retained as a credit. With E=2q+U,

`2N >=496+2(h-q+R3+c)-5t+5w+U`.

Thus `h-q>=2,t=1` gives `2N>=496+4-5=495`, while `N<=247` gives `2N<=494`. The signs, constant 496, and negative triangle coefficient -5 are correct.

The other forcing inequalities were re-derived: from `N>=288+h+R3+2c+2w-2(t+q+P)` and `h=28-P-J`, `q<=h-o` gives `N>=260-P+J+R3+2c+2w-2t+2o`. Stage54's independent pre-allocation bound with Ptotal<=5 gives `N>=316-55-12=249`; it does not rely on the source theorem being proved.

## 6. Finishing lemmas and exhaustive shapes

For distinct x,y, the three disjoint doubling pairs meet at most two of {x,y}. Choose a completely disjoint pair b,2b. Remove x,y,b,2b and add z and three b's. Starting multiplicities are 1, and the four removed positions are distinct, so every resulting coordinate is nonnegative even if z equals a removed or retained label. The word still has eight terms. Its difference is `z+3b-(x+y+b+2b)=z-x-y`. It differs from allones: at most one of distinct x,y can be restored by z, and b is neither. This handles z=x,y,b,2b or any other label without a generic-position hypothesis.

The independent script checks all 360 identities obtained by using EVERY eligible disjoint doubling pair, rather than only the first selected pair in Stage63's 224 cases.

For a paired edge a->b, the closure equation is y=x+b. If x!=b, it is the forbidden sum of two distinct labels x,b. Hence the only closure is x=b,y=2b, exactly an outgoing doubling edge at b. This proof is about actual physical labels. Extra ordinary collisions, pure collisions, or fiber mergers cannot evade it. The open condition is terminality of the HEAD b; calling b the edge's “tail” in Stage63 is terminology, not a different oriented edge.

The cycle proof was checked separately because the final checker assumes it. A normalized directed cycle has order d dividing 2^r-1. For full-order cycles, binary expansion and cyclic coin splitting prove rB=H; the remaining projected labels have graded validity, not merely fixed-degree validity. Their subset cube has 2^(8-r) distinct points and misses its midpoint. The displayed proper-order rivals for r=4,6,8 have the correct mass and sum. For r=3, the graded-five quotient argument excludes orders 33 and 35, giving N>=7*37=259. Two-cycles cannot support a triangle because their zero-sum block plus two disjoint doubling pairs supplies the explicit mass-eight rival. Four disjoint aligned edges contradict the ordinary quintic cap. These arguments precede Stage60 and do not use its class bound.

Independently enumerating partitions of eight with path matching number three gives exactly the nine listed forests. Stage60 excludes the six large ones outright, Stage61 confines triangles to one class, and Stage62 excludes (3,2,2,1). The only survivors are (2,2,2,1,1), with one triangle and three terminal paired edges, and (4,2,1,1), with one triangle and two terminal paired edges. A new aligned edge either changes the class to one of the excluded shapes or violates the four-edge bound; it is not silently ignored. Distinct paired edges are counted once. Odd doubling plus private labels prevents identifying their endpoints. Thus actual t=1 and o>=2.

## 7. Computational coverage and assumptions audited

The checker node types are not self-justifying. Their mathematical premises were checked as follows:

* Label/protected/rival leaves contradict V directly. Four-word cubic/ordinary leaves invoke the independently audited caps, not C4=0.
* A genuine split source with a third ordinary quartic invokes Stage54 only after its source and genuine-split identities are reconstructed.
* Alignment-cycle leaves invoke the hand Stage56 argument; uniform five-edge leaves invoke the completed Stage60 theorem.
* Cyclic three-coset reasoning uses the cyclic kernel of multiplication by 3. It is not valid over arbitrary groups with larger 3-torsion, and this audit does not extend the cyclic theorem to them.
* Stage61 first closes its alternating component using Stage60 and P>=9, then permits reuse of that completed result. Physical affine reuse verifies an eight-label permutation, an actual triangle alignment, translation by its value, and the target constraints. Visited/active sets reject dependency cycles.
* Stage62's interaction leaves exhibit two triangle matchings with at least five distinct directed edges. If they had the same alignment, Stage60's four-edge cap would fail; if not, Stage61 excludes them. Thus the union-edge test is sufficient here.
* Stage62's five global-credit leaves use monotone R3, persistent ordinary cubic triple/quartic split fibers under the cap, and a maximum of two triangles or the fixed four-edge primary class. They do not assume model-open edges survive arbitrary new ordinary equalities.
* Its one split-guard leaf invokes the separate Stage62 single-class split lemma, derived from Stage59's complete residual classification and explicit rivals, not from the two-triangle exclusion being proved.

All 31 Stage62 refinement nodes use **P9**. None uses `robust_count`, `credit`, or `conditional_quintic`. Every positive leaf in the pinned component has degree four and 89 words. Consequently the more complicated conditional quintic and pure-credit methods in `stage62_open_credit_proof.md` are not needed for this component's closure. Their no-new-ordinary assumptions must remain conditional if used elsewhere; they have not been promoted here to arbitrary realization claims.

Why P<=8 forces an extra ordinary equality: if the 56 ordinary cubic words acquire no new equality, their pair partition and P remain unchanged regardless of pure-only mergers. The actual theorem P>=9 then contradicts that branch. A nonformal ordinary equality must use four different labels: equal centers/tails or a cross center/tail overlap gives a label collision or protected pair. Every such pair is included in private-pair coverage. Stage58's P>=9 argument counts pure closures by distinct center edges; it does not infer new ordinary pairs from pure collisions.

For a relation matrix K, the check verifies `L*K*V=D`, with determinants of L,V equal to +/-1. Writing coordinates x=V*y gives exactly D*y=0 over the group, not just over rationals. Powers of two in diagonal factors may be removed in odd order; every odd factor remains a torsion coordinate. The resulting universal free/torsion model maps onto every realization's parameter tuple. `forced` verifies that reused target constraints vanish in this exact quotient. A one-way implication is sufficient for unconditional target exclusion; conditional source reuse in Stage58 explicitly fixes the chosen pair and verifies both directions. Signs and pair permutations act on centers AND their doubles.

Coverage sets are built from words/ordered physical frames, and `seen==expected` is checked at every refinement. Whole-row sign/power-two normalization is safe. Growth proofs check every unordered pair of the selected words, including both free and torsion components. Witness reuse is harmless because it proves separation implications; it is not a claim of distinct rival words or fresh outputs.

Stage43's rank-one reasoning is also safe in the allowed residual directions: I,II,III have primitive integer coefficient rows and unit pivots. An integer difference rationally proportional to such a row is an integer multiple of it; there is no extra nonsaturated odd-torsion relation hidden in the rank-one step. Rank-two cases then use the checked unimodular reduction and retained odd factors. The conditional dimension assumption is removed by complete second-relation coverage, not applied to all realizations.

Stage60 closes 2,666 nodes; Stage61 checks 803 alternating and 2,857 required coupling nodes; Stage62 closes all 13,333 nodes in its component. Extra unvisited Stage61 stored nodes are not premises and do not correspond to missing required roots. The pinned Stage62 archive contains only the 3221 component; its `full_triangle_family_closed=false` status is correct. Stage63's elementary argument closes the other shapes.

The 10 Stage60 parts and 11 Stage61 parts were individually hash-checked and independently reassembled to their declared whole SHA256 values. The whole-archive reader and contiguous numbered-part fallback were inspected. Removing a required root coverage case, changing one relation coefficient, flipping a witness multiplier sign, admitting factor 3, corrupting a coordinate matrix, removing a pair identity, substituting allones as a rival, and changing word degree were rejected in separate in-memory/copy controls. These controls are samples of failure detection, not a completeness proof by themselves.

## 8. Sharpness checked independently

For ai=2^i-1 and sum mi=8, let S=sum mi*2^i. Original sum A is 247, so equality modulo 248 is S congruent to 255. Since 8<=S<=1024, the complete integer list is 255,503,751,999 (the representative 7 is below the minimum).

For denominations through 128, carry equal lower coins upward. Each carry reduces the number of coins; the final lower digits are 0/1 and the number of 128-coins is floor(S/128). Thus the minimum coin count is floor(S/128)+popcount(S mod128). The minima are:

|S|128-coins|Lower popcount|Minimum|
|---:|---:|---:|---:|
|255|1|7|8|
|503|3|6|9|
|751|5|6|11|
|999|7|5|12|

An eight-coin representation of 255 is already minimal, so no carry can occur; uniqueness of binary digits forces every denomination once. The other targets cannot have eight coins. Independently, dynamic programming counted representations and obtained exactly [1,0,0,0] eight-coin representations for those four targets. Direct multiset enumeration found only allones among all 6,435 degree-eight words modulo 248. See `independent_results.json`.

## 9. Reproduction and results

Use Python 3 with assertions enabled. In this environment the executable is:

`python`.

In PowerShell, substitute that full path for `$auditPython`:

```powershell
$auditPython = 'python'
& $auditPython -B audit_pr28/prepare_snapshot.py
& $auditPython -B audit_pr28/run_checkers.py
& $auditPython -B audit_pr28/run_checkers.py stage41_case_certificate_check stage42_certificate_check stage43_certificate_check stage44_certificate_check stage48_independent_check stage48_global_accounting_check stage53_certificate_check stage54_certificate_check stage55_certificate_check stage58_certificate_check stage59_certificate_check stage30_even_independent stage31_even_independent stage32_even_independent stage34_seven_sum_independent stage34_extension_independent stage35_antipodal_independent
& $auditPython -B audit_pr28/replay_stage34_remaining.py
& $auditPython -B audit_pr28/replay_stage32_remaining.py
& $auditPython -B audit_pr28/independent_checks.py
& $auditPython -B audit_pr28/coverage_corruption_checks.py
& $auditPython -B audit_pr28/stage42_threshold_control.py
& $auditPython -B audit_pr28/validate_parity.py
& $auditPython -B audit_pr28/verify_final_scope.py
```

The runner removes PYTHONOPTIMIZE from subprocess environments; no `-O` was used. `prepare_snapshot.py` copies only blobs matching the captured tree. `independent_checks.py` restores the two remotely retrieved pinned documentation files. Reproduction should use a fresh audit copy so previous generated result files cannot be mistaken for saved package evidence. Per-checker logs/status files are authoritative; the convenience `checker_runs.json` is overwritten by each batch, so use `audit_scope.json` for the aggregate.

|Check|Fresh result|
|---|---|
|Stage63 dependency|20 package files; three archive/result hash matches; passed before result regeneration|
|Stage63 finishing|224 original rival identities and stated forests/ledger; passed|
|Stage60|2,666 nodes; 4,904 direction cases; 1,723,040 separation identities; passed|
|Stage61|3,360 second triangles; 5,605 private directions; 1,570,316 separation identities; passed|
|Stage62|13,333 nodes; 21,761 directions; 25,851 literal pairs; 7,945,564 separation identities; passed|
|Stage41,42,43,44|All retained arithmetic/cap evidence checked; passed|
|Stage48|Midpoint, overlap, graph inverse identities and declared controls checked; mathematical ledger separately recalculated|
|Stage53|Complete old C4=0 coverage, direct row identities and 116-value closed-source proof; passed|
|Stage54|901 first directions; 4,339 second directions; 5,407,996 reconstructed pair identities and 3,860 direct identities; passed|
|Stage55|All 56 restricted inferences replaced; eight cubic-star replacements; 184,052 new pair identities; passed|
|Stage58|720 presentations; 190 model exclusions; 23,496 growth identities; passed|
|Stage59|12 local cases; 15 residual pairs; 3,916 growth identities and nine forests; passed|
|Stage30,31|Every half-order 94–123 complete with zero survivors|
|Stage32|Fresh complete per-order coverage assembled from original-limit run and restricted remaining-order replay; zero survivors|
|Stage34|Fresh complete per-order coverage assembled from original-limit run and restricted remaining-order replay; exactly 58 retained six-sets|
|Stage34 extension, Stage35|All saved seven-term rivals and antipodal lift coverage checked; passed|
|Independent finish/sharpness|360 disjoint-choice identities; exhaustive nine forests; all 6,435 mass-eight words; independent coin DP; passed|
|Negative controls|Eight invalid sign/word/unit/matrix/coverage changes rejected; weakened Stage42 threshold accepted and reported above|

These results support explicit identities and finite coverage. The mathematical conclusion additionally requires the protection, packing, inverse-map, unit, cyclic-kernel, auxiliary-component, and low-P arguments reconstructed above. Certificate counts alone do not certify those arguments.

## 10. What remains outside this audit

No essential reachable proof leaf is knowingly left unverified after the finite parity completion checks. Original withdrawn Stage50 intermediate messages/cells are unavailable at the pinned head; only their corrected local historical accounts and the active replacement were checked. Discovery producers were not rerun to prove their optimization/search claims. Unused exploratory node handlers, unfinished inventories, general N>=207 numerical history, novelty, and mathematical publication status are outside the verdict.

The smallest useful next action is to tighten the Stage42 theorem threshold and make parity completion mandatory in the reproduction wrapper, followed by another independent mathematical review of this dependency ledger. No change to the pinned proof, PR, public comment, merge, Lean development, or exploratory modulus sweep was made by this audit.
