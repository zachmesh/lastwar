---
title: Changelog part 3
created: 2026-11-23T09:03:48Z
modified: 2026-11-23T09:03:48Z
version: 0.1.0
sequence: 57
description: 0.31.0, 2026-11-21 - section 12 synced to the 120, 60 sweep geometry (PR 614, Refs 606;
---
- 0.31.0, 2026-11-21 - section 12 synced to the [120, 60] sweep geometry (PR #614, Refs #606; renumbered from 0.23.0, issue #739): the pair stages at 120 and 60 minutes before the reset instant (16:00 and 17:00 PST in winter, 17:00 and 18:00 PDT in summer), not 90 and 30. The entry was first labeled 0.23.0 and collided with the R15 entry (PR #715) that already claims 0.23.0; this change renumbers it to the next free version and bumps the frontmatter from its stale 0.17.0 to 0.31.0.
- 0.30.0, 2026-11-21 - section 4 states the VIP expiry rule explicitly (issue #733): a VIP unit staged for a reset opens that reset day and expires at the next reset, so expires_at is planned_for + 24h; the 2026-11-19T02:00:00Z expiry on vip-2026-11-17-1800 is correct and the ticker-2034 flag is refuted. No tool change: the daily-reset branch already computes planned_utc + 1 day.
- 0.29.0, 2026-11-21 - section 11 gains rule R21 (worktree-create base check, issue #709): `pass_worktree.py create` with an explicit `--base` reuses an existing branch only when its tip is the base and refuses a stale branch, exit 2, naming both tips, so a pass never decides from a stale main it did not ask for; without `--base` the checkout-as-is semantics stand.
- 0.28.0, 2026-11-21 - section 11 gains rule R20 (sweep ledger-walk task text, issue #748): the production path appends the standing ledger-walk task section to each pre-reset sweep pair body (first/final pass by chain_seq), so a staged pair carries its walk instructions instead of the generic body; slot and reset times come from the unit's own fields and the ledger line count is read live from the ledger.
