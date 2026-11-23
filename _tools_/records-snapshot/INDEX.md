---
title: Records Snapshot
created: 2026-11-23T10:22:29Z
modified: 2026-11-23T10:33:43Z
version: 1.2.0
description: records_snapshot.py, which lands the records the live checkout holds without a merge, and converges local main with origin
---

# Records snapshot

Local main and origin main are different lines and other seats' records are untracked in the live checkout, so a merge conflicts in
hundreds of files. This tool never merges, pushes, or touches the live index or working tree except `converge`'s mixed reset.

`python3 _tools_/records-snapshot/records_snapshot.py snapshot [--base origin/main] [--branch NAME] [--exclude PATH ...] [--on-conflict stop|main|origin] [--dry-run]`

- Refuses unless the clone is whole and the branch is main. Copies what local main adds or modifies (a rename is an add; plus
  `_tools_/state/`; never a deletion) onto a scratch worktree of a branch on the base tip. Default excludes: `_tools_` code and
  `_activities_`; any `--exclude` replaces them.
- Against the merge base: only main changed it, apply; only origin, skip. Changed on both lines: origin's blob already in main's
  history is main ahead (apply); main's blob in origin's history is origin ahead (skip); else a true conflict (`stop` by default).
- One commit through the gate, a counts-only message, then applied, main ahead and true conflicts, the whole-tree denylist scan,
  the landing check, parent equals base. Exit 0 only when all pass. The branch stays; the worktree goes.

`converge [--dry-run]`: when every tracked file of main outside the excludes equals origin's, move `main` to the base (`update-ref`,
mixed `reset`), keep the old tip under `refs/backup/`, print how many paths then differ; else refuse with counts by folder.

`converge --accept-newer [--accept-main-deleted PREFIX]`: also when every difference is newer local content. Refuses a true conflict
and an origin file main deleted (queue units that moved state: accept by prefix). Then counts of tracked paths modified, missing or
untracked by folder, and untracked files at an old path of `_run_notes_/moved-paths/moved-paths.csv`; nothing deleted.

Tests (two diverged lines): `python3 -m unittest discover -s _tools_/records-snapshot`.
