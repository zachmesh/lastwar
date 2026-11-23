---
title: Changelog part 3
created: 2026-11-23T08:37:05Z
modified: 2026-11-23T08:37:05Z
version: 0.1.0
sequence: 43
description: 0.26.0, 2026-11-21 - section 11 gains rule R18 (chain event-end guard, issue 745) - enqueue refuses
---
- 0.26.0, 2026-11-21 - section 11 gains rule R18 (chain event-end guard, issue #745): `enqueue` refuses a chain successor when the chain's latest recorded `event_ends_at` is past, so a dead event's chain stops minting instead of seeding units for it; no reading recorded means no signal and the mint proceeds as before.
- 0.25.0, 2026-11-21 - section 11 gains rule R17 (doomed-probe zombie preference, issue #746): `next --probe` hands out a queued zombie chain unit ahead of the overlay steering and the normal pick, so a probe pass burns the re-minted chain unit instead of a scout unit; with no zombie unit queued, actionable and inside budget, the probe falls through to the normal pick.
- 0.24.0, 2026-11-21 - section 11 gains rule R16 (enqueue chain-seq reconciliation, issue #750): `enqueue` takes the next chain seq from the highest seq named by the live pool, its completion markers, or the given root's snapshot pool, so a finished seq the live pool forgot is never re-minted. 0.23.0 is now claimed by the merged R15 change (PR #715); the competing R15 branch PR #751 stands superseded, and the geometry fold (PR #761) still claims 0.23.0 per issue #739 and must renumber on rebase, so this change takes the next free number.
- 0.23.0, 2026-11-21 - section 11 gains rule R15 (expired-window and chain-step dedupe, issue #712): the production path refuses a window whose computed expiry is already past and a reset-anchored slot whose chain step the pool already holds at another slot, so plan no longer stages a stillborn zero-sweep unit for yesterday's slot or a second sweep pair at the new geometry beside the old one; both refusals are recorded and reported by plan and sweep.
- 0.22.0, 2026-11-12 - section 11 gains rule R14 (live-pool reap/expire, issue #705): `sync`, `plan` and `reap` resolve the given root through live_pool_root before reaping expired claims, expiring stale inbox units and dropping stale inbox copies, so a worktree-root run expires the live pool instead of the snapshot; the pool-integrity guard in sync now covers the live pool.
- 0.21.0, 2026-11-12 - section 11 gains rule R13 (tool-identity evidence, issue #694): `queue.py version` prints this copy's identity - resolved path, sha256, git HEAD and currency against main - so a pass record cites it and a stale-tool handout is diagnosable from the record alone; the command only reports and never refuses.
