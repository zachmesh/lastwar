---
title: Repository Tools
created: 2026-11-01T07:58:31Z
modified: 2026-11-01T07:58:31Z
version: 1.0.0
description: Executable helpers, configuration and runtime state
---

# Repository tools

Run commands from the repository root with Python 3. These helpers use the
standard library and locate their data relative to their script or repository.

| Tool | Purpose | Data |
|---|---|---|
| [queue.py](queue.py) | Enqueue, claim and complete execution units; `next` prefers the unit that clears a recorded screen-blocking overlay (issue #436); `complete` records a shared completion marker so a unit closed in a detached worktree is never re-picked (issue #438); `validate` checks pool integrity and `sync`/`next` refuse a corrupt pool (issue #441); `sync` drops inbox copies already done on today's delivered records branch (issue #446); `sync` skips producing a unit for a slot already closed on the branch or by a completion marker (issue #466); `plan` stages no unit for a slot already closed on the branch or by a completion marker, and `sync`/`plan` expiry drops (never expires) an inbox copy already done on the branch (issue #465); `token-acquire` renews the lease when the holder re-acquires within 60 seconds of expiry (issue #461) | `../_queue_/` |
| [regulars.py](regulars.py) | Track recurring activities | [regulars.json](regulars.json) and [state](state/INDEX.md) |
| [duel.py](duel.py) | Calculate the active duel day and advice | [duel_schedule.json](duel_schedule.json) |
| [resource_map.py](resource_map.py) | Record resource snapshots and check floors | [resources.json](resources.json) and [state](state/INDEX.md) |
| [scout_diff.py](scout_diff.py) | Compare observations with activities and plan work | `../_activities_/` and `../_queue_/` |
| [retro_report.py](retro_report.py) | Aggregate queue results into review metrics | `../_queue_/` and `../_records_/retro/` |
| [log_append.py](log_append.py) | Newline-safe append, check and repair for JSONL logs | `_logs_/repo-actions/action-log.jsonl` |
| [live_checkout_check.py](live_checkout_check.py) | Check the live checkout's tools against main's `_tools_/` code tree and report drift loudly (issue #415); exit 0 in sync, 1 drifted, 2 cannot run | `~/workspace/lastwar` (live checkout) |
| [branch_guard.py](branch_guard.py) | Verify a records-branch tip is a fast-forward over the previous tip before a reconcile merge or push (issue #485); exit 0 fast-forward, 1 not, 2 cannot verify (a missing parent object is unverifiable, never "unrelated") | `refs/remotes/branch-guard/` |

For example, run `python3 _tools_/regulars.py todo --json` or
`python3 _tools_/queue.py next --budget-minutes 15`.

`_tools_/` is the canonical directory. The root `tools` symlink keeps existing
external job commands and historical paths working during migration. It shares
all configuration and state with `_tools_/`; it is not a second installation.
New job commands, stage pathspecs and documentation use `_tools_/`. Keep the
compatibility link until external callers have been verified to use that path.
Git cannot stage files through a directory symlink. Records writers must use
`git add -- _tools_/state/` for runtime state; update any external job stage
pathspecs before relying on them to publish state.

This executable payload retains its existing Python and JSON filenames as
specified in the [type registry](../_conventions_/local-conventions/typed-folder-adoption.md).
Validate write operations against an isolated pool and output directory.
