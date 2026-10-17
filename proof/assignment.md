# Sources and the global split assignment

Throughout, A is a valid eight-set in an odd cyclic group of order N<248.
Dependencies are Lemmas 1–2, 5–6: protection, packing, multiplicity caps, and [the
weighted inequality](counting.md). Lemmas 7–8 are computer-assisted; their global
counting and graph steps are elementary. The archived cap-two coverage is an input
inventory, never a general multiplicity assumption.

## Canonical splits and the exact closure rule

A split has the form

$$
2x+c+d+e = 2y+a+d+e = 2z+a+b+c,
$$

where all eight displayed labels are distinct. Its cubic relation is

$$
2x+c = 2y+a.
$$

Its two disjoint-tail quartic sources are

$$
2x+d+e=2z+a+b,\qquad 2y+d+e=2z+b+c.
$$

Deleting the unique common tail recovers each source word pair. Their injection into
distinct E outputs is proved after the source-fiber theorem; it is not inferred from
the two displayed word pairs alone.

For a source 2u+l1+l2=2v+r1+r2 with disjoint tails, suppose 2(u-v)=f-g belongs to
Delta. Then

$$
l_1+l_2+f = r_1+r_2+g.
$$

The two count vectors differ. Full protection requires both sides to repeat, so f is
one of the left tails and g one of the right tails. Thus the four possible closures
are exact, with their sign fixed:

$$
2(u-v)=\ell-r.
$$

This rule introduces no missing ambient labels or extra closure assumption.

## Every split has an open source edge under the quartic budget

If both source-center edges are closed, compare the two closures with 2(x-y)=a-c. Of
sixteen tail placements, twelve give a protected cubic collision, two give 2a=2c,
and only two d/e-mirror placements survive:

$$
2(x-z)=d-a,  2(y-z)=e-c.
$$

Translate z=0 and set u=x-y, v=y, r=c. The equations force, without dividing by an
odd integer,

$$
(x,y,z,a,b,c,d,e) =(u+v,v,0,r+2u,r+4u+6v,r,r+4u+2v,r+2v).
$$

The closed-source lemma certificate separates 116 repeated quartic words for every
full-valid odd realization of this complete model. Every selected pair has an
explicit identity

$$
2^j (\operatorname{val}(\mathrm{rival})-s) = m (\operatorname{val}(\mathrm{left})-\operatorname{val}(\mathrm{right})),
$$

where the rival is nonnegative, has mass eight, and differs from all-ones. Equality
of the two quartic values would therefore contradict full validity. The 6,670
identities cover every pair of the 116 words and give T4>=116, contrary to T4<=88.

This certificate is included in the base assignment lemma bundle, rather than
relying on an unpublished report. Its sixteen closure placements, words and all
6,670 pair identities are checked by the new standalone verifier. Thus every split
has at least one open source-center edge.

## Lemma 7. Split-source fibers and the E budget

**Conclusion:** every genuine quintic split has two recoverable, distinct quartic
source outputs, each with exactly two ordinary representations. No source serves two
splits. Thus E>=2q, including the general cap-three case.

### Four splits per cubic pair

Fix an ordinary cubic word pair

$$
2x+c = 2y+a,
$$

where all four labels are distinct. A genuine quintic split descending to this pair
has the form

$$
2x+c+d+e = 2y+a+d+e = 2z+a+b+c,
$$

where z,b,d,e are precisely the other four physical labels. Let their sum be R.
Since d+e=R-z-b, the second source relation gives

$$
2x+R-z-b=2z+a+b
\quad\Longleftrightarrow\quad
3z+2b=2x+R-a.
$$

For each possible third center z, the last equality determines at most one b,
because multiplication by two is injective in an odd group. Then the unordered pair
d,e is recovered as the other two labels. The split output and its word fiber are
therefore recovered uniquely. There are four possible choices of z, so the fixed
ordinary cubic pair supports at most four genuine split outputs.

Every genuine split has exactly one word pair whose two common tail labels can be
deleted to give an ordinary cubic pair. Hence globally

$$
q \le  4 P_3^{\mathrm{ord}}.
$$

No division by three is used. The result allows reused labels and outputs between
different cubic pairs; the unique descent prevents counting a split twice.

### A global consequence that forces further cubic relations

For quartic triangles, the elementary recoverable lift count gives 3t<=4P3 ordinary:
each triangle has three cubic pair descents, and each fixed cubic pair has four
possible one-label quartic lifts.

In the inherited small-order setting, the number O4 of ordinary quartic values is
168-P4+C4 <=88. Thus

$$
\begin{aligned}
P_4&\ge80+C_4,&\qquad S_4&=P_4-4P_3^{\mathrm{ord}},\\
C_4&=t+2c+p+w,& S_4&=p+2w+E.
\end{aligned}
$$

Therefore

$$
E \ge 80+t+2c-w-4P_3^{\mathrm{ord}}.
$$

Substitute this into the weighted count bound

$$
2N \ge 496+2k+2c-5t+5w-4q+E
$$

to obtain

$$
N \ge 288+k+2c+2w-2(t+q+P_3^{\mathrm{ord}}).\tag{COUNT}
$$

Let Ptotal be the number of unordered equal pairs among all 64 repeated cubic marks,
including pure cubes. Ordered-difference uniqueness gives Ptotal=28-h. The exact
cubic formula gives k=h+R3=28-Ptotal+R3, and P3 ordinary<=Ptotal.

If Ptotal<=5, the two incidence bounds and COUNT imply

$$
N \ge 316-11P_{\mathrm{tot}}-2 \lfloor 4P_{\mathrm{tot}}/3\rfloor+R_3 \ge 316-55-12=249.
$$

This contradicts odd N<248. Hence every remaining counterexample needs at least SIX
cubic collision pairs.

The exact source-path model from the source-path parameterization below has sixty
formal repeated cubic values: four pair collisions and no multiway fiber. Without
any new cubic equality, Ptotal=4, so COUNT already excludes it. Each of the six
first-cubic residual models has 59 formal repeated cubic values, with exactly five
pair collisions and no multiway fiber. Unless a further formally new cubic equality
occurs, Ptotal=5 and COUNT excludes that model as well.

This supplies the mathematical premise for the complete second-cubic inventory. It
does not declare an incomplete inventory, weak growth bound or timeout an exclusion.
The general assignment below supplies the remaining allocation premise.

Under full eight-term validity, odd N<248, and the established ordinary
cubic/quartic/quintic caps, each quartic word-pair source of a genuine quintic split
lies at a value with exactly two ordinary quartic representations. Mixed
representations at that value are allowed.

Consequently, with E counting two-ordinary disjoint-tail quartic fibers and q
genuine quintic split outputs,

$$
E \ge  2q
$$

holds in the general branch. The distinction between source pairs and E outputs is
essential: an E fiber must have exactly two ordinary words.

The proof has two elementary reductions and complete computer-assisted exclusions
for one specific remaining source-path family. No group elements, parameters or
moduli are enumerated. Only powers of two are canceled, including in all finite
growth certificates.

### A third quartic center must be the added label

Normalize a genuine split as

$$
2x+c+d+e = 2y+a+d+e = 2z+a+b+c.
$$

Focus on its source

$$
Q=2x+d+e=2z+a+b.
$$

The two unused source labels are c and y. Ordinary centers are private, so a third
ordinary quartic word at Q must have center c or y.

Suppose its center is y and its two tails are u,v. Then Q=2y+u+v, while the cubic
descent is 2x+c=2y+a. Subtracting gives

$$
a+d+e = c+u+v.
$$

The left side is squarefree and its labels do not contain c. The right side contains
c and is a different word of the same degree, regardless of whether u or v equals c.
Full cubic protection forbids it. Thus center y is impossible.

The only possible third word is therefore

$$
Q=2c+u+v,
$$

where u,v are two different labels among y,a,b,d,e. There are exactly ten
possibilities. The other source of the split is symmetric by exchanging x,y and a,c.

### The ten added-center possibilities

The retained proof archive handles every pair u,v. Six give direct protected
collisions or label equalities:

| Tails | Positive consequence |
| --- | --- |
| y,a | y+d+e=3c |
| y,b | y+a+d+e=3c+b |
| y,d | y+a+e=3c |
| y,e | y+a+d=3c |
| a,b | 2z=2c |
| d,e | 2x=2c |

All squarefree words displayed differ from their rivals. The factor two is a unit in
odd order.

The b,d case has a positive certificate separating 89 repeated quartic values in its
complete dyadic parameter model, contradicting T4<=88. The b,e case is its d/e
mirror. The checker reconstructs a positive mass-eight separation identity for every
pair of the 89 selected quartic words.

The only remaining shape is u,v=a,d or its a,e mirror. Its quartic source triple is

$$
2x+d+e=2z+a+b=2c+a+d.
$$

The tail edges de,ab,ad form a quartic path. This source-path family is excluded by
the first- and second-relation coverage below. The proof does not assume a local
fiber cap, fresh mixed output, or distinct source credit to remove it.

### Why additional cubic relations are forced

The preceding elementary count proves

$$
q\le 4P_3^{\mathrm{ord}},     3t\le 4P_3^{\mathrm{ord}},
$$

and combines them with the inherited exact lift identities and the weighted count
bound to show:

> Every putative odd N<248 counterexample has at least SIX unordered equal pairs
among its 64 repeated cubic marks.

This deduction precedes and does not use the theorem E>=2q being proved here. In
particular, it does not rely on q<=h or C4=0. There is no circular source allocation
premise.

The complete source-path model consists of three original relations: the split's
cubic descent, its first quartic source equality, and the equality of that source
with 2c+a+d. A dyadic unit-pivot parametrization is surjective over any odd group.
It has 60 formal repeated cubic values: 56 singleton classes and four double
classes. Thus a realization with no further equality would have only four cubic
collision pairs, already impossible by the preceding global count.

There MUST be an equality between two formally different cubic classes. This is an
actual necessary relation; generic integer examples or absence in a search are not
premises.

### Complete first-cubic coverage, with odd torsion retained

The 64 repeated cubic words have 2,012 pairs with different formal coefficient
values in this model. Normalize a coefficient difference only by sign and powers of
two, obtaining 901 distinct directions. Odd common factors are deliberately
retained.

For each direction, an integer unimodular column transformation U gives

$$
\mathrm{direction} \cdot  U = (g,0,0,0).
$$

The first new parameter satisfies g*delta=0. Remove only the power of two in g,
leaving its odd part as explicit torsion. The full label model is obtained by
multiplying the original coefficient matrix by U; the remaining parameters are free.
This describes every odd-group solution, not merely a rational or torsion-free
embedding.

The first inventory has:

- 568 positive direct exclusions: label/protected collisions, eight-term rivals, or four ordinary quartic/quintic words violating the inherited cap three;
- 327 complete models with positive 89-value quartic growth certificates;
- six remaining necessary models, indices 389,740,764,794,800,805.

The six residuals have no torsion coordinate. Each has 59 formal repeated cubic
values, consisting of 54 singleton and five double classes. With no further equality
it would have only five cubic collision pairs, again contradicted by the SAME
elementary global count. Therefore a second formally new cubic equality is
compulsory in each residual.

Weak positive bounds for these six models are not treated as exclusions. The second
equality is forced deductively, rather than by raising a clique-search timeout.

### Complete second-cubic coverage closes the source-path family

Within each residual, normalize every formally new cubic equality by sign and powers
of two, and apply the same unimodular reduction. The complete inventories are:

| First residual | Second directions | Result |
| --- | ---: | --- |
| 389 | 734 | All positively excluded |
| 740 | 687 | All positively excluded |
| 764 | 739 | All positively excluded |
| 794 | 746 | All positively excluded |
| 800 | 717 | All positively excluded |
| 805 | 716 | All positively excluded |
| Total | 4,339 | Complete coverage |

Of these, 3,286 have direct integer exclusions; 1,053 have positive 89-value quartic
growth proofs. Odd torsion orders 3,5,7,9 are kept in these models. Every
first/second model is bound to its exact representative cubic equality and complete
direction inventory.

The standalone verifier imports no discovery or elimination code. It checks the base
unit minor, free-label coordinate recovery, unimodular determinants, retained
gcd/torsion constraints, every coverage direction, and every direct integer
identity. For each retained set of 89 quartic words it independently constructs an
explicit nonnegative mass-eight rival identity for every selected pair, using the
finite list of all 6,435 mass-eight words.

This reconstructs 5,407,996 positive quartic separation identities across the source
b,d model and the first/second inventories, plus 3,860 direct integer identities. No
failed search, timeout, rational rank, or unverified model-surjectivity assertion
supplies an exclusion.

Thus the source a,d path family is impossible below 248. The a,e family follows by
swapping the physical labels d,e, which preserves the entire canonical split. All
ten added-center cases are now closed. Together with the private-center argument, no
third ordinary quartic word can occur at a genuine split source value.

### Recoverable sources establish the general E budget

Every genuine split has exactly two disjoint-tail quartic source word pairs.
Removing the unique common tail label is the inverse. Write a fixed source pair as
$Q=2u+s_L=2v+s_K$, where L,K are disjoint two-element tail sets and $s_L=\sum L$,
$s_K=\sum K$. Its two unused labels are i,j. If both lifts were genuine splits,
their third words would imply

$$
2j+s_L+s_K-r=Q+i,\qquad 2i+s_L+s_K-r'=Q+j,
$$

where r and r' belong to $L\cup K$. Each expression removes one actual tail
occurrence and is a nonnegative word.

Adding these equations and the two quartic words gives

$$
s=3u+3v+r+r',
$$

a nonnegative mass-eight rival omitting i,j. Hence one source cannot serve two
different split outputs.

The theorem just proved places all these sources in two-ordinary quartic fibers.
Such a fiber contains exactly one ordinary word pair, so distinct source pairs are
also distinct E outputs. Consequently E>=2q globally in the hypothetical odd
small-order setting, even if other quartic values contain triangles, paths, stars or
splits.

## Lemma 8. An injective assignment of splits to open center edges

**Dependencies:** Lemma 7 and the finite replacements below. **Conclusion:** every
split can be assigned to a distinct incident open center edge, so q<=h. Source
values and center edges remain different objects.

### One ordinary cubic triple supports at most one genuine split

Normalize an ordinary cubic triple as

$$
2x_0+a_0=2x_1+a_1=2x_2+a_2=V.
$$

Private centers and protection give six distinct labels x0,x1,x2,a0,a1,a2. Name the
other two p,r. A genuine split descending to one of the three cubic pairs chooses
its third center z and middle tail b among the other four labels, with the last two
added to that pair. There are exactly 36 candidate fibers; no physical overlap is
omitted.

Complete direct/source/growth exclusions remove 30 candidates below 248. The six
necessary residuals have third center p or r and middle tail ak of the unused cubic
word. Their added labels are xk and the other free label. For a fixed free center p,
the third quintic word is

$$
2p+a_0+a_1+a_2,
$$

while its output is V+xk+r. Two choices of k would force equal distinct xk labels.
Hence at most one output can use each free center.

The proof retains and checks all fifteen pairs of the six residuals, including the
opposite-center cases. Six pairs give direct label collisions; nine have positive
quartic-growth bounds 108 or 110. Three of those models retain genuine order-three
torsion. Each model is surjective over all relevant odd-group solutions; no odd
factor is divided out. Every selected quartic pair has a positively reconstructed
mass-eight rival identity, proving T4>=89 and contradicting the budget.

Thus two genuine split outputs cannot descend to the same ordinary cubic triple in a
putative small-order counterexample. This is a value-level restriction with an exact
cubic descent, not an assumed allocation of c credits.

### Replace all 56 former cap-two inferences

The base coverage has 56 leaves producing three ordinary quartic words. Those words
are not contradictions under the general cap three. Every such inference is replaced
here:

| Former inference | General replacement |
| --- | --- |
|28 paths in one-root/two-open coverage|Explicit rival or split-source contradiction, or positive growth to at least 89 repeated quartic values.|
|14 paths in two-open sharing coverage|Positive growth to at least 89 values.|
|Four paths in repeated-mark coverage|Split-source contradiction or positive growth.|
|Two triangles in repeated-mark coverage|A third ordinary word at an actual genuine-split source, contradicting the source-budget lemma. No t=0 assumption is used.|
|Eight stars: two one-root and six sharing cases|Removing the common tail gives an ordinary cubic triple containing both split descents, contradicting the preceding one-triple/one-split lemma.|

The star inverse is literal common-tail removal. Its six cubic labels are distinct,
and each of the two actual split descents is a pair from that triple. The two split
fibers differ. The new verifier checks these facts and their integer identities; it
never treats the star itself as forbidden generally.

Some path relation systems require more than a chosen dyadic pivot sequence. Solve a
unit-minor subsystem and recover its free labels using a power-of-two scale. The
remaining integer constraints, after an integer unimodular coordinate change, are
n_i*delta=0. Bezout makes their combined condition gcd(n_i)*delta=0. Only the power
of two is removed; the odd part remains torsion. The verifier checks the unit minor,
coordinate recovery, every remaining constraint, unimodularity, and the retained odd
gcd.

All other base exclusions are positive identities involving a label collision,
closure of a declared open edge, a protected squarefree word, or a non-original
mass-eight rival. They remain valid generally. The new verifier traverses the
complete saved base coverage and intercepts all 56 quartic-triple inferences instead
of accepting the old C4=0 conclusion.

### Four complete local lemmas

Call a split with two open sources a two-open split. Call one with exactly one open
source a root mark at that source-center edge. With the source-fiber theorem and all
replacements above, the following statements hold under the general cap three:

1. **One open center edge cannot carry two distinct root marks.**
2. **The two open source edges of a two-open split cannot both carry root marks.**
3. **A root mark cannot be followed by a two-edge auxiliary path.** More explicitly: if a two-open split joins open center edges U,V and U carries a root mark, no distinct two-open split can join V to an edge W different from U.
4. **No open center edge is incident to three distinct two-open splits with different other source edges.** Also, two different two-open splits cannot have the same two open source-center edges.

Here "different" refers to genuine word fibers/outputs, not alternate presentations
of the same fiber. These lemmas allow every physical label overlap among different
splits: each split uses the same eight positions.

#### Finite coverage and positive proof identities

Fix a canonical two-open split on labels 0,...,7 with open source edges 02 and 12. A
split using a specified source edge is recovered by choosing its third center (six
choices), the added label (five choices), a two-tail partition (six choices), and
the omitted label of its third word (four choices). There are exactly 720 fibers. A
root mark also chooses one of the four possible closures of its other source, giving
2,880 presentations.

No repeated-center configuration is removed by assumption. Choices using the central
split's same center triple are included. Presentations of the identical fiber are
omitted only when the statement explicitly requires a distinct additional split.

| Local statement | Complete positive coverage |
| --- | --- |
| Root on 02 beside a canonical two-open split | 2,870 of 2,880 presentations excluded; ten remain as necessary relation systems. |
| Root marks at both ends of that split | All 100 pairs of the ten surviving left/right relation systems excluded. |
| Root followed by a second auxiliary edge | All 7,190 distinct extensions excluded; the ten identical-central presentations are explicitly skipped. |
| Two distinct two-open splits sharing 02 | 685 of 719 additional fibers excluded; 34 necessary systems remain. Cases with the same other edge as the central split are all excluded, proving no parallel auxiliary edges. |
| Three two-open splits incident to 02 | All 962 pairs with different other source edges excluded. The 194 same-other-edge pairs do not describe three distinct incident auxiliary edges. |
| Two distinct root marks at 02 | All 11,504 presentations excluded, covering four first-mark closures and every second mark. The sixteen identical-first-fiber presentations are explicitly skipped. |

Each exclusion supplies an integer combination of its original cubic/quintic/closure
relations equal to a power of two times one of:

- a label difference, contradicting distinctness;
- an open doubled-center difference minus an actual label difference;
- a protected squarefree word minus another word;
- a non-original nonnegative mass-eight word minus all-ones; or
- both differences between three ordinary quartic words.

The last type is only a replacement trigger. A triple does not contradict the
general cap three; all 56 occurrences are resolved below. All factors canceled are
powers of two. Rational elimination is only a discovery aid, never a proof premise.
The checker reconstructs coverage by a different source-and-unused-label enumeration
and checks all identities by integer multiplication.

One instructive degree-three residual has the three cubic descents

$$
2x+c=2y+a,\qquad2x+y=2d+e,\qquad2x+d=2c+e,
$$

and two quartic source equations

$$
2x+a+c=2z+e+b,\qquad2x+y+a=2z+e+b.
$$

Subtracting the last two directly gives c=y. No cancellation of three, rational-rank
inference, or torsion argument is needed. Its d/e mirror has the same direct label
collision. Explicit original-row identities retain these cases even when a chosen
rational basis would suggest unnecessary odd denominators.

### Auxiliary graph and injection

Use the h open center edges as vertices. A two-open split is an edge between its
source vertices; a single-open split is a mark on its only open source. Include
unused center edges as isolated vertices.

Every split has an open source: the complete closed-both-source model forces
T4>=116. Its 6,670 positive growth-pair identities and closure placements are
checked in the new chain; this premise is independent of C4=0.

The general replacements restore all four local statements:

1. No vertex carries two marks.
2. The ends of one auxiliary edge cannot both carry marks.
3. A mark cannot be followed by a two-edge auxiliary path.
4. The graph has no parallel edges and has maximum degree two.

The unchanged complete coverage includes 2,880 one-root presentations, 100 end-mark
residual pairs, 7,190 path extensions, 719 sharing presentations and 962 degree-three
residual pairs, and 11,504 repeated-mark presentations. Identical-fiber skips and
same-other-edge cases are explicitly checked. All physical labels are shared within
the same eight positions.

A component cannot have two marks: adjacent ones violate Statement 2, and more
distant ones violate Statement 3 along a shortest path. A marked cycle also violates
Statement 3. Thus components are unmarked paths, unmarked cycles, or paths with one
mark, including isolated vertices.

Orient an unmarked path from a chosen root and assign each edge to its child. Orient
an unmarked cycle consistently. Assign a marked path's mark to its vertex, then
orient both sides away from that vertex and assign edges to children. These
assignments cover every split and use distinct incident open center edges across all
components. Therefore

$$
q\le h
$$

for any hypothetical odd N<248 counterexample, even with quartic stars, paths,
splits or triangles elsewhere.

By Lemma 6 and E>=2q, the case t=0 gives

$$
2N\ge496+2(h-q+R_3+c)+5w+(E-2q)\ge496.
$$

It is impossible for N<=247. Every remaining counterexample has a quartic
triangle. See [Alignment](alignment.md) for its normalized family.
