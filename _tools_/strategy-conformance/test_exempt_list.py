"""Tests for the serves exempt list (Steer A, 2026-11-25): the parser and validation (every roster regular is on the list, no listed id is outside the roster,
valid classes, dates and ledger rows), the dated baseline (a changed line needs a new decided_utc, nothing is re-based without --accept-exempt-list) and
DEFINITION B of the coverage figure beside definition A. Every pool and list here is made up in a temporary folder; one test holds the real list to the
real roster and ledger.

Run: python3 -m unittest discover -s _tools_/strategy-conformance
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import re
from pathlib import Path

from test_conformance import NOW, SECRET, PoolCase, TOOL, iso

HERE = Path(__file__).resolve().parent
HEADER = "regular_id,class,serves,reason,decided_utc,review_utc\n"
DAY = "2026-11-22"
DECIDED = "2026-11-23T08:00Z"
REVIEW = "2026-12-30T00:00Z"


def load_module():
    spec = importlib.util.spec_from_file_location("exempt_list_under_test", str(HERE / "exempt_list.py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ExemptCase(PoolCase):
    ROSTER = {"harvest": "PL-01", "mail": "PL-19", "scout": "upkeep"}

    def setUp(self):
        super().setUp()
        self.ledger("PL-01", "PL-02", "PL-17", "PL-19")
        self.write_roster(self.ROSTER)
        self.write_list([("harvest", "plan", "PL-01", DECIDED), ("mail", "income", "PL-19", DECIDED), ("scout", "exempt", "upkeep-read", DECIDED)])

    def write_roster(self, serves: dict):
        (self.root / "_tools_").mkdir(exist_ok=True)
        (self.root / "_tools_" / "regulars.json").write_text(json.dumps({"regulars": [{"id": k, "serves": v} for k, v in serves.items()]}))

    def list_path(self) -> Path:
        folder = self.root / "_records_" / DAY / "strategy"
        folder.mkdir(parents=True, exist_ok=True)
        return folder / "serves-exempt-list.csv"

    def write_list(self, lines, header=HEADER, reason="looks only", review=REVIEW):
        body = header + "".join(f'{i},{c},{s},"{reason}",{d},{review}\n' for i, c, s, d in lines)
        self.list_path().write_text(body)

    def data(self, *args):
        r = self.run_tool("--format", "json", "--since", iso(600), *args)
        self.assertIn(r.returncode, (0, 1), r.stdout + r.stderr)
        return r, json.loads(r.stdout)

    def exempt_alarm(self, d):
        return next((a for a in d["alarms"] if a["alarm"] == "exempt-list"), None)


class Validation(ExemptCase):
    def test_a_complete_list_is_valid_and_prints_its_line_with_no_alarm(self):
        r, d = self.data()
        el = d["counts"]["exempt_list"]
        self.assertEqual((el["regulars"], el["classes"], el["roster"], el["unlabeled"], el["stale"], el["errors"]), (3, {"plan": 1, "income": 1, "exempt": 1}, 3, [], [], []))
        self.assertIsNone(self.exempt_alarm(d))
        out = self.run_tool("--since", iso(600)).stdout
        self.assertIn("exempt list _records_/2026-11-22/strategy/serves-exempt-list.csv (newest decision 2026-11-23T08:00Z): 3 regulars - plan 1, income 1, exempt 1", out)
        self.assertIn("roster 3: unlabeled 0, stale 0", out)

    def test_a_roster_regular_that_is_not_on_the_list_is_an_error_naming_it(self):
        self.write_roster({**self.ROSTER, "newbie": "upkeep"})
        r, d = self.data()
        alarm = self.exempt_alarm(d)
        self.assertEqual(r.returncode, 1)
        self.assertIn("newbie: in the roster and not on the list (unlabeled)", alarm["first"])
        self.assertEqual(d["counts"]["exempt_list"]["unlabeled"], ["newbie"])

    def test_a_listed_id_outside_the_roster_is_an_error(self):
        self.write_list([("harvest", "plan", "PL-01", DECIDED), ("mail", "income", "PL-19", DECIDED), ("scout", "exempt", "upkeep-read", DECIDED),
                         ("ghost", "plan", "PL-02", DECIDED)])
        _r, d = self.data()
        self.assertIn("ghost: on the list and not in the roster", self.exempt_alarm(d)["first"])

    def test_bad_lines_each_name_their_regular_and_never_a_reason_text(self):
        self.write_list([("harvest", "plan", "PL-01", DECIDED), ("harvest", "plan", "PL-01", DECIDED),        # a duplicate
                         ("mail", "daily", "PL-19", DECIDED),                                                    # a class that does not exist
                         ("scout", "exempt", "upkeep-read", "yesterday")], reason=SECRET)                       # a date that is not a date
        r, d = self.data()
        errors = d["counts"]["exempt_list"]["errors"]
        self.assertIn("harvest: listed twice", errors)
        self.assertTrue(any(e.startswith("mail: class daily is not one of") for e in errors))
        self.assertIn("scout: decided_utc is not YYYY-MM-DDTHH:MMZ", errors)
        self.assertNotIn(SECRET, r.stdout + r.stderr)

    def test_an_empty_reason_or_serves_and_a_missing_header_column_are_errors(self):
        path = self.list_path()
        path.write_text(HEADER + f'harvest,plan,,"",{DECIDED},{REVIEW}\nmail,income,PL-19,x,{DECIDED},{REVIEW}\nscout,exempt,upkeep-read,x,{DECIDED},{REVIEW}\n')
        _r, d = self.data()
        errors = d["counts"]["exempt_list"]["errors"]
        self.assertIn("harvest: serves is empty", errors)
        self.assertIn("harvest: reason is empty", errors)
        path.write_text("regular_id,class,serves\nharvest,plan,PL-01\n")
        _r, d = self.data()
        self.assertTrue(any(e.startswith("header lacks column(s):") for e in d["counts"]["exempt_list"]["errors"]))

    def test_plan_and_income_serves_must_be_plan_item_ids_with_a_ledger_row(self):
        self.write_list([("harvest", "plan", "PL-99", DECIDED), ("mail", "income", "PL-19 the claims chain", DECIDED), ("scout", "exempt", "upkeep-read", DECIDED)])
        _r, d = self.data()
        errors = d["counts"]["exempt_list"]["errors"]
        self.assertIn("harvest: PL-99 has no row in the forecast ledger", errors)
        self.assertIn("mail: a income line's serves must be plan item ids (PL-n) only", errors)

    def test_an_exempt_line_must_not_name_a_plan_item(self):
        self.write_list([("harvest", "plan", "PL-01", DECIDED), ("mail", "income", "PL-19", DECIDED), ("scout", "exempt", "PL-01", DECIDED)])
        _r, d = self.data()
        self.assertIn("scout: an exempt line must not name a plan item", d["counts"]["exempt_list"]["errors"])

    def test_a_passed_review_date_and_a_roster_that_differs_are_notes_not_alarms(self):
        self.write_list([("harvest", "plan", "PL-01", DECIDED), ("mail", "income", "PL-19", DECIDED), ("scout", "exempt", "upkeep-read", DECIDED)], review="2026-11-01T00:00Z")
        self.write_roster({"harvest": "PL-02", "mail": "upkeep", "scout": "upkeep"})                          # units carry the roster's serves: differs from the list
        r, d = self.data()
        self.assertIsNone(self.exempt_alarm(d))
        warnings = d["counts"]["exempt_list"]["warnings"]
        self.assertIn("harvest: review date has passed", warnings)
        self.assertTrue(any(w.startswith("roster serves differs from the list for 2 regular(s): harvest, mail") for w in warnings))
        self.assertIn("note: roster serves differs from the list", self.run_tool("--since", iso(600)).stdout)

    def test_no_list_is_not_applicable_and_not_an_alarm(self):
        self.list_path().unlink()
        r, d = self.data()
        self.assertIn("exempt-list", d["not_applicable"])
        self.assertIsNone(self.exempt_alarm(d))
        self.assertIsNone(d["counts"]["exempt_list"])
        self.assertIn("exempt list: none found", self.run_tool().stdout)

    def test_the_flag_names_another_list(self):
        other = self.root / "other.csv"
        other.write_text(HEADER + f"harvest,plan,PL-01,x,{DECIDED},{REVIEW}\n")
        _r, d = self.data("--exempt-list", str(other))
        self.assertEqual(d["counts"]["exempt_list"]["regulars"], 1)
        self.assertIn("mail: in the roster and not on the list (unlabeled)", self.exempt_alarm(d)["first"])

    def test_the_real_list_holds_for_the_real_roster_and_ledger(self):
        """A regression guard: a regular added to the roster must be labeled in the Strategist's list before it lands (and the reverse)."""
        ex = load_module()
        root = HERE.parent.parent
        path = ex.find(root)
        if path is None:
            self.skipTest("no serves-exempt-list.csv in this checkout")
        rows, parse_errors, _sha = ex.parse(path)
        roster_serves, error = ex.roster(root)
        self.assertEqual(error, "")
        spec = importlib.util.spec_from_file_location("queue_for_exempt_test", str(root / "_tools_" / "queue.py"))
        queue = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(queue)
        ids, reason = queue.load_forecast_ledger(str(root / "_queue_"))
        self.assertIsNotNone(ids, reason)
        found = ex.validate(rows, parse_errors, roster_serves, ids, NOW)
        self.assertEqual(found["errors"], [])


class Baseline(ExemptCase):
    def accept(self):
        r = self.run_tool("--format", "json", "--since", iso(600), "--accept-exempt-list")
        self.assertIn(r.returncode, (0, 1), r.stdout + r.stderr)
        return r, json.loads(r.stdout)

    def baseline_file(self) -> Path:
        return self.root / "_tools_" / "state" / "serves-exempt-baseline.json"

    def test_without_the_flag_the_tool_writes_nothing_and_says_no_baseline_is_accepted(self):
        before = sorted(str(p.relative_to(self.root)) for p in self.root.rglob("*"))
        r = self.run_tool("--since", iso(600))
        self.assertIn("baseline: none accepted yet (--accept-exempt-list records it)", r.stdout)
        self.assertEqual(sorted(str(p.relative_to(self.root)) for p in self.root.rglob("*")), before)
        self.assertFalse(self.baseline_file().exists())

    def test_accepting_records_the_list_and_the_next_run_says_unchanged(self):
        _r, d = self.accept()
        self.assertTrue(d["counts"]["exempt_list"]["accepted"].endswith("serves-exempt-baseline.json"))
        saved = json.loads(self.baseline_file().read_text())
        self.assertEqual(sorted(saved["lines"]), ["harvest", "mail", "scout"])
        self.assertEqual(saved["sha256"], hashlib.sha256(self.list_path().read_bytes()).hexdigest())
        self.assertNotIn("looks only", self.baseline_file().read_text())                                      # reason hashes, never reason texts
        _r, d = self.data()
        self.assertEqual(d["counts"]["exempt_list"]["baseline"]["state"], "unchanged")
        self.assertIn("baseline: accepted", self.run_tool("--since", iso(600)).stdout)

    def test_a_changed_line_without_a_newer_decided_utc_is_an_error_with_one_that_is_dated_it_is_only_reported(self):
        self.accept()
        self.write_list([("harvest", "income", "PL-19", DECIDED), ("mail", "income", "PL-19", DECIDED), ("scout", "exempt", "upkeep-read", DECIDED)])   # class changed, same date
        r, d = self.data()
        self.assertEqual(r.returncode, 1)
        self.assertIn("harvest: changed since the accepted baseline without a newer decided_utc", self.exempt_alarm(d)["first"])
        self.write_list([("harvest", "income", "PL-19", "2026-11-24T10:00Z"), ("mail", "income", "PL-19", DECIDED), ("scout", "exempt", "upkeep-read", DECIDED)])
        r, d = self.data()
        self.assertIsNone(self.exempt_alarm(d))
        base = d["counts"]["exempt_list"]["baseline"]
        self.assertEqual((base["state"], base["edited"], base["added"], base["removed"]), ("changed", ["harvest"], [], []))
        self.assertIn("(+0 -0 ~1)", self.run_tool("--since", iso(600)).stdout)

    def test_the_baseline_is_not_re_based_by_running_the_tool_only_by_the_flag(self):
        self.accept()
        self.write_list([("harvest", "income", "PL-19", "2026-11-24T10:00Z"), ("mail", "income", "PL-19", DECIDED), ("scout", "exempt", "upkeep-read", DECIDED)])
        before = self.baseline_file().read_text()
        for _ in range(2):
            self.data()
        self.assertEqual(self.baseline_file().read_text(), before)
        self.accept()
        _r, d = self.data()
        self.assertEqual(d["counts"]["exempt_list"]["baseline"]["state"], "unchanged")

    def test_added_and_removed_lines_are_listed(self):
        self.accept()
        self.write_roster({**self.ROSTER, "newbie": "upkeep"})
        self.write_list([("harvest", "plan", "PL-01", DECIDED), ("scout", "exempt", "upkeep-read", DECIDED), ("newbie", "exempt", "upkeep-read", "2026-11-24T10:00Z")])
        _r, d = self.data()
        base = d["counts"]["exempt_list"]["baseline"]
        self.assertEqual((base["added"], base["removed"]), (["newbie"], ["mail"]))

    def test_a_line_added_with_a_date_before_the_baseline_is_a_note(self):
        self.write_roster({**self.ROSTER, "newbie": "upkeep"})
        self.accept_with(lines=[("harvest", "plan", "PL-01", DECIDED), ("mail", "income", "PL-19", DECIDED), ("scout", "exempt", "upkeep-read", DECIDED),
                                ("newbie", "exempt", "upkeep-read", DECIDED)])
        self.write_roster({**self.ROSTER, "newbie": "upkeep", "later": "upkeep"})
        self.write_list([("harvest", "plan", "PL-01", DECIDED), ("mail", "income", "PL-19", DECIDED), ("scout", "exempt", "upkeep-read", DECIDED),
                         ("newbie", "exempt", "upkeep-read", DECIDED), ("later", "exempt", "upkeep-read", "2020-01-01T00:00Z")])
        _r, d = self.data()
        self.assertIn("later: added with a decided_utc before the baseline was accepted", d["counts"]["exempt_list"]["warnings"])

    def accept_with(self, lines):
        self.write_list(lines)
        self.accept()

    def test_accepting_is_refused_while_the_list_has_errors(self):
        self.write_roster({**self.ROSTER, "newbie": "upkeep"})                                                # unlabeled
        r, d = self.accept()
        self.assertEqual(r.returncode, 1)
        self.assertEqual(d["counts"]["exempt_list"]["accepted"], "refused: the list has errors")
        self.assertFalse(self.baseline_file().exists())

    def test_an_unreadable_baseline_is_an_error(self):
        self.baseline_file().parent.mkdir(parents=True, exist_ok=True)
        self.baseline_file().write_text("{broken")
        _r, d = self.data()
        self.assertTrue(any("could not be read" in e for e in self.exempt_alarm(d)["first"]))


class DefinitionB(ExemptCase):
    def pool(self):
        self.unit("done", ago=10, serves="PL-01", regular="harvest", hours=1.0)       # plan, served
        self.unit("done", ago=20, serves="upkeep", regular="mail", hours=1.0)         # income by the list although the unit says upkeep
        self.unit("done", ago=30, serves="upkeep", regular="scout", hours=1.0)        # exempt: leaves the denominator
        self.unit("done", ago=40, serves="upkeep", regular="stranger", hours=1.0)     # off the list: counts as unserved

    def test_the_share_is_by_the_regular_class_with_exempt_hours_out_of_the_denominator(self):
        self.pool()
        _r, d = self.data()
        b = d["counts"]["coverage_b"]["rolling"]
        self.assertEqual((b["served_hours"], b["exempt_hours"], b["denominator_hours"], b["total_hours"]), (2.0, 1.0, 3.0, 4.0))
        self.assertEqual(b["percent"], 66.7)
        self.assertEqual((b["unlisted_units"], b["unlisted_hours"]), (1, 1.0))
        self.assertEqual(b["hours_by_class"], {"plan": 1.0, "income": 1.0, "exempt": 1.0})
        self.assertEqual(d["counts"]["coverage_b"]["since_cutover"]["percent"], 66.7)

    def test_definition_a_stays_by_the_units_own_serves_and_both_print_side_by_side(self):
        self.pool()
        r, d = self.data()
        self.assertEqual(d["counts"]["rolling"]["unit_hours_percent"], 25.0)                       # A: one unit of four serves a ranked item
        out = self.run_tool("--since", iso(600)).stdout
        self.assertIn("coverage ROLLING 12 h", out)
        self.assertRegex(out, r"coverage DEFINITION B \(regular class from the list; exempt hours leave the denominator\), beside definition A above: ROLLING 66\.7% of 3 h")
        self.assertIn("hours by class, rolling: plan 1 h, income 1 h, exempt 1 h, off the list 1 h", out)
        self.assertEqual(r.returncode, 1)                                                           # A's alarm is untouched (25 percent of the hours)

    def test_b_never_decides_the_alarm(self):
        for i in range(6):
            self.unit("done", ago=10 + i, serves="PL-01", regular="harvest", hours=1.0)
        self.unit("done", ago=20, serves="upkeep", regular="stranger", hours=0.1)
        _r, d = self.data()
        self.assertEqual(d["counts"]["coverage_b"]["rolling"]["percent"], 98.4)
        self.assertNotIn("coverage", {a["alarm"] for a in d["alarms"]})                              # A is high too here
        self.assertEqual(d["counts"]["coverage_verdict_metric"], "unit-hours")

    def test_the_output_never_prints_a_reason_text(self):
        self.write_list([("harvest", "plan", "PL-01", DECIDED), ("mail", "income", "PL-19", DECIDED), ("scout", "exempt", "upkeep-read", DECIDED)], reason=SECRET)
        self.pool()
        r, d = self.data()
        self.assertNotIn(SECRET, r.stdout + r.stderr)
        self.assertNotIn(SECRET, self.run_tool().stdout)
