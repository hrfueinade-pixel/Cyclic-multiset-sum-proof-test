# The minimum cyclic modulus for eight points is 248

**Theorem.** Let A={a0,...,a7} be eight distinct points in Z/NZ. Suppose
the nonnegative integer solutions of

    sum mi=8,    sum mi*ai=sum ai (mod N)

consist only of m0=...=m7=1. Then N>=248. Equality is attained by

    A={0,1,3,7,15,31,63,127} in Z/248Z.

The final argument below is elementary. It uses the earlier proved
counting/assignment theorems and the checked symbolic exclusions of
large alignment classes, multiple triangle classes, and the two-triangle
class. The resulting full proof is computer-assisted; it has not received
independent external mathematical review or proof-assistant certification.

## 1. Established reductions and the exact ledger

The established parity proof excludes every even N<248. For odd N<248,
the earlier proofs give the following quantities and statements. Here
t is the number of ordinary quartic triangle outputs; q the number of
genuine quintic split outputs; h the number of open unordered center
edges; R3 the repeated-cubic excess; c the number of ordinary cubic
triple outputs; w the number of ordinary quartic split outputs; and
U=E-2q the number of unused two-ordinary disjoint-tail quartic sources.
They are nonnegative, and

    2N >= 496+2(h-q+R3+c)-5t+5w+U.                 (1)

The general assignment proves q<=h. Thus t=0 is impossible below248.
Stage58 strengthens the assignment to

    q<=h-o,                                        (2)

where o counts DISTINCT open paired edges belonging to quartic triangles.
This counts actual edges once, rather than fresh witnesses per triangle.

A triangle is three disjoint directed edges with common alignment
tau=2x-a. Translate all eight labels by -tau. Its three pairs become

    A=(u,2u,v,2v,w,2w,p,r).                         (3)

Translation preserves the full degree-eight validity condition and
uses no division. Stage60 bounds every alignment class by four edges
and leaves only shapes (2,2,2,1,1), (4,2,1,1), (3,2,2,1). Stage61
permits only one triangle-bearing alignment class globally. The complete
Stage62 proof excludes (3,2,2,1), including every additional ordinary
and pure refinement. Therefore t=1, and the only shapes remaining are
(2,2,2,1,1) and (4,2,1,1).

## 2. A triangle forbids every distinct-pair sum inside the normalized set

**Lemma.** In (3), no two distinct physical labels x,y of A have x+y=z
for any physical label z of A.

The triangle contains three disjoint doubling pairs. The two labels
x,y meet at most two pairs, so choose another pair b,2b disjoint from
{x,y}. Starting from the original eight-term word, remove x,y,b,2b
and add z and three copies of b. Keep each of the other four labels
once. This is a nonnegative degree-eight word: four terms are removed
and four added. Its change in value is

    z+3b-(x+y+b+2b)=z-x-y=0.

It differs from the original: both x and y were removed, and only one
new term z can restore either of them; b is different from both. This
is a forbidden mass-eight rival. The lemma allows z to coincide with
any of the labels, including x,y,b,2b. No odd cancellation is used.

## 3. A paired edge is open exactly when it is terminal

Consider a paired edge a->b=2a in the normalized alignment class. Its
unordered center edge is closed exactly when

    2(a-b)=x-y

for distinct physical labels x,y. Since 2(a-b)=-b, this is y=x+b.
If x!=b, the lemma forbids it: x,b are distinct physical labels whose
sum is y. The only possibility is x=b, y=2b, which is precisely an
outgoing aligned edge b->2b in the same zero-alignment class.
Conversely such an edge supplies the difference b-2b=-b and closes
the center edge. Consequently every terminal paired edge is OPEN,
under all ordinary and pure collisions, without a no-new-collision
hypothesis.

In shape (2,2,2,1,1), all three triangle edges are terminal: o=3.
In shape (4,2,1,1), the unique triangle uses the first and last edges
of the four-vertex path and the isolated two-vertex path. The latter
two edges are terminal: o=2. Hence every remaining case has o>=2.

## 4. The global contradiction

By (2), h-q>=2. Substitute this and t=1 into (1), retaining the
nonnegative R3,c,w,U:

    2N >= 496+4-5 = 495.

But N<248 implies 2N<=494. This contradiction excludes every remaining
odd order. Together with the proved even-order exclusions, N>=248.
No modulus sweep, absent witness, timeout or incomplete search is used
in this finishing argument.

## 5. Equality at 248

Write ai=2^i-1, i=0,...,7. A nonnegative degree-eight word has

    sum mi*ai=sum mi*2^i-8.

The original sum is247, so a rival modulo248 would give

    S=sum mi*2^i congruent to255 modulo248,
    8<=S<=1024,    sum mi=8.

Thus S is255,503,751 or999. With coins 1,2,...,128, the minimum number
of coins for S is floor(S/128)+popcount(S mod128): carrying pairs
upwards reduces their number until each smaller denomination occurs
at most once. The four minima are respectively8,9,11,12. Only255
can use eight terms; its unique minimum representation uses every
denomination once. Therefore the displayed A is full-valid modulo248,
and the bound is sharp.

## 6. Checkable dependency boundary

The elementary final lemmas and both remaining forest counts are
checked by stage63_finishing_check.py using exact integer identities.
This is symbolic coverage of the lemma, not an enumeration of groups.
The main non-elementary local dependencies added here are:

- Stage60: six large forest exclusions and the uniform four-edge cap;
  stage60_certificate_check.py with stage60_forest_certificates.json.gz.
- Stage61: at most one triangle-bearing alignment class;
  stage61_certificate_check.py with stage61_interaction_certificates.json.gz.
- Stage62: no two-triangle class;
  stage62_certificate_check.py with stage62_single_class_certificates.json.gz.

The already published Stage54/55/58/59 proofs supply source allocation,
the weighted count, paired-edge source exclusion, at least nine ordinary
cubic pairs, and the local split restrictions used in these exclusions.
The earlier parity proof is summarized in stage37_findings.md, including
the complete Stage30-32 parity splits and the Stage35 antipodal lift.
The incomplete Stage56/57 and one-triangle Stage62 discovery trees are
not premises; they may be left terminal. Their positive identities are
used only when individually reconstructed and checked in the completed
proof graphs.

The Stage60 and Stage61 compressed archives may be stored as numbered
`.part000`, `.part001`, ... files beside their checkers. The standard-library
reader concatenates these in order when the whole archive is absent.
The manifest checks every part and the unchanged reassembled archive hash.
