"""Tests for _tools_/integrator/integrator.py on a fake remote (a bare repository) and a fake gh. Every denylist, name and
branch here is made up; no credential is real, and none may ever appear in an output or a log.

Run: python3 -m unittest discover -s _tools_/integrator
"""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOOL = HERE / "integrator.py"
FAKE_GH = HERE / "fake_gh.py"
LINT_GATE = HERE.parent / "lint-gate" / "lint_gate.py"
TOKEN = "ghp_" + "a1b2c3d4e5f6" * 3                      # made up, token-shaped
NAME = "Zorvane Quill"                                    # made up
TEAM = """seats:
  - key: toolsmith
    write_scopes:
      - _tools_/
    excluded_write_scopes:
      - _queue_/
      - _records_/
  - key: coordinator
    write_scopes:
      - TEAM.yaml
      - _seats_/
    excluded_write_scopes: []
"""


def git(cwd, *args, check=True, env=None):
    base = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    base.update(env or {})
    return subprocess.run(["git", "-C", str(cwd), "-c", "user.email=t@example.org", "-c", "user.name=tester", *args],
                          capture_output=True, text=True, check=check, env=base)


class Case(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="integrator-test-", dir="/tmp"))
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.origin = self.tmp / "origin.git"
        subprocess.run(["git", "init", "-q", "--bare", "-b", "main", str(self.origin)], check=True)
        seed = self.tmp / "seed"
        subprocess.run(["git", "init", "-q", "-b", "main", str(seed)], check=True)
        (seed / "TEAM.yaml").write_text(TEAM)
        (seed / "README.md").write_text("# fixture\n")
        (seed / "_tools_").mkdir()
        (seed / "_tools_" / "INDEX.md").write_text("# tools\n")
        (seed / "_queue_" / "claimed").mkdir(parents=True)
        (seed / "_queue_" / "claimed" / ".gitkeep").write_text("")
        git(seed, "add", "-A")
        git(seed, "commit", "-q", "-m", "seed")
        git(seed, "remote", "add", "origin", str(self.origin))
        git(seed, "push", "-q", "origin", "main")
        self.work = self.tmp / "work"
        subprocess.run(["git", "clone", "-q", str(self.origin), str(self.work)], check=True, capture_output=True)
        (self.work / ".git" / "privacy-denylist.txt").write_text(f"# made-up\n# marker: owner account\nzorvane\\s+quill\n")
        self.state = self.tmp / "gh-state.json"
        bindir = self.tmp / "bin"
        bindir.mkdir()
        self.env = dict(os.environ, INTEGRATOR_GH=str(self.fake_gh_wrapper(bindir)), FAKE_GH_STATE=str(self.state),
                        FAKE_GH_REMOTE=str(self.origin), GH_TOKEN=TOKEN)

    def fake_gh_wrapper(self, bindir):
        script = bindir / "gh"
        script.write_text(f"#!/bin/sh\nexec {sys.executable} {FAKE_GH} \"$@\"\n")
        script.chmod(0o755)
        return script

    def run_tool(self, *args, env=None, root=None):
        return subprocess.run([sys.executable, "-B", str(TOOL), "--root", str(root or self.work), *args], capture_output=True,
                              text=True, env=env or self.env)

    def branch(self, name, files, message="change", author=None):
        git(self.work, "checkout", "-q", "-B", name, "main")
        for rel, text in files.items():
            path = self.work / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            if isinstance(text, bytes):
                path.write_bytes(text)
            else:
                path.write_text(text)
        git(self.work, "add", "-A")
        env = {"GIT_AUTHOR_NAME": author, "GIT_COMMITTER_NAME": author} if author else None
        git(self.work, "commit", "-q", "-m", message, env=env)
        sha = git(self.work, "rev-parse", "HEAD").stdout.strip()
        git(self.work, "checkout", "-q", "main")
        return sha

    def check(self, name, seat="toolsmith", *extra):
        return self.run_tool("check", name, "--seat", seat, "--lint-gate", str(LINT_GATE), *extra)

    def log_lines(self):
        lines = []
        for path in sorted((self.work / "_records_").glob("*/integration/actions.jsonl")):
            lines += [json.loads(x) for x in path.read_text().splitlines()]
        return lines

    def silent(self, *results):
        for r in results:
            out = r.stdout + r.stderr
            for text in ("zorvane", "quill", TOKEN, "ghp_"):
                self.assertNotIn(text.lower(), out.lower())

    def gh_calls(self):
        return json.loads(self.state.read_text())["calls"] if self.state.exists() else []

    def land(self, name="work/clean", files=None):
        """check, push and open a clean branch; returns (sha, pr number)."""
        sha = self.branch(name, files or {"_tools_/INDEX.md": "# tools\n\nok\n"})
        self.assertEqual(self.check(name).returncode, 0)
        self.assertEqual(self.run_tool("push", name).returncode, 0)
        r = self.run_tool("open", name, "--title", "a clean change")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        return sha, int(re.search(r"#(\d+)", r.stdout).group(1))


class Refusals(Case):
    def test_force_squash_rebase_delete_and_skip_flags_are_refused_wherever_they_appear(self):
        self.branch("work/x", {"_tools_/a.py": "x = 1\n"})
        for argv in (["push", "work/x", "--force"], ["push", "-f", "work/x"], ["push", "work/x", "--force-with-lease"],
                     ["merge", "1", "--head-sha", "abc", "--squash"], ["merge", "1", "--head-sha", "abc", "--rebase"],
                     ["push", "work/x", "--delete-branch"], ["push", "--delete", "work/x"], ["merge", "1", "--head-sha", "a", "--admin"],
                     ["push", "+work/x"], ["open", "work/x", "--title", "t", "--no-verify"]):
            r = self.run_tool(*argv)
            self.assertEqual(r.returncode, 3, f"{argv}: {r.stdout}{r.stderr}")
            self.assertIn("refused", r.stdout)
        self.assertEqual(git(self.origin, "branch", "--list", "work/x").stdout.strip(), "")
        self.assertEqual(self.gh_calls(), [])

    def test_main_is_never_pushed_opened_checked_or_merged(self):
        for name in ("main", "origin/main", "refs/heads/main", "HEAD", "MAIN"):
            for verb in (["push", name], ["open", name, "--title", "t"], ["check", name, "--seat", "toolsmith"]):
                r = self.run_tool(*verb)
                self.assertEqual(r.returncode, 3, f"{verb}: {r.stdout}{r.stderr}")
                self.assertIn("main is never", r.stdout)

    def test_a_branch_name_must_be_plain(self):
        for name in ("--evil", "a..b", "x y", "work/x.lock", "-x"):
            self.assertIn(self.run_tool("push", name).returncode, (2, 3), name)


class Check(Case):
    def test_a_clean_branch_passes_with_counts_only_and_one_log_line(self):
        sha = self.branch("work/clean", {"_tools_/INDEX.md": "# tools\n\nok\n"})
        r = self.check("work/clean")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn(f"check work/clean head {sha[:10]} against origin/main: PASS", r.stdout)
        for line in ("changed_files: 1", "outside_scope: 0", "binaries_added: 0", "positive_control: ok", "tree_files_matching: 0",
                     "file_names_matching: 0", "commit_messages_matching: 0", "wrap_aware_files_matching: 0", "overlapping_prs: 0"):
            self.assertIn(line, r.stdout)
        self.silent(r)
        lines = [x for x in self.log_lines() if x["action"] == "check"]
        self.assertEqual(len(lines), 1)
        self.assertEqual((lines[0]["head"], lines[0]["result"]), (sha, "pass"))

    def test_a_name_in_a_file_a_file_name_a_message_or_an_author_fails_and_is_never_echoed(self):
        cases = {
            "content": ({"_tools_/a.md": f"The owner is {NAME} today.\n"}, "change", None),
            "filename": ({"_tools_/zorvane-quill-notes.md": "clean\n"}, "change", None),
            "message": ({"_tools_/b.md": "clean\n"}, f"about {NAME}", None),
            "author": ({"_tools_/c.md": "clean\n"}, "change", "Zorvane Quill"),
        }
        for label, (files, message, author) in cases.items():
            self.branch(f"work/{label}", files, message, author)
            r = self.check(f"work/{label}")
            self.assertEqual(r.returncode, 1, f"{label}: {r.stdout}{r.stderr}")
            self.assertIn("privacy-matches", r.stdout, label)
            self.silent(r)
        self.assertTrue(all(x["result"] == "fail" for x in self.log_lines() if x["action"] == "check"))

    def test_a_name_wrapped_over_a_line_break_is_caught_by_the_wrap_aware_scan(self):
        self.branch("work/wrapped", {"_tools_/w.md": "the owner is Zorvane\n    Quill and so on\n"})
        r = self.check("work/wrapped")
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("tree_files_matching: 0", r.stdout)                  # git grep is line-based and misses it
        self.assertIn("wrap_aware_files_matching: 1", r.stdout)
        self.silent(r)

    def test_scope_is_checked_against_the_seat_in_team_yaml(self):
        self.branch("work/queue", {"_queue_/inbox/x.md": "x\n"})
        r = self.check("work/queue")
        self.assertEqual(r.returncode, 1)
        self.assertIn("outside_scope: 1", r.stdout)
        self.branch("work/team", {"TEAM.yaml": TEAM + "# edit\n"})
        self.assertIn("outside_scope: 1", self.check("work/team").stdout)                 # a toolsmith may not edit TEAM.yaml
        self.assertEqual(self.check("work/team", "coordinator").returncode, 0)             # the coordinator may
        self.assertIn("unknown-seat", self.check("work/team", "nobody").stdout)

    def test_a_binary_or_image_blocks(self):
        self.branch("work/img", {"_tools_/pic.png": b"\x89PNG\r\n\x1a\n\0\0"})
        r = self.check("work/img")
        self.assertEqual(r.returncode, 1)
        self.assertIn("binary-added", r.stdout)

    def test_no_denylist_means_no_pass(self):
        (self.work / ".git" / "privacy-denylist.txt").unlink()
        self.branch("work/clean", {"_tools_/INDEX.md": "# tools\n\nx = 1\n"})
        r = self.check("work/clean")
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("no-denylist", r.stdout)

    def test_a_broken_scan_engine_is_a_failure_not_a_zero(self):
        broken = self.tmp / "broken_gate.py"
        broken.write_text("import sys\nsys.exit(0)\n")                     # prints no census: the positive control cannot pass
        self.branch("work/clean", {"_tools_/INDEX.md": "# tools\n\nx = 1\n"})
        r = self.run_tool("check", "work/clean", "--seat", "toolsmith", "--lint-gate", str(broken))
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("positive-control-failed", r.stdout)

    def test_named_tests_run_in_the_clean_worktree_and_a_failure_blocks(self):
        stub = "---\ntitle: T\ncreated: 2026-11-23T00:00:00Z\nmodified: 2026-11-23T00:00:00Z\nversion: 1.0.0\ndescription: t\n---\n\n# T\n"
        good = {"_tools_/t-tests/INDEX.md": stub, "_tools_/t-tests/test_ok.py": "import unittest\nclass T(unittest.TestCase):\n    def test_a(self): pass\n"}
        bad = {"_tools_/t-tests/INDEX.md": stub, "_tools_/t-tests/test_bad.py": "import unittest\nclass T(unittest.TestCase):\n    def test_a(self): self.fail('x')\n"}
        self.branch("work/good", good)
        r = self.check("work/good", "toolsmith", "--test", "_tools_/t-tests")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("tests[_tools_/t-tests]: 1 ran, ok", r.stdout)
        self.branch("work/bad", bad)
        r = self.check("work/bad", "toolsmith", "--test", "_tools_/t-tests")
        self.assertEqual(r.returncode, 1)
        self.assertIn("FAILED", r.stdout)

    def test_overlap_with_another_open_pr_is_reported(self):
        self.branch("work/first", {"_tools_/INDEX.md": "# tools\n\na = 1\n"})
        self.assertEqual(self.check("work/first").returncode, 0)
        self.run_tool("push", "work/first")
        self.run_tool("open", "work/first", "--title", "first")
        self.branch("work/second", {"_tools_/INDEX.md": "# tools\n\na = 2\n"})
        r = self.check("work/second")
        self.assertIn("overlapping_prs: 1", r.stdout)

    def test_the_worktree_and_temp_files_are_cleaned_up(self):
        self.branch("work/clean", {"_tools_/INDEX.md": "# tools\n\nx = 1\n"})
        self.check("work/clean")
        self.assertEqual(git(self.work, "worktree", "list").stdout.strip().count("\n"), 0)
        self.assertEqual(list(Path("/tmp").glob("integrator-patterns-*")), [])


class Landing(Case):
    def test_push_needs_a_passing_check_of_this_exact_head_and_is_never_forced(self):
        sha = self.branch("work/clean", {"_tools_/INDEX.md": "# tools\n\nx = 1\n"})
        r = self.run_tool("push", "work/clean")
        self.assertEqual(r.returncode, 3)
        self.assertIn("no passing check", r.stdout)
        self.assertEqual(self.check("work/clean").returncode, 0)
        self.assertEqual(self.run_tool("push", "work/clean").returncode, 0)
        self.assertEqual(git(self.origin, "rev-parse", "refs/heads/work/clean").stdout.strip(), sha)
        git(self.work, "checkout", "-q", "work/clean")
        (self.work / "_tools_" / "more.py").write_text("y = 2\n")
        git(self.work, "add", "-A")
        git(self.work, "commit", "-q", "-m", "moved head")
        git(self.work, "checkout", "-q", "main")
        self.assertEqual(self.run_tool("push", "work/clean").returncode, 3)                # the head moved: check again first

    def test_a_non_fast_forward_push_fails_and_origin_keeps_its_branch(self):
        sha = self.branch("work/clean", {"_tools_/INDEX.md": "# tools\n\nx = 1\n"})
        self.check("work/clean")
        git(self.work, "push", "-q", "origin", "work/clean")
        other = self.tmp / "other"
        subprocess.run(["git", "clone", "-q", str(self.origin), str(other)], check=True, capture_output=True)
        git(other, "checkout", "-q", "work/clean")
        (other / "theirs.txt").write_text("theirs\n")
        git(other, "add", "-A")
        git(other, "commit", "-q", "-m", "theirs")
        git(other, "push", "-q", "origin", "work/clean")
        theirs = git(self.origin, "rev-parse", "refs/heads/work/clean").stdout.strip()
        git(self.work, "checkout", "-q", "work/clean")
        git(self.work, "reset", "-q", "--hard", sha)
        (self.work / "_tools_" / "mine.py").write_text("m = 1\n")
        git(self.work, "add", "-A")
        git(self.work, "commit", "-q", "-m", "mine")
        mine = git(self.work, "rev-parse", "HEAD").stdout.strip()
        git(self.work, "checkout", "-q", "main")
        self.assertEqual(self.check("work/clean").returncode, 0)
        r = self.run_tool("push", "work/clean")
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertEqual(git(self.origin, "rev-parse", "refs/heads/work/clean").stdout.strip(), theirs)
        self.assertNotEqual(theirs, mine)

    def test_open_needs_the_branch_on_origin_at_the_same_head(self):
        self.branch("work/clean", {"_tools_/INDEX.md": "# tools\n\nx = 1\n"})
        r = self.run_tool("open", "work/clean", "--title", "t")
        self.assertEqual(r.returncode, 1)
        self.assertIn("push it first", r.stdout)

    def test_the_full_landing_merges_with_a_merge_commit_and_reads_back_clean(self):
        sha, pr = self.land()
        r = self.run_tool("merge", str(pr), "--head-sha", sha)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        merge = re.search(r"merge commit (\w+)", r.stdout).group(1)
        calls = [c for c in self.gh_calls() if c[:2] == ["pr", "merge"]]
        self.assertEqual(len(calls), 1)
        self.assertIn("--merge", calls[0])
        self.assertIn("--match-head-commit", calls[0])
        for forbidden in ("--squash", "--rebase", "--delete-branch", "--admin"):
            self.assertNotIn(forbidden, calls[0])
        read = self.run_tool("readback", str(pr))
        self.assertEqual(read.returncode, 0, read.stdout + read.stderr)
        for fact in ("parents: 2", "branch_head_is_a_parent: True", "tree_equals_branch_tree: True",
                     "branch_head_ancestor_of_main: True", "merge_on_main: True", "readback: OK"):
            self.assertIn(fact, read.stdout)
        self.assertEqual(git(self.origin, "rev-parse", "--verify", "refs/heads/work/clean").returncode, 0)   # branch not deleted
        self.assertTrue(merge)

    def test_a_moved_head_is_refused_and_gh_never_merges(self):
        sha, pr = self.land()
        other = self.tmp / "other"
        subprocess.run(["git", "clone", "-q", str(self.origin), str(other)], check=True, capture_output=True)
        git(other, "checkout", "-q", "work/clean")
        (other / "late.txt").write_text("late\n")
        git(other, "add", "-A")
        git(other, "commit", "-q", "-m", "late push")
        git(other, "push", "-q", "origin", "work/clean")
        r = self.run_tool("merge", str(pr), "--head-sha", sha)
        self.assertEqual(r.returncode, 3, r.stdout + r.stderr)
        self.assertIn("not the", r.stdout)
        self.assertEqual([c for c in self.gh_calls() if c[:2] == ["pr", "merge"]], [])
        self.assertEqual(self.log_lines()[-1]["reason"], "head-moved")

    def test_nothing_unscanned_is_merged(self):
        sha = self.branch("work/clean", {"_tools_/INDEX.md": "# tools\n\nx = 1\n"})
        git(self.work, "push", "-q", "origin", "work/clean")                               # pushed around the wrapper
        opened = self.run_tool("open", "work/clean", "--title", "t")
        self.assertEqual(opened.returncode, 0, opened.stdout + opened.stderr)
        r = self.run_tool("merge", "1", "--head-sha", sha)
        self.assertEqual(r.returncode, 3)
        self.assertIn("nothing unscanned is merged", r.stdout)

    def test_a_pr_that_does_not_target_main_is_refused(self):
        sha, pr = self.land()
        state = json.loads(self.state.read_text())
        state["prs"][0]["base"] = "release"
        self.state.write_text(json.dumps(state))
        r = self.run_tool("merge", str(pr), "--head-sha", sha)
        self.assertEqual(r.returncode, 3)
        self.assertIn("does not target main", r.stdout)

    def test_readback_flags_a_commit_that_is_not_the_merge_of_the_branch(self):
        sha, pr = self.land()
        self.run_tool("merge", str(pr), "--head-sha", sha)
        other_sha = self.branch("work/other", {"_tools_/INDEX.md": "# tools\n\no = 1\n"})
        git(self.work, "push", "-q", "origin", "work/other")
        r = self.run_tool("readback", "--branch", "work/clean", "--merge-sha", other_sha)
        self.assertEqual(r.returncode, 1)
        self.assertIn("readback: DIFFERS", r.stdout)


class Status(Case):
    def test_status_counts_prs_ahead_behind_and_the_claimed_folder(self):
        self.land()
        (self.work / "_queue_" / "claimed" / "run-unit.md").write_text("x\n")
        git(self.work, "checkout", "-q", "main")
        (self.work / "local.txt").write_text("local\n")
        git(self.work, "add", "local.txt")
        git(self.work, "commit", "-q", "-m", "local only")
        r = self.run_tool("status", "--json")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        data = json.loads(r.stdout)
        self.assertEqual(len(data["open_prs"]), 1)
        self.assertEqual((data["main_ahead_of_origin"], data["main_behind_origin"]), ("1", "0"))
        self.assertEqual(data["claimed_units"], 1)
        text = self.run_tool("status").stdout
        self.assertIn("a live run holds the desktop", text)
        self.assertIn("ahead 1, behind 0", text)

    def test_a_shallow_clone_is_called_out(self):
        shallow = self.tmp / "shallow"
        subprocess.run(["git", "clone", "-q", "--depth", "1", f"file://{self.origin}", str(shallow)], check=True, capture_output=True)
        r = self.run_tool("status", root=shallow)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("this clone is shallow", r.stdout)


class Secrets(Case):
    def test_a_token_in_the_environment_or_in_gh_output_never_reaches_an_output_or_the_log(self):
        sha = self.branch("work/clean", {"_tools_/INDEX.md": "# tools\n\nx = 1\n"})
        self.check("work/clean")
        self.run_tool("push", "work/clean")
        leaking = dict(self.env, FAKE_GH_LEAK="1")
        r = self.run_tool("open", "work/clean", "--title", "t", env=leaking)
        self.assertEqual(r.returncode, 1)
        self.assertIn("[token]", r.stdout)                                               # scrubbed, not echoed
        every = [r] + [self.run_tool("status")]
        self.silent(*every)
        for path in (self.work / "_records_").rglob("*"):
            if path.is_file():
                self.assertNotIn(TOKEN, path.read_text())
        self.assertTrue(sha)

    def test_every_log_line_is_json_with_counts_and_shas_only(self):
        sha, pr = self.land()
        self.run_tool("merge", str(pr), "--head-sha", sha)
        self.run_tool("readback", str(pr))
        lines = self.log_lines()
        self.assertEqual([x["action"] for x in lines], ["check", "push", "open", "merge", "readback"])
        for x in lines:
            self.assertRegex(x["at"], r"^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
            self.assertEqual(x["result"] in ("pass", "ok"), True)
            self.assertNotIn("token", json.dumps(x).lower())
        self.assertTrue((self.work / "_records_").glob("*/integration/INDEX.md"))

    def test_scrub_removes_token_shapes(self):
        sys.path.insert(0, str(HERE))
        import integrator
        os.environ["GH_TOKEN"] = "plainsecretvalue"
        self.addCleanup(os.environ.pop, "GH_TOKEN", None)
        text = integrator.scrub(f"a {TOKEN} b github_pat_{'x' * 30} c plainsecretvalue d")
        self.assertNotIn("ghp_", text)
        self.assertNotIn("github_pat_", text)
        self.assertNotIn("plainsecretvalue", text)
        self.assertEqual(text.count("[token]"), 3)


if __name__ == "__main__":
    unittest.main()
