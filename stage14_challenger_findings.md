# Stage 14 independent challenger: singleton cone III

Scope: one focused continuation from the Stage13 checkpoint. No
numerical computation or independent solver rerun was performed by
this challenger. The current root computation was read and audited;
its finite-computation dependency is retained. The full D=0 and
248 targets remain open.

## 1. Elementary reduction and subgroup-bound audit

Stage12's fresh one-pure core cone has precisely its five-point core
component and an isolated ordinary vertex on the complementary three
points. Normalize z=0 and the singleton cone to b=-2a. Then

    0=2a+b=2d+e,       b=2u+v+w.

The Stage13 nonpure-cone argument forces the unique representation
2u=r-s to have r in {v,w}, s=b. After swapping the ordinary tails,

    v=2u-2a,       w=-4u,
    III: (0,a,-2a,d,-2d,u,2u-2a,-4u).

All eight points must be distinct. This is not Family II, whose final
point is 2a-4u and whose ordinary value is zero.

The two deletions 2u+v and 2u+w from the isolated ordinary vertex
are unpaired cubic marks. Seven center-collision incidences at u
therefore force another cubic fiber of size at least three. This
fiber is different from the original fiber: a mark of the original
fiber at u would cone into the core component and enlarge its exact
five-point support. Hence R3>=2 elementarily. Cubic exterior packing
gives |H|>=184+2R3>=188. The singleton-tree determinant argument,
without R3=0, independently gives |H|<=2187. H is odd.

No uniqueness of partners of other pure cubics was assumed. Freshness
excludes extra original-fiber partners only because their cones
would enlarge the core support.

## 2. Closure-check mathematical and implementation coverage

The max-functional rank argument applies to III itself. Its formal
ordered differences span three coordinates because a,d,u occur
relative to zero. At partial rational rank below three, choose a
nonzero integer annihilator f of the existing integer rows. Signed
symmetry gives M=max_D f(D)>0. For D attaining M, every closure
equation 2D-E has f(2D-E)>=M, so it raises rank. Every actual h=0
realization satisfies one of the 56 branches. Three steps therefore
produce a full-rank integer presentation covering that realization.

Its parameters generate H; thus H is an odd determinant divisor in
188..2187. The determinant itself need not be odd or at most 2187.
Only common powers of two are divided from relation rows; no odd
torsion is discarded. Deduplication is by exact integer rows, not
rational rowspace. These are the same previously audited safeguards,
now checked for the III input rather than inferred from I/II outputs.

The current `stage14_singleton_cone_closure.py` and imported
`stage13_pure_cone_closure.py` were read in full. The wrapper calls
only check_family('III'); it does NOT call Stage13's I/II run loop.
Imports execute no historical search. Primitive local kernel orbits
and CRT use Stage10's shared kernel implementation. Distinct-point,
pair-sum, global doubling-closure, and optional full validity filters
are unchanged. Deadline checks are cooperative; one factorization
or kernel call is not preempted, and output serialization is outside
the deadline. The complete flag requires full exhaustion.

Read-only verification of `stage14_singleton_cone_results.json`:

* Scope: only III, cooperative 30-second deadline.
* Status COMPLETE, recorded total 6.343 seconds.
* 154788 full-rank matrices and 41859 derived order incidences.
* 40166 quotient maps; 36999 recorded images after 3167 duplicates.
* 598 repeated-point images; 21695 pair-sum failures.
* 14706 Sidon images; all 14706 fail doubling closure.
* No closure survivors, so no degree-eight validity loop was needed.

The arithmetic counters agree with the code's rejection categories.
This is a code/coverage audit, NOT an independent numerical execution
or formal certificate. The new exclusion remains computer-assisted.

## 3. A fully proved valid non-h0 control

The local III equations and validity alone are compatible. Set
u=1,a=R,d=R^2 with R=33, and take N=24R^2+1=26137. The integer lifts are

    A=(0,33,-66,1089,-2178,1,-64,-4).

All eight points are distinct. They generate the entire odd cyclic
group because 1 belongs to A. N is not divisible by three, so no
order-three difference occurs. Difference 4 occurs as 0-(-4), while
8 and -8 do not occur: sorted low-point gaps are 2,60,4,1,32, and
the two high points are separated from these by much more than eight.
The largest absolute lifted difference is less than N-8, so modular
wrap cannot create difference eight. Thus h>0 by the explicit missing
double 4 -> 8, not by appeal to an unproved h=0 theorem.

### Validity proof

Every eight-term lift sum belongs to [-16R^2,8R^2], an interval of
width N-1. Equality modulo N with the target -R^2-3R-1 is therefore
integer equality. Write k_t for point multiplicities, including k_0.
The formal coefficients at d,a,u satisfy

    k_d-2k_e=-1,
    k_a-2k_b-2k_v=-3,
    k_u+2k_v-4k_w=-1.

These coefficient equations follow without carry: the difference
of the u-coefficient from -1 lies in [-31,17], which contains no
nonzero multiple of 33. After reducing modulo R and dividing, the
difference of the a-coefficient from -3 lies in [-13,11], again
containing no nonzero multiple of R. The d-coefficient then follows.

If k_e>=2, its d-block uses at least five slots. With at most three
slots left, the u-equation forces k_u=k_v=k_w=1, whose a-coefficient
is -2 rather than -3; extra a/b slots would be needed. Hence
k_d=k_e=1 and six slots remain.

Put q=k_w. The u-equation yields k_u=4q-2k_v-1, so q>=1. If q=1,
k_v is zero or one. When zero, k_u=3 and k_a=2k_b-3 require at
least seven slots total outside d/e, impossible. When k_v=1,
k_u=1 and k_a=2k_b-1 force k_a=k_b=1, leaving k_0=1. If q=2,
the six-slot bound forces k_v=3,k_u=1 and no a/b slots; the resulting
a-coefficient is -6 instead of -3. For q>=3 the u/v/w block needs
at least 3q>6 slots. Thus the all-ones multiset is unique.

### Exact quartic fiber at b

The same no-wrap/no-carry argument applies to degree four, now with
target b=-2R. Its coordinate equations are

    k_d=2k_e,       k_a-2k_b-2k_v=-2,
    k_u+2k_v=4k_w.

A nonzero d/e block needs three slots. Its one remaining point must
be b to satisfy the other coordinates, giving 2d+e+b. Otherwise
k_d=k_e=0. If k_w=0, the u-equation forces k_u=k_v=0, and the
a-equation gives either 3*0+b or 2a+2b. If k_w=1, the slot bound
allows k_v=1,k_u=2, giving 2u+v+w. The alternative k_v=2,k_u=0
would need two extra a-points and exceed four slots. Values k_w>=2
need at least six slots.

The entire fiber at b consequently consists of exactly

    3*0+b,       2a+2b,       2d+e+b,       2u+v+w.

The first three are connected by coning the cubic fiber at zero
with b. The last has disjoint support and is isolated. This control
is valid but not h=0, and is NOT a counterexample to any target.
No numerical computation is used in this proof.

## 4. Additional elementary role restriction

In the one-pure core, 3a cannot have a partner 2*0+q. If q is
outside {0,a,b}, coning by b gives the ordinary-center-zero vertex
2*0+q+b at value a, while 3*0+a is another representation at that
same value containing zero. This contradicts ordinary-center exclusion.
If q=0, Stage9 excludes its order-three difference; q=a would give
a=0 by oddness; and q=b gives 5a=0, whence 2b=a=0+a, a forbidden
pair equality. The same argument applies to d and e. This restriction
alone is not an elementary exclusion of III.

## 5. Dependency refinement: every multiway cubic cone is connected

Stage10's numerical four-way exclusion is NOT needed for this
conclusion. Stage9 gives at most one pure mark per fiber. A fiber
with at least four marks therefore contains three nonpure marks;
their centers and singleton labels are disjoint by foreign-center
exclusion. Stage12's no-pure-cone proposition applies to those three
displayed marks even if further marks are present and connects the
ENTIRE quartic fiber for every cone point.

A three-mark no-pure fiber is covered directly by Stage12. A three-
mark one-pure fiber is covered by Stage12's outside-core proof,
Stage13's elementary doubled-center proof and computer-assisted pure-
cone exclusion, and the new Stage14 computer-assisted singleton-cone
exclusion. Thus every cone of a multiway cubic fiber is connected.

This dependency uses Stage9/12 elementary results plus Stage13/14
finite computations. Stage10's KERNEL IMPLEMENTATION is shared; its
four-way zero-survivor theorem is not a logical premise. None of
these statements excludes the cubic triples themselves, proves
R3=0, controls all fresh quartic fibers, or establishes the original
248 bound. Fresh fibers coning no multiway cubic remain the next
separate obstruction.

## 6. Conditional local-defect theorem: independent audit

The entire `stage14_alternative_findings.md` argument was read. Its
conditional theorem is valid with the following exact hypotheses:
validity, eight distinct points in odd H, h=0, Stage9's no-order-three
difference result, and (MC) that every quartic fiber containing a cone
of a multiway repeated cubic is connected. For its contradiction
argument it further assumes only LOCAL conditions on the putatively
fresh fiber X: no isolated ordinary vertex, and injective singleton
labels on U(X), the SET of literal unpaired repeated cubic multisets
obtained by deleting a point from a vertex of X.

Using literal multisets matters: two identical deletions arising from
different vertices are one element of U(X), not two defects. All uses
of duplicate singleton labels in the proof involve distinct centers,
and consequently genuinely distinct cubic multisets.

(MC) implies that every relevant repeated deletion at a fresh X has
fiber size at most two; otherwise its cone is at X. This local fact
gives maximum propagation degree two, while pure pairing and Stage9
give each pure quartic exactly one ordinary neighbor. No global
singleton permutation or bound R3=0 is inferred.

The localized 31/31 argument correctly uses only U(X): 2a+b is an
unpaired deletion of 3a+b, and 2p+b is a deletion of 2p+q+b. If both
were unpaired they would violate local singleton injectivity. Once
2p+b is paired, its cone by q avoids ordinary center p. Among the
remaining points {a,b,q}, 22 is prohibited opposite the other31;
31 centers b,q violate the exhausted order-five coset, and center a
forces q=b; ordinary centers a,b,q each appear in an already known
other vertex; and the only possible pure coned vertex is 4q.
This is the retained pure-quartic option, not a discarded exception.

For two-vertex all-ordinary components, the common tail is the only
shared support point, so the other two deletions are distinct unpaired
marks with that same singleton. In an ordinary-plus-single31 component,
the 31's paired pure deletion forces the shared point to be its
singleton; the remaining deletions again produce precisely such a
local defect. Thus these exclusions use local U(X) injectivity, not
global uniqueness of unpaired labels. The remaining support reductions
and Stage8 algebraic contradiction table use only these local conditions,
ordinary-center exclusion, doubling closure, and the elementary subgroup
lower bound. No additional computation or case census was performed.

The singleton incidence identity is also valid globally without R3=0:
each unordered singleton pair collides exactly once because doubling
bijections center pairs and singleton pairs. A singleton-label defect
therefore forces some cubic fiber with at least three marks, just as
a two-unpaired-marks center defect does. That fiber's value is not
specified. Its cone at X is NOT established by the incidence identity.

Verdict: no proof gap found in the conditional local-defect theorem.
The precise outstanding statement is a transport lemma bringing one
of these forced multiway fibers back to the SAME fresh quartic value,
or an argument directly prohibiting both local defects. It remains
unproved; (MC) alone does not supply it.

### The forced center fiber cannot itself transport back

There is a stronger elementary obstacle to the naive center-transport
step. Let X have isolated ordinary vertex 2a+b+c. For any multiway
cubic fiber with a mark 2a+q, write its value as Y=2a+q. If
X=Y+t for some t in A, then b+c=q+t. Pair uniqueness forces the
literal pair multisets to agree, so q is b or c. But 2a+b and
2a+c are unpaired because the ordinary vertex is isolated. Neither
can belong to a multiway fiber. This is a contradiction.

In fact the argument excludes every paired cubic mark at that same
center from coning to X, not just multiway ones. Consequently the
center-incidence defect's forced multiway fiber cannot be the desired
same-value bridge. Any successful transport must find a DIFFERENT-
center multiway fiber or directly rule out the isolated ordinary.
This restriction is elementary and does not prove global D=0.
