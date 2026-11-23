"""Tests for `lint_gate.py redact`. Every denylist, marker and fixture is made up in a temporary repository; no real
identifier, pattern or marker appears here and the real denylist is never read.

Run: python3 -m unittest discover -s _tools_/lint-gate
"""
from __future__ import annotations

import os
import re
import subprocess
import sys
import time
from pathlib import Path

from test_lint_gate import HERE
from test_privacy import PrivacyCase, NAME_TOKEN, CODE_TOKEN

SPLIT = HERE.parent / "split-doc" / "split_doc.py"
MARK_ONE, MARK_TWO = "the redacted name", "[tag]"
DENYLIST = ["# made-up fixture patterns", f"# marker: {MARK_ONE}", "zorblax", "# expect-min 0", f"# marker: {MARK_TWO}",
            r"krt-?\d{3}", r"quuxy[a-z]+"]                     # the third pattern has no marker
FRONT = "---\ntitle: Profile\ncreated: 2026-11-01T00:00:00Z\nmodified: 2026-11-02T00:00:00Z\nversion: 1.2.3\ndescription: A profile\n---\n"
NEVER = ("zorblax", "krt-123", "krt123", "quuxy", MARK_ONE, MARK_TWO, r"\d{3}")


class RedactCase(PrivacyCase):
    def setUp(self):
        super().setUp()
        self.deny(DENYLIST)

    def path(self, rel):
        return str(self.repo / rel)

    def redact(self, *args):
        return self.gate("redact", *args)

    def read(self, rel):
        return (self.repo / rel).read_bytes().decode()

    def quiet(self, r):
        out = (r.stdout + r.stderr).lower()
        for text in NEVER:
            self.assertNotIn(text.lower(), out)


class DryRun(RedactCase):
    def test_default_is_a_dry_run_with_counts_and_no_matched_text(self):
        self.write("_activities_/p/INDEX.md", FRONT + f"\nhello {NAME_TOKEN} and {NAME_TOKEN.upper()}\nid {CODE_TOKEN}\n")
        before = self.read("_activities_/p/INDEX.md")
        r = self.redact(self.path("_activities_/p"))
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("_activities_/p/INDEX.md: pattern 1 x2, pattern 2 x1", r.stdout)
        self.assertIn("per pattern (files/matches): 1: 1/2, 2: 1/1", r.stdout)
        self.assertIn("dry run", r.stdout)
        self.quiet(r)
        self.assertEqual(self.read("_activities_/p/INDEX.md"), before)

    def test_a_file_name_that_matches_is_shown_redacted(self):
        self.write(f"_activities_/p/{NAME_TOKEN.lower()}-copy.md", f"{NAME_TOKEN}\n")
        r = self.redact(self.path("_activities_/p"))
        self.assertIn("[redacted]-copy.md", r.stdout)
        self.quiet(r)


class Apply(RedactCase):
    def test_every_match_becomes_its_marker_and_nothing_else_changes(self):
        crlf = (FRONT + f"\r\n  indented {NAME_TOKEN} line\r\nplain\r\ncode {CODE_TOKEN.lower()} here\r\n").replace("\n", "\r\n").replace("\r\r", "\r")
        no_newline = f"first {NAME_TOKEN}\n    keep four spaces\nlast line {NAME_TOKEN.upper()} without newline"
        self.write("_activities_/p/crlf.md", crlf)
        self.write("_activities_/p/plain.md", no_newline)
        r = self.redact(self.path("_activities_/p"), "--apply")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.quiet(r)
        a, b = self.read("_activities_/p/crlf.md"), self.read("_activities_/p/plain.md")
        self.assertEqual(b, f"first {MARK_ONE}\n    keep four spaces\nlast line {MARK_ONE} without newline")   # no final newline added
        self.assertEqual(a.count("\r\n"), crlf.count("\r\n"))                                                 # line endings kept
        self.assertIn(f"  indented {MARK_ONE} line\r\n", a)                                                  # indentation kept
        self.assertIn(f"code {MARK_TWO} here\r\n", a)
        self.assertFalse(re.search(r"zorblax|krt-?\d{3}", a + b, re.I))
        self.assertEqual(self.redact(self.path("_activities_/p"), "--verify").returncode, 0)

    def test_the_replacement_is_the_same_for_every_match_and_idempotent(self):
        self.write("_activities_/p/a.md", FRONT + f"\n{NAME_TOKEN} {NAME_TOKEN.upper()} {NAME_TOKEN.title()}\n")
        self.redact(self.path("_activities_/p"), "--apply")
        first = self.read("_activities_/p/a.md")
        self.assertEqual(first.count(MARK_ONE), 3)
        again = self.redact(self.path("_activities_/p"), "--apply")
        self.assertEqual(again.returncode, 0)
        self.assertIn("0 of 1 file(s) match", again.stdout)
        self.assertEqual(self.read("_activities_/p/a.md"), first)             # no second bump

    def test_a_match_over_a_line_break_keeps_its_whitespace_so_the_line_structure_is_stable(self):
        self.deny(["# marker: X Y", r"alpha\s+beta"])
        self.write("_activities_/p/a.md", "alpha\nbeta\nalpha  beta\n  alpha\n    beta tail\n")
        self.redact(self.path("_activities_/p"), "--apply")
        self.assertEqual(self.read("_activities_/p/a.md"), "X\nY\nX  Y\n  X\n    Y tail\n")

    def test_a_marker_that_would_leave_a_match_is_refused_and_nothing_is_written(self):
        self.deny([f"# marker: see {NAME_TOKEN}", "zorblax"])
        self.write("_activities_/p/a.md", f"{NAME_TOKEN}\n")
        r = self.redact(self.path("_activities_/p"), "--apply")
        self.assertEqual(r.returncode, 1)
        self.assertIn("would leave pattern(s) 1 matching", r.stdout)
        self.assertEqual(self.read("_activities_/p/a.md"), f"{NAME_TOKEN}\n")


class Markers(RedactCase):
    def test_apply_refuses_a_matching_pattern_with_no_marker_and_writes_nothing(self):
        self.write("_activities_/p/a.md", f"{NAME_TOKEN}\n")
        self.write("_activities_/p/b.md", "has quuxyabc here\n")
        r = self.redact(self.path("_activities_/p"), "--apply")
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("pattern(s) 3 match but have no `# marker:` line", r.stdout)
        self.assertIn("nothing written", r.stdout)
        self.assertEqual(self.read("_activities_/p/a.md"), f"{NAME_TOKEN}\n")        # the marked match is untouched too
        self.assertEqual(self.read("_activities_/p/b.md"), "has quuxyabc here\n")
        self.quiet(r)

    def test_a_dry_run_reports_the_unmarked_pattern_and_exits_zero(self):
        self.write("_activities_/p/b.md", "has quuxyabc here\n")
        r = self.redact(self.path("_activities_/p"))
        self.assertEqual(r.returncode, 0)
        self.assertIn("pattern(s) 3 match but have no `# marker:` line", r.stdout)

    def test_an_unmarked_pattern_that_matches_nothing_does_not_stop_the_run(self):
        self.write("_activities_/p/a.md", f"{NAME_TOKEN}\n")
        r = self.redact(self.path("_activities_/p"), "--apply")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_annotations_may_come_in_either_order_before_a_pattern(self):
        for lines in (["# expect-min 0", "# marker: M", "zorblax"], ["# marker: M", "# expect-min 0", "zorblax"]):
            self.deny(lines)
            self.write("_activities_/p/a.md", f"{NAME_TOKEN}\n")
            r = self.redact(self.path("_activities_/p"), "--apply")
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
            self.assertNotIn("not immediately followed", r.stdout)
            self.assertEqual(self.read("_activities_/p/a.md"), "M\n")

    def test_both_annotations_of_a_stacked_pattern_are_kept(self):
        self.deny(["# marker: M", "# expect-min 1", "zorblax", "# expect-min 1", "# marker: N", r"krt-?\d{3}"])
        self.write("_activities_/p/a.md", f"{NAME_TOKEN} {CODE_TOKEN}\n")
        self.redact(self.path("_activities_/p"), "--apply")
        self.assertEqual(self.read("_activities_/p/a.md"), "M N\n")


class Refusals(RedactCase):
    def test_records_and_the_done_queue_need_allow_records(self):
        self.write("_records_/2026-11-22/x/run.md", f"{NAME_TOKEN}\n")
        self.write("_queue_/done/unit.md", f"{NAME_TOKEN}\n")
        for rel in ("_records_/2026-11-22/x/run.md", "_queue_/done/unit.md", "_records_"):
            r = self.redact(self.path(rel), "--apply")
            self.assertEqual(r.returncode, 1, rel)
            self.assertIn("immutable play records (C1)", r.stdout)
            self.assertIn("nothing written", r.stdout)
        self.assertEqual(self.read("_records_/2026-11-22/x/run.md"), f"{NAME_TOKEN}\n")
        r = self.redact(self.path("_records_/2026-11-22/x/run.md"), "--apply", "--allow-records")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertEqual(self.read("_records_/2026-11-22/x/run.md"), f"{MARK_ONE}\n")

    def test_git_binary_symlink_and_outside_paths_are_refused(self):
        (self.repo / "_activities_").mkdir(exist_ok=True)
        (self.repo / "_activities_/blob.bin").write_bytes(b"\0\1\2" + NAME_TOKEN.encode())
        (self.repo / "_activities_/link.md").symlink_to(self.repo / "_tools_/INDEX.md")
        for target in (self.repo / ".git" / "privacy-denylist.txt", self.repo / "_activities_/blob.bin",
                       self.repo / "_activities_/link.md", self.tmp / "outside.md"):
            (self.tmp / "outside.md").write_text(f"{NAME_TOKEN}\n")
            r = self.redact(str(target), "--apply")
            self.assertEqual(r.returncode, 1, str(target))
            self.assertIn("refused", r.stdout)
        self.assertEqual((self.tmp / "outside.md").read_text(), f"{NAME_TOKEN}\n")
        self.assertTrue((self.repo / ".git" / "privacy-denylist.txt").read_text().startswith("# made-up"))

    def test_a_walk_skips_sockets_and_pipes_instead_of_reading_them(self):
        import socket as sock
        self.write("_activities_/p/a.md", f"{NAME_TOKEN}\n")
        (self.repo / "_tools_" / "state").mkdir(parents=True, exist_ok=True)
        server = sock.socket(sock.AF_UNIX, sock.SOCK_STREAM)
        self.addCleanup(server.close)
        server.bind(str(self.repo / "_tools_" / "state" / "x.sock"))
        os.mkfifo(self.repo / "_tools_" / "state" / "pipe")
        r = self.redact(str(self.repo))
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("_activities_/p/a.md", r.stdout)
        self.assertRegex(r.stdout, r"[1-9]\d* other")

    def test_walking_a_folder_skips_records_binary_and_git_and_counts_them(self):
        self.write("_activities_/p/a.md", f"{NAME_TOKEN}\n")
        (self.repo / "_activities_/p/pic.bin").write_bytes(b"\0" + NAME_TOKEN.encode())
        self.write("_records_/2026-11-22/x/run.md", f"{NAME_TOKEN}\n")
        r = self.redact(str(self.repo))
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("1 binary", r.stdout)
        self.assertRegex(r.stdout, r"skipped: 1 binary, [1-9]\d* in records or done queue")
        self.assertIn("_activities_/p/a.md", r.stdout)
        self.assertNotIn("run.md", r.stdout)


class Outside(RedactCase):
    def scratch(self):
        import shutil, tempfile
        d = Path(tempfile.mkdtemp(prefix="redact-outside-", dir="/tmp"))
        self.addCleanup(shutil.rmtree, d, True)
        return d

    def test_an_explicit_file_under_tmp_needs_allow_outside_and_is_then_redacted(self):
        saved = self.scratch() / "original.md"
        saved.write_text(FRONT + f"\nname {NAME_TOKEN}\n")
        refused = self.redact(str(saved), "--apply")
        self.assertEqual(refused.returncode, 1, refused.stdout)
        self.assertIn("--allow-outside takes only an explicit file under /tmp", refused.stdout)
        self.assertIn(NAME_TOKEN, saved.read_text())
        ok = self.redact(str(saved), "--apply", "--allow-outside")
        self.assertEqual(ok.returncode, 0, ok.stdout + ok.stderr)
        text = saved.read_text()
        self.assertIn(f"name {MARK_ONE}\n", text)
        self.assertIn("version: 1.3.0\n", text)                    # the saved original is bumped like any file
        self.assertIn("(outside, under /tmp)", ok.stdout)
        self.quiet(ok)

    def test_allow_outside_takes_neither_folders_nor_files_elsewhere(self):
        folder = self.scratch()
        (folder / "a.md").write_text(f"{NAME_TOKEN}\n")
        r = self.redact(str(folder), "--apply", "--allow-outside")
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertEqual((folder / "a.md").read_text(), f"{NAME_TOKEN}\n")
        elsewhere = self.tmp / "elsewhere.md"                        # a temporary folder outside /tmp proper
        elsewhere.write_text(f"{NAME_TOKEN}\n")
        r = self.redact(str(elsewhere), "--apply", "--allow-outside")
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertEqual(elsewhere.read_text(), f"{NAME_TOKEN}\n")

    def test_the_saved_original_and_the_split_folder_compare_equal_after_redaction(self):
        text = (FRONT + "\n# Doc\n\nIntro.\n" + "".join(
            f"\n## Part {i}\n\n" + " ".join(f"a{i}x{j}" for j in range(220)) + f" {NAME_TOKEN} tail\n" for i in range(4)))
        saved = self.scratch() / "saved.md"
        saved.write_text(text)
        self.write("_activities_/docs/doc.md", text)
        subprocess.run([sys.executable, "-B", str(SPLIT), self.path("_activities_/docs/doc.md"), "--apply"], capture_output=True)
        self.assertEqual(self.redact(self.path("_activities_/docs/doc"), "--apply").returncode, 0)
        self.assertEqual(self.redact(str(saved), "--apply", "--allow-outside").returncode, 0)
        r = subprocess.run([sys.executable, "-B", str(SPLIT), "--check", self.path("_activities_/docs/doc"), str(saved)],
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)


class Report(RedactCase):
    def setUp(self):
        super().setUp()
        for n in range(60):
            self.write(f"_activities_/bulk/f{n:02d}.md", f"line {NAME_TOKEN}\n")
        for n in range(5):
            self.write(f"_activities_/other/g{n}.md", f"{NAME_TOKEN} {NAME_TOKEN}\n{CODE_TOKEN}\n")

    def test_the_listing_stops_at_forty_files_unless_report_all(self):
        short = self.redact(self.path("_activities_"))
        self.assertIn("... and 25 more file(s); --report-all lists them all", short.stdout)
        self.assertEqual(len(re.findall(r"^_activities_/\w+/\w+\.md: pattern", short.stdout, re.M)), 40)
        full = self.redact(self.path("_activities_"), "--report-all")
        self.assertNotIn("more file(s)", full.stdout)
        self.assertEqual(len(re.findall(r"^_activities_/\w+/\w+\.md: pattern", full.stdout, re.M)), 65)
        self.quiet(full)

    def test_per_profile_totals_name_files_and_matches(self):
        r = self.redact(self.path("_activities_"), "--apply", "--report-all")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertRegex(r.stdout, r"_activities_/bulk\s+60 files, 60 matches: p1 60f/60m")
        self.assertRegex(r.stdout, r"_activities_/other\s+5 files, 15 matches: p1 5f/10m, p2 5f/5m")
        self.quiet(r)


class Frontmatter(RedactCase):
    def test_version_and_modified_move_only_in_a_changed_file_and_the_report_names_it(self):
        self.write("_activities_/p/changed.md", FRONT + f"\nname {NAME_TOKEN}\n")
        self.write("_activities_/p/untouched.md", FRONT + "\nnothing to redact\n")
        self.write("_activities_/p/quoted.md", '---\ntitle: Q\nmodified: "2026-11-02T00:00:00Z"\nversion: "2.0.1"\n---\n' + f"{NAME_TOKEN}\n")
        self.write("_activities_/p/noversion.md", f"---\ntitle: N\n---\n{NAME_TOKEN}\n")
        self.write("_activities_/p/nofront.md", f"{NAME_TOKEN}\n")
        untouched = self.read("_activities_/p/untouched.md")
        r = self.redact(self.path("_activities_/p"), "--apply")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        changed = self.read("_activities_/p/changed.md")
        self.assertIn("version: 1.3.0\n", changed)
        self.assertRegex(changed, r"modified: \d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ\n")
        self.assertNotIn("modified: 2026-11-02T00:00:00Z", changed)
        self.assertIn("created: 2026-11-01T00:00:00Z\n", changed)
        self.assertIn('version: "2.1.0"\n', self.read("_activities_/p/quoted.md"))
        self.assertRegex(self.read("_activities_/p/quoted.md"), r'modified: "\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ"\n')
        self.assertEqual(self.read("_activities_/p/untouched.md"), untouched)
        self.assertEqual(self.read("_activities_/p/noversion.md"), f"---\ntitle: N\n---\n{MARK_ONE}\n")
        self.assertEqual(self.read("_activities_/p/nofront.md"), f"{MARK_ONE}\n")
        self.assertIn("needs a changelog line: _activities_/p/changed.md (version 1.2.3 -> 1.3.0)", r.stdout)
        self.assertIn("needs a changelog line: _activities_/p/quoted.md (version 2.0.1 -> 2.1.0)", r.stdout)
        self.assertIn("no version fields to bump: _activities_/p/nofront.md", r.stdout)
        self.assertNotIn("untouched.md", r.stdout)
        self.quiet(r)

    def test_every_frontmatter_value_is_covered_including_unchanged_list_lines(self):
        front = (f"---\ntitle: Profile\ncreated: 2026-11-01T00:00:00Z\nmodified: 2026-11-02T00:00:00Z\nversion: 3.4.5\n"
                 f"description: about {NAME_TOKEN}\ngrounded_in:\n  - source: observation by {NAME_TOKEN.upper()} on 2026-11-01\n"
                 f"  - source: {CODE_TOKEN} screen\nstatus: active\n---\n")
        self.write("_activities_/p/INDEX.md", front + "\nclean body\n")
        self.commit_clean("legacy with identifiers in frontmatter only")
        dry = self.redact(self.path("_activities_/p"))
        self.assertIn("_activities_/p/INDEX.md: pattern 1 x2, pattern 2 x1", dry.stdout)          # found although no line is added
        self.quiet(dry)
        self.redact(self.path("_activities_/p"), "--apply")
        text = self.read("_activities_/p/INDEX.md")
        self.assertIn(f"  - source: observation by {MARK_ONE} on 2026-11-01\n", text)
        self.assertIn(f"  - source: {MARK_TWO} screen\n", text)
        self.assertIn(f"description: about {MARK_ONE}\n", text)
        self.assertIn("version: 3.5.0\n", text)
        self.assertTrue(text.endswith("status: active\n---\n\nclean body\n"))
        self.assertEqual(self.redact(self.path("_activities_/p"), "--verify").returncode, 0)

    def test_a_match_inside_the_frontmatter_is_replaced_and_the_file_stays_valid(self):
        self.write("_activities_/p/a.md", f"---\ntitle: About {NAME_TOKEN}\nmodified: 2026-11-02T00:00:00Z\nversion: 0.1.0\n---\nbody\n")
        self.redact(self.path("_activities_/p"), "--apply")
        text = self.read("_activities_/p/a.md")
        self.assertTrue(text.startswith(f"---\ntitle: About {MARK_ONE}\n"))
        self.assertIn("version: 0.2.0\n", text)
        self.assertTrue(text.endswith("---\nbody\n"))


class Verify(RedactCase):
    def test_verify_fails_while_a_pattern_matches_and_passes_after_apply(self):
        self.write("_activities_/p/a.md", f"{NAME_TOKEN}\n")
        r = self.redact(self.path("_activities_/p"), "--verify")
        self.assertEqual(r.returncode, 1)
        self.assertIn("1 file(s) still match", r.stdout)
        self.quiet(r)
        self.redact(self.path("_activities_/p"), "--apply")
        self.assertEqual(self.redact(self.path("_activities_/p"), "--verify").returncode, 0)

    def test_a_redaction_commit_passes_the_privacy_gate(self):
        self.write("_activities_/p/a.md", FRONT + f"\nname {NAME_TOKEN}\n")
        self.commit_clean("legacy with the identifier")
        self.redact(self.path("_activities_/p"), "--apply")
        r = self.stage_check("_activities_/p/a.md")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)


class WithSplitDoc(RedactCase):
    TEXT = (FRONT + "\n# Profile\n\nIntro line.\n" + "".join(
        f"\n## Section {i}\n\n" + " ".join(f"w{i}x{j}" for j in range(150)) + f" {NAME_TOKEN} " + " ".join(
            f"v{i}x{j}" for j in range(40)) + f" and {CODE_TOKEN.lower()} again.\n" for i in range(6)))

    def split(self, *args):
        return subprocess.run([sys.executable, "-B", str(SPLIT), *args], capture_output=True, text=True)

    def test_redacting_the_original_and_its_split_folder_keeps_check_equal(self):
        self.write("_activities_/docs/register.md", self.TEXT)
        self.write("_activities_/refs/register-copy.md", self.TEXT)
        self.assertEqual(self.split(self.path("_activities_/docs/register.md"), "--apply").returncode, 0)
        folder = self.repo / "_activities_/docs/register"
        self.assertEqual(self.redact(str(folder), "--apply").returncode, 0)
        self.assertEqual(self.redact(self.path("_activities_/refs/register-copy.md"), "--apply").returncode, 0)
        r = self.split("--check", str(folder), self.path("_activities_/refs/register-copy.md"))
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("EQUAL", r.stdout)
        self.assertEqual(self.redact(str(folder), "--verify").returncode, 0)

    BIG = (f"---\ntitle: Big profile\ncreated: 2026-11-01T00:00:00Z\nmodified: 2026-11-02T00:00:00Z\nversion: 2.0.0\n"
           f"description: about {NAME_TOKEN}\ngrounded_in:\n  - source: seen by {NAME_TOKEN.upper()} on 2026-11-01\n  - source: {CODE_TOKEN} screen\n---\n"
           "\n# Big\n\nIntro line.\n" + "".join(
               f"\n## Section {i}\n\nThe {NAME_TOKEN} case {i} began here. " + " ".join(f"w{i}x{j}" for j in range(290)) + "\n"
               for i in range(70)))

    def test_a_split_with_catalog_pages_and_frontmatter_values_redacts_cleanly_and_stays_equal(self):
        self.write("_activities_/docs/big.md", self.BIG)
        self.write("_activities_/refs/big-copy.md", self.BIG)
        self.assertEqual(self.split(self.path("_activities_/docs/big.md"), "--apply").returncode, 0)
        folder = self.repo / "_activities_/docs/big"
        catalogs = sorted(folder.glob("catalog-*.md"))
        self.assertTrue(catalogs, "the fixture must produce catalog pages")
        self.assertTrue(any(NAME_TOKEN.lower() in c.read_text().lower() for c in catalogs), "catalog lines copy the first sentences")
        self.assertIn(NAME_TOKEN.upper(), (folder / "INDEX.md").read_text())                        # INDEX keeps the original frontmatter
        dry = self.redact(str(folder))
        self.assertEqual(dry.returncode, 0, dry.stdout + dry.stderr)
        self.assertIn("catalog-01.md", dry.stdout)
        self.assertIn("INDEX.md", dry.stdout)
        self.quiet(dry)
        applied = self.redact(str(folder), "--apply")
        self.assertEqual(applied.returncode, 0, applied.stdout + applied.stderr)
        self.assertIn("redact verified: 0 file(s) still match", applied.stdout)
        for p in folder.glob("*.md"):
            self.assertFalse(re.search(r"zorblax|krt-?\d{3}", p.read_text(), re.I), p.name)        # every file, frontmatter included
        self.assertEqual(self.redact(self.path("_activities_/refs/big-copy.md"), "--apply").returncode, 0)
        r = self.split("--check", str(folder), self.path("_activities_/refs/big-copy.md"))
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("EQUAL", r.stdout)

    def test_the_same_holds_for_the_entry_form(self):
        self.write("_activities_/docs/register.md", self.TEXT)
        self.write("_activities_/refs/register-copy.md", self.TEXT)
        r = self.split(self.path("_activities_/docs/register.md"), "--keep-entry", "register-log", "--apply")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertEqual(self.redact(self.path("_activities_/docs"), "--apply").returncode, 0)
        self.assertEqual(self.redact(self.path("_activities_/refs/register-copy.md"), "--apply").returncode, 0)
        r = self.split("--check", self.path("_activities_/docs/register-log"), self.path("_activities_/refs/register-copy.md"))
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertEqual(self.redact(self.path("_activities_/docs"), "--verify").returncode, 0)

    def test_redacting_before_splitting_gives_clean_file_names(self):
        text = FRONT + f"\n## {NAME_TOKEN} plan\n\n" + " ".join(f"w{j}" for j in range(200)) + f"\n\n## Other {NAME_TOKEN}\n\ntext\n"
        self.write("_activities_/docs/register.md", text)
        self.assertEqual(self.redact(self.path("_activities_/docs/register.md"), "--apply").returncode, 0)
        self.assertEqual(self.split(self.path("_activities_/docs/register.md"), "--apply").returncode, 0)
        names = os.listdir(self.repo / "_activities_/docs/register")
        self.assertFalse([n for n in names if re.search("zorblax", n, re.I)], names)
        self.run_git("add", "-A")
        r = self.gate("check", "--staged", "--rules", "privacy")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)


class Speed(RedactCase):
    def test_a_hundred_files_redact_in_under_three_seconds(self):
        lines = ["# made-up"]
        for i in range(17):
            lines += [f"# marker: M{i}", rf"madeup{i}[a-z]+z"]
        self.deny(lines)
        for n in range(100):
            self.write(f"_activities_/bulk/f{n:03d}.md", FRONT + "".join(
                f"line {i} of file {n} madeup{i % 17}abcz and ordinary words here\n" for i in range(50)))
        started = time.time()
        dry = self.redact(self.path("_activities_/bulk"))
        dry_time = time.time() - started
        started = time.time()
        applied = self.redact(self.path("_activities_/bulk"), "--apply")
        apply_time = time.time() - started
        self.assertEqual((dry.returncode, applied.returncode), (0, 0), dry.stdout + applied.stdout + applied.stderr)
        self.assertIn("100 of 100 file(s) match", dry.stdout)
        self.assertLess(dry_time, 3, f"{dry_time:.1f}s")
        self.assertLess(apply_time, 3, f"{apply_time:.1f}s")


if __name__ == "__main__":
    import unittest
    unittest.main()
