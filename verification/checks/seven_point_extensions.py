"""Independent finite survivor and extension audit; five-second cap."""

from pathlib import Path
from itertools import combinations_with_replacement
from time import monotonic
import json

start = monotonic()
cap = 5
producer = json.loads(Path("seven-point-survivors.json").read_text())
auditor = json.loads(Path("seven-point-reference.json").read_text())
extensions = json.loads(Path("seven-point-extensions.json").read_text())
assert (
    producer["completion"]
    == auditor["completion"]
    == extensions["completion"]
    == "COMPLETE"
)
p = {(r["M"], tuple(r["B"])): r["missing_7B"] for r in producer["survivors"]}
a = {(r["M"], tuple(r["B"])): r["missing"] for r in auditor["survivors"]}
assert p == a and len(p) == 58
checked = []
for row in extensions["extensions"]:
    if monotonic() - start >= cap:
        raise TimeoutError("Audit incomplete")
    m = row["M"]
    b = tuple(row["B"])
    target = sum(b) % m
    rivals = [v for v in combinations_with_replacement(b, 6) if sum(v) % m == target]
    assert rivals == [b]
    missing = sorted(
        set(range(m)) - {sum(v) % m for v in combinations_with_replacement(b, 7)}
    )
    assert missing == p[m, b] == [row["missing_7B"]]
    x = (missing[0] - target) % m
    assert x == row["seventh_point"]
    if x in b:
        assert row["outcome"] == "REPEATED POINT"
    else:
        points = sorted(b + (x,))
        counts = row["rival_counts"]
        assert points == row["A"] and row["outcome"] == "EXPLICIT SEVEN-TERM RIVAL"
        assert len(counts) == 7 and all((isinstance(c, int) and c >= 0 for c in counts))
        assert sum(counts) == 7 and counts != [1] * 7
        assert sum(((c - 1) * z for c, z in zip(counts, points))) % m == 0
        all_targets = [
            v
            for v in combinations_with_replacement(points, 7)
            if sum(v) % m == sum(points) % m
        ]
        assert len(all_targets) > 1
    checked.append([m, list(b), x, row["outcome"]])
assert len(checked) == 58 and {(r[0], tuple(r[1])) for r in checked} == set(p)
out = {
    "completion": "COMPLETE",
    "cap_seconds": cap,
    "elapsed_seconds": monotonic() - start,
    "checked": checked,
    "six_sets": 58,
    "possible_seventh_points": 58,
    "valid_seven_survivors": 0,
    "imports_producer": False,
    "method": "Direct degree-six and degree-seven multiset enumeration",
}
Path("seven-point-extensions-report.json").write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps({k: v for k, v in out.items() if k != "checked"}))
