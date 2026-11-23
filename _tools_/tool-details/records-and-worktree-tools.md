---
title: Records and worktree tools
created: 2026-11-23T04:53:59Z
modified: 2026-11-23T04:53:59Z
version: 1.0.0
description: Verbatim index rows for observation.py, retro_report.py, log_append.py, live_checkout_check.py, pass_worktree.py
---

# Records and worktree tools

Moved verbatim from the former `_tools_/INDEX.md` table; only link destinations are adjusted for this folder. Back to the [tool index](../INDEX.md).

| Tool | Purpose | Data |
|---|---|---|
| [observation.py](../observation.py) | Append-only writer and checker for the day observation file (issue #668): `append` appends one `## Pass ...` section and computes the new day counters as the per-field maximum of the live file and the delivered branch copy plus the unit's deltas, refuses a heading that already exists (a continued pass is a NEW section, never a replacement), refuses a negative cumulative delta, and restores any delivered pass section missing from the live file before appending, so a stale live copy heals at write time instead of dropping the earlier pass; `check` flags a missing delivered section, a duplicate heading, and a cumulative counter below the delivered copy; exit 0 ok, 1 problem/refused, 2 unreadable | `_records_/<date>/perception-scout/observation.md` |
| [retro_report.py](../retro_report.py) | Aggregate queue results into review metrics; the summed attainment excludes star-ceremony achieved figures that are duel screen totals, counted under achieved_screen_excluded (issue #483); points on trucks units are excluded as Handbook-rate expected scores, counted under points_expected_excluded (issue #300); points beside a string achieved naming the same total are excluded as running-total copies, counted under points_string_achieved_excluded (issue #672) | `../_queue_/` and `../_records_/retro/` |
| [log_append.py](../log_append.py) | Newline-safe append, check and repair for JSONL logs | `_logs_/repo-actions/action-log.jsonl` |
| [live_checkout_check.py](../live_checkout_check.py) | Check the live checkout's tools against main's `_tools_/` code tree and report drift loudly (issue #415); exit 0 in sync, 1 drifted, 2 cannot run | `~/workspace/lastwar` (live checkout) |
| [pass_worktree.py](../pass_worktree.py) | Create, list and prune pass worktrees under `~/workspace/lastwar-worktrees/`, refusing any target under the system temp directory (issue #429); `sync` refreshes a pass worktree's `_activities_` and `_conventions_` trees from the fresh tip of main (fetched from `github` by default) so an executor never plays against a superseded profile (issue #631); sync refuses only a file it would overwrite whose disk content differs from both the index and main, updates the working tree only (never the index), restores files missing on disk, leaves files main does not have alone, and re-verifies every refreshed file against the source blob before reporting; exit 0 synced or already in sync, 1 git or verification failure, 2 cannot run; `create` with an explicit `--base` reuses an existing branch only when its tip is the base and refuses a stale branch, exit 2 (issue #709), while without `--base` an existing branch is checked out as-is | `~/workspace/lastwar-worktrees/` |
