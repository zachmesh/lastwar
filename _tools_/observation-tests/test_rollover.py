"""Tests for the day observation file rollover of observation.py: a day file that would pass 400 body words rolls into
observation-pN.md (never past 450), the earlier files stay byte-identical, the new part carries the cumulative counters,
and the folder index lists it. Every file is made up in a temporary folder.

Run: python3 -m unittest discover -s _tools_/observation-tests
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

TOOL = Path(__file__).resolve().parent.parent / "observation.py"
WORD_BUDGET = Path.home() / "dtadpole/reflection/_tools_/document-word-budget/word-budget.py"


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


OBS = load(TOOL, "observation_under_test")
FRONT = ("---\ntitle: Perception scout observations 2026-11-23\ncreated: 2026-11-23T00:00:00Z\nmodified: 2026-11-23T01:00:00Z\n"
         "version: 1.3.0\ndescription: The day observation file\nitems_observed: {items}\nred_dots_seen: {seen}\n"
         "red_dots_explained: {explained}\nunexplained_red_dots: {unexplained}\n---\n")


def section(heading: str, words: int) -> str:
    return f"## Pass {heading}\n\n" + " ".join(f"w{i}" for i in range(words)) + "\n"


class RolloverCase(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="observation-test-"))
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.day = self.tmp / "2026-11-23" / "perception-scout"
        self.day.mkdir(parents=True)
        self.base = self.day / "observation.md"

    def write_base(self, section_words, items=10, seen=6, explained=4, unexplained=2):
        text = FRONT.format(items=items, seen=seen, explained=explained, unexplained=unexplained)
        text += "\n# Observations\n\nThe day file.\n"
        for i, words in enumerate(section_words, 1):
            text += "\n" + section(f"{i} at 0{i}00", words)
        self.base.write_text(text)

    def sha(self, path):
        return hashlib.sha256(Path(path).read_bytes()).hexdigest()

    def append(self, heading, words, items=2, seen=1, explained=1, unexplained=0, target=None, reference=None):
        sec = self.tmp / f"section-{heading.replace(' ', '-')}.md"
        sec.write_text(section(heading, words))
        args = [sys.executable, "-B", str(TOOL), "append", "--file", str(target or self.base), "--section", str(sec),
                "--add-items", str(items), "--add-seen", str(seen), "--add-explained", str(explained),
                "--add-unexplained", str(unexplained), "--format", "json"]
        if reference:
            args += ["--reference", str(reference)]
        r = subprocess.run(args, capture_output=True, text=True)
        return r, (json.loads(r.stdout) if r.stdout.strip().startswith("{") else {})

    def words(self, path):
        return OBS._file_words(Path(path).read_text())

    def parts(self):
        return sorted(p.name for p in self.day.glob("observation*.md"))


class Appending(RolloverCase):
    def test_a_section_that_fits_still_appends_to_the_day_file(self):
        self.write_base([100])
        r, out = self.append("2 at 0200", 100)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertFalse(out["result"]["rolled_over"])
        self.assertEqual(self.parts(), ["observation.md"])
        self.assertLessEqual(self.words(self.base), 400)

    def test_a_section_that_would_pass_400_words_goes_to_a_new_part_and_the_old_file_is_untouched(self):
        self.write_base([150, 150])
        before = self.sha(self.base)
        r, out = self.append("3 at 0300", 120)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertTrue(out["result"]["rolled_over"])
        self.assertEqual(self.parts(), ["observation-p2.md", "observation.md"])
        self.assertEqual(self.sha(self.base), before)                                  # records are immutable
        part = self.day / "observation-p2.md"
        self.assertTrue(re.match(r"^observation-p\d+\.md$", part.name))
        self.assertLessEqual(self.words(part), 450)
        text = part.read_text()
        self.assertIn("title: Perception scout observations 2026-11-23 part 2", text)
        self.assertIn("version: 0.1.0", text)
        self.assertIn("## Pass 3 at 0300", text)
        self.assertNotIn("## Pass 1 at 0100", text)

    def test_the_new_part_carries_the_cumulative_counters(self):
        self.write_base([300], items=10, seen=6, explained=4, unexplained=2)
        r, out = self.append("2 at 0200", 120, items=3, seen=2, explained=1, unexplained=1)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        counters = OBS._parse_file(str(self.day / "observation-p2.md"))[0]
        self.assertEqual(counters, {"items_observed": 13, "red_dots_seen": 8, "red_dots_explained": 5, "unexplained_red_dots": 3})
        self.assertEqual(OBS._parse_file(str(self.base))[0]["items_observed"], 10)      # the old file keeps its own

    def test_a_day_file_already_over_the_limit_sends_the_next_section_to_a_part(self):
        self.write_base([700])                                                           # like the 760-word file that blocked commits
        r, out = self.append("2 at 0200", 100)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertTrue(out["result"]["rolled_over"])
        self.assertEqual(self.parts(), ["observation-p2.md", "observation.md"])

    def test_parts_fill_to_400_then_roll_and_no_file_passes_450(self):
        self.write_base([300])
        for i in range(2, 9):
            r, out = self.append(f"{i} at 0{i}00", 120, target=self.base)
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        names = self.parts()
        self.assertGreater(len(names), 3)
        for name in names:
            self.assertLessEqual(self.words(self.day / name), 450, name)
        last = max(self.day.glob("observation-p*.md"), key=lambda p: int(re.search(r"p(\d+)", p.name).group(1)))
        self.assertEqual(OBS._parse_file(str(last))[0]["items_observed"], 10 + 2 * 7)       # cumulative across every part

    def test_naming_the_latest_part_as_the_file_appends_to_the_day_not_beside_it(self):
        self.write_base([700])
        self.append("2 at 0200", 100)
        r, out = self.append("3 at 0300", 80, target=self.day / "observation-p2.md")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertEqual(out["result"]["file"], str(self.day / "observation-p2.md"))
        self.assertEqual(self.parts(), ["observation-p2.md", "observation.md"])

    def test_a_section_too_long_for_any_part_is_refused_and_nothing_is_written(self):
        self.write_base([100])
        before = self.sha(self.base)
        r, out = self.append("2 at 0200", 460)
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("too long for a day file part", out["error"])
        self.assertEqual(self.parts(), ["observation.md"])
        self.assertEqual(self.sha(self.base), before)

    def test_a_heading_already_in_any_part_is_refused(self):
        self.write_base([700])
        self.append("2 at 0200", 100)
        r, out = self.append("2 at 0200", 50)
        self.assertEqual(r.returncode, 1)
        self.assertIn("heading already present", out["error"])
        r, out = self.append("1 at 0100", 50)                                            # a heading of the base file
        self.assertEqual(r.returncode, 1)

    def test_a_reference_heals_a_stale_day_file_into_the_part_it_writes(self):
        self.write_base([100])
        reference = self.tmp / "reference.md"
        text = self.base.read_text() + "\n" + section("9 delivered elsewhere", 50)
        reference.write_text(text.replace("items_observed: 10", "items_observed: 15"))
        r, out = self.append("2 at 0200", 120, reference=reference)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertEqual(out["result"]["restored_sections"], ["## Pass 9 delivered elsewhere"])
        self.assertLessEqual(self.words(self.base) + 0, 450)

    def test_the_folder_index_lists_each_part_once(self):
        self.write_base([700])
        self.append("2 at 0200", 100)
        index = (self.day / "INDEX.md").read_text()
        self.assertEqual(index.count("(observation-p2.md)"), 1)
        self.assertIn("(observation.md)", index)
        self.assertTrue(index.startswith("---\n"))
        self.append("3 at 0300", 80)                                                      # fits in p2: no second line for it
        self.assertEqual((self.day / "INDEX.md").read_text().count("(observation-p2.md)"), 1)
        existing = self.day / "INDEX.md"
        existing.write_text("---\ntitle: X\ncreated: 2026-11-23T00:00:00Z\nmodified: 2026-11-23T00:00:00Z\nversion: 1.2.0\n"
                            "description: d\n---\n\n# X\n\n- [observation.md](observation.md) - base\n")
        for i in range(4, 9):
            self.append(f"{i} at 0{i}00", 150)
        text = existing.read_text()
        self.assertRegex(text, r"version: 1\.[3-9]\.0")                                       # the index version moved on
        self.assertEqual(text.count("(observation-p3.md)"), 1)

    def test_other_file_names_never_roll_over(self):
        other = self.day / "scratch.md"
        other.write_text(FRONT.format(items=1, seen=1, explained=1, unexplained=0) + "\n# X\n\n" + section("1", 600))
        r, out = self.append("2 at 0200", 100, target=other)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertFalse(out["result"]["rolled_over"])
        self.assertEqual(sorted(p.name for p in self.day.glob("*.md")), ["scratch.md"])


class Checking(RolloverCase):
    def check(self, *extra):
        r = subprocess.run([sys.executable, "-B", str(TOOL), "check", "--file", str(self.base), "--format", "json", *extra],
                           capture_output=True, text=True)
        return r, json.loads(r.stdout)

    def test_check_reads_every_part_and_is_clean_after_a_rollover(self):
        self.write_base([700])
        self.append("2 at 0200", 100)
        r, out = self.check()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertEqual(out["info"]["parts"], ["observation.md", "observation-p2.md"])

    def test_a_heading_repeated_across_parts_or_a_falling_counter_is_a_problem(self):
        self.write_base([700])
        self.append("2 at 0200", 100)
        part = self.day / "observation-p2.md"
        part.write_text(part.read_text() + "\n" + section("1 at 0100", 20))             # repeats a heading of the base file
        r, out = self.check()
        self.assertEqual(r.returncode, 1)
        self.assertTrue(any("repeats across parts" in p for p in out["problems"]))
        part.write_text(part.read_text().replace("items_observed: 12", "items_observed: 3"))
        r, out = self.check()
        self.assertTrue(any("counter regression across parts" in p for p in out["problems"]))


class WordBudget(RolloverCase):
    @unittest.skipUnless(WORD_BUDGET.is_file(), "word-budget checker not found")
    def test_every_part_stays_under_the_documents_hard_limit_by_the_official_counter(self):
        budget = load(WORD_BUDGET, "word_budget")
        self.write_base([300])
        for i in range(2, 12):
            self.append(f"{i} at 0{i}00", 130)
        for path in self.day.glob("observation-p*.md"):
            self.assertLess(budget.check_text(path.read_text(), path.name)["body_words"], 500, path.name)


if __name__ == "__main__":
    unittest.main()
