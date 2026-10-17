# The weighted counting inequality

This chapter derives equation (4) of [the proof](../PROOF.md).
Its only inherited inputs are squarefree protection, the packing bounds,
and the multiplicity caps proved in [Multiplicity](multiplicity.md).
Here P3 always counts ordinary pairs; repeated-cubic totals include pure
cubes only when explicitly stated.

## Hypotheses and counts

Full validity means allones is the unique nonnegative mass-eight word at
s=sum(A). Adding the complement of a squarefree word proves its protection
against EVERY different same-degree multiset. Use this full protection
throughout, never a weaker protected-set condition.

Suppose for contradiction that N is odd and below248. The inherited results
give ordinary cubic, quartic and quintic multiplicity at most three, total
cubic multiplicity at most three, and

    N>=56+T3+T5,     N>=71+2T4,     T4<=88,
    T3=36+k,        k=h+R3>=0.

Here Tj means |T_j|. Let n1,n2,n3 count quintic outputs with one,two,three
ordinary words; M counts repeated quintic outputs with no ordinary word.
Let C4 count ALL three-ordinary quartic outputs, not just triangles. Let Pj
count unordered pairs of different ordinary degree-j words at equal values.
Let Sj count such pairs whose tails are disjoint. The ordinary word counts
at degrees3,4,5 are56,168,280 respectively. Thus exactly

    P5=n2+3n3=140-n1/2+3n3/2,
    T5=140+(n1-n3)/2+M,
    O4=168-P4+C4<=T4<=88,
    delta=N-56-T3-T5>=0,
    N=232+k+(n1-n3)/2+M+delta.

O4 counts ordinary quartic VALUE outputs. The formulas count pairs and
outputs separately; mixed words at an ordinary output do not make a new value.

## The universal midpoint rival supplies the missing placement constraint

For each unordered label pair c,d, allowing repetition, put
q=(s+c+d)/2. Its reflection (s-c-d)/2 cannot be a cubic multiset value:
a degree-three word W there would give the nonnegative mass-eight rival
2W+e_c+e_d at s. This word has at most two odd coordinates, so cannot
be allones. The 36 midpoint values are distinct: full protected pair sums
handle squarefree pairs and collisions with repeated pairs, while oddness
makes 2c=2d imply c=d.

Suppose q has two ordinary quintic words O,O'. Their doubled centers are
private in the whole fiber, so coordinatewise O+O'<=2. Then

    r=2*allones+e_c+e_d-O-O'

is integer, nonnegative, has mass eight and value s. Validity forces
O+O'=allones+e_c+e_d. If c=d this is impossible: its c coordinate is
three. If c!=d it forces the centers to be precisely c,d and the six
tail labels to occur once each. This is exactly an S5 pair. No third
ordinary word can occur: every other label already appears in those two
words and therefore cannot be a third private doubled center.

Consequently EVERY one of the 36 midpoints is either an S5 output, a
single-ordinary output, a mixed-only output, or outside T5. The disjoint
sets 3A and s-T5 leave exactly delta group elements uncovered. Since
every reflected midpoint is outside3A, at most delta midpoint values are
outside T5. Recovering the center pair from an S5 output proves uniqueness,
including when different pairs reuse labels. Therefore

    36<=S5+n1+M+delta.                            (A)

This is the new structural coverage step. It is not inferred from local
caps or a chosen allocation of distinct witnesses. Nonnegativity in the
rival is explicit; no factor three is canceled.

## Quartic compression and midpoint coverage close the no-triple branch

Ordinary pairs have private centers. Removing their common tail labels
gives a recoverable inverse. At degree four, a pair either has one shared
tail label and descends to a cubic pair, or has disjoint tails. A cubic
pair uses four labels, leaving exactly four one-label lifts. At degree
five, intersection size2,1,0 gives respectively a cubic pair with six
two-label lifts, a disjoint-tail quartic pair with two one-label lifts,
or an S5 pair. Hence the exact inherited pair identities are

    P4=4P3+S4,
    P5=6P3+2S4+S5=(3/2)P4+(1/2)S4+S5.           (B)

Pairs in a triple fiber are counted separately; no pair is lost and no
distinct output is inferred from a lift. Since O4<=88, P4>=80+C4.
Combining (A),(B) with the exact output counts gives

    n1/2+3n3/2+M+delta>=16+3C4/2+S4/2,
    2N>=496+2k-4n3+3C4+S4.                       (G)

If n3=0, every term on the right after496 is nonnegative, contradicting
N<=247. **Thus the entire no-three-ordinary-quintic branch is closed.**
This handles systems with no useful triangle core, including mixed-only
outputs, without assuming that a mixed-only output must exist.

## Paths cancel; the surviving weighted obstruction is precise

Classify a three-ordinary quartic fiber by its three tail edges on the
five noncenter labels. Classify a quintic fiber by its three omitted
edges there. The exhaustive graph types are triangle,star,path,split.
Write c=C3ordinary, t=C4triangle, p=C4path, w=C4split, q=C5split, and
E=S4double, the number of two-ordinary quartic fibers with disjoint tails.
Recoverable common-tail removal and unused-label addition prove

    n3=c+2t+p+q,     C4=t+2c+p+w,
    S4=p+2w+E.                                    (C)

Here are the four bijections, including their inverses. Centers are private,
so the labels mentioned in each removal are distinct from the centers.
The multiplicity caps ensure that a lifted fiber has exactly three ordinary
words. Distinct added labels give distinct output values.

| Target fibers | Construction and inverse |
| --- | --- |
| Quintic triangles: C5triangle=c | Omitted triangle edges ab,bc,ca give tails cde,ade,bde. Remove the two common labels d,e to obtain an ordinary cubic triple. A cubic triple uses six labels, so adding its two unused labels is the unique inverse. |
| Quintic stars: C5star=2t | Omitted star edges ha,hb,hc give tails bcd,acd,abd. Removing the common label d gives a quartic triangle. A quartic triangle uses six labels and has two distinct one-label lifts, giving the factor two. |
| Quartic stars: C4star=2c | Remove the common hub from tails ha,hb,hc to obtain a cubic triple. Conversely add either of the two unused labels to the three cubic words. |
| Quintic paths: C5path=p | Omitted path edges 01,12,23 leave label 4 common to all tails. Remove it to get quartic tail edges 23,03,01, also a path. A quartic path uses seven labels, leaving exactly one inverse lift. |

This last correspondence corrects the historical assertion that both
quintic paths and splits have no common tail. A quintic split has none;
a quintic path has exactly the common tail described above.

For S4, a quartic path has one disjoint pair of tail edges, a quartic split
has two, and a triangle or star has none. Two-word fibers contribute
exactly E. This proves the third identity in (C) as well as the first two.

Substitution of (C) into (G) yields

    2N>=496+2k+2c-5t+5w-4q+E.

In particular every remaining N<=247 counterexample requires

    5t+4q>=2+2k+2c+5w+E.                         (J)

If t=q=0 there is an immediate contradiction. Thus a remaining system
with NO quartic triangle must have genuine SPLIT quintic triples; path
triples cannot supply its compression deficit. Mixed-only fibers are
already included in (A) and in the exact packing slack, not omitted.
