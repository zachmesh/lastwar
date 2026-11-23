"""Tests for whitespace-aware redaction, `redact --verify-diff` and the redaction-only exemption in `check --staged`. All
names, patterns and markers are made up; the real denylist is never read.

Run: python3 -m unittest discover -s _tools_/lint-gate
"""
from __future__ import annotations

import json
import re
import time

from test_lint_gate import doc
from test_redact import RedactCase

NAME = "Quen Tira"                    # made up: a two-word name
MARK = "owner account"
DENYLIST = ["# made-up fixture", f"# marker: {MARK}", r"quen\s+tira"]
SILENT = ("quen", "tira")
FRONT = "---\ntitle: Profile\ncreated: 2026-11-01T00:00:00Z\nmodified: 2026-11-02T00:00:00Z\nversion: 1.2.3\ndescription: A profile\n---\n"
RECORD_FRONT = FRONT.replace("1.2.3", "0.1.0")


class WrapCase(RedactCase):
    def setUp(self):
        super().setUp()
        self.deny(DENYLIST)

    def silent(self, r):
        out = (r.stdout + r.stderr).lower()
        for text in SILENT:
            self.assertNotIn(text, out)

    def legacy(self, rel, extra=""):
        """An oversized legacy document that carries the name, committed before the gate sees any change."""
        text = doc(650, "Legacy").rstrip("\n") + f"\n\nThe owner is {NAME} here.\n{extra}"
        self.write(rel, text)
        return text


class Wrapped(WrapCase):
    def test_single_line_and_wrapped_matches_keep_every_line_and_indentation(self):
        text = (FRONT + f"\n{NAME} said hi\nthen Quen\n    Tira left\n\tQUEN   TIRA end\n  quen\n\ttira\nplain\n")
        self.write("_activities_/p/a.md", text)
        dry = self.redact(self.path("_activities_/p"))
        self.assertIn("pattern 1 x4", dry.stdout)
        self.silent(dry)
        r = self.redact(self.path("_activities_/p"), "--apply")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        out = self.read("_activities_/p/a.md")
        self.assertIn(f"\n{MARK} said hi\nthen owner\n    account left\n\towner   account end\n  owner\n\taccount\nplain\n", out)
        self.assertEqual(out.count("\n"), text.count("\n"))
        self.assertFalse(re.search("quen|tira", out, re.I))
        self.silent(r)

    def test_crlf_wrapped_match_keeps_its_crlf(self):
        self.write("_activities_/p/a.md", f"one Quen\r\n   Tira two\r\n".replace("\r\n", "\r\n"))
        self.redact(self.path("_activities_/p"), "--apply")
        self.assertEqual(self.read("_activities_/p/a.md"), "one owner\r\n   account two\r\n")

    def test_a_marker_with_fewer_or_more_words_than_the_match_still_keeps_the_line_count(self):
        self.deny(["# marker: solo", r"quen\s+tira\s+vale"])
        self.write("_activities_/p/a.md", "x Quen\nTira\nVale y\n")
        self.redact(self.path("_activities_/p"), "--apply")
        out = self.read("_activities_/p/a.md")
        self.assertEqual(out.count("\n"), 3)
        self.assertTrue(out.startswith("x solo\n"))
        self.deny(["# marker: one two three", r"quen\s+tira"])
        self.write("_activities_/p/b.md", "Quen\nTira\n")
        self.redact(self.path("_activities_/p/b.md"), "--apply")
        self.assertEqual(self.read("_activities_/p/b.md"), "one\ntwo three\n")

    def test_the_staged_check_finds_a_name_wrapped_over_added_lines(self):
        self.write("_activities_/p/a.md", f"first line\nthe name Quen\n   Tira wraps\nlast\n")
        r = self.stage_check("_activities_/p/a.md")
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("_activities_/p/a.md:2: an added line matches denylist pattern 1", r.stdout)
        self.silent(r)

    def test_census_lines_count_each_line_a_wrapped_match_covers(self):
        self.write("_activities_/p/c.md", f"{NAME}\nplain\nQuen\nTira\n")
        self.commit_clean("seed")
        data = json.loads(self.gate("watch", "--privacy", "--format", "json").stdout)
        self.assertEqual(data["per_pattern"]["1"]["lines"], 3)


class VerifyDiff(WrapCase):
    def seed(self):
        self.write("_activities_/p/a.md", FRONT + f"\nThe {NAME} and Quen\n  Tira again.\nTail line.\n")
        self.write("_records_/2026-11-22/x/run.md", RECORD_FRONT + f"\nPlayed as {NAME}.\n")
        self.write("_logs_/repo-actions/actions.jsonl",
                   json.dumps({"n": 1, "text": "start"}) + "\n" + json.dumps({"n": 2, "text": f"by {NAME}"}) + "\n"
                   + json.dumps({"n": 3, "text": "end"}) + "\n")
        self.commit_clean("legacy")

    def apply_all(self):
        r = self.redact(self.path("_activities_"), self.path("_records_"), self.path("_logs_"), "--apply", "--allow-records")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_a_pure_redaction_is_proven_and_records_keep_their_version_lines(self):
        self.seed()
        self.apply_all()
        record = self.read("_records_/2026-11-22/x/run.md")
        self.assertIn("version: 0.1.0\n", record)                        # a record changes only the name
        self.assertIn("modified: 2026-11-02T00:00:00Z\n", record)
        r = self.redact("--verify-diff", "--report-all")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("3 changed file(s), 3 redaction-only (1 with version or modified moved), 0 violation(s)", r.stdout)
        self.silent(r)

    def test_one_extra_changed_word_is_a_violation_with_a_line_number_and_no_value(self):
        self.seed()
        self.apply_all()
        text = self.read("_activities_/p/a.md").replace("Tail line.", "Tail line changed.")
        (self.repo / "_activities_/p/a.md").write_text(text)
        r = self.redact("--verify-diff")
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertRegex(r.stdout, r"violation: _activities_/p/a\.md: differs from the deterministic substitution on 1 line\(s\), first at line \d+")
        self.silent(r)

    def test_version_and_modified_may_move_in_a_versioned_file_but_never_in_a_record(self):
        self.seed()
        self.apply_all()
        (self.repo / "_activities_/p/a.md").write_text(self.read("_activities_/p/a.md").replace("version: 1.3.0", "version: 1.9.0"))
        self.assertEqual(self.redact("--verify-diff").returncode, 0)
        rec = self.repo / "_records_/2026-11-22/x/run.md"
        rec.write_text(rec.read_text().replace("version: 0.1.0", "version: 0.2.0"))
        r = self.redact("--verify-diff")
        self.assertEqual(r.returncode, 1)
        self.assertIn("_records_/2026-11-22/x/run.md", r.stdout)
        self.assertIn("version and modified may not move in a record", r.stdout)

    def test_json_lines_keep_their_line_count_and_stay_valid(self):
        self.seed()
        self.apply_all()
        log = self.repo / "_logs_/repo-actions/actions.jsonl"
        lines = log.read_text().split("\n")
        for line in lines:
            if line:
                json.loads(line)
        self.assertEqual(len(lines), 4)                                   # three entries and the final newline, as before
        self.assertIn(f"by {MARK}", lines[1])
        self.assertEqual(self.redact("--verify-diff").returncode, 0)
        log.write_text("\n".join([lines[0], lines[2], ""]))               # a deleted line
        r = self.redact("--verify-diff")
        self.assertEqual(r.returncode, 1)
        self.assertIn("line count", r.stdout)
        log.write_text("\n".join(lines + ["{}", ""][:1]) + "\n")           # an added line
        self.assertEqual(self.redact("--verify-diff").returncode, 1)

    def test_a_marker_that_breaks_json_is_caught_even_when_the_text_equals_the_substitution(self):
        self.write("_logs_/repo-actions/actions.jsonl", json.dumps({"text": f"by {NAME}"}) + "\n")
        self.commit_clean("legacy")
        self.deny(["# marker: say \"hi\" now", r"quen\s+tira"])
        self.redact(self.path("_logs_"), "--apply")                       # the tool writes it; the proof must refuse it
        r = self.redact("--verify-diff")
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("no longer valid JSON lines", r.stdout)

    def test_yaml_frontmatter_must_keep_its_shape(self):
        self.write("_activities_/p/a.md", FRONT.replace("description: A profile", f"description: about {NAME}") + "\nbody\n")
        self.commit_clean("legacy")
        self.deny(["# marker: owner: account", r"quen\s+tira"])         # a marker with a colon and a space inside a value
        self.redact(self.path("_activities_/p"), "--apply")
        r = self.redact("--verify-diff")
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("frontmatter no longer looks like valid YAML", r.stdout)

    def test_added_and_deleted_files_are_violations_and_base_can_be_named(self):
        self.seed()
        self.write("_activities_/p/new.md", "new file\n")
        self.run_git("add", "-A")
        (self.repo / "_activities_/p/a.md").unlink()
        r = self.redact("--verify-diff")
        self.assertEqual(r.returncode, 1)
        self.assertIn("violation: _activities_/p/new.md: file added", r.stdout)
        self.assertIn("violation: _activities_/p/a.md: file deleted", r.stdout)
        clean = self.redact("--verify-diff", "--base", "HEAD", "_records_")
        self.assertEqual(clean.returncode, 0, clean.stdout)
        self.assertIn("0 changed file(s)", clean.stdout)


class Exemption(WrapCase):
    def prove(self, rel):
        r = self.redact(self.path(rel), "--apply", "--allow-records")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_an_oversized_legacy_file_redacted_only_passes_and_one_extra_word_blocks_it(self):
        rel = "_activities_/p/big.md"
        self.legacy(rel)
        self.commit_clean("legacy oversized with the name")
        self.prove(rel)
        ok = self.stage_check(rel)
        self.assertEqual(ok.returncode, 0, ok.stdout + ok.stderr)
        self.assertRegex(ok.stdout, r"[1-9]\d* exempt finding")
        self.silent(ok)
        (self.repo / rel).write_text(self.read(rel).rstrip("\n") + " extra\n")
        self.run_git("reset", "-q")
        blocked = self.stage_check(rel)
        self.assertEqual(blocked.returncode, 1, blocked.stdout + blocked.stderr)
        self.assertIn(f"BLOCKED [document-concision] {rel}", blocked.stdout)
        self.silent(blocked)

    def test_a_record_redacted_only_passes_the_size_rule_without_no_verify(self):
        rel = "_records_/2026-11-22/x/long.md"
        self.legacy(rel)
        self.commit_clean("legacy record")
        self.prove(rel)
        r = self.stage_check(rel)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_the_exemption_is_per_file_so_a_mixed_commit_blocks_only_the_unproven_file(self):
        good, bad = "_activities_/p/good.md", "_activities_/p/bad.md"
        self.legacy(good)
        self.legacy(bad)
        self.commit_clean("legacy")
        self.prove("_activities_/p")
        (self.repo / bad).write_text(self.read(bad).rstrip("\n") + " one more word\n")
        r = self.stage_check("_activities_/p")
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn(f"BLOCKED [document-concision] {bad}", r.stdout)
        self.assertNotIn(f"BLOCKED [document-concision] {good}", r.stdout)
        self.silent(r)

    def test_a_new_oversized_file_and_an_edit_without_the_name_are_never_exempt(self):
        new = "_activities_/p/new.md"
        self.write(new, doc(650, "Brand new"))
        blocked = self.stage_check(new)
        self.assertEqual(blocked.returncode, 1)
        self.run_git("reset", "-q")
        rel = "_activities_/p/old.md"
        self.write(rel, doc(650, "Old"))
        self.commit_clean("legacy without the name")
        (self.repo / rel).write_text(self.read(rel).rstrip("\n") + " edited\n")
        self.assertEqual(self.stage_check(rel).returncode, 1)

    def test_without_a_marker_nothing_is_proven_and_the_normal_rules_apply(self):
        rel = "_activities_/p/big.md"
        self.legacy(rel)
        self.commit_clean("legacy")
        self.prove(rel)
        self.deny(["# made-up, no marker any more", r"quen\s+tira"])
        r = self.stage_check(rel)
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)


class WholeTree(WrapCase):
    def test_a_whole_tree_dry_run_stays_under_twenty_seconds(self):
        for n in range(700):
            self.write(f"_activities_/bulk/a{n:03d}.md", FRONT + "".join(f"line {i} of file {n} ordinary words\n" for i in range(20))
                       + (f"{NAME}\n" if n % 3 == 0 else ""))
        for n in range(40):
            self.write(f"_records_/2026-11-22/x/r{n:02d}.md", RECORD_FRONT + f"by Quen\n   Tira in record {n}\n")
        self.commit_clean("tree")
        started = time.time()
        r = self.redact(str(self.repo), "--allow-records")
        elapsed = time.time() - started
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("274 of ", r.stdout)                                # 234 files with the name on one line, 40 records with it wrapped
        self.assertLess(elapsed, 20, f"{elapsed:.1f}s")
        self.silent(r)


if __name__ == "__main__":
    import unittest
    unittest.main()
