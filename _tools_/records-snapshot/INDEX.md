---
title: Records Snapshot
created: 2026-11-23T10:22:29Z
modified: 2026-11-23T10:27:28Z
version: 1.1.0
description: records_snapshot.py, which lands the records the live checkout holds without a merge, and converges local main with origin
---

# Records snapshot

Local main and origin main are different lines and other seats' records are untracked in the live checkout, so a merge conflicts in
hundreds of files. `snapshot` builds a branch on the origin tip and copies onto it only what local main adds or changes.

`python3 _tools_/records-snapshot/records_snapshot.py snapshot [--base origin/main] [--branch NAME] [--exclude PATH ...] [--on-conflict stop|main|origin] [--dry-run]`

- Refuses unless the clone is whole and the working branch is main. Never pushes, never touches main, the index or the working tree.
- Takes added and modified files from local main (a rename is an add) outside the excludes, plus `_tools_/state/`. Never deletes.
  Default excludes: `_tools_` code and `_activities_`; any `--exclude` replaces them.
- Judged against the merge base: only main changed it, apply; only origin changed it, skip. Changed on both lines: if origin's blob is
  already in main's history of the file, main is ahead (origin holds an earlier snapshot): apply, no conflict; if main's blob is in
  origin's history, origin is ahead: skip; otherwise a TRUE conflict, and `--on-conflict stop` (the default) ends the run (or `main`,
  `origin`). Origin deleted it: skip. Reports applied, main ahead, true conflicts.
- One commit through the gate with a counts-only message, then counts: files by status and folder, the whole-tree denylist scan (text,
  names, messages, authors), the landing check, parent equals base. Exit 0 only when the scan is 0, the landing check passes and the
  parent is the base. The scratch worktree goes; the branch stays.

`converge [--dry-run]`: when every tracked file of local main outside the excludes equals origin's, moves `main` to the base with
`update-ref` and a mixed `reset`, keeps the old tip under `refs/backup/`, and prints how many tracked paths then differ; otherwise
refuses with counts by folder.

Tests (two diverged lines): `python3 -m unittest discover -s _tools_/records-snapshot`.
