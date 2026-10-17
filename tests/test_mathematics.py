"""Small exhaustive oracles; none assumes an eight-point theorem at n=6,7."""

from collections import Counter, defaultdict
from itertools import combinations, combinations_with_replacement, permutations
from math import comb, gcd
from pathlib import Path
import importlib
import sys
import unittest

from verification import independent as I
from verification.parity import (
    affine_preimages,
    extend_sumsets,
    normalized_roots,
    rotate,
    sumsets,
    valid_extension,
)


def brute_valid(points, modulus):
    return (
        sum(
            sum(w) % modulus == sum(points) % modulus
            for w in combinations_with_replacement(points, len(points))
        )
        == 1
    )


def brute_levels(points, degree, modulus):
    return [
        sum(
            1 << x
            for x in {
                sum(w) % modulus for w in combinations_with_replacement(points, d)
            }
        )
        for d in range(degree + 1)
    ]


class ParityOracles(unittest.TestCase):
    def test_sumsets_extension_and_validity_against_multisets(self):
        for m in range(3, 17):
            for size in range(1, 4):
                for tail in combinations(range(1, m), size - 1):
                    points = (0,) + tail
                    levels = brute_levels(points, 8, m)
                    self.assertEqual(sumsets(points, 8, m), levels)
                    if not brute_valid(points, m):
                        continue
                    for x in range(m):
                        if x in points:
                            continue
                        self.assertEqual(
                            valid_extension(points, levels, x, m),
                            brute_valid(points + (x,), m),
                        )
                        self.assertEqual(
                            extend_sumsets(levels, x, m),
                            brute_levels(points + (x,), 8, m),
                        )

    def test_all_nonunit_preimages_and_rotations(self):
        for m in range(3, 19):
            masks = {0, (1 << m) - 1, sum(1 << x for x in range(0, m, 2))}
            masks.update(1 << x for x in range(m))
            for mask in masks:
                preimage = affine_preimages(mask, m)
                for c in range(m):
                    self.assertEqual(
                        rotate(mask, c, m),
                        sum(1 << ((x + c) % m) for x in range(m) if mask >> x & 1),
                    )
                    for a in (-1, 1, 2, 3):
                        self.assertEqual(
                            preimage(a, c),
                            sum(
                                1 << x
                                for x in range(m)
                                if mask >> ((a * x + c) % m) & 1
                            ),
                        )
        self.assertEqual(affine_preimages(1, 6)(3, 0), 0b010101)

    def test_normalization_covers_unitless_and_subgroup_cases(self):
        samples = [(m, p) for m in range(3, 19) for p in combinations(range(m), 3)]
        samples += [(30, (0, 6, 10, 15)), (30, (0, 6, 12)), (105, (0, 15, 35, 42))]
        for m, points in samples:
            if any(2 * (a - b) % m == 0 for a, b in combinations(points, 2)):
                continue
            primitive = gcd(m, *(a - points[0] for a in points)) == 1
            for primitive_mode in (False, True) if primitive else (False,):
                roots = normalized_roots(m, primitive_mode)
                unit_pair = any(gcd(a - b, m) == 1 for a, b in combinations(points, 2))
                images = [
                    tuple(sorted(u * (x - o) % m for x in points))
                    for o in points
                    for u in range(1, m)
                    if gcd(u, m) == 1
                ]
                self.assertTrue(
                    any(
                        0 in image and r in image and (r == 1 or not unit_pair)
                        for image in images
                        for r in roots
                    )
                )

    def test_validity_invariance_and_heredity(self):
        for m in range(3, 19):
            for points in combinations(range(m), 3):
                valid = brute_valid(points, m)
                self.assertEqual(
                    valid, brute_valid(tuple((x + 2) % m for x in points), m)
                )
                for u in range(1, m):
                    if gcd(u, m) == 1:
                        self.assertEqual(
                            valid, brute_valid(tuple(u * x % m for x in points), m)
                        )
                if valid:
                    for sub in combinations(points, 2):
                        self.assertTrue(brute_valid(sub, m))

    def test_antipodal_projection_and_full_lift_domain(self):
        for m in range(4, 19, 2):
            for size in (3, 4):
                for points in combinations(range(m), size):
                    if not brute_valid(points, m):
                        continue
                    pairs = [
                        (a, b)
                        for a, b in combinations(points, 2)
                        if (a - b) % m == m // 2
                    ]
                    self.assertLessEqual(len(pairs), 1)
                    if pairs:
                        projected = tuple(sorted({x % (m // 2) for x in points}))
                        self.assertEqual(len(projected), size - 1)
                        self.assertTrue(brute_valid(projected, m // 2))
        # Build the lift domain by subsets upstairs, rather than by choosing
        # a duplicated fiber and binary offsets as the production checker does.
        for m in range(3, 10):
            for quotient in combinations(range(m), 3):
                actual = {
                    a
                    for a in combinations(range(2 * m), 4)
                    if tuple(sorted({x % m for x in a})) == quotient
                }
                expected = set()
                for duplicate in quotient:
                    rest = [x for x in quotient if x != duplicate]
                    for a in (rest[0], rest[0] + m):
                        for b in (rest[1], rest[1] + m):
                            expected.add(
                                tuple(sorted((duplicate, duplicate + m, a, b)))
                            )
                self.assertEqual(actual, expected)


class CountingOracles(unittest.TestCase):
    def test_split_source_presentations_cover_all_physical_frames(self):
        from verification.checks.assignment_base import presentations

        expected = set()
        for x, y, z, a, b, c, d, e in permutations(range(8)):
            if {x, z} != {0, 2} and {y, z} != {0, 2}:
                continue
            indices = ((x, x, c, d, e), (y, y, a, d, e), (z, z, a, b, c))
            expected.add(
                tuple(sorted(tuple(w.count(i) for i in range(8)) for w in indices))
            )
        fibers, roots = presentations((0, 2))
        self.assertEqual(set(fibers), expected)
        self.assertEqual(len(expected), 720)
        self.assertEqual(len(roots), 2880)

    def test_pair_lifts_as_words_for_six_seven_and_eight(self):
        # These examples test general lift identities. They neither prove the
        # minima 60,124 nor extend eight-specific caps or midpoint arguments.
        for n in (6, 7, 8):
            points = tuple(2**i - 1 for i in range(n))
            modulus = 2**n - 1
            self.assertTrue(brute_valid(points, modulus))
            pairs, disjoint = {}, {}
            for d in (3, 4, 5):
                fibers = defaultdict(list)
                for center in range(n):
                    for tails in combinations(
                        [i for i in range(n) if i != center], d - 2
                    ):
                        word = tuple(2 * (i == center) + (i in tails) for i in range(n))
                        fibers[
                            sum(w * a for w, a in zip(word, points)) % modulus
                        ].append((center, set(tails)))
                equal = [p for fiber in fibers.values() for p in combinations(fiber, 2)]
                pairs[d] = len(equal)
                disjoint[d] = sum(not a[1] & b[1] for a, b in equal)
                for a, b in equal:
                    self.assertNotIn(a[0], b[1])
                    self.assertNotIn(b[0], a[1])
            self.assertEqual(pairs[4], (n - 4) * pairs[3] + disjoint[4])
            self.assertEqual(
                pairs[5],
                comb(n - 4, 2) * pairs[3] + (n - 6) * disjoint[4] + disjoint[5],
            )

    def test_all_tail_graphs_and_common_tail_inverse(self):
        kinds = Counter()
        for omitted in combinations(list(combinations(range(5), 2)), 3):
            tails = [set(range(5)) - set(e) for e in omitted]
            common = set.intersection(*tails)
            degrees = tuple(sorted(Counter(i for e in omitted for i in e).values()))
            kinds[degrees] += 1
            if degrees == (1, 1, 2, 2):  # path: exactly one common tail
                self.assertEqual(len(common), 1)
                removed = [t - common for t in tails]
                self.assertEqual(
                    tuple(sorted(Counter(i for e in removed for i in e).values())),
                    degrees,
                )
                self.assertEqual([e | common for e in removed], tails)
            if degrees == (1, 1, 1, 1, 2):
                self.assertFalse(common)
        self.assertEqual(sum(kinds.values()), 120)
        self.assertEqual(len(kinds), 4)


class CertificateFailureControls(unittest.TestCase):

    def test_fractional_rival_rejected_even_when_its_cleared_row_holds(self):
        from verification.checks import assignment_base as B, split_sources as S

        points = (0, 1, 3, 7, 15, 31, 63, 127)
        self.assertTrue(brute_valid(points, 255))
        row = (2, -1, -2, 1, 0, 0, 0, 0)
        self.assertEqual(sum(a * b for a, b in zip(points, row)) % 255, 0)
        witness = {
            "kind": "mass_eight_rival",
            "word": [2, 0.5, 0, 1.5, 1, 1, 1, 1],
            "factor": 2,
            "multipliers": [1],
        }
        with self.assertRaises(AssertionError):
            B.check_witness((row,), set(), witness)
        with self.assertRaises(AssertionError):
            S.check_exclusion((row,), witness)

    def test_determinant_one_rational_matrix_is_not_unimodular(self):
        from verification.checks import alignment_forests as F, triangle_ownership as O
        from verification.checks import split_sources as S, quintic_cap as Q

        fractional = [[1, 0.5, 0], [0, 1, 0], [0, 0, 1]]
        for determinant in (F.determinant, O.determinant, S.determinant, Q.det3):
            with self.subTest(checker=determinant.__module__), self.assertRaises(
                AssertionError
            ):
                determinant(fractional)

    def test_quartic_growth_requires_the_right_degree_units_and_threshold(self):
        from verification.checks.quintic_cap import require_quartic_contradiction

        good = {"degree": 4, "units": [2]}
        require_quartic_contradiction(good, {"kind": "growth", "bound": 89})
        for data, bound in (
            (good, 88),
            ({"degree": 5, "units": [2]}, 89),
            ({"degree": 4, "units": [2, 3]}, 89),
        ):
            with self.assertRaises(AssertionError):
                require_quartic_contradiction(data, {"kind": "growth", "bound": bound})

    def test_conditional_credit_cannot_be_accepted_as_a_contradiction(self):
        path = str(Path(__file__).resolve().parents[1] / "verification/checks")
        sys.path.insert(0, path)
        try:
            checker = importlib.import_module("two_triangle_exclusion")
        finally:
            sys.path.remove(path)
        value = lambda w: I.evaluate(w, self.model())
        checker.require_ordinary_refinement({"reason": "P9"}, value)
        for reason in ("credit", "conditional_quintic", "robust_count", None):
            with self.assertRaisesRegex(AssertionError, "conditional"):
                checker.require_ordinary_refinement({"reason": reason}, value)

    def model(self):
        return {
            "rows": [list(row) for row in I.BASE],
            "torsion_matrix": [[] for _ in range(8)],
            "torsion_orders": [],
        }

    def test_missing_duplicate_and_invalid_symmetry_branches(self):
        m = self.model()
        expected = I.private_directions(m)
        # Empty child constraints make the symmetry failure, rather than an
        # unrelated implication, the only invalid part of this fixture.
        cases = [
            {
                "direction": list(d),
                "node": 0,
                "reduction": {
                    "right": [[int(i == j) for j in range(5)] for i in range(5)],
                    "rank": 0,
                    "odd_diagonals": [],
                },
            }
            for d in sorted(expected)
        ]
        nodes = [{"constraints": []}]
        I.validate_branches(m, cases, nodes)
        for broken in (cases[:-1], cases + [cases[0]]):
            with self.assertRaisesRegex(AssertionError, "branch"):
                I.validate_branches(m, broken, nodes)
        broken = [dict(c) for c in cases]
        broken[0]["permutation"] = [3, 1, 2, 0, 4]
        with self.assertRaisesRegex(AssertionError, "symmetry"):
            I.validate_branches(m, broken, nodes)
        broken[0].pop("permutation")
        broken[0]["reduction"]["right"][0][1] = 0.5
        with self.assertRaisesRegex(AssertionError, "integral"):
            I.validate_branches(m, broken, nodes)

    def test_odd_torsion_cannot_be_canceled(self):
        rows = [[3, 0, 0, 0, 0]]
        r = {
            "rank": 1,
            "D": rows,
            "right": [[int(i == j) for j in range(5)] for i in range(5)],
        }
        I.check_cyclic_surjectivity(rows, r, 3)
        r["D"] = [[1, 0, 0, 0, 0]]
        with self.assertRaisesRegex(AssertionError, "lost"):
            I.check_cyclic_surjectivity(rows, r, 3)


if __name__ == "__main__":
    unittest.main()
