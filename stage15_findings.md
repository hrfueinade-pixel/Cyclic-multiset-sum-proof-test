# Stage 15: an elementary order-seven block exclusion

Date: 2026-10-10. One focused continuation from the Stage 14 checkpoint.
The previous round made progress: all multiway cubic cones now have
connected entire quartic fibers, with its computational dependencies.
This round investigates the remaining local defects. No new numerical
computation, Lean, sampling, modulus sweep, or historical rerun was used.
No novelty claim is made. The full D=0 and original 248 targets remain open.

## 1. Complete elementary order-seven exclusion

**Proposition.** A valid eight-point set in an odd cyclic difference-
generated subgroup H with h=0 cannot contain

    C={x,x+d,x-2d}, where d has order seven.

This result has NO dependency on MC, Stage 9's order-three exclusion,
Stage 10's four-way exclusion, or any finite computation. Its proof uses
validity, oddness, cyclicity, and doubling closure of the actual differences.

### 1.1 Normalize, saturate the subgroup, and lift short replacements

Translate x to 0. Put J=<d>, C={0,d,-2d}, and A=C union B with |B|=5.
Validity forbids any different equal-length representation of a squarefree
sum of at most eight points: add its complementary points. In particular
all pair sums are unique. At odd order this also gives uniqueness of all
56 nonzero ordered differences.

The six ordered differences of C exhaust J\{0}. No other ordered pair
of A can have its difference in J. Therefore the five points of B lie
in DISTINCT NONZERO cosets of J. Write Q=H/J, and beta_i for their
distinct nonzero projections. Q is odd and cyclic.

Three-term multisets from C realize EVERY element of J. In units of d,
C={0,1,5} modulo 7; representatives for residues 0,1,2,3,4,5,6 are

    0+0+0, 0+0+1, 0+1+1, 1+1+1, 1+5+5, 0+0+5, 0+1+5.

Consequently any number k>=3 of terms from C realizes all of J, by
padding these representations with k-3 zeros.

Two consequences will be used:

1. The projected five-point set beta(B) is VALID for five-term sums.
   A different five-term projected multiset with sum sum(beta(B))
   lifts to five terms from B; its discrepancy from the target sum(A)
   lies in J and can be corrected by exactly three C terms. This is a
   rival eight-term multiset, since the B counts differ.
2. No squarefree subset of beta(B) with k terms can equal a DIFFERENT
   multiset of l<=k terms from beta(B). The empty multiset l=0 is allowed.
   Remove the corresponding k distinct B points from the all-ones vector,
   insert the l B points, and use exactly 3+k-l C terms to correct the
   J discrepancy. These C terms exist by the preceding surjectivity.
   The resulting eight-term multiset differs on B and contradicts validity.

Identical multisets at equal length are not prohibited. This quantifier
is essential. The lifting statement does not assert arbitrary longer
replacements, since those could leave fewer than three C slots.

The second consequence excludes beta_i=-beta_j: for distinct i,j the
squarefree pair would equal zero, and the case i=j is excluded by oddness
and beta_i!=0. Thus Bbar={beta_i} and -Bbar are disjoint five-element sets.
The first consequence and oddness give 20 distinct nonzero ordered
differences Delta_B of Bbar, by the usual squarefree-pair argument.

### 1.2 Projected difference multiplicities

Let w(q) count the ACTUAL nonzero differences of A whose image in Q is q.
The preceding uniqueness and coset separation give exactly:

    w(0)=6;
    w(q)=3+epsilon(q) if q in Bbar union (-Bbar);
    w(q)=1 if q in Delta_B outside that signed set;
    w(q)=0 otherwise,

where epsilon(q) is 1 or 0 according as q is in Delta_B or not.
There are three cross differences for each signed B coset, plus at most
one B-B difference because Delta_B is unique. No two signed B cosets
coincide. This accounts for all 6+30+20=56 ordered differences.

We need the precise overlap characterization at a positive beta_i:

    beta_i in Delta_B  iff  2 beta_i in Bbar.                 (1)

Indeed beta_i=beta_p-beta_q would give beta_i+beta_q=beta_p.
If q!=i this is a squarefree two-term subset replaced by one term,
forbidden by the short-replacement consequence. If q=i, it is exactly
2 beta_i=beta_p. Conversely that doubling relation supplies the difference.
The possible p=i would force beta_i=0 and cannot occur.

Since h=0, doubling permutes the 56 actual differences. It induces a
bijection from the fiber over q to the fiber over 2q, so

    w(2q)=w(q).

The signed B cosets are precisely the cosets with weight 3 or 4.
Thus doubling permutes Bbar union (-Bbar). Each positive beta_i doubles
either to a positive beta_j or to a negative -beta_j.

### 1.3 Negative transitions are impossible

Suppose 2 beta_i=-beta_j. Signed disjointness says 2 beta_i is not in
Bbar, so (1) gives epsilon(beta_i)=0 and w(beta_i)=3. Weight invariance
also gives w(-beta_j)=3. Their actual difference fibers contain only
the three C-B cross differences. Write b_i,b_j for the original lifts.
Doubling closure therefore gives the equality of three-element sets in H:

    2b_i-2C = C-b_j,
    -2C = C-(2b_i+b_j).                                    (2)

Here 2b_i+b_j lies in J. Directly, for C={0,d,-2d} in J of order seven,

    2C=C+2d.

Equation (2) consequently says -C is a translate of C, i.e. C is invariant
under a reflection y -> L-y. On an odd group such a reflection has a
unique possible fixed point. Its involution on the three-point set C must
fix one point and exchange the other two. Those two distinct points
then sum to twice the fixed point, contradicting pair-sum uniqueness.
Thus no negative transition exists.

It follows that 2Bbar=Bbar as sets. Summing their five elements gives
2 sum(Bbar)=sum(Bbar), hence sum(Bbar)=0. This is a nonempty squarefree
five-term subset replaced by the empty multiset, forbidden by Section 1.1.
Contradiction. This proves the proposition completely elementarily.

The independent challenger audited the lifting, overlap characterization,
weight counts, negative-transition argument, and final contradiction.
Its delivered audit is recorded in stage15_challenger_findings.md, a
ROOT-WRITTEN reconstruction after the agent hit a usage limit before
saving its own file. No numerical
execution or assertion based on passing examples is hidden in this proof.

## 2. No small 31-only component in a fresh quartic fiber

**Corollary.** Under validity, odd h=0, Stage 9's absence of order-three
differences, and MC (all multiway cubic cones connected), a fresh quartic
fiber has no component consisting only of 31 vertices and using at most
five support points.

Every pure cubic is paired by the general singleton-base spanning-tree
lemma. In a fresh fiber, MC makes that partner unique: otherwise the
vertex cones a multiway cubic. For a 31 vertex 3a+b, its pure-cubic
partner coned by b must be another 31 if the component is 31-only.
It must have doubled center b, giving

    3a=2b+c, next vertex 3b+c, c=3a-2b.

A pure partner 3p is excluded by Stage 9; an ordinary or 22 cone is
excluded by the component type. A 31 with the same center is identical.
Other propagation edges are reverses of this successor: deleting a
leaves 2a+b, and a new 31 cone can only come from a pure cubic partner.
Stage 9 also excludes distinct 31s with one singleton, so predecessors
are unique. A finite component with one successor and at most one
predecessor per vertex is a directed cycle. Distinct vertices have
distinct centers, and each singleton is the next center; support size
equals cycle length k.

Normalize the first two centers to 0,d. The successive centers are

    0, d, -2d, 7d, -20d, 61d, ... .

Length one is impossible. Length two forces 2d=0, contrary to oddness
and distinctness. Length three forces order(d)=7 and the block excluded
in Section 1. Length four forces 20d=0, so order(d)=5 at odd order;
four distinct points in that coset would have 12 ordered differences
in a subgroup with only four nonzero elements, impossible. Length five
forces order(d)=61. The order of 2 modulo 61 is 60: 2^30=-1, 2^20=47,
and 2^12=9 modulo 61 rule out the maximal proper divisors 30,20,12.
Doubling closure would then put all 60 nonzero multiples in Delta,
whose size is only 56. This is impossible as well.

All k<=5 are excluded. The cycle/type argument was independently checked
by the alternative-route researcher. MC retains Stage 13/14 computational
dependencies, but the new order-seven exclusion itself does not.

In particular an isolated ordinary vertex (support three) cannot be
opposite a 31-only component: that component would have at most five
support points. This removes a concrete center-defect branch.

## 3. Sharper singleton and forced-center restrictions

The alternative-route researcher proves, with complete proofs in
stage15_alternative_findings.md:

* Every singleton defect in a fresh fiber is an EXACT two-vertex component:
  either two ordinary vertices, or a 31 and an ordinary. It is not an
  arbitrary pair of unpaired deletions elsewhere in a path. The common
  singleton is the point whose deletion gives their sole propagation edge.
* A multiway fiber having that SAME singleton cannot cone back to X.
  The shared-edge cubic at X is already a pair; any such cone would
  identify its center with one of the two unpaired defect marks.
* A two-ordinary component cannot be opposite a three-point pure/ordinary
  component. Sixteen algebraic tail cases give complete squarefree/pair
  contradictions without global unpaired-label injectivity.
* Such a two-ordinary component's remaining opposite possibilities are
  isolated 22, a 22/31 pair, or isolated ordinary. The formerly possible
  order-seven 31 triangle is now excluded by Section 1.

### 3.1 Further elementary exclusion of the 22/31 opponent

The following proof was obtained by root while continuing after the
alternative note was finished. It closes one of that note's three
remaining shapes without a computation or a global unpaired permutation.

Suppose a two-ordinary endpoint component opposes a 22/31 pair at X.
Write the opposite pair as

    X=3t+r=2r+2s, with 3t=r+2s.

The common singleton of the 31 must be one of the two doubled points
of the 22; otherwise the two multisets would have no shared point and
would not form this component. The three core points are distinct.
Translate t=0. Then r=-2s and X=r. Write the ordinary endpoints as

    r=2a+b+p=2c+b+q,
    p=r-2a-b, q=r-2c-b.

Their support has five distinct points a,c,b,p,q and is disjoint from
the opposite support {0,r,s}. All eight points are therefore distinct.

Use h=0 to write 2a=e-f. The ordinary/31 equality gives

    e+b+p=0+r+f.

If either side were squarefree, validity would require literal multiset
identity; that is impossible because the two left tails b,p and the
two right core points 0,r cannot both be supplied by the one extra
point on the other side. Thus both sides repeat: e is b or p, and f
is 0 or r. If f=0, then 2a=0+e is a forbidden squarefree-pair replacement.
Hence f=r. Substitution of e=b or e=p leaves exactly

    A1: 2a=b-r=b+2s;
    A2: 4a=-b.

For c, the same argument leaves C1:2c=b+2s or C2:4c=-b.
These are all choices; no partner uniqueness or omitted role is assumed.

The four cases give:

| | C1 | C2 |
| --- | --- | --- |
| A1 | a=c | a+q+s=0 |
| A2 | c+p+s=0 | a=c |

The diagonal entries use invertible doubling (or quadrupling) in odd H.
For A1,C2, write b=-4c and a=s-2c. Then q=r-2c-b=2c-2s,
so a+q+s=0. The reversed mixed case gives c+p+s=0 identically.
Each mixed triple has three distinct points (two ordinary-component
points and the opposite point s) and equals three copies of 0.
This is a forbidden squarefree replacement. All cases contradict validity.

Thus two-ordinary endpoint components cannot oppose 22/31 components.
This is a complete elementary proof, not an inference from a finite
test. The earlier alternative note's three-shape list is now reduced
to TWO: isolated 22 or isolated ordinary. The 31/ordinary endpoint
defect remains separate and unresolved.

The independent challenger proves stronger center-role restrictions:
if isolated X=2u+v+w forces a multiway cubic with a mark 2u+q, at most
ONE of that cubic's OTHER centers can occur doubled in any opposing
quartic vertex at X, across ALL quartic types. In particular q=u
precludes opposite ordinary or 31 centers from that cubic. The three
coverage cases must remain distinct: no-pure cubic; one-pure with pure
center u; one-pure with pure center different from u. Its full role
proofs and a valid non-h0 diagnostic are in stage15_challenger_findings.md.
These restrictions are not complete exclusions of the remaining defects.

## 4. Dependencies, limitations, and next checkpoint

| Statement | Status |
| --- | --- |
| No order-seven block {x,x+d,x-2d} | NEW complete elementary proof above; no MC or computation dependency |
| No fresh 31-only component with support <=5 | Elementary conditional on Stage 9 and MC, whose Stage 13/14 computation dependency is retained |
| Singleton defect is an exact two-vertex endpoint component | Elementary conditional on MC/Stage 9; complete alternative proof |
| Same-singleton defect transport impossible | Elementary conditional on MC; complete alternative proof |
| Two-ordinary vs pure/ordinary component excluded | Complete elementary 16-case proof; not inferred from tests |
| Two-ordinary vs 22/31 component excluded | NEW complete elementary four-case proof in Section 3.1 |
| Forced-center role limits | Complete elementary challenger proofs; not a full defect exclusion |
| Valid non-h0 diagnostic | Elementary; NOT a valid h=0 counterexample |
| Defect exclusion / different-center and different-singleton transport | OPEN |
| h=0=>D=0 | OPEN |
| Original E4-size >=60 / 248 bound | OPEN; regular Sigma>=53 and h>0 also remain |

No new experiment was run in this round. The residue/power checks in the
proof are explicit elementary identities, not a numerical search. The
historical MC computations were read as dependencies and NOT rerun.
No claim of literature novelty is made.

**Next useful targeted lemma:** exclude a fresh TWO-ORDINARY endpoint
component opposite an isolated 22. The 22/31 branch is now excluded
by Section 3.1. The other remaining opponent, isolated ordinary,
additionally has a center defect and requires its own argument.
The 31/ordinary endpoint defect also remains unresolved;
do not silently fold it into the two-ordinary case.

The full transport proposal remains unproved; the forced fiber at the
SAME center or SAME singleton cannot itself supply the desired bridge.
No sufficiently general different-role transport argument was obtained.

One focused round is complete, with no live computation. Save local
working notes and continue from these exact branches, not the completed
one-pure cone checks. Per the latest user request, GitHub checkpoints
are reserved for necessary saves; NO new branch or PR is created in this
round. Existing research PRs are not merged or modified.
