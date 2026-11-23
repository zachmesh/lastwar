"""Tests for the playbook-card rule of lint_gate.py: a changed activity card that lost its shape or passes the 300-word cap blocks; every other
card finding is a counted warning; an INDEX that is not a card is skipped; a repository without the tool, or a tool that cannot run, never blocks.
The fixture copies the real playbook-check tool into a temporary repository.

Run: python3 -m unittest discover -s _tools_/lint-gate
"""
from __future__ import annotations

import shutil
import sys
import unittest
from pathlib import Path

from test_lint_gate import GateCase, HERE

TOOL_DIR = HERE.parent / "playbook-check"
sys.path.insert(0, str(TOOL_DIR))
R1 = "_records_/2026-11-21/alpha-one/0145-queue-run.md"
INDEX = "_activities_/alpha-one/INDEX.md"
SECRET = "rule sentence that must never be printed by the gate"


def card(words=0, rules=None, route=None):
    rules = rules if rules is not None else [f"- R1 [verified 2026-11-21] Donate coins first {SECRET}. (evidence: {R1})"]
    route = route if route is not None else ["1. Open the menu.", "2. Tap donate."]
    pad = " ".join(f"w{i}" for i in range(words))
    return ("---\ntitle: Alpha One\ncreated: 2026-11-23T05:00:00Z\nmodified: 2026-11-23T05:00:00Z\nversion: 1.0.0\ndescription: Playbook card of alpha-one\n---\n"
            "# Alpha one\n\n## Goal\nDonate every cycle.\n\n## Route\n" + "\n".join(route) + "\n\n## Rules\n" + "\n".join(rules) + "\n\n## Failures\n"
            "- The button is grey - wait.\n\n## Open questions\n- Does the cap reset? test: read twice.\n\n## Numbers\n"
            f"42 donations in 6 units ({R1}).\n\n## Links\n- [digest](rule-digest.md)\n" + (f"\n{pad}\n" if words else ""))


@unittest.skipUnless(TOOL_DIR.is_dir(), "playbook-check is not in this checkout yet")
class PlaybookRule(GateCase):
    def setUp(self):
        super().setUp()
        shutil.copytree(TOOL_DIR, self.repo / "_tools_/playbook-check", ignore=shutil.ignore_patterns("__pycache__", "test_*"))
        self.write(R1, "---\ntitle: record\ncreated: 2026-11-21T01:45:00Z\nmodified: 2026-11-21T01:45:00Z\nversion: 1.0.0\ndescription: r\n---\nrecord\n")
        self.write("_activities_/INDEX.md", "# activities\n")
        self.write("_activities_/alpha-one/rule-digest.md", "---\ntitle: digest\ncreated: 2026-11-23T05:00:00Z\nmodified: 2026-11-23T05:00:00Z\nversion: 1.0.0\ndescription: d\n---\nrules\n")
        self.write(INDEX, card())
        self.write("_activities_/beta-two/INDEX.md", "---\ntitle: Beta\ncreated: 2026-11-23T05:00:00Z\nmodified: 2026-11-23T05:00:00Z\nversion: 1.0.0\ndescription: b\n---\n# Beta\n\n- [a](a.md)\n")
        self.write("_activities_/beta-two/a.md", "---\ntitle: a\ncreated: 2026-11-23T05:00:00Z\nmodified: 2026-11-23T05:00:00Z\nversion: 1.0.0\ndescription: a\n---\na\n")
        self.run_git("add", "-A")
        self.run_git("commit", "-q", "--no-verify", "-m", "cards")

    def test_a_good_card_edit_passes_silently(self):
        self.write(INDEX, card().replace("42 donations", "43 donations"))
        r = self.stage_check(INDEX)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertNotIn("playbook", r.stdout)

    def test_a_card_over_the_word_cap_blocks_but_stays_under_the_document_limit(self):
        self.write(INDEX, card(words=330))
        r = self.stage_check(INDEX)
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn(f"BLOCKED [playbook-card] {INDEX}: card-too-long (a card is 300 words or fewer)", r.stdout)
        self.assertNotIn("document-concision", r.stdout)                              # under 500 words: only the card rule objects
        self.assertIn("Playbook cards: keep a card at 300 words or fewer", r.stdout)
        self.assertNotIn(SECRET, r.stdout + r.stderr)

    def test_a_card_that_lost_its_shape_blocks(self):
        self.write(INDEX, "---\ntitle: Alpha\ncreated: 2026-11-23T05:00:00Z\nmodified: 2026-11-23T05:00:00Z\nversion: 1.1.0\ndescription: a\n---\n# Alpha\n\n- [digest](rule-digest.md)\n")
        r = self.stage_check(INDEX)
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn(f"BLOCKED [playbook-card] {INDEX}: card-shape-lost", r.stdout)

    def test_other_findings_are_a_counted_warning_and_never_block(self):
        rules = [f"- R{n} [unverified 2026-10-01] rule {n}. (evidence: {R1})" for n in range(1, 7)] + [f"- R7 [verified 2026-11-21] x. (evidence: _records_/gone.md)"]
        self.write(INDEX, card(rules=rules, route=[f"{n}. step" for n in range(1, 10)]))
        r = self.stage_check(INDEX)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("lint-gate: warning: playbook-card: card finding(s) that do not block - ", r.stdout)
        for code in ("too-many-rules 1", "route-too-long 1", "warn stale-unverified 6", "unresolved-path 1"):
            self.assertIn(code, r.stdout)
        self.assertNotIn("BLOCKED", r.stdout)

    def test_an_index_that_is_not_a_card_is_skipped(self):
        self.write("_activities_/beta-two/INDEX.md", "---\ntitle: Beta\ncreated: 2026-11-23T05:00:00Z\nmodified: 2026-11-23T05:00:00Z\nversion: 1.1.0\ndescription: b\n---\n# Beta\n\n- [a](a.md)\n- [more](a.md)\n")
        r = self.stage_check("_activities_/beta-two/INDEX.md")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertNotIn("playbook", r.stdout)

    def test_a_change_outside_activity_indexes_is_not_looked_at(self):
        self.write("_activities_/alpha-one/rule-digest.md", "---\ntitle: digest\ncreated: 2026-11-23T05:00:00Z\nmodified: 2026-11-23T05:30:00Z\nversion: 1.1.0\ndescription: d\n---\nrules changed\n")
        r = self.stage_check("_activities_/alpha-one/rule-digest.md")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertNotIn("playbook", r.stdout)

    def test_the_base_form_checks_the_working_tree_against_the_base(self):
        self.write(INDEX, card(words=330))
        r = self.gate("check", "--base", "HEAD")
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn(f"BLOCKED [playbook-card] {INDEX}: card-too-long", r.stdout)

    def test_the_rule_can_be_left_out(self):
        self.write(INDEX, card(words=330))
        self.run_git("add", INDEX)
        r = self.gate("check", "--staged", "--rules", "document-concision,entry-points,type-instance-trees")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_a_repository_without_the_tool_is_silent_and_a_broken_tool_is_a_warning(self):
        self.write(INDEX, card(words=330))
        self.run_git("add", INDEX)
        shutil.rmtree(self.repo / "_tools_/playbook-check")
        r = self.gate("check", "--staged")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertNotIn("playbook", r.stdout)
        (self.repo / "_tools_/playbook-check").mkdir()
        (self.repo / "_tools_/playbook-check/playbook_check.py").write_text("raise SystemExit('boom')\n")
        r = self.gate("check", "--staged")
        self.assertIn("lint-gate: warning: playbook-card: the card check could not run; nothing was blocked", r.stdout)
        self.assertNotIn("BLOCKED [playbook-card]", r.stdout)


if __name__ == "__main__":
    unittest.main()
