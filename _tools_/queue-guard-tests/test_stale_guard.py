"""Tests for the stale-tool guard of queue.py (issue 694): refuse only when main's copy is newer than this one or the two
histories diverged; a copy that is ahead of main runs, with a warning naming both blobs. Each case is a fake remote (a
bare repository), a live clone holding queue.py, and a second clone that plays the other author. Nothing touches the real
repository or pool.

Run: python3 -m unittest discover -s _tools_/queue-guard-tests
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

QUEUE = Path(__file__).resolve().parent.parent / "queue.py"


def git(cwd, *args, check=True):
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    return subprocess.run(["git", "-C", str(cwd), "-c", "user.email=t@example.org", "-c", "user.name=t", *args],
                          capture_output=True, text=True, check=check, env=env)


def blob(text: str) -> str:
    return subprocess.run(["git", "hash-object", "--stdin"], input=text.encode(), capture_output=True).stdout.decode().strip()


class GuardCase(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="stale-guard-", dir="/tmp"))
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.origin = self.tmp / "origin.git"
        subprocess.run(["git", "init", "-q", "--bare", "-b", "main", str(self.origin)], check=True)
        seed = self.tmp / "seed"
        subprocess.run(["git", "init", "-q", "-b", "main", str(seed)], check=True)
        (seed / "_tools_").mkdir()
        shutil.copy(QUEUE, seed / "_tools_" / "queue.py")
        for state in ("inbox", "claimed", "done"):
            (seed / "_queue_" / state).mkdir(parents=True)
            (seed / "_queue_" / state / ".gitkeep").write_text("")
        git(seed, "add", "-A")
        git(seed, "commit", "-q", "-m", "seed")
        git(seed, "remote", "add", "origin", str(self.origin))
        git(seed, "push", "-q", "origin", "main")
        self.other = self.clone("other")
        self.live = self.clone("live")
        self.env = dict(os.environ, LASTWAR_QUEUE_ALLOW_TMP_ROOT="1")
        self.env.pop("LASTWAR_QUEUE_ALLOW_STALE_TOOL", None)

    def clone(self, name, *extra):
        path = self.tmp / name
        subprocess.run(["git", "clone", "-q", *extra, str(self.origin) if not extra else f"file://{self.origin}", str(path)],
                       check=True, capture_output=True)
        return path

    def tool(self, repo):
        return repo / "_tools_" / "queue.py"

    def edit(self, repo, marker):
        path = self.tool(repo)
        path.write_text(path.read_text() + f"\n# {marker}\n")

    def commit(self, repo, marker):
        self.edit(repo, marker)
        git(repo, "commit", "-q", "-am", marker)

    def push(self, repo):
        git(repo, "push", "-q", "origin", "main")

    def run_queue(self, repo, *args, env=None):
        return subprocess.run([sys.executable, "-B", str(self.tool(repo)), "--root", str(repo / "_queue_"), *args],
                              capture_output=True, text=True, env=env or self.env, cwd=str(repo))

    def enqueue(self, repo=None, env=None):
        return self.run_queue(repo or self.live, "enqueue", "--regular", "daily-activities", "--activity", "daily-activities",
                              "--est-minutes", "5", env=env)


class States(GuardCase):
    def test_equal_runs_without_a_warning(self):
        r = self.enqueue()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertNotIn("ahead", r.stderr)
        self.assertNotIn("refused", r.stdout + r.stderr)

    def test_ahead_by_a_local_commit_runs_and_names_both_blobs(self):
        origin_blob = git(self.live, "rev-parse", "HEAD:_tools_/queue.py").stdout.strip()
        self.commit(self.live, "held before it landed")
        local_blob = git(self.live, "rev-parse", "HEAD:_tools_/queue.py").stdout.strip()
        self.assertNotEqual(origin_blob, local_blob)
        r = self.enqueue()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("is ahead of main's", r.stderr)
        self.assertIn(f"blob {local_blob[:10]}", r.stderr)
        self.assertIn(f"blob {origin_blob[:10]}", r.stderr)
        self.assertNotIn("refused", r.stdout + r.stderr)

    def test_ahead_by_an_uncommitted_edit_runs_too(self):
        self.edit(self.live, "edited, not committed")
        r = self.enqueue()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("is ahead of main's", r.stderr)

    def test_behind_is_refused(self):
        self.commit(self.other, "landed on main by someone else")
        self.push(self.other)
        r = self.enqueue()
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("enqueue refused", r.stderr)
        self.assertIn("not ahead of it", r.stderr)
        self.assertEqual(list((self.live / "_queue_" / "inbox").glob("*.md")), [])      # nothing was queued

    def test_diverged_is_refused(self):
        self.commit(self.live, "my change")
        self.commit(self.other, "their change")
        self.push(self.other)
        r = self.enqueue()
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("histories diverged", r.stderr)

    def test_a_live_copy_that_pulls_the_newer_main_runs_again(self):
        self.commit(self.other, "landed")
        self.push(self.other)
        self.assertEqual(self.enqueue().returncode, 1)
        git(self.live, "pull", "-q", "--ff-only")
        r = self.enqueue()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertNotIn("ahead", r.stderr)

    def test_the_guard_leaves_the_clone_whole_and_origin_main_untouched(self):
        self.commit(self.other, "landed")
        self.push(self.other)
        before = git(self.live, "rev-parse", "origin/main").stdout.strip()
        self.enqueue()
        self.assertEqual(git(self.live, "rev-parse", "--is-shallow-repository").stdout.strip(), "false")
        self.assertEqual(git(self.live, "rev-parse", "origin/main").stdout.strip(), before)     # only the private ref moved
        self.assertNotEqual(git(self.live, "rev-parse", "refs/queue-fresh/main").stdout.strip(), before)
        self.assertEqual(git(self.live, "rev-list", "--count", "main..refs/queue-fresh/main").stdout.strip(), "1")

    def test_an_unreadable_origin_warns_and_proceeds(self):
        git(self.live, "remote", "set-url", "origin", str(self.tmp / "gone.git"))
        r = self.enqueue()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("fetch of main failed, tool-currency check skipped", r.stderr)

    def test_no_remote_at_all_warns_and_proceeds(self):
        git(self.live, "remote", "remove", "origin")
        r = self.enqueue()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("no git remote, tool-currency check skipped", r.stderr)

    def test_the_environment_escape_still_works_when_behind(self):
        self.commit(self.other, "landed")
        self.push(self.other)
        env = dict(self.env, LASTWAR_QUEUE_ALLOW_STALE_TOOL="1")
        r = self.enqueue(env=env)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("LASTWAR_QUEUE_ALLOW_STALE_TOOL=1, tool-currency check bypassed", r.stderr)


class ShallowAndVersion(GuardCase):
    def test_a_shallow_live_clone_that_is_ahead_still_runs(self):
        self.commit(self.other, "second version on main")
        self.push(self.other)
        shallow = self.clone("shallow", "--depth", "1")
        self.assertTrue(git(shallow, "rev-parse", "--is-shallow-repository").stdout.strip() == "true")
        self.commit(shallow, "ahead of main, shallow history")
        r = self.enqueue(shallow)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("is ahead of main's", r.stderr)

    def test_a_shallow_live_clone_that_is_behind_is_refused(self):
        shallow = self.clone("shallow", "--depth", "1")
        self.commit(self.other, "newer on main")
        self.push(self.other)
        r = self.enqueue(shallow)
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)

    def test_the_version_command_reports_ahead_stale_and_current(self):
        def currency(repo):
            r = self.run_queue(repo, "version", "--format", "json")
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
            return json.loads(r.stdout)["currency"]
        self.assertEqual(currency(self.live), "current")
        self.commit(self.live, "ahead")
        self.assertEqual(currency(self.live), "ahead")
        self.commit(self.other, "behind")
        self.push(self.other)
        self.assertEqual(currency(self.live), "stale")                      # diverged now

    def test_blob_ids_in_the_warning_are_git_blob_ids(self):
        self.commit(self.live, "ahead")
        text = self.tool(self.live).read_text()
        r = self.enqueue()
        self.assertIn(f"blob {blob(text)[:10]}", r.stderr)


if __name__ == "__main__":
    unittest.main()
