"""Independent arithmetic and coverage check for the four-pair exclusion.

No imports from inventory, quotient construction, or graph discovery.
Enumerate count compositions; verify every integer/torsion equation,
unimodular coordinate change, cubic-direction orbit, and joint orbit.
"""
import gzip
import itertools
import json
import math
from pathlib import Path


def compositions(n,k=8):
    if k == 1:
        yield (n,)
    else:
        for x in range(n+1):
            for tail in compositions(n-x,k-1):
                yield (x,)+tail


def decode(w,degree):
    assert isinstance(w,str) and len(w) == 8 and w.isascii() and w.isdigit()
    c = tuple(map(int,w))
    assert sum(c) == degree
    return c


def paired(c):
    a,b,c0,d,e,f,g,h = c
    return (a+2*e,b+2*f,c0+2*g,d+2*h)


def evaluate(c,model):
    dimensions = len(model['rows'][0])
    free = tuple(sum(c[i]*model['rows'][i][j] for i in range(8)) for j in range(dimensions))
    torsion = sum(c[i]*model['torsion_rows'][i] for i in range(8)) % model['torsion_order']
    return free,torsion


def difference(a,b,order):
    return tuple(x-y for x,y in zip(a[0],b[0])),(a[1]-b[1]) % order


def check_pair(left,right,record,model,units):
    c = decode(record['rival'],8)
    assert c != (1,)*8
    divisor = record['canceled_unit_factor']
    k = record['multiplier']
    assert isinstance(divisor,int) and divisor > 0
    residue = divisor
    for p in units:
        assert p in (2,3) and math.gcd(p,model['torsion_order']) == 1
        while residue % p == 0:
            residue //= p
    assert residue == 1 and isinstance(k,int) and k != 0
    d = difference(evaluate(left,model),evaluate(right,model),model['torsion_order'])
    f = difference(evaluate(c,model),evaluate((1,)*8,model),model['torsion_order'])
    assert any(d[0]) or d[1]
    assert all(divisor*x == k*y for x,y in zip(f[0],d[0]))
    assert (divisor*f[1]-k*d[1]) % model['torsion_order'] == 0


def check_certificate(data):
    model = data['model']
    if data.get('kind') == 'direct_rival':
        rival = decode(data['rival'],8)
        assert rival != (1,)*8 and evaluate(rival,model) == evaluate((1,)*8,model)
        return {'kind':'direct_rival','pairs':0,'bound':0}
    selected = [decode(w,data['degree']) for w in data['words']]
    assert len(set(selected)) == len(selected) and all(max(w)>1 for w in selected)
    assert len(set(evaluate(w,model) for w in selected)) == len(selected)
    pairs = list(itertools.combinations(selected,2))
    assert len(pairs) == len(data['pairs'])
    for (left,right),record in zip(pairs,data['pairs']):
        check_pair(left,right,record,model,data['units'])
    bad_records = [{**data['pairs'][0],'rival':'00000000'},
                   {**data['pairs'][0],'rival':'11111111'},
                   {**data['pairs'][0],'multiplier':0},
                   {**data['pairs'][0],'canceled_unit_factor':7}]
    rejected = 0
    for bad in bad_records:
        try:
            check_pair(*pairs[0],bad,model,data['units'])
        except AssertionError:
            rejected += 1
    assert rejected == 4
    return {'kind':'growth','pairs':len(pairs),'bound':len(selected),'corruptions_rejected':rejected}


def normal(v):
    first = next(x for x in v if x)
    return tuple(x if first>0 else -x for x in v)


def cubic_class(v):
    while all(x % 2 == 0 for x in v):
        v = tuple(x//2 for x in v)
    return min(tuple(sign*v[i] for i in p) for p in itertools.permutations(range(4)) for sign in (-1,1))


def pair_class(a,b):
    candidates = []
    for permutation in itertools.permutations(range(4)):
        x = normal(tuple(a[i] for i in permutation))
        y = normal(tuple(b[i] for i in permutation))
        candidates.append(tuple(sorted((x,y))))
    return min(candidates)


def det3(m):
    return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
            -m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
            +m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))


def check_single_model(model):
    d = model['direction']
    rows = model['rows']
    torsion = model['torsion_rows']
    order = model['torsion_order']
    assert rows[4:] == [[2*x for x in row] for row in rows[:4]]
    assert all((torsion[i+4]-2*torsion[i]) % order == 0 for i in range(4))
    if d == [-6,0,0,3]:
        assert order == 3 and torsion == [0,0,0,1,0,0,0,2]
        assert rows[:4] == [[1,0,0,0],[0,1,0,0],[0,0,1,0],[2,0,0,0]]
    elif d == [-5,0,0,5]:
        assert order == 5 and torsion == [0,0,0,1,0,0,0,2]
        assert rows[:4] == [[1,0,0,0],[0,1,0,0],[0,0,1,0],[1,0,0,0]]
    elif d == [-6,0,0,5]:
        assert order == 1 and rows[:4] == [[5,0,0,0],[0,1,0,0],[0,0,1,0],[6,0,0,0]]
    else:
        assert order == 1 and torsion == [0]*8
        pivot = next(i for i,x in enumerate(d) if x and abs(x) & (abs(x)-1) == 0)
        others = [i for i in range(4) if i != pivot]
        scale = abs(d[pivot])
        sign = 1 if d[pivot] > 0 else -1
        for j,i in enumerate(others):
            assert rows[i] == [scale if column == j else 0 for column in range(4)]
            assert rows[pivot][j] == -sign*d[i]
        assert rows[pivot][3] == 0
    assert all(sum(d[i]*rows[i][j] for i in range(4)) == 0 for j in range(4))
    assert sum(d[i]*torsion[i] for i in range(4)) % order == 0


def check_joint_model(model):
    left,right = model['relations']
    base = model['first_rows']
    pivot = model['first_unit_pivot']
    scale = model['first_unit_scale']
    assert scale == abs(left[pivot]) and scale & (scale-1) == 0
    others = [i for i in range(4) if i != pivot]
    sign = 1 if left[pivot] > 0 else -1
    for j,i in enumerate(others):
        assert base[i] == [scale if column == j else 0 for column in range(3)]
        assert base[pivot][j] == -sign*left[i]
    vector = [sum(right[i]*base[i][j] for i in range(4)) for j in range(3)]
    assert vector == model['second_after_first'] and any(vector)
    transform = model['unimodular_transform']
    assert abs(det3(transform)) == 1
    diagonal = [sum(vector[k]*transform[k][j] for k in range(3)) for j in range(3)]
    assert diagonal == [math.gcd(*vector),0,0]
    assert diagonal[0] == model['diagonal_gcd']
    order = diagonal[0]
    while order % 2 == 0:
        order //= 2
    assert order == model['torsion_order']
    merged = [[sum(base[i][k]*transform[k][j] for k in range(3)) for j in range(3)] for i in range(4)]
    expected_rows = [[row[1],row[2],0,0] for row in merged]
    expected_torsion = [row[0] % order for row in merged]
    assert model['rows'] == expected_rows+[[2*x for x in row] for row in expected_rows]
    assert model['torsion_rows'] == expected_torsion+[2*x % order for x in expected_torsion]


def check_three_model(model):
    edges = {'triangle':((0,1),(0,2),(1,2)), 'star':((0,1),(0,2),(0,3)),
             'path':((0,1),(1,2),(2,3)), 'split':((0,1),(1,2),(3,4))}
    kind = model['id'][3:]
    assert kind in edges and model['edges'] == list(map(list,edges[kind]))
    assert model['torsion_order'] == 1 and model['torsion_rows'] == [0]*8
    tails = [[0]*5]+[[2 if column == i else 0 for column in range(5)] for i in range(4)]
    expected = tails+[[((tails[a][j]+tails[b][j])//2 if j<4 else 1) for j in range(5)] for a,b in edges[kind]]
    assert model['rows'] == expected
    # Three-edge simple graphs on five vertices exhaust these four types.
    ordinary = []
    for index,(a,b) in enumerate(edges[kind]):
        word = [int(i not in (a,b)) for i in range(5)]+[2 if i == index else 0 for i in range(3)]
        ordinary.append(tuple(word))
    assert len(set(evaluate(c,model) for c in ordinary)) == 1


def read_certificates():
    bundle = Path('stage43_certificates.json.gz')
    if bundle.exists():
        return json.loads(gzip.decompress(bundle.read_bytes()))['certificates']
    return {path.name:json.loads(gzip.decompress(path.read_bytes()))
            for path in Path('.').glob('stage43_*_certificate.json.gz')}


def main():
    inventory = json.loads(Path('stage43_fourpair_inventory_results.json').read_text())
    cubic = {paired(c) for c in compositions(3) if max(c)>1}
    assert len(cubic) == inventory['formal_cubic_values'] == 58
    classes = {cubic_class(tuple(x-y for x,y in zip(a,b))) for a,b in itertools.combinations(cubic,2)}
    recorded = {tuple(row['direction']):row for row in inventory['classes']}
    assert classes == set(recorded)
    permitted = []
    for d,row in recorded.items():
        if row['direct_rival'] is None:
            permitted.append(d)
        else:
            rival = tuple(row['direct_rival']['rival'])
            assert len(rival) == 8 and min(rival)>=0 and sum(rival) == 8 and rival != (1,)*8
            k = row['direct_rival']['multiplier']
            assert k != 0 and tuple(x-3 for x in paired(rival)) == tuple(k*x for x in d)
    assert set(permitted) == set(map(tuple,inventory['permitted_classes'])) and len(permitted) == 16
    certificates = read_certificates()
    checks = {}
    singles = {}
    for name,data in sorted(certificates.items()):
        model = data['model']
        if model['id'].startswith('r'):
            check_single_model(model)
            if data.get('degree') == 4:
                singles[tuple(model['direction'])] = data
        elif model['id'].startswith('j'):
            check_joint_model(model)
        else:
            check_three_model(model)
        checks[name] = check_certificate(data)
    assert set(singles) == set(permitted)
    remaining = {d for d,data in singles.items() if len(data['words'])<89}
    assert remaining == {(-4,0,0,1),(-5,0,1,4),(-4,-1,1,4)}
    for d in remaining:
        model = singles[d]['model']
        formal_cubics = {evaluate(c,model) for c in compositions(3) if max(c)>1}
        assert len(formal_cubics) == (54 if d == (-4,0,0,1) else 57)
    # Explicitly check the retained Stage 42 bounds used in the rank argument.
    inherited = []
    for name,minimum in [('stage42_doubling4_degree5_certificate.json.gz',135),
                         ('stage42_pairchain_degree5_certificate.json.gz',142)]:
        old = json.loads(gzip.decompress(Path(name).read_bytes()))
        if old['model'] == 'doubling4':
            rows = [[int(i%4 == j)*(1 if i<4 else 2) for j in range(4)] for i in range(8)]
        else:
            centers = [[1,0,0,0],[4,0,0,0],[0,1,0,0],[0,0,1,0]]
            rows = centers+[[2*x for x in row] for row in centers]
        converted = {'model':{'rows':rows,'torsion_rows':[0]*8,'torsion_order':1},
                     'degree':old['degree'],'units':old['units'],'words':old['words'],
                     'pairs':[{**p,'canceled_unit_factor':p['canceled_power_two']} for p in old['pairs']]}
        result = check_certificate(converted)
        assert result['bound']>=minimum
        inherited.append(result)
    joint = json.loads(Path('stage43_joint_relations_results.json').read_text())
    directions = {normal(tuple(d[i] for i in p)) for d in remaining for p in itertools.permutations(range(4))}
    assert len(directions) == joint['direction_count'] == 48
    expected_pairs = {pair_class(a,b) for a,b in itertools.combinations(directions,2)}
    models = {tuple(map(tuple,m['relations'])):m for m in joint['models']}
    assert set(models) == expected_pairs and len(models) == 57
    for pair,model in models.items():
        a,b = pair
        assert any(a[i]*b[j] != a[j]*b[i] for i in range(4) for j in range(i))
        filename = f"stage43_{model['id']}_degree4_units2_certificate.json.gz"
        assert certificates[filename]['model'] == model
        result = checks[filename]
        assert result['kind'] == 'direct_rival' or result['bound'] >= 89
    graph_types = set()
    edges = list(itertools.combinations(range(5),2))
    for triple in itertools.combinations(edges,3):
        degrees = [sum(i in edge for edge in triple) for i in range(5)]
        graph_types.add(tuple(sorted(degrees)))
    assert graph_types == {(0,0,2,2,2),(0,1,1,1,3),(0,1,1,2,2),(1,1,1,1,2)}
    output = {'cubic_formal_values':58,'cubic_direction_classes':len(classes),
              'permitted_classes':16,'quartic_excluded_single_classes':13,
              'remaining_direction_types':3,'actual_oriented_directions':48,
              'joint_raw_pairs':math.comb(48,2),'joint_orbits_verified':57,
              'joint_direct_rivals':sum(checks[f"stage43_{m['id']}_degree4_units2_certificate.json.gz"]['kind']=='direct_rival' for m in models.values()),
              'joint_growth_certificates':sum(checks[f"stage43_{m['id']}_degree4_units2_certificate.json.gz"]['kind']=='growth' for m in models.values()),
              'new_positive_pair_records':sum(row['pairs'] for row in checks.values()),
              'inherited_pair_records_rechecked':sum(row['pairs'] for row in inherited),
              'fourpair_exclusion_verified':True,
              'boundary':'Computer-assisted proof for the four-doubling-pair family only. Same-author independent implementation; general odd N>=248 theorem remains open.'}
    Path('stage43_certificate_check_results.json').write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(output,indent=2))


if __name__ == '__main__':
    main()
