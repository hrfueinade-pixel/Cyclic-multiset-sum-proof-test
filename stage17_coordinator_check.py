"""Independent integer audit of Stage 17 torsion and global certificates.

Checks saved matrices, adjugates, fixed signed-doubling arithmetic, and
the global producer's saved eight-coordinate integer identities.
No kernel imports, candidate sets, modulus sweep, or historical reruns.
The structural group/rook arguments are proved in the research reports.
"""
import json
from pathlib import Path


def determinant(matrix):
    a, b, c = matrix
    return (a[0] * (b[1] * c[2] - b[2] * c[1])
            - a[1] * (b[0] * c[2] - b[2] * c[0])
            + a[2] * (b[0] * c[1] - b[1] * c[0]))


def adjugate(matrix):
    result = []
    for i in range(3):
        row = []
        for j in range(3):
            minor = [[matrix[r][s] for s in range(3) if s != i]
                     for r in range(3) if r != j]
            row.append((-1) ** (i + j) *
                       (minor[0][0] * minor[1][1] - minor[0][1] * minor[1][0]))
        result.append(row)
    return result


def valid_adjugate(matrix, candidate, det):
    return all(sum(matrix[i][k] * candidate[k][j] for k in range(3))
               == (det if i == j else 0) for i in range(3) for j in range(3))


def signed_orbit(modulus):
    powers = []
    value = 1
    while value not in powers:
        powers.append(value)
        value = 2 * value % modulus
    assert value == 1
    return powers, sorted(set(powers) | {-x % modulus for x in powers})


def valid_global_certificate(record):
    rows, coefficients = record['rows'], record['integer_coefficients']
    rival, power = record['rival'], record['power_of_two']
    if type(power) is not int or power < 0 or len(rows) != len(coefficients):
        return False
    if any(type(z) is not int for z in coefficients):
        return False
    if (len(rival) != 8 or any(type(n) is not int or n < 0 for n in rival)
            or sum(rival) != 8 or rival == [1] * 8):
        return False
    if any(len(row) != 8 or any(type(n) is not int for n in row)
           or sum(row) != 0 for row in rows):
        return False
    return all((1 << power) * (rival[j] - 1)
               == sum(z * row[j] for z, row in zip(coefficients, rows))
               for j in range(8))


def main():
    directory = Path(__file__).resolve().parent
    data = json.loads((directory / 'stage17_local_results.json').read_text(encoding='utf-8'))
    assert data['complete'] and not data['timed_out']
    entries = data['rank_forcing_survivors']
    assert len(entries) == 6
    matrices = []
    for entry in entries:
        matrix = entry['rows']
        det = determinant(matrix)
        candidate = adjugate(matrix)
        assert det and valid_adjugate(matrix, candidate, det)
        corrupted = [row[:] for row in candidate]
        corrupted[0][0] += 1
        assert not valid_adjugate(matrix, corrupted, det)
        matrices.append({'parent_roles': entry['parent_roles'],
                         'partner_role': entry['partner_role'],
                         'rows': matrix, 'determinant': det, 'adjugate': candidate})
    assert [abs(item['determinant']) for item in matrices] == [503, 489, 501, 483, 549, 531]
    arithmetic = {}
    for prime in (503, 163, 167, 61, 59):
        assert all(prime % d for d in range(2, int(prime ** .5) + 1))
        powers, signed = signed_orbit(prime)
        assert len(signed) > 56
        arithmetic[str(prime)] = {'prime': True, 'doubling_order': len(powers),
                                  'signed_orbit_size': len(signed),
                                  'doubling_powers': powers, 'signed_orbit': signed}
    for det, prime in ((503, 503), (489, 163), (501, 167), (549, 61), (531, 59)):
        assert det % prime == 0 and det // prime <= 9
    powers, signed = signed_orbit(161)
    assert len(powers) == 33 and len(signed) == 66
    divisors = [d for d in range(1, 484) if 483 % d == 0]
    assert max(d for d in divisors if d % 7 or d % 23) == 69
    global_data = json.loads((directory / 'stage17_global_results.json').read_text(encoding='utf-8'))
    assert global_data['completed'] and not global_data['timed_out']
    records = global_data['certificates']
    assert len(records) == 194
    for record in records:
        assert valid_global_certificate(record)
        corrupted = dict(record)
        coefficients = record['integer_coefficients'][:]
        index = next(i for i, row in enumerate(record['rows']) if any(row))
        coefficients[index] += 1
        corrupted['integer_coefficients'] = coefficients
        assert not valid_global_certificate(corrupted)
        coefficients[index] = 1 / 3
        assert not valid_global_certificate(corrupted)
    result = {'scope': 'six saved full-rank matrices, fixed torsion arithmetic, and 194 global certificates',
              'completion': 'COMPLETE', 'matrix_checks': matrices,
              'corrupted_adjugates_rejected': 6, 'prime_arithmetic': arithmetic,
              'mod_161': {'doubling_order': 33, 'signed_orbit_size': 66,
                          'doubling_powers': powers, 'signed_orbit': signed},
              'divisors_483': divisors,
              'global_certificate_audit': {'accepted': len(records),
                                           'corrupted_coefficients_rejected': len(records),
                                           'noninteger_coefficients_rejected': len(records),
                                           'imports_global_producer': False},
              'limits': ['This checks integer arithmetic, not a census of groups or sets.',
                         'The group generation and rook-clique coverage are elementary report proofs.']}
    (directory / 'stage17_coordinator_results.json').write_text(
        json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print('COMPLETE: six adjugates, fixed orbit arithmetic, 194 global certificates and 388 rejection tests.')


if __name__ == '__main__':
    main()
