"""Tests for the pre-merge-commit hook, the shrink-only exempt list and exempt-prune. All names, patterns and documents are
made up in a throwaway repository; the real denylist is never read.

Run: python3 -m unittest discover -s _tools_/lint-gate
"""
from __future__ import annotations

import os
import re
import subprocess
import sys
import unittest

from test_lint_gate import HERE, doc
from test_privacy import PrivacyCase

NAME = "Zorvane Quill"                         # made up
BIG = "_activities_/legacy-profile/INDEX.md"
SMALL = "_activities_/small-profile/INDEX.md"


class MergeCase(PrivacyCase):
    def setUp(self):
        super().setUp()
        self.deny(["# made-up", "# marker: owner account", r"zorvane\s+quill"])
        self.write(BIG, doc(650, "Legacy").rstrip("\n") + f"\n\nThe owner is {NAME} here.\n")
        self.write(SMALL, doc(50, "Small"))
        self.run_git("add", "-A")
        self.run_git("commit", "-q", "--no-verify", "-m", "legacy oversized profile and a small one")
        self.assertEqual(self.gate("install").returncode, 0)

    def head(self):
        return self.run_git("rev-parse", "HEAD").stdout.strip()

    def read(self, rel):
        return (self.repo / rel).read_text()

    def feature(self, name, edit):
        self.run_git("checkout", "-q", "-b", name)
        edit()
        self.run_git("add", "-A")
        self.run_git("commit", "-q", "--no-verify", "-m", name)
        self.run_git("checkout", "-q", "main")
        self.write("_tools_/other.py", f"x = '{name}'\n")                       # main moves too: a real merge, not a fast-forward
        self.run_git("add", "-A")
        self.run_git("commit", "-q", "--no-verify", "-m", f"main moves for {name}")

    def merge(self, name, *extra, env=None):
        full = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
        full.update(env or {})
        return subprocess.run(["git", "-C", str(self.repo), "merge", "--no-ff", *extra, name, "-m", f"merge {name}"],
                              capture_output=True, text=True, env=full)

    def parents(self):
        return len(self.run_git("rev-list", "--parents", "-n", "1", "HEAD").stdout.split()) - 1

    def abort(self):
        self.run_git("merge", "--abort", check=False)


class Hook(MergeCase):
    def test_install_sets_up_both_hooks(self):
        for name in ("pre-commit", "pre-merge-commit"):
            path = self.repo / "_tools_/lint-gate/hooks" / name
            self.assertTrue(path.is_file(), name)
            self.assertTrue(os.access(path, os.X_OK), name)
        self.assertEqual(self.run_git("config", "--local", "core.hooksPath").stdout.strip(), "_tools_/lint-gate/hooks")
        dry = self.gate("install", "--dry-run")
        self.assertEqual(dry.returncode, 0, dry.stdout + dry.stderr)

    def test_a_merge_commit_touching_an_oversized_legacy_document_is_blocked(self):
        self.feature("work/big", lambda: self.write(BIG, self.read(BIG) + "one more word here\n"))
        before = self.head()
        r = self.merge("work/big")
        self.assertNotEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn(f"BLOCKED [document-concision] {BIG}", r.stdout + r.stderr)
        self.assertEqual(self.head(), before)                                     # no merge commit was made
        self.assertEqual(self.run_git("rev-parse", "-q", "--verify", "MERGE_HEAD", check=False).returncode, 0)   # still pending
        self.abort()

    def test_a_small_merge_passes_and_makes_a_merge_commit(self):
        self.feature("work/small", lambda: self.write(SMALL, self.read(SMALL) + "one more word\n"))
        r = self.merge("work/small")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertEqual(self.parents(), 2)

    def test_a_redaction_only_merge_passes_and_one_extra_word_blocks_it(self):
        def redact():
            r = self.gate("redact", str(self.repo / BIG), "--apply")
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.feature("work/redact", redact)
        r = self.merge("work/redact")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertEqual(self.parents(), 2)
        self.assertNotIn(NAME.split()[0].lower(), self.read(BIG).lower())

        self.write("_tools_/second.py", "y = 1\n")                                   # a fresh scenario on the merged main
        self.run_git("add", "-A")
        self.run_git("commit", "-q", "--no-verify", "-m", "more")
        self.write(BIG, self.read(BIG).replace("owner account", f"{NAME}"))          # put the name back, then redact plus a word
        self.run_git("add", "-A")
        self.run_git("commit", "-q", "--no-verify", "-m", "name back")
        def redact_plus():
            self.gate("redact", str(self.repo / BIG), "--apply")
            self.write(BIG, self.read(BIG) + "an extra changed word\n")
        self.feature("work/redact-plus", redact_plus)
        before = self.head()
        r = self.merge("work/redact-plus")
        self.assertNotEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn(f"BLOCKED [document-concision] {BIG}", r.stdout + r.stderr)
        self.assertEqual(self.head(), before)
        self.abort()

    def test_no_verify_stays_the_owners_override(self):
        self.feature("work/big", lambda: self.write(BIG, self.read(BIG) + "one more word here\n"))
        r = self.merge("work/big", "--no-verify")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertEqual(self.parents(), 2)

    def test_when_the_gate_cannot_run_the_merge_is_allowed_with_a_warning(self):
        self.feature("work/big", lambda: self.write(BIG, self.read(BIG) + "one more word here\n"))
        r = self.merge("work/big", env={"LINT_GATE_REFLECTION": "/nonexistent"})
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("could not run; merge commit allowed", r.stderr)

    def test_a_conflicted_merge_concluded_with_commit_is_checked_too(self):
        self.write("_activities_/small-profile/note.md", "line\n")
        self.write("_tools_/x.py", "x = 0\n")
        self.run_git("add", "-A")
        self.run_git("commit", "-q", "--no-verify", "-m", "conflict base")
        def both():
            self.write("_tools_/x.py", "x = 1\n")
            self.write(BIG, self.read(BIG) + "one more word here\n")
        self.run_git("checkout", "-q", "-b", "work/conflict")
        both()
        self.run_git("add", "-A")
        self.run_git("commit", "-q", "--no-verify", "-m", "feature")
        self.run_git("checkout", "-q", "main")
        self.write("_tools_/x.py", "x = 2\n")
        self.run_git("add", "-A")
        self.run_git("commit", "-q", "--no-verify", "-m", "main edits the same line")
        first = self.merge("work/conflict")
        self.assertNotEqual(first.returncode, 0)                                   # the conflict stops it
        self.write("_tools_/x.py", "x = 3\n")
        self.run_git("add", "-A")
        before = self.head()
        done = subprocess.run(["git", "-C", str(self.repo), "commit", "--no-edit"], capture_output=True, text=True,
                              env={k: v for k, v in os.environ.items() if not k.startswith("GIT_")})
        self.assertNotEqual(done.returncode, 0, done.stdout + done.stderr)
        self.assertIn("BLOCKED [document-concision]", done.stdout + done.stderr)
        self.assertEqual(self.head(), before)
        self.abort()


class ExemptShrinks(MergeCase):
    def exempt_path(self):
        return self.repo / "_tools_/lint-gate/exempt.txt"

    def test_an_added_entry_blocks_and_so_does_a_reworded_one(self):
        self.exempt_path().write_text(self.exempt_path().read_text() + "_records_/2026-11-23/some-activity/0900-queue-run.md\n")
        r = self.stage_check("_tools_/lint-gate/exempt.txt")
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("BLOCKED [exempt-list] _records_/2026-11-23/some-activity/0900-queue-run.md: added to exempt.txt", r.stdout)
        self.run_git("reset", "-q")
        self.run_git("checkout", "--", "_tools_/lint-gate/exempt.txt")
        text = self.exempt_path().read_text().replace("_records_/*/INDEX.md", "_records_/*/*/INDEX.md")
        self.exempt_path().write_text(text)
        self.assertEqual(self.stage_check("_tools_/lint-gate/exempt.txt").returncode, 1)

    def test_an_activities_exemption_can_never_be_added(self):
        self.exempt_path().write_text(self.exempt_path().read_text() + "_activities_/*/INDEX.md\n")
        r = self.stage_check("_tools_/lint-gate/exempt.txt")
        self.assertEqual(r.returncode, 1)
        self.assertIn("[exempt-list] _activities_/*/INDEX.md", r.stdout)

    def test_removing_entries_is_allowed(self):
        lines = self.exempt_path().read_text().splitlines()
        kept = [l for l in lines if "queue-run.md" not in l]
        self.assertLess(len(kept), len(lines))
        self.exempt_path().write_text("\n".join(kept) + "\n")
        r = self.stage_check("_tools_/lint-gate/exempt.txt")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertNotIn("exempt-list", r.stdout)

    def test_an_unchanged_list_is_never_a_finding(self):
        self.write(SMALL, self.read(SMALL) + "edit\n")
        r = self.stage_check(SMALL)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertNotIn("exempt-list", r.stdout)

    def test_an_oversized_activities_document_blocks_when_changed(self):
        self.write(BIG, self.read(BIG) + "changed\n")
        r = self.stage_check(BIG)
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn(f"BLOCKED [document-concision] {BIG}", r.stdout)

    def test_the_exempt_list_cannot_grow_in_a_merge_either(self):
        def grow():
            self.exempt_path().write_text(self.exempt_path().read_text() + "_records_/2026-11-23/x/0900-queue-run.md\n")
        self.feature("work/grow", grow)
        before = self.head()
        r = self.merge("work/grow")
        self.assertNotEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("[exempt-list]", r.stdout + r.stderr)
        self.assertEqual(self.head(), before)
        self.abort()

    def test_exempt_prune_lists_and_removes_only_what_exempts_nothing(self):
        before = self.exempt_path().read_text()
        dry = self.gate("exempt-prune")
        self.assertEqual(dry.returncode, 0, dry.stdout + dry.stderr)
        self.assertIn("obsolete: _records_/2026-11-22/alliance-duel/2037-queue-run.md", dry.stdout)
        self.assertNotIn("obsolete: _records_/*/INDEX.md", dry.stdout)               # it still exempts the oversized day index
        self.assertIn("dry run", dry.stdout)
        self.assertEqual(self.exempt_path().read_text(), before)
        applied = self.gate("exempt-prune", "--apply")
        self.assertEqual(applied.returncode, 0, applied.stdout + applied.stderr)
        after = self.exempt_path().read_text()
        self.assertIn("_records_/*/INDEX.md", after)
        self.assertNotIn("queue-run.md", after)
        self.assertIn("# Documents the commit gate does not block", after)           # comments stay
        gate = self.stage_check("_tools_/lint-gate/exempt.txt")
        self.assertEqual(gate.returncode, 0, gate.stdout + gate.stderr)               # a prune is a pure removal: it passes


if __name__ == "__main__":
    unittest.main()
