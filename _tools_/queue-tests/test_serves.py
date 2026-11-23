"""Tests for the `serves` key of a queue unit: it survives claim, release and complete, enqueue --serves writes it, and
validate warns (never errors) when an upgrade-type unit has none. Every pool is a throwaway git repository in /tmp.

Run: python3 -m unittest discover -s _tools_/queue-tests
"""
from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

QUEUE = Path(__file__).resolve().parent.parent / "queue.py"
SERVES = "keeps the builders hut upgrade on its window"


def load_queue_module():
    import importlib.util
    spec = importlib.util.spec_from_file_location("queue_under_test", QUEUE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class PoolCase(unittest.TestCase):
    def setUp(self):
        self.repo = Path(tempfile.mkdtemp(prefix="queue-serves-", dir="/tmp"))
        self.addCleanup(shutil.rmtree, self.repo, True)
        self.pool = self.repo / "_queue_"
        for state in ("inbox", "claimed", "done"):
            (self.pool / state).mkdir(parents=True)
        subprocess.run(["git", "init", "-q", str(self.repo)], check=True)
        subprocess.run(["git", "-C", str(self.repo), "config", "user.email", "t@example.org"], check=True)
        subprocess.run(["git", "-C", str(self.repo), "config", "user.name", "t"], check=True)
        self.env = dict(os.environ, LASTWAR_QUEUE_ALLOW_TMP_ROOT="1", LASTWAR_QUEUE_ALLOW_STALE_TOOL="1",
                        LASTWAR_QUEUE_ALLOW_UNREAD_CLAIM="1")

    def queue(self, *args):
        return subprocess.run([sys.executable, "-B", str(QUEUE), "--root", str(self.pool), *args], capture_output=True,
                              text=True, env=self.env, cwd=str(self.repo))

    def enqueue(self, *extra, activity="upgrade-builders-hut-to", regular="building-queues"):
        r = self.queue("enqueue", "--regular", regular, "--activity", activity, "--est-minutes", "5", *extra)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        return re.search(r"queued (\S+)", r.stdout).group(1)

    def path(self, state, unit):
        return self.pool / state / f"{unit}.md"

    def frontmatter_line(self, state, unit, key):
        for line in self.path(state, unit).read_text().split("\n---\n", 1)[0].split("\n"):
            if line.startswith(f"{key}:"):
                return line
        return None


class Survives(PoolCase):
    def test_enqueue_serves_is_written_and_survives_claim_release_claim_and_complete(self):
        unit = self.enqueue("--serves", SERVES)
        want = f"serves: {SERVES}"
        self.assertEqual(self.frontmatter_line("inbox", unit, "serves"), want)
        self.assertIn(f"Serves: {SERVES}", self.path("inbox", unit).read_text())
        self.assertEqual(self.queue("claim", "--unit", unit, "--executor", "tester").returncode, 0)
        self.assertEqual(self.frontmatter_line("claimed", unit, "serves"), want)
        self.assertEqual(self.queue("release", "--unit", unit).returncode, 0)
        self.assertEqual(self.frontmatter_line("inbox", unit, "serves"), want)
        self.assertEqual(self.queue("claim", "--unit", unit, "--executor", "tester").returncode, 0)
        done = self.queue("complete", "--unit", unit, "--status", "done", "--summary", "fixture")
        self.assertEqual(done.returncode, 0, done.stdout + done.stderr)
        self.assertEqual(self.frontmatter_line("done", unit, "serves"), want)
        self.assertIn("  status: done", self.path("done", unit).read_text())          # the result section is still written

    def test_a_serves_line_added_by_hand_is_no_longer_dropped_at_the_next_claim(self):
        unit = self.enqueue()
        self.assertIsNone(self.frontmatter_line("inbox", unit, "serves"))
        text = self.path("inbox", unit).read_text()
        self.path("inbox", unit).write_text(text.replace("est_minutes: 5\n", f"est_minutes: 5\nserves: {SERVES}\n", 1))
        self.assertEqual(self.queue("claim", "--unit", unit, "--executor", "tester").returncode, 0)
        self.assertEqual(self.frontmatter_line("claimed", unit, "serves"), f"serves: {SERVES}")
        self.assertEqual(self.queue("complete", "--unit", unit, "--status", "done", "--summary", "x").returncode, 0)
        self.assertEqual(self.frontmatter_line("done", unit, "serves"), f"serves: {SERVES}")

    def test_a_value_with_a_colon_and_commas_comes_back_unchanged(self):
        value = "the 3 upgrades: hut, wall and lab, in that order"
        unit = self.enqueue("--serves", value)
        self.queue("claim", "--unit", unit, "--executor", "tester")
        self.assertEqual(self.frontmatter_line("claimed", unit, "serves"), f"serves: {value}")

    def test_a_multi_line_value_is_folded_to_one_line_and_an_empty_one_is_refused(self):
        unit = self.enqueue("--serves", "first line\n   second line")
        self.assertEqual(self.frontmatter_line("inbox", unit, "serves"), "serves: first line second line")
        r = self.queue("enqueue", "--regular", "building-queues", "--est-minutes", "5", "--serves", "   ")
        self.assertEqual(r.returncode, 1)
        self.assertIn("--serves is empty text", r.stdout)

    def test_a_unit_without_serves_gets_no_serves_line(self):
        unit = self.enqueue(activity="daily-activities", regular="daily-activities")
        self.assertIsNone(self.frontmatter_line("inbox", unit, "serves"))
        self.assertNotIn("Serves:", self.path("inbox", unit).read_text())
        self.queue("claim", "--unit", unit, "--executor", "tester")
        self.assertIsNone(self.frontmatter_line("claimed", unit, "serves"))

    def test_serves_is_in_the_frontmatter_order_after_est_minutes(self):
        queue = load_queue_module()
        order = queue.FM_ORDER
        self.assertEqual(order[order.index("est_minutes") + 1], "serves")
        dumped = queue.dump_frontmatter({"unit": "u", "est_minutes": 5, "serves": SERVES, "attempts": 0})
        self.assertEqual(dumped.split("\n")[:5], ["---", "unit: u", "est_minutes: 5", f"serves: {SERVES}", "attempts: 0"])
        self.assertNotIn("serves", queue.dump_frontmatter({"unit": "u", "est_minutes": 5}))


class Warnings(PoolCase):
    def validate(self, *extra):
        return self.queue("validate", *extra)

    def test_an_upgrade_type_unit_without_serves_warns_and_still_validates(self):
        unit = self.enqueue()                                                       # activity upgrade-builders-hut-to
        r = self.validate()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn(f"warning: inbox/{unit}.md: upgrade-type unit has no serves line", r.stdout)
        self.assertIn("pool valid (1 warning(s))", r.stdout)

    def test_a_serves_line_clears_the_warning_and_other_units_never_warn(self):
        self.enqueue("--serves", SERVES)
        self.enqueue(activity="daily-activities", regular="daily-activities")
        r = self.validate()
        self.assertEqual(r.returncode, 0, r.stdout)
        self.assertNotIn("warning", r.stdout)
        self.assertIn("pool valid", r.stdout)

    def warned(self):
        return re.findall(r"warning: inbox/(\S+?)\.md", self.validate().stdout)

    def test_the_three_growth_activities_are_upgrade_type_whatever_the_regular(self):
        units = [self.enqueue(activity=a, regular=f"r-{i}") for i, a in
                 enumerate(("building-queues", "research-queue", "troop-training"))]
        self.assertEqual(sorted(self.warned()), sorted(units))

    def test_an_id_containing_upgrade_or_growth_fill_is_upgrade_type_in_activity_regular_or_unit(self):
        by_activity = self.enqueue(activity="x-upgrade-y", regular="plain-one")
        by_regular = self.enqueue(activity="plain-act", regular="tech-upgrade")
        by_fill = self.enqueue(activity="plain-act", regular="building-queues-growth-fill")     # the planner's fill units
        by_substring = self.enqueue(activity="plain-act", regular="upgradeless-thing")           # contains the word: counts
        plain = self.enqueue(activity="daily-activities", regular="daily-activities")
        warned = self.warned()
        self.assertEqual(sorted(warned), sorted([by_activity, by_regular, by_fill, by_substring]))
        self.assertNotIn(plain, warned)
        self.assertIn("growth-fill", by_fill)                                                    # the unit id carries it too

    def test_a_unit_id_alone_is_enough(self):
        queue = load_queue_module()
        self.assertTrue(queue.is_upgrade_type({"unit": "building-queues-growth-fill-2026-11-23-0801", "activity": "x", "regular": "y"}))
        self.assertTrue(queue.is_upgrade_type({"unit": "z-upgrade-2026", "activity": "x", "regular": "y"}))
        self.assertFalse(queue.is_upgrade_type({"unit": "daily-2026", "activity": "daily-activities", "regular": "daily-activities"}))
        self.assertFalse(queue.is_upgrade_type({}))

    def test_claimed_units_warn_and_done_units_do_not(self):
        unit = self.enqueue()
        self.queue("claim", "--unit", unit, "--executor", "tester")
        self.assertIn(f"warning: claimed/{unit}.md", self.validate().stdout)
        self.queue("complete", "--unit", unit, "--status", "done", "--summary", "x")
        r = self.validate()
        self.assertNotIn("warning", r.stdout)
        self.assertEqual(r.returncode, 0)

    def test_a_real_pool_problem_is_still_an_error_beside_the_warning(self):
        self.enqueue()
        (self.pool / "inbox" / "broken-2026-11-23-0000.md").write_text("no frontmatter here\n")
        r = self.validate()
        self.assertEqual(r.returncode, 1)
        self.assertIn("warning: inbox/", r.stdout)
        self.assertIn("no frontmatter block", r.stdout)

    def test_validate_ref_reports_the_same_warning_for_a_committed_pool(self):
        unit = self.enqueue()
        subprocess.run(["git", "-C", str(self.repo), "add", "-A"], check=True)
        subprocess.run(["git", "-C", str(self.repo), "commit", "-q", "-m", "pool"], check=True)
        r = self.validate("--ref", "HEAD")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn(f"warning: inbox/{unit}.md: upgrade-type unit has no serves line", r.stdout)
        self.assertIn("pool valid at HEAD (1 warning(s))", r.stdout)


if __name__ == "__main__":
    unittest.main()
