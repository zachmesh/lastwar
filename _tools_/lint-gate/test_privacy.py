"""Tests for the privacy rule of lint_gate.py. Every denylist and fixture here is built in a temporary repository from
made-up strings; no real identifier or pattern appears in this file, and the real denylist is never read.

Run: python3 -m unittest discover -s _tools_/lint-gate
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
import unittest

from test_lint_gate import GateCase, HAVE_REFLECTION

NAME_TOKEN = "Zorblax"          # made up
CODE_TOKEN = "KRT-123"          # made up
PATTERNS = ["# made-up fixture patterns", "zorblax", r"krt-?\d{3}"]
NEVER_PRINTED = ("zorblax", "krt-123", "krt123", r"\d{3}", "unclosed")
NOTE = "_records_/2026-11-22/legacy-activity/0300-note.md"


class PrivacyCase(GateCase):
    def setUp(self):
        super().setUp()
        self.deny(PATTERNS)

    def deny(self, lines):
        (self.repo / ".git" / "privacy-denylist.txt").write_text("\n".join(lines) + "\n")

    def commit_clean(self, message="base"):
        self.run_git("add", "-A")
        self.run_git("commit", "-q", "--no-verify", "-m", message)

    def silent(self, result, *extra):
        out = (result.stdout + result.stderr).lower()
        for text in NEVER_PRINTED + extra:
            self.assertNotIn(text.lower(), out, "matched text or pattern printed")


class Blocking(PrivacyCase):
    def test_an_added_line_blocks_and_the_message_gives_path_and_line_only(self):
        self.write(NOTE, f"alpha\nbeta {NAME_TOKEN} gamma\ndelta\n")
        r = self.stage_check(NOTE)
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn(f"BLOCKED [privacy] {NOTE}:2: an added line matches denylist pattern 1", r.stdout)
        self.silent(r)

    def test_the_second_pattern_is_a_regular_expression_and_is_numbered(self):
        self.write(NOTE, f"alpha\nbeta\ncode krt123 here\n")
        r = self.stage_check(NOTE)
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn(f"{NOTE}:3: an added line matches denylist pattern 2", r.stdout)
        self.silent(r)

    def test_matching_ignores_case(self):
        self.write(NOTE, "alpha\nZORBLAX shouting\n")
        self.assertEqual(self.stage_check(NOTE).returncode, 1)

    def test_a_file_name_blocks_and_the_name_is_not_echoed(self):
        path = "_records_/2026-11-22/legacy-activity/zorblax-notes.md"
        self.write(path, "alpha\n")
        r = self.stage_check(path)
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("BLOCKED [privacy] _records_/2026-11-22/legacy-activity/[redacted]-notes.md: the file name matches "
                      "denylist pattern 1", r.stdout)
        self.silent(r)

    def test_a_line_in_a_file_whose_name_also_matches_is_reported_without_the_name(self):
        path = "_records_/2026-11-22/legacy-activity/zorblax-copy.md"
        self.write(path, f"alpha\n{NAME_TOKEN}\n")
        r = self.stage_check(path)
        self.assertIn("[redacted]-copy.md:2:", r.stdout)
        self.silent(r)

    def test_many_hits_are_listed_up_to_a_limit(self):
        self.write(NOTE, "".join(f"line {i} {NAME_TOKEN}\n" for i in range(45)))
        r = self.stage_check(NOTE)
        self.assertEqual(r.returncode, 1)
        self.assertIn("and 5 more", r.stdout)
        self.assertEqual(r.stdout.count("BLOCKED [privacy] " + NOTE + ":"), 40)
        self.silent(r)

    def test_a_clean_commit_passes_and_says_what_it_checked(self):
        self.write(NOTE, "alpha\nbeta\ngamma\n")
        r = self.stage_check(NOTE)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("privacy 2 pattern(s) over 3 added line(s)", r.stdout)


class Redaction(PrivacyCase):
    def test_removed_lines_and_deleted_files_do_not_block_a_redaction_commit(self):
        old_name = "_records_/2026-11-22/legacy-activity/zorblax-old.md"
        self.write(NOTE, f"alpha\nbeta {NAME_TOKEN}\ngamma\n")
        self.write(old_name, f"{NAME_TOKEN} everywhere\n")
        self.commit_clean("legacy with identifiers")
        self.write(NOTE, "alpha\nbeta [removed]\ngamma\n")        # the redaction itself adds no identifier
        self.run_git("rm", "-q", old_name)
        r = self.stage_check(NOTE)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.silent(r)

    def test_untouched_old_lines_are_not_judged_when_a_clean_line_is_added(self):
        self.write(NOTE, f"alpha\nbeta {NAME_TOKEN}\n")
        self.commit_clean()
        with open(self.repo / NOTE, "a") as f:
            f.write("a clean line\n")
        self.assertEqual(self.stage_check(NOTE).returncode, 0)

    def test_a_pure_rename_of_a_legacy_file_adds_no_line(self):
        self.write(NOTE, f"alpha\nbeta {NAME_TOKEN}\ngamma\ndelta\nepsilon\n")
        self.commit_clean()
        self.run_git("mv", NOTE, "_records_/2026-11-22/legacy-activity/0400-moved.md")
        self.run_git("add", "-A")
        r = self.gate("check", "--staged")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_a_new_identifier_added_beside_a_removed_one_still_blocks(self):
        self.write(NOTE, f"alpha\nbeta {NAME_TOKEN}\n")
        self.commit_clean()
        self.write(NOTE, f"alpha\nbeta changed {NAME_TOKEN} again\n")
        r = self.stage_check(NOTE)
        self.assertEqual(r.returncode, 1)
        self.assertIn(f"{NOTE}:2:", r.stdout)


class Denylist(PrivacyCase):
    def test_a_missing_denylist_is_a_warning_and_never_a_block(self):
        (self.repo / ".git" / "privacy-denylist.txt").unlink()
        self.write(NOTE, f"alpha\n{NAME_TOKEN}\n")
        r = self.stage_check(NOTE)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("warning: privacy denylist not found at .git/privacy-denylist.txt", r.stdout)
        self.assertIn("privacy not checked", r.stdout)
        self.silent(r)

    def test_an_empty_or_comment_only_denylist_warns(self):
        self.deny(["# nothing here", ""])
        self.write(NOTE, f"alpha\n{NAME_TOKEN}\n")
        r = self.stage_check(NOTE)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("holds no usable pattern", r.stdout)

    def test_an_invalid_line_is_named_by_number_only_and_the_rest_still_apply(self):
        self.deny(["# header", "[unclosed", "zorblax"])
        self.write(NOTE, f"alpha\n{NAME_TOKEN}\n")
        r = self.stage_check(NOTE)
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("denylist line 2 is not a valid regular expression", r.stdout)
        self.assertIn("denylist pattern 2", r.stdout)       # numbered among the usable and unusable lines in order
        self.silent(r)

    def test_the_privacy_rule_can_be_left_out_by_naming_the_rules(self):
        self.write(NOTE, f"alpha\n{NAME_TOKEN}\n")
        self.run_git("add", "--", NOTE)
        r = self.gate("check", "--staged", "--rules", "document-concision")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("privacy not checked", r.stdout)


class Hook(PrivacyCase):
    def test_the_hook_blocks_a_commit_and_no_verify_stays_the_owners_override(self):
        self.assertEqual(self.gate("install").returncode, 0)
        self.write(NOTE, f"alpha\n{NAME_TOKEN}\n")
        self.run_git("add", "-A")
        head = self.run_git("rev-parse", "HEAD").stdout
        blocked = self.run_git("commit", "-q", "-m", "identifier", check=False)
        self.assertNotEqual(blocked.returncode, 0)
        self.assertIn("BLOCKED [privacy]", blocked.stdout + blocked.stderr)
        self.silent(blocked)
        self.assertEqual(self.run_git("rev-parse", "HEAD").stdout, head)
        forced = self.run_git("commit", "-q", "--no-verify", "-m", "owner override", check=False)
        self.assertEqual(forced.returncode, 0, forced.stdout + forced.stderr)

    def test_commit_all_reads_the_temporary_index(self):
        self.write(NOTE, "alpha\nbeta\n")
        self.commit_clean()
        self.gate("install")
        with open(self.repo / NOTE, "a") as f:
            f.write(f"{NAME_TOKEN}\n")
        r = self.run_git("commit", "-a", "-q", "-m", "all", check=False)
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("BLOCKED [privacy]", r.stdout + r.stderr)
        self.silent(r)

    def test_a_privacy_hit_blocks_even_when_the_linter_cannot_run(self):
        self.write(NOTE, f"alpha\n{NAME_TOKEN}\n")
        self.run_git("add", "--", NOTE)
        r = self.gate("check", "--staged", "--reflection", str(self.tmp / "nowhere"))
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("BLOCKED [privacy]", r.stdout)
        self.silent(r)


class Census(PrivacyCase):
    def setUp(self):
        super().setUp()
        self.write("_records_/a.md", f"one {NAME_TOKEN}\ntwo {NAME_TOKEN}\nthree {NAME_TOKEN} and {CODE_TOKEN}\nfour\n")
        self.write("_records_/b.md", f"x {NAME_TOKEN}\n")
        self.write("_records_/zorblax-copy.md", f"{NAME_TOKEN}\n")
        self.write("_activities_/c.md", f"{NAME_TOKEN}\nplain\n{NAME_TOKEN}\n")
        self.write("notes-zorblax.md", "clean content\n")
        self.commit_clean("seed")

    def census(self, *extra):
        return self.gate("watch", "--privacy", *extra)

    def test_counts_per_top_folder_for_each_pattern(self):
        r = self.census("--format", "json")
        self.assertEqual(r.returncode, 0, r.stderr)
        data = json.loads(r.stdout)
        one, two = data["per_pattern"]["1"], data["per_pattern"]["2"]
        self.assertEqual((one["files"], one["lines"], one["file_names"]), (4, 7, 2))
        self.assertEqual(one["by_top_folder"]["_records_"], {"files": 3, "lines": 5})
        self.assertEqual(one["by_top_folder"]["_activities_"], {"files": 1, "lines": 2})
        self.assertEqual((two["files"], two["lines"], two["file_names"]), (1, 1, 0))
        self.assertEqual(data["files_matching_any"], 4)
        self.silent(r)

    def test_text_report_has_counts_and_paths_and_no_matched_text(self):
        r = self.census()
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("pattern 1: 4 files, 7 lines, 2 file name(s)", r.stdout)
        self.assertIn("_records_", r.stdout)
        self.assertIn("[redacted]-copy.md", r.stdout)        # a path whose name matches is shown redacted
        self.silent(r)

    def test_reads_head_by_default_and_the_working_tree_with_worktree(self):
        self.write("_records_/d.md", f"new {NAME_TOKEN}\n")
        head = json.loads(self.census("--format", "json").stdout)["per_pattern"]["1"]["files"]
        tree = json.loads(self.census("--format", "json", "--worktree").stdout)["per_pattern"]["1"]["files"]
        self.assertEqual((head, tree), (4, 5))

    def test_it_writes_nothing(self):
        before = self.run_git("status", "--porcelain", "--ignored").stdout
        self.census()
        self.assertEqual(self.run_git("status", "--porcelain", "--ignored").stdout, before)

    def test_without_a_denylist_it_cannot_measure(self):
        (self.repo / ".git" / "privacy-denylist.txt").unlink()
        r = self.census()
        self.assertEqual(r.returncode, 2)
        self.assertIn("not found", r.stderr)


MESSAGE = "denylist does not match as expected (regex versus fixed string?)"


class Expectations(PrivacyCase):
    """`# expect-min N` before a pattern: it must match at least N tracked files at HEAD, or the check fails loudly."""

    def setUp(self):
        super().setUp()
        self.deny(["# made-up", "# expect-min 2", r"qq[0-9]+x"])
        self.write("_records_/e1.md", "see qq12x here\n")
        self.write("_records_/e2.md", "QQ7X and qq8x\n")

    def clean(self):
        self.write(NOTE, "alpha\nbeta\n")
        return self.stage_check(NOTE)

    def test_entries_are_read_as_regular_expressions_not_fixed_strings(self):
        self.commit_clean()
        self.write(NOTE, "alpha\nthe literal text qq[0-9]+x is no match\n")
        self.assertEqual(self.stage_check(NOTE).returncode, 0)
        self.run_git("reset", "-q")
        self.write(NOTE, "alpha\nQQ42x is a match\n")
        r = self.stage_check(NOTE)
        self.assertEqual(r.returncode, 1)
        self.assertIn(f"{NOTE}:2: an added line matches denylist pattern 1", r.stdout)

    def test_met_expectation_passes_check_and_census(self):
        self.commit_clean()
        r = self.clean()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertNotIn(MESSAGE, r.stdout)
        census = self.gate("watch", "--privacy")
        self.assertEqual(census.returncode, 0, census.stdout + census.stderr)
        self.assertNotIn(MESSAGE, census.stdout)

    def test_a_pattern_matching_too_few_files_fails_loudly_in_check_and_census(self):
        (self.repo / "_records_/e2.md").unlink()
        self.commit_clean()
        r = self.clean()
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn(MESSAGE, r.stdout)
        self.assertIn("pattern 1 matches 1 tracked file(s) at HEAD, expected at least 2", r.stdout)
        self.silent(r, "qq")
        census = self.gate("watch", "--privacy")
        self.assertEqual(census.returncode, 1, census.stdout + census.stderr)
        self.assertIn(MESSAGE, census.stdout)
        self.assertIn("pattern 1: 1 files", census.stdout)       # the counts are still reported
        self.silent(census, "qq")

    def test_a_pattern_that_matches_nothing_fails_loudly(self):
        self.deny(["# expect-min 1", r"nomatchzz[0-9]+"])
        self.commit_clean()
        r = self.clean()
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("pattern 1 matches 0 tracked file(s) at HEAD, expected at least 1", r.stdout)
        self.silent(r, "nomatchzz")

    def test_files_are_counted_not_lines(self):
        self.write("_records_/e2.md", "".join(f"qq{i}x\n" for i in range(6)))     # six lines, still one file
        (self.repo / "_records_/e1.md").unlink()
        self.commit_clean()
        r = self.clean()
        self.assertIn("matches 1 tracked file(s)", r.stdout)
        self.assertEqual(r.returncode, 1)

    def test_check_without_staged_also_fails_loudly(self):
        (self.repo / "_records_/e2.md").unlink()
        self.commit_clean()
        r = self.gate("check", "--base", "HEAD")
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn(MESSAGE, r.stdout)

    def test_an_annotation_must_sit_immediately_before_its_pattern(self):
        self.commit_clean()
        for lines in (["# expect-min 50", "", r"qq[0-9]+x"], ["# expect-min 50", "# comment", r"qq[0-9]+x"]):
            self.deny(lines)
            r = self.clean()
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
            self.assertIn("expect-min is not immediately followed by a pattern and is ignored", r.stdout)
            self.run_git("reset", "-q")

    def test_the_hook_blocks_on_a_failed_expectation(self):
        self.deny(["# expect-min 9", r"qq[0-9]+x"])
        self.commit_clean()
        self.gate("install")
        self.write(NOTE, "alpha\n")
        self.run_git("add", "-A")
        blocked = self.run_git("commit", "-q", "-m", "x", check=False)
        self.assertNotEqual(blocked.returncode, 0)
        self.assertIn(MESSAGE, blocked.stdout + blocked.stderr)
        self.assertEqual(self.run_git("commit", "-q", "--no-verify", "-m", "owner override", check=False).returncode, 0)

    def test_the_cache_holds_no_pattern_text_and_follows_new_commits_and_denylist_edits(self):
        (self.repo / "_records_/e2.md").unlink()
        self.commit_clean()
        self.assertEqual(self.clean().returncode, 1)                       # one file, two expected
        cache = (self.repo / ".git" / "lint-gate-privacy-cache.json")
        self.assertTrue(cache.is_file())
        self.assertNotIn("qq", cache.read_text().lower())
        self.run_git("reset", "-q")
        self.write("_records_/e2.md", "QQ7X and qq8x\n")
        self.run_git("add", "_records_/e2.md")
        self.run_git("commit", "-q", "--no-verify", "-m", "second matching file")
        self.assertEqual(self.clean().returncode, 0)                       # only the new blob was scanned
        self.run_git("reset", "-q")
        self.deny(["# expect-min 3", r"qq[0-9]+x"])                        # an edited denylist rebuilds the cache
        self.assertEqual(self.clean().returncode, 1)


class Guard(PrivacyCase):
    """The guard tolerates decreases: a census recorded by `watch --privacy` replaces `# expect-min N` for a known pattern,
    and only a drop to zero from more than ten files fails. Fresh clones and changed patterns keep `# expect-min N`."""

    def setUp(self):
        super().setUp()
        self.deny(["# made-up", "# expect-min 3", r"qq[0-9]+x"])
        for i in range(5):
            self.write(f"_records_/m{i}.md", f"see qq{i}x here\n")
        self.commit_clean("matching files")

    def census(self, *extra):
        return self.gate("watch", "--privacy", *extra)

    def census_file(self):
        return self.repo / ".git" / "privacy-census.json"

    def verdict(self):
        self.write(NOTE, "alpha\nbeta\n")
        r = self.stage_check(NOTE)
        self.run_git("reset", "-q")
        return r

    def redact_commit(self, names, token_free="clean text now\n"):
        for n in names:
            self.write(f"_records_/{n}.md", token_free)
        self.run_git("add", "-A")
        self.run_git("commit", "-q", "--no-verify", "-m", "redaction")

    def test_a_redaction_that_lowers_a_count_below_expect_min_passes_with_a_census(self):
        self.assertEqual(self.census().returncode, 0)
        self.assertTrue(self.census_file().is_file())
        self.redact_commit(["m0", "m1", "m2", "m3"])                # 5 files down to 1, below expect-min 3
        r = self.verdict()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertNotIn(MESSAGE, r.stdout)
        self.census_file().unlink()                                # a fresh clone has no census: expect-min applies again
        r = self.verdict()
        self.assertEqual(r.returncode, 1)
        self.assertIn("matches 1 tracked file(s) at HEAD, expected at least 3 (no census yet)", r.stdout)

    def test_the_census_holds_hashes_and_counts_never_pattern_text(self):
        self.census()
        text = self.census_file().read_text()
        self.assertNotIn("qq", text.lower())
        self.assertNotIn("[0-9]", text)
        data = json.loads(text)
        self.assertEqual(list(data["patterns"].values()), [{"files": 5, "lines": 5}])
        self.assertRegex(next(iter(data["patterns"])), r"^[0-9a-f]{16}$")

    def test_a_drop_to_zero_from_more_than_ten_fails_loudly_and_accept_records_it(self):
        for i in range(12):
            self.write(f"_records_/z{i}.md", f"zz qq{i}x\n")
        self.commit_clean("more matches")
        self.assertEqual(self.census().returncode, 0)
        before = self.census_file().read_text()
        self.redact_commit([f"m{i}" for i in range(5)] + [f"z{i}" for i in range(12)])
        r = self.verdict()
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn(MESSAGE, r.stdout)
        self.assertIn("matches 0 tracked file(s) at HEAD, but the last census saw 17", r.stdout)
        self.silent(r, "qq")
        failed = self.census()
        self.assertEqual(failed.returncode, 1, failed.stdout + failed.stderr)
        self.assertIn(MESSAGE, failed.stdout)
        self.assertEqual(self.census_file().read_text(), before)    # a failing census never overwrites the record
        accepted = self.census("--accept")
        self.assertEqual(accepted.returncode, 0, accepted.stdout + accepted.stderr)
        self.assertIn("accepted 1 dropped pattern(s)", accepted.stdout)
        self.assertEqual(list(json.loads(self.census_file().read_text())["patterns"].values()), [{"files": 0, "lines": 0}])
        self.assertEqual(self.verdict().returncode, 0)

    def test_a_zero_from_ten_or_fewer_files_is_a_legitimate_redaction(self):
        self.census()
        self.redact_commit([f"m{i}" for i in range(5)])
        r = self.verdict()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_editing_other_denylist_lines_keeps_the_census_valid(self):
        self.census()
        self.deny(["# made-up, edited", "# expect-min 3", r"qq[0-9]+x", "# another entry", "unrelatedmadeup"])
        self.redact_commit(["m0", "m1", "m2", "m3"])
        r = self.verdict()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_a_changed_pattern_starts_afresh_so_a_regex_that_matches_nothing_fails_loudly(self):
        self.census()
        self.deny(["# made-up", "# expect-min 2", r"qq[0-9]+y"])      # written wrongly: matches nothing
        r = self.verdict()
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn(MESSAGE, r.stdout)
        self.assertIn("matches 0 tracked file(s) at HEAD, expected at least 2 (no census yet)", r.stdout)
        self.silent(r, "qq")

    def test_only_a_census_taken_at_head_is_recorded(self):
        self.assertEqual(self.census("--worktree").returncode, 0)
        self.assertFalse(self.census_file().exists())

    def test_expect_min_alone_still_guards_a_fresh_clone(self):
        self.redact_commit(["m0", "m1", "m2"])                       # 2 files left, no census yet
        r = self.verdict()
        self.assertEqual(r.returncode, 1)
        self.assertIn("(no census yet)", r.stdout)


class Speed(PrivacyCase):
    def test_seventeen_patterns_over_a_300_file_staged_diff_stay_under_five_seconds(self):
        import time
        lines = ["# made-up"]
        for i in range(17):
            lines += [f"# expect-min 1", rf"madeup{i}[a-z]+z"] if i < 4 else [rf"madeup{i}[a-z]+z"]
        self.deny(lines)
        for i in range(4):
            self.write(f"_records_/seed{i}.md", f"madeup{i}abcz\n")
        self.commit_clean("seed")
        for n in range(300):
            self.write(f"_records_/2026-11-22/legacy-activity/05{n:03d}-run.md",
                       "".join(f"line {i} of file {n} with some ordinary words\n" for i in range(40)))
        self.run_git("add", "-A")
        started = time.time()
        r = self.gate("check", "--staged")
        elapsed = time.time() - started
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("privacy 17 pattern(s) over 12000 added line(s)", r.stdout)
        self.assertLess(elapsed, 5, f"{elapsed:.1f}s")


class NothingCommitted(unittest.TestCase):
    def test_the_tool_files_carry_no_pattern_of_the_real_denylist_by_construction(self):
        # the real denylist is never read here: this only proves the fixtures use the made-up strings above
        self.assertEqual(NAME_TOKEN.lower(), "zorblax")
        self.assertRegex(CODE_TOKEN, r"^[A-Z]{3}-\d{3}$")


if __name__ == "__main__":
    unittest.main()
