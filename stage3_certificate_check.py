"""Independent small checker for the eight N=187 difference templates.

No imports from the template generator, clique search, or hereditary search.
Reconstructs each delta arithmetically, checks supplied colorings, then
enumerates every six-subset directly, without search pruning.
"""

from itertools import combinations
import json
from math import comb
from pathlib import Path


def reconstruct(a, mask):
    n = 187
    length = 28 - 5 * a - 4 * mask.bit_count()
    delta = {sign * pow(94, j, n) % n
             for j in range(length) for sign in (-1, 1)}
    if a:
        delta.update(17 * k for k in range(1, 11))
    for i, start in enumerate((11, 33)):
        if mask & (1 << i):
            delta.update(start * pow(2, j, n) % n for j in range(8))
    assert len(delta) == 56
    assert {(-x) % n for x in delta} == delta
    assert sum(2 * x % n not in delta for x in delta) == 2
    return delta


def check_templates(path):
    saved = json.loads(Path(path).read_text(encoding="ascii"))
    assert saved["N"] == 187
    indexed = {(r["a"], r["mask"]): r for r in saved["templates"]}
    assert len(saved["templates"]) == len(indexed) == 8
    records = []
    for a in (0, 1):
        for mask in range(4):
            delta = reconstruct(a, mask)
            row = indexed[a, mask]
            assert row["delta"] == sorted(delta)
            vertices = [x for x in range(2, 187)
                        if x in delta and (x - 1) % 187 in delta]
            assert vertices == row["plain"]["candidate_vertices"]
            edges = {(x, y) for x, y in combinations(vertices, 2)
                     if (x - y) % 187 in delta}
            certificate = row["five_color_certificate"]
            color_count = None
            if certificate is not None:
                assert certificate["vertices"] == vertices
                colors = certificate["colors"]
                assert len(colors) == len(vertices)
                assert all(type(c) is int and 0 <= c < 5 for c in colors)
                assigned = dict(zip(vertices, colors))
                assert all(assigned[x] != assigned[y] for x, y in edges)
                color_count = len(set(colors))
            tested = 0
            cliques = []
            for candidate in combinations(vertices, 6):
                tested += 1
                if all(pair in edges for pair in combinations(candidate, 2)):
                    cliques.append(candidate)
            assert tested == comb(len(vertices), 6)
            assert not cliques
            records.append({"a": a, "mask": mask,
                            "vertices": len(vertices), "edges": len(edges),
                            "verified_coloring_colors": color_count,
                            "six_subsets_checked": tested,
                            "six_cliques": len(cliques)})
    return {"N": 187, "independent_template_checks": records,
            "total_six_subsets_checked": sum(r["six_subsets_checked"] for r in records),
            "verified_coloring_certificates": sum(r["verified_coloring_colors"] is not None
                                                  for r in records),
            "all_templates_excluded_by_direct_six_subset_check": True}


def inspect_complete_search(path, modulus):
    row = json.loads(Path(path).read_text(encoding="ascii"))
    assert row["N"] == modulus and row["n"] == 8
    assert row["status"] == "COMPLETE" and row["complete_search"] is True
    assert row["initial"] == [0, 1]
    assert row["first_extension_min"] is None
    assert row["first_extension_max"] is None
    assert not row["accepted_sets"]
    assert row["visited_valid_prefixes_by_size"][8] == 0
    assert len(row["fully_completed_first_extension_branches"]) == \
        row["visited_valid_prefixes_by_size"][3]
    return {"N": modulus, "observed_status": row["status"],
            "elapsed_seconds": row["elapsed_seconds"],
            "visited_prefixes_by_size": row["visited_valid_prefixes_by_size"],
            "finished_third_coordinate_branches": len(row["fully_completed_first_extension_branches"]),
            "accepted_sets": len(row["accepted_sets"]),
            "search_was_independently_rerun": False}


def main():
    result = check_templates("stage3_187_template_certificates.json")
    result["observed_completed_search_records"] = [
        inspect_complete_search("stage3_search_187_complete.json", 187),
        inspect_complete_search("stage3_search_188.json", 188)]
    print(json.dumps(result, indent=2))
    Path("stage3_independent_certificate_result.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="ascii")


if __name__ == "__main__":
    main()
