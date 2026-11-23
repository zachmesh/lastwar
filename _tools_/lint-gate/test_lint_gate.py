"""Tests for lint_gate.py on isolated temporary git repositories; they never touch a live repository.

Run: python3 -m unittest discover -s _tools_/lint-gate
They need the reflection checkout (~/dtadpole/reflection or LINT_GATE_REFLECTION) and skip without it.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
GATE = HERE / "lint_gate.py"
REFLECTION = Path(os.environ.get("LINT_GATE_REFLECTION", "~/dtadpole/reflection")).expanduser()
HAVE_REFLECTION = (REFLECTION / "_tools_/convention-linter/lint-conventions.py").is_file()


TOOLS_INDEX = "# tools\n\n[lint-gate](lint-gate/INDEX.md)\n"


def words(n: int) -> str:
    return " ".join(f"word{i}" for i in range(n)) + "\n"


def doc(n: int, title: str = "Doc") -> str:
    return f"---\ntitle: {title}\n---\n\n" + words(n)


@unittest.skipUnless(HAVE_REFLECTION, "reflection checkout not found")
class GateCase(unittest.TestCase):
    """One fixture repository per test: a clean base commit holding a legacy oversized record, an oversized
    append-only day index, an INDEX-less records folder and a stray file in a type folder."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="lint-gate-test-"))
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.repo = self.tmp / "repo"
        self.repo.mkdir()
        self.run_git("init", "-q", "-b", "main")
        self.run_git("config", "user.name", "test")
        self.run_git("config", "user.email", "test@example.com")
        shutil.copytree(HERE, self.repo / "_tools_/lint-gate", ignore=shutil.ignore_patterns("__pycache__", "test_*"))
        self.write("_tools_/INDEX.md", TOOLS_INDEX)
        self.write("_tools_/old.py", "x = 1\n")
        self.write("_records_/INDEX.md", "# records\n")
        self.write("_records_/2026-11-22/INDEX.md", doc(600, "Day"))
        self.write("_records_/2026-11-22/legacy-activity/INDEX.md", "# legacy\n")
        self.write("_records_/2026-11-22/legacy-activity/0100-legacy-run.md", doc(600, "Legacy"))
        self.write("_records_/2026-11-22/bare-activity/0100-run.md", doc(50, "Bare"))
        self.run_git("add", "-A")
        self.run_git("commit", "-q", "--no-verify", "-m", "base")

    def run_git(self, *args, check=True):
        env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
        return subprocess.run(["git", "-C", str(self.repo), *args], capture_output=True, text=True, env=env, check=check)

    def write(self, rel: str, text: str):
        path = self.repo / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def gate(self, *args, env=None):
        full = dict(os.environ, **(env or {}))
        full.pop("GIT_INDEX_FILE", None)
        return subprocess.run([sys.executable, "-B", str(self.repo / "_tools_/lint-gate/lint_gate.py"), *args,
                               "--root", str(self.repo)], capture_output=True, text=True, env=full)

    def stage_check(self, *paths):
        self.run_git("add", "--", *paths)
        return self.gate("check", "--staged")


class CheckStaged(GateCase):
    def test_new_600_word_document_blocks(self):
        self.write("_records_/2026-11-22/legacy-activity/0200-big-run.md", doc(600, "Big"))
        r = self.stage_check("_records_/2026-11-22/legacy-activity")
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("BLOCKED [document-concision] _records_/2026-11-22/legacy-activity/0200-big-run.md", r.stdout)

    def test_new_400_word_document_passes(self):
        self.write("_records_/2026-11-22/legacy-activity/0200-ok-run.md", doc(400, "Ok"))
        r = self.stage_check("_records_/2026-11-22/legacy-activity")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_untouched_legacy_document_passes(self):
        self.write("_records_/2026-11-22/legacy-activity/0200-ok-run.md", doc(100, "Small"))
        r = self.stage_check("_records_/2026-11-22/legacy-activity/0200-ok-run.md")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_changed_legacy_document_blocks(self):
        with open(self.repo / "_records_/2026-11-22/legacy-activity/0100-legacy-run.md", "a") as f:
            f.write(words(40))
        r = self.stage_check("_records_/2026-11-22/legacy-activity/0100-legacy-run.md")
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("0100-legacy-run.md", r.stdout)

    def test_new_folder_without_index_blocks(self):
        self.write("_records_/2026-11-23/fresh-activity/0100-run.md", doc(50, "Fresh"))
        r = self.stage_check("_records_/2026-11-23")
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("[entry-points] _records_/2026-11-23/fresh-activity", r.stdout)

    def test_legacy_folder_without_index_passes(self):
        self.write("_records_/2026-11-22/bare-activity/0200-run.md", doc(50, "Bare two"))
        r = self.stage_check("_records_/2026-11-22/bare-activity")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("1 legacy structural", r.stdout)

    def test_new_file_in_type_folder_blocks_but_old_one_does_not(self):
        self.write("_tools_/INDEX.md", TOOLS_INDEX + "\nA changed line.\n")
        self.assertEqual(self.stage_check("_tools_/INDEX.md").returncode, 0)
        self.write("_tools_/fresh.py", "y = 2\n")
        r = self.stage_check("_tools_/fresh.py")
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("[type-instance-trees] _tools_", r.stdout)
        self.assertIn("fresh.py", r.stdout)
        self.assertNotIn("old.py", r.stdout)

    def test_gitignored_file_in_type_folder_is_not_a_new_defect(self):
        (self.repo / ".gitignore").write_text("_tools_/scratch.py\n")
        self.write("_tools_/scratch.py", "z = 3\n")
        self.write("_tools_/INDEX.md", TOOLS_INDEX + "\nAnother changed line.\n")
        r = self.stage_check("_tools_/INDEX.md", ".gitignore")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_day_index_is_exempt_and_exemption_is_visible(self):
        with open(self.repo / "_records_/2026-11-22/INDEX.md", "a") as f:
            f.write("- 21:00 PT tick line\n")
        r = self.stage_check("_records_/2026-11-22/INDEX.md")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("1 exempt finding", r.stdout)

    def test_grandfathered_records_are_ten_exact_paths(self):
        lines = [ln.strip() for ln in (HERE / "exempt.txt").read_text().splitlines() if ln.strip() and not ln.startswith("#")]
        records = [ln for ln in lines if ln != "_records_/*/INDEX.md" and not ln.startswith("folder ")]
        self.assertEqual(len(records), 10)
        for ln in records:
            self.assertRegex(ln, r"^_records_/2026-11-22/[a-z-]+/\d{4}-queue-run\.md$")
            self.assertFalse(set(ln) & set("*?["), ln)

    def test_grandfathered_record_passes_and_its_neighbour_blocks(self):
        self.write("_records_/2026-11-22/alliance-gifts/INDEX.md", "# gifts\n")
        self.write("_records_/2026-11-22/alliance-gifts/2030-queue-run.md", doc(650, "Gifts"))
        r = self.stage_check("_records_/2026-11-22/alliance-gifts")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("1 exempt finding", r.stdout)
        self.write("_records_/2026-11-22/alliance-gifts/2031-queue-run.md", doc(650, "Gifts next"))
        r = self.stage_check("_records_/2026-11-22/alliance-gifts/2031-queue-run.md")
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("2031-queue-run.md", r.stdout)

    def test_untracked_offender_that_is_not_staged_does_not_block(self):
        self.write("_tools_/loose.py", "z = 1\n")   # untracked, left out of the commit
        self.write("_tools_/INDEX.md", TOOLS_INDEX + "\nOne more line.\n")
        self.assertEqual(self.stage_check("_tools_/INDEX.md").returncode, 0)
        r = self.stage_check("_tools_/loose.py")
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("loose.py", r.stdout)

    def test_folder_exemption_lever_is_off_until_a_folder_line_is_added(self):
        self.write("_records_/2026-11-23/fresh-activity/0100-run.md", doc(50, "Fresh"))
        self.write("_records_/2026-11-23/INDEX.md", "# day\n")
        self.assertEqual(self.stage_check("_records_/2026-11-23").returncode, 1)
        with open(self.repo / "_tools_/lint-gate/exempt.txt", "a") as f:
            f.write("folder _records_/*/*\n")
        r = self.stage_check("_records_/2026-11-23")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("1 exempt finding", r.stdout)

    def test_rules_option_limits_what_blocks(self):
        self.write("_records_/2026-11-22/legacy-activity/0200-big-run.md", doc(600, "Big"))
        self.run_git("add", "-A")
        r = self.gate("check", "--staged", "--rules", "entry-points")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_staged_check_is_fast_on_the_fixture(self):
        self.write("_records_/2026-11-22/legacy-activity/0200-ok-run.md", doc(100, "Small"))
        self.run_git("add", "-A")
        started = time.time()
        self.assertEqual(self.gate("check", "--staged").returncode, 0)
        self.assertLess(time.time() - started, 30)

    def test_missing_reflection_exits_two(self):
        r = self.gate("check", "--staged", "--reflection", str(self.tmp / "nowhere"))
        self.assertEqual(r.returncode, 2)
        self.assertIn("cannot run", r.stderr)


class CheckBase(GateCase):
    def test_base_ref_blocks_what_the_ref_lacks(self):
        self.write("_records_/2026-11-22/legacy-activity/0200-big-run.md", doc(600, "Big"))
        self.run_git("add", "-A")
        self.run_git("commit", "-q", "--no-verify", "-m", "oversized")
        self.assertEqual(self.gate("check", "--base", "HEAD").returncode, 0)
        r = self.gate("check", "--base", "HEAD~1")
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("0200-big-run.md", r.stdout)


class Install(GateCase):
    def commit(self, message="change"):
        return self.run_git("commit", "-q", "-m", message, check=False)

    def test_hook_runs_from_git_commit(self):
        r = self.gate("install")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("git config --unset core.hooksPath", r.stdout)
        self.assertEqual(self.run_git("config", "--local", "core.hooksPath").stdout.strip(), "_tools_/lint-gate/hooks")
        head = self.run_git("rev-parse", "HEAD").stdout
        self.write("_records_/2026-11-22/legacy-activity/0200-big-run.md", doc(600, "Big"))
        self.run_git("add", "-A")
        blocked = self.commit("big")
        self.assertNotEqual(blocked.returncode, 0)
        self.assertIn("BLOCKED [document-concision]", blocked.stdout + blocked.stderr)
        self.assertEqual(self.run_git("rev-parse", "HEAD").stdout, head)
        self.write("_records_/2026-11-22/legacy-activity/0200-big-run.md", doc(400, "Ok"))
        self.run_git("add", "-A")
        ok = self.commit("ok")
        self.assertEqual(ok.returncode, 0, ok.stdout + ok.stderr)
        self.assertNotEqual(self.run_git("rev-parse", "HEAD").stdout, head)
        self.write("_records_/2026-11-22/legacy-activity/0300-note.md", doc(30, "Note"))
        self.run_git("add", "-A")
        self.assertEqual(self.commit("legacy untouched").returncode, 0)

    def test_commit_all_flag_is_gated_too(self):
        self.gate("install")
        with open(self.repo / "_records_/2026-11-22/legacy-activity/0100-legacy-run.md", "a") as f:
            f.write(words(40))
        r = self.run_git("commit", "-a", "-q", "-m", "grow legacy", check=False)
        self.assertNotEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_hook_allows_commit_when_the_gate_cannot_run(self):
        self.gate("install")
        self.write("_records_/2026-11-22/legacy-activity/0200-big-run.md", doc(600, "Big"))
        self.run_git("add", "-A")
        env = dict(os.environ, LINT_GATE_REFLECTION=str(self.tmp / "nowhere"))
        env = {k: v for k, v in env.items() if not k.startswith("GIT_")}
        r = subprocess.run(["git", "-C", str(self.repo), "commit", "-q", "-m", "no gate"], capture_output=True, text=True, env=env)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("could not run", r.stderr)

    def test_dry_run_changes_nothing_and_a_foreign_hooks_path_is_not_replaced(self):
        self.assertEqual(self.gate("install", "--dry-run").returncode, 0)
        self.assertEqual(self.run_git("config", "--local", "--get", "core.hooksPath", check=False).stdout.strip(), "")
        self.run_git("config", "--local", "core.hooksPath", ".githooks")
        self.assertEqual(self.gate("install").returncode, 1)
        self.assertEqual(self.run_git("config", "--local", "core.hooksPath").stdout.strip(), ".githooks")
        self.assertEqual(self.gate("install", "--force").returncode, 0)

    def test_rollback_restores_plain_commits(self):
        self.gate("install")
        self.run_git("config", "--unset", "core.hooksPath")
        self.write("_records_/2026-11-22/legacy-activity/0200-big-run.md", doc(600, "Big"))
        self.run_git("add", "-A")
        self.assertEqual(self.commit("big after rollback").returncode, 0)


class RecordCheck(GateCase):
    def test_limit_is_480_words(self):
        self.write("rec/a.md", doc(479, "A"))   # frontmatter is not counted: 479 words
        self.write("rec/b.md", doc(480, "B"))
        a = self.gate("record-check", str(self.repo / "rec/a.md"))
        b = self.gate("record-check", str(self.repo / "rec/b.md"))
        self.assertEqual(a.returncode, 0, a.stdout)
        self.assertIn("479 body words", a.stdout)
        self.assertEqual(b.returncode, 1, b.stdout)
        self.assertIn("480 body words", b.stdout)
        self.assertIn("TRIM BEFORE CLOSING", b.stdout)

    def test_frontmatter_is_not_counted_and_a_missing_file_exits_two(self):
        self.write("rec/c.md", "---\n" + "title: x\n" * 600 + "---\n\nthree words here\n")
        c = self.gate("record-check", str(self.repo / "rec/c.md"))
        self.assertEqual(c.returncode, 0)
        self.assertIn("3 body words", c.stdout)
        self.assertEqual(self.gate("record-check", str(self.repo / "rec/none.md")).returncode, 2)


class Watch(GateCase):
    def watch(self, *extra):
        return self.gate("watch", "--format", "json", "--baseline", str(self.tmp / "baseline.json"), *extra)

    def test_counts_new_errors_baseline_summary_and_growth(self):
        first = self.watch()
        self.assertEqual(first.returncode, 0, first.stderr)
        summary = json.loads(first.stdout.split("\nbaseline summary written")[0])
        self.assertEqual((summary["over_500"], summary["legacy"], summary["new"]), (2, 2, 0))
        self.assertEqual(summary["new_errors_total"], 0)
        self.assertEqual(summary["exempt_documents"], 0)
        saved = json.loads((self.tmp / "baseline.json").read_text())
        self.assertNotIn("documents_list", saved)
        self.assertLessEqual(len(saved["top"]), 50)
        self.assertEqual(saved["git_head"], self.run_git("rev-parse", "HEAD").stdout.strip())
        self.assertIn("_records_", saved["by_top_folder"])
        # a new oversized record, and a legacy record that grows by more than 20 percent
        self.write("_records_/2026-11-22/legacy-activity/0200-big-run.md", doc(600, "Big"))
        with open(self.repo / "_records_/2026-11-22/legacy-activity/0100-legacy-run.md", "a") as f:
            f.write(words(150))
        self.run_git("add", "-A")
        self.run_git("commit", "-q", "--no-verify", "-m", "grow")
        second = self.watch()
        self.assertEqual(second.returncode, 0, second.stderr)
        summary = json.loads(second.stdout.split("\nbaseline summary written")[0])
        self.assertEqual(summary["anchor"], saved["anchor"])
        self.assertEqual(summary["new"], 2)   # the new record and the grown legacy record
        self.assertEqual(summary["new_errors"]["document-concision"], 2)
        grown = {g["path"]: g for g in summary["growth"]}
        self.assertIn("_records_/2026-11-22/legacy-activity/0100-legacy-run.md", grown)
        self.assertGreater(grown["_records_/2026-11-22/legacy-activity/0100-legacy-run.md"]["growth_pct"], 20)

    def test_text_report_names_the_trigger_and_the_largest_documents(self):
        self.write("_records_/2026-11-22/legacy-activity/0200-big-run.md", doc(700, "Big"))
        r = self.gate("watch", "--baseline", str(self.tmp / "baseline.json"))
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("NEW ERRORS vs anchor: 1", r.stdout)
        self.assertIn("assign the owning seat a fix", r.stdout)
        self.assertIn("0200-big-run.md", r.stdout)
        self.assertIn("largest documents", r.stdout)

    def test_top_list_is_capped_and_no_full_list_is_stored(self):
        rows = [{"path": f"_records_/d{i}.md", "body_words": 100 + i, "legacy": False, "hard_violation": False,
                 "severity": "ok"} for i in range(80)]
        report = self.tmp / "report.json"
        report.write_text(json.dumps({"errors": [], "document_budgets": {"documents": rows}}))
        r = self.watch("--from-json", str(report))
        self.assertEqual(r.returncode, 0, r.stderr)
        saved = json.loads((self.tmp / "baseline.json").read_text())
        self.assertEqual(len(saved["top"]), 50)
        self.assertEqual(saved["top"][0]["words"], 179)
        self.assertEqual(saved["documents"], 80)
        self.assertNotIn("documents_list", saved)
        self.assertLess((self.tmp / "baseline.json").stat().st_size, 20000)


if __name__ == "__main__":
    unittest.main()
