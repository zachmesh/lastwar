"""Tests for the playbook stats of `queue.py complete` (OD-20261123-15): optional --rules-used, --rule-failed and --rule-gap, stored as
result stats rules_used, rule_failed and rule_gap - never `gap`, which thirteen older units carry as a score.

Run: python3 -m unittest discover -s _tools_/queue-tests
"""
from __future__ import annotations

import re

from test_serves import PoolCase, load_queue_module


class RuleStats(PoolCase):
    def finish(self, *extra, status="done", regular="building-queues", activity="building-queues"):
        unit = self.enqueue("--serves", "made up", activity=activity, regular=regular)
        self.assertEqual(self.queue("claim", "--unit", unit, "--executor", "tester").returncode, 0)
        r = self.queue("complete", "--unit", unit, "--status", status, "--summary", "x", *extra)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        fields, _ = load_queue_module().read_unit(str(self.path("done", unit)))
        return fields["result"]

    def test_the_three_flags_are_stored_as_result_stats(self):
        result = self.finish("--rules-used", "R1,R3", "--rule-failed", "R2", "--rule-gap", "no rule covers the second tab")
        stats = result["stats"]
        self.assertEqual((stats["rules_used"], stats["rule_failed"], stats["rule_gap"]), ("R1,R3", "R2", "no rule covers the second tab"))
        self.assertNotIn("gap", stats)
        self.assertEqual(result["stats_warnings"], [])

    def test_all_three_are_optional_and_a_unit_without_them_is_unchanged(self):
        stats = self.finish()["stats"]
        for key in ("rules_used", "rule_failed", "rule_gap"):
            self.assertNotIn(key, stats)
        only = self.finish("--rule-failed", "R4", regular="research-queue", activity="research-queue")["stats"]
        self.assertEqual(only["rule_failed"], "R4")
        self.assertNotIn("rules_used", only)

    def test_ids_are_normalised_without_ever_refusing_the_completion(self):
        stats = self.finish("--rules-used", " R1 , R3,R1 ,, R7 ")["stats"]
        self.assertEqual(stats["rules_used"], "R1,R3,R7")
        self.assertNotIn("rule_failed", self.finish("--rule-failed", " , ,", regular="research-queue", activity="research-queue")["stats"])

    def test_oversize_values_are_cut_with_a_warning_and_the_unit_still_completes(self):
        result = self.finish("--rules-used", ",".join(f"R{n}" for n in range(30)), "--rule-gap", "g" * 300)
        self.assertEqual(len(result["stats"]["rules_used"].split(",")), 20)
        self.assertEqual(len(result["stats"]["rule_gap"]), 200)
        self.assertIn("rules_used: more than 20 rule ids; the rest were dropped", result["stats_warnings"])
        self.assertIn("rule_gap: cut to 200 characters", result["stats_warnings"])
        long_id = self.finish("--rule-failed", "x" * 90, regular="research-queue", activity="research-queue")
        self.assertEqual(len(long_id["stats"]["rule_failed"]), 60)
        self.assertIn("rule_failed: a rule id was cut to 60 characters", long_id["stats_warnings"])

    def test_a_multi_line_gap_is_folded_and_a_colon_survives(self):
        stats = self.finish("--rule-gap", "first line\n  second line: with a colon, and commas")["stats"]
        self.assertEqual(stats["rule_gap"], "first line second line: with a colon, and commas")

    def test_the_legacy_gap_score_and_rule_gap_do_not_collide(self):
        stats = self.finish("--stat", "gap=7", "--rule-gap", "a missing rule")["stats"]
        self.assertEqual((stats["gap"], stats["rule_gap"]), (7, "a missing rule"))
        old = self.finish("--stat", "gap=3", regular="research-queue", activity="research-queue")["stats"]
        self.assertEqual(old["gap"], 3)
        self.assertNotIn("rule_gap", old)

    def test_the_flags_work_for_partial_and_failed_closings_and_win_over_a_stat_of_the_same_name(self):
        for status in ("partial", "failed"):
            self.setUp()
            stats = self.finish("--rule-failed", "R2", "--stat", "rule_failed=R9", status=status)["stats"]
            self.assertEqual(stats["rule_failed"], "R2", status)

    def test_a_numeric_id_survives_as_a_value(self):
        self.assertEqual(str(self.finish("--rules-used", "3")["stats"]["rules_used"]), "3")

    def test_the_flags_are_listed_in_the_help(self):
        out = self.queue("complete", "--help")
        for flag in ("--rules-used", "--rule-failed", "--rule-gap"):
            self.assertIn(flag, out.stdout)
        self.assertIn("never the legacy gap score", re.sub(r"\s+", " ", out.stdout))
