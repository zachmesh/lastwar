"""Tests for `observation.py migrate`: an UNCOMMITTED growth of a day observation file (appended sections and moved counters, made
before the rollover existed) goes into the next part, and the file is put back to its committed text byte for byte. A throwaway git
repository holds the day folder; nothing real is touched.

Run: python3 -m unittest discover -s _tools_/observation-tests
"""
from __future__ import annotations

import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from test_rollover import FRONT, OBS, TOOL, section


class MigrateCase(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp(prefix="observation-migrate-"))
        self.addCleanup(shutil.rmtree, self.root, True)
        subprocess.run(["git", "init", "-q", "-b", "main", str(self.root)], check=True)
        self.day = self.root / "_records_" / "2026-11-22" / "perception-scout"
        self.day.mkdir(parents=True)
        (self.root / "_queue_" / "claimed").mkdir(parents=True)
        (self.root / "_queue_" / "claimed" / ".gitkeep").write_text("")
        self.rel = "_records_/2026-11-22/perception-scout/observation.md"
        self.base = FRONT.format(items=20, seen=11, explained=8, unexplained=3) + "\n# Observations\n\nThe day file.\n\n" + section("1 at 1800", 120)
        (self.root / self.rel).write_text(self.base)
        self.git("add", "-A")
        self.git("-c", "user.email=t@e.org", "-c", "user.name=t", "commit", "-q", "-m", "base")

    def git(self, *args):
        return subprocess.run(["git", "-C", str(self.root), *args], capture_output=True, text=True, check=True).stdout

    @property
    def file(self):
        return self.root / self.rel

    def grow(self, *sections, items=29, seen=19, explained=14, unexplained=5):
        """What the old writer did: the counters moved in place and whole sections appended to the committed file."""
        text = self.base
        for pair in (("items_observed: 20", f"items_observed: {items}"), ("red_dots_seen: 11", f"red_dots_seen: {seen}"),
                     ("red_dots_explained: 8", f"red_dots_explained: {explained}"),
                     ("unexplained_red_dots: 3", f"unexplained_red_dots: {unexplained}")):
            text = text.replace(*pair)
        for heading, words in sections:
            text += "\n" + section(heading, words)
        self.file.write_text(text)
        return text

    def migrate(self, *extra):
        return subprocess.run([sys.executable, "-B", str(TOOL), "migrate", "--file", str(self.file), *extra], capture_output=True, text=True)

    def digest(self):
        return {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(self.day.iterdir())}

    def words(self, path):
        return OBS._file_words(Path(path).read_text())


class Migration(MigrateCase):
    def test_a_dry_run_reports_counts_and_writes_nothing(self):
        self.grow(("2 at 1900", 200))
        before = self.digest()
        r = self.migrate()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("dry run, nothing written", r.stdout)
        self.assertIn("1 section(s) would move", r.stdout)
        self.assertIn("observation-p2.md", r.stdout)
        self.assertEqual(self.digest(), before)

    def test_apply_puts_the_file_back_and_the_growth_into_the_next_part(self):
        grown = self.grow(("2 at 1900", 200))
        r = self.migrate("--apply")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertEqual(self.file.read_text(), self.git("show", f"HEAD:{self.rel}"))                  # byte for byte what git holds
        self.assertEqual(self.git("status", "--short", "--", self.rel), "")                              # the file is clean again
        part = self.day / "observation-p2.md"
        text = part.read_text()
        self.assertIn("## Pass 2 at 1900", text)
        self.assertNotIn("## Pass 1 at 1800", text)
        counters = OBS._parse_file(str(part))[0]
        self.assertEqual(counters, {"items_observed": 29, "red_dots_seen": 19, "red_dots_explained": 14, "unexplained_red_dots": 5})
        self.assertIn("title: Perception scout observations 2026-11-23 part 2", text)
        self.assertLessEqual(self.words(part), 450)
        self.assertIn("(observation-p2.md)", (self.day / "INDEX.md").read_text())
        self.assertIn(section("2 at 1900", 200).split("\n\n", 1)[1].strip(), text)                       # the section text itself is intact
        self.assertTrue(grown.split("## Pass 2 at 1900")[1].strip() in text)
        check = subprocess.run([sys.executable, "-B", str(TOOL), "check", "--file", str(self.file), "--format", "json"], capture_output=True, text=True)
        self.assertEqual(check.returncode, 0, check.stdout)
        self.assertEqual(json.loads(check.stdout)["info"]["parts"], ["observation.md", "observation-p2.md"])

    def test_the_output_is_counts_only(self):
        self.grow(("2 at 1900", 200))
        r = self.migrate("--apply")
        for text in ("w10", "w199", "Pass 2 at 1900"):
            self.assertNotIn(text, r.stdout + r.stderr)
        self.assertIn("committed", r.stdout)
        self.assertIn("counters: items_observed=29", r.stdout)

    def test_it_is_idempotent_and_a_file_equal_to_head_is_nothing_to_do(self):
        r = self.migrate("--apply")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("nothing to do", r.stdout)
        self.grow(("2 at 1900", 200))
        self.migrate("--apply")
        after = self.digest()
        again = self.migrate("--apply")
        self.assertEqual(again.returncode, 0)
        self.assertIn("nothing to do", again.stdout)
        self.assertEqual(self.digest(), after)

    def test_a_later_growth_goes_into_the_following_part(self):
        self.grow(("2 at 1900", 200))
        self.migrate("--apply")
        self.grow(("3 at 2000", 200), items=33)
        self.migrate("--apply")
        self.assertEqual(sorted(p.name for p in self.day.glob("observation*.md")), ["observation-p2.md", "observation-p3.md", "observation.md"])
        self.assertEqual(OBS._parse_file(str(self.day / "observation-p3.md"))[0]["items_observed"], 33)

    def test_many_sections_are_packed_under_the_part_limit(self):
        self.grow(("2 at 1900", 200), ("3 at 2000", 200), ("4 at 2100", 200))
        r = self.migrate("--apply")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        parts = sorted(self.day.glob("observation-p*.md"))
        self.assertEqual(len(parts), 2)
        for part in parts:
            self.assertLessEqual(self.words(part), 450, part.name)
        joined = "".join(p.read_text() for p in parts)
        for heading in ("## Pass 2 at 1900", "## Pass 3 at 2000", "## Pass 4 at 2100"):
            self.assertEqual(joined.count(heading), 1)


class Refusals(MigrateCase):
    def test_a_rewrite_of_earlier_text_is_refused_and_nothing_changes(self):
        text = self.grow(("2 at 1900", 100))
        self.file.write_text(text.replace("w5 ", "REWRITTEN ", 1))
        before = self.digest()
        r = self.migrate("--apply")
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("not a byte-exact prefix", r.stdout)
        self.assertEqual(self.digest(), before)

    def test_a_falling_counter_is_refused(self):
        self.grow(("2 at 1900", 100), items=5)
        r = self.migrate("--apply")
        self.assertEqual(r.returncode, 1)
        self.assertIn("cumulative counter items_observed fell", r.stdout)

    def test_a_heading_that_repeats_a_committed_one_is_refused(self):
        self.grow(("1 at 1800", 50))
        self.assertIn("repeats a committed heading", self.migrate("--apply").stdout)

    def test_a_single_section_too_long_for_a_part_is_refused(self):
        self.grow(("2 at 1900", 470))
        r = self.migrate("--apply")
        self.assertEqual(r.returncode, 1)
        self.assertIn("too long for a day file part", r.stdout)
        self.assertFalse((self.day / "observation-p2.md").exists())

    def test_a_claimed_unit_stops_apply_until_the_operator_is_between_units(self):
        self.grow(("2 at 1900", 100))
        (self.root / "_queue_" / "claimed" / "scout-unit.md").write_text("x")
        before = self.digest()
        r = self.migrate("--apply")
        self.assertEqual(r.returncode, 1)
        self.assertIn("_queue_/claimed/ holds a unit", r.stdout)
        self.assertEqual(self.digest(), before)
        self.assertEqual(self.migrate().returncode, 0)                                                    # a dry run is always allowed
        self.assertEqual(self.migrate("--apply", "--allow-claimed").returncode, 0)

    def test_a_file_that_changes_while_it_is_read_is_refused(self):
        text = self.grow(("2 at 1900", 100))
        _report, error, code = OBS.migrate_uncommitted(str(self.file), "HEAD", apply=True, require_idle=True,
                                                       _before_write=lambda: self.file.write_text(text + "\n## Pass 3 at 2000\n\nlate\n"))
        self.assertEqual(code, 1)
        self.assertIn("changed while it was being read", error)
        self.assertFalse((self.day / "observation-p2.md").exists())
        self.assertIn("## Pass 3 at 2000", self.file.read_text())                                         # the late write is untouched

    def test_a_file_outside_git_or_missing_at_the_revision_is_exit_two(self):
        outside = Path(tempfile.mkdtemp(prefix="not-git-"))
        self.addCleanup(shutil.rmtree, outside, True)
        (outside / "observation.md").write_text(self.base)
        r = subprocess.run([sys.executable, "-B", str(TOOL), "migrate", "--file", str(outside / "observation.md")], capture_output=True, text=True)
        self.assertEqual(r.returncode, 2)
        self.assertEqual(self.migrate("--base", "no-such-rev").returncode, 2)


if __name__ == "__main__":
    unittest.main()
