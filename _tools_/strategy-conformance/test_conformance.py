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
        self.ledger("PL-01", "PL-02", "PL-17")
        self.n = 0

    def ledger(self, *ids):
        """The newest forecast ledger beside the queue: the plan items a unit may serve (queue.py validate reads the same file)."""
        folder = self.root / "_records_" / "2026-11-23" / "strategy"
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "forecast-ledger.csv").write_text("forecast_id,plan_item,lever\n" + "".join(f"F-{n},{i},read\n" for n, i in enumerate(ids, 1)))

    def unit(self, folder, ago=10, status="done", serves="PL-01", activity="mail-rewards", hours=0.25, stats=None,
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
            self.unit("done", ago=10 + i * 20, serves="PL-01", status="partial" if i == 0 else "done")
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
        self.assertEqual(sorted(p.name for p in self.root.iterdir()), ["_queue_", "_records_"])          # the queue and the ledger fixture, nothing new


class NoExecution(PoolCase):
    def test_forty_four_minutes_is_fine_and_forty_six_is_an_alarm(self):
        self.healthy()
        for p in (self.root / "_queue_" / "done").glob("*.md"):
            p.unlink()
        self.unit("done", ago=44, serves="PL-01")
        self.assertNotIn("no-execution", self.alarms()[1])
        (self.root / "_queue_" / "done").joinpath(next(p.name for p in (self.root / "_queue_" / "done").iterdir())).unlink()
        self.unit("done", ago=46, serves="PL-01")
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


class BlockedByCapacity(PoolCase):
    """The planner's slot-read units write slots_blocked_capacity beside the idle count; it is subtracted from every idle key and printed beside it
    (the barracks queues blocked by Drill Ground Full)."""
    TEXT = "blocked by capacity: Drill Ground Full"

    def read(self, ago, activity="troop-training", key="slots_idle", idle=1, **more):
        self.unit("done", ago=ago, activity=activity, serves="upkeep", stats={key: idle, **more})

    def rows(self):
        r = self.run_tool("--format", "json")
        return r, json.loads(r.stdout)

    def row(self, activity="troop-training"):
        return next(x for x in self.rows()[1]["counts"]["slot_reads"] if x["activity"] == activity)

    def test_one_blocked_slot_and_one_idle_slot_alarm_for_the_idle_one_only(self):
        self.healthy()
        self.read(60, idle=2, slots_blocked_capacity=1, slots_blocked_note=self.TEXT)
        r, data = self.rows()
        alarm = next(a for a in data["alarms"] if a["alarm"] == "idle-slot")
        self.assertEqual((alarm["activity"], alarm["idle_slots"]), ("troop-training", 1))
        row = self.row()
        self.assertEqual((row["idle_slots"], row["slots_blocked_capacity"], row["blocker"]), (1, 1, "Drill Ground Full"))
        self.assertIn("slot read troop-training: 1 idle + 1 blocked by capacity (Drill Ground Full)", self.run_tool().stdout)

    def test_a_slot_that_is_only_blocked_does_not_alarm_and_is_still_printed(self):
        self.healthy()
        self.read(60, idle=1, slots_blocked_capacity=1, slots_blocked_note=self.TEXT)
        r, alarms = self.alarms()
        self.assertNotIn("idle-slot", alarms)
        self.assertIn("slot read troop-training: 0 idle + 1 blocked by capacity (Drill Ground Full)", self.run_tool().stdout)

    def test_it_is_subtracted_from_every_idle_key(self):
        for key in ("builders_idle", "slots_idle", "queue_slots_idle", "queues_idle", "labs_idle", "idle_slots"):
            self.setUp()
            self.healthy()
            self.read(60, activity="building-queues", key=key, idle=2, slots_blocked_capacity=1)
            r, data = self.rows()
            alarm = next(a for a in data["alarms"] if a["alarm"] == "idle-slot")
            self.assertEqual(alarm["idle_slots"], 1, key)
            self.assertEqual(self.row("building-queues")["slots_blocked_capacity"], 1, key)

    def test_the_planners_count_is_subtracted_even_when_no_blocker_text_comes_with_it(self):
        self.healthy()
        self.read(60, idle=1, slots_blocked_capacity=1)
        self.assertNotIn("idle-slot", self.alarms()[1])
        self.assertIn("1 blocked by capacity (blocker not named)", self.run_tool().stdout)

    def test_the_count_is_capped_at_the_open_slots_and_what_the_unit_started_comes_off_first(self):
        self.healthy()
        self.read(60, idle=1, slots_blocked_capacity=5, slots_blocked_note=self.TEXT)
        self.assertNotIn("idle-slot", self.alarms()[1])
        self.assertEqual(self.row()["slots_blocked_capacity"], 1)
        self.setUp()
        self.healthy()
        self.read(60, activity="building-queues", key="builders_idle", idle=3, upgrades_started=1, slots_blocked_capacity=2)
        self.assertNotIn("idle-slot", self.alarms()[1])                          # 3 idle - 1 started = 2 open, 2 blocked

    def test_the_earlier_names_and_the_blocker_keys_still_work(self):
        self.healthy()
        self.read(60, idle=1, slots_blocked_by_capacity=1, capacity_blocker="Drill Ground Full")
        self.assertNotIn("idle-slot", self.alarms()[1])
        self.assertEqual(self.row()["blocker"], "Drill Ground Full")

    def test_the_screen_blocking_stats_are_not_a_capacity_blocker(self):
        self.healthy()
        self.read(60, idle=1, slots_blocked_capacity=1, blocker_category="b", blocker_overlay="daily-popup")
        self.assertEqual(self.row()["blocker"], "")

    def test_the_blocker_text_is_short_and_nothing_else_of_the_unit_is_printed(self):
        self.healthy()
        self.read(60, idle=1, slots_blocked_capacity=1, slots_blocked_note="x" * 90)
        out = self.run_tool().stdout
        self.assertNotIn("x" * 41, out)
        self.assertNotIn(SECRET, out)

    def test_without_the_stat_nothing_changes(self):
        self.healthy()
        self.read(60, idle=1)
        r, data = self.rows()
        self.assertIn("idle-slot", {a["alarm"] for a in data["alarms"]})
        self.assertNotIn("slots_blocked_capacity", self.row())


class RankedExactly(PoolCase):
    """A serves is ranked only by queue.py validate's exact check: a plan item id with a ledger row. Wording around an exempt word is not."""

    def kinds(self):
        r = self.run_tool("--format", "json")
        self.assertIn(r.returncode, (0, 1), r.stdout + r.stderr)
        return json.loads(r.stdout)["counts"], r

    def test_snapshot_with_a_note_is_not_ranked_and_is_counted_as_other_wording(self):
        self.unit("done", ago=10, serves="snapshot (Story 868)")
        self.unit("done", ago=11, serves="PL-01")
        counts, r = self.kinds()
        self.assertEqual(counts["serves_kinds"]["unrecognised"], 1)
        self.assertEqual(counts["serves_kinds"]["ranked"], 1)
        self.assertEqual(counts["coverage_units_percent"], 50)                      # the old rule counted 100
        self.assertIn("other wording 1 (not ranked)", self.run_tool().stdout)

    def test_an_id_without_a_ledger_row_is_not_ranked_and_is_counted_apart(self):
        self.unit("done", ago=10, serves="PL-99")
        self.unit("done", ago=11, serves="PL-17")
        counts, _ = self.kinds()
        self.assertEqual((counts["serves_kinds"]["no_row"], counts["serves_kinds"]["ranked"]), (1, 1))
        self.assertEqual(counts["coverage_units_percent"], 50)
        self.assertIn("id without a ledger row 1 (not ranked)", self.run_tool().stdout)

    def test_exempt_words_and_fill_idle_slot_are_exempt_and_a_list_with_one_row_is_ranked(self):
        for tag in ("upkeep", "Snapshot", "baseline", "fill idle slot with research"):
            self.unit("done", ago=10, serves=tag)
        self.unit("done", ago=10, serves="upkeep, PL-02")
        self.unit("done", ago=10, serves="upkeep; unknown words")
        counts, _ = self.kinds()
        self.assertEqual(counts["serves_kinds"], {"ranked": 1, "exempt": 4, "no_row": 0, "unrecognised": 1, "no_serves_line": 0, "ranked_by_name": 0})

    def test_an_id_in_the_wrong_case_is_other_wording_like_validate_says(self):
        self.unit("done", ago=10, serves="pl-01")
        counts, _ = self.kinds()
        self.assertEqual(counts["serves_kinds"]["unrecognised"], 1)

    def test_with_no_ledger_an_id_counts_by_its_shape_and_the_output_says_so(self):
        (self.root / "_records_" / "2026-11-23" / "strategy" / "forecast-ledger.csv").unlink()
        self.unit("done", ago=10, serves="PL-99")
        counts, _ = self.kinds()
        self.assertEqual(counts["serves_kinds"]["ranked"], 1)
        self.assertIn("id shape only, ranked by wording only", counts["ranking_basis"])
        self.assertIn("ranking basis: id shape only, ranked by wording only", self.run_tool().stdout)
        self.assertEqual(self.kinds()[0]["ranking_basis"].startswith("id shape only"), True)

    def test_with_a_ledger_the_basis_is_the_ledger_rows(self):
        self.unit("done", ago=10, serves="PL-01")
        self.assertEqual(self.kinds()[0]["ranking_basis"], "ledger rows")

    def test_units_without_a_serves_line_keep_the_name_rule_and_are_counted(self):
        self.unit("done", ago=10, serves=None, chain="growth-capacity-2026-11-23", regular="building-queues")
        self.unit("done", ago=10, serves=None, regular="mail")
        counts, _ = self.kinds()
        self.assertEqual((counts["serves_kinds"]["no_serves_line"], counts["serves_kinds"]["ranked_by_name"]), (2, 1))

    def test_it_is_the_check_queue_py_validate_uses(self):
        import importlib.util
        spec = importlib.util.spec_from_file_location("q", TOOL.parent.parent / "queue.py")
        q = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(q)
        spec = importlib.util.spec_from_file_location("sc", TOOL)
        sc = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(sc)
        self.assertEqual(sc.NON_RANKED, set(q.FORECAST_EXEMPT))                                    # the fallback words are the exempt words
        self.assertEqual(sc.PLAN_ITEM.pattern, q.PLAN_ITEM_ID.pattern)
        self.assertEqual(sc.FILL_IDLE.pattern, q.FORECAST_FILL.pattern)
        sc.RANKING.update(ids={"PL-01"}, queue=q)
        for serves in ("upkeep", "PL-01", "PL-99", "snapshot (Story 868)", "upkeep, PL-01", "fill idle slot x", "pl-01", ""):
            want = q.forecast_class(serves, {"PL-01"})
            kind = sc.serves_kind(serves)
            self.assertEqual({"ok": kind in ("ranked", "exempt"), "no-row": kind == "no-row", "unknown": kind == "unrecognised"}[want], True, (serves, want, kind))


class Coverage(PoolCase):
    def fill(self, ranked, other, hours_ranked=0.25, hours_other=0.25):
        for i in range(ranked):
            self.unit("done", ago=10 + i, serves="PL-01", hours=hours_ranked)
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
            self.unit("done", ago=10, serves="PL-01", status=status)
        r, alarms = self.alarms()
        self.assertNotIn("growth-partial", alarms)
        self.assertEqual(json.loads(r.stdout)["counts"]["growth_partial_percent"], 33)
        self.setUp()
        for status in ("partial", "partial", "done", "failed"):
            self.unit("done", ago=10, serves="PL-01", status=status)
        self.assertIn("growth-partial", self.alarms()[1])

    def test_exactly_the_limit_is_not_over_it_and_upkeep_partials_do_not_count(self):
        for status in ["partial"] * 7 + ["done"] * 13:                               # 35 percent
            self.unit("done", ago=10, serves="PL-01", status=status)
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
        self.unit("done", ago=50, serves="PL-01")
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
