---
title: Donations queue run 1606
created: 2026-11-06T00:12:00Z
modified: 2026-11-06T00:12:00Z
level: L0
version: 1.0.0
description: Ticker-1604 donations unit, failed on Mac mini offline with no wake-up path, same blocker as Issue 284
status: unverified
---

# 1606 queue run - Alliance donations

Executor: ticker-1604. Unit: donations-2026-11-05-1403.
Session window about 16:04 to 16:12 America/Los_Angeles.

## Not performed

- No game screen was ever read and no game input was dispatched.
  Every device invoke to the Mac mini returned node_offline or
  timed out, so Alliance Techs could not be opened, the live
  Donation Count was never read, no coin donation was made and
  nothing was claimed. The loss is the unexecuted donation work
  and the missing closing read for this slot.

## Blocker, measured

- Device: Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd),
  listed offline. device.list last_seen 2026-11-05T15:36:52Z
  (07:36 local) - stale about 8 hours 30 minutes at pass time,
  unchanged since the ticker-1025 pass.
- computer.session start on the Mac mini: node_offline, device
  is offline and does not advertise a wake-up path (attempts
  1, 2 and 3, then attempt 6 after the repair tries).
- connection.repair (native) on the recovery device
  (endo-recovery-8a2744fe-3281-4d50-a6d1-0ad28e99c05c):
  node_invoke_timeout after 25000ms (attempt 4).
- connection.health on the recovery device:
  node_invoke_timeout after 25000ms (attempt 5).
- Six device invokes, zero responses. This meets the
  standing retry rule of at least 3 attempts before recording
  a unit as access-failed.

## Repeated failure mode

- This is the same blocker already filed as GitHub Issue #284
  (label tooling, still open at this pass): the fifty-second
  consecutive pass with a Mac device-access blocker was
  ticker-1534 (arms-race unit, 15:34 local), and this pass is
  the fifty-third, fourteenth in the worsened zero-response
  form. The form is unchanged since the afternoon of
  2026-11-04 - a fully offline device with a stalled invoke
  channel; the ticker-1025 pass classified it CHANNEL_STALL
  and noted recovery needs the Mac-side agent gateway restart
  before re-probing, and re-probing is owed only after
  device.list last_seen refreshes. That condition is not met
  - last_seen is still 15:36:52Z - so no further probe was
  run after the six attempts above. This pass commented on
  #284 instead of filing a duplicate. Until the Mac gateway
  recovers, further ticker passes will fail their first unit
  the same way; the inbox held 76 units at this pass.

## Other pass steps

- Own PRs checked first: the live records PR for today is
  PR 334 (records/2026-11-05, post-1500 batch), Owner
  lastwar-pr-integrator, with no comments. No question
  addressed to this job, so nothing was owed before game work.
- Sync: reaped 0, expired 0, due 21, produced nothing new,
  all 21 regulars already queued.
- No zombie seeding: zombie chain zombie-2026-10-28 closed
  with unit 066 on 2026-10-30 (event ended about the 19:00
  reset 2026-10-30, no Zombie tab in the Events hub), and the
  seeding rule forbids a fresh chain until a Zombie Invasion
  tab is seen live again.
- Pre-reset zero-sweep pair staged for tonight's 19:00 reset,
  chain pre-reset-sweep-2026-11-05: unit 001 not_before
  2026-11-06T01:30:00Z, unit 002 not_before
  2026-11-06T02:30:00Z, both priority 1, expiring at the
  reset 2026-11-06T03:00:00Z. No sweep pair had been staged
  for this reset before this pass.
- Tracker untouched: a failed unit does not mark the
  regular, so the next tick re-produces the donations unit.
- Delivery note: the local working tree sits on branch
  work/ops-execution-records and holds another job's
  in-flight state (unrelated modifications and deletions),
  so this pass's outputs were delivered through a temporary
  worktree onto the records/2026-11-05 branch, leaving that
  state undisturbed.
- The pass stopped after this one unit: with the device
  fully offline, further units would fail identically.

## Outcome

Failed. No Donation Count read, no donation made, no
diamonds, money, speedups or other spending. No alliance
diplomacy, no assembly, no teleport.

## Result stats

- target 30, achieved 0, resources_gained none,
  costs no_game_input, verified no, blocker_category e,
  device_takeovers 0, capture_attempts 6, issue 284
