"""Tests for tool_sync.py on throwaway repositories: a bare origin, a developer clone that lands PRs on it, and the live checkout the tool runs in.

Run: python3 -m unittest discover -s _tools_/tool-sync
"""
from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOOL = HERE / "tool_sync.py"
GUARD_REF = "refs/queue-fresh/main"


class Repos(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="tool-sync-"))
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.origin, self.dev, self.live = self.tmp / "origin.git", self.tmp / "dev", self.tmp / "live"
        subprocess.run(["git", "init", "-q", "--bare", "-b", "main", str(self.origin)], check=True)
        subprocess.run(["git", "clone", "-q", str(self.origin), str(self.dev)], check=True, capture_output=True)
        self.git(self.dev, "checkout", "-q", "-b", "main")
        self.put(self.dev, "_tools_/queue.py", "queue v1\n")
        self.put(self.dev, "_tools_/regulars.json", "{}\n")
        self.put(self.dev, "_tools_/old_tool.py", "old\n")
        self.put(self.dev, "_tools_/state/queue-state.json", "{}\n")
        self.put(self.dev, "_records_/note.md", "record v1\n")
        self.commit(self.dev, "base")
        self.git(self.dev, "push", "-q", "origin", "main")
        subprocess.run(["git", "clone", "-q", str(self.origin), str(self.live)], check=True, capture_output=True)
        self.git(self.live, "checkout", "-q", "main")

    def git(self, repo, *args, check=True):
        return subprocess.run(["git", "-C", str(repo), "-c", "user.email=t@e.org", "-c", "user.name=t", *args], capture_output=True, text=True, check=check).stdout.strip()

    def put(self, repo, rel, text):
        path = Path(repo) / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)

    def commit(self, repo, message):
        self.git(repo, "add", "-A")
        self.git(repo, "commit", "-q", "-m", message)

    def land(self, message, **files):
        """What the Integrator does: a PR's change arrives on origin main as one merge commit."""
        for rel, text in files.items():
            if text is None:
                (self.dev / rel.replace("__", "/")).unlink()
            else:
                self.put(self.dev, rel.replace("__", "/"), text)
        self.commit(self.dev, message)
        self.git(self.dev, "push", "-q", "origin", "main")

    def sync(self, *args):
        return subprocess.run([sys.executable, "-B", str(TOOL), "--root", str(self.live), *args], capture_output=True, text=True)

    def head(self):
        return self.git(self.live, "rev-parse", "HEAD")

    def read(self, rel):
        return (self.live / rel).read_text()


class Quiet(Repos):
    def test_equal_is_silent_and_changes_nothing(self):
        before = self.head()
        r = self.sync()
        self.assertEqual((r.returncode, r.stdout, r.stderr), (0, "", ""))
        self.assertEqual(self.head(), before)

    def test_only_non_tool_changes_on_origin_are_not_tool_sync_business(self):
        self.land("Merge pull request #5 from x/y", **{"_records_/note.md": "record v2\n", "_tools_/state/queue-state.json": "{\"n\": 1}\n"})
        before = self.head()
        r = self.sync()
        self.assertEqual((r.returncode, r.stdout), (0, ""))
        self.assertEqual(self.head(), before)
        self.assertEqual(self.read("_records_/note.md"), "record v1\n")

    def test_a_checkout_ahead_of_origin_is_left_alone(self):
        self.put(self.live, "_tools_/queue.py", "queue v1 plus a local commit\n")
        self.put(self.live, "_tools_/new_local_tool.py", "new\n")
        self.commit(self.live, "local work not landed yet")
        before = self.head()
        r = self.sync()
        self.assertEqual((r.returncode, r.stdout, r.stderr), (0, "", ""))
        self.assertEqual(self.head(), before)
        self.assertEqual(self.read("_tools_/queue.py"), "queue v1 plus a local commit\n")


class Sync(Repos):
    def test_behind_files_are_synced_in_one_commit_with_the_fixed_message(self):
        self.land("Merge pull request #7 from zachmesh/land/thing", **{"_tools_/queue.py": "queue v2\n", "_tools_/new_tool.py": "new\n",
                                                                         "_tools_/old_tool.py": None, "_records_/note.md": "record v2\n"})
        before = self.head()
        r = self.sync()
        self.assertEqual((r.returncode, r.stdout.strip(), r.stderr), (0, "synced 3 files", ""))
        self.assertEqual(self.read("_tools_/queue.py"), "queue v2\n")
        self.assertEqual(self.read("_tools_/new_tool.py"), "new\n")
        self.assertFalse((self.live / "_tools_/old_tool.py").exists())
        self.assertEqual(self.read("_records_/note.md"), "record v1\n")                  # not a tool: not synced
        self.assertEqual(self.git(self.live, "rev-list", "--count", f"{before}..HEAD"), "1")
        self.assertEqual(self.git(self.live, "log", "-1", "--format=%s"), "chore(tools): sync live tools from origin after PR 7")
        self.assertEqual(sorted(self.git(self.live, "show", "--name-only", "--format=", "HEAD").splitlines()),
                         ["_tools_/new_tool.py", "_tools_/old_tool.py", "_tools_/queue.py"])
        self.assertEqual(self.sync().stdout, "")                                          # the next tick is silent again
        self.assertEqual(self.git(self.live, "status", "--porcelain"), "")

    def test_the_newest_pr_in_the_range_names_the_commit_and_a_squash_subject_works(self):
        self.land("Merge pull request #7 from a/b", **{"_tools_/queue.py": "queue v2\n"})
        self.land("feat(tools): another (#12)", **{"_tools_/regulars.json": "{\"a\": 1}\n"})
        self.assertEqual(self.sync().stdout.strip(), "synced 2 files")
        self.assertEqual(self.git(self.live, "log", "-1", "--format=%s"), "chore(tools): sync live tools from origin after PR 12")

    def test_without_a_pr_number_the_origin_tip_is_named(self):
        self.land("tidy the tool", **{"_tools_/queue.py": "queue v2\n"})
        self.sync()
        tip = self.git(self.dev, "rev-parse", "--short=8", "HEAD")
        self.assertEqual(self.git(self.live, "log", "-1", "--format=%s"), f"chore(tools): sync live tools from origin after origin {tip}")

    def test_only_the_synced_paths_are_committed_other_work_in_the_checkout_is_untouched(self):
        self.land("Merge pull request #8 from a/b", **{"_tools_/queue.py": "queue v2\n"})
        self.put(self.live, "_records_/note.md", "record edited locally\n")
        self.put(self.live, "_records_/staged.md", "staged\n")
        self.git(self.live, "add", "_records_/staged.md")
        self.put(self.live, "_tools_/state/queue-state.json", "{\"local\": true}\n")
        self.assertEqual(self.sync().stdout.strip(), "synced 1 files")
        self.assertEqual(self.git(self.live, "show", "--name-only", "--format=", "HEAD").splitlines(), ["_tools_/queue.py"])
        self.assertEqual(self.read("_records_/note.md"), "record edited locally\n")
        self.assertIn("A  _records_/staged.md", self.git(self.live, "status", "--porcelain"))
        self.assertEqual(self.read("_tools_/state/queue-state.json"), "{\"local\": true}\n")

    def test_a_file_behind_is_synced_while_one_ahead_is_left_alone(self):
        self.put(self.live, "_tools_/regulars.json", "{\"mine\": 1}\n")
        self.commit(self.live, "local roster change")
        self.land("Merge pull request #9 from a/b", **{"_tools_/queue.py": "queue v2\n"})
        self.assertEqual(self.sync().stdout.strip(), "synced 1 files")
        self.assertEqual(self.read("_tools_/regulars.json"), "{\"mine\": 1}\n")
        self.assertEqual(self.read("_tools_/queue.py"), "queue v2\n")

    def test_a_dry_run_reports_and_changes_nothing(self):
        self.land("Merge pull request #7 from a/b", **{"_tools_/queue.py": "queue v2\n", "_tools_/new_tool.py": "n\n"})
        before = self.head()
        r = self.sync("--dry-run")
        self.assertEqual(r.returncode, 0)
        self.assertEqual(r.stdout.strip(), "would sync 2 files: _tools_/new_tool.py, _tools_/queue.py")
        self.assertEqual(self.head(), before)
        self.assertEqual(self.read("_tools_/queue.py"), "queue v1\n")

    def test_the_fetch_is_into_the_guards_private_ref_and_touches_no_remote_tracking_ref(self):
        tracking = self.git(self.live, "rev-parse", "refs/remotes/origin/main")
        self.land("Merge pull request #7 from a/b", **{"_tools_/queue.py": "queue v2\n"})
        self.sync("--dry-run")
        self.assertEqual(self.git(self.live, "rev-parse", GUARD_REF), self.git(self.dev, "rev-parse", "HEAD"))
        self.assertEqual(self.git(self.live, "rev-parse", "refs/remotes/origin/main"), tracking)
        self.assertEqual(self.git(self.live, "rev-parse", "--is-shallow-repository"), "false")


class Refusals(Repos):
    def refused(self, r, *names):
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("tool_sync refused", r.stdout)
        for name in names:
            self.assertIn(name, r.stdout)

    def test_an_uncommitted_change_to_a_file_to_sync_refuses_everything_and_overwrites_nothing(self):
        self.land("Merge pull request #7 from a/b", **{"_tools_/queue.py": "queue v2\n", "_tools_/regulars.json": "{\"a\": 1}\n"})
        self.put(self.live, "_tools_/queue.py", "queue v1 hand edited\n")
        before = self.head()
        r = self.sync()
        self.refused(r, "_tools_/queue.py (uncommitted local change)")
        self.assertNotIn("regulars.json", r.stdout)
        self.assertEqual(self.read("_tools_/queue.py"), "queue v1 hand edited\n")
        self.assertEqual(self.read("_tools_/regulars.json"), "{}\n")                         # all or nothing
        self.assertEqual(self.head(), before)

    def test_a_staged_change_and_an_untracked_file_in_the_way_both_refuse(self):
        self.land("Merge pull request #7 from a/b", **{"_tools_/queue.py": "queue v2\n", "_tools_/new_tool.py": "new\n"})
        self.put(self.live, "_tools_/queue.py", "staged edit\n")
        self.git(self.live, "add", "_tools_/queue.py")
        self.put(self.live, "_tools_/new_tool.py", "an untracked file already here\n")
        r = self.sync()
        self.refused(r, "_tools_/queue.py", "_tools_/new_tool.py")
        self.assertEqual(self.read("_tools_/new_tool.py"), "an untracked file already here\n")

    def test_a_diverged_file_refuses(self):
        self.put(self.live, "_tools_/queue.py", "queue local change\n")
        self.commit(self.live, "local change to queue")
        self.land("Merge pull request #7 from a/b", **{"_tools_/queue.py": "queue origin change\n"})
        r = self.sync()
        self.refused(r, "_tools_/queue.py (diverged: both changed)")
        self.assertEqual(self.read("_tools_/queue.py"), "queue local change\n")

    def test_a_checkout_on_another_branch_is_not_synced_onto(self):
        self.land("Merge pull request #7 from a/b", **{"_tools_/queue.py": "queue v2\n"})
        self.git(self.live, "checkout", "-q", "-b", "someone-elses-work")
        before = self.head()
        r = self.sync()
        self.assertEqual(r.returncode, 1)
        self.assertIn("is on someone-elses-work, not main", r.stdout)
        self.assertEqual(self.head(), before)
        self.assertEqual(self.sync("--branch", "someone-elses-work").stdout.strip(), "synced 1 files")


class GitErrors(Repos):
    def test_an_unreachable_remote_is_exit_two_and_changes_nothing(self):
        self.git(self.live, "remote", "set-url", "origin", str(self.tmp / "no-such-origin.git"))
        before = self.head()
        r = self.sync()
        self.assertEqual(r.returncode, 2, r.stdout + r.stderr)
        self.assertIn("tool_sync: git fetch failed", r.stderr)
        self.assertEqual((r.stdout, self.head()), ("", before))

    def test_no_remote_is_exit_two(self):
        self.git(self.live, "remote", "remove", "origin")
        r = self.sync()
        self.assertEqual(r.returncode, 2)
        self.assertIn("no git remote", r.stderr)

    def test_a_commit_the_gate_refuses_is_rolled_back_with_exit_two(self):
        hook = self.live / ".git" / "hooks" / "pre-commit"
        hook.write_text("#!/bin/sh\necho 'lint-gate: refused for a test' >&2\nexit 1\n")
        hook.chmod(0o755)
        self.land("Merge pull request #7 from a/b", **{"_tools_/queue.py": "queue v2\n", "_tools_/new_tool.py": "new\n", "_tools_/old_tool.py": None})
        before = self.head()
        r = self.sync()
        self.assertEqual(r.returncode, 2, r.stdout + r.stderr)
        self.assertIn("refused and rolled back", r.stderr)
        self.assertEqual(self.head(), before)
        self.assertEqual(self.read("_tools_/queue.py"), "queue v1\n")
        self.assertFalse((self.live / "_tools_/new_tool.py").exists())
        self.assertEqual(self.read("_tools_/old_tool.py"), "old\n")
        self.assertEqual(self.git(self.live, "status", "--porcelain"), "")
        hook.unlink()
        self.assertEqual(self.sync().stdout.strip(), "synced 3 files")                       # and the retry works once the gate allows it


if __name__ == "__main__":
    unittest.main()
