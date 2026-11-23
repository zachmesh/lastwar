---
title: Held patches and 1 more
created: 2026-11-23T09:06:22Z
modified: 2026-11-23T09:06:22Z
version: 0.1.0
sequence: 2
description: Machine-readable table - _tools_/held_patches.py parses these rows (the Issue, Status, Canonical patch and Superseding PR columns).
---
## Held patches

Machine-readable table: `_tools_/held_patches.py` parses these rows
(the Issue, Status, Canonical patch and Superseding PR columns).
Keep the table format fixed and one row per issue.

| Issue | Status | Canonical patch | Superseding PR / note |
|---|---|---|---|
| #383 | HELD | `tooldev-0032-383/token-patch-383.py` | Live-held since 2026-11-07, do not re-take |
| #709 | SUPERSEDED | `tool-development/work-pass-worktree-base-check.patch` | PR #792, squash d2b0512b8 |
| #712 | SUPERSEDED | `tool-development/2026-11-14-2232-issue-712-part1/0001-refs-712-plan-expired-window.patch` | PR #715, squash 8b9a83bc0 |

## Rules

- One held patch per issue, named here. A second copy is a
  duplicate: do not create it, update this register instead.
- A patch marked SUPERSEDED must never be re-applied; its issue is
  implemented on main by the named merged PR.
- When a held patch's issue merges, mark it SUPERSEDED here with the
  PR number and squash commit, in the same run that verifies the
  merge. Do not leave a merged issue's patch looking live.
- A new held patch is added here (status HELD, canonical path, date)
  in the run that holds it, together with the evidence inventory
  entry in the goal `hidden_files/`.
