"""Tests for result.state_read of `queue.py complete --state-read` (Steer A, 2026-11-24): the one-line evidence a DONE that rests on a verified
nothing-to-claim or nothing-to-do state carries - '<what was read, quoted> | <frame: step number or file> | <HH:MM:SSZ>'. A new key beside
`evidence`; optional; stored as given; a pattern mismatch is a warning (in the closing and in result.stats_warnings), never a refusal.

Run: python3 -m unittest discover -s _tools_/queue-tests
"""
from __future__ import annotations

import re

from test_serves import PoolCase, load_queue_module

GOOD = "Already claimed today (S1) | step 6 frame | 15:07:44Z"


class StateRead(PoolCase):
    def finish(self, *extra, status="done"):
        unit = self.enqueue("--serves", "made up")
        self.assertEqual(self.queue("claim", "--unit", unit, "--executor", "tester").returncode, 0)
        r = self.queue("complete", "--unit", unit, "--status", status, "--summary", "x", *extra)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)                      # never a refusal
        fields, _ = load_queue_module().read_unit(str(self.path("done", unit)))
        return r, fields["result"], unit

    def test_a_valid_line_is_stored_beside_evidence_with_no_warning(self):
        r, result, unit = self.finish("--evidence", "_records_/x/y.md", "--state-read", GOOD)
        self.assertEqual(result["state_read"], GOOD)
        self.assertEqual(result["evidence"], "_records_/x/y.md")                       # the record path stays where it was
        self.assertNotIn("state_read", r.stdout)
        self.assertFalse([w for w in result["stats_warnings"] if "state_read" in w])
        text = self.path("done", unit).read_text()
        self.assertLess(text.index("evidence:"), text.index("state_read:"))
        self.assertLess(text.index("state_read:"), text.index("follow_up:"))

    def test_without_the_flag_the_key_is_absent_and_nothing_changes(self):
        r, result, unit = self.finish()
        self.assertNotIn("state_read", result)
        self.assertNotIn("state_read", self.path("done", unit).read_text())
        self.assertFalse([w for w in result["stats_warnings"] if "state_read" in w])
        self.assertNotIn("state_read", r.stdout)

    def test_the_frame_may_be_a_step_a_step_frame_or_a_file(self):
        for frame in ("step 6", "step 6 frame", "step6", "frame-06.png", "shots/claim.jpg", "_records_/x/screen.md"):
            self.setUp()                                                               # a fresh pool: unit names are minute-stamped
            r, result, _ = self.finish("--state-read", f"No claim button | {frame} | 09:05:01Z")
            self.assertFalse([w for w in result["stats_warnings"] if w.startswith("state_read")], frame)

    def test_a_mismatch_is_a_warning_with_the_reason_never_a_refusal_and_never_the_text(self):
        cases = {
            "Already claimed today": "three parts",
            "a | b": "three parts",
            " | step 6 | 15:07:44Z": "first part (what was read) is empty",
            "Already claimed | the screen | 15:07:44Z": "frame part must be",
            "Already claimed | step 6 | 15:07Z": "time part must be HH:MM:SSZ",
            "Already claimed | step 6 | 25:00:00Z": "time part must be HH:MM:SSZ",
            "Already claimed | step 6 | 15:07:44": "time part must be HH:MM:SSZ",
            "Already claimed | step 6 | 15:07:44Z | extra": "three parts",
        }
        for text, why in cases.items():
            self.setUp()
            r, result, _ = self.finish("--state-read", text)
            self.assertIn("warning:", r.stdout, text)
            self.assertIn(why, r.stdout, text)
            self.assertIn("a warning for now, not a refusal", r.stdout)
            self.assertEqual(result["state_read"], " ".join(text.split()), text)             # stored as given, on one line
            self.assertTrue(any(w.startswith("state_read does not fit the pattern") for w in result["stats_warnings"]), text)
            self.assertNotIn("Already claimed", r.stdout.split("warning:", 1)[1].split("\\n")[0] if False else "".join(re.findall(r"warning:[^\\n]*", r.stdout)))

    def test_a_multi_line_value_is_stored_on_one_line_and_warned(self):
        r, result, unit = self.finish("--state-read", "Already claimed\n| step 6 | 15:07:44Z")
        self.assertIn("it must be one line", r.stdout)
        self.assertNotIn("\n", result["state_read"])

    def test_it_is_kept_for_every_closing_status(self):
        for status in ("done", "partial", "failed", "skipped-needs-owner"):
            self.setUp()
            _r, result, _ = self.finish("--state-read", GOOD, status=status)
            self.assertEqual(result["state_read"], GOOD, status)

    def test_a_state_read_line_inside_the_summary_counts_when_there_is_no_flag(self):
        unit = self.enqueue("--serves", "made up")
        self.assertEqual(self.queue("claim", "--unit", unit, "--executor", "tester").returncode, 0)
        summary = f"Nothing to claim.\nstate_read: {GOOD}\nLab timers quoted above."
        r = self.queue("complete", "--unit", unit, "--status", "done", "--summary", summary)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        fields, _ = load_queue_module().read_unit(str(self.path("done", unit)))
        self.assertEqual(fields["result"]["state_read"], GOOD)
        self.assertIn("Nothing to claim.", fields["result"]["summary"])              # the summary is kept whole (on one line)
        self.assertIn("Lab timers quoted above.", fields["result"]["summary"])

    def test_a_state_read_at_the_end_of_a_one_line_summary_counts_and_a_multi_line_summary_no_longer_breaks_the_unit(self):
        unit = self.enqueue("--serves", "made up")
        self.assertEqual(self.queue("claim", "--unit", unit, "--executor", "tester").returncode, 0)
        r = self.queue("complete", "--unit", unit, "--status", "done", "--summary", f"Nothing to claim. state_read: {GOOD}")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        fields, _ = load_queue_module().read_unit(str(self.path("done", unit)))
        self.assertEqual(fields["result"]["state_read"], GOOD)
        self.assertEqual(fields["result"]["summary"], f"Nothing to claim. state_read: {GOOD}")
        self.setUp()                                                                  # a multi-line summary used to write its later lines as top-level keys
        unit = self.enqueue("--serves", "made up")
        self.assertEqual(self.queue("claim", "--unit", unit, "--executor", "tester").returncode, 0)
        r = self.queue("complete", "--unit", unit, "--status", "done", "--summary", "first line\nsecond line\nthird")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        fields, _ = load_queue_module().read_unit(str(self.path("done", unit)))
        self.assertEqual(fields["result"]["summary"], "first line second line third")
        self.assertEqual(sorted(k for k in fields if k not in ("unit", "regular", "activity", "segment", "priority", "created_at", "expires_at", "planned_for",
                                                               "not_before", "window", "est_minutes", "serves", "chain_id", "chain_seq", "attempts",
                                                               "max_attempts", "claimed_by", "claimed_at", "lease_until", "result")), [])

    def test_the_flag_wins_over_a_line_in_the_summary(self):
        _r, result, _ = self.finish("--state-read", GOOD, "--summary", "x\nstate_read: other | step 1 | 01:02:03Z")
        self.assertEqual(result["state_read"], GOOD)

    def test_the_flag_is_listed_in_the_help_with_its_pattern(self):
        out = re.sub(r"\s+", " ", self.queue("complete", "--help").stdout)
        self.assertIn("--state-read", out)
        self.assertIn("<what was read, quoted> | <frame: step number or file> | <HH:MM:SSZ>", out)
        self.assertIn("never a refusal", out)

    def test_validate_accepts_a_pool_whose_done_unit_carries_the_key(self):
        self.finish("--state-read", GOOD)
        r = self.queue("validate")
        self.assertNotIn("state_read", r.stdout + r.stderr)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)


class StateChange(PoolCase):
    """result.state_change: the unit's own declaration yes or no, stored beside evidence and state_read; optional, no warning when absent."""

    def finish(self, *extra, status="done"):
        unit = self.enqueue("--serves", "made up")
        self.assertEqual(self.queue("claim", "--unit", unit, "--executor", "tester").returncode, 0)
        r = self.queue("complete", "--unit", unit, "--status", status, "--summary", "x", *extra)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        fields, _ = load_queue_module().read_unit(str(self.path("done", unit)))
        return r, fields["result"], unit

    def test_yes_and_no_are_stored_beside_evidence_and_state_read_without_a_warning(self):
        for value in ("yes", "no"):
            self.setUp()
            r, result, unit = self.finish("--state-change", value, "--state-read", GOOD, "--evidence", "_records_/x.md")
            self.assertEqual(result["state_change"], value)
            self.assertNotIn("state_change", r.stdout)
            text = self.path("done", unit).read_text()
            self.assertLess(text.index("evidence:"), text.index("state_read:"))
            self.assertLess(text.index("state_read:"), text.index("state_change:"))
            self.assertLess(text.index("state_change:"), text.index("follow_up:"))

    def test_case_and_spaces_are_normalised(self):
        _r, result, _ = self.finish("--state-change", "  YES ")
        self.assertEqual(result["state_change"], "yes")

    def test_absent_means_no_key_and_no_warning(self):
        r, result, unit = self.finish()
        self.assertNotIn("state_change", result)
        self.assertNotIn("state_change", r.stdout)
        self.assertNotIn("state_change", self.path("done", unit).read_text())

    def test_anything_else_is_not_stored_and_never_refuses_the_closing(self):
        for value in ("maybe", "true", "1", "yes, partly"):
            self.setUp()
            r, result, _ = self.finish("--state-change", value)
            self.assertNotIn("state_change", result, value)
            self.assertIn("warning:", r.stdout)
            self.assertIn("state_change that is not yes or no - not stored; it never refuses the closing", r.stdout)

    def test_it_is_kept_for_every_closing_status_and_listed_in_the_help(self):
        for status in ("done", "partial", "failed", "skipped-needs-owner"):
            self.setUp()
            _r, result, _ = self.finish("--state-change", "no", status=status)
            self.assertEqual(result["state_change"], "no", status)
        out = re.sub(r"\s+", " ", self.queue("complete", "--help").stdout)
        self.assertIn("--state-change", out)
        self.assertIn("yes if the unit changed the game state", out)
