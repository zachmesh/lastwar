"""Tests for strategist_health.py: each check at its threshold, calibration arithmetic, counts-only output and read-only
behaviour. Every repository, ledger and relay here is made up in a temporary folder.

Run: python3 -m unittest discover -s _tools_/strategist-health
"""
from __future__ import annotations

import csv
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

TOOL = Path(__file__).resolve().parent / "strategist_health.py"
NOW = datetime(2026, 11, 23, 12, 0, tzinfo=timezone.utc)
CLAIM_TEXT = "a claim sentence that must never be printed"
REGISTER_FIELDS = ["id", "claim", "source", "tag", "test", "owner_seat", "read_by_utc", "status", "effect_if_false"]
LEDGER_FIELDS = ["forecast_id", "plan_item", "lever", "metric", "kind", "p_success", "value_if_success", "predicted_low",
                 "predicted_point", "predicted_high", "tolerance_pct", "value_source", "p_source", "created_at_utc", "actual_value",
                 "actual_realized", "actual_start"]


def iso(hours_ago=0.0, dt=NOW):
    return (dt - timedelta(hours=hours_ago)).strftime("%Y-%m-%dT%H:%MZ")


def git(root, *args):
    return subprocess.run(["git", "-C", str(root), "-c", "user.email=t@example.org", "-c", "user.name=t", *args],
                          capture_output=True, text=True, check=True)


class Repo(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp(prefix="strategist-health-"))
        self.addCleanup(shutil.rmtree, self.root, True)
        subprocess.run(["git", "init", "-q", "-b", "main", str(self.root)], check=True)
        self.dir = self.root / "_records_" / "2026-11-23" / "strategy"
        self.dir.mkdir(parents=True)

    def write(self, name, text, age_hours=1.0, commit=True):
        path = self.dir / name
        path.write_text(text)
        t = (NOW - timedelta(hours=age_hours)).timestamp()
        os.utime(path, (t, t))
        if commit:
            git(self.root, "add", "--", str(path))
            subprocess.run(["git", "-C", str(self.root), "-c", "user.email=t@example.org", "-c", "user.name=t", "commit", "-q", "-m", name,
                            "--no-verify"], capture_output=True)                     # a rewrite with the same text commits nothing
        return path

    def csv_text(self, fields, rows):
        buf = io.StringIO()
        writer = csv.DictWriter(buf, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
        return buf.getvalue()

    def register(self, rows, **kw):
        full = [{"id": f"H{i:02d}", "claim": CLAIM_TEXT, "source": "s", "tag": "M", "test": "re-read it", "owner_seat": "scout",
                 "read_by_utc": iso(-5), "status": "open", "effect_if_false": "n/a", **r} for i, r in enumerate(rows, 1)]
        return self.write("hypothesis-register.csv", self.csv_text(REGISTER_FIELDS, full), **kw)

    def ledger(self, rows, **kw):
        full = [{"forecast_id": f"F-{i:03d}", "created_at_utc": iso(30), **r} for i, r in enumerate(rows, 1)]
        return self.write("forecast-ledger.csv", self.csv_text(LEDGER_FIELDS, full), **kw)

    def healthy_base(self):
        self.write("plan-of-record.csv", "id,lever\nPL-01,read\n")
        self.register([{}, {}])
        self.ledger([])

    def run_tool(self, *args, env=None):
        full = dict(os.environ)
        full.pop("STRATEGIST_HEALTH_RELAY", None)
        full.update(env or {})
        return subprocess.run([sys.executable, "-B", str(TOOL), "--root", str(self.root), "--now", NOW.isoformat(), "--no-session", *args],
                              capture_output=True, text=True, env=full)

    def result(self, *args, **kw):
        r = self.run_tool("--format", "json", *args, **kw)
        self.assertIn(r.returncode, (0, 1), r.stdout + r.stderr)
        data = json.loads(r.stdout)
        return r, data, {a["alarm"] for a in data["alarms"]}


class Durability(Repo):
    def test_committed_strategy_files_are_landed(self):
        self.healthy_base()
        r, data, alarms = self.result()
        self.assertNotIn("durability", alarms)
        self.assertEqual(data["checks"]["durability"]["untracked"], 0)

    def test_an_untracked_file_over_two_hours_alarms_and_under_two_does_not(self):
        self.healthy_base()
        self.write("notes.md", "x", age_hours=1.9, commit=False)
        r, data, alarms = self.result()
        self.assertNotIn("durability", alarms)
        self.assertEqual(data["checks"]["durability"]["untracked"], 1)
        self.write("notes.md", "x", age_hours=2.1, commit=False)
        r, data, alarms = self.result()
        self.assertIn("durability", alarms)
        self.assertEqual(r.returncode, 1)
        self.assertEqual(next(a for a in data["alarms"] if a["alarm"] == "durability")["untracked_over_limit"], 1)

    def test_a_modified_uncommitted_file_counts_by_its_own_age(self):
        self.healthy_base()
        self.write("plan-of-record.csv", "id,lever\nPL-01,read\nPL-02,x\n", age_hours=3, commit=False)
        r, data, alarms = self.result()
        self.assertIn("durability", alarms)
        self.assertEqual(data["checks"]["durability"]["modified_uncommitted"], 1)
        self.write("plan-of-record.csv", "id,lever\nPL-01,read\nPL-02,x\n", age_hours=0.5, commit=False)
        self.assertNotIn("durability", self.result()[2])

    def test_a_flag_moves_the_limit(self):
        self.healthy_base()
        self.write("notes.md", "x", age_hours=3, commit=False)
        self.assertNotIn("durability", self.result("--untracked-hours", "4")[2])


class Freshness(Repo):
    def test_a_key_file_older_than_twelve_hours_alarms(self):
        self.write("plan-of-record.csv", "id\nPL-01\n", age_hours=11.9)
        r, data, alarms = self.result()
        self.assertNotIn("freshness", alarms)
        self.write("plan-of-record.csv", "id\nPL-01\n", age_hours=12.5)
        r, data, alarms = self.result()
        self.assertIn("freshness", alarms)

    def test_the_newest_key_file_counts_not_the_oldest(self):
        self.write("plan-of-record.csv", "id\nPL-01\n", age_hours=30)
        self.register([{}], age_hours=1)
        self.assertNotIn("freshness", self.result()[2])

    def test_a_missing_plan_of_record_alarms_once_strategy_files_exist(self):
        self.register([{}], age_hours=1)
        r, data, alarms = self.result()
        self.assertIn("no-plan-of-record", alarms)

    def test_no_strategy_files_at_all_is_not_applicable(self):
        shutil.rmtree(self.root / "_records_")
        r, data, alarms = self.result()
        self.assertEqual(alarms, set())
        self.assertTrue(any(n.startswith("freshness") for n in data["not_applicable"]))


class Register(Repo):
    def test_a_complete_register_with_nothing_overdue_is_healthy(self):
        self.healthy_base()
        self.register([{}, {"status": "confirmed (4 panels)"}])
        r, data, alarms = self.result()
        self.assertFalse(alarms & {"register-incomplete", "register-overdue"})
        self.assertEqual(data["checks"]["register"]["claims"], 2)
        self.assertEqual((data["checks"]["register"]["open"], data["checks"]["register"]["closed"]), (1, 1))

    def test_a_claim_without_a_test_an_owner_or_a_read_by_date_is_incomplete(self):
        self.healthy_base()
        for field in ("test", "owner_seat", "read_by_utc"):
            self.register([{}, {field: ""}])
            r, data, alarms = self.result()
            self.assertIn("register-incomplete", alarms, field)
        self.register([{}, {"read_by_utc": "tomorrow-ish"}])
        self.assertIn("register-incomplete", self.result()[2])                      # an unreadable date is not a date

    def test_an_open_claim_past_its_read_by_is_overdue_and_a_closed_one_is_not(self):
        self.healthy_base()
        self.register([{"read_by_utc": iso(1)}])
        r, data, alarms = self.result()
        self.assertIn("register-overdue", alarms)
        self.assertEqual(data["checks"]["register"]["overdue_open_reads"], 1)
        self.register([{"read_by_utc": iso(1), "status": "retired"}])
        self.assertNotIn("register-overdue", self.result()[2])
        self.register([{"read_by_utc": iso(-0.1)}])                                  # due in six minutes: not yet overdue
        self.assertNotIn("register-overdue", self.result()[2])

    def test_the_output_names_no_claim_and_no_id(self):
        self.healthy_base()
        self.register([{"read_by_utc": iso(1)}])
        r = self.run_tool()
        self.assertNotIn(CLAIM_TEXT, r.stdout + r.stderr)
        self.assertNotIn("H01", r.stdout)


class Forecasts(Repo):
    def binary(self, p, realized, tag="M"):
        return {"kind": "binary", "p_success": p, "actual_realized": realized, "p_source": tag}

    def cont(self, low, point, high, actual, tag="M"):
        return {"kind": "continuous", "predicted_low": low, "predicted_point": point, "predicted_high": high, "actual_value": actual,
                "value_source": tag}

    def test_brier_is_the_mean_squared_error_and_reliability_is_by_band(self):
        self.write("plan-of-record.csv", "id\nPL-01\n")
        self.ledger([self.binary(0.9, 1), self.binary(0.8, 1), self.binary(0.7, 0), self.binary(0.3, 0), self.binary(0.2, 1)])
        r, data, alarms = self.result()
        expected = ((0.1) ** 2 + (0.2) ** 2 + (0.7) ** 2 + (0.3) ** 2 + (0.8) ** 2) / 5
        self.assertAlmostEqual(data["checks"]["forecasts"]["brier"], round(expected, 3))
        self.assertIn("brier", alarms)                                                 # 1.27 / 5 = 0.254, just over the 0.25 limit
        bands = {b["band"]: b for b in data["checks"]["forecasts"]["reliability"]}
        self.assertEqual(bands["0.8-1.0"]["n"], 2)
        self.assertEqual(bands["0.6-0.8"]["n"], 1)
        self.assertEqual(bands["0.2-0.4"]["observed"], 0.5)

    def test_a_brier_score_over_the_limit_alarms_only_with_enough_rows(self):
        self.write("plan-of-record.csv", "id\nPL-01\n")
        self.ledger([self.binary(0.9, 0)] * 4)
        r, data, alarms = self.result()
        self.assertNotIn("brier", alarms)                                              # four rows: a note, not an alarm
        self.assertTrue(any("calibration needs at least 5" in n for n in data["not_applicable"]))
        self.ledger([self.binary(0.9, 0)] * 5)
        r, data, alarms = self.result()
        self.assertIn("brier", alarms)
        self.assertEqual(data["checks"]["forecasts"]["brier"], 0.81)
        self.ledger([self.binary(0.6, 1)] * 3 + [self.binary(0.6, 0)] * 2)
        self.assertNotIn("brier", self.result()[2])

    def test_interval_hit_rate_against_eighty_percent(self):
        self.write("plan-of-record.csv", "id\nPL-01\n")
        hit, miss = self.cont(10, 20, 30, 25), self.cont(10, 20, 30, 50)
        self.ledger([hit] * 4 + [miss])                                                # 80 percent
        r, data, alarms = self.result()
        self.assertEqual(data["checks"]["forecasts"]["interval_hit_percent"], 80)
        self.assertNotIn("interval-hit-rate", alarms)
        self.ledger([hit] * 2 + [miss] * 3)                                            # 40 percent: 40 points under
        self.assertIn("interval-hit-rate", self.result()[2])
        self.ledger([hit] * 5)                                                         # 100 percent is 20 over: on the limit, not beyond
        self.assertNotIn("interval-hit-rate", self.result()[2])
        self.assertIn("interval-hit-rate", self.result("--hit-tolerance", "10")[2])

    def test_bias_is_the_mean_signed_error_in_percent_of_the_point(self):
        self.write("plan-of-record.csv", "id\nPL-01\n")
        self.ledger([self.cont(10, 20, 40, 26)] * 5)                                   # +30 percent each
        r, data, alarms = self.result()
        self.assertEqual(data["checks"]["forecasts"]["bias_percent"], 30.0)
        self.assertIn("bias", alarms)
        self.ledger([self.cont(10, 20, 40, 21)] * 5)
        r, data, alarms = self.result()
        self.assertEqual(data["checks"]["forecasts"]["bias_percent"], 5.0)
        self.assertNotIn("bias", alarms)
        self.ledger([self.cont(10, 20, 40, 14)] * 5)                                   # an under-shoot is negative bias
        self.assertEqual(self.result()[1]["checks"]["forecasts"]["bias_percent"], -30.0)

    def test_deterministic_and_retired_rows_and_a_point_outside_its_interval_are_excluded(self):
        self.write("plan-of-record.csv", "id\nPL-01\n")
        rows = [{"kind": "deterministic", "predicted_low": 1, "predicted_point": 2, "predicted_high": 3, "actual_value": 99},
                {"kind": "retired", "p_success": 0.9, "actual_realized": 0},
                self.cont(0, 0, 200, 500),                                             # point equals low
                self.cont(10, 20, 30, 25)]
        self.ledger(rows)
        r, data, _ = self.result()
        f = data["checks"]["forecasts"]
        self.assertEqual((f["continuous_scored"], f["continuous_point_not_inside_interval"], f["binary_scored"]), (1, 1, 0))
        self.assertEqual(f["excluded_deterministic_or_retired"], 2)

    def test_the_error_is_split_by_source_tag(self):
        self.write("plan-of-record.csv", "id\nPL-01\n")
        self.ledger([self.cont(10, 20, 30, 25, "M")] * 3 + [self.cont(10, 20, 30, 90, "G")] * 2
                    + [self.binary(0.9, 1, "M"), self.binary(0.9, 0, "S")])
        split = self.result()[1]["checks"]["forecasts"]["by_tag"]
        self.assertEqual((split["M"]["continuous_n"], split["M"]["hit_percent"]), (3, 100))
        self.assertEqual((split["G"]["continuous_n"], split["G"]["hit_percent"]), (2, 0))
        self.assertEqual(split["S"]["brier"], 0.81)
        self.assertEqual(split["M"]["binary_n"], 1)

    def test_rows_written_after_their_action_started_are_counted(self):
        self.write("plan-of-record.csv", "id\nPL-01\n")
        self.ledger([{**self.cont(10, 20, 30, 25), "created_at_utc": iso(1), "actual_start": iso(2)},
                     {**self.cont(10, 20, 30, 25), "created_at_utc": iso(3), "actual_start": iso(2)}])
        self.assertEqual(self.result()[1]["checks"]["forecasts"]["rows_written_after_their_action_started"], 1)

    def test_a_missing_ledger_alarms_beside_a_plan_and_is_not_applicable_without_one(self):
        self.register([{}])
        r, data, alarms = self.result()
        self.assertNotIn("no-forecast-ledger", alarms)
        self.write("plan-of-record.csv", "id\nPL-01\n")
        self.assertIn("no-forecast-ledger", self.result()[2])


class Session(Repo):
    def relay(self, context=None, window=200000, fail=False):
        script = self.root / "fake_relay.py"
        view = {"running": False, "turns": 7, "last_event_ms": int((NOW - timedelta(minutes=12)).timestamp() * 1000),
                "context": {"projectedTokens": context, "contextWindow": window} if context is not None else {}}
        script.write_text("import json, sys\nopen(%r, 'a').write(' '.join(sys.argv[1:]) + '\\n')\n%s\nprint(json.dumps(%r))\n"
                          % (str(self.root / "relay-calls.txt"), "sys.exit(1)" if fail else "", view))
        return f"{sys.executable} {script}"

    def session(self, **kw):
        env = {"STRATEGIST_HEALTH_RELAY": self.relay(**{k: v for k, v in kw.items() if k in ("context", "window", "fail")})}
        full = dict(os.environ, **env)
        r = subprocess.run([sys.executable, "-B", str(TOOL), "--root", str(self.root), "--now", NOW.isoformat(), "--format", "json",
                            "--session", "session-made-up", *kw.get("extra", [])], capture_output=True, text=True, env=full)
        data = json.loads(r.stdout)
        return r, data, {a["alarm"] for a in data["alarms"]}

    def test_context_at_seventy_five_percent_alarms_and_seventy_four_does_not(self):
        self.healthy_base()
        r, data, alarms = self.session(context=148000)
        self.assertNotIn("session-context", alarms)
        self.assertEqual(data["checks"]["session"]["context_percent"], 74)
        r, data, alarms = self.session(context=150000)
        self.assertIn("session-context", alarms)
        self.assertEqual(r.returncode, 1)

    def test_the_relay_is_asked_to_inspect_that_session_as_json(self):
        self.healthy_base()
        self.session(context=1000)
        calls = (self.root / "relay-calls.txt").read_text()
        self.assertIn("inspect --runtime dsh --session session-made-up --json", calls)

    def test_the_session_id_comes_from_the_strategist_seat_in_team_yaml(self):
        self.healthy_base()
        (self.root / "TEAM.yaml").write_text("seats:\n  - key: scout\n    session_id: session-not-this\n  - key: strategist\n"
                                             "    session_id: session-from-team\n")
        env = dict(os.environ, STRATEGIST_HEALTH_RELAY=self.relay(context=1000))
        subprocess.run([sys.executable, "-B", str(TOOL), "--root", str(self.root), "--now", NOW.isoformat()], capture_output=True, text=True, env=env)
        self.assertIn("--session session-from-team", (self.root / "relay-calls.txt").read_text())

    def test_an_unreachable_relay_or_no_context_figure_is_not_applicable_never_an_alarm(self):
        self.healthy_base()
        r, data, alarms = self.session(fail=True)
        self.assertNotIn("session-context", alarms)
        self.assertTrue(any(n.startswith("session") for n in data["not_applicable"]))
        r, data, alarms = self.session(context=None)
        self.assertNotIn("session-context", alarms)

    def test_no_session_skips_the_relay_entirely(self):
        self.healthy_base()
        env = dict(os.environ, STRATEGIST_HEALTH_RELAY=self.relay(context=199000))
        r = subprocess.run([sys.executable, "-B", str(TOOL), "--root", str(self.root), "--now", NOW.isoformat(), "--no-session"],
                           capture_output=True, text=True, env=env)
        self.assertEqual(r.returncode, 0, r.stdout)
        self.assertFalse((self.root / "relay-calls.txt").exists())


class Cli(Repo):
    def test_a_healthy_repository_exits_zero(self):
        self.healthy_base()
        r = self.run_tool()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("healthy", r.stdout)

    def test_it_writes_nothing_and_leaves_the_index_alone(self):
        self.healthy_base()
        self.write("notes.md", "x", age_hours=5, commit=False)
        def digest():
            return {str(p.relative_to(self.root)): p.read_bytes() for p in sorted(self.root.rglob("*")) if p.is_file() and ".git/objects" not in str(p)}
        before = digest()
        self.run_tool()
        self.run_tool("--format", "json")
        self.assertEqual(digest(), before)                                             # including .git/index, byte for byte

    def test_a_bad_root_or_time_exits_two(self):
        r = subprocess.run([sys.executable, "-B", str(TOOL), "--root", "/nonexistent-root", "--no-session"], capture_output=True, text=True)
        self.assertEqual(r.returncode, 2)
        r = subprocess.run([sys.executable, "-B", str(TOOL), "--root", str(self.root), "--now", "soon", "--no-session"], capture_output=True, text=True)
        self.assertEqual(r.returncode, 2)

    def test_the_real_repository_runs(self):
        real = TOOL.parent.parent.parent
        if not list((real / "_records_").glob("*/strategy")):
            self.skipTest("no strategy folder in this checkout")
        r = subprocess.run([sys.executable, "-B", str(TOOL), "--root", str(real), "--no-session"], capture_output=True, text=True)
        self.assertIn(r.returncode, (0, 1), r.stdout + r.stderr)
        self.assertIn("== STRATEGIST HEALTH", r.stdout)


if __name__ == "__main__":
    unittest.main()
