"""Tests for split_doc.py on fixture documents in temporary folders; they never touch a live repository.

Run: python3 -m unittest discover -s _tools_/split-doc
They need the reflection checkout (word counter) and skip without it.
"""
from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOOL = HERE / "split_doc.py"
REFLECTION = Path(os.environ.get("LINT_GATE_REFLECTION", "~/dtadpole/reflection")).expanduser()
COUNTER = REFLECTION / "_tools_/document-word-budget/word-budget.py"
NAME = re.compile(r"^[a-z0-9]+(-[a-z0-9]+){1,3}$")

FRONT = "---\ntitle: Sample register\ncreated: 2026-11-01T00:00:00Z\nmodified: 2026-11-02T00:00:00Z\nversion: 1.2.3\ndescription: A sample register for the tests\nstatus: active\n---\n"


def para(n: int, tag: str = "w") -> str:
    return " ".join(f"{tag}{i}" for i in range(n)) + ".\n"


def sections(count: int, words: int, level: str = "##") -> str:
    return "".join(f"\n{level} Section {i}\n\n{para(words, f's{i}x')}" for i in range(count))


@unittest.skipUnless(COUNTER.is_file(), "reflection checkout not found")
class SplitCase(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="split-doc-test-"))
        self.addCleanup(shutil.rmtree, self.tmp, True)
        spec = __import__("importlib.util").util.spec_from_file_location("split_doc_under_test", TOOL)
        self.sd = __import__("importlib.util").util.module_from_spec(spec)
        sys.modules["split_doc_under_test"] = self.sd
        spec.loader.exec_module(self.sd)
        self.counter = self.sd.Counter(self.sd.load_counter(None))

    def doc(self, name: str, text: str) -> Path:
        path = self.tmp / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(text.encode())
        return path

    def run_tool(self, *args):
        return subprocess.run([sys.executable, "-B", str(TOOL), *map(str, args)], capture_output=True, text=True)

    def plan(self, text: str):
        return self.sd.build(text, "sample", self.counter, "2026-11-23T06:00:00Z")

    def assert_sound(self, plan):
        self.assertEqual(self.sd.verify(plan, self.counter), [])
        for name, text in plan.files:
            self.assertLessEqual(self.counter.file_words(text), 300 if name == "INDEX.md" else 450, name)
            if name != "INDEX.md":
                self.assertRegex(name[:-3], NAME)


class Splitting(SplitCase):
    def test_sections_split_at_headings_and_rebuild_the_body_exactly(self):
        text = FRONT + "\n# Sample register\n\nIntro line.\n" + sections(6, 150) + sections(3, 90, "###")
        plan = self.plan(text)
        self.assert_sound(plan)
        self.assertGreater(len(plan.articles), 3)
        self.assertEqual("".join(self.sd.split_frontmatter(t)[1] for n, t in plan.files if n in plan.articles), plan.body)
        for name, t in plan.files:
            if name in plan.articles:
                body = self.sd.split_frontmatter(t)[1]
                self.assertTrue(body.lstrip().startswith("#") or "continued" in t.split("---")[1] or name.startswith("001"))

    def test_a_document_within_the_limit_is_one_article(self):
        plan = self.plan(FRONT + "\n# Small\n\n" + para(200))
        self.assertEqual(len(plan.articles), 1)
        self.assert_sound(plan)

    def test_a_large_section_splits_at_paragraphs(self):
        body = "\n## Big\n\n" + "\n".join(para(120, f"p{i}x") for i in range(12))
        plan = self.plan(FRONT + body)
        self.assertGreater(len(plan.articles), 2)
        self.assert_sound(plan)
        for name in plan.articles:   # cut at paragraph boundaries: every article ends with a full paragraph
            self.assertTrue(self.sd.split_frontmatter(dict(plan.files)[name])[1].rstrip().endswith("."))

    def test_long_list_and_table_split_at_items_and_rows_verbatim(self):
        items = "".join(f"- item {i} " + " ".join(f"t{i}x{j}" for j in range(20)) + "\n" for i in range(80))
        rows = "| a | b |\n|---|---|\n" + "".join(f"| row {i} {'x ' * 25} | v{i} |\n" for i in range(60))
        plan = self.plan(FRONT + "\n## List\n\n" + items + "\n## Table\n\n" + rows)
        self.assert_sound(plan)
        bodies = [self.sd.split_frontmatter(dict(plan.files)[n])[1] for n in plan.articles]
        for b in bodies:
            for line in b.splitlines():
                if line.startswith("- item"):
                    self.assertRegex(line, r"^- item \d+ t\d+x0 ")   # an item is never cut inside

    def test_one_giant_paragraph_is_cut_at_sentences_then_words(self):
        giant = " ".join(("word%d " % i) * 8 + "ends here." for i in range(120)) + "\n"
        plan = self.plan(FRONT + "\n## Giant\n\n" + giant)
        self.assert_sound(plan)
        self.assertGreater(len(plan.articles), 2)

    def test_fenced_code_keeps_fake_headings_and_blank_lines_together(self):
        fence = "```\n## not a heading\n\nstill code\n```\n"
        plan = self.plan(FRONT + "\n## Real\n\n" + para(60) + "\n" + fence + "\n" + sections(2, 300))
        self.assert_sound(plan)
        owners = [n for n in plan.articles if "## not a heading" in dict(plan.files)[n]]
        self.assertEqual(len(owners), 1)
        self.assertIn("still code\n```", dict(plan.files)[owners[0]])

    def test_crlf_and_missing_final_newline_are_preserved_byte_for_byte(self):
        text = (FRONT + "\n## One\n\n" + para(200) + "\n## Two\n\n" + para(300)).replace("\n", "\r\n").rstrip("\r\n")
        path = self.doc("crlf.md", text)
        self.assertEqual(self.run_tool(path, "--apply").returncode, 0)
        out = self.tmp / "crlf"
        joined = b"".join(self.sd.split_frontmatter((out / n).read_bytes().decode())[1].encode()
                          for n in sorted(os.listdir(out)) if self.sd.ARTICLE_FILE.match(n))
        self.assertEqual(joined, self.sd.split_frontmatter(text)[1].encode())

    def test_frontmatter_of_the_index_is_kept_with_version_and_modified_bumped(self):
        plan = self.plan(FRONT + "\n# Sample register\n" + sections(4, 200))
        index = dict(plan.files)["INDEX.md"]
        front = self.sd.split_frontmatter(index)[0]
        for line in ("title: Sample register", "created: 2026-11-01T00:00:00Z", "status: active",
                     "description: A sample register for the tests", "version: 1.3.0", "modified: 2026-11-23T06:00:00Z"):
            self.assertIn(line + "\n", front)
        art = self.sd.split_frontmatter(dict(plan.files)[plan.articles[0]])[0]
        self.assertIn("version: 0.1.0\n", art)
        self.assertNotIn("grounded_in", art)

    def test_a_document_without_frontmatter_gets_one_on_the_index(self):
        plan = self.plan("# Plain\n\n" + para(100) + sections(3, 200))
        front = self.sd.split_frontmatter(dict(plan.files)["INDEX.md"])[0]
        self.assertIn("version: 0.1.0", front)
        self.assert_sound(plan)

    def test_odd_headings_still_give_valid_file_names(self):
        odd = "\n## ???\n\n" + para(300, "a") + "\n## Ünïcode: heading, with #hash and `code`\n\n" + para(300, "b") + "\n##  \n\n" + para(300, "c")
        plan = self.plan(FRONT + odd)
        self.assert_sound(plan)
        titles = [self.sd.field(self.sd.split_frontmatter(dict(plan.files)[n])[0], "title") for n in plan.articles]
        for t in titles:
            self.assertNotIn(":", t)


class Index(SplitCase):
    def test_many_articles_get_catalog_pages_and_every_article_is_reachable(self):
        text = FRONT + "\n# Big\n" + sections(120, 300)
        plan = self.plan(text)
        self.assert_sound(plan)
        pages = [n for n, _ in plan.files if n not in plan.articles and n != "INDEX.md"]
        self.assertTrue(pages)
        self.assertRegex(pages[0], r"^catalog-\d\d\.md$")
        linked = set()
        for n, t in plan.files:
            if n not in plan.articles:
                linked |= set(re.findall(r"\]\(([^)]+\.md)\)", self.sd.split_frontmatter(t)[1]))
        self.assertTrue(set(plan.articles) <= linked)
        self.assertTrue(set(pages) <= linked)

    def test_a_small_split_lists_each_article_with_its_first_sentence_in_the_index(self):
        plan = self.plan(FRONT + "\n# S\n\n" + "".join(f"\n## Part {i}\n\nFirst sentence of part {i}. More text here.\n\n" + para(250) for i in range(4)))
        index = self.sd.split_frontmatter(dict(plan.files)["INDEX.md"])[1]
        for i in range(4):
            self.assertIn(f"First sentence of part {i}", index)
        self.assertEqual(index.count("\n- ["), len(plan.articles))
        self.assertEqual([n for n, _ in plan.files if n not in plan.articles], ["INDEX.md"])


class Running(SplitCase):
    def test_dry_run_is_the_default_and_writes_nothing(self):
        path = self.doc("reg/register.md", FRONT + sections(5, 200))
        before = sorted(p.name for p in self.tmp.rglob("*"))
        r = self.run_tool(path)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("dry run", r.stdout)
        self.assertEqual(sorted(p.name for p in self.tmp.rglob("*")), before)

    def test_verify_flag_reports_the_byte_for_byte_proof(self):
        path = self.doc("register.md", FRONT + sections(5, 200))
        r = self.run_tool(path, "--verify")
        self.assertIn("verify: PASS, article bodies rebuild the original body byte for byte", r.stdout)
        self.assertIn("not run", self.run_tool(path).stdout)

    def test_apply_turns_the_single_file_into_a_folder_and_removes_the_original(self):
        text = FRONT + sections(6, 200)
        path = self.doc("reg/register.md", text)
        r = self.run_tool(path, "--apply")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertFalse(path.exists())
        folder = self.tmp / "reg/register"
        self.assertTrue((folder / "INDEX.md").is_file())
        self.assertGreater(len(list(folder.glob("0*.md"))), 2)
        self.assertEqual([p.name for p in (self.tmp / "reg").iterdir()], ["register"])   # no staging folder left behind
        original = self.doc("original.md", text)
        self.assertEqual(self.run_tool("--check", folder, original).returncode, 0)

    def test_check_detects_a_tampered_article(self):
        text = FRONT + sections(6, 200)
        path = self.doc("register.md", text)
        original = self.doc("copy.md", text)
        self.run_tool(path, "--apply")
        folder = self.tmp / "register"
        victim = sorted(folder.glob("0*.md"))[1]
        victim.write_text(victim.read_text().rstrip("\n") + " EDITED\n")
        r = self.run_tool("--check", folder, original)
        self.assertEqual(r.returncode, 1)
        self.assertIn("DIFFER", r.stdout)

    def test_index_form_replaces_index_md_and_places_articles_beside_it(self):
        path = self.doc("activity/INDEX.md", FRONT + sections(6, 200))
        other = self.doc("activity/notes.txt", "keep me\n")
        r = self.run_tool(path, "--apply")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertTrue(path.is_file())
        self.assertIn("split verbatim", path.read_text())
        self.assertEqual(other.read_text(), "keep me\n")
        self.assertGreater(len(list((self.tmp / "activity").glob("0*.md"))), 2)

    def test_never_overwrites_an_existing_file_or_folder(self):
        path = self.doc("register.md", FRONT + sections(6, 200))
        (self.tmp / "register").mkdir()
        (self.tmp / "register/keep.txt").write_text("x")
        r = self.run_tool(path, "--apply")
        self.assertEqual(r.returncode, 1)
        self.assertIn("already exists", r.stderr)
        self.assertTrue(path.exists())
        self.assertEqual(sorted(p.name for p in (self.tmp / "register").iterdir()), ["keep.txt"])
        clash = self.doc("act/INDEX.md", FRONT + sections(6, 200))
        self.doc("act/001-section-0.md", "precious\n")
        r = self.run_tool(clash, "--apply")
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertEqual((self.tmp / "act/001-section-0.md").read_text(), "precious\n")

    def test_it_acts_only_on_the_files_it_is_given(self):
        a = self.doc("a.md", FRONT + sections(6, 200))
        b = self.doc("b.md", FRONT + sections(6, 200))
        r = self.run_tool(a, "--apply")
        self.assertEqual(r.returncode, 0)
        self.assertTrue(b.exists())
        self.assertFalse((self.tmp / "b").exists())

    def test_refuses_a_directory_a_symlink_and_a_non_markdown_file(self):
        real = self.doc("real.md", FRONT + sections(6, 200))
        link = self.tmp / "link.md"
        link.symlink_to(real)
        text = self.doc("notes.txt", "x")
        for target in (self.tmp, link, text):
            r = self.run_tool(target, "--apply")
            self.assertEqual(r.returncode, 1, str(target))
            self.assertIn("refused", r.stderr)
        self.assertTrue(real.exists() and link.is_symlink())
        self.assertFalse((self.tmp / "real").exists())

    def test_missing_counter_exits_two(self):
        path = self.doc("register.md", FRONT + sections(3, 100))
        r = self.run_tool(path, "--reflection", self.tmp / "nowhere")
        self.assertEqual(r.returncode, 2)
        self.assertIn("cannot run", r.stderr)


class KeepEntry(SplitCase):
    def make(self, count=6, words=200):
        text = FRONT + "\n# Sample register\n\nIntro line.\n" + sections(count, words)
        return self.doc("reg/register.md", text), text

    def run_keep(self, path, *extra):
        return self.run_tool(path, "--keep-entry", "register-log", "--entry-example", "od-20261123-04", *extra)

    def test_dry_run_writes_nothing_and_reports_the_entry_page(self):
        path, text = self.make()
        before = sorted(p.name for p in self.tmp.rglob("*"))
        r = self.run_keep(path, "--verify")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("entry page register.md", r.stdout)
        self.assertIn("verify: PASS", r.stdout)
        self.assertIn("keep working", r.stdout)
        self.assertEqual(sorted(p.name for p in self.tmp.rglob("*")), before)
        self.assertEqual(path.read_text(), text)

    def test_apply_keeps_the_path_as_a_small_entry_page_and_moves_the_articles(self):
        path, text = self.make()
        original = self.doc("copy.md", text)
        r = self.run_keep(path, "--apply")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertTrue(path.is_file())
        self.assertFalse((self.tmp / "reg/register").exists())          # the type never exists in both forms
        log = self.tmp / "reg/register-log"
        self.assertTrue((log / "INDEX.md").is_file())
        entry = path.read_text()
        self.assertLessEqual(self.counter.file_words(entry), 300)
        self.assertIn("version: 1.3.0\n", entry)                        # the entry page's own version bumps
        self.assertIn("title: Sample register\n", entry)
        self.assertNotIn("Section 2", entry.split("## Articles")[0])      # generated text, not original text
        self.assertEqual([p.name for p in (self.tmp / "reg").iterdir() if p.name.startswith(".")], [])   # no staging left
        self.assertEqual(self.run_tool("--check", log, original).returncode, 0)

    def test_the_entry_page_links_every_article_directly_or_through_catalogs(self):
        path, _ = self.make()
        self.run_keep(path, "--apply")
        log = self.tmp / "reg/register-log"
        entry = path.read_text()
        pages = {p.name: p.read_text() for p in log.glob("*.md")}
        reachable = set(re.findall(r"\]\(register-log/([^)]+\.md)\)", entry))
        for name in list(reachable):
            if name.startswith("catalog"):
                reachable |= set(re.findall(r"\]\(([^)]+\.md)\)", self.sd.split_frontmatter(pages[name])[1]))
        for name in pages:
            if re.match(r"^\d", name):
                self.assertIn(name, reachable)

    def test_big_register_uses_catalogs_that_link_back_to_the_entry_page(self):
        path, _ = self.make(count=80, words=300)
        self.run_keep(path, "--apply")
        log = self.tmp / "reg/register-log"
        catalogs = sorted(log.glob("catalog-*.md"))
        self.assertTrue(catalogs)
        self.assertIn("](../register.md)", catalogs[0].read_text())
        self.assertLessEqual(self.counter.file_words(path.read_text()), 300)
        for c in catalogs:
            self.assertLessEqual(self.counter.file_words(c.read_text()), 450)

    def test_there_is_headroom_for_entries_added_later_as_one_article_and_one_line(self):
        path, text = self.make()
        original = self.doc("copy.md", text)
        self.run_keep(path, "--apply")
        log = self.tmp / "reg/register-log"
        before = self.counter.file_words(path.read_text())
        self.assertLessEqual(before, 300 - self.sd.HEADROOM + 8)
        for n in range(4):
            (log / f"od-20261123-0{n}.md").write_text(
                f"---\ntitle: OD-20261123-0{n}\ncreated: 2026-11-23T00:00:00Z\nmodified: 2026-11-23T00:00:00Z\n"
                f"version: 1.0.0\ndescription: New entry\n---\n\n# OD-20261123-0{n}\n\nA new entry.\n")
            with open(path, "a") as f:
                f.write(f"- [OD-20261123-0{n} - new entry](register-log/od-20261123-0{n}.md) - A new entry\n")
            self.assertRegex(f"od-20261123-0{n}", NAME)
        self.assertLessEqual(self.counter.file_words(path.read_text()), 300)
        self.assertEqual(self.run_tool("--check", log, original).returncode, 0)   # later entries are not original text

    def test_check_detects_a_tampered_article_in_this_mode(self):
        path, text = self.make()
        original = self.doc("copy.md", text)
        self.run_keep(path, "--apply")
        victim = sorted((self.tmp / "reg/register-log").glob("0*.md"))[1]
        victim.write_text(victim.read_text().rstrip("\n") + " EDITED\n")
        r = self.run_tool("--check", self.tmp / "reg/register-log", original)
        self.assertEqual(r.returncode, 1)
        self.assertIn("DIFFER", r.stdout)

    def test_refuses_bad_names_index_documents_existing_folders_and_several_files(self):
        path, _ = self.make()
        for bad in ("Log", "log", "a-b-c-d-e", "x/y", "register"):
            r = self.run_tool(path, "--keep-entry", bad, "--apply")
            self.assertEqual(r.returncode, 1, bad)
            self.assertIn("refused", r.stderr)
        self.assertTrue(path.read_text().startswith("---"))
        (self.tmp / "reg/register-log").mkdir()
        (self.tmp / "reg/register-log/keep.txt").write_text("x")
        r = self.run_keep(path, "--apply")
        self.assertEqual(r.returncode, 1)
        self.assertIn("already exists", r.stderr)
        self.assertEqual([p.name for p in (self.tmp / "reg/register-log").iterdir()], ["keep.txt"])
        idx = self.doc("act/INDEX.md", FRONT + sections(6, 200))
        r = self.run_tool(idx, "--keep-entry", "act-log", "--apply")
        self.assertEqual(r.returncode, 1)
        self.assertIn("not INDEX.md", r.stderr)
        other = self.doc("other.md", FRONT + sections(3, 100))
        r = self.run_tool(path, other, "--keep-entry", "register-log")
        self.assertNotEqual(r.returncode, 0)


if __name__ == "__main__":
    unittest.main()
