---
title: Tool Sync
created: 2026-11-23T09:55:32Z
modified: 2026-11-23T09:55:32Z
version: 1.0.0
description: tool_sync.py, the silent first step of every tick that brings the live checkout's tools up to origin main
---

# Tool sync

The queue's tool-currency guard (issue 694) refuses `next`, `enqueue`, `sync`, `plan` and `sweep` while the live copy of `queue.py`
differs from main's and is not ahead of it. Every PR that changed `queue.py` stopped the planner until the live checkout was synced
by hand. `tool_sync.py` is that sync, run as the first step of every tick; it prints nothing when there is nothing to do.

`python3 _tools_/tool-sync/tool_sync.py [--dry-run] [--branch main] [--root R] [--remote NAME]`

1. Fetch origin main into the guard's private ref `refs/queue-fresh/main` (whole, no tags, no remote-tracking ref touched).
2. List the files under `_tools_/` (not `_tools_/state/`) that differ from HEAD and classify each by its own history: behind (origin is
   newer: sync), ahead (this checkout's own later version or a local-only file: leave), diverged (both changed).
3. If no file to sync has an uncommitted change (staged, unstaged or an untracked file in the way), check them out from origin and
   commit only those paths through the repo's own hooks as `chore(tools): sync live tools from origin after PR N`.
4. Otherwise refuse and print the file names; nothing is overwritten. A commit the gate refuses is rolled back.

Prints `synced N files`, or nothing when equal or only ahead. Exit 0 equal or synced, 1 refused (a local change, a diverged file, or a
branch other than `--branch`), 2 a git error. `--dry-run` prints `would sync` and changes nothing.

Tests (a bare origin, a developer clone, a live clone): `python3 -m unittest discover -s _tools_/tool-sync`.
