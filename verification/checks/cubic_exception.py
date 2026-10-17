"""Check positive Stage 42 witnesses without importing their producer.

The equation is checked after MULTIPLYING by the claimed power of two;
only the group's oddness is used to cancel it. The exception's last
coordinate is reduced modulo three and is never divided by three.
"""

import gzip
import itertools
import json
from pathlib import Path


def decode(text, degree):
    assert (
        isinstance(text, str) and len(text) == 8 and text.isascii() and text.isdigit()
    )
    result = tuple(map(int, text))
    assert sum(result) == degree
    return result


def coords(word, model):
    a, b, c, d, e, f, g, h = word
    if model == "exception3":
        return (c - 2 * d, e - 2 * f, g, h, b % 3)
    paired = (a + 2 * e, b + 2 * f, c + 2 * g, d + 2 * h)
    if model == "doubling4":
        return paired + (0,)
    if model == "pairchain":
        return (paired[0] + 4 * paired[1], paired[2], paired[3], 0, 0)
    if model == "twochains":
        return (paired[0] + 4 * paired[1], paired[2] + 4 * paired[3], 0, 0, 0)
    if model == "chain3":
        return (sum((x * w for x, w in zip(paired, (1, 4, 16, 64)))), 0, 0, 0, 0)
    raise AssertionError("Unknown model")


def check_pair(left, right, record, model):
    c = decode(record["rival"], 8)
    assert c != (1,) * 8
    factor = record["canceled_power_two"]
    multiplier = record["multiplier"]
    assert isinstance(factor, int) and factor > 0 and (factor & factor - 1 == 0)
    assert isinstance(multiplier, int) and multiplier != 0
    d = tuple((x - y for x, y in zip(coords(left, model), coords(right, model))))
    f = tuple((x - y for x, y in zip(coords(c, model), coords((1,) * 8, model))))
    assert any(d[:4]) or d[4] % 3
    assert all((factor * f[i] == multiplier * d[i] for i in range(4)))
    assert (factor * f[4] - multiplier * d[4]) % 3 == 0


def check_file(path):
    with gzip.open(path, "rt", encoding="utf-8") as stream:
        data = json.load(stream)
    assert data["units"] == [2]
    assert data["torsion_order"] == (3 if data["model"] == "exception3" else 1)
    selected = [decode(word, data["degree"]) for word in data["words"]]
    assert all((max(word) >= 2 for word in selected))
    assert len(set(selected)) == len(selected)
    assert len(set((coords(word, data["model"]) for word in selected))) == len(selected)
    pairs = list(itertools.combinations(selected, 2))
    assert len(pairs) == len(data["pairs"])
    for (left, right), record in zip(pairs, data["pairs"]):
        check_pair(left, right, record, data["model"])
    rejected = 0
    first = data["pairs"][0]
    for bad in ("00000000", "11111111"):
        try:
            check_pair(*pairs[0], {**first, "rival": bad}, data["model"])
        except AssertionError:
            rejected += 1
    try:
        check_pair(*pairs[0], {**first, "multiplier": 0}, data["model"])
    except AssertionError:
        rejected += 1
    for j in range(8):
        bad = "".join(("8" if i == j else "0" for i in range(8)))
        try:
            check_pair(*pairs[0], {**first, "rival": bad}, data["model"])
        except AssertionError:
            rejected += 1
    assert rejected >= 4
    return {
        "file": path.name,
        "model": data["model"],
        "degree": data["degree"],
        "distinct_repeated_values": len(selected),
        "pair_witnesses_checked": len(pairs),
        "corruptions_rejected": rejected,
    }


def main():
    required = [
        "cap-cubic-exception-quartic.json.gz",
        "cap-four-pairs-quintic.json.gz",
        "cap-single-chain-quintic.json.gz",
    ]
    results = [check_file(Path(name)) for name in required]
    assert results
    exception = [r for r in results if r["model"] == "exception3" and r["degree"] == 4]
    assert len(exception) == 1 and exception[0]["distinct_repeated_values"] >= 89
    output = {
        "certificates": results,
        "total_pair_witnesses": sum((r["pair_witnesses_checked"] for r in results)),
        "boundary": "Separate arithmetic implementation, not human or formal review. The exception3 quartic threshold certifies its sub-248 fiber exclusion; other entries certify positive model bounds only.",
    }
    Path("cubic-exception-report.json").write_text(
        json.dumps(output, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
