---
title: Incident - a detached HEAD in the shared checkout - 2026-11-23 10:56Z
created: 2026-11-23T03:12:00-08:00
modified: 2026-11-23T03:14:00-08:00
level: L3
version: 0.1.0
description: A read-only listing command ran git checkout --detach in the live checkout, which split my commits across a detached HEAD and main until the coordinator re-joined them; no content was lost
status: done
activity: team-operations
run_id: team-operations-2026-11-23-1056-checkout-incident
trigger: the coordinator's landing branch showed 2 commits above origin where 4 were expected (the reflog showed a checkout of origin/main at 02:56:49 PT)
started_at: 2026-11-23T03:03:00-08:00
finished_at: 2026-11-23T03:14:00-08:00
verified: reflog read; the four commits and every record present in the repaired chain; clean-worktree check exit 0 and scan 0 on the rebuilt landing branch; the scribe confirmed it ran the command
---

# Incident: detached HEAD in the shared checkout

## What happened

At 10:56:49Z (02:56:49 PT) the scribe ran `git checkout --detach origin/main` in the live checkout as the first step of a read-only listing command (the working directory was the live repo). HEAD became detached; the coordinator's next two commits (the first-builder decision and a records delivery) landed on the detached HEAD while the branch `main` kept an older tip with the converge record and a tick. The landing branch built from HEAD therefore lacked two commits.

## Repair (no content lost)

The two chains were joined by cherry-picking `main`'s two commits onto the detached chain (one conflict in the day index, resolved by union), then `update-ref refs/heads/main HEAD` and `symbolic-ref HEAD refs/heads/main`, which do not touch the working tree. Backup refs: `refs/backup/main-before-reattach-1104` and `refs/backup/main-before-converge-20261123T103611Z`. The landing branch was rebuilt and re-verified in a clean worktree.

## Rules from now

In the live checkout nobody runs `checkout`, `switch`, `reset`, `rebase` or `stash` except the coordinator's post-landing `git rebase --autostash origin/main`; any other ref is read with `git show` or a worktree under /tmp. The scribe's scripts that take a directory refuse the live path. A reflog read of `HEAD` after any odd landing result is the first diagnostic.
