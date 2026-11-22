---
title: Held Patches Register
created: 2026-11-22T10:32:17Z
modified: 2026-11-22T10:32:17Z
version: 1.0.0
description: The in-repo record of tool patches held outside the repository, so the tool-developer step-2 in-flight check can see them
grounded_in:
  - source: issue #809 - held patches in hidden_files are invisible to the tool-developer in-flight check
  - source: hidden_files/tool-development/held-patches/RECONCILED-2026-11-22.md - the reconciled held-patch inventory this register mirrors
  - source: merged PR #792 (squash d2b0512b8) implements issue #709 on main
  - source: merged PR #715 (squash 8b9a83bc0) implements issue #712 on main
---

# Held patches register

A held patch is tool work that exists as a patch file outside this
repository, in the goal `hidden_files/` workspace, because it could
not be delivered as a pull request when it was written. A held patch
counts as in-flight work (job step 2). Before re-implementing an
issue, a tool-developer run MUST consult this register with
`_tools_/held_patches.py check <issue>`; a HELD entry means the
issue already has a live patch and must not be re-taken, and a
SUPERSEDED entry means the issue is implemented on main by the named
merged PR and no patch may be applied.

This register is the step-2 source. The reconciled inventory in the
goal `hidden_files/` (`tool-development/held-patches/
RECONCILED-2026-11-22.md`) is the evidence for it: patch copies,
duplicate designations and the verification behind each row below.
The two are mirrors: when a held patch's status changes, update
both in the same run. Patch paths below are relative to the goal
`hidden_files/` directory.

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
