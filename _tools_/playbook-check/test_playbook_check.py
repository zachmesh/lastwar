"""Tests for playbook_check.py on a throwaway git repository: each card finding, the stale rule, citations that resolve directly or through
moved-paths.csv, the changed and daily modes, counts-only output and read-only behaviour.

Run: python3 -m unittest discover -s _tools_/playbook-check
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

HERE = Path(__file__).resolve().parent
TOOL = HERE / "playbook_check.py"
NOW = "2026-11-23T12:00:00Z"
R1 = "_records_/2026-11-21/alpha-one/0145-queue-run.md"
R2 = "_records_/2026-11-20/alpha-one/0900-queue-run.md"
SECRET = "a rule sentence that must never be printed"


def card(rules=None, route=None, failures=None, questions=None, numbers=None, links=None, extra="", order=None, drop=()):
    rules = rules if rules is not None else [f"- R1 [verified 2026-11-21] Donate with coins first {SECRET}. (evidence: {R1})",
                                             f"- R2 [unverified 2026-11-20] The button greys after nine. (evidence: {R2})"]
    route = route if route is not None else ["1. Open the menu.", "2. Tap donate."]
    failures = failures if failures is not None else ["- The button is grey - wait for the cooldown."]
    questions = questions if questions is not None else ["- Does the cap reset at the daily reset? test: read the counter at 01:55 and 02:05."]
    numbers = numbers if numbers is not None else [f"42 donations in 6 units over 7 days ({R1})."]
    links = links if links is not None else ["- [rule digest](rule-digest.md)"]
    sections = {"Goal": ["Donate every available coin donation each cycle."], "Route": route, "Rules": rules, "Failures": failures,
                "Open questions": questions, "Numbers": numbers, "Links": links}
    names = order or list(sections)
    text = "---\ntitle: Alpha One\ncreated: 2026-11-23T05:00:00Z\nmodified: 2026-11-23T05:00:00Z\nversion: 1.0.0\ndescription: Playbook card of alpha-one\n---\n# Alpha one\n"
    for name in names:
        if name in drop:
            continue
        text += f"\n## {name}\n" + "\n".join(sections[name]) + "\n"
    return text + extra


class Repo(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp(prefix="playbook-check-"))
        self.addCleanup(shutil.rmtree, self.root, True)
        subprocess.run(["git", "init", "-q", "-b", "main", str(self.root)], check=True)
        for rec in (R1, R2):
            self.write(rec, "---\ntitle: record\n---\nrecord\n")
        self.write("_activities_/alpha-one/rule-digest.md", "---\ntitle: digest\n---\nrules\n")
        self.write("_activities_/alpha-one/INDEX.md", card())
        self.write("_activities_/beta-two/INDEX.md", "---\ntitle: Beta\n---\n# Beta\n\n- [a](a.md)\n- [b](b.md)\n")           # a link list, not a card yet
        self.commit("base")

    def write(self, rel, text):
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)

    def git(self, *args):
        return subprocess.run(["git", "-C", str(self.root), "-c", "user.email=t@e.org", "-c", "user.name=t", *args], capture_output=True, text=True, check=True).stdout

    def commit(self, message):
        self.git("add", "-A")
        self.git("commit", "-q", "-m", message)

    def run_tool(self, *args, now=NOW):
        return subprocess.run([sys.executable, "-B", str(TOOL), "--root", str(self.root), "--now", now, *args], capture_output=True, text=True)

    def check(self, text, *top):
        self.write("_activities_/alpha-one/INDEX.md", text)
        r = self.run_tool("--format", "json", *top, "check", "_activities_/alpha-one/INDEX.md")
        self.assertIn(r.returncode, (0, 1), r.stdout + r.stderr)
        data = json.loads(r.stdout)
        return r, data["cards"][0]


class Shape(Repo):
    def test_a_good_card_passes_with_no_findings(self):
        r, c = self.check(card())
        self.assertEqual(r.returncode, 0, r.stdout)
        self.assertEqual((c["errors"], c["warnings"]), ({}, {}))
        self.assertEqual((c["counts"]["rules_total"], c["counts"]["rules_verified"], c["counts"]["rules_unverified"]), (2, 1, 1))
        self.assertEqual((c["counts"]["citations_direct"], c["counts"].get("citations_missing", 0)), (3, 0))

    def test_a_card_over_300_words_is_too_long(self):
        r, c = self.check(card(failures=["- " + " ".join(f"w{i}" for i in range(320)) + " - fix"]))
        self.assertEqual(r.returncode, 1)
        self.assertIn("card-too-long", c["errors"])
        r, c = self.check(card(), "--card-words", "20")
        self.assertIn("card-too-long", c["errors"])

    def test_missing_and_misordered_and_unexpected_sections(self):
        self.assertIn("missing-section", self.check(card(drop=("Failures",)))[1]["errors"])
        order = ["Goal", "Rules", "Route", "Failures", "Open questions", "Numbers", "Links"]
        self.assertIn("section-order", self.check(card(order=order))[1]["errors"])
        self.assertIn("unexpected-section", self.check(card(extra="\n## Errata\n- a correction\n"))[1]["errors"])
        self.assertNotIn("unexpected-section", self.check(card(extra="\n## Changelog\n\n- 1.0.0 - first.\n"))[1]["errors"])

    def test_counts_are_limited(self):
        steps = [f"{n}. step" for n in range(1, 10)]
        self.assertIn("route-too-long", self.check(card(route=steps))[1]["errors"])
        self.assertIn("route-empty", self.check(card(route=["no numbers here"]))[1]["errors"])
        six = [f"- R{n} [verified 2026-11-21] rule {n}. (evidence: {R1})" for n in range(1, 7)]
        self.assertIn("too-many-rules", self.check(card(rules=six))[1]["errors"])
        self.assertIn("too-many-failures", self.check(card(failures=[f"- f{n} - fix" for n in range(4)]))[1]["errors"])
        self.assertIn("too-many-questions", self.check(card(questions=[f"- q{n}? test: t" for n in range(4)]))[1]["errors"])
        self.assertIn("too-many-links", self.check(card(links=[f"- [x{n}](rule-digest.md)" for n in range(6)]))[1]["errors"])
        five = [f"- R{n} [verified 2026-11-21] rule {n}. (evidence: {R1})" for n in range(1, 6)]
        self.assertNotIn("too-many-rules", self.check(card(rules=five))[1]["errors"])

    def test_rule_lines_have_a_status_a_date_and_an_evidence(self):
        for bad in (f"- R1 Donate. (evidence: {R1})", f"- R1 [verified] Donate. (evidence: {R1})", "- R1 [verified 2026-11-21] Donate.",
                    f"- Donate [verified 2026-11-21]. (evidence: {R1})", f"- R1 [probably 2026-11-21] Donate. (evidence: {R1})"):
            self.assertIn("rule-format", self.check(card(rules=[bad]))[1]["errors"], bad)

    def test_a_rule_cites_a_record_never_a_run_note_or_a_run_article(self):
        self.write("_run_notes_/alpha-one/run-20261101-1141.md", "x")
        self.write("_activities_/alpha-one/run-20261101-1141.md", "x")
        for evidence in ("_run_notes_/alpha-one/run-20261101-1141.md", "_activities_/alpha-one/run-20261101-1141.md",
                         "_activities_/alpha-one/rule-digest.md", f"{R1}, _run_notes_/alpha-one/run-20261101-1141.md"):
            c = self.check(card(rules=[f"- R1 [verified 2026-11-21] Donate. (evidence: {evidence})"]))[1]
            self.assertIn("evidence-not-a-record", c["errors"], evidence)
        self.assertNotIn("evidence-not-a-record", self.check(card(rules=[f"- R1 [verified 2026-11-21] Donate. (evidence: {R1}, {R2})"]))[1]["errors"])

    def test_a_superseded_rule_or_a_repeated_id_is_an_error(self):
        self.assertIn("rule-superseded-left", self.check(card(rules=[f"- R1 [superseded 2026-11-21] Old. (evidence: {R1})"]))[1]["errors"])
        twice = [f"- R1 [verified 2026-11-21] a. (evidence: {R1})", f"- R1 [verified 2026-11-21] b. (evidence: {R1})"]
        self.assertIn("rule-id-repeats", self.check(card(rules=twice))[1]["errors"])

    def test_every_open_question_has_its_test_and_the_numbers_line_cites_a_record(self):
        c = self.check(card(questions=["- Does it reset? test: read twice.", "- Is it capped?"]))[1]
        self.assertEqual(c["errors"].get("open-question-without-test"), 1)
        for numbers in (["42 donations."], [f"no digits here ({R1})."], [f"42 and {R1}.", "a second line 7."]):
            self.assertIn("numbers-line", self.check(card(numbers=numbers))[1]["errors"], numbers)


class Citations(Repo):
    def test_a_missing_path_and_a_missing_relative_link_are_unresolved(self):
        c = self.check(card(numbers=["42 donations (_records_/2026-11-21/alpha-one/9999-queue-run.md)."]))[1]
        self.assertIn("unresolved-path", c["errors"])
        c = self.check(card(links=["- [gone](missing-page.md)"]))[1]
        self.assertIn("unresolved-path", c["errors"])

    def test_a_moved_path_resolves_through_the_table_and_is_flagged_to_update(self):
        old = "_activities_/alpha-one/run-20261101-1141.md"
        new = "_run_notes_/alpha-one/run-20261101-1141.md"
        self.write(new, "moved")
        self.write("_run_notes_/moved-paths/moved-paths.csv", f"old_path,new_path,record\n{old},{new},{R1}\n")
        c = self.check(card(links=[f"- [the run]({old})"]))[1]
        self.assertEqual(c["errors"], {})
        self.assertEqual(c["warnings"], {"cites-moved-path": 1})
        self.assertEqual(c["counts"]["citations_moved"], 1)

    def test_a_table_row_whose_new_file_is_gone_is_still_unresolved(self):
        old = "_activities_/alpha-one/run-20261101-1141.md"
        self.write("_run_notes_/moved-paths/moved-paths.csv", f"old_path,new_path,record\n{old},_run_notes_/alpha-one/missing.md,{R1}\n")
        self.assertIn("unresolved-path", self.check(card(links=[f"- [the run]({old})"]))[1]["errors"])


class Stale(Repo):
    def rules(self, date):
        return [f"- R1 [unverified {date}] Donate. (evidence: {R1})"]

    def test_an_unverified_rule_older_than_fourteen_days_is_a_warning(self):
        r, c = self.check(card(rules=self.rules("2026-11-09")))                         # 14 days old: fine
        self.assertEqual(c["warnings"], {})
        r, c = self.check(card(rules=self.rules("2026-11-08")))                         # 15 days old
        self.assertEqual(c["warnings"], {"stale-unverified": 1})
        self.assertEqual(r.returncode, 0)                                                # a warning at commit time
        self.assertEqual(self.run_tool("--stale-fail", "check", "_activities_/alpha-one/INDEX.md").returncode, 1)

    def test_a_verified_rule_never_goes_stale_and_the_limit_is_a_flag(self):
        old = [f"- R1 [verified 2026-01-01] Donate. (evidence: {R1})"]
        self.assertEqual(self.check(card(rules=old))[1]["warnings"], {})
        self.write("_activities_/alpha-one/INDEX.md", card(rules=self.rules("2026-11-20")))
        r = self.run_tool("--format", "json", "--stale-days", "2", "check", "_activities_/alpha-one/INDEX.md")
        self.assertEqual(json.loads(r.stdout)["cards"][0]["warnings"], {"stale-unverified": 1})


class Changed(Repo):
    def test_a_staged_card_is_checked_and_a_link_list_is_skipped(self):
        self.write("_activities_/alpha-one/INDEX.md", card(failures=[f"- f{n} - fix" for n in range(4)]))
        self.write("_activities_/beta-two/INDEX.md", "---\ntitle: Beta\n---\n# Beta\n\n- [a](a.md)\n- [c](c.md)\n")
        self.git("add", "-A")
        r = self.run_tool("--format", "json", "changed", "--staged")
        data = json.loads(r.stdout)
        self.assertEqual(r.returncode, 1)
        self.assertEqual((data["checked"], data["skipped_not_cards"]), (1, 1))
        self.assertIn("too-many-failures", data["cards"][0]["errors"])

    def test_a_staged_good_card_passes_and_an_unstaged_edit_is_not_looked_at(self):
        self.write("_activities_/alpha-one/INDEX.md", card(numbers=[f"43 donations ({R1})."]))
        self.git("add", "-A")
        self.write("_activities_/alpha-one/INDEX.md", card(failures=[f"- f{n} - fix" for n in range(9)]))     # not staged
        r = self.run_tool("changed", "--staged")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_a_card_that_lost_its_shape_is_an_error(self):
        self.write("_activities_/alpha-one/INDEX.md", "---\ntitle: Alpha\n---\n# Alpha\n\n- [rules](rule-digest.md)\n")
        self.git("add", "-A")
        r = self.run_tool("--format", "json", "changed", "--staged")
        self.assertEqual(r.returncode, 1)
        self.assertEqual(json.loads(r.stdout)["cards"][0]["errors"], {"card-shape-lost": 1})

    def test_against_a_base_revision(self):
        self.write("_activities_/alpha-one/INDEX.md", card(drop=("Links",)))
        r = self.run_tool("--format", "json", "changed", "--base", "HEAD")
        self.assertEqual(r.returncode, 1)
        self.assertIn("missing-section", json.loads(r.stdout)["cards"][0]["errors"])

    def test_changed_needs_exactly_one_of_staged_or_base(self):
        self.assertEqual(self.run_tool("changed").returncode, 2)
        self.assertEqual(self.run_tool("changed", "--staged", "--base", "HEAD").returncode, 2)

    def test_files_outside_activity_index_pages_are_ignored(self):
        self.write("_activities_/alpha-one/rule-digest.md", "---\ntitle: d\n---\n## Route\n## Rules\n")
        self.write("_records_/x.md", "x")
        self.git("add", "-A")
        r = self.run_tool("--format", "json", "changed", "--staged")
        self.assertEqual((json.loads(r.stdout)["checked"], r.returncode), (0, 0))


class Daily(Repo):
    def test_counts_for_the_coach_and_the_verified_share(self):
        self.write("_activities_/gamma-three/rule-digest.md", "---\ntitle: digest\n---\nrules\n")
        self.write("_activities_/gamma-three/INDEX.md", card(rules=[f"- R1 [verified 2026-11-22] a. (evidence: {R1})",
                                                                  f"- R2 [verified 2026-11-22] b. (evidence: {R2})"]))
        r = self.run_tool("--format", "json", "daily")
        data = json.loads(r.stdout)
        self.assertEqual(r.returncode, 0, r.stdout)
        self.assertEqual((data["checked"], data["skipped_not_cards"], data["failing"]), (2, 1, 0))
        self.assertEqual((data["totals"]["rules_total"], data["totals"]["rules_verified"]), (4, 3))
        self.assertEqual(data["verified_share_percent"], 75.0)
        self.assertEqual({c["activity"] for c in data["cards"]}, {"alpha-one", "gamma-three"})

    def test_a_failing_card_or_a_stale_rule_makes_the_daily_run_exit_one(self):
        self.write("_activities_/alpha-one/INDEX.md", card(drop=("Numbers",)))
        self.assertEqual(self.run_tool("daily").returncode, 1)
        self.write("_activities_/alpha-one/INDEX.md", card(rules=[f"- R1 [unverified 2026-10-01] Donate. (evidence: {R1})"]))
        r = self.run_tool("daily")
        self.assertEqual(r.returncode, 1)                                               # stale alarms in the daily run only
        self.assertEqual(self.run_tool("check", "_activities_/alpha-one/INDEX.md").returncode, 0)

    def test_the_text_output_names_the_activity_and_codes_and_never_a_card_text(self):
        self.write("_activities_/alpha-one/INDEX.md", card(failures=[f"- f{n} - fix" for n in range(4)]))
        r = self.run_tool("daily")
        self.assertIn("alpha-one: too-many-failures 1", r.stdout)
        for text in (SECRET, "Donate every", "42 donations", "button is grey"):
            self.assertNotIn(text, r.stdout + r.stderr)
        self.assertIn("rules: 2 (verified 1, unverified 1, verified share 50.0%", r.stdout)

    def test_it_writes_nothing(self):
        before = {p.relative_to(self.root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(self.root.rglob("*")) if p.is_file()}
        for args in (("daily",), ("check", "_activities_/alpha-one/INDEX.md"), ("changed", "--base", "HEAD")):
            self.run_tool(*args)
        after = {p.relative_to(self.root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(self.root.rglob("*")) if p.is_file()}
        self.assertEqual(after, before)

    def test_bad_input_is_exit_two(self):
        self.assertEqual(self.run_tool("daily", now="soon").returncode, 2)
        outside = Path(tempfile.mkdtemp(prefix="outside-"))
        self.addCleanup(shutil.rmtree, outside, True)
        (outside / "c.md").write_text(card())
        self.assertEqual(self.run_tool("check", str(outside / "c.md")).returncode, 2)


class Template(unittest.TestCase):
    def test_the_template_is_a_card_the_checker_understands(self):
        text = (HERE / "card-template.md").read_text()
        block = text.split("```\n")[1]
        sys.path.insert(0, str(HERE))
        import playbook_check
        self.assertTrue(playbook_check.is_card(block))
        self.assertEqual([h for h, _l in playbook_check.sections_of(block)], list(playbook_check.SECTIONS))
        self.assertLessEqual(playbook_check.body_words(text), 300)


if __name__ == "__main__":
    unittest.main()
