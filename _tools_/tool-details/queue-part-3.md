---
title: queue.py, part 3 of 4
created: 2026-11-23T04:53:59Z
modified: 2026-11-23T04:53:59Z
version: 1.0.0
description: Verbatim index text for queue.py
---

# queue.py, part 3 of 4

Moved verbatim from the former `_tools_/INDEX.md` row for [queue.py](../queue.py); only link destinations are adjusted. Back to the [tool index](../INDEX.md). Continues [part 2](queue-part-2.md). The text continues in [part 4](queue-part-4.md).

Purpose, continued: `next` hands out nothing while a recorded control-lock blocker stands, `complete` records one when a short closing names `blocker_overlay=control-lock` and lifts it on any later closing that sent input, and `sync` reaps a control-lock blocker older than 4 hours so the next tick probes with one input (issue #689); `next`, `sync`, `plan`, `sweep` and `enqueue` refuse when this copy of queue.py differs from main's _tools_/queue.py, so a stale tree cannot decide on old behaviour (issue #694); `next`, `sync`, `plan`, `sweep` and `enqueue` refuse when this copy of queue.py - or the pool it would decide on - sits under the system temp directory, so a pass worktree created under /tmp fails loudly instead of losing its records to the /tmp sweep mid-pass (issue #429); `next` decides from the live pool (issue #694): it resolves the given root through live_pool_root before listing candidates, so a worktree-root `next` reads the live inbox instead of the snapshot, and `claim` claims the live-pool copy into the pass root, so a unit handed out from the live pool is claimable even when the snapshot never held it; a unit the live pool holds claimed or done is refused instead of claimed from a stale snapshot copy; `version` prints this copy's identity - resolved path, sha256, git HEAD and currency against main's copy - so a pass record cites it and a stale-tool handout is diagnosable from the record alone (issue #694); `sync`, `plan` and `reap` reap expired claims, expire stale inbox units and drop stale inbox copies in the live pool even when run from a linked worktree, so expired units leave the live inbox instead of accumulating there (issue #705); `plan` and `sweep` refuse a window whose computed expiry is already past and a reset-anchored slot whose chain step the pool already holds at another slot, so no stillborn unit or duplicate sweep pair is staged (issue #712); `enqueue` reconciles the next chain seq across the live pool, its completion markers and the given root's snapshot, so a finished seq the live pool forgot is never re-minted (issue #750);
