# Stage 33: odd five-block reduction and a precise search obstruction

Saved checkpoint, 2026-10-10. This round supplies a complete necessary
shape reduction for the odd h>0 branch. Its180-second search timed
out at191 after completing189, and is INCONCLUSIVE for all later
orders. The completed189 report is not independently certified here.

## Coverage

Any eight-set in N<248 has128 distinct subset sums, so its difference
subgroup is the whole cyclic group: a proper subgroup has order at
most123. Odd N<=247 has at most three distinct prime factors. Translate
one point to0 and choose, for each prime divisor, one point not
divisible by that prime. At most four selected points, including0,
generate the whole group; fill to a primitive five-subset B. Validity
of B is hereditary. It has distinct ordered differences in odd order.

For at most two primes, the elementary unit-difference lemma supplies
a pair normalizable to0,1. At three-prime orders, ALL divisor roots
0,g are included, retaining only unitless prefixes for g>1. Units act
transitively on elements with the same gcd with N. Thus every relevant
primitive B is covered, including the possible unitless case.

## Every opposing triple shape, then the base

Write the other three points as C=c+D, D={0,u,v},0<u<v,c+v<N.
Put s=sum B and z=u+v. For q=5 terms from B, uniqueness forces every
one of the nine repeated cubic deviations of D into

    G={s-r:r NOT in5B}.

These are the six differences and -u-v,2u-v,2v-u. All are enumerated
before computing any triple base. For q=6,7,8, necessary conditions are

    c in intersection over r in2D of (complement(6B)-s-z+r),
    2c in intersection over d in D of (complement(7B)-s-z+d),
    3c in complement(8B)-s-z.

If6P already fills the group for a prefix P, adding points keeps6B
full because0 remains, and the q=6 condition is impossible. Exact
copy-count prefix validity and this sumset pruning retain every valid B.
Only actual disjoint eight-point candidates need the distinct-difference
and remaining q=0..4 checks. Those exact checks preserve eight-term
rival identities or an actual surviving A for direct certification.

## What completed, and why pivot

The raw normalized search completed189:637838 primitive B blocks and
3795864 triple shapes, with zero bases surviving q=6/7/8. It then
timed out during191; partial counts remain in
stage33_odd_five_three_results.json. The empty rival archive is
stage33_rivals.json.gz. No global odd exclusion follows from this run.

The obstruction is duplicated affine five-block representatives:
many ordered unit-pair normalizations describe the same block and
repeat the complete complementary-triple calculation. Stage36 keeps
the least normalized unit-pair representative, transforms C along
with B, and retains all unitless roots. This is a coverage-preserving
pivot with a measurable runtime target, not another unbounded sweep.
The separate required milestone, self-contained seven-point exclusion,
is handled in Stages34 and35 while this odd route is developed.
