"""Direct small positive controls for the independent modular kernel solver."""

from itertools import product
from math import gcd
import json
from pathlib import Path

from stage10_modular_audit import adjugate, local_projective_kernel


def canonical(x, modulus, prime):
    first = next(i for i, value in enumerate(x) if value % prime)
    unit = pow(x[first], -1, modulus)
    return tuple(unit * value % modulus for value in x)


def main():
    diagonal_cases = ((9, 1), (3, 3), (9, 3), (9, 9))
    records = []
    vectors_checked = 0
    for a, b in diagonal_cases:
        diagonal = ((a, 0, 0, 0), (0, b, 0, 0),
                    (0, 0, 1, 0), (0, 0, 0, 1))
        # Column additions and permutations preserve the presentation but
        # move unit coordinates away from the first coordinate.
        mixed = tuple((row[2], row[0] + row[1], row[3] + row[0], row[1])
                      for row in diagonal)
        for matrix in (diagonal, mixed):
            _, cols = adjugate(matrix)
            for exponent in (1, 2):
                n = 3 ** exponent
                expected = set()
                for x in product(range(n), repeat=4):
                    vectors_checked += 1
                    if gcd(n, *x) != 1:
                        continue
                    if all(sum(c * v for c, v in zip(row, x)) % n == 0
                           for row in matrix):
                        expected.add(canonical(x, n, 3))
                actual, _ = local_projective_kernel(matrix, cols, 3, exponent)
                assert len(actual) == len(set(actual))
                assert set(actual) == expected, (matrix, n, actual, expected)
                records.append({"matrix": matrix, "modulus": n,
                                "primitive_unit_orbits": len(actual)})
    result = {"vectors_checked": vectors_checked,
              "complete_fixed_controls": True, "controls": records,
              "scope": "Sixteen fixed small matrix/modulus checks; not a set search."}
    Path("stage10_kernel_control_results.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(json.dumps({"vectors_checked": vectors_checked,
                      "complete_fixed_controls": True,
                      "orbit_counts": [r["primitive_unit_orbits"] for r in records]}))


if __name__ == "__main__":
    main()
