---
title: queue.py, part 1 of 4
created: 2026-11-23T04:53:59Z
modified: 2026-11-23T04:53:59Z
version: 1.0.0
description: Verbatim index text for queue.py
---

# queue.py, part 1 of 4

Moved verbatim from the former `_tools_/INDEX.md` row for [queue.py](../queue.py); only link destinations are adjusted. Back to the [tool index](../INDEX.md). The text continues in [part 2](queue-part-2.md).

Purpose: Enqueue, claim and complete execution units; `next` prefers the unit that clears a recorded screen-blocking overlay (issue #436); `complete` records a shared completion marker so a unit closed in a detached worktree is never re-picked (issue #438); `validate` checks pool integrity and `sync`/`next` refuse a corrupt pool (issue #441); `validate --ref <git-ref>` runs the same checks on the committed `_queue_` tree at a ref with no checkout, so a merge resolution is checked before commit and a records PR is gated on its branch tip before merging to main (issue #661); `sync` drops inbox copies already done on today's delivered records branch (issue #446); `sync` skips producing a unit for a slot already closed on the branch or by a completion marker (issue #466); `plan` stages no unit for a slot already closed on the branch or by a completion marker, and `sync`/`plan` expiry drops (never expires) an inbox copy already done on the branch (issue #465); `token-acquire` renews the lease on a same-holder re-acquire (issue #461); `sweep` and `plan` stage one pre-reset fix-up unit per ledger regular at the pair-midpoint slot, priority 1, expiring at the reset, so the sweep's fix-ups are claimable before the reset (issue #147); `--root` accepts a repository root, resolved to its `_queue_` folder, or a pool directory directly, and `enqueue` refuses a root holding no pool state directory, so a wrong root never mints units into a fresh empty directory (issue #510); a repository root holding both a stray top-level pool and a _queue_ subdir resolves to the _queue_ pool, and pool_root_warning names the stray so it gets removed (issue #539); `complete` warns when a gifts closing writes its Gift Level progress gain into stats.points (issue #300); `complete` warns when a closing writes a blocker_category outside the a-to-i miss-audit enum, and `stats` counts those closings (issue #130); `sync` names markers aged out with no local done record separately as `completion_markers_lost`, so a closing the delivery never carried stays visible for triage (issue #563);
