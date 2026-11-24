---
title: Bridge Tests
created: 2026-11-23T07:10:00Z
modified: 2026-11-24T01:17:44Z
version: 1.6.0
description: Tests for the computer-use bridge daemon lifecycle, run against a fake MCP server in a temporary copy
---

# Bridge tests

Tests for IMP-20261123-07 (a restart left an orphan daemon and a stuck run). Each test copies `cu_bridge.py` into a temporary tree under
/tmp and points it at a fake MCP server, so no real server, device or run is touched. Waits are on conditions, never a guessed sleep, and
the fake server runs under a seat name of its own. Every test is skipped while `_queue_/claimed/` of this checkout or the main one holds a
file; `CU_TESTS_IGNORE_LIVE_RUN=1` runs them anyway.

`test_cu_bridge.py`: a restart during a run ends the old daemon and its MCP child; a second `serve` refuses; `ensure` never starts a second
daemon while one is busy; `status` lists every daemon and run; `control stop` reaches the owning daemon or ends an unreachable one; SIGTERM
cleans up the child.

`test_desktop_lock.py`: the bridge reads the computer-use desktop-run lock before `start` (read-only, through `run-lock.mjs status`): a free
desktop starts; a live run, hold or waiter refuses once, with a retry-later report and no wait or break; an orphan entry is refused unless
`--accept-orphan`; the default seat is `cu-lastwar` and a `CU_SEAT` the lock would refuse stops `start`. Fakes stand in.

`test_owner_idle.py`: the owner-idle value: the launcher line `LAUNCHER_OWNER_IDLE_SECONDS` (None since the CU-721 tree move ended OD-20261123-27),
an explicit `CU_OWNER_IDLE_SECONDS` that wins when the tree reads it, else 300. The daemon prints `owner_idle_seconds=N (source: launcher | env |
default)` at start; `ensure`, `restart`, `status` and `runs` show its own value; a tree whose run-lock has no override (main's) ignores both, and the
report says so.

`test_project_path.py`: the tree the bridge runs (CU-721): the default is the worktree under `~/dtadpole/computer-use-wt/`, not the pinned checkout;
`CU_PROJECT` overrides it; the daemon prints, records and shows `project=PATH (source: env | default)`; a missing default refuses to start.

Run: `python3 -m unittest discover -s _tools_/cu-bridge-tests`.
