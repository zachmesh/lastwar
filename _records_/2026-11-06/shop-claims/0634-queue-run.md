---
title: Passes queue run 0634
created: 2026-11-06T14:37:00Z
modified: 2026-11-06T14:37:00Z
level: L0
version: 1.0.0
description: Ticker-0634 passes unit, failed on Mac mini offline with no wake-up path, same blocker as Issue 284
status: unverified
---

# 0634 queue run - Passes

Executor: ticker-0634. Unit: passes-2026-11-06-0257.
Session window about 06:34 to 06:37 America/Los_Angeles.

## Not performed

- No game screen was ever read and no game input was dispatched.
  Every device invoke to the Mac mini returned node_offline, so
  the shop and passes pages were never opened, no free pack or
  pass reward was checked or claimed. The loss is the unexecuted
  passes check for this slot (planned 02:57 local 2026-11-06,
  expires 06:57 local 2026-11-06).

## Blocker, measured

- Device: Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd),
  listed offline. device.list last_seen 2026-11-05T15:36:52Z
  (07:36 local) - stale about 23 hours at the 06:36 re-check,
  unchanged since the ticker-0534 pass and re-verified
  unchanged by the ticker-0604 pass.
- Four device invokes, zero responses, all node_offline with
  "device is offline and does not advertise a wake-up path":
  connection.health (attempts 1 and 4), connection.repair web
  (attempt 2), computer.session start (attempt 3). This meets
  the standing retry rule of at least 3 attempts before
  recording a unit as access-failed.
- No recovery-device attempts were made in this pass: the
  recovery device (endo-recovery-8a2744fe-3281-4d50-a6d1-0ad28e99c05c)
  is offline with the same frozen last_seen 15:36:52Z, and the
  ticker-0234 pass attempted its recovery channel and timed out
  after 25 seconds, so nothing new would be learned by repeating
  it (same reasoning as the ticker-0104, ticker-0342 and
  ticker-0404 passes).

## Repeated failure mode

- This is the same blocker already filed as GitHub Issue #284
  (label tooling, still open at this pass): the seventy-second
  recorded consecutive pass with a Mac device-access blocker,
  thirty-third in the worsened zero-response form. The last
  recorded one was ticker-0604, the seventy-first and
  thirty-second. No executed pass is recorded between 0604 and
  this one: the latest executed failure in the pool is the
  0604 pass's unit (finished 14:10:21Z). This pass commented
  on #284 instead of filing a duplicate. Until the Mac gateway
  recovers, further ticker passes will fail their first unit
  the same way; the inbox held 50 units at this pass's close
  (50 at sync, after 15 expired units were reaped and the
  duel-score-2026-11-06-0630 unit was produced).

## Other pass steps

- Own PRs checked first: PR 347 (records/2026-11-06) carries no
  new comments since the ticker-0342 pass reconciled its 03:00
  batch conflict on the branch side (merge 9a716619ce); the
  other open records PRs (351, 350, 301, 265, 256) carry no new
  comments. Nothing addressed to this job. No PR action needed
  this pass.
- Sync: reaped 0, expired 15, due 22, produced one new unit
  (duel-score-2026-11-06-0630), 20 regulars already queued.
- No zombie seeding: zombie chain zombie-2026-10-28 closed
  with unit 066 on 2026-10-30 (event ended about the 19:00
  reset 2026-10-30, no Zombie tab in the Events hub), and the
  seeding rule forbids a fresh chain until a Zombie Invasion
  tab is seen live again.
- Pre-reset zero-sweep pair for the 2026-11-06 19:00 reset
  (chain pre-reset-sweep-2026-11-06) sits in the inbox
  (not_before 01:30Z and 02:30Z on 2026-11-07, expires
  03:00Z); not yet due, untouched by this pass.
- Tracker untouched: a failed unit does not mark the regular,
  so the next tick re-produces the passes unit.
- Delivery note: the local working tree sits on branch
  work/ops-execution-records and holds another job's
  in-flight state (unrelated modifications and deletions),
  so this pass's outputs were delivered through a temporary
  worktree onto the records/2026-11-06 branch, leaving that
  state undisturbed. PR 347 already covers the branch, so no
  new PR was opened.
- The pass stopped after this one unit: with the device
  fully offline, further units would fail identically.

## Outcome

Failed. No passes screen read, no pack or pass reward checked
or claimed. No diamonds, money, speedups or other spending.
No alliance diplomacy, no assembly, no teleport.

## Result stats

- target 1, achieved 0, resources_gained none,
  costs no_game_input, verified no, blocker_category e,
  device_takeovers 0, capture_attempts 4, issue 284
