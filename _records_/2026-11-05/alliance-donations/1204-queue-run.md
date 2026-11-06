---
title: Alliance donations queue run 1204
created: 2026-11-05T20:04:00Z
modified: 2026-11-05T20:15:00Z
level: L0
version: 1.0.0
description: Ticker-1204 donations unit, failed on Mac mini offline with no wake-up path, same blocker as Issue 284
status: unverified
---

# 1204 queue run - Alliance donations

Executor: ticker-1204. Unit: donations-2026-11-05-1003.
Session window about 12:04 to 12:15 America/Los_Angeles.

## Not performed

- No game screen was ever read and no game input was dispatched.
  Every device invoke to the Mac mini returned node_offline or
  timed out, so Alliance Techs could not be opened, the live
  Donation Count was never read, no coin donation was made and
  no daily donation reward was claimed. This was the 10:03
  local slot unit; the loss is the unexecuted donation work
  and the missing closing read against the 30-of-30 daily
  target.

## Blocker, measured

- Device: Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd),
  listed offline. device.list last_seen 2026-11-05T15:36:52Z
  (07:36 local) - stale about 4 hours 30 minutes at pass
  time, unchanged since the ticker-1025 pass.
- computer.session start on the Mac mini: node_offline, device
  is offline and does not advertise a wake-up path (attempt 1).
- connection.health on the Mac mini: node_offline (attempt 2).
- connection.repair (web) on the Mac mini: node_offline
  (attempt 3).
- device.list re-check: still offline, last_seen unchanged
  15:36:52Z.
- computer.session start on the Mac mini again: node_offline
  (attempt 4).
- connection.health on the recovery device
  (endo-recovery-8a2744fe-3281-4d50-a6d1-0ad28e99c05c):
  node_invoke_timeout after 25000ms (attempt 5).
- Five device invokes, zero responses. This meets the standing
  retry rule of at least 3 attempts before recording a unit
  as access-failed.

## Repeated failure mode

- This is the same blocker already filed as GitHub Issue #284
  (label tooling, still open at this pass): the forty-fourth
  consecutive pass with a Mac device-access blocker was
  ticker-1134 (arms-race unit, 11:34 local), and this pass is
  the forty-fifth. The form is the worsened zero-response one
  seen since the morning of 2026-11-05: the device is fully
  offline with a stalled invoke channel, not just the LastWar
  window capture failure of the earlier passes. The
  ticker-1025 pass classified it CHANNEL_STALL and noted
  recovery needs the Mac-side agent gateway restart before
  re-probing, and re-probing is owed only after device.list
  last_seen refreshes. That condition is not met - last_seen
  is still 15:36:52Z - so no further probe was run this pass.
  This pass commented on #284 instead of filing a duplicate.
  Until the Mac gateway recovers, further ticker passes will
  fail their first unit the same way; the inbox held 76 units
  at this pass.

## Other pass steps

- Own PRs checked first: the live records PR for today is
  PR 310 (records/2026-11-05). The integrator's 1145
  non-batch verification found it MERGEABLE/CLEAN against
  main 48c83df8 and it awaits the 15:00 batch; no question
  addressed to this job, so nothing was owed before game
  work.
- Sync: reaped 0, expired 0, due 21, produced nothing new,
  all 21 regulars already queued.
- No zombie seeding: zombie chain zombie-2026-10-28 closed
  with unit 066 on 2026-10-30 (event ended about the 19:00
  reset 2026-10-30, no Zombie tab in the Events hub), and the
  seeding rule forbids a fresh chain until a Zombie Invasion
  tab is seen live again.
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

Failed. No Donation Count read, no donation made, no reward
claimed, no diamonds, money, speedups or other spending. No
alliance diplomacy, no assembly, no teleport.

## Result stats

- target 30 coin donations, achieved 0,
  resources_gained none, costs no_game_input, verified no,
  blocker_category e, device_takeovers 0, capture_attempts 5,
  issue 284
