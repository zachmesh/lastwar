---
title: Radar Tasks queue run 1104
created: 2026-11-06T19:20:00Z
modified: 2026-11-06T19:20:00Z
level: L0
version: 1.0.0
description: Ticker-1104 radar unit, failed on Mac mini offline with no wake-up path, same blocker as Issue 284
status: unverified
---

# 1104 queue run - Radar Tasks

Executor: ticker-1104. Unit: radar-2026-11-06-1003.
Session window about 11:04 to 11:23 America/Los_Angeles.

## Not performed

- No game screen was ever read and no game input was dispatched.
  Every device invoke to the Mac mini returned node_offline, so
  the Radar screen was never opened, no radar task was read or
  claimed, and no duel-day radar release was collected. The loss
  is the unexecuted radar check for this slot (duel day 5,
  planned 10:03 local 2026-11-06, expires 14:03 local
  2026-11-06).

## Blocker, measured

- Device: Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd),
  listed offline. device.list last_seen 2026-11-05T15:36:52Z
  (07:36 local 2026-11-05) - stale about 27 hours 45 minutes at
  the 11:23 re-check, unchanged since the ticker-0934 pass.
- Five device invokes, zero responses:
  - computer.session start (attempt 1) on the Mac mini:
    node_offline, "device is offline and does not advertise a
    wake-up path".
  - connection.health (attempt 2) on the Mac mini:
    node_offline, same message.
  - connection.repair web (attempt 3) on the Mac mini:
    node_offline, same message.
  - computer.session start (attempt 4, retry) on the Mac mini:
    node_offline, same message.
  - connection.health (attempt 5) on the recovery device
    (endo-recovery-8a2744fe-3281-4d50-a6d1-0ad28e99c05c,
    "Zhen's Mac mini connection recovery"): node_invoke_timeout
    after 25000ms.
  This meets the standing retry rule of at least 3 attempts
  before recording a unit as access-failed.
- Recovery-device attempt was made, as in recent passes: it
  timed out rather than answering node_offline, so the
  recovery channel accepts the invoke and never answers
  within 25 seconds. The recovery device's last_seen is frozen
  at the same 2026-11-05T15:36:52Z as the Mac mini. No new
  recovery route was learned; the timeout signature matches
  the ticker-0741, ticker-0832 and ticker-0934 passes.

## Repeated failure mode

- This is the same blocker already filed as GitHub Issue #284
  (label tooling, still open at this pass): the seventy-seventh
  recorded consecutive pass with a Mac device-access blocker,
  thirty-eighth in the worsened zero-response form. The last
  recorded one was ticker-0934, the seventy-sixth and
  thirty-seventh. No executed pass is recorded between 0934 and
  this one: the newest executed closing in the pool is
  2026-11-06T17:56:17Z (the 0934 unit). This pass commented
  on #284 instead of filing a duplicate. Until the Mac gateway
  recovers, further ticker passes will fail their first unit
  the same way; the inbox held 68 units at this pass's stats
  (plus 1 claimed, this unit).

## Other pass steps

- Own PRs checked first: PR 359 (records/2026-11-06,
  post-0700 batch) was merged at the 11:00 batch (merge commit
  a469658df2). PR 365, opened by the pr-integration 1100 pass
  for the post-1100-batch appends, already covers the branch,
  so no new PR is opened by this pass. Older records PRs 351,
  350, 301, 265 and 256 remain open under the integrator,
  unchanged; their newest comments are the 11:00 batch
  conflict notes on the single-file action-log append-append,
  with nothing addressed to this job.
- Sync: reaped 0, expired 6, due 22, produced 12 new units,
  9 regulars already queued. Queue stats at 19:18Z: inbox 68,
  claimed 1, done 956, upcoming 48.
- No zombie seeding: zombie chain zombie-2026-10-28 closed
  with unit 066 on 2026-10-30 (event ended about the 19:00
  reset 2026-10-30, no Zombie tab in the Events hub), and the
  seeding rule forbids a fresh chain until a Zombie Invasion
  tab is seen live again.
- Pre-reset zero-sweep pair for the 2026-11-06 19:00 reset
  (chain pre-reset-sweep-2026-11-06) sits in the inbox
  (pending 2); not yet due, untouched by this pass.
- Tracker untouched: a failed unit does not mark the regular,
  so the next tick re-produces the radar unit.
- Delivery note: the local working tree sits on branch
  work/ops-execution-records and holds another job's
  in-flight state (unrelated modifications and deletions),
  so this pass's outputs were delivered through a temporary
  worktree onto the records/2026-11-06 branch, leaving that
  state undisturbed.
- The pass stopped after this one unit: with the device
  fully offline, further units would fail identically.

## Outcome

Failed. No Radar screen read, no radar task claimed, no duel-day
release collected. No diamonds, money, speedups or other
spending. No alliance diplomacy, no assembly, no teleport.

## Result stats

- target 1, achieved 0, resources_gained none,
  costs no_game_input, verified no, blocker_category e,
  device_takeovers 0, capture_attempts 5, issue 284
