"""Failure controls for portable manuscript links, discovery and release binding."""

from copy import deepcopy
import gzip
import hashlib
import io
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tarfile
import tempfile
import textwrap
import unittest
from unittest.mock import patch

from verification import book, regeneration, release


class PublicationWorkflow(unittest.TestCase):
    def test_first_release_and_existing_tag_guards_use_the_real_publish_script(self):
        workflow = (book.ROOT / ".github/workflows/verify.yml").read_text()
        script = textwrap.dedent(workflow.rsplit("        run: |\n", 1)[1])
        sha = "a" * 40
        mock_cli = textwrap.dedent(
            r"""
            import json, os, sys
            from pathlib import Path
            args = sys.argv[1:]
            mode = os.environ['TEST_MODE']
            sha = os.environ['GITHUB_SHA']
            state = Path('created.json')
            with open('events.jsonl', 'a') as log:
                log.write(json.dumps(args) + '\n')
            if args[:2] == ['release', 'view']:
                sys.exit(0 if mode == 'existing-release' else 1)
            if args[0] == 'api' and '/git/ref/tags/' in args[1]:
                print('tag-object' if mode in ['correct-tag', 'wrong-tag'] else 'null')
                sys.exit(0 if mode in ['correct-tag', 'wrong-tag'] else 1)
            if args[0] == 'api' and '/commits/' in args[1]:
                if state.exists() or mode == 'correct-tag':
                    print(sha)
                    sys.exit(0)
                print('b' * 40 if mode == 'wrong-tag' else 'null')
                sys.exit(0 if mode == 'wrong-tag' else 1)
            if args[:2] == ['release', 'create']:
                state.write_text(json.dumps(args))
                print('https://example.invalid/review-release')
                sys.exit(0)
            raise SystemExit('Unexpected CLI call: ' + repr(args))
        """
        )
        for mode in ["missing-tag", "correct-tag", "wrong-tag", "existing-release"]:
            with self.subTest(mode=mode), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                cli = root / "gh"
                cli.write_text("#!" + sys.executable + "\n" + mock_cli)
                cli.chmod(0o755)
                (root / "review-package").mkdir()
                (root / "review-package/release.json").write_text(
                    json.dumps(
                        {
                            "status": "Test fixture",
                            "source_commit": sha,
                            "source_manifest_sha256": "m" * 64,
                        }
                    )
                )
                env = {
                    **os.environ,
                    "PATH": directory + os.pathsep + os.environ["PATH"],
                    "GITHUB_SHA": sha,
                    "GITHUB_REF": "refs/heads/review/releases/v0.1.0-review.1",
                    "REVIEW_VERSION": "v0.1.0-review.1",
                    "GITHUB_REPOSITORY": "example/review",
                    "RUNNER_TEMP": directory,
                    "TEST_MODE": mode,
                }
                result = subprocess.run(
                    ["bash", "-e"],
                    input=script,
                    cwd=root,
                    env=env,
                    text=True,
                    capture_output=True,
                )
                created = root / "created.json"
                if mode in ["missing-tag", "correct-tag"]:
                    self.assertEqual(result.returncode, 0, result.stderr)
                    args = json.loads(created.read_text())
                    self.assertEqual(args[args.index("--target") + 1], sha)
                    self.assertIn("--prerelease", args)
                else:
                    self.assertNotEqual(result.returncode, 0)
                    self.assertFalse(created.exists())


class ManuscriptLinks(unittest.TestCase):
    def fixture(self, root):
        for name in book.SOURCES:
            path = root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(
                "# Chapter\n\n"
                + "\n\n".join(
                    f"## Lemma {n}. Test\n\nLemma 6 and Lemmas 7–9."
                    for n, file in book.LEMMA_FILES.items()
                    if file == name
                )
            )
        p = root / "PROOF.md"
        p.write_text(p.read_text() + "\n[counting](proof/counting.md#lemma-6-test)\n")

    def test_cross_file_and_bare_lemma_references_reach_real_targets(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.fixture(root)
            text = book.manuscript(root, "a" * 40, "b" * 64)
            targets = set(re.findall(r"\{#([^}]+)\}", text))
            links = set(re.findall(r"\]\(#([^)]+)\)", text))
            self.assertLessEqual(links, targets)
            self.assertIn("[counting](#lemma-6)", text)
            self.assertEqual(
                {f"lemma-{n}" for n in range(1, 17)} & targets,
                {f"lemma-{n}" for n in range(1, 17)},
            )

    def test_unknown_heading_is_not_silently_changed_to_external_link(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.fixture(root)
            path = root / "PROOF.md"
            path.write_text(path.read_text() + "\n[bad](proof/counting.md#missing)\n")
            with self.assertRaisesRegex(ValueError, "Unresolved PDF heading"):
                book.manuscript(root, "a" * 40, "b" * 64)


class HistoricalRecovery(unittest.TestCase):
    def test_missing_or_reordered_parts_and_changed_bytes_fail(self):
        entry = {
            "path": "certificates/test.json.gz",
            "source_files": ["stage60.gz.part000", "stage60.gz.part001"],
            "transformation": "exact concatenation",
            "sha256": hashlib.sha256(b"AB").hexdigest(),
        }
        load = {"stage60.gz.part000": b"A", "stage60.gz.part001": b"B"}.__getitem__
        self.assertEqual(regeneration.recover_payload(entry, load), b"AB")
        for names in [
            ["stage60.gz.part001", "stage60.gz.part000"],
            ["stage60.gz.part001"],
        ]:
            with self.assertRaises(ValueError):
                regeneration.recover_payload({**entry, "source_files": names}, load)
        with self.assertRaisesRegex(ValueError, "hash mismatch"):
            regeneration.recover_payload({**entry, "sha256": "0" * 64}, load)

    def test_incomplete_reference_rows_never_supply_order_coverage(self):
        rows = [{"M": n, "completion": "COMPLETE"} for n in range(94, 124)]
        self.assertEqual(
            len(
                json.loads(
                    regeneration.completed_reference([json.dumps({"reports": rows})])
                )["reports"]
            ),
            30,
        )
        rows[-1]["completion"] = "RUNNING"
        with self.assertRaisesRegex(ValueError, "30 required orders"):
            regeneration.completed_reference([json.dumps({"reports": rows})])

    def test_generator_cannot_reuse_a_stale_parent_certificate(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            output = root / ".verification/output"
            output.mkdir(parents=True)
            (output / "old.json.gz").write_bytes(gzip.compress(b"{}"))
            producer = b"pass\n"
            catalog = {
                "archive_commit": "a" * 40,
                "program_sha256": {
                    "stage41_probe.py": hashlib.sha256(producer).hexdigest()
                },
            }
            recipe = {
                "id": "test",
                "required_values": 89,
                "scripts": ["stage41_probe.py"],
                "program": "stage41_probe.py",
                "model": "test",
                "degree": 4,
                "units": [2],
                "schema": "stage41",
                "certificate": "certificates/old.json.gz",
            }
            with patch.object(regeneration, "archive_blob", return_value=producer):
                record = regeneration.generate_one(root, output, catalog, recipe, 10)
            self.assertEqual(record["status"], "INCOMPLETE")
            self.assertNotIn("validation", record)

    def test_wrong_recovered_program_is_rejected_before_execution(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            program = root / "stage41_probe.py"
            program.write_text("raise RuntimeError('must not execute')")
            recipe = {"id": "test", "required_values": 89, "scripts": [program.name]}
            catalog = {
                "archive_commit": "a" * 40,
                "program_sha256": {program.name: "0" * 64},
            }
            with patch.object(
                regeneration.subprocess,
                "run",
                side_effect=AssertionError("Executed altered generator"),
            ):
                record = regeneration.generate_one(
                    root, root / "output", catalog, recipe, 10, root
                )
            self.assertEqual(record["status"], "INCOMPLETE")
            self.assertIn("hash mismatch", record["error"])


class ReleaseBinding(unittest.TestCase):
    def evidence(self):
        return {
            "exit_code": 0,
            "manifest_sha256": "m",
            "summary": {
                "scope": "full",
                "status": "FULL_CHECKS_PASSED",
                "manifest_sha256": "m",
                "parity": {
                    "required_order_checks": 150,
                    "completed_order_checks": 150,
                    "reused_completed_orders": 0,
                },
                "failure_controls": "PASSED",
                "privacy": "PASSED",
            },
        }

    def test_partial_resumed_or_cross_source_evidence_cannot_ship(self):
        good = self.evidence()
        release.evidence_check(good, "m")
        for key, value in [
            ("status", "LIMITED_PHASE_PASSED"),
            ("manifest_sha256", "different"),
        ]:
            bad = deepcopy(good)
            bad["summary"][key] = value
            with self.assertRaises(ValueError):
                release.evidence_check(bad, "m")
        for key, value in [
            ("completed_order_checks", 149),
            ("reused_completed_orders", 1),
        ]:
            bad = deepcopy(good)
            bad["summary"]["parity"][key] = value
            with self.assertRaises(ValueError):
                release.evidence_check(bad, "m")

    def test_dirty_or_cross_commit_pdf_cannot_ship(self):
        pdf = b"%PDF-test"
        report = {
            "kind": "typeset-proof",
            "source_commit": "c",
            "dirty_preview": False,
            "source_manifest_sha256": "m",
            "pdf_sha256": hashlib.sha256(pdf).hexdigest(),
        }
        release.pdf_check(pdf, report, "c", "m")
        for key, value in [
            ("dirty_preview", True),
            ("source_commit", "other"),
            ("pdf_sha256", "other"),
        ]:
            with self.assertRaises(ValueError):
                release.pdf_check(pdf, {**report, key: value}, "c", "m")

    def test_one_successful_recipe_cannot_masquerade_as_complete_regeneration(self):
        catalog = {
            "archive_commit": "a",
            "program_sha256": {"stage41.py": "h"},
            "recipes": [
                {
                    "id": str(n),
                    "required_values": 89,
                    "scripts": ["stage41.py"],
                    "certificate": f"certificates/{n}.json.gz",
                }
                for n in range(7)
            ],
        }
        rows = [
            {
                "recipe": str(n),
                "status": "POSITIVE_CERTIFICATE_VERIFIED",
                "certificate": f"{n}.json.gz",
                "work_directory": f"recipe-{n}",
                "validation": {"forced_distinct_repeated_values": 89},
                "scripts": {"stage41.py": "h"},
            }
            for n in range(7)
        ]
        report = {
            "status": "COMPLETE",
            "source_manifest_sha256": "m",
            "archive_commit": "a",
            "recipes": rows,
        }
        release.generation_check(report, catalog, "m")
        for incomplete in [rows[:1], rows[:-1] + [rows[0]]]:
            with self.assertRaises(ValueError):
                release.generation_check(
                    {**report, "recipes": incomplete}, catalog, "m"
                )

    def test_changed_payload_fails_even_when_a_bundle_can_be_opened(self):
        version = "v0.1.0-review.1"
        metadata = {
            "format": 1,
            "prerelease": True,
            "version": version,
            "source_commit": "c",
            "files": {
                "proof.pdf": {
                    "bytes": 9,
                    "sha256": hashlib.sha256(b"%PDF-test").hexdigest(),
                }
            },
        }
        files = {
            "proof.pdf": b"%PDF-evil",
            "release.json": json.dumps(metadata).encode(),
            "SHA256SUMS": b"",
        }
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "review.tar.gz"
            prefix = f"cyclic-multiset-sums-{version}/"
            path.write_bytes(
                release.tar_bytes({prefix + k: v for k, v in files.items()}, 0)
            )
            with self.assertRaisesRegex(ValueError, "content changed"):
                release.verify_bundle(path, "c")

    def test_archive_paths_and_links_are_rejected_without_extraction(self):
        for name, kind in [
            ("../../escape", tarfile.REGTYPE),
            ("safe", tarfile.SYMTYPE),
        ]:
            stream = io.BytesIO()
            with tarfile.open(fileobj=stream, mode="w") as archive:
                info = tarfile.TarInfo(name)
                info.type = kind
                archive.addfile(info, io.BytesIO(b""))
            with self.assertRaises(ValueError):
                release.read_tar(stream.getvalue())

    def test_review_versions_exclude_stable_or_injected_names(self):
        self.assertEqual(release.version_check("v0.1.0-review.1"), "v0.1.0-review.1")
        for value in ["v1.0.0", "../v0.1.0-review.1", "v0.1.0-review.1\nother"]:
            with self.assertRaises(ValueError):
                release.version_check(value)


if __name__ == "__main__":
    unittest.main()
