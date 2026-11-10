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
| [queue.py](queue.py) | Enqueue, claim and complete execution units; `next` prefers the unit that clears a recorded screen-blocking overlay (issue #436); `complete` records a shared completion marker so a unit closed in a detached worktree is never re-picked (issue #438); `validate` checks pool integrity and `sync`/`next` refuse a corrupt pool (issue #441); `sync` drops inbox copies already done on today's delivered records branch (issue #446); `sync` skips producing a unit for a slot already closed on the branch or by a completion marker (issue #466); `plan` stages no unit for a slot already closed on the branch or by a completion marker, and `sync`/`plan` expiry drops (never expires) an inbox copy already done on the branch (issue #465); `token-acquire` renews the lease when the holder re-acquires within 60 seconds of expiry (issue #461); `sweep` and `plan` stage one pre-reset fix-up unit per ledger regular at the pair-midpoint slot, priority 1, expiring at the reset, so the sweep's fix-ups are claimable before the reset (issue #147); `--root` accepts a repository root, resolved to its `_queue_` folder, or a pool directory directly, and `enqueue` refuses a root holding no pool state directory, so a wrong root never mints units into a fresh empty directory (issue #510); a repository root holding both a stray top-level pool and a _queue_ subdir resolves to the _queue_ pool, and pool_root_warning names the stray so it gets removed (issue #539) | `../_queue_/` |
| [regulars.py](regulars.py) | Track recurring activities | [regulars.json](regulars.json) and [state](state/INDEX.md) |
| [duel.py](duel.py) | Calculate the active duel day and advice | [duel_schedule.json](duel_schedule.json) |
| [resource_map.py](resource_map.py) | Record resource snapshots and check floors | [resources.json](resources.json) and [state](state/INDEX.md) |
| [scout_diff.py](scout_diff.py) | Compare observations with activities and plan work; `--root` accepts a repository root, resolved to its `_queue_` folder, or a pool directory directly, and `--apply` refuses a root holding no pool state directory, so a wrong root fails loudly instead of writing units into a fresh empty directory (issue #510); a dry run against a root holding no pool state directory prints the pool_root_warning, so its counts never silently describe an empty pool (issue #537); --apply prints the pool_root_warning too, so a stray pool beside the resolved pool is named on the write path as well (issue #539); the diff consults today's delivered records branch before enqueueing, so a unit already closed on the branch - or an exploration already closed on the branch today - is reported already-queued instead of re-enqueued (issue #466); unmatched-label lines that are the prose form of an empty list (`- none (...)` block lines, `unmatched_labels: none (...)` scalars and `none  # ...` trailing comments) are skipped instead of filed as exploration candidates (issue #527); the diff also reads the shared main-checkout pool's done/ records before enqueueing, so a slot the ticker already closed in the live pool - whose delivery has not landed on the branch yet - is reported already-queued instead of re-enqueued (issue #533) | `../_activities_/` and `../_queue_/` |
| [retro_report.py](retro_report.py) | Aggregate queue results into review metrics | `../_queue_/` and `../_records_/retro/` |
| [log_append.py](log_append.py) | Newline-safe append, check and repair for JSONL logs | `_logs_/repo-actions/action-log.jsonl` |
| [live_checkout_check.py](live_checkout_check.py) | Check the live checkout's tools against main's `_tools_/` code tree and report drift loudly (issue #415); exit 0 in sync, 1 drifted, 2 cannot run | `~/workspace/lastwar` (live checkout) |
| [branch_guard.py](branch_guard.py) | Verify a records-branch tip is a fast-forward over the previous tip before a reconcile merge or push (issue #485); sweep the merged tree for unresolved conflict-marker lines before the push (issue #441) | `refs/remotes/branch-guard/` |
| [tree_check.py](tree_check.py) | Verify the ten expected top-level entries (AGENTS.md, README.md, `_activities_`, `_conventions_`, `_knowledge_`, `_logs_`, `_queue_`, `_records_`, `_tools_`, `tools`) are present in the git index and working tree before a delivery commit, or in a committed tree (`--tree REF`) before a push, so a sparse-checkout worktree whose index holds only `_records_` can never push a poisoned tree (issue #541); exit 0 complete, 1 entries missing, 2 cannot verify | the repository root being delivered |
| [tapcal.py](tapcal.py) | Score tap logs (first-try rate, miss vectors), calibrate a session offset from anchor observations, compensate aim points, keep per-activity visual anchors, and decide one step of the tap-verify loop for a single target (issue #123); tap and anchor records may name the window geometry so a fullscreen-only shift is never averaged away (issue #475) | executor tap logs and anchor stores |

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
