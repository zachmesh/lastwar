"""Tests for _tools_/strategy_conformance.py: each alarm at its threshold (just under and just over), counts-only output,
read-only behaviour, and the plan-item check. Every pool is made up in a temporary folder.

Run: python3 -m unittest discover -s _tools_/strategy-conformance
"""
from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

TOOL = Path(__file__).resolve().parent / "strategy_conformance.py"
NOW = datetime(2026, 11, 23, 9, 0, tzinfo=timezone.utc)
SECRET = "free text that must never be printed"


def iso(minutes_ago: float) -> str:
    return (NOW - timedelta(minutes=minutes_ago)).strftime("%Y-%m-%dT%H:%M:%SZ")


class PoolCase(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp(prefix="conformance-"))
        self.addCleanup(shutil.rmtree, self.root, True)
        for folder in ("inbox", "claimed", "done"):
            (self.root / "_queue_" / folder).mkdir(parents=True)
        self.n = 0

    def unit(self, folder, ago=10, status="done", serves="growth-lever", activity="mail-rewards", hours=0.25, stats=None,
             claimed=False, chain="", regular="mail", name=None):
        self.n += 1
        name = name or f"{regular}-2026-11-23-{self.n:04d}"
        front = [f"unit: {name}", f"regular: {regular}", f"activity: {activity}", "est_minutes: 15"]
        if serves is not None:
            front.append(f"serves: {serves}")
        if chain:
            front.append(f"chain_id: {chain}")
        if claimed or folder != "inbox":
            front.append(f"claimed_at: {iso(ago + 5)}")
        if folder == "done":
            front.append("result:")
            front += [f"  status: {status}", f"  finished_at: {iso(ago)}", f"  duration_seconds: {int(hours * 3600)}",
                      f"  summary: {SECRET}", "  stats:", f"    target: {SECRET}"]
            for key, value in (stats or {}).items():
                front.append(f"    {key}: {value}")
        text = "---\n" + "\n".join(front) + "\n---\n\nbody\n"
        (self.root / "_queue_" / folder / f"{name}.md").write_text(text)
        return name

    def run_tool(self, *args, now=NOW):
        return subprocess.run([sys.executable, "-B", str(TOOL), "--root", str(self.root), "--now", now.isoformat(), *args],
                              capture_output=True, text=True)

    def alarms(self, *args):
        r = self.run_tool("--format", "json", *args)
        self.assertIn(r.returncode, (0, 1), r.stdout + r.stderr)
        return r, {a["alarm"] for a in json.loads(r.stdout)["alarms"]}

    def healthy(self):
        """Ten executed units: six serve a ranked item, one partial; the last finished 10 minutes ago."""
        for i in range(6):
            self.unit("done", ago=10 + i * 20, serves="growth-lever", status="partial" if i == 0 else "done")
        for i in range(4):
            self.unit("done", ago=30 + i * 20, serves="upkeep")


class Conforming(PoolCase):
    def test_a_conforming_pool_exits_zero_with_counts_only(self):
        self.healthy()
        self.unit("inbox", serves="upkeep")
        r = self.run_tool()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("conforming", r.stdout)
        self.assertIn("executed in window 10", r.stdout)
        self.assertIn("coverage serving a ranked item: units 60%", r.stdout)
        self.assertNotIn(SECRET, r.stdout + r.stderr)                     # no summary, target or unit text
        self.assertNotIn("mail-2026", r.stdout)                           # no unit ids either

    def test_it_writes_nothing(self):
        self.healthy()
        def digest():
            return hashlib.sha256("".join(f"{p.relative_to(self.root)}:{p.stat().st_mtime_ns}:{p.read_bytes().hex()}"
                                          for p in sorted(self.root.rglob("*")) if p.is_file()).encode()).hexdigest()
        before = digest()
        self.run_tool()
        self.run_tool("--format", "json")
        self.assertEqual(digest(), before)
        self.assertEqual(sorted(p.name for p in self.root.iterdir()), ["_queue_"])


class NoExecution(PoolCase):
    def test_forty_four_minutes_is_fine_and_forty_six_is_an_alarm(self):
        self.healthy()
        for p in (self.root / "_queue_" / "done").glob("*.md"):
            p.unlink()
        self.unit("done", ago=44, serves="growth-lever")
        self.assertNotIn("no-execution", self.alarms()[1])
        (self.root / "_queue_" / "done").joinpath(next(p.name for p in (self.root / "_queue_" / "done").iterdir())).unlink()
        self.unit("done", ago=46, serves="growth-lever")
        r, alarms = self.alarms()
        self.assertIn("no-execution", alarms)
        self.assertEqual(r.returncode, 1)

    def test_an_expired_sweep_is_not_an_execution(self):
        self.unit("done", ago=90, status="done")
        self.unit("done", ago=1, status="expired")
        self.assertIn("no-execution", self.alarms()[1])

    def test_an_empty_pool_alarms_and_the_ratios_are_not_applicable(self):
        r, alarms = self.alarms()
        self.assertEqual(alarms, {"no-execution"})
        self.assertEqual(json.loads(r.stdout)["not_applicable"][:2], ["coverage", "growth-partial"])


class IdleSlots(PoolCase):
    def read(self, ago, activity="building-queues", key="builders_idle", idle=1, **more):
        self.unit("done", ago=ago, activity=activity, serves="upkeep", stats={key: idle, **more})

    def test_a_builder_idle_for_thirty_one_minutes_alarms_and_twenty_nine_does_not(self):
        self.healthy()
        self.read(29)
        r, alarms = self.alarms()
        self.assertNotIn("idle-slot", alarms)
        self.read(31, idle=1)                                                         # an older read: the latest still counts
        self.assertNotIn("idle-slot", self.alarms()[1])
        for p in (self.root / "_queue_" / "done").glob("*.md"):
            if "activity: building-queues" in p.read_text():
                p.unlink()
        self.read(31)
        r, alarms = self.alarms()
        self.assertIn("idle-slot", alarms)
        alarm = next(a for a in json.loads(r.stdout)["alarms"] if a["alarm"] == "idle-slot")
        self.assertEqual((alarm["activity"], alarm["idle_slots"]), ("building-queues", 1))

    def test_labs_and_queue_slots_count_too(self):
        self.healthy()
        self.read(40, activity="research-queue", key="slots_idle", idle=2)
        self.read(41, activity="troop-training", key="slots_idle", idle=1)
        r, _ = self.alarms()
        found = [a for a in json.loads(r.stdout)["alarms"] if a["alarm"] == "idle-slot"]
        self.assertEqual(sorted(a["activity"] for a in found), ["research-queue", "troop-training"])

    def test_what_the_same_unit_started_is_not_idle(self):
        self.healthy()
        self.read(40, idle=1, upgrades_started=1)
        self.assertNotIn("idle-slot", self.alarms()[1])

    def test_a_busy_read_is_not_idle(self):
        self.healthy()
        self.read(120, idle=0)
        self.assertNotIn("idle-slot", self.alarms()[1])


class Coverage(PoolCase):
    def fill(self, ranked, other, hours_ranked=0.25, hours_other=0.25):
        for i in range(ranked):
            self.unit("done", ago=10 + i, serves="growth-lever", hours=hours_ranked)
        for i in range(other):
            self.unit("done", ago=10 + i, serves="snapshot", hours=hours_other)

    def test_sixty_percent_passes_and_fifty_nine_is_an_alarm(self):
        self.fill(6, 4)
        self.assertNotIn("coverage", self.alarms()[1])
        self.setUp()
        self.fill(59, 41)
        r, alarms = self.alarms()
        self.assertIn("coverage", alarms)
        self.assertEqual(next(a for a in json.loads(r.stdout)["alarms"] if a["alarm"] == "coverage")["below"], ["units", "unit-hours"])

    def test_unit_hours_can_alarm_when_the_unit_count_does_not(self):
        self.fill(6, 4, hours_ranked=0.1, hours_other=1.0)
        r, alarms = self.alarms()
        self.assertIn("coverage", alarms)
        self.assertEqual(next(a for a in json.loads(r.stdout)["alarms"] if a["alarm"] == "coverage")["below"], ["unit-hours"])

    def test_upkeep_snapshot_and_baseline_are_not_ranked_and_a_name_tells_an_untagged_unit(self):
        for tag in ("upkeep", "snapshot", "baseline"):
            self.unit("done", ago=10, serves=tag)
        self.unit("done", ago=10, serves=None, chain="growth-capacity-2026-11-23", regular="building-queues")   # ranked by name
        self.unit("done", ago=10, serves=None, regular="mail")                                                    # not
        r, _ = self.alarms()
        counts = json.loads(r.stdout)["counts"]
        self.assertEqual(counts["growth_executed"], 1)
        self.assertEqual(counts["executed_without_serves"], 2)

    def test_units_outside_the_window_do_not_count(self):
        self.fill(6, 4)
        self.unit("done", ago=13 * 60, serves="snapshot")
        self.unit("done", ago=14 * 60, serves="snapshot")
        r, _ = self.alarms("--hours", "12")
        self.assertEqual(json.loads(r.stdout)["counts"]["executed_in_window"], 10)
        r, alarms = self.alarms("--hours", "20")
        self.assertEqual(json.loads(r.stdout)["counts"]["executed_in_window"], 12)


class GrowthPartial(PoolCase):
    def test_thirty_three_percent_passes_and_fifty_is_an_alarm(self):
        for status in ("partial", "done", "done"):
            self.unit("done", ago=10, serves="growth-lever", status=status)
        r, alarms = self.alarms()
        self.assertNotIn("growth-partial", alarms)
        self.assertEqual(json.loads(r.stdout)["counts"]["growth_partial_percent"], 33)
        self.setUp()
        for status in ("partial", "partial", "done", "failed"):
            self.unit("done", ago=10, serves="growth-lever", status=status)
        self.assertIn("growth-partial", self.alarms()[1])

    def test_exactly_the_limit_is_not_over_it_and_upkeep_partials_do_not_count(self):
        for status in ["partial"] * 7 + ["done"] * 13:                               # 35 percent
            self.unit("done", ago=10, serves="growth-lever", status=status)
        for _ in range(5):
            self.unit("done", ago=10, serves="upkeep", status="partial")
        self.assertNotIn("growth-partial", self.alarms()[1])


class PlanItems(PoolCase):
    def plan(self, *rows):
        path = self.root / "plan.csv"
        path.write_text("rank,item,trigger_at,serves\n" + "".join(f"{r},{i},{t},{s}\n" for r, i, t, s in rows))
        return str(path)

    def test_a_top_item_not_started_two_hours_after_its_trigger_alarms(self):
        self.healthy()
        plan = self.plan((1, "capacity-first", iso(181), "p2-capacity"))
        r, alarms = self.alarms("--plan", plan)
        self.assertIn("plan-item", alarms)
        alarm = next(a for a in json.loads(r.stdout)["alarms"] if a["alarm"] == "plan-item")
        self.assertEqual((alarm["item"], alarm["rank"]), ("capacity-first", 1))
        self.assertGreaterEqual(alarm["hours_past_trigger"], 3.0)

    def test_inside_the_grace_or_started_or_ranked_below_the_top_is_not_an_alarm(self):
        self.healthy()
        self.assertNotIn("plan-item", self.alarms("--plan", self.plan((1, "a", iso(100), "p2-capacity")))[1])         # 1h40m
        self.assertNotIn("plan-item", self.alarms("--plan", self.plan((4, "late-and-low", iso(600), "p9-other")))[1])  # rank 4
        plan = self.plan((1, "capacity-first", iso(600), "p2-capacity"))
        self.assertIn("plan-item", self.alarms("--plan", plan)[1])
        self.unit("claimed", ago=30, serves="p2-capacity")                                                              # now started
        self.assertNotIn("plan-item", self.alarms("--plan", plan)[1])

    def test_a_finished_unit_with_the_tag_also_counts_as_started_but_an_expired_one_does_not(self):
        self.healthy()
        plan = self.plan((1, "capacity-first", iso(600), "p2-capacity"))
        self.unit("done", ago=500, serves="p2-capacity", status="expired")
        self.assertIn("plan-item", self.alarms("--plan", plan)[1])
        self.unit("done", ago=200, serves="p2-capacity", status="partial")
        self.assertNotIn("plan-item", self.alarms("--plan", plan)[1])

    def test_without_a_plan_file_the_check_is_skipped_and_says_so(self):
        self.healthy()
        r, _ = self.alarms()
        self.assertIn("plan-item (no plan file)", json.loads(r.stdout)["not_applicable"])
        r, _ = self.alarms("--plan", str(self.root / "nope.csv"))
        self.assertIn("plan-item (no plan file)", json.loads(r.stdout)["not_applicable"])


class Cli(PoolCase):
    def test_text_names_each_alarm_and_exits_one(self):
        self.unit("done", ago=100, serves="snapshot", status="partial")
        r = self.run_tool()
        self.assertEqual(r.returncode, 1)
        self.assertIn("ALARM no-execution", r.stdout)
        self.assertIn("ALARM coverage", r.stdout)

    def test_an_unreadable_queue_and_a_bad_time_exit_two(self):
        shutil.rmtree(self.root / "_queue_" / "claimed")
        r = self.run_tool()
        self.assertEqual(r.returncode, 2)
        self.assertIn("cannot read the queue", r.stderr)
        self.setUp()
        bad = subprocess.run([sys.executable, "-B", str(TOOL), "--root", str(self.root), "--now", "yesterday"], capture_output=True, text=True)
        self.assertEqual(bad.returncode, 2)

    def test_thresholds_are_flags(self):
        self.unit("done", ago=50, serves="growth-lever")
        self.assertEqual(self.alarms("--stale-minutes", "60")[1] & {"no-execution"}, set())
        self.assertIn("no-execution", self.alarms("--stale-minutes", "40")[1])

    def test_the_real_repository_runs_and_names_only_counts(self):
        real = TOOL.parent.parent.parent
        if not (real / "_queue_" / "done").is_dir():
            self.skipTest("no queue folders in this checkout")
        r = subprocess.run([sys.executable, "-B", str(TOOL), "--root", str(real)], capture_output=True, text=True)
        self.assertIn(r.returncode, (0, 1), r.stdout + r.stderr)
        self.assertIn("== STRATEGY CONFORMANCE", r.stdout)


if __name__ == "__main__":
    unittest.main()
