"""Tests for the gate's handling of git-ignored paths: the linter walks the working tree, so a folder `.gitignore` excludes (the queue's live-only
`completed/`) used to be reported as a content folder with no entry point and its documents were counted. The gate now drops findings and document
rows about ignored paths; tracked paths and everything else are judged as before.

Run: python3 -m unittest discover -s _tools_/lint-gate
"""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

from test_lint_gate import GateCase, HAVE_REFLECTION, doc, HERE

sys.path.insert(0, str(HERE))
import lint_gate  # noqa: E402

IGNORED = "_queue_/completed/unit-1.md"


@unittest.skipUnless(HAVE_REFLECTION, "the reflection linter is not installed")
class IgnoredFolders(GateCase):
    def setUp(self):
        super().setUp()
        self.write("_queue_/INDEX.md", "# queue\n")
        self.write(".gitignore", "completed/\n")
        self.run_git("add", "-A")
        self.run_git("commit", "-q", "--no-verify", "-m", "queue and ignore rule")

    def documents(self):
        r = self.gate("watch", "--format", "json", "--no-write")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        data = json.loads(r.stdout[r.stdout.index("{"):r.stdout.rindex("}") + 1])
        return data

    def test_an_ignored_folder_without_an_index_is_no_finding_in_the_base_form(self):
        self.write(IGNORED, doc(50, "Unit"))
        r = self.gate("check", "--base", "HEAD")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertNotIn("entry-points", r.stdout)
        self.assertNotIn("completed", r.stdout)

    def test_the_same_folder_not_ignored_is_still_blocked(self):
        self.write(IGNORED, doc(50, "Unit"))
        (self.repo / ".gitignore").write_text("# nothing ignored\n")
        r = self.gate("check", "--base", "HEAD")
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("BLOCKED [entry-points] _queue_/completed: no entry point", r.stdout)

    def test_a_tracked_file_in_a_folder_the_pattern_matches_is_not_ignored(self):
        self.write(IGNORED, doc(50, "Unit"))
        self.run_git("add", "-f", IGNORED)                                                  # tracked: git no longer calls it ignored
        r = self.gate("check", "--base", "HEAD")
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("BLOCKED [entry-points] _queue_/completed", r.stdout)

    def test_an_oversized_ignored_document_is_neither_blocked_nor_counted(self):
        self.write(IGNORED, doc(600, "Big unit"))
        r = self.gate("check", "--base", "HEAD")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertNotIn("document-concision", r.stdout)
        watched = self.documents()
        self.assertNotIn(IGNORED, [row["path"] for row in watched["top"]])
        self.assertEqual(watched["new_errors_total"], 0)

    def test_watch_leaves_the_ignored_documents_out_of_the_census(self):
        before = self.documents()
        self.write(IGNORED, doc(450, "Unit"))
        self.write("_queue_/completed/unit-2.md", doc(450, "Unit two"))
        after = self.documents()
        self.assertEqual(after["documents"], before["documents"])
        self.assertEqual(after["by_top_folder"].get("_queue_", {}).get("documents"), before["by_top_folder"].get("_queue_", {}).get("documents"))

    def test_the_staged_form_is_unchanged(self):
        self.write(IGNORED, doc(50, "Unit"))
        self.write("_records_/2026-11-22/legacy-activity/0200-ok-run.md", doc(50, "Real"))
        self.run_git("add", "_records_/2026-11-22/legacy-activity/0200-ok-run.md")
        r = self.gate("check", "--staged")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)


class IgnoredAmong(unittest.TestCase):
    def test_tracked_untracked_and_nested_names(self):
        tmp = Path(tempfile.mkdtemp(prefix="ignored-among-"))
        self.addCleanup(__import__("shutil").rmtree, tmp, True)
        import subprocess
        subprocess.run(["git", "init", "-q", str(tmp)], check=True)
        (tmp / ".gitignore").write_text("completed/\n*.tmp\n")
        (tmp / "_queue_/completed").mkdir(parents=True)
        (tmp / "_queue_/completed/u.md").write_text("x")
        (tmp / "_queue_/keep.md").write_text("x")
        (tmp / "scratch.tmp").write_text("x")
        names = {"_queue_/completed", "_queue_/completed/u.md", "_queue_/keep.md", "scratch.tmp", "../outside.md", "/abs.md", ""}
        self.assertEqual(lint_gate.ignored_among(tmp, names), {"_queue_/completed", "_queue_/completed/u.md", "scratch.tmp"})

    def test_a_directory_that_is_not_a_repository_ignores_nothing(self):
        tmp = Path(tempfile.mkdtemp(prefix="not-a-repo-"))
        self.addCleanup(__import__("shutil").rmtree, tmp, True)
        self.assertEqual(lint_gate.ignored_among(tmp, {"a.md", "b/c.md"}), set())
        self.assertEqual(lint_gate.ignored_among(tmp, set()), set())

    def test_drop_ignored_removes_only_the_ignored_rows_and_leaves_a_clean_report_as_it_was(self):
        tmp = Path(tempfile.mkdtemp(prefix="drop-ignored-"))
        self.addCleanup(__import__("shutil").rmtree, tmp, True)
        import subprocess
        subprocess.run(["git", "init", "-q", str(tmp)], check=True)
        (tmp / ".gitignore").write_text("completed/\n")
        (tmp / "_q_/completed").mkdir(parents=True)
        clean = {"errors": ["_q_/x: no entry point [entry-points]"], "document_budgets": {"documents": [{"path": "_q_/x.md", "body_words": 3}]}, "other": 1}
        self.assertIs(lint_gate.drop_ignored(tmp, clean), clean)
        mixed = {"errors": ["_q_/x: no entry point [entry-points]", "_q_/completed: no entry point [entry-points]"],
                 "document_budgets": {"documents": [{"path": "_q_/x.md", "body_words": 3}, {"path": "_q_/completed/u.md", "body_words": 9}], "keep": 1},
                 "other": 1}
        out = lint_gate.drop_ignored(tmp, mixed)
        self.assertEqual(out["errors"], ["_q_/x: no entry point [entry-points]"])
        self.assertEqual(out["document_budgets"], {"documents": [{"path": "_q_/x.md", "body_words": 3}], "keep": 1})
        self.assertEqual(out["other"], 1)
        self.assertEqual(len(mixed["errors"]), 2)                                          # the input report is not modified


if __name__ == "__main__":
    unittest.main()
