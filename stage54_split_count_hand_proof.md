# Stage 54: a fixed cubic pair supports at most four genuine splits

2026-10-12. Elementary counting for the full odd N<248 proof. This lemma is independent of the source-triple computation and requires no computer search or cancellation by an odd prime.

## Lemma

Fix an ordinary cubic word pair

    2x+c = 2y+a,

where all four labels are distinct. A genuine quintic split descending to this pair has the form

    2x+c+d+e = 2y+a+d+e = 2z+a+b+c,

where z,b,d,e are precisely the other four physical labels. Let their sum be R. Since d+e=R-z-b, the second source relation gives

    2x+R-z-b = 2z+a+b,
    3z+2b = 2x+R-a.

For each possible third center z, the last equality determines at most one b, because multiplication by TWO is injective in an odd group. Then the unordered pair d,e is recovered as the other two labels. The split output and its word fiber are therefore recovered uniquely. There are four possible choices of z, so the fixed ordinary cubic pair supports at most four genuine split outputs.

Every genuine split has exactly one word pair whose two common tail labels can be deleted to give an ordinary cubic pair. Hence globally

    q <= 4 P3ordinary.

No division by three is used. The result allows reused labels and outputs between different cubic pairs; the unique descent prevents counting a split twice.

## A global consequence that forces further cubic relations

For quartic triangles, the elementary recoverable lift count gives 3t<=4P3ordinary: each triangle has three cubic pair descents, and each fixed cubic pair has four possible one-label quartic lifts.

In the inherited small-order setting, the number O4 of ordinary quartic values is 168-P4+C4 <=88. Thus

    P4 >=80+C4,       S4=P4-4P3ordinary,
    C4=t+2c+p+w,      S4=p+2w+E.

Therefore

    E >=80+t+2c-w-4P3ordinary.

Substitute this into the Stage48 bound

    2N >=496+2k+2c-5t+5w-4q+E

to obtain

    N >=288+k+2c+2w-2(t+q+P3ordinary).             (COUNT)

Let Ptotal be the number of unordered equal pairs among all 64 repeated cubic marks, including pure cubes. Ordered-difference uniqueness gives Ptotal=28-h. The exact cubic formula gives k=h+R3=28-Ptotal+R3, and P3ordinary<=Ptotal.

If Ptotal<=5, the two incidence bounds and COUNT imply

    N >=316-11Ptotal-2 floor(4Ptotal/3)+R3
      >=316-55-12=249.

This contradicts odd N<248. Hence every remaining counterexample needs at least SIX cubic collision pairs.

The exact source-path model from stage54_source_triple_probe.py has sixty formal repeated cubic values: four pair collisions and no multiway fiber. Without any new cubic equality, Ptotal=4, so COUNT already excludes it. Each of the six first-cubic residual models has 59 formal repeated cubic values, with exactly five pair collisions and no multiway fiber. Unless a further formally new cubic equality occurs, Ptotal=5 and COUNT excludes that model as well.

This supplies the mathematical premise for the complete second-cubic inventory. It does not declare an incomplete inventory, weak growth bound or timeout an exclusion. The full N>=248 theorem and the remaining C4>0 allocation are still open until every required branch is closed.
