"""Tests for _tools_/resource_map.py: amounts with a K, M, G or B suffix, commas and bare numbers, and the power breakdown
keys. `snap` runs on a temporary copy of the tool and its definitions, so the real snapshot history is never touched.

Run: python3 -m unittest discover -s _tools_/resource-map-tests
"""
from __future__ import annotations

import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
POWER_KEYS = ("power_total", "power_hero", "power_unit", "power_building", "power_drone", "power_tech")


def load():
    spec = importlib.util.spec_from_file_location("resource_map_under_test", TOOLS / "resource_map.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ParseAmount(unittest.TestCase):
    def setUp(self):
        self.parse = load().parse_amount

    def test_the_cases_the_hud_shows(self):
        self.assertEqual(self.parse("1.1G"), 1_100_000_000)          # crashed with ValueError before
        self.assertEqual(self.parse("1.0G"), 1_000_000_000)
        self.assertEqual(self.parse("638.0M"), 638_000_000)
        self.assertEqual(self.parse("276.9M"), 276_900_000)
        self.assertEqual(self.parse("565.1K"), 565_100)
        self.assertEqual(self.parse("81"), 81)
        self.assertEqual(self.parse("0"), 0)

    def test_commas_and_a_bare_number(self):
        self.assertEqual(self.parse("1,234,567"), 1_234_567)
        self.assertEqual(self.parse("96,560"), 96_560)
        self.assertEqual(self.parse("1,234.5K"), 1_234_500)
        self.assertEqual(self.parse("149689618"), 149_689_618)

    def test_b_for_billion_and_any_case_and_spaces(self):
        self.assertEqual(self.parse("1.2B"), 1_200_000_000)
        self.assertEqual(self.parse("2.5b"), 2_500_000_000)
        self.assertEqual(self.parse(" 1.1g "), 1_100_000_000)
        self.assertEqual(self.parse("3m"), 3_000_000)
        self.assertEqual(self.parse("7k"), 7_000)

    def test_a_one_decimal_value_that_float_would_land_one_short_is_exact(self):
        self.assertEqual(int(float("32.3") * 1_000), 32_299)          # what int(float(text) * mult) gave: one short
        self.assertEqual(self.parse("32.3K"), 32_300)
        self.assertEqual(int(float("64.1") * 1_000), 64_099)
        self.assertEqual(self.parse("64.1K"), 64_100)
        self.assertEqual(self.parse("4.35M"), 4_350_000)
        self.assertEqual(self.parse("0.29K"), 290)

    def test_every_one_decimal_value_is_exact_for_all_four_suffixes(self):
        for suffix, mult in (("K", 10**3), ("M", 10**6), ("G", 10**9), ("B", 10**9)):
            for n in range(1, 10000):
                text = f"{n / 10:.1f}"
                self.assertEqual(self.parse(text + suffix), n * mult // 10, text + suffix)

    def test_it_still_truncates_a_fraction_toward_zero(self):
        self.assertEqual(self.parse("1.23456K"), 1234)
        self.assertEqual(self.parse("0.9"), 0)

    def test_text_that_is_not_an_amount_is_a_value_error_with_a_clear_message(self):
        for bad in ("", "  ", "abc", "1.1T", "G", "1.2.3M", "--5"):
            with self.assertRaises(ValueError, msg=bad) as caught:
                self.parse(bad)
            self.assertIn("cannot read the amount", str(caught.exception))


class Snap(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="resource-map-"))
        self.addCleanup(shutil.rmtree, self.tmp, True)
        shutil.copy(TOOLS / "resource_map.py", self.tmp / "resource_map.py")
        shutil.copy(TOOLS / "resources.json", self.tmp / "resources.json")
        self.history = self.tmp / "state" / "resources.jsonl"

    def run_tool(self, *args):
        return subprocess.run([sys.executable, "-B", str(self.tmp / "resource_map.py"), *args], capture_output=True, text=True)

    def test_snap_with_a_g_suffix_no_longer_crashes_and_stores_the_integer(self):
        r = self.run_tool("snap", "power_total=1.1G", "food=638.0M", "coin=1,234,567", "stamina=81")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertNotIn("Traceback", r.stderr)
        row = json.loads(self.history.read_text().strip().split("\n")[-1])
        self.assertEqual(row["values"], {"power_total": 1_100_000_000, "food": 638_000_000, "coin": 1_234_567, "stamina": 81})

    def test_the_power_breakdown_keys_are_defined_so_snap_stops_flagging_them(self):
        r = self.run_tool("snap", *[f"{k}=1.{i}G" for i, k in enumerate(POWER_KEYS)])
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertNotIn("unknown resource", r.stdout)
        self.assertNotIn("FLAG", r.stdout)                              # no floors on growth metrics
        shown = self.run_tool("show")
        for key in POWER_KEYS:
            self.assertRegex(shown.stdout, rf"{key}\s+[\d,]+\s+Power breakdown")

    def test_an_unlisted_key_is_still_flagged_unknown(self):
        r = self.run_tool("snap", "made_up_thing=5")
        self.assertIn("unknown resource", r.stdout)

    def test_a_bad_amount_is_an_error_message_with_exit_2_and_writes_nothing(self):
        r = self.run_tool("snap", "food=1.1T")
        self.assertEqual(r.returncode, 2)
        self.assertIn("error: food: cannot read the amount '1.1T'", r.stderr)
        self.assertNotIn("Traceback", r.stderr)
        self.assertFalse(self.history.exists())

    def test_history_rows_are_appended_never_rewritten(self):
        self.run_tool("snap", "food=1M")
        first = self.history.read_text()
        self.run_tool("snap", "food=2G")
        both = self.history.read_text()
        self.assertTrue(both.startswith(first))
        self.assertEqual(len(both.strip().split("\n")), 2)


class Definitions(unittest.TestCase):
    def test_resources_json_has_the_six_power_keys_and_keeps_the_old_ones(self):
        defs = json.loads((TOOLS / "resources.json").read_text())["resources"]
        for key in POWER_KEYS:
            self.assertIn(key, defs)
            self.assertIsNone(defs[key]["crit_below"])
            self.assertIsNone(defs[key]["warn_below"])
            self.assertTrue(defs[key]["label"].startswith("Power breakdown"))
        for key in ("coin", "food", "iron", "total_power", "stamina", "honor"):
            self.assertIn(key, defs)

    def test_the_recorded_history_rows_still_parse_with_the_tool(self):
        tool = load()
        history = TOOLS / "state" / "resources.jsonl"
        rows = [json.loads(line) for line in history.read_text().split("\n") if line.strip()]
        self.assertTrue(rows)
        for row in rows:
            for value in row["values"].values():
                self.assertIsInstance(value, int)


if __name__ == "__main__":
    unittest.main()
