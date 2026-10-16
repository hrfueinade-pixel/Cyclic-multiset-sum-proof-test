# Stage 44: simultaneous quintic triples with shared centers

2026-10-11. Continues Stage 43 / open PR #15 at
archived-source. Earlier PRs remain unmerged.
The complete N>=248 theorem is still OPEN and the goal remains ACTIVE.
No arbitrary new odd modulus has been excluded. The target is N>=248,
not N>248; the valid equality example at 248 remains intact.

This stage proves a new conditional shared-center rigidity theorem and
two exact cubic/quartic/quintic correspondences. These genuinely constrain
simultaneous collisions, but do not supply the required numerical tradeoff.
No modulus or parameter sweep, historical search restart, or increased
discovery timeout was used.

## 1. Notation and inherited restrictions

An ordinary degree-k word is 2c plus k-2 different other labels. Its doubled
center c is private within its fiber under full squarefree protection at
degree k-1: canceling one c would otherwise give a second representation
of the squarefree degree-(k-1) word consisting of its distinct labels.
This applies against EVERY other representation, not just ordinary ones.

Throughout the conclusions below, assume a hypothetical full-valid eight-set
in an odd group with N<248. Stages 41-43 give:

- Total cubic multiplicity at most three.
- Ordinary quartic multiplicity at most three.
- Ordinary quintic multiplicity at most three.
- |T4|<=88 and |T3|+|T5|<=191 from the exact packing bounds.

These hypotheses are not transferred to merely cubic-protected sets.

## 2. Shared-center rigidity theorem

**Theorem.** Fix three different doubled centers c1,c2,c3. At most two
quintic values can each have ordinary representations with ALL these
three centers. If two such values occur, their triples must be

    2ci + b + xj + xk,       and       2ci + a + xj + xk,
    {i,j,k}={1,2,3},

where the eight distinct labels are c1,c2,c3,a,b,x1,x2,x3.
Both triples are lifts of the same ordinary quartic triangle

    2ci+xj+xk = y,   i=1,2,3.

The two quintic values are y+b and y+a, and are different because a!=b.
In particular a triangle-, path-, or split-type quintic triple cannot
share its center triple with a different quintic value. Star-type triples
have exactly one partner, not an independently selectable second fiber.

### Complete finite reduction

By privacy, the tails of either quintic triple lie on the other five
labels B. Write a tail as B minus an edge P_i. Within one fiber the three
edges are different: equal tails would imply 2ci=2cj, hence ci=cj in odd
order. Three distinct edges on five vertices have four isomorphism types:
triangle, star, a length-three path, or a two-edge path plus a disjoint edge.
Normalize the FIRST triple to one of these four types, permitting the
corresponding permutation of its three centers.

Let Q_i be the omitted edges for a second fiber with those same centers,
aligned by center. Subtracting the two quintic equations gives

    sum Q_i - sum P_i = constant,  i=1,2,3.             (1)

There are only 10*9*8=720 ordered second-edge triples for each first type,
or 2880 symbolic configurations. These are edge assignments, not group
elements, moduli, or candidate cyclic sets. No assumption says the outputs
or the labels used by different configurations are disjoint.

For 2860 configurations, two cross-differences R1,R2 from (1) have an
explicit certificate

    2^j*(p-1_B) = u*R1+v*R2,                         (2)

where p is a non-original nonnegative five-term count word on B.
Appending one copy of each of c1,c2,c3 makes a mass-eight rival. Since
R1,R2 vanish, oddness cancels only 2^j. The witness is allowed to reuse
labels; its nonnegativity and mass are checked explicitly.

Four configurations are the identical second fiber. One is the formal star
lift, with first omitted edges (a,x_i) and second omitted edges (b,x_i).
Its equations are identically zero. Fifteen additional configurations
remain after the tail-only rival test: five for a path and ten for a split.
Thus the tempting claim that all non-lifts fail by tail-only protection
was FALSE as an inference from this test; an extra argument was necessary.

### Closing the fifteen residual configurations

Translate one B label to zero and write B=(0,2u,2v,2w,2t), valid because
doubling is invertible. The first quintic equations give

    ci=z+half the omitted edge sum.

The cross rows of (1), after canceling their common factor two, constrain
u,v,w,t. A signed power-of-two pivot parametrizes the first row
surjectively. If the second row is independent, an explicitly recorded
3-by-3 integer matrix U of determinant +/-1 reduces it to (g,0,0).
The odd part of g is retained as torsion; it is NOT divided out.
In these fifteen actual models that odd part is one. The checker verifies
this, rather than assuming absence of an odd-torsion branch.

The complete group models give two explicit eight-term rivals and thirteen
positive quartic certificates, with bounds

    95,95,113,95,95,95,95,121,116,121,121,114,121.

Each bound is at least 89 and contradicts |T4|<=88. The two direct rivals
contradict validity. This closes ALL configurations except the identical
fiber and the one formal star lift, proving the theorem.

No failed clique or timeout is a premise. These positive bounds come from
pairwise distinct selected outputs, each supported by an explicit rival
if they were equal. Discovery retained its fixed two-second cap per model.

## 3. Exact cross-degree correspondences, with proved inverses

Let C3 denote the number of cubic fibers having three ordinary words.
Let C4tri denote the number of quartic fibers having three ordinary words
whose three tail edges form a triangle on three labels.
Let C5tri,C5star count three-ordinary quintic fibers by omitted-edge type.
Under the inherited small-order caps,

    C5tri=C3 <= R3,       C5star=2*C4tri.               (3)

These are elementary bijections, not discovery-based counting guesses.

### Cubic triples to triangle quintics

The three cubic words have private centers c1,c2,c3 and different tails
x1,x2,x3, disjoint from the centers. They use six labels. Let a,b be the
other two labels. Add a+b to each word. The three resulting ordinary
quintics have tails {xi,a,b}; their omitted edges are the other two x's,
a triangle. The quintic cap says there are exactly three ordinary words.

Conversely the tails of a triangle-type quintic triple have intersection
{a,b}. Remove those two labels from each word. This recovers its cubic
fiber uniquely. Thus different cubic fibers cannot give the same quintic
fiber, even when they reuse a or b. This inverse is the injectivity proof.
A cubic fiber of three words contributes binomial(3-1,2)=1 to R3, so
C3<=R3; cubic triples containing a pure cube need not appear in C3.

### Quartic triangles to paired star quintics

An ordinary quartic triangle uses three private centers and three different
tail labels x1,x2,x3, leaving a,b. Adding a or b separately gives two star
quintic triples, at different values y+a and y+b. The cap again ensures
exactly three ordinary words at each output.

Conversely the ordinary tails in a star quintic triple have a ONE-label
intersection, precisely its added label. Removing it recovers the quartic
triangle fiber and its three words uniquely. Two different quartic cores
therefore cannot share a star quintic output. The remaining unused label
is forced by the eight-set and supplies its partner. This proves both the
factor two and disjointness of output pairs; no fresh-label assumption is
used. The shared-center theorem further rules out every additional quintic
value on those same centers.

Path and split quintic triples have no common tail label, so neither is
one of these lifts. Each can occur at at most one quintic value on its
fixed triple of doubled centers. Different center triples are NOT proved
independent, and may share labels or have other coupled equalities.

## 4. Verification and challenges

stage44_certificates.json.gz packs the complete edge inventory, models and
all fifteen residual certificates. The standalone checker imports no
inventory, parametrization, clique, or earlier discovery modules. It
independently reconstructs all first-graph orbits, all 2880 assignments,
all cross rows, and the exact coverage models bound to each certificate.

It verifies all 2860 multiplied tail rivals, both direct eight-term rivals,
and all 75269 growth-pair witnesses. Every count vector's degree and
non-original status, unit factor, integer equation, torsion congruence,
pivot, gcd, unimodular determinant, and complete model binding is checked.
Wrong mass, an original word, and a factor-three cancellation are rejected
by corruption controls. Only powers of two are canceled in this stage.

Two declared large odd controls were checked against all 6435 eight-term
multisets each. They have respectively one quartic triangle/two star
quintics and one cubic triple/one triangle quintic, and the inverse maps
and shared-center condition pass. Their common modulus is 670481; the
sets and full results are saved. These controls verify the stated maps,
not the conditional exclusion of arbitrary sub-248 sets. No numerical
minimum, absence search, or transfer to weaker protected sets is inferred.

The separate checker is a same-author independent implementation, not an
independent human review or a formal proof-assistant verification. No
novelty claim is made.

Independent deductive challenges were applied before accepting the result:
the second edges are ordered by the original centers; first normalizations
move centers with their edge assignments; both fibers' privacy is needed;
the first parametrization is invertible in every odd group; the second
transformation is unimodular over the group; the original rival word is
excluded explicitly; and output uniqueness in (3) follows from recoverable
tail intersections, not from a generic-distinctness assumption.

## 5. Exact remaining gap

The first structural attempt, tail-only shared-center rigidity, left fifteen
cases. Joint full-set rivals and quartic growth close them. The second
attempt is to use the resulting cross-degree bijections to finish the
GLOBAL quintic lower bound. That step still fails, for a concrete reason.

There are 736 repeated quintic words. Ordinary words account for 280.
The other 456 have shapes 5,41,32,311,221, respectively with counts

    8,56,56,168,168.

The bijections control which three-ordinary fibers are inherited from lower
degrees. They do not bound how those 456 mixed words share outputs with
ordinary words, with each other, or across different center triples.
There is no proved injective charge, fresh-output contribution, or bound
on their total compression. Even the ordinary cap alone gives only
ceil(280/3)=94 outputs, far short of the needed quintic growth.

The sharply stated remaining lemma is still:

> For a full-valid eight-set in odd 207<=N<248 with |T4|<=88, the proved
> cubic/quartic/quintic caps and shared-center rigidity imply
> |T5|>=156-h-R3, or an explicit eight-term rival exists.

This is an UNPROVED target. The new correspondences constrain some
overlaps without resolving mixed-word compression. The next targeted
structural question is coupling path/split quintic triples with DIFFERENT
center triples, or coupling their mixed-word representations to necessary
quartic compression. Same-center triples are now completely handled.
No remaining family is declared realizable merely because it survived
discovery, and no arbitrary odd order 207..247 is promoted to excluded.

## 6. Reproduction and delivery

Check the shipped positive evidence without discovery:

```text
python -B stage44_certificate_check.py
```

Regenerate the fixed inventory and its positive residual certificates:

```text
python -B stage44_same_centers.py
python -B stage44_shared_growth.py
python -B stage44_pack_certificates.py
python -B stage44_certificate_check.py
```

The discovery code uses the Stage 43 generic positive-certificate engine
and its Bezout helper, both already present on the base PR. It imports no
historical search entry point. Individually generated residual files have
the inherited stage43_s44_* prefix; the shipped Stage 44 bundle contains
them all, so the independent checker does not need loose certificate files.

This report and supporting code continue the existing stack on a new PR
based on Stage 43 / PR #15. No earlier PR is merged. The full N>=248 goal
remains active and incomplete.
