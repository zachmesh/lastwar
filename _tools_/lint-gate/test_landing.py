"""Tests for the landing form of the gate: `check --base REF --landing` exits 2 - never 0 - when the gate cannot run (a base
that does not resolve, a missing or empty denylist, a crashed rule), while the plain forms and the hooks keep today's warn and
allow. Everything is made up in a throwaway repository.

Run: python3 -m unittest discover -s _tools_/lint-gate
"""
from __future__ import annotations

import os
import unittest

from test_lint_gate import doc
from test_privacy import PrivacyCase

SMALL = "_activities_/small-profile/INDEX.md"


class Landing(PrivacyCase):
    def setUp(self):
        super().setUp()
        self.deny(["# made-up", "# marker: owner account", r"zorvane\s+quill"])
        self.write(SMALL, doc(50, "Small"))
        self.commit_clean("small profile")
        self.run_git("update-ref", "refs/remotes/origin/main", "HEAD")
        self.write(SMALL, doc(60, "Small"))                                           # the change being landed
        self.commit_clean("a small change")

    def landing(self, *extra, base="origin/main"):
        return self.gate("check", "--base", base, "--landing", *extra)

    def test_a_ready_landing_check_passes(self):
        r = self.landing()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("lint-gate: ok", r.stdout)

    def test_a_missing_denylist_is_exit_two_in_the_landing_form_and_a_warning_in_the_plain_form(self):
        (self.repo / ".git" / "privacy-denylist.txt").unlink()
        r = self.landing()
        self.assertEqual(r.returncode, 2, r.stdout + r.stderr)
        self.assertIn("denylist is missing or empty", r.stderr)
        plain = self.gate("check", "--base", "origin/main")
        self.assertEqual(plain.returncode, 0, plain.stdout + plain.stderr)               # today: only a warning, privacy not checked
        self.assertIn("privacy not checked", plain.stdout)

    def test_a_denylist_with_only_comments_is_the_same(self):
        self.deny(["# only a comment", "# marker: owner account"])
        self.assertEqual(self.landing().returncode, 2)

    def test_a_base_that_does_not_resolve_is_exit_two_and_the_plain_form_reads_it_as_an_empty_tree(self):
        r = self.landing(base="origin/nope")
        self.assertEqual(r.returncode, 2, r.stdout + r.stderr)
        self.assertIn("does not resolve to a commit", r.stderr)
        plain = self.gate("check", "--base", "origin/nope")
        self.assertEqual(plain.returncode, 1)                                            # today: everything looks new, blocked for the wrong reason

    def test_an_unreadable_reflection_checkout_is_exit_two_in_every_form(self):
        self.assertEqual(self.landing("--reflection", "/nonexistent").returncode, 2)
        self.assertEqual(self.gate("check", "--base", "origin/main", "--reflection", "/nonexistent").returncode, 2)

    def test_a_crashed_rule_is_exit_two_in_the_landing_form_not_a_traceback_with_exit_one(self):
        (self.repo / "_tools_/lint-gate/exempt.txt").write_bytes(b"\xff\xfe not text \x80\n")     # the exemption reader cannot decode it
        r = self.landing()
        self.assertEqual(r.returncode, 2, r.stdout + r.stderr)
        self.assertIn("a rule crashed (", r.stderr)
        self.assertNotIn("Traceback", r.stderr)
        plain = self.gate("check", "--base", "origin/main")
        self.assertEqual(plain.returncode, 1, plain.stdout + plain.stderr)               # unchanged: a traceback, exit 1
        self.assertIn("Traceback", plain.stderr)

    def test_the_landing_form_is_only_the_base_form_and_needs_the_privacy_rule(self):
        self.assertEqual(self.gate("check", "--staged", "--landing").returncode, 2)
        self.assertEqual(self.gate("check", "--landing").returncode, 2)
        r = self.landing("--rules", "document-concision")
        self.assertEqual(r.returncode, 2)
        self.assertIn("privacy rule must run", r.stderr)

    def test_a_real_blocking_finding_is_still_exit_one(self):
        self.write("_tools_/big.md", doc(650, "Big"))
        self.commit_clean("an oversized new document")
        r = self.landing()
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("BLOCKED", r.stdout)

    def test_the_hooks_do_not_pass_landing_and_still_allow_on_exit_two(self):
        for name in ("pre-commit", "pre-merge-commit"):
            text = (self.repo / "_tools_/lint-gate/hooks" / name).read_text() if (self.repo / "_tools_/lint-gate/hooks" / name).exists() else ""
            self.assertNotIn("--landing", text, name)
            if text:
                self.assertIn('if [ "$rc" -eq 2 ]', text, name)


if __name__ == "__main__":
    unittest.main()
