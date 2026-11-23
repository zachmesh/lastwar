"""Tests for the forecast-ledger check (the owner wants the strategy observed): `validate` warns for a live inbox unit whose serves names a
plan item the newest forecast ledger has no row for, or is neither a ledger plan item nor an exempt word, and for a missing or unreadable
ledger; counts and unit names only. `enqueue --require-forecast` refuses the same units; off by default.

Run: python3 -m unittest discover -s _tools_/queue-tests
"""
from __future__ import annotations

import re
import subprocess

from test_serves import PoolCase

LEDGER_HEADER = "forecast_id,plan_item,lever,metric,note\n"
SECRET_NOTE = "ledger note that must never be printed"


class ForecastCase(PoolCase):
    def setUp(self):
        super().setUp()
        self.n = 0
        self.ledger("2026-11-22", ["PL-01", "PL-02", "PL-06"])

    def ledger(self, day, items, header=LEDGER_HEADER):
        path = self.repo / "_records_" / day / "strategy" / "forecast-ledger.csv"
        path.parent.mkdir(parents=True, exist_ok=True)
        rows = "".join(f"F-{i},{item},lever text,metric text,{SECRET_NOTE}\n" for i, item in enumerate(items))
        path.write_text(header + rows)

    def unit(self, serves):
        self.n += 1
        return self.enqueue("--serves", serves, regular=f"regular-{self.n}", activity=f"activity-{self.n}")

    def validate(self, *extra):
        r = self.queue("validate", *extra)
        self.assertIn(r.returncode, (0, 1), r.stdout + r.stderr)
        return r

    def warnings(self, r):
        return [line for line in r.stdout.splitlines() if line.startswith("warning: forecast")]

    def no_leak(self, r, *texts):
        for text in (SECRET_NOTE, "lever text", "metric text", *texts):
            self.assertNotIn(text, r.stdout + r.stderr)


class Validate(ForecastCase):
    def test_ledger_plan_items_and_exempt_words_pass_silently(self):
        for serves in ("PL-01", "PL-06", "upkeep", "Snapshot", "baseline", "fill idle slot with the research queue", "fill-idle-slot", "PL-01, upkeep"):
            self.unit(serves)
        r = self.validate()
        self.assertEqual((r.returncode, self.warnings(r)), (0, []), r.stdout)
        self.assertIn("pool valid", r.stdout)

    def test_a_plan_item_id_with_no_ledger_row_warns_with_a_count_and_the_unit_name(self):
        bad = self.unit("PL-99")
        self.unit("PL-01")
        r = self.validate()
        self.assertEqual(r.returncode, 0, r.stdout)
        lines = self.warnings(r)
        self.assertEqual(len(lines), 1)
        self.assertIn("1 live inbox unit(s) serve a plan item id that has no row in the forecast ledger", lines[0])
        self.assertIn(f"inbox/{bad}.md", lines[0])
        self.assertIn("(1 warning(s))", r.stdout)
        self.no_leak(r)

    def test_something_that_is_neither_a_plan_item_nor_an_exempt_word_warns_without_printing_its_text(self):
        self.unit("grow the account somehow")
        self.unit("PL-1000")                                                          # not an id shape either: unknown
        r = self.validate()
        lines = self.warnings(r)
        self.assertEqual(len(lines), 1)
        self.assertIn("2 live inbox unit(s) serve something that is neither a ledger plan item nor an exempt word", lines[0])
        self.assertNotIn("grow the account somehow", r.stdout)
        self.no_leak(r)

    def test_a_comma_list_is_judged_by_its_worst_part(self):
        self.unit("PL-01, PL-99")
        self.unit("PL-02, a vague thing")
        lines = self.warnings(self.validate())
        self.assertEqual(len(lines), 2)
        self.assertTrue(any("plan item id that has no row" in l for l in lines))
        self.assertTrue(any("neither a ledger plan item" in l for l in lines))

    def test_the_newest_ledger_by_date_is_the_one_read(self):
        self.ledger("2026-11-20", ["PL-77"])
        self.unit("PL-77")
        self.assertEqual(len(self.warnings(self.validate())), 1)                      # the 22nd's ledger has no PL-77
        self.ledger("2026-11-23", ["PL-77"])
        self.assertEqual(self.warnings(self.validate()), [])                          # now the newest has it

    def test_a_missing_ledger_warns_only_when_a_unit_needs_it(self):
        (self.repo / "_records_" / "2026-11-22" / "strategy" / "forecast-ledger.csv").unlink()
        self.unit("upkeep")
        self.assertEqual(self.warnings(self.validate()), [])
        bad = self.unit("PL-01")
        r = self.validate()
        lines = self.warnings(r)
        self.assertEqual(len(lines), 1)
        self.assertIn("no forecast ledger found (1 live inbox unit(s) serve something that needs it and could not be checked)", lines[0])
        self.assertIn(f"inbox/{bad}.md", lines[0])
        self.assertEqual(r.returncode, 0)

    def test_an_unusable_ledger_is_a_warning_with_its_reason(self):
        self.ledger("2026-11-23", ["PL-01"], header="forecast_id,item,lever\n")
        self.unit("PL-01")
        lines = self.warnings(self.validate())
        self.assertEqual(len(lines), 1)
        self.assertIn("it has no plan_item column", lines[0])

    def test_claimed_and_done_units_are_not_checked_and_a_real_problem_still_fails(self):
        unit = self.unit("PL-99")
        self.assertEqual(self.queue("claim", "--unit", unit, "--executor", "tester").returncode, 0)
        self.assertEqual(self.warnings(self.validate()), [])
        self.unit("PL-98")
        path = next((self.pool / "inbox").glob("*.md"))
        path.write_text(path.read_text() + "\n<<<<<<< HEAD\n")
        r = self.validate()
        self.assertEqual(r.returncode, 1)
        self.assertEqual(len(self.warnings(r)), 1)

    def test_validate_ref_reads_the_ledger_at_the_ref(self):
        self.unit("PL-99")
        self.unit("PL-01")
        subprocess.run(["git", "-C", str(self.repo), "add", "-A"], check=True)
        subprocess.run(["git", "-C", str(self.repo), "commit", "-q", "-m", "pool"], check=True)
        r = self.validate("--ref", "HEAD")
        self.assertEqual(r.returncode, 0, r.stdout)
        self.assertEqual(len(self.warnings(r)), 1)
        self.assertIn("plan item id that has no row", self.warnings(r)[0])
        self.no_leak(r)
        subprocess.run(["git", "-C", str(self.repo), "rm", "-q", "_records_/2026-11-22/strategy/forecast-ledger.csv"], check=True)
        subprocess.run(["git", "-C", str(self.repo), "commit", "-q", "-m", "no ledger"], check=True)
        gone = self.validate("--ref", "HEAD")
        self.assertIn("no forecast ledger at the ref", "".join(self.warnings(gone)))


class Enqueue(ForecastCase):
    def refused(self, serves, **kw):
        self.n += 1
        r = self.queue("enqueue", "--regular", f"regular-{self.n}", "--activity", f"activity-{self.n}", "--est-minutes", "5",
                       "--serves", serves, "--require-forecast")
        return r

    def test_off_by_default_so_nothing_changes_for_the_planner(self):
        r = self.queue("enqueue", "--regular", "regular-9", "--activity", "activity-9", "--est-minutes", "5", "--serves", "PL-99")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_a_ledger_plan_item_and_the_exempt_words_are_queued(self):
        for serves in ("PL-01", "upkeep", "baseline", "snapshot", "fill idle slot with the research queue"):
            r = self.refused(serves)
            self.assertEqual(r.returncode, 0, f"{serves}: {r.stdout}{r.stderr}")

    def test_a_plan_item_without_a_row_and_an_unknown_serves_are_refused_and_nothing_is_queued(self):
        r = self.refused("PL-99")
        self.assertEqual(r.returncode, 1)
        self.assertIn("--require-forecast: its serves line names a plan item id that has no row in the forecast ledger", r.stdout)
        r = self.refused("grow the account somehow")
        self.assertEqual(r.returncode, 1)
        self.assertIn("neither a ledger plan item nor an exempt word", r.stdout)
        self.assertEqual(list((self.pool / "inbox").glob("*.md")), [])
        self.no_leak(r)

    def test_a_missing_ledger_refuses_a_plan_item_but_not_an_exempt_word(self):
        (self.repo / "_records_" / "2026-11-22" / "strategy" / "forecast-ledger.csv").unlink()
        r = self.refused("PL-01")
        self.assertEqual(r.returncode, 1)
        self.assertIn("no forecast ledger found, so its serves line cannot be checked", r.stdout)
        self.assertEqual(self.refused("upkeep").returncode, 0)

    def test_the_flag_is_in_the_help(self):
        out = self.queue("enqueue", "--help")
        self.assertIn("--require-forecast", out.stdout)
        self.assertIn("Strategist", re.sub(r"\s+", " ", out.stdout))
