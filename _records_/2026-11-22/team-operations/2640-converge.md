---
title: Local main converged onto origin - 2026-11-23 10:36Z
created: 2026-11-23T02:40:00-08:00
modified: 2026-11-23T02:42:00-08:00
level: L3
version: 0.1.0
description: After the second records snapshot landed, local main was moved onto origin main so that deliveries are linear; the superseded old-path run articles were verified and removed from the working tree
status: done
activity: team-operations
run_id: team-operations-2026-11-23-1036-converge
trigger: PR 892 (records snapshot 2) merged; the toolsmith's records-snapshot converge helper
started_at: 2026-11-23T02:33:00-08:00
finished_at: 2026-11-23T02:42:00-08:00
verified: the helper's dry run passed (no true conflict); main, origin/main and HEAD all read 457fdd460 afterwards; 1,095 old-path files verified byte-identical in body to their moved notes before deletion; the backup ref keeps the old tip
---

# Local main converged onto origin

## What was done

- **Problem:** local main and origin main were different lines from one base (a dry-run merge showed 246 conflicts), so every landing needed a hand-built snapshot.
- **Fix:** after PR 892 landed the last records delta, the toolsmith's `records_snapshot.py converge --accept-newer` moved the branch ref `main` onto `origin/main` (457fdd460) and reset the index only; the working tree stayed byte for byte. The old tip 5d4d87b35 is kept as `refs/backup/main-before-converge-20261123T103611Z`.
- **Cleanup:** `_activities_` and `_run_notes_` were restored from origin; the 1,095 untracked old-path run articles were each checked against the moved note (the body is an exact prefix) and removed; 0 failed.
- **Result:** deliveries now sit directly on origin's tip; a landing branch is just a branch name at HEAD; the first one is `land/records-1037` (26 files, scan 0, clean-worktree base check exit 0).

## Cautions

- Run the base check in a clean worktree of the branch: it reads untracked files of the live tree (a 508-word strategist file and the `_queue_/completed` marker produced false findings).
- Never merge origin into this checkout again: not needed, history is linear.
