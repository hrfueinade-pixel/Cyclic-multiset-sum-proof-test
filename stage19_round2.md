# Round 2 of 8: every regular quartic cycle is a triangle

Assume validity, eight distinct points, odd cyclic H, h=R3=0.
Stage 17 reduced long cycles to QOOO, QPOO, PPOOO, POPOO,
QPOOP, QPOOO (Q=22, P=31, O=ordinary). This round excludes
all six, with a complete checked finite family of rival identities.

For length L, give consecutive edges the distinct points x_0,...,x_(L-1).
An ordinary vertex is 2y_i+x_(i-1)+x_i, with private center y_i.
A 31 vertex has center at one of these two incident points; a 22
vertex is 2x_(i-1)+2x_i. These encode every incidence orientation,
because equal distinct quartics share at most one occurrence and
three quartics cannot share a point when R3=0. No unused point is
identified with another support point. Use up to eight independent
point symbols, retaining unused points as separate symbols.

Filter only support patterns with the prescribed cycle intersections.
A 31 adjacent to 22 shares its singleton: sharing its center would
give a forbidden squarefree-pair equality. All remaining orientations
are retained, including both orientations when not symmetry-normalized.

For a disjoint ordinary pair 2a+b+c=2d+e+f, h=0 gives
2(a-d)=v-u. Subtraction equates b+c+v to e+f+u.
A squarefree side would contradict validity (literal equality is
impossible on disjoint tails), so v is b or c and u is e or f.
All four roles are included. For a disjoint 31/ordinary pair
3a+b=2d+e+f, the same argument puts v in {a,b}, u in {e,f}.
The choice v=a gives a+u=2d, a forbidden squarefree pair;
thus v=b and both u choices are retained. For disjoint 31s,
Stage 8 Lemma 2.1 supplies 5(a-d)=0; no division by five occurs.

The producer attaches every combination of these necessary relations
to the cycle equalities. Each accepted branch has an eight-term rival
k and an exact integer identity

    2^j*(k-ones) = sum z_i*row_i.

Multiplication by 2 is invertible in odd H, so such an identity
contradicts validity. Rational rowspace by itself is never an exclusion.

Complete branch counts: QOOO 4; QPOO 2; PPOOO 256;
POPOO 256; QPOOP 4; QPOOO 16. All 538 have saved identities,
with no symbolic survivors. Producer COMPLETE in 0.781 seconds
under 60 seconds. Independent checker, with no producer import,
reconstructs incidence models and all role domains, verifies exact
coverage and every certificate, and rejects 1076 altered multiplier
or noninteger-coefficient certificates. Its run completed under 30 seconds.

These calculations were specified before execution as finite cycle-role
checks. They enumerate no modulus or actual sets. Historical Stage 17
length/type reductions remain dependencies, but its numerical checks
were not rerun. All new identities and intermediate roles are preserved
in stage19_cycle_results.json. Separate implementation is verification,
not a formal proof assistant certificate or a separate human review.

**Consequence:** t4=t5=0. The exact target is now I<=29+c2.
This round does not prove that remaining inequality or the full theorem.
Round 2 checkpoint saved.
