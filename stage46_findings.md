# Stage 46: a proof-first mixed-fiber restriction

2026-10-11. Continues Stage 45 / open PR #17 at
archived-source. Earlier PRs remain unmerged.
The full theorem N>=248 remains OPEN. Equality at 248 is attainable;
N>248 is not the intended conclusion. No arbitrary new modulus is excluded.

This stage gives elementary proofs, not a modulus search or a larger
growth-certificate search. Its main new result is:

> In any odd group, a full-valid eight-set with an ordinary quartic
> triangle has NO coexisting 4 or 22 word and at most TWO coexisting
> 31 words at that value.

Under the inherited ordinary cap, the entire triangle fiber consequently
has at most five representations. Its paired star quintics have at most
two additional representations containing the added label. A simultaneous
parity obstruction also couples mixed representations across the paired
quintic fibers. These restrictions do not yet prove the global tradeoff.

## 1. Conventions and the identity used throughout

Every squarefree sum is uniquely represented under full validity: append
the omitted labels to a competing word to obtain a mass-eight rival.
In odd order, fixed-parity quartic and quintic words are injective within
each parity class. Indeed a word p has the unique form p=epsilon+2v;
for degree four or five, v has degree at most two. Equality for two words
with the same epsilon cancels two and contradicts protected pair sums,
or distinctness of single labels. This is cancellation by two, NOT by three.

An ordinary word is 2c plus distinct other labels. Its doubled center
cannot occur in another representation of the same value: cancel one c
and the ordinary side becomes squarefree. Thus three ordinary centers are
distinct and private, and all other words at their value lie on the other
five labels B. This argument requires full protection, not merely cubic
protection.

Let three ordinary words of degree d, for d=4 or 5, be

    O_i=2c_i+t_i,  value(O_i)=q,  i=0,1,2,

where t_i is squarefree on B, of degree d-2. Write D=t_0+t_1+t_2
as a COUNT VECTOR, and S=sum B as a group value. For s=sum A,

    2s=2S+3q-value(D).                                  (1)

Suppose M_1,M_2,M_3 are ANY three words on B at value q, with repetition
of the same word permitted. If their count-vector sum has the same parity
as D, then

    r=1_B+(M_1+M_2+M_3-D)/2                             (2)

is an integer nonnegative mass-eight word on B, and value(r)=s by (1).
Its mass is 5+(3d-3(d-2))/2=8. Each coordinate D_j is at most three.
If D_j=3, parity forces the corresponding M sum to be odd and at least
one, repairing the only possible negative coordinate. If D_j<=2 there
is no negativity. The three centers have count zero, so r is not original.

This proves a simultaneous-collision obstruction. Overlapping supports,
repeated witnesses, and reused labels are explicitly allowed in (2).
There is no assertion that different triples give distinct rivals.

### A local consequence, and its quantitative limitation

Let P be the set of parities of words on B at q. Put
E={p+parity(D):p in P}, with addition in F_2^5. E lies in the
four-dimensional even-weight subspace. Equation (2) says E is sum-free:
there are no x,y,z in E with x+y=z, including repeated choices.
For any x in nonempty E, E and x+E are disjoint, so |E|<=8.
Fixed-parity injectivity therefore bounds the number of B words by eight.
The entire fiber has at most eleven words if there are exactly three
ordinary ones. This is a LOCAL conclusion, not a global growth estimate.

## 2. Normalize an ordinary quartic triangle

Let X={a,b,c}, let the two other B labels be u,v, and write the triangle as

    2x+b+c=2y+a+c=2z+a+b=q.                              (3)

The eight labels are a,b,c,u,v,x,y,z, all distinct. Translate every label
by -q/4, which is legitimate in odd order, so the new q is zero. The target
changes by eight times the translation, exactly as any mass-eight word does.
We now have

    2x=-(b+c),  2y=-(a+c),  2z=-(a+b),  s=u+v.          (4)

No parameter is divided by three; odd torsion is retained.

### No 4 or 22 word

If a B word 2p+2r (allowing p=r) represents zero, oddness gives p+r=0.
The word 3p+3r+u+v has mass eight and value s. Its missing centers make
it a genuine rival, even if p,r reuse u or v. Equivalently apply (2) to
three copies of this even-parity quartic word. Thus 4 and 22 are excluded.

### No more than two 31 words: hand proof

Draw a directed edge i->j for a word 3i+j=0 on B.
Tripled centers are distinct, since equal centers force equal tails.
The following restrictions are elementary.

1. There is no edge within X. Its parity would be one of the triangle
   tail parities in (3), violating fixed-parity injectivity and private centers.
2. Opposite edges i->j and j->i give 2(i-j)=0, violating distinctness.
3. Two different X centers cannot have edges to the same outside label.
   For example 3a+u=3b+u gives 3(a-b)=0. From (4),
   2[(a+x)-(b+y)]=3(a-b)=0. Oddness gives a+x=b+y,
   a forbidden collision of different squarefree pairs.
4. Two X centers cannot have edges to different outside labels either.
   If 3a+u=3b+v=0, then c+x+y+5z is a mass-eight rival:
   its doubled value is -6a-6b=2(u+v).
5. A directed path a->u->b, with distinct a,b in X, is impossible.
   Here u=-3a and b=9a, so z=-5a by (4).
   The mass-eight word 5a+u+v+z has value u+v=s.
6. A directed triangle is impossible. Its three 31 parities sum to zero,
   so (2) supplies a rival. In the only relevant triangle a->u->v->a,
   summing its equations and canceling four gives a+u+v=0;
   2a+3u+3v is an explicit mass-eight rival for s=u+v.

Now suppose there are three 31 words. Rules 3 and 4 allow at most one
tripled center in X, so the centers are a,u,v. Relabel u,v to make a->u.
The edge from u cannot point to a (rule 2) or another X label (rule 5),
so it points to v. The edge from v cannot point to u (rule 2) or a
(rule 6), leaving v->b for a different b in X. Thus the ONLY remaining
case is

    a->u->v->b,  with c the third X label.

Its equations give u=-3a, v=9a, b=-27a. The word

    2a+b+c+2v+x+y                                       (5)

has eight terms. Twice its value, using (4), is
3a+b+4v=12a=2(u+v). Oddness proves that (5) represents s. It is not
the all-ones word. This closes the final case and proves the cap TWO.

The proof is universal for a full-valid eight-set in an odd group. Only
the statement that the WHOLE fiber has at most five additionally uses
the Stage 41 conditional ordinary cap three under N<248.

## 3. Consequences for paired star quintics

In the hypothetical sub-248 case, (3) has the two ordinary quintic lifts
at q+u and q+v. Stage 44 proves their exact pairing and unique quartic core.
For a B-only word M at q+u that contains u, remove one u. The result is
a B-only quartic word at q. It cannot be squarefree; it cannot be ordinary
under the conditional ordinary quartic cap; Section 2 excludes 4 and 22.
It must be 31. Removal and addition of u are inverse maps, so at most
TWO additional quintic words at q+u contain u. The same holds for v.
This is a bijection, not a fresh-label charge. Words avoiding the added
label are not bounded by this argument.

In particular a 221 companion cannot contain the added label: removing
it would give either a 22 word or a fourth ordinary quartic word. Across
ALL paired star fibers there is an exact representation-incidence count

    2 * sum_(quartic triangle cores q) number_of_31_words_at_q
      <= 4*C4triangle = 2*C5star.                       (8)

Different cores have different star outputs by the recoverable inverse
in Stage 44; the two outputs of one core are different since u!=v.
Thus (8) does not reuse a word at two outputs. It bounds representations
at existing outputs, not newly produced quintic VALUES.

There is also a direct CROSS-FIBER obstruction. Keep q general. If L is
a B-only quartic word at q, and M,M' are B-only quintic words at q+u,q+v,
then

    parity(M)+parity(M')+parity(L)=e_u+e_v               (6)

is impossible. Otherwise

    r=(M+M'+L+e_u+e_v)/2                               (7)

is nonnegative, integer and mass eight. Its value is
(3q+2u+2v)/2=s by (3), and it omits all three centers. Equation (7)
handles every mixed word shape and arbitrary overlaps. It assumes no
distinctness of labels used by different words beyond the original A.

## 4. Failed routes and the small targeted experiment

**First structural attempt: use the single-fiber parity bound globally.**
Equation (2) is proved and gives at most eight accompanying B words.
It does not say that B-only outputs in different fibers are disjoint,
or force sufficiently many fibers. The 456 nonordinary quintic words
can still overlap ordinary outputs without a proved global allocation.
Therefore this route stops before any T5>=156-h-R3 conclusion.

**Second structural attempt: bound quartic predecessors by seven.**
Section 2 controls total WORD multiplicity in triangle fibers, but even
one 31 word using u,v can make all eight predecessor labels occur. The
unrestricted seven-predecessor bound is false, not an available lemma.
A new positive control below realizes precisely this obstruction.

A small fixed symbolic experiment tested three 31
words beside the quartic triangle, with all centers and tails on B.
No X-X edge need be included, by fixed-parity injectivity. Choosing three
distinct centers and their allowed tails gives exactly 200 assignments;
S3 on X and S2 on u,v reduce these to 22 orbits. Every orbit has a saved
positive mass-eight rival with only dyadic cancellation. The retained
identities suggested the much shorter hand proof in Section 2. The
theorem does NOT rely on rational kernels as complete group models.

An earlier diagnostic on FOUR accompanying 31 words retained 256
assignments and 30 orbits. Its B-only rival test did not close 100 cases.
That absence was never promoted: it missed squarefree rivals involving
the centers and torsion consequences. The hand proof above closes three
words already, so the full four-word family is now excluded as a consequence.

### Positive counterexample to the seven-predecessor shortcut

Take the translated set

    A={14741,14773,15317,19652,0,14433,14449,14721}
      in Z/157217.

Before translation by 14739, its labels are
2,34,578,4913,-14739,-306,-290,-18. Its quartic value zero has exactly
the three ordinary triangle words on X={2,34,578} and the 31 word
3*4913+(-14739). Their supports together use all eight labels, so all
eight values q-a lie in 3A. This respects the new cap two, but defeats
the predecessor cap seven. It is not a sub-248 counterexample.

An elementary validity proof is included in the companion control script:
write parameters as powers of 17. The first three coefficient equations
force all three triangle-center counts to have the same parity; the last
equation forces outside counts to be (1,1) or (4,2). The latter leaves
only two triangle terms, impossible, and the former forces all six
triangle counts to one. The complete fixed 6435-word check is secondary
arithmetic support, not the proof or a modulus search.

## 5. Challenge and remaining global lemma

The hand proof was challenged separately against reused labels, both
orientations of each 31 edge, the possibility of order-three torsion,
the precise count mass, and non-originalness of every rival. In rule 3,
3(a-b)=0 is NOT canceled; it is used in a doubled squarefree-pair identity.
In (5), a may be torsion or a nonunit; it is never divided out.
The parity constructions check nonnegativity, not merely integrality.
The starred quintic consequence alone needs the small-order ordinary caps.

The standalone checker imports no discovery code. It independently checks
the 22 positive orbit identities, all 200 assignments and hand-classification
coverage, the universal rivals in Section 2, and the positive control.
This is same-author separate arithmetic checking, not independent human
review or formal proof-assistant verification.

The sharply stated missing step is now:

> For a full-valid eight-set in odd 207<=N<248 with T4<=88, prove that
> quintic words avoiding the added labels in paired star fibers, and
> mixed words in all other fibers, cannot collectively compress below
> T5>=156-h-R3, using the new within- and cross-fiber obstructions.

There is no proved injection or allocation across those outputs yet.
Triangle-fiber closure alone is not a necessity theorem for an arbitrary
hypothetical counterexample. The 558 four-311-on-five-label assignments
from Stage 45 have NOT been reclassified here. No discovery-only historical
exclusion is promoted, and no old search or longer timeout is used.

## 6. Reproduction

    python -B stage46_proof_check.py

Optional regeneration of the fixed symbolic diagnostics:

    python -B stage46_triangle_31.py
    python -B stage46_three_31_probe.py
    python -B stage46_positive_control.py

The supporting code and separate report are stacked on PR #17. Earlier
PRs remain unmerged. The original odd-interval theorem remains OPEN.
