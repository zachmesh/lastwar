"""Tests for records_snapshot.py on scratch repositories whose local main and origin main are two diverged lines: a bare origin, a developer
clone that lands origin's side, and the live checkout holding local commits. A fake gate script stands in for lint_gate.py.

Run: python3 -m unittest discover -s _tools_/records-snapshot
"""
from __future__ import annotations

import os
import shutil
import stat
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOOL = HERE / "records_snapshot.py"
TOKEN = "zorblax"                      # made up: the fixture denylist matches it
FAKE_GATE = r'''
import os, sys
args = sys.argv[1:]
if args[:2] == ["check", "--help"]:
    print("usage: check [--staged] [--base REF] [--landing]" if not os.environ.get("FAKE_GATE_NO_LANDING") else "usage: check [--staged] [--base REF]")
elif "--staged" in args:
    if os.environ.get("FAKE_GATE_STAGED"):
        print("BLOCKED [fake] _records_/new-1.md: blocked for a test"); print("lint-gate: 1 blocking finding(s)"); sys.exit(1)
    print("lint-gate: ok (staged)")
elif "--landing" in args:
    if os.environ.get("FAKE_GATE_LANDING"):
        print("BLOCKED [fake] _records_/shared.md: landing refused for a test"); print("lint-gate: 1 blocking finding(s) (base)"); sys.exit(1)
    print("lint-gate: ok (base origin/main, 0.1s); privacy 1 pattern(s) over 0 added line(s).")
'''


class Lines(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="records-snapshot-test-"))
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.origin, self.dev, self.live = self.tmp / "origin.git", self.tmp / "dev", self.tmp / "live"
        self.gate = self.tmp / "fake_gate.py"
        self.gate.write_text(FAKE_GATE)
        subprocess.run(["git", "init", "-q", "--bare", "-b", "main", str(self.origin)], check=True)
        subprocess.run(["git", "clone", "-q", str(self.origin), str(self.dev)], check=True, capture_output=True)
        self.git(self.dev, "checkout", "-q", "-b", "main")
        for rel, text in {"_records_/INDEX.md": "# records\n", "_records_/shared.md": "shared v0\n", "_records_/both.md": "both v0\n",
                          "_records_/origin-only-changed.md": "oc v0\n", "_records_/deleted-locally.md": "dl v0\n", "_records_/ren-old.md": "ren v0\n", "_records_/ahead.md": "ahead v0\n", "_records_/oa.md": "oa v0\n",
                          "_activities_/alpha-one/run-old.md": "run article body kept private\n",
                          "_tools_/code.py": "code v0\n", "_tools_/state/queue-state.json": "{}\n", "_activities_/alpha-one/INDEX.md": "act v0\n",
                          "_knowledge_/page.md": "k v0\n"}.items():
            self.put(self.dev, rel, text)
        self.commit(self.dev, "C0")
        self.git(self.dev, "push", "-q", "origin", "main")
        subprocess.run(["git", "clone", "-q", str(self.origin), str(self.live)], check=True, capture_output=True)
        self.git(self.live, "checkout", "-q", "main")
        # origin's line: another seat's record, a changed file, a conflicting change, code and an activity page
        self.put(self.dev, "_records_/seat-x.md", "seat x record\n")
        self.put(self.dev, "_records_/origin-only-changed.md", "oc origin\n")
        self.put(self.dev, "_records_/both.md", "both origin\n")
        self.put(self.dev, "_records_/ahead.md", "ahead v1\n")                                            # origin holds my earlier snapshot of this file
        self.put(self.dev, "_records_/oa.md", "oa v1\n")
        self.commit(self.dev, "O1a")
        self.put(self.dev, "_records_/oa.md", "oa v2\n")                                                  # and has moved on from it
        self.git(self.dev, "mv", "_activities_/alpha-one/run-old.md", "_activities_/alpha-one/run-moved.md")      # origin moved a run article to _run_notes_
        (self.dev / "_run_notes_/alpha-one").mkdir(parents=True)
        self.git(self.dev, "mv", "_activities_/alpha-one/run-moved.md", "_run_notes_/alpha-one/run-old.md")
        self.put(self.dev, "_run_notes_/moved-paths/moved-paths.csv",
                 "old_path,new_path,record\n_activities_/alpha-one/run-old.md,_run_notes_/alpha-one/run-old.md,_records_/r.md\n")
        self.put(self.dev, "_tools_/code2.py", "code two\n")
        self.put(self.dev, "_activities_/alpha-one/INDEX.md", "act origin\n")
        self.commit(self.dev, "O1")
        self.git(self.dev, "push", "-q", "origin", "main")
        # local main's line: first the version origin later received, a new version of it, and an older version of oa.md
        self.put(self.live, "_records_/ahead.md", "ahead v1\n")
        self.put(self.live, "_records_/oa.md", "oa v1\n")
        self.commit(self.live, "L0")
        self.put(self.live, "_records_/ahead.md", "ahead v2\n")
        # local main's line: new records, a modified record, a conflicting change, a deletion, a rename, a binary, an executable, code, state
        self.put(self.live, "_records_/new-1.md", "new record one\n")
        (self.live / "_records_/pic.bin").write_bytes(b"\x89PNG\r\n\x00\x01\x02binary\xff")
        self.put(self.live, "_records_/run.sh", "#!/bin/sh\necho hi\n")
        (self.live / "_records_/run.sh").chmod(0o755)
        self.put(self.live, "_knowledge_/local-page.md", "local knowledge\n")
        self.put(self.live, "_records_/shared.md", "shared local\n")
        self.put(self.live, "_records_/both.md", "both local\n")
        (self.live / "_records_/deleted-locally.md").unlink()
        self.git(self.live, "mv", "_records_/ren-old.md", "_records_/ren-new.md")
        self.put(self.live, "_tools_/code.py", "code local\n")
        self.put(self.live, "_tools_/state/queue-state.json", "{\"n\": 1}\n")
        self.put(self.live, "_activities_/alpha-one/INDEX.md", "act local\n")
        self.commit(self.live, "L1")
        self.git(self.live, "fetch", "-q", "origin")
        (self.live / ".git" / "privacy-denylist.txt").write_text(f"# made-up fixture pattern\n{TOKEN}\n")

    def git(self, repo, *args, check=True):
        env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
        return subprocess.run(["git", "-C", str(repo), "-c", "user.email=t@e.org", "-c", "user.name=tester", *args], capture_output=True, text=True,
                              check=check, env=env).stdout.strip()

    def put(self, repo, rel, text):
        path = Path(repo) / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)

    def commit(self, repo, message):
        self.git(repo, "add", "-A")
        self.git(repo, "commit", "-q", "-m", message)

    def run_tool(self, *args, root=None, env=None):
        full = dict(os.environ, **(env or {}))
        return subprocess.run([sys.executable, "-B", str(TOOL), "--root", str(root or self.live), *args], capture_output=True, text=True, env=full)

    def snapshot(self, *args, env=None, **kw):
        return self.run_tool(*args[:0], "snapshot", "--gate", str(self.gate), *args, env=env, **kw)

    def show(self, rev, rel):
        return subprocess.run(["git", "-C", str(self.live), "show", f"{rev}:{rel}"], capture_output=True).stdout

    def refs(self, repo):
        return self.git(repo, "for-each-ref", "--format=%(refname) %(objectname)")


class Snapshot(Lines):
    def test_only_what_local_main_adds_or_changes_lands_on_the_origin_tip_and_nothing_is_deleted(self):
        before_status = self.git(self.live, "status", "--porcelain")
        main_before, origin_refs = self.git(self.live, "rev-parse", "main"), self.refs(self.origin)
        r = self.snapshot("--branch", "land/records-test", "--on-conflict", "main")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        b = "land/records-test"
        base = self.git(self.live, "rev-parse", "origin/main")
        self.assertEqual(self.git(self.live, "rev-parse", f"{b}^"), base)                          # one commit on the base tip
        self.assertEqual(self.git(self.live, "rev-list", "--count", f"{base}..{b}"), "1")
        # added and modified by local main, content intact
        self.assertEqual(self.show(b, "_records_/new-1.md"), b"new record one\n")
        self.assertEqual(self.show(b, "_records_/pic.bin"), b"\x89PNG\r\n\x00\x01\x02binary\xff")
        self.assertEqual(self.show(b, "_records_/ren-new.md"), b"ren v0\n")                        # a rename lands as an add of the new path
        self.assertEqual(self.show(b, "_records_/shared.md"), b"shared local\n")
        self.assertEqual(self.show(b, "_tools_/state/queue-state.json"), b"{\"n\": 1}\n")           # the state lands though _tools_ code is excluded
        self.assertEqual(self.show(b, "_knowledge_/local-page.md"), b"local knowledge\n")
        self.assertIn("100755", self.git(self.live, "ls-tree", b, "_records_/run.sh"))              # the mode survives
        # a change both lines made: a TRUE conflict, main's version because --on-conflict main was asked for
        self.assertEqual(self.show(b, "_records_/both.md"), b"both local\n")
        # origin held an earlier version of main's ahead.md: main ahead, applied without a conflict
        self.assertEqual(self.show(b, "_records_/ahead.md"), b"ahead v2\n")
        # origin is ahead of main on oa.md: skipped, origin's version stays
        self.assertEqual(self.show(b, "_records_/oa.md"), b"oa v2\n")
        # origin's own changes survive; nothing local overwrote them
        self.assertEqual(self.show(b, "_records_/origin-only-changed.md"), b"oc origin\n")
        self.assertEqual(self.show(b, "_records_/seat-x.md"), b"seat x record\n")
        self.assertEqual(self.show(b, "_tools_/code.py"), b"code v0\n")                            # excluded: code and activities stay as origin has them
        self.assertEqual(self.show(b, "_tools_/code2.py"), b"code two\n")
        self.assertEqual(self.show(b, "_activities_/alpha-one/INDEX.md"), b"act origin\n")
        # never a deletion: what main lacks but origin has is still there
        self.assertEqual(self.show(b, "_records_/deleted-locally.md"), b"dl v0\n")
        self.assertEqual(self.show(b, "_records_/ren-old.md"), b"ren v0\n")
        self.assertEqual(self.git(self.live, "diff", "--name-status", "--diff-filter=D", base, b), "")
        # counts, never content
        self.assertIn("files: A 5, M 4", r.stdout)
        self.assertIn("applied 7 | main ahead 1 (applied: origin holds an earlier version of main's) | true conflicts 1 (applied main's version) "
                      "| skipped: origin is newer 2", r.stdout)
        self.assertIn("parent is the base tip: yes", r.stdout)
        self.assertIn("files matching 0, file names 0, commit messages and authors 0", r.stdout)
        self.assertIn("landing check: ok (exit 0)", r.stdout)
        message = self.git(self.live, "log", "-1", "--format=%B", b)
        self.assertIn("A 5, M 4", message)
        self.assertIn("_records_ A 4 M 3", message)
        self.assertIn("main ahead 1", message)
        for text in ("new-1", "shared local", "pic.bin"):
            self.assertNotIn(text, message + r.stdout)
        # the live checkout is untouched: main, index, working tree, origin, and no scratch worktree left
        self.assertEqual(self.git(self.live, "rev-parse", "main"), main_before)
        self.assertEqual(self.git(self.live, "status", "--porcelain"), before_status)
        self.assertEqual(self.git(self.live, "diff", "--cached", "--name-only"), "")
        self.assertEqual(self.refs(self.origin), origin_refs)
        self.assertEqual(len(self.git(self.live, "worktree", "list").splitlines()), 1)

    def test_a_dry_run_reports_the_plan_and_creates_nothing(self):
        refs, status = self.refs(self.live), self.git(self.live, "status", "--porcelain")
        r = self.snapshot("--dry-run", "--on-conflict", "main")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("(dry run, nothing created): would land A 5, M 4", r.stdout)
        self.assertIn("_records_ A 4 M 3", r.stdout)
        self.assertIn("applied 7 | main ahead 1 (would apply:", r.stdout)
        self.assertIn("true conflicts 1 (would apply main's version)", r.stdout)
        self.assertEqual((self.refs(self.live), self.git(self.live, "status", "--porcelain")), (refs, status))
        self.assertEqual(len(self.git(self.live, "worktree", "list").splitlines()), 1)
        stop = self.snapshot("--dry-run")                                                                    # the default: a true conflict would stop it
        self.assertEqual(stop.returncode, 1)
        self.assertIn("true conflicts 1 (would stop)", stop.stdout)
        self.assertIn("true conflicts by folder: _records_ conflict 1", stop.stdout)

    def test_a_true_conflict_stops_the_run_by_default_and_can_keep_origins_version(self):
        r = self.snapshot("--branch", "land/s")
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("1 true conflict(s) - origin holds a version of a file that main's history never had", r.stdout)
        self.assertIn("main ahead 1 would have applied", r.stdout)
        self.assertIn("_records_ conflict 1", r.stdout)
        self.assertEqual(self.git(self.live, "branch", "--list", "land/s"), "")
        r = self.snapshot("--branch", "land/o", "--on-conflict", "origin")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertEqual(self.show("land/o", "_records_/both.md"), b"both origin\n")
        self.assertIn("files: A 5, M 3", r.stdout)
        self.assertIn("applied 7 | main ahead 1", r.stdout)
        self.assertIn("true conflicts 1 (kept origin's version)", r.stdout)

    def test_main_ahead_is_applied_silently_and_with_no_true_conflict_the_default_run_passes(self):
        self.git(self.live, "reset", "-q", "--hard", "HEAD")
        (self.live / "_records_/both.md").write_text("both origin\n")                                   # drop the one true conflict
        self.commit(self.live, "take origin's both.md")
        r = self.snapshot("--branch", "land/clean")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertEqual(self.show("land/clean", "_records_/ahead.md"), b"ahead v2\n")
        self.assertIn("main ahead 1 (applied: origin holds an earlier version of main's) | true conflicts 0 |", r.stdout)

    def test_the_default_branch_name_and_a_custom_exclude_that_replaces_the_defaults(self):
        r = self.snapshot("--exclude", "_knowledge_", "--on-conflict", "main")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        name = self.git(self.live, "branch", "--list", "land/records-*", "--format=%(refname:short)")
        self.assertRegex(name, r"^land/records-\d{8}T\d{6}Z$")
        self.assertEqual(self.show(name, "_tools_/code.py"), b"code local\n")                      # no longer excluded
        self.assertEqual(subprocess.run(["git", "-C", str(self.live), "cat-file", "-e", f"{name}:_knowledge_/local-page.md"], capture_output=True).returncode, 128)

    def test_a_denylist_match_in_a_file_a_name_or_an_author_fails_with_counts_only(self):
        self.put(self.live, "_records_/leak.md", f"this has {TOKEN} in it\n")
        self.put(self.live, f"_records_/{TOKEN}-name.md", "clean text\n")
        self.commit(self.live, "leak")
        r = self.snapshot("--branch", "land/leak", "--on-conflict", "main")
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("files matching 1, file names 1", r.stdout)
        self.assertNotIn(TOKEN, r.stdout + r.stderr)
        self.git(self.live, "branch", "-D", "land/leak")
        self.git(self.live, "config", "user.name", f"{TOKEN.title()} Person")
        (self.live / "_records_/leak.md").unlink()
        (self.live / f"_records_/{TOKEN}-name.md").unlink()
        self.commit(self.live, "clean again")

    def test_a_missing_denylist_is_not_a_pass(self):
        (self.live / ".git" / "privacy-denylist.txt").unlink()
        r = self.snapshot("--branch", "land/nodeny", "--on-conflict", "main")
        self.assertEqual(r.returncode, 1)
        self.assertIn("denylist scan: NOT RUN", r.stdout)

    def test_the_gate_blocking_the_staged_files_stops_before_any_commit_and_leaves_no_branch(self):
        r = self.snapshot("--branch", "land/blocked", "--on-conflict", "main", env={"FAKE_GATE_STAGED": "1"})
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("the gate blocks 1 staged finding(s); nothing was committed", r.stdout)
        self.assertEqual(self.git(self.live, "branch", "--list", "land/blocked"), "")
        self.assertEqual(len(self.git(self.live, "worktree", "list").splitlines()), 1)

    def test_a_failing_or_missing_landing_check_is_not_a_pass(self):
        r = self.snapshot("--branch", "land/f", "--on-conflict", "main", env={"FAKE_GATE_LANDING": "1"})
        self.assertEqual(r.returncode, 1)
        self.assertIn("landing check: FAILED (exit 1)", r.stdout)
        self.assertIn("BLOCKED [fake] _records_/shared.md", r.stdout)
        r = self.snapshot("--branch", "land/n", "--on-conflict", "main", env={"FAKE_GATE_NO_LANDING": "1"})
        self.assertEqual(r.returncode, 1)
        self.assertIn("landing check: NOT RUN - the gate has no --landing form", r.stdout)

    def test_refusals(self):
        self.git(self.live, "checkout", "-q", "-b", "elsewhere")
        r = self.snapshot("--branch", "land/x")
        self.assertEqual(r.returncode, 1)
        self.assertIn("the working branch is elsewhere, not main", r.stdout)
        self.git(self.live, "checkout", "-q", "main")
        self.git(self.live, "branch", "land/taken")
        r = self.snapshot("--branch", "land/taken")
        self.assertIn("the branch land/taken already exists", r.stdout)
        r = self.snapshot("--base", "origin/nope", "--branch", "land/y") if False else self.run_tool("--base", "origin/nope", "snapshot", "--gate", str(self.gate))
        self.assertEqual(r.returncode, 1)
        self.assertIn("does not resolve", r.stdout)
        shallow = self.tmp / "shallow"
        subprocess.run(["git", "clone", "-q", "--depth", "1", f"file://{self.origin}", str(shallow)], check=True, capture_output=True)
        r = self.run_tool("snapshot", "--gate", str(self.gate), root=shallow)
        self.assertEqual(r.returncode, 1)
        self.assertIn("this clone is shallow", r.stdout)

    def test_nothing_to_land_when_main_adds_nothing(self):
        clone = self.tmp / "same"
        subprocess.run(["git", "clone", "-q", str(self.origin), str(clone)], check=True, capture_output=True)
        r = self.run_tool("snapshot", "--gate", str(self.gate), root=clone)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("nothing to land", r.stdout)
        self.assertEqual(self.git(clone, "branch", "--list", "land/*"), "")


class Converge(Lines):
    def make_equal_records(self):
        """local main differs from origin only in the excluded paths: drop the records commit and keep the code and activity edits."""
        self.git(self.live, "reset", "-q", "--hard", "HEAD~1")
        self.put(self.live, "_tools_/code.py", "code local\n")
        self.put(self.live, "_activities_/alpha-one/INDEX.md", "act local\n")
        self.commit(self.live, "L1 code only")
        # origin's O1 changed both.md and origin-only-changed.md: make local main hold origin's records at those paths
        self.put(self.live, "_records_/both.md", "both origin\n")
        self.put(self.live, "_records_/origin-only-changed.md", "oc origin\n")
        self.put(self.live, "_records_/oa.md", "oa v2\n")
        self.commit(self.live, "records equal origin")

    def test_converges_main_to_origin_without_touching_the_working_tree(self):
        self.make_equal_records()
        self.put(self.live, "_records_/shared.md", "shared work in progress\n")                     # another seat's uncommitted work
        self.put(self.live, "_records_/seat-x.md", "seat x record\n")                                  # untracked here, tracked on origin
        old = self.git(self.live, "rev-parse", "main")
        tree_before = (self.live / "_tools_/code.py").read_text(), (self.live / "_records_/shared.md").read_text()
        r = self.run_tool("converge")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        new = self.git(self.live, "rev-parse", "origin/main")
        self.assertEqual(self.git(self.live, "rev-parse", "main"), new)
        backups = self.git(self.live, "for-each-ref", "--format=%(refname) %(objectname)", "refs/backup/")
        self.assertIn(old, backups)
        self.assertEqual(self.git(self.live, "diff", "--cached", "--name-only"), "")                  # the index follows the new main
        self.assertEqual((self.live / "_tools_/code.py").read_text(), tree_before[0])                  # the working tree is untouched
        self.assertEqual((self.live / "_records_/shared.md").read_text(), tree_before[1])
        differing = [l for l in self.git(self.live, "diff", "--name-only").splitlines() if l]
        self.assertIn("_tools_/code.py", differing)
        self.assertIn("_records_/shared.md", differing)
        self.assertNotIn("_records_/seat-x.md", differing)                                             # identical to origin's: not a difference
        self.assertIn(f"tracked paths that now differ from the index: {len(differing)}", r.stdout)
        self.assertIn(f"main moved from {old[:8]} to {new[:8]}", r.stdout)
        self.assertEqual(self.run_tool("converge").stdout.strip(), "records_snapshot converge: main already is the base")

    def test_refuses_when_a_non_excluded_tracked_file_differs_and_changes_nothing(self):
        r = self.run_tool("converge")                                                                    # L1 changed records: shared, both, new, ...
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("converge refused:", r.stdout)
        self.assertIn("_records_ differs", r.stdout)
        self.assertIn("_knowledge_ differs 1", r.stdout)
        self.assertNotIn("code.py", r.stdout)
        self.assertNotEqual(self.git(self.live, "rev-parse", "main"), self.git(self.live, "rev-parse", "origin/main"))
        self.assertEqual(self.git(self.live, "for-each-ref", "refs/backup/"), "")

    def test_a_dry_run_changes_nothing_and_the_exclude_list_is_honoured(self):
        self.make_equal_records()
        before = self.git(self.live, "rev-parse", "main")
        r = self.run_tool("converge", "--dry-run")
        self.assertEqual(r.returncode, 0, r.stdout)
        self.assertIn("would move main", r.stdout)
        self.assertEqual(self.git(self.live, "rev-parse", "main"), before)
        r = self.run_tool("--exclude", "_records_", "converge", "--dry-run")                          # now the code differs and is not excluded
        self.assertEqual(r.returncode, 1)
        self.assertIn("_tools_ differs", r.stdout)

    def test_refuses_off_main_and_in_a_shallow_clone(self):
        self.make_equal_records()
        self.git(self.live, "checkout", "-q", "-b", "elsewhere")
        r = self.run_tool("converge")
        self.assertEqual(r.returncode, 1)
        self.assertIn("not main", r.stdout)
        shallow = self.tmp / "shallow"
        subprocess.run(["git", "clone", "-q", "--depth", "1", f"file://{self.origin}", str(shallow)], check=True, capture_output=True)
        self.assertIn("shallow", self.run_tool("converge", root=shallow).stdout)


class ConvergeNewer(Lines):
    def make_newer_only(self, restore_deleted=True):
        """Local main differs from origin only by newer local content: take origin's version where origin holds one main never had, and (by
        default) bring back what main deleted that origin holds."""
        for rel in ("_records_/both.md", "_records_/oa.md", "_records_/origin-only-changed.md") + (
                ("_records_/deleted-locally.md", "_records_/ren-old.md") if restore_deleted else ()):
            self.put(self.live, rel, self.git(self.live, "show", f"origin/main:{rel}") + "\n")
        self.commit(self.live, "take origin's versions" + (", restore what main deleted" if restore_deleted else ""))

    def hashes(self):
        out = {}
        for p in sorted(self.live.rglob("*")):
            rel = p.relative_to(self.live).as_posix()
            if p.is_file() and not rel.startswith(".git/"):
                out[rel] = p.read_bytes()
        return out

    def test_refuses_a_true_conflict_and_a_file_main_deleted_that_origin_holds(self):
        r = self.run_tool("converge", "--accept-newer")
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("3 true conflict(s) - origin holds a version main's history never had; by folder: _records_ conflict 3", r.stdout)
        self.assertIn("2 file(s) origin holds that main deleted, which converge would bring back; by folder: _records_ main-deleted 2", r.stdout)
        self.assertNotEqual(self.git(self.live, "rev-parse", "main"), self.git(self.live, "rev-parse", "origin/main"))
        self.assertEqual(self.git(self.live, "for-each-ref", "refs/backup/"), "")

    def test_a_dry_run_changes_nothing_and_reports_the_same_counts_as_the_real_run(self):
        self.make_newer_only()
        refs, status, cached = self.refs(self.live), self.git(self.live, "status", "--porcelain"), self.git(self.live, "diff", "--cached", "--name-only")
        dry = self.run_tool("converge", "--accept-newer", "--dry-run")
        self.assertEqual(dry.returncode, 0, dry.stdout + dry.stderr)
        self.assertIn("(dry run): no true conflict, no refused deletion", dry.stdout)
        self.assertEqual((self.refs(self.live), self.git(self.live, "status", "--porcelain"), self.git(self.live, "diff", "--cached", "--name-only")),
                         (refs, status, cached))
        real = self.run_tool("converge", "--accept-newer")
        self.assertEqual(real.returncode, 0, real.stdout + real.stderr)
        count_line = lambda out, key: next(l for l in out.splitlines() if key in l).split("relative to the new HEAD")[0].split("tracked paths now ")[1]
        self.assertEqual(count_line(dry.stdout, "tracked paths now"), count_line(real.stdout, "tracked paths now"))

    def test_converges_main_keeps_every_file_byte_for_byte_and_reports_the_moved_old_paths(self):
        self.make_newer_only()
        old = self.git(self.live, "rev-parse", "main")
        before = self.hashes()
        r = self.run_tool("converge", "--accept-newer")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        new = self.git(self.live, "rev-parse", "origin/main")
        self.assertEqual(self.git(self.live, "rev-parse", "main"), new)
        self.assertIn(old, self.git(self.live, "for-each-ref", "--format=%(refname) %(objectname)", "refs/backup/"))
        self.assertEqual(self.git(self.live, "diff", "--cached", "--name-only"), "")                      # the index follows the new main
        self.assertEqual(self.hashes(), before)                                                          # the working tree is byte for byte what it was
        status = subprocess.run(["git", "-C", str(self.live), "status", "--porcelain", "--untracked-files=all"], capture_output=True, text=True).stdout.splitlines()
        self.assertIn("?? _activities_/alpha-one/run-old.md", status)                                    # the old path of the moved run article
        self.assertIn(" M _records_/shared.md", status)                                                 # newer local content, now a modification
        self.assertIn("?? _records_/new-1.md", status)
        self.assertIn(" D _run_notes_/alpha-one/run-old.md", status)                                    # origin's new path, not in this working tree
        self.assertIn("untracked files at an OLD path of _run_notes_/moved-paths/moved-paths.csv: 1 (counted, never deleted)", r.stdout)
        untracked = sum(1 for l in status if l.startswith("??"))
        modified = sum(1 for l in status if l.startswith(" M"))
        missing = sum(1 for l in status if l.startswith(" D"))
        self.assertIn(f"tracked paths now modified {modified}, missing {missing}, untracked {untracked} relative to the new HEAD", r.stdout)
        self.assertIn("_activities_ ", r.stdout)
        for text in ("shared local", "new record one", "kept private"):
            self.assertNotIn(text, r.stdout)                                                             # counts only
        self.assertEqual(self.run_tool("converge", "--accept-newer").stdout.strip(), "records_snapshot converge: main already is the base")

    def test_a_file_main_deleted_that_origin_holds_can_be_accepted_by_prefix_and_shows_as_missing(self):
        self.make_newer_only(restore_deleted=False)
        refused = self.run_tool("converge", "--accept-newer", "--dry-run")
        self.assertEqual(refused.returncode, 1)
        self.assertIn("2 file(s) origin holds that main deleted", refused.stdout)
        partial = self.run_tool("converge", "--accept-newer", "--dry-run", "--accept-main-deleted", "_records_/deleted-locally.md")
        self.assertEqual(partial.returncode, 1)
        self.assertIn("1 file(s) origin holds that main deleted", partial.stdout)
        before = self.hashes()
        ok = self.run_tool("converge", "--accept-newer", "--accept-main-deleted", "_records_/deleted-locally.md", "--accept-main-deleted", "_records_/ren-old.md")
        self.assertEqual(ok.returncode, 0, ok.stdout + ok.stderr)
        self.assertIn("2 origin file(s) main deleted were accepted by --accept-main-deleted (by folder: _records_ accepted 2) and show as missing", ok.stdout)
        status = subprocess.run(["git", "-C", str(self.live), "status", "--porcelain"], capture_output=True, text=True).stdout.splitlines()
        self.assertIn(" D _records_/deleted-locally.md", status)
        self.assertIn(" D _records_/ren-old.md", status)
        self.assertEqual(self.hashes(), before)                                                          # still nothing was deleted or restored on disk

    def test_excluded_paths_are_not_judged_unless_the_exclude_list_says_so(self):
        self.make_newer_only()
        self.put(self.dev, "_tools_/code.py", "code origin\n")
        self.commit(self.dev, "origin changes code")
        self.git(self.dev, "push", "-q", "origin", "main")
        self.git(self.live, "fetch", "-q", "origin")
        ok = self.run_tool("converge", "--accept-newer", "--dry-run")
        self.assertEqual(ok.returncode, 0, ok.stdout + ok.stderr)                                        # _tools_ code is excluded by default
        strict = self.run_tool("--exclude", "_knowledge_", "converge", "--accept-newer", "--dry-run")
        self.assertEqual(strict.returncode, 1)
        self.assertIn("_tools_ conflict 1", strict.stdout)

    def test_the_plain_converge_is_unchanged_and_still_refuses_any_difference(self):
        self.make_newer_only()
        r = self.run_tool("converge", "--dry-run")
        self.assertEqual(r.returncode, 1)
        self.assertIn("converge refused:", r.stdout)


if __name__ == "__main__":
    unittest.main()
