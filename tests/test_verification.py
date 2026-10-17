"""Failure controls for theorem strength, arithmetic, and complete coverage."""

from __future__ import annotations

import contextlib
import copy
import gzip
import hashlib
import importlib.util
import io
from itertools import combinations
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

from verification.core import (
    CASES,
    ROOT,
    VerificationError,
    check_integrity,
    require_orders,
)
from verification.worker import run_order

TEMP_ROOT = ROOT / ".verification" / "test-temporary"
TEMP_ROOT.mkdir(parents=True, exist_ok=True)


def cubic_checker():
    path = ROOT / "verification/checks/cubic_exception.py"
    spec = importlib.util.spec_from_file_location("cubic_controls", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ArithmeticControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.checker = cubic_checker()
        cls.path = (
            ROOT / "certificates/multiplicity/cap-cubic-exception-quartic.json.gz"
        )
        cls.data = json.loads(gzip.decompress(cls.path.read_bytes()))

    def test_growth_threshold_rejects_87_and_88_accepts_89_and_94(self):
        for limit in (87, 88, 89, 94):
            with self.subTest(values=limit), tempfile.TemporaryDirectory(
                dir=TEMP_ROOT
            ) as directory:
                work = Path(directory)
                for name in (
                    "cap-four-pairs-quintic.json.gz",
                    "cap-single-chain-quintic.json.gz",
                ):
                    shutil.copyfile(self.path.parent / name, work / name)
                data = copy.deepcopy(self.data)
                pairs = list(combinations(range(len(data["words"])), 2))
                data["pairs"] = [
                    record for (i, j), record in zip(pairs, data["pairs"]) if j < limit
                ]
                data["words"] = data["words"][:limit]
                (work / self.path.name).write_bytes(
                    gzip.compress(json.dumps(data).encode(), mtime=0)
                )
                original = Path.cwd()
                try:
                    os.chdir(work)
                    with contextlib.redirect_stdout(io.StringIO()):
                        if limit < 89:
                            with self.assertRaises(AssertionError):
                                self.checker.main()
                        else:
                            self.checker.main()
                finally:
                    os.chdir(original)

    def first_pair(self):
        words = [self.checker.decode(w, 4) for w in self.data["words"]]
        for pair, record in zip(combinations(words, 2), self.data["pairs"]):
            a = self.checker.coords(pair[0], "exception3")
            b = self.checker.coords(pair[1], "exception3")
            if any(x != y for x, y in zip(a[:4], b[:4])):
                return pair, record
        raise AssertionError("No free-coordinate fixture")

    def test_changed_sign_and_unauthorized_unit_are_rejected(self):
        pair, record = self.first_pair()
        self.checker.check_pair(*pair, record, "exception3")
        for change in (
            {"multiplier": -record["multiplier"]},
            {"canceled_power_two": 3},
            {"rival": "11111111"},
            {"rival": "00000000"},
        ):
            with self.subTest(change=tuple(change)):
                with self.assertRaises(AssertionError):
                    self.checker.check_pair(*pair, {**record, **change}, "exception3")


class CoverageControls(unittest.TestCase):
    def test_circular_or_missing_mathematical_premises_are_rejected(self):
        from verification.core import check_dependencies

        with tempfile.TemporaryDirectory(dir=TEMP_ROOT) as directory:
            root = Path(directory)
            (root / "certificates").mkdir()
            ledger = {
                "theorem": "finish",
                "claims": [{"id": "finish", "depends_on": ["finish"]}],
            }
            path = root / "certificates/dependencies.json"
            path.write_text(json.dumps(ledger))
            with self.assertRaisesRegex(VerificationError, "Circular"):
                check_dependencies(root)
            ledger["claims"][0]["depends_on"] = ["absent"]
            path.write_text(json.dumps(ledger))
            with self.assertRaisesRegex(
                VerificationError, "Missing mathematical premise"
            ):
                check_dependencies(root)

    def records(self):
        return [
            {
                "case": "two-six",
                "order": m,
                "fingerprint": "fixture",
                "completion": "COMPLETE",
                "report": {"M": m, "completion": "COMPLETE"},
                "survivors": [],
            }
            for m in CASES["two-six"][1]
        ]

    def test_missing_duplicate_and_incomplete_orders_are_rejected(self):
        records = self.records()
        require_orders(records, "two-six", "fixture")
        for broken in (
            records[:-1],
            records[:-1] + [records[0]],
            [{**records[0], "completion": "INCOMPLETE"}] + records[1:],
            [{**records[0], "fingerprint": "different"}] + records[1:],
        ):
            with self.assertRaises(VerificationError):
                require_orders(broken, "two-six", "fixture")

    def test_real_enumerator_zero_budget_is_incomplete(self):
        with tempfile.TemporaryDirectory(dir=TEMP_ROOT) as directory:
            output = Path(directory) / "incomplete.json"
            with contextlib.redirect_stdout(io.StringIO()):
                status = run_order("two-six", 94, 0, output)
            self.assertEqual(status, 2)
            self.assertEqual(json.loads(output.read_text())["completion"], "INCOMPLETE")

    def test_optimized_execution_is_refused(self):
        run = subprocess.run(
            [sys.executable, "-O", str(ROOT / "verify.py"), "--only", "elementary"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(run.returncode, 2)
        self.assertIn("requires assertions", run.stderr)

    def test_missing_or_corrupted_manifest_input_is_rejected(self):
        with tempfile.TemporaryDirectory(dir=TEMP_ROOT) as directory:
            root = Path(directory)
            data = root / "certificates"
            data.mkdir()
            path = data / "witness.json"
            path.write_bytes(b"{}")
            manifest = {
                "files": [
                    {
                        "path": "certificates/witness.json",
                        "bytes": 2,
                        "sha256": hashlib.sha256(b"{}").hexdigest(),
                    }
                ]
            }
            (data / "manifest.json").write_text(json.dumps(manifest))
            check_integrity(root)
            path.write_bytes(b"[]")
            with self.assertRaises(VerificationError):
                check_integrity(root)
            path.unlink()
            with self.assertRaises(VerificationError):
                check_integrity(root)


if __name__ == "__main__":
    unittest.main()
