---
title: Changelog part 5
created: 2026-11-23T09:03:48Z
modified: 2026-11-23T09:03:48Z
version: 0.1.0
sequence: 59
description: 0.23.0, 2026-11-21 - section 11 gains rule R15 (expired-window and chain-step dedupe, issue 712) - the
---
- 0.23.0, 2026-11-21 - section 11 gains rule R15 (expired-window and chain-step dedupe, issue #712): the production path refuses a window whose computed expiry is already past and a reset-anchored slot whose chain step the pool already holds at another slot, so plan no longer stages a stillborn zero-sweep unit for yesterday's slot or a second sweep pair at the new geometry beside the old one; both refusals are recorded and reported by plan and sweep.
- 0.22.0, 2026-11-12 - section 11 gains rule R14 (live-pool reap/expire, issue #705): `sync`, `plan` and `reap` resolve the given root through live_pool_root before reaping expired claims, expiring stale inbox units and dropping stale inbox copies, so a worktree-root run expires the live pool instead of the snapshot; the pool-integrity guard in sync now covers the live pool.
- 0.21.0, 2026-11-12 - section 11 gains rule R13 (tool-identity evidence, issue #694): `queue.py version` prints this copy's identity - resolved path, sha256, git HEAD and currency against main - so a pass record cites it and a stale-tool handout is diagnosable from the record alone; the command only reports and never refuses.
- 0.20.0, 2026-11-12 - section 11 gains rule R12 (live-pool handout, issue #694): `next` resolves the given root through the live pool before listing candidates, so a worktree-root `next` reads the live inbox instead of the snapshot, and `claim` claims the live-pool copy into the pass root, so a unit handed out from the live pool is claimable even when the snapshot never held it.
