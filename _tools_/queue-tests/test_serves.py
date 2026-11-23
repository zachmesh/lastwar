"""Tests for the `serves` key of a queue unit: it survives claim, release and complete, enqueue --serves writes it, and
validate warns (never errors) when an upgrade-type unit has none. Every pool is a throwaway git repository in /tmp.

Run: python3 -m unittest discover -s _tools_/queue-tests
"""
from __future__ import annotations

import json
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

    def untagged(self, *extra, **kw):
        """A queued unit with its serves line removed: what a hand-written unit or an older tool copy leaves behind."""
        unit = self.enqueue("--serves", "temporary", *extra, **kw)
        path = self.path("inbox", unit)
        path.write_text(re.sub(r"(?m)^serves:.*\n", "", path.read_text(), count=1).replace("Serves: temporary\n", ""))
        return unit

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
        unit = self.untagged()
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

    def test_enqueue_refuses_a_unit_with_no_serves_unless_the_roster_gives_one(self):
        r = self.queue("enqueue", "--regular", "building-queues-growth-fill", "--activity", "building-queues", "--est-minutes", "5")
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("a unit needs a serves line", r.stdout)
        self.assertIn("is not in the roster", r.stdout)
        self.assertEqual(list((self.pool / "inbox").glob("*.md")), [])                  # nothing was queued
        ok = self.queue("enqueue", "--regular", "building-queues-growth-fill", "--activity", "building-queues",
                        "--est-minutes", "5", "--serves", "growth fill for the builders hut")
        self.assertEqual(ok.returncode, 0, ok.stdout + ok.stderr)

    def test_a_roster_regular_inherits_its_roster_serves_and_an_explicit_value_wins(self):
        unit = self.enqueue(activity="mail-rewards", regular="mail")                      # a roster id, no --serves
        self.assertEqual(self.frontmatter_line("inbox", unit, "serves"), "serves: upkeep")
        self.assertIn("Serves: upkeep", self.path("inbox", unit).read_text())
        other = self.enqueue("--serves", "a one-off snapshot", activity="mail-rewards", regular="help")
        self.assertEqual(self.frontmatter_line("inbox", other, "serves"), "serves: a one-off snapshot")

    def test_a_custom_roster_file_decides_what_is_inherited(self):
        roster = self.repo / "roster.json"
        roster.write_text(json.dumps({"regulars": [{"id": "snap-one", "serves": "snapshot"}, {"id": "bare-one"}]}))
        one = self.enqueue("--regulars-json", str(roster), activity="x-activity", regular="snap-one")
        two = self.enqueue("--regulars-json", str(roster), activity="x-activity", regular="bare-one")
        self.assertEqual(self.frontmatter_line("inbox", one, "serves"), "serves: snapshot")
        self.assertEqual(self.frontmatter_line("inbox", two, "serves"), "serves: upkeep")
        r = self.queue("enqueue", "--regulars-json", str(roster), "--regular", "mail", "--est-minutes", "5")
        self.assertEqual(r.returncode, 1)                                                 # mail is not in THIS roster
        gone = self.queue("enqueue", "--regulars-json", str(self.repo / "missing.json"), "--regular", "mail", "--est-minutes", "5")
        self.assertEqual(gone.returncode, 1)                                              # an unreadable roster never lets one through

    def test_serves_is_in_the_frontmatter_order_after_est_minutes(self):
        queue = load_queue_module()
        order = queue.FM_ORDER
        self.assertEqual(order[order.index("est_minutes") + 1], "serves")
        dumped = queue.dump_frontmatter({"unit": "u", "est_minutes": 5, "serves": SERVES, "attempts": 0})
        self.assertEqual(dumped.split("\n")[:5], ["---", "unit: u", "est_minutes: 5", f"serves: {SERVES}", "attempts: 0"])
        self.assertNotIn("serves", queue.dump_frontmatter({"unit": "u", "est_minutes": 5}))


class Validate(PoolCase):
    def validate(self, *extra):
        return self.queue("validate", *extra)

    def test_a_live_inbox_unit_without_serves_is_an_error(self):
        unit = self.untagged()
        r = self.validate()
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn(f"inbox/{unit}.md: live inbox unit has no serves line", r.stdout)
        self.assertIn("pool invalid: 1 problem(s)", r.stdout)

    def test_a_tagged_pool_is_valid_and_done_units_are_history(self):
        self.enqueue("--serves", SERVES)
        done = self.untagged(activity="mail-rewards", regular="mail")
        self.queue("claim", "--unit", done, "--executor", "tester")
        self.queue("complete", "--unit", done, "--status", "done", "--summary", "x")
        r = self.validate()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("pool valid", r.stdout)
        self.assertNotIn("no serves", r.stdout)

    def test_a_claimed_upgrade_type_unit_without_serves_warns_and_does_not_fail(self):
        unit = self.untagged()                                                         # activity upgrade-builders-hut-to
        self.queue("claim", "--unit", unit, "--executor", "tester")
        r = self.validate()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn(f"warning: claimed/{unit}.md: upgrade-type unit has no serves line", r.stdout)
        plain = self.untagged(activity="mail-rewards", regular="mail")
        self.queue("claim", "--unit", plain, "--executor", "tester")
        self.assertNotIn(f"claimed/{plain}.md", self.validate().stdout)               # not upgrade-type: nothing to say

    def test_a_real_pool_problem_and_a_missing_serves_are_both_errors(self):
        self.untagged()
        (self.pool / "inbox" / "broken-2026-11-23-0000.md").write_text("no frontmatter here\n")
        r = self.validate()
        self.assertEqual(r.returncode, 1)
        self.assertIn("no frontmatter block", r.stdout)
        self.assertIn("live inbox unit has no serves line", r.stdout)
        self.assertIn("pool invalid: 2 problem(s)", r.stdout)

    def test_validate_ref_gives_the_same_error_for_a_committed_pool(self):
        unit = self.untagged()
        subprocess.run(["git", "-C", str(self.repo), "add", "-A"], check=True)
        subprocess.run(["git", "-C", str(self.repo), "commit", "-q", "-m", "pool"], check=True)
        r = self.validate("--ref", "HEAD")
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn(f"inbox/{unit}.md: live inbox unit has no serves line", r.stdout)
        self.assertIn("pool invalid at HEAD", r.stdout)

    def test_sync_only_warns_about_an_untagged_inbox_unit_and_still_runs(self):
        self.untagged()
        r = self.queue("sync")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("inbox unit(s) carry no serves line; validate reports them as errors", r.stderr)
        self.assertNotIn("sync refused", r.stderr)

    def test_the_roster_default_is_in_place_wherever_the_refusal_is(self):
        # the refusal must never land without the roster default: every roster regular is both accepted by enqueue
        # without --serves and minted with one
        for item in json.loads((QUEUE.parent / "regulars.json").read_text())["regulars"]:
            self.assertEqual(load_queue_module()._roster_serves(item["id"], str(QUEUE.parent / "regulars.json")), "upkeep", item["id"])


class UpgradeType(unittest.TestCase):
    def test_the_definition(self):
        queue = load_queue_module()
        for fields in ({"activity": "building-queues"}, {"activity": "research-queue"}, {"activity": "troop-training"},
                       {"activity": "x-upgrade-y"}, {"regular": "tech-upgrade"}, {"regular": "building-queues-growth-fill"},
                       {"regular": "upgradeless-thing"},                             # contains the word: counts
                       {"unit": "building-queues-growth-fill-2026-11-23-0801"}, {"unit": "z-upgrade-2026"}):
            self.assertTrue(queue.is_upgrade_type(fields), fields)
        for fields in ({}, {"activity": "daily-activities", "regular": "daily-activities", "unit": "daily-2026"},
                       {"activity": "mail-rewards", "regular": "mail"}):
            self.assertFalse(queue.is_upgrade_type(fields), fields)

    def test_warnings_cover_claimed_units_only(self):
        queue = load_queue_module()
        text = "---\nunit: u\nregular: tech-upgrade\nactivity: a\n---\nbody\n"
        self.assertEqual(len(queue._unit_warnings("claimed/u.md", text)), 1)
        self.assertEqual(queue._unit_warnings("inbox/u.md", text), [])
        self.assertEqual(queue._unit_warnings("done/u.md", text), [])
        self.assertEqual(len(queue._missing_serves("inbox/u.md", text)), 1)
        self.assertEqual(queue._missing_serves("claimed/u.md", text), [])


if __name__ == "__main__":
    unittest.main()
