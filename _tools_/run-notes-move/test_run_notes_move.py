"""Tests for run_notes_move.py on a throwaway git repository shaped like the real tree: activities with run articles of class a, b
and c, a rule digest, catalogs that link to the run articles, dated records, and pages outside _activities_ that cite old paths.

Run: python3 -m unittest discover -s _tools_/run-notes-move
"""
from __future__ import annotations

import csv
import hashlib
import importlib.util
import io
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOOL = HERE / "run_notes_move.py"
NOW = "2026-11-23T10:00:00Z"
spec = importlib.util.spec_from_file_location("rnm", TOOL)
rnm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rnm)
NOW_DT = rnm.parse_now(NOW)
AUDIT = "_records_/2026-11-22/coach/run-articles-audit.csv"


def article(stem: str, words: int = 40, version: str = "0.1.0", extra: str = "") -> str:
    body = " ".join(f"w{i}" for i in range(words))
    return (f"---\ntitle: What the {stem} unit added\ncreated: 2026-11-23T06:11:49Z\nmodified: 2026-11-23T06:11:49Z\nversion: {version}\n"
            f"sequence: 62\ndescription: First words of the {stem} article\n{extra}---\n## What the {stem} unit added\n\n"
            f"- Recommended tech {stem} was entered from the menu. Then a second sentence follows here.\n  {body}\n")


def doc(title: str, body: str, version: str = "1.0.0", changelog: bool = False) -> str:
    text = f"---\ntitle: {title}\ncreated: 2026-11-23T05:00:00Z\nmodified: 2026-11-23T05:00:00Z\nversion: {version}\ndescription: {title}\n---\n\n{body}\n"
    return text + ("\n## Changelog\n\n- 1.0.0, 2026-11-23 - First.\n" if changelog else "")


class Tree(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp(prefix="run-notes-"))
        self.addCleanup(shutil.rmtree, self.root, True)
        subprocess.run(["git", "init", "-q", "-b", "main", str(self.root)], check=True)
        self.audit_rows = []
        for act, stems in (("alpha-one", ["20261101-1141", "20261101-1619", "20261102-0100", "20261103-0100"]),
                           ("beta-two", ["20261101-0900"]), ("gamma-three", ["20261104-0100"])):
            self.write(f"_activities_/{act}/rule-digest.md", doc(f"{act} digest", "The standing rules."))
            links = []
            for stem in stems:
                self.write(f"_activities_/{act}/run-{stem}.md", article(stem))
                links.append(f"- [run {stem}](run-{stem}.md) - run")
            self.write(f"_activities_/{act}/catalog-01.md", doc(f"{act} catalog", "\n".join(links), changelog=True))
            self.write(f"_activities_/{act}/INDEX.md", doc(f"{act} index", f"See the [first run](run-{stems[0]}.md).\n\n- [digest](rule-digest.md)"))
        classes = {"20261102-0100": "b", "20261103-0100": "c"}
        for act, stems in (("alpha-one", ["20261101-1141", "20261101-1619", "20261102-0100", "20261103-0100"]),
                           ("beta-two", ["20261101-0900"]), ("gamma-three", ["20261104-0100"])):
            for stem in stems:
                record = f"_records_/{stem[:4]}-{stem[4:6]}-{stem[6:8]}/{act}/{stem[9:]}-queue-run.md".replace("_records_/2026", "_records_/2026-").replace("--", "-")
                record = f"_records_/2026-{stem[4:6]}-{stem[6:8]}/{act}/{stem[9:]}-queue-run.md"
                self.write(record, doc("record", "Measured values 1,450 and 2,750."))
                self.audit_rows.append({"path": f"_activities_/{act}/run-{stem}.md", "activity": act, "words": "60", "mapped_record_path": record,
                                        "shared_number_share": "0.9", "class": classes.get(stem, "a"), "reason": "test"})
        self.write("_records_/2026-11-10/team-operations/0900-note.md", doc("note", "Cites _activities_/alpha-one/run-20261101-1141.md by path."))
        self.write("_knowledge_/topic/page.md", doc("page", "See _activities_/beta-two/run-20261101-0900.md for the first read."))
        self.write_audit()
        self.commit("base")

    def write(self, rel, text):
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)

    def write_audit(self):
        buf = io.StringIO()
        w = csv.DictWriter(buf, fieldnames=["path", "activity", "words", "mapped_record_path", "shared_number_share", "class", "reason"], lineterminator="\n")
        w.writeheader()
        w.writerows(self.audit_rows)
        self.write(AUDIT, buf.getvalue())

    def commit(self, message):
        subprocess.run(["git", "-C", str(self.root), "add", "-A"], check=True)
        subprocess.run(["git", "-C", str(self.root), "-c", "user.email=t@e.org", "-c", "user.name=t", "commit", "-q", "-m", message], check=True)

    def run_tool(self, *args):
        return subprocess.run([sys.executable, "-B", str(TOOL), "--root", str(self.root), "--now", NOW, *args], capture_output=True, text=True)

    def read(self, rel):
        return (self.root / rel).read_text()

    def exists(self, rel):
        return (self.root / rel).exists()

    def digest_of(self, skip=()):
        h = {}
        for p in sorted(self.root.rglob("*")):
            rel = p.relative_to(self.root).as_posix()
            if p.is_file() and not rel.startswith(".git/") and not any(rel.startswith(s) for s in skip):
                h[rel] = hashlib.sha256(p.read_bytes()).hexdigest()
        return h

    def apply(self, *acts, reviewed=None):
        return self.run_tool("apply", "--activities", ",".join(acts), "--reviewed", ",".join(reviewed if reviewed is not None else acts))


class Plan(Tree):
    def test_the_dry_run_writes_nothing_and_reports_counts(self):
        before = self.digest_of()
        r = self.run_tool("plan")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertEqual(self.digest_of(), before)
        self.assertEqual(subprocess.run(["git", "-C", str(self.root), "status", "--short"], capture_output=True, text=True).stdout, "")
        self.assertRegex(r.stdout, r"alpha-one\s+2\s+\d+\s+2\s+0\s+0")                      # class a only: 2 of the 4 alpha files
        self.assertIn("UNREVIEWED", r.stdout)
        self.assertIn("references outside _activities_", r.stdout)
        self.assertIn("_knowledge_ 1", r.stdout)
        self.assertIn("_records_ 2", r.stdout)                                                # the note and the audit CSV itself
        self.assertIn("dangling links in _activities_ now: 0", r.stdout)

    def test_the_sample_diff_shows_only_the_marked_lines_and_never_a_body(self):
        r = self.run_tool("plan", "--sample", "1")
        self.assertIn("+status: superseded", r.stdout)
        self.assertIn("+superseded_by: _records_/", r.stdout)
        self.assertIn("-version: 0.1.0", r.stdout)
        self.assertIn("+version: 0.2.0", r.stdout)
        self.assertIn("## Changelog", r.stdout)
        self.assertNotIn("Recommended tech", r.stdout)
        self.assertNotIn("w39", r.stdout)

    def test_json_and_the_reviewed_flag(self):
        r = self.run_tool("plan", "--format", "json", "--reviewed", "alpha-one")
        import json
        data = json.loads(r.stdout)
        reviewed = {a["activity"]: a["digest_reviewed"] for a in data["activities"]}
        self.assertEqual(reviewed, {"alpha-one": True, "beta-two": False, "gamma-three": False})
        self.assertEqual(data["total"]["to_move"], 4)


class Apply(Tree):
    def test_an_unreviewed_digest_refuses_the_whole_activity_and_writes_nothing(self):
        before = self.digest_of()
        r = self.run_tool("apply", "--activities", "alpha-one")
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("NOT APPLIED", r.stdout)
        self.assertEqual(self.digest_of(), before)
        self.assertFalse(self.exists("_run_notes_"))

    def test_apply_needs_a_named_block_of_at_most_three(self):
        self.assertNotEqual(self.run_tool("apply", "--reviewed", "alpha-one").returncode, 0)
        self.assertNotEqual(self.run_tool("apply", "--activities", "all", "--reviewed", "alpha-one").returncode, 0)
        r = self.run_tool("--audit", AUDIT, "apply", "--activities", "alpha-one,beta-two,gamma-three", "--block-limit", "2", "--reviewed", "alpha-one,beta-two,gamma-three")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("limit is 2", r.stderr)
        self.assertFalse(self.exists("_run_notes_"))

    def test_class_a_moves_marked_and_class_b_and_c_stay(self):
        r = self.apply("alpha-one")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        for stem in ("20261101-1141", "20261101-1619"):
            self.assertFalse(self.exists(f"_activities_/alpha-one/run-{stem}.md"))
            self.assertTrue(self.exists(f"_run_notes_/alpha-one/run-{stem}.md"))
        for stem in ("20261102-0100", "20261103-0100"):                                 # class b and c stay
            self.assertTrue(self.exists(f"_activities_/alpha-one/run-{stem}.md"))
            self.assertFalse(self.exists(f"_run_notes_/alpha-one/run-{stem}.md"))
        self.assertTrue(self.exists("_activities_/beta-two/run-20261101-0900.md"))     # another activity: not in this block
        git_status = subprocess.run(["git", "-C", str(self.root), "status", "--short"], capture_output=True, text=True).stdout
        self.assertIn("R  _activities_/alpha-one/run-20261101-1141.md -> _run_notes_/alpha-one/run-20261101-1141.md", git_status)

    def test_each_moved_file_equals_its_original_apart_from_the_marked_frontmatter_and_one_changelog_line(self):
        original = {s: self.read(f"_activities_/alpha-one/run-{s}.md") for s in ("20261101-1141", "20261101-1619")}
        self.apply("alpha-one")
        for stem, old in original.items():
            new = self.read(f"_run_notes_/alpha-one/run-{stem}.md")
            record = f"_records_/2026-11-01/alpha-one/{stem[9:]}-queue-run.md"
            self.assertEqual(rnm.verify_pair(old, new, record, "alpha-one"), [])
            self.assertTrue(new.split("\n---\n", 1)[1].startswith(old.split("\n---\n", 1)[1]))      # the body is a byte-exact prefix
            front = new.split("\n---\n", 1)[0]
            self.assertIn("status: superseded", front)
            self.assertIn(f"superseded_by: {record}", front)
            self.assertIn("version: 0.2.0", front)
            self.assertIn("created: 2026-11-23T06:11:49Z", front)
            self.assertIn("modified: 2026-11-23T10:00:00Z", front)
            self.assertEqual(new.count("## Changelog"), 1)
        v = self.run_tool("verify", "--base", "HEAD")
        self.assertEqual(v.returncode, 0, v.stdout + v.stderr)
        self.assertIn("2 files equal their original", v.stdout)

    def test_the_table_the_type_index_and_the_catalogs(self):
        self.apply("alpha-one")
        with open(self.root / "_run_notes_/moved-paths/moved-paths.csv", newline="") as handle:
            rows = list(csv.DictReader(handle))
        self.assertEqual([r["old_path"] for r in rows], ["_activities_/alpha-one/run-20261101-1141.md", "_activities_/alpha-one/run-20261101-1619.md"])
        self.assertEqual(rows[0]["new_path"], "_run_notes_/alpha-one/run-20261101-1141.md")
        self.assertEqual(rows[0]["record"], "_records_/2026-11-01/alpha-one/1141-queue-run.md")
        children = sorted(p.name for p in (self.root / "_run_notes_").iterdir())
        self.assertEqual(children, ["INDEX.md", "alpha-one", "moved-paths"])               # only an INDEX and instance folders
        self.assertIn("[alpha-one](alpha-one/INDEX.md)", self.read("_run_notes_/INDEX.md"))
        index = self.read("_run_notes_/alpha-one/INDEX.md")
        self.assertLessEqual(rnm.body_words(index), 300)
        self.assertIn("(catalog-01.md)", index)
        catalog = self.read("_run_notes_/alpha-one/catalog-01.md")
        self.assertIn("[run-20261101-1141](run-20261101-1141.md) - Recommended tech 20261101-1141 was entered from the menu.", catalog)
        self.assertNotIn("second sentence", catalog)                                         # one first sentence, no body copied
        self.assertIn("moved paths table", index)

    def test_references_in_activities_are_rewritten_and_nothing_dangles(self):
        self.apply("alpha-one")
        catalog = self.read("_activities_/alpha-one/catalog-01.md")
        self.assertIn("](../../_run_notes_/alpha-one/run-20261101-1141.md)", catalog)
        self.assertIn("](run-20261102-0100.md)", catalog)                                    # class b stays where it is
        self.assertIn("](../../_run_notes_/alpha-one/run-20261101-1619.md)", catalog)
        self.assertIn("[first run](../../_run_notes_/alpha-one/run-20261101-1141.md)", self.read("_activities_/alpha-one/INDEX.md"))
        self.assertEqual(rnm.dangling_links(self.root), 0)
        self.assertIn("version: 1.1.0", catalog)                                              # an edited page moves its version
        self.assertIn("- 1.1.0, 2026-11-23 - Links to run notes that moved", catalog)        # and its changelog, which it has
        self.assertNotIn("Changelog", self.read("_activities_/alpha-one/INDEX.md"))          # a page with none gets none
        self.assertIn("version: 1.1.0", self.read("_activities_/alpha-one/INDEX.md"))

    def test_nothing_outside_activities_and_run_notes_is_ever_touched(self):
        before = self.digest_of(skip=("_activities_/", "_run_notes_/"))
        self.apply("alpha-one", "beta-two")
        self.assertEqual(self.digest_of(skip=("_activities_/", "_run_notes_/")), before)
        self.assertIn("run-20261101-1141.md", self.read("_records_/2026-11-10/team-operations/0900-note.md"))   # the record still cites the old path
        with self.assertRaises(SystemExit):
            rnm.write_safe(self.root, "_records_/2026-11-01/alpha-one/1141-queue-run.md", "x")
        with self.assertRaises(SystemExit):
            rnm.write_safe(self.root, "_activities_/../_records_/x.md", "x")

    def test_it_is_idempotent_and_a_second_run_changes_nothing(self):
        self.apply("alpha-one")
        after_first = self.digest_of()
        r = self.apply("alpha-one")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("moved 0, already done 2", r.stdout)
        self.assertEqual(self.digest_of(), after_first)

    def test_a_run_that_stopped_after_marking_resumes_without_a_second_bump(self):
        path = "_activities_/alpha-one/run-20261101-1141.md"
        record = "_records_/2026-11-01/alpha-one/1141-queue-run.md"
        original = self.read(path)
        marked = rnm.mark_text(original, record, "alpha-one", NOW_DT)
        self.write(path, marked)                                                              # marked in place, never moved
        r = self.apply("alpha-one")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        new = self.read("_run_notes_/alpha-one/run-20261101-1141.md")
        self.assertEqual(new, marked)
        self.assertEqual(new.count("## Changelog"), 1)
        self.assertIn("version: 0.2.0", new)

    def test_a_page_that_has_to_change_keeps_its_created_and_moves_its_version(self):
        self.apply("alpha-one")
        before = self.read("_run_notes_/alpha-one/catalog-01.md")
        self.write("_activities_/alpha-one/run-20261105-0100.md", article("20261105-0100"))
        record = "_records_/2026-11-05/alpha-one/0100-queue-run.md"
        self.write(record, doc("record", "Measured 1,450."))
        self.audit_rows.append({"path": "_activities_/alpha-one/run-20261105-0100.md", "activity": "alpha-one", "words": "60",
                                "mapped_record_path": record, "shared_number_share": "0.9", "class": "a", "reason": "test"})
        self.write_audit()
        self.apply("alpha-one")
        after = self.read("_run_notes_/alpha-one/catalog-01.md")
        self.assertIn("run-20261105-0100", after)
        self.assertNotIn("run-20261105-0100", before)
        self.assertEqual(re.search(r"created: (\S+)", before).group(1), re.search(r"created: (\S+)", after).group(1))
        self.assertIn("version: 1.1.0", after)
        self.assertIn("(run-20261101-1141.md)", after)                                   # the earlier entries are still there

    def test_a_block_of_two_activities_and_the_second_block_adds_to_the_table(self):
        self.apply("alpha-one")
        self.apply("beta-two")
        with open(self.root / "_run_notes_/moved-paths/moved-paths.csv", newline="") as handle:
            self.assertEqual(len(list(csv.DictReader(handle))), 3)
        self.assertIn("[beta-two](beta-two/INDEX.md)", self.read("_run_notes_/INDEX.md"))
        self.assertIn("[alpha-one](alpha-one/INDEX.md)", self.read("_run_notes_/INDEX.md"))
        self.assertIn("3 rows", self.read("_run_notes_/moved-paths/INDEX.md"))


class Refusals(Tree):
    def entry(self, **row_changes):
        row = dict(self.audit_rows[0], words=60, record=self.audit_rows[0]["mapped_record_path"], cls="a", share="0.9")
        row.update(row_changes)
        return rnm.evaluate_row(self.root, row, NOW_DT, {"alpha-one"})

    def test_a_file_whose_class_is_not_a_is_refused(self):
        self.assertEqual(self.entry(cls="b")["reason"], "class")
        self.assertEqual(self.entry(cls="c")["state"], "refuse")

    def test_a_missing_record_is_refused_and_the_file_is_left_alone(self):
        (self.root / self.audit_rows[0]["mapped_record_path"]).unlink()
        e = self.entry()
        self.assertEqual((e["state"], e["reason"]), ("refuse", "record-missing"))
        r = self.apply("alpha-one")
        self.assertEqual(r.returncode, 1)
        self.assertTrue(self.exists("_activities_/alpha-one/run-20261101-1141.md"))
        self.assertTrue(self.exists("_run_notes_/alpha-one/run-20261101-1619.md"))           # the other one still moved

    def test_a_record_path_outside_records_is_refused(self):
        self.assertEqual(self.entry(record="_activities_/alpha-one/rule-digest.md")["reason"], "record-missing")

    def test_an_activity_without_a_reviewed_digest_or_without_a_digest_is_refused(self):
        row = dict(self.audit_rows[0], words=60, record=self.audit_rows[0]["mapped_record_path"], cls="a", share="0.9")
        self.assertEqual(rnm.evaluate_row(self.root, row, NOW_DT, {"beta-two"})["reason"], "digest-unreviewed")
        (self.root / "_activities_/alpha-one/rule-digest.md").unlink()
        self.assertEqual(rnm.evaluate_row(self.root, row, NOW_DT, {"alpha-one"})["reason"], "digest-unreviewed")

    def test_a_path_that_is_not_directly_in_its_activity_folder_is_refused(self):
        self.assertEqual(self.entry(path="_activities_/alpha-one/sub/run-20261101-1141.md")["reason"], "outside-activity-folder")
        self.assertEqual(self.entry(activity="beta-two")["reason"], "outside-activity-folder")

    def test_a_missing_source_and_a_conflicting_target_are_refused(self):
        self.write("_run_notes_/alpha-one/run-20261101-1141.md", "---\ntitle: x\n---\nsomething else\n")
        self.assertEqual(self.entry()["reason"], "target-conflict")                           # both exist
        (self.root / "_activities_/alpha-one/run-20261101-1141.md").unlink()
        self.assertEqual(self.entry()["reason"], "target-conflict")                           # target there, not marked
        (self.root / "_run_notes_/alpha-one/run-20261101-1141.md").unlink()
        self.assertEqual(self.entry()["reason"], "source-missing")

    def test_a_file_without_version_or_frontmatter_is_refused(self):
        self.write("_activities_/alpha-one/run-20261101-1141.md", "---\ntitle: x\ncreated: 2026-11-23T06:11:49Z\n---\nbody\n")
        self.assertEqual(self.entry()["reason"], "frontmatter-incomplete")
        self.write("_activities_/alpha-one/run-20261101-1141.md", "no frontmatter at all\n")
        self.assertEqual(self.entry()["reason"], "no-frontmatter")

    def test_a_file_that_would_reach_the_word_limit_with_its_changelog_is_refused(self):
        self.write("_activities_/alpha-one/run-20261101-1141.md", article("20261101-1141", words=489))
        self.assertEqual(self.entry()["reason"], "word-budget")
        self.write("_activities_/alpha-one/run-20261101-1141.md", article("20261101-1141", words=440))
        self.assertEqual(self.entry()["state"], "move")

    def test_a_file_that_fails_its_proof_is_put_back_and_not_moved(self):
        original = self.read("_activities_/alpha-one/run-20261101-1141.md")
        real = rnm.mark_text
        rnm.mark_text = lambda text, record, activity, now: real(text, record, activity, now).replace("w1 ", "CHANGED ", 1)
        self.addCleanup(setattr, rnm, "mark_text", real)
        a = type("A", (), {"sentence_words": 12})()
        report = rnm.apply_activity(a, self.root, rnm.read_audit(self.root / AUDIT), "alpha-one", NOW_DT, {"alpha-one"})
        self.assertEqual(report["proof_failures"], 2)
        self.assertEqual(report["moved"], 0)
        self.assertEqual(self.read("_activities_/alpha-one/run-20261101-1141.md"), original)
        self.assertFalse(self.exists("_run_notes_/alpha-one/run-20261101-1141.md"))


class Verify(Tree):
    def test_verify_catches_a_changed_body_and_a_missing_file(self):
        self.apply("alpha-one")
        path = self.root / "_run_notes_/alpha-one/run-20261101-1141.md"
        path.write_text(path.read_text().replace("w1 ", "TAMPERED ", 1))
        v = self.run_tool("verify", "--base", "HEAD")
        self.assertEqual(v.returncode, 1)
        self.assertIn("1 differ", v.stdout)
        (self.root / "_run_notes_/alpha-one/run-20261101-1619.md").unlink()
        self.assertIn("1 could not be compared", self.run_tool("verify").stdout)


class Catalogs(unittest.TestCase):
    def test_a_big_activity_is_split_under_the_word_budget_with_every_file_listed_once(self):
        entries = [(f"run-20261101-{n:04d}.md", "Recommended tech was entered from the menu and then a read followed") for n in range(227)]
        pages = rnm.build_pages("alliance-donations", entries, NOW_DT)
        catalogs = {k: v for k, v in pages.items() if k != "INDEX.md"}
        self.assertGreater(len(catalogs), 5)
        for name, text in catalogs.items():
            self.assertLessEqual(rnm.body_words(text), 300, name)
        listed = re.findall(r"\]\((run-\d{8}-\d{4}\.md)\)", "".join(catalogs.values()))
        self.assertEqual(sorted(listed), sorted(n for n, _ in entries))
        self.assertLessEqual(rnm.body_words(pages["INDEX.md"]), 300)
        for name in catalogs:
            self.assertIn(f"({name})", pages["INDEX.md"])

    def test_first_sentence(self):
        body = "## Heading\n\n- Recommended tech is Rallied HP 5 of 10 | marked with\n  the badge. Second sentence here.\n"
        self.assertEqual(rnm.first_sentence(body, 40), "Recommended tech is Rallied HP 5 of 10 / marked with the badge.")
        self.assertEqual(rnm.first_sentence(body, 4), "Recommended tech is Rallied")
        self.assertEqual(rnm.first_sentence(body, 0), "")
        self.assertEqual(rnm.first_sentence("## Only a heading\n", 10), "")

    def test_version_bumps(self):
        self.assertEqual(rnm.bump_minor("0.1.0"), "0.2.0")
        self.assertEqual(rnm.bump_minor("1.9.3"), "1.10.0")
        with self.assertRaises(rnm.Refusal):
            rnm.bump_minor("v2")

    def test_an_existing_status_is_replaced_in_place_and_other_lines_stay(self):
        text = article("20261101-1141", extra="status: unverified\nsuperseded_by: old\n")
        marked = rnm.mark_text(text, "_records_/2026-11-01/a/1-queue-run.md", "alpha-one", NOW_DT)
        front = marked.split("\n---\n", 1)[0]
        self.assertEqual(front.count("status:"), 1)
        self.assertIn("status: superseded", front)
        self.assertIn("superseded_by: _records_/2026-11-01/a/1-queue-run.md", front)
        self.assertEqual(rnm.verify_pair(text, marked, "_records_/2026-11-01/a/1-queue-run.md", "alpha-one"), [])


if __name__ == "__main__":
    unittest.main()
