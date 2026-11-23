"""Tests for the forecast switch: `coordination.queue.require_forecast: true` in TEAM.yaml (LASTWAR_TEAM_FILE in these tests) makes every code path that
creates a unit refuse one whose serves is not a ledger plan item or an exempt word - `enqueue`, and the minting of `plan`, `sweep` and `sync` - with
`--no-require-forecast` as the emergency override and the refusal naming it. Off when the key or the file is absent.

Run: python3 -m unittest discover -s _tools_/queue-tests
"""
from __future__ import annotations

import datetime
import json
import re
import shutil
import subprocess
import sys

from test_forecast import ForecastCase
from test_serves import QUEUE, load_queue_module

REAL_ROSTER = json.loads((QUEUE.parent / "regulars.json").read_text(encoding="utf-8"))
SWITCH_ON = "coordination:\n  queue:\n    require_forecast: true\n"


class Switchable(ForecastCase):
    def setUp(self):
        super().setUp()
        self.team_path = self.repo / "TEAM.yaml"
        self.env["LASTWAR_TEAM_FILE"] = str(self.team_path)

    def team(self, text=SWITCH_ON):
        self.team_path.write_text(text)

    def roster(self, name, serves, only=None):
        """The real roster with one regular's serves replaced (or only that regular, for plan)."""
        items = [dict(r, serves=serves) if r["id"] == name else r for r in REAL_ROSTER["regulars"]]
        if only:
            items = [r for r in items if r["id"] == only]
        path = self.repo / f"roster-{name}-{len(serves)}.json"
        path.write_text(json.dumps({**REAL_ROSTER, "regulars": items}))
        return path

    def inbox(self):
        return sorted(p.name for p in (self.pool / "inbox").glob("*.md"))

    def enqueue_raw(self, serves, *extra, regular="regular-1", activity="activity-1"):
        return self.queue("enqueue", "--regular", regular, "--activity", activity, "--est-minutes", "5", "--serves", serves, *extra)


class Switch(Switchable):
    def test_off_when_the_file_or_the_key_is_absent(self):
        self.assertEqual(self.enqueue_raw("PL-99").returncode, 0)                        # no TEAM file at all
        self.team("coordination:\n  execution:\n    approved_model: x\n")
        self.assertEqual(self.enqueue_raw("PL-99", regular="regular-2", activity="activity-2").returncode, 0)
        self.team("coordination:\n  queue:\n    require_forecast: false\n")
        self.assertEqual(self.enqueue_raw("PL-99", regular="regular-3", activity="activity-3").returncode, 0)

    def test_on_by_the_key_alone_and_the_refusal_names_the_source_and_the_override(self):
        self.team()
        r = self.enqueue_raw("PL-99")
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("forecast check (coordination.queue.require_forecast in TEAM.yaml)", r.stdout)
        self.assertIn("plan item id that has no row in the forecast ledger", r.stdout)
        self.assertIn("for an emergency enqueue pass --no-require-forecast", r.stdout)
        self.assertEqual(self.inbox(), [])
        for serves in ("PL-01", "upkeep", "baseline", "snapshot", "fill idle slot with research"):
            self.assertEqual(self.enqueue_raw(serves, regular="r-" + re.sub(r"\W", "", serves), activity="a-" + re.sub(r"\W", "", serves)).returncode, 0, serves)

    def test_the_key_must_sit_at_coordination_queue(self):
        for text in ("queue:\n  require_forecast: true\n", "coordination:\n  require_forecast: true\n",
                     "coordination:\n  execution:\n    require_forecast: true\n"):
            self.team(text)
            self.assertEqual(self.enqueue_raw("PL-99").returncode, 0, text)
            shutil.rmtree(self.pool / "inbox")
            (self.pool / "inbox").mkdir()

    def test_quoted_true_and_the_other_spellings_count(self):
        for value in ("'true'", "yes", "True"):
            self.team(f"coordination:\n  queue:\n    require_forecast: {value}\n")
            self.assertEqual(self.enqueue_raw("PL-99").returncode, 1, value)

    def test_an_unreadable_team_file_warns_and_is_off(self):
        self.team("coordination: [unclosed\n")
        r = self.enqueue_raw("PL-99")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("require_forecast is treated as off", r.stderr)

    def test_the_emergency_override_and_the_flag_that_forces_it_on(self):
        self.team()
        ok = self.enqueue_raw("PL-99", "--no-require-forecast")
        self.assertEqual(ok.returncode, 0, ok.stdout + ok.stderr)
        self.team("coordination:\n  queue:\n    require_forecast: false\n")
        forced = self.enqueue_raw("PL-99", "--require-forecast", regular="regular-2", activity="activity-2")
        self.assertEqual(forced.returncode, 1)
        both = self.enqueue_raw("PL-99", "--require-forecast", "--no-require-forecast", regular="regular-3", activity="activity-3")
        self.assertEqual(both.returncode, 2)
        self.assertIn("contradict each other", both.stdout)

    def test_without_pyyaml_the_indentation_scanner_reads_the_same_key(self):
        q = load_queue_module()
        self.assertEqual(q._scan_require_forecast(SWITCH_ON), "true")
        self.assertEqual(q._scan_require_forecast("coordination:\n  queue:\n    require_forecast: true  # flipped\nseats:\n"), "true")
        self.assertIsNone(q._scan_require_forecast("queue:\n  require_forecast: true\n"))
        self.assertIsNone(q._scan_require_forecast("coordination:\n  execution:\n    approved_model: x\n  queue:\n    other: 1\n"))
        self.assertEqual(q._scan_require_forecast("coordination:\n  execution:\n    a: 1\n  queue:\n    require_forecast: false\n"), "false")


class Paths(Switchable):
    """One test per path that creates a unit."""

    def setUp(self):
        super().setUp()
        self.team()

    def test_enqueue_a_roster_regular_inherits_upkeep_and_passes_a_custom_serves_is_judged(self):
        roster = self.repo / "roster.json"
        roster.write_text(json.dumps({"version": 1, "regulars": [{"id": "mail", "activity": "mail-rewards", "cadence": "every-run", "serves": "upkeep"}]}))
        r = self.queue("enqueue", "--regulars-json", str(roster), "--regular", "mail", "--est-minutes", "5")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        roster.write_text(json.dumps({"version": 1, "regulars": [{"id": "mail", "activity": "mail-rewards", "cadence": "every-run", "serves": "PL-99"}]}))
        r = self.queue("enqueue", "--regulars-json", str(roster), "--regular", "mail", "--segment", "2", "--est-minutes", "5")
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("no row in the forecast ledger", r.stdout)

    def plan(self, serves, *extra):
        roster = self.roster("mail", serves, only="mail")
        r = self.queue("plan", "--regulars-json", str(roster), "--hours", "2", *extra)
        self.assertIn(r.returncode, (0, 1), r.stdout + r.stderr)
        return r, json.loads(r.stdout[r.stdout.index("{"):r.stdout.rindex("}") + 1])

    def test_plan_refuses_to_mint_a_unit_whose_roster_serves_has_no_ledger_row(self):
        r, out = self.plan("PL-99")
        self.assertEqual(r.returncode, 1)
        self.assertEqual(out["planned"], [])
        self.assertTrue(out["forecast_refusals"])
        self.assertEqual({f["reason"] for f in out["forecast_refusals"]}, {"no-row"})
        self.assertEqual(sorted(out["skipped_forecast_refusals"]), sorted(f["unit"] for f in out["forecast_refusals"]))
        self.assertEqual(out["already_present"], 0)                                      # a refusal is not "already present"
        self.assertEqual(self.inbox(), [])
        self.assertIn("fails the forecast check (no-row)", r.stderr)

    def test_plan_mints_for_a_ledger_row_an_exempt_serves_the_override_and_the_switch_off(self):
        for serves, extra in (("PL-01", ()), ("upkeep", ()), ("fill idle slot with research", ()), ("PL-99", ("--no-require-forecast",))):
            self.setUp()
            r, out = self.plan(serves, *extra)
            self.assertEqual(r.returncode, 0, f"{serves}: {r.stdout}{r.stderr}")
            self.assertTrue(out["planned"], serves)
            self.assertEqual(out["forecast_refusals"], [])
        self.setUp()
        self.team("coordination:\n  queue:\n    require_forecast: false\n")
        self.assertTrue(self.plan("PL-99")[1]["planned"])

    def test_sweep_refuses_to_mint_the_sweep_when_the_roster_serves_has_no_ledger_row(self):
        tomorrow = (datetime.date.today() + datetime.timedelta(days=1)).isoformat()
        roster = self.roster("zero-sweep", "PL-99")
        r = self.queue("sweep", "--regulars-json", str(roster), "--date", tomorrow)
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        out = json.loads(r.stdout[r.stdout.index("{"):r.stdout.rindex("}") + 1])
        self.assertEqual(out["produced"], [])
        self.assertTrue(out["skipped_forecast_refusals"])
        self.assertTrue(all(f["regular"] == "zero-sweep" for f in out["forecast_refusals"]))
        self.assertFalse(any(n.startswith("zero-sweep") for n in self.inbox()))
        ok = self.queue("sweep", "--regulars-json", str(self.roster("zero-sweep", "PL-01")), "--date", tomorrow)
        self.assertEqual(ok.returncode, 0, ok.stdout + ok.stderr)
        self.assertTrue(json.loads(ok.stdout[ok.stdout.index("{"):ok.stdout.rindex("}") + 1])["produced"])

    def test_sync_refuses_to_mint_a_due_regular_whose_serves_has_no_ledger_row(self):
        mail = next(dict(r, serves="PL-99", due=True) for r in REAL_ROSTER["regulars"] if r["id"] == "mail")
        due = self.repo / "due.json"
        due.write_text(json.dumps({"items": [mail]}))
        r = self.queue("sync", "--due-json", str(due))
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        out = json.loads(r.stdout[r.stdout.index("{"):r.stdout.rindex("}") + 1])
        self.assertEqual(out["produced"], [])
        self.assertEqual(out["already_queued"], [])
        self.assertEqual([f["regular"] for f in out["forecast_refusals"]], ["mail"])
        self.assertEqual(self.inbox(), [])
        ok = self.queue("sync", "--due-json", str(due), "--no-require-forecast")
        self.assertEqual(ok.returncode, 0, ok.stdout + ok.stderr)
        self.assertTrue(json.loads(ok.stdout[ok.stdout.index("{"):ok.stdout.rindex("}") + 1])["produced"])

    def test_sync_still_mints_the_real_rosters_upkeep_units_when_the_switch_is_on(self):
        mail = next(dict(r, due=True) for r in REAL_ROSTER["regulars"] if r["id"] == "mail")
        due = self.repo / "due.json"
        due.write_text(json.dumps({"items": [mail]}))
        r = self.queue("sync", "--due-json", str(due))
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertEqual(len(self.inbox()), 1)

    def test_the_minting_commands_take_both_flags(self):
        for command in ("plan", "sweep", "sync", "enqueue"):
            out = self.queue(command, "--help").stdout
            self.assertIn("--no-require-forecast", out, command)
            self.assertIn("--require-forecast", out, command)

    def test_the_real_roster_has_nothing_the_switch_would_refuse(self):
        serves = {r.get("serves", "upkeep") for r in REAL_ROSTER["regulars"]}
        q = load_queue_module()
        self.assertEqual({q.forecast_class(s, set()) for s in serves}, {"ok"})


class ScoutDiffPath(Switchable):
    """scout_diff.py feeds every enqueue entry to `queue.py enqueue`; the switch reaches it through that call."""

    def setUp(self):
        super().setUp()
        import importlib.util
        spec = importlib.util.spec_from_file_location("scout_diff_under_test", QUEUE.parent / "scout_diff.py")
        self.scout = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.scout)
        tools = self.repo / "toolcopy" / "_tools_"
        tools.mkdir(parents=True)
        shutil.copy(QUEUE, tools / "queue.py")
        self.tool_copy = tools
        import os
        for key, value in self.env.items():
            if key.startswith("LASTWAR_"):
                self.addCleanup(os.environ.pop, key, None)
                os.environ[key] = value

    def entry(self):
        return {"action": "enqueue", "regular": "mail", "activity": "mail-rewards", "priority": 3, "est_minutes": 5, "window": "scout window",
                "segment": "", "expires_at": "", "not_before": "", "chain_id": ""}

    def apply(self, serves):
        (self.tool_copy / "regulars.json").write_text(json.dumps({"version": 1, "regulars": [
            {"id": "mail", "activity": "mail-rewards", "cadence": "every-run", "serves": serves}]}))
        return self.scout.apply_enqueue_plan([self.entry()], str(self.pool), str(self.tool_copy / "queue.py"))

    def test_a_unit_whose_roster_serves_has_no_ledger_row_is_refused_through_the_enqueue_call(self):
        self.team()
        applied, failures = self.apply("PL-99")
        self.assertEqual(applied, [])
        self.assertEqual([f["entry"] for f in failures], ["mail"])
        self.assertIn("refused: forecast check (coordination.queue.require_forecast in TEAM.yaml)", failures[0]["output"])
        self.assertEqual(self.inbox(), [])

    def test_the_same_entry_is_queued_with_a_ledger_row_an_exempt_serves_or_the_switch_off(self):
        self.team()
        for serves in ("PL-01", "upkeep"):
            self.setUp()
            self.team()
            applied, failures = self.apply(serves)
            self.assertEqual((len(applied), failures), (1, []), serves)
        self.setUp()
        self.team("coordination:\n  queue:\n    require_forecast: false\n")
        self.assertEqual(len(self.apply("PL-99")[0]), 1)
