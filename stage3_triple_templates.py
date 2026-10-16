"""Exact N=187 difference-template checks derived from cubic slack.

This is not a generic search over moduli. Eight explicit templates suffice
by the independently audited orbit argument in stage3_audit_notes.md.
All operations are exact integer/set/bitset computations.
"""

from itertools import combinations
import json
from pathlib import Path
from time import monotonic

from research_experiments import collision, cube


def doubling_orbits(n):
    unseen = set(range(1, n))
    result = []
    while unseen:
        value = min(unseen)
        orbit = []
        while value not in orbit:
            orbit.append(value)
            value = 2 * value % n
        assert value == orbit[0]
        unseen.difference_update(orbit)
        result.append(tuple(orbit))
    return result


def templates():
    n = 187
    orbits = doubling_orbits(n)
    order11 = next(set(o) for o in orbits if len(o) == 10)
    order17 = [set(o) for o in orbits if len(o) == 8]
    assert len(order17) == 2 and sum(len(o) == 40 for o in orbits) == 4
    inverse2 = pow(2, -1, n)
    for a in (0, 1):
        for mask in range(4):
            b = mask.bit_count()
            length = 28 - 5 * a - 4 * b
            units = {sign * pow(inverse2, j, n) % n
                     for j in range(length) for sign in (-1, 1)}
            delta = set(units)
            if a:
                delta.update(order11)
            for i in range(2):
                if mask & (1 << i):
                    delta.update(order17[i])
            assert len(delta) == 56 and {(-d) % n for d in delta} == delta
            assert sum((2 * d) % n not in delta for d in delta) == 2
            yield {"a": a, "mask": mask, "b": b, "unit_interval_length": length}, delta


def clique_scan(delta, target=8, sidon=False):
    n = 187
    vertices = sorted(x for x in delta if x != 1 and (x - 1) % n in delta)
    adjacency = [sum(1 << j for j, y in enumerate(vertices)
                     if x != y and (x - y) % n in delta) for x in vertices]
    nodes = [0] * 9
    witnesses = []
    largest = (0, 1)

    def visit(chosen, available, differences):
        nonlocal largest
        nodes[len(chosen)] += 1
        if len(chosen) > len(largest):
            largest = chosen
        if len(chosen) == target:
            witnesses.append(chosen)
            return
        if len(chosen) + available.bit_count() < target:
            return
        while available:
            bit = available & -available
            available ^= bit
            index = bit.bit_length() - 1
            value = vertices[index]
            new_differences = [(value - x) % n for x in chosen]
            new_differences += [(-d) % n for d in new_differences]
            if sidon and (len(set(new_differences)) != len(new_differences)
                          or differences.intersection(new_differences)):
                continue
            visit(chosen + (value,), available & adjacency[index],
                  differences | set(new_differences))

    visit((0, 1), (1 << len(vertices)) - 1, {1, 186})
    return {"candidate_vertices": vertices, "nodes_by_depth": nodes,
            "eight_point_cliques": len(witnesses), "witnesses": witnesses,
            "largest_visited_clique": largest}


def color_certificate(delta, limit=5):
    """A proper five-coloring excludes six extra vertices beside 0 and 1."""
    n = 187
    vertices = sorted(x for x in delta if x != 1 and (x - 1) % n in delta)
    neighbors = [{j for j, y in enumerate(vertices)
                  if x != y and (x - y) % n in delta} for x in vertices]
    colors = [-1] * len(vertices)

    def assign():
        if all(c >= 0 for c in colors):
            return True
        uncolored = [i for i, c in enumerate(colors) if c < 0]
        i = max(uncolored, key=lambda j:
                (len({colors[k] for k in neighbors[j] if colors[k] >= 0}),
                 len(neighbors[j])))
        forbidden = {colors[j] for j in neighbors[i] if colors[j] >= 0}
        used = max(colors) + 1
        for c in range(min(limit, used + 1)):
            if c in forbidden:
                continue
            colors[i] = c
            if assign():
                return True
        colors[i] = -1
        return False

    if not assign():
        return None
    return {"vertices": vertices, "colors": colors, "color_limit": limit}


def check_color_certificate(delta, certificate):
    n = 187
    vertices = certificate["vertices"]
    colors = certificate["colors"]
    expected = sorted(x for x in delta if x != 1 and (x - 1) % n in delta)
    if vertices != expected or len(colors) != len(vertices):
        return False
    if not all(isinstance(c, int) and 0 <= c < 5 for c in colors):
        return False
    return all(colors[i] != colors[j]
               for i, x in enumerate(vertices)
               for j, y in enumerate(vertices[:i]) if (x - y) % n in delta)


def main():
    start = monotonic()
    records = []
    for description, delta in templates():
        plain = clique_scan(delta)
        sidon = clique_scan(delta, sidon=True)
        checked = []
        for a in sidon["witnesses"]:
            sums = cube(a[1:], 187)
            witness = collision(a, 187)
            checked.append({"A": a, "cube_size": len(sums) if sums else None,
                            "rival": witness})
        record = {**description, "delta": sorted(delta), "plain": plain,
                  "sidon": sidon, "direct_checks": checked}
        certificate = color_certificate(delta)
        record["five_color_certificate"] = certificate
        if certificate is not None:
            assert check_color_certificate(delta, certificate)
        records.append(record)
        print(json.dumps(record))
    print(json.dumps({"templates_checked": len(records), "elapsed_seconds": monotonic() - start,
                      "complete_template_search": True,
                      "all_sidon_template_exclusions": all(r["sidon"]["eight_point_cliques"] == 0 for r in records)}))
    output = {"N": 187, "templates": records,
              "all_five_colored": all(r["five_color_certificate"] is not None for r in records)}
    Path("stage3_187_template_certificates.json").write_text(
        json.dumps(output, indent=2) + "\n", encoding="ascii")


if __name__ == "__main__":
    main()
