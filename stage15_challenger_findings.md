# Stage 15 challenger results, reconstructed from delivered messages

Date: 2026-10-10. The challenger delivered the audits and restrictions
below, then its turn ended with a usage-limit error before saving its
own report. This file is ROOT-WRITTEN reconstruction of those delivered
messages, with the complete proofs checked and recorded by root.
Do not represent it as a successfully completed independent final report
or an independent numerical execution. No computation was performed.

## 1. Independent audit of the order-seven exclusion

The challenger explicitly confirmed the complete proof now saved in
stage15_findings.md, Section 1. Its audited steps were:

* C={0,d,-2d}, order(d)=7, exhausts all six nonzero J differences.
  All remaining five points therefore have distinct nonzero quotient
  images. Three C terms realize every J residue; padding zero gives
  every residue using any number of C slots >=3.
* A different projected five-term B rival lifts with three C slots;
  a shorter or different equal-length squarefree-B replacement lifts
  with 3+k-l C slots. Identical equal-length multisets are NOT prohibited.
* Projected B is valid at length five in the odd quotient. Its 20
  nonzero ordered differences are distinct. Bbar and -Bbar are disjoint
  because a squarefree B pair cannot have quotient sum zero.
* Projected difference weights are 6 at zero, 3+epsilon at the ten signed
  B cosets, 1 at other projected B differences, and zero otherwise.
  Overlap at beta_i occurs exactly when 2 beta_i is another positive B
  point. The reverse overlap with a different second summand would be a
  prohibited shorter squarefree replacement.
* Global doubling closure preserves weights. A negative transition has
  weight three at both ends, so its complete actual fibers are the
  three cross differences. Their equality forces -2C to be a translate
  of C. Since 2C=C+2d, C would be centrally symmetric, contradicting
  pair-sum uniqueness for its three distinct points at odd order.
* Therefore 2Bbar=Bbar, whose summed relation gives sum(Bbar)=0.
  The squarefree five-point set would be replaceable by the empty
  projected multiset, which lifts to an eight-term C-only rival.

Verdict delivered: no gap found. This argument needs no MC, Stage9,
finite enumeration, or external n<=7 computational certification.
The root proof records every identity and all lifting quantifiers.

## 2. Forced-center roles at an isolated ordinary vertex

Let X=2u+v+w be isolated in a fresh quartic fiber. Its two deletion
marks 2u+v and 2u+w are unpaired. The center-incidence identity forces
some cubic fiber Y with at least three marks and a mark 2u+q.
Necessarily q is neither v nor w. The arguments below handle EVERY
available other center/partner of that fiber, not a preferred choice.

Suppose another center c of Y occurs doubled in ANY quartic vertex
opposing the isolated support. Write

    Y=2u+q=2c+b_c, X=2c+R_c,

where R_c is the remaining literal pair. Its two points, including any
repetition, lie outside {u,v,w}. Subtraction gives

    b_c+v+w=q+R_c.

If b_c is neither v nor w, the left is squarefree. It cannot agree
literally with the right: q is neither v nor w, and R_c contains neither.
Validity therefore forces b_c in {v,w}.

For an ordinary opposite vertex R_c is a squarefree pair. Its right
triple can repeat only if q belongs to R_c. For a 31 opposite vertex
R_c={c,r}; the cubic foreign-center rule excludes q=c, so r=q.
If the mark at u is pure (q=u), support separation therefore excludes
both ordinary and 31 opposite centers from this forced cubic.
This does NOT by itself exclude an opposing pure or 22 vertex.

### At most one other center can occur doubled, across all types

Suppose distinct other centers c,d both occur doubled, in one or two
opposing vertices. Their different singleton labels must exhaust v,w:

    Y=2c+v=2d+w,
    X=2c+R_c=2d+R_d.

Consequently R_c+w=R_d+v. If either R pair is squarefree, its triple
with the isolated tail is squarefree and cannot equal the other literal
triple, which lacks that isolated tail. Both R pairs must therefore
be doubles, say R_c=2r and R_d=2s. Oddness and pair uniqueness applied
to X give {c,r}={d,s}. Since c!=d this means r=d,s=c: the two vertices
are actually the SAME 22 multiset, X=2c+2d.

Add the two Y equations:

    2Y=X+v+w=2u+2(v+w).

Odd doubling is invertible, so Y=u+v+w. Comparing Y=2u+q gives
u+q=v+w, a prohibited squarefree-pair replacement. This contradiction
proves that at most ONE other center of Y can occur doubled anywhere
opposite the isolated vertex, including pure and 22 possibilities.

No computation, choice of unique partner, R3=0, or MC was used in this
role bound; it uses validity, oddness and the specified isolation.

## 3. Three coverage cases, not two

With Stage9's at-most-one-pure-mark result, the forced cubic must be
handled in THREE distinct cases:

1. No pure mark, with a nonpure mark 2u+q.
2. One pure mark centered at u, so q=u.
3. One pure mark centered at z!=u, so Y=3z=2u+q.

In case 3, z cannot occur doubled in an opposing quartic vertex:
the preceding necessary label condition would require b_z=z to equal
v or w, but opposite supports exclude both. Equivalently, subtraction
from a vertex X=2z+R yields z+v+w=q+R, a different squarefree triple
on the left. The pure center z may still occur as an ordinary TAIL or
a 31 SINGLETON whose doubled center is outside Y. Do not infer that
z is absent from the whole opposing support.

The one-pure-at-u and one-pure-elsewhere branches must not be merged.
None of these role bounds is a complete exclusion of the defects.

## 4. Fully proved valid non-h0 diagnostic

The no-pure forced-center equations and isolation can genuinely coexist
without global doubling closure. Let R=33, c=R, d=R^2, L=R^3, Y=R^4,
w=4Y-L, and work modulo N=8w+1. Take the integer lifts

    A=(0,c,d,Y,Y-2c,Y-2d,L,w),
    N=37661977.

They are distinct and nonnegative. There is a no-pure cubic triple

    Y=2*0+Y=2c+(Y-2c)=2d+(Y-2d),

and a quartic equality X=4Y=2*0+L+w on disjoint supports.

### Complete validity proof

Every eight-term lift sum is between 0 and 8w<N, so congruence to the
all-ones target 7Y-c-d is integer equality. Denote multiplicities of
Y-2c,Y-2d by k_b,k_e. Base-R coefficient comparison gives

    k_c-2k_b=-1, k_d-2k_e=-1,
    k_L=k_w=r, k_Y+k_b+k_e+4r=7.

To justify no carry, divide by R and reduce modulo R. The first
coefficient's difference from -1 lies in [-15,9], forcing it to zero;
repeat for the d coefficient, then the L coefficient lies in [-8,8],
forcing equality. The Y coefficient then follows exactly.

Put m=k_b+k_e>=2. The c/d blocks use 3m-2 slots, and

    k_Y=7-m-4r, k_0=3-2m+2r.

Nonnegativity of k_0 implies r>=m-1. If m>=3, then
k_Y<=11-5m<0, impossible. Thus m=2, k_b=k_e=1. The two remaining
inequalities force r=1, k_Y=1,k_0=1, and every count is one.
This proves validity without any numerical multiset enumeration.

### Complete quartic fiber proof

Degree-four congruence at 4Y also cannot wrap. The same coefficient
comparison, now at target 4Y, gives

    k_c=2k_b, k_d=2k_e, k_L=k_w=r,
    k_Y+k_b+k_e+4r=4.

With m=k_b+k_e>=0, the four-slot count gives k_0=2r-2m, so r>=m.
Nonnegative k_Y gives m+4r<=4. Hence m=0 and r=0 or1. These produce
exactly the two literal quartics 4Y and 2*0+L+w. They have disjoint
supports, so the ordinary vertex is isolated and this fiber is fresh.

Y is a difference (Y-0), but 2Y is not. Every lift except w is at
most Y; differences among them are at most Y. Differences involving
w are at least w-Y=3Y-L>2Y. Negative differences cannot wrap to 2Y
because N-2Y>w. Thus this is explicitly h>0.

The diagnostic is valid, but NOT a valid h=0 counterexample, NOT a
counterexample to the transport goal or 248, and not evidence that the
necessary constraints can be realized with doubling closure. It rules
out an attempted exclusion using only these local equations and validity.

## 5. Completion and audit boundary

The order-seven audit and role restrictions were delivered before the
challenger's usage-limit failure. The note above was then reconstructed
by root, not emitted as a successful final answer by the challenger.
Root also read the alternative note's complete endpoint and algebraic
case proofs. No agent or root ran a new numerical experiment this round.
MC retains the earlier Stage13/14 computation dependencies. The complete
D=0 and original 248 targets remain open.
