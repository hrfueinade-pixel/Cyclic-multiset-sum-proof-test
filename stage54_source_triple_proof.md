# Stage 54: genuine splits use only two-ordinary quartic source fibers

2026-10-12. This is a global source restriction in the full hypothetical odd N<248 problem, including C4>0. It does not prove the final modulus bound.

## Theorem

Under full eight-term validity, odd N<248, and the established ordinary cubic/quartic/quintic caps, each quartic word-pair source of a genuine quintic split lies at a value with exactly TWO ordinary quartic representations. Mixed representations at that value are allowed.

Consequently, with E counting two-ordinary disjoint-tail quartic fibers and q genuine quintic split outputs,

    E >= 2q

holds in the GENERAL branch. Previously the known source injection gave only S4>=2q; E=S4 was available only in C4=0.

The proof has two elementary reductions and complete computer-assisted exclusions for one specific remaining source-path family. No group elements, parameters or moduli are enumerated. Only powers of two are canceled, including in all finite growth certificates.

## 1. A third quartic center must be the added label

Normalize a genuine split as

    2x+c+d+e = 2y+a+d+e = 2z+a+b+c.

Focus on its source

    Q=2x+d+e=2z+a+b.

The two unused source labels are c and y. Ordinary centers are private, so a third ordinary quartic word at Q must have center c or y.

Suppose its center is y and its two tails are u,v. Then Q=2y+u+v, while the cubic descent is 2x+c=2y+a. Subtracting gives

    a+d+e = c+u+v.

The left side is squarefree and its labels do not contain c. The right side contains c and is a different word of the same degree, regardless of whether u or v equals c. Full cubic protection forbids it. Thus center y is impossible.

The only possible third word is therefore

    Q=2c+u+v,

where u,v are two different labels among y,a,b,d,e. There are exactly ten possibilities. The other source of the split is symmetric by exchanging x,y and a,c.

## 2. The ten added-center possibilities

The retained proof archive handles every pair u,v. Six give direct protected collisions or label equalities:

| Tails | Positive consequence |
| --- | --- |
| y,a | y+d+e=3c |
| y,b | y+a+d+e=3c+b |
| y,d | y+a+e=3c |
| y,e | y+a+d=3c |
| a,b | 2z=2c |
| d,e | 2x=2c |

All squarefree words displayed differ from their rivals. The factor two is a unit in odd order.

The b,d case has a positive certificate separating 89 repeated quartic values in its complete dyadic parameter model, contradicting T4<=88. The b,e case is its d/e mirror. The checker reconstructs a positive mass-eight separation identity for every pair of the 89 selected quartic words.

The only remaining shape is u,v=a,d or its a,e mirror. Its quartic source triple is

    2x+d+e=2z+a+b=2c+a+d.

The tail edges de,ab,ad form a quartic path. This source-path family is excluded in Sections 3-5. The proof does not assume a local fiber cap, fresh mixed output, or distinct source credit to remove it.

## 3. Why additional cubic relations are forced

Read stage54_split_count_hand_proof.md for the independent elementary argument. It proves

    q<=4P3ordinary,     3t<=4P3ordinary,

and combines them with the inherited exact lift identities and Stage48 bound to show:

> Every putative odd N<248 counterexample has at least SIX unordered equal pairs among its 64 repeated cubic marks.

This deduction precedes and does NOT use the theorem E>=2q being proved here. In particular, it does not rely on q<=h or C4=0. There is no circular source allocation premise.

The complete source-path model consists of three original relations: the split's cubic descent, its first quartic source equality, and the equality of that source with 2c+a+d. A dyadic unit-pivot parametrization is surjective over any odd group. It has 60 formal repeated cubic values: 56 singleton classes and four double classes. Thus a realization with no further equality would have only four cubic collision pairs, already impossible by the preceding global count.

There MUST be an equality between two formally different cubic classes. This is an actual necessary relation; generic integer examples or absence in a search are not premises.

## 4. Complete first-cubic coverage, with odd torsion retained

The 64 repeated cubic words have 2,012 pairs with different formal coefficient values in this model. Normalize a coefficient difference only by sign and powers of TWO, obtaining 901 distinct directions. Odd common factors are deliberately retained.

For each direction, an integer unimodular column transformation U gives

    direction * U = (g,0,0,0).

The first new parameter satisfies g*delta=0. Remove only the power of two in g, leaving its odd part as explicit torsion. The full label model is obtained by multiplying the original coefficient matrix by U; the remaining parameters are free. This describes EVERY odd-group solution, not merely a rational or torsion-free embedding.

The first inventory has:

- 568 positive direct exclusions: label/protected collisions, eight-term rivals, or four ordinary quartic/quintic words violating the inherited cap three;
- 327 complete models with positive 89-value quartic growth certificates;
- six remaining necessary models, indices 389,740,764,794,800,805.

The six residuals have no torsion coordinate. Each has 59 formal repeated cubic values, consisting of 54 singleton and five double classes. With no further equality it would have only five cubic collision pairs, again contradicted by the SAME elementary global count. Therefore a second formally new cubic equality is compulsory in each residual.

Weak positive bounds for these six models are not treated as exclusions. The second equality is forced deductively, rather than by raising a clique-search timeout.

## 5. Complete second-cubic coverage closes the source-path family

Within each residual, normalize every formally new cubic equality by sign and powers of two, and apply the same unimodular reduction. The complete inventories are:

| First residual | Second directions | Result |
| --- | ---: | --- |
| 389 | 734 | All positively excluded |
| 740 | 687 | All positively excluded |
| 764 | 739 | All positively excluded |
| 794 | 746 | All positively excluded |
| 800 | 717 | All positively excluded |
| 805 | 716 | All positively excluded |
| Total | 4,339 | Complete coverage |

Of these, 3,286 have direct integer exclusions; 1,053 have positive 89-value quartic growth proofs. Odd torsion orders 3,5,7,9 are kept in these models. Every first/second model is bound to its exact representative cubic equality and complete direction inventory.

The standalone verifier imports no discovery or elimination code. It checks the base unit minor, free-label coordinate recovery, unimodular determinants, retained gcd/torsion constraints, every coverage direction, and every direct integer identity. For each retained set of 89 quartic words it independently constructs an explicit nonnegative mass-eight rival identity for EVERY selected pair, using the finite list of all 6,435 mass-eight words.

This reconstructs 5,407,996 positive quartic separation identities across the source b,d model and the first/second inventories, plus 3,860 direct integer identities. No failed search, timeout, rational rank, or unverified model-surjectivity assertion supplies an exclusion.

Thus the source a,d path family is impossible below248. The a,e family follows by swapping the physical labels d,e, which preserves the entire canonical split. All ten added-center cases are now closed. Together with Section1, no third ordinary quartic word can occur at a genuine split source value.

## 6. Recoverable sources establish the general E budget

Every genuine split has exactly two disjoint-tail quartic source word pairs. Removing the unique common tail label is the inverse. A fixed source pair Q=2u+A=2v+B has exactly two unused labels i,j. If both free-label lifts were genuine splits, their third words would give

    2j+A+B-r=Q+i,     2i+A+B-r'=Q+j.

Adding these equations and the two quartic words gives

    s=3u+3v+r+r',

a nonnegative mass-eight rival omitting i,j. Hence one source cannot serve two different split outputs.

The theorem just proved places all these sources in two-ordinary quartic fibers. Such a fiber contains exactly one ordinary word pair, so distinct source pairs are also distinct E outputs. Consequently E>=2q globally in the hypothetical odd small-order setting, even if other quartic values contain triangles, paths, stars or splits.

## 7. The remaining finishing inequality

Put U=E-2q. This now has a valid general meaning: the number of two-ordinary disjoint-tail quartic source pairs unused by every genuine split. The Stage48 bound becomes

    2N >=496+2(h+R3+c)-5t+5w-2q+U.

A sufficient full finishing statement is therefore

    5t+2q <=2(h+R3+c)+5w+U.                       (STILL OPEN)

The original full weighted inequality is still unproved. In particular E>=2q does not supply an injection q<=h in C4>0. The Stage53 local graph arguments may now encounter quartic path/star/triangle configurations which are not valid contradictions in the general branch. Their ownership and interaction with triangle doubling-path reuse must still be proved.

The general N>=207, even N>=248, Stage53 C4=0 conclusion, equality248, and Stage45 residual558 are unchanged. No arbitrary odd207..247 modulus is claimed excluded in full. This theorem supplies a general source budget for the original objective; it does not mark that objective achieved.
