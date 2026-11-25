"""Tests for `check --list-ignored` (the coordinator's request, 2026-11-25): `check` prints only counts of what it ignores ('N legacy structural finding(s),
M error(s) of other rules'); with the flag it also prints the path and rule of each one - never the finding text - sorted, with ` xN` when a path has N
findings of a rule, so two runs diff to what is new (a second stray file in a folder that already had one is not a new path, only an `x2`).

Run: python3 -m unittest discover -s _tools_/lint-gate
"""
from __future__ import annotations

import re
import unittest

from test_lint_gate import GateCase, HAVE_REFLECTION

ROW = re.compile(r"^  \S+  \[[a-z-]+\]( x\d+)?$")


def section(out: str, title: str) -> list[str]:
    lines = out.splitlines()
    start = next(i for i, l in enumerate(lines) if l.startswith(f"ignored - {title}"))
    rows = []
    for line in lines[start + 1:]:
        if not line.startswith("  "):
            break
        rows.append(line)
    return rows


@unittest.skipUnless(HAVE_REFLECTION, "the reflection linter is not installed")
class ListIgnored(GateCase):
    def test_without_the_flag_no_list_is_printed(self):
        r = self.gate("check", "--base", "HEAD")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertNotIn("ignored -", r.stdout)
        self.assertIn("legacy structural finding(s)", r.stdout)

    def test_the_flag_lists_every_legacy_finding_by_path_and_rule_sorted_and_counted(self):
        r = self.gate("check", "--base", "HEAD", "--list-ignored")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        header = next(l for l in r.stdout.splitlines() if l.startswith("ignored - legacy structural findings"))
        count = int(re.search(r": (\d+)", header).group(1))
        rows = section(r.stdout, "legacy structural findings")
        self.assertTrue(rows)
        self.assertTrue(all(ROW.match(row) for row in rows), rows)
        self.assertEqual(rows, sorted(rows))
        self.assertIn("  _records_/2026-11-22/bare-activity  [entry-points]", rows)
        self.assertEqual(sum(int(m.group(1)) if (m := re.search(r" x(\d+)$", row)) else 1 for row in rows), count)     # every finding is on a row
        self.assertIn(f"{count} legacy structural finding(s)", r.stdout)                                                  # the count line agrees with the list
        self.assertIn("ignored - exempt findings (exempt.txt): 0 (none)", r.stdout)

    def test_the_list_never_carries_the_finding_text(self):
        r = self.gate("check", "--base", "HEAD", "--list-ignored")
        for row in section(r.stdout, "legacy structural findings"):
            self.assertNotIn("no entry point", row)
            self.assertNotIn(": ", row)

    def test_a_second_stray_file_in_a_folder_that_already_had_one_shows_as_x2_and_two_runs_diff_to_it(self):
        before = self.gate("check", "--base", "HEAD", "--list-ignored").stdout
        self.write("_tools_/new-stray.py", "y = 2\n")                                            # a second stray file in the same type folder, already in the base
        self.run_git("add", "-A")
        self.run_git("commit", "-q", "--no-verify", "-m", "a second stray file")
        r = self.gate("check", "--base", "HEAD", "--list-ignored")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        old_rows, new_rows = set(section(before, "legacy structural findings")), set(section(r.stdout, "legacy structural findings"))
        self.assertEqual(new_rows - old_rows, {"  _tools_  [type-instance-trees] x2"})
        self.assertEqual(old_rows - new_rows, {"  _tools_  [type-instance-trees]"})

    def test_the_staged_form_lists_too(self):
        self.write("_tools_/INDEX.md", self.repo.joinpath("_tools_/INDEX.md").read_text() + "\n")
        self.run_git("add", "_tools_/INDEX.md")
        r = self.gate("check", "--staged", "--list-ignored")
        self.assertIn("ignored - legacy structural findings", r.stdout)

    def test_a_blocked_check_lists_as_well_as_blocks(self):
        self.write("_records_/2026-11-23/legacy-two/0100-run.md", "# no frontmatter\n")
        self.run_git("add", "-A")
        r = self.gate("check", "--staged", "--list-ignored")
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("BLOCKED", r.stdout)
        self.assertIn("ignored - errors of other rules", r.stdout)

    def test_the_flag_is_in_the_help(self):
        out = re.sub(r"\s+", " ", self.gate("check", "--help").stdout)
        self.assertIn("--list-ignored", out)
        self.assertIn("legacy structural, exempt and other rules", out)
