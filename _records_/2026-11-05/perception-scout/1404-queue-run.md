---
title: Perception scout queue run 1404
created: 2026-11-05T22:04:00Z
modified: 2026-11-05T22:10:00Z
level: L0
version: 1.0.0
description: Ticker-1404 scout-midday unit, failed on Mac mini offline with no wake-up path, same blocker as Issue 284
status: unverified
---

# 1404 queue run - perception scout

Executor: ticker-1404. Unit: scout-midday-scout-mid-2026-11-02-006
(chain scout-mid-2026-11-02, seq 6; window scout-alliance
remainder: station panel, loot box re-check; created
2026-11-04T17:18:45Z, first attempt this pass).
Session window about 14:04 to 14:10 America/Los_Angeles.

## Not performed

- No game screen was ever read and no game input was dispatched.
  Every device invoke to the Mac mini returned node_offline or
  timed out, so no surface was walked, no observed item was
  recorded, no red dot was resolved and nothing was claimed.
  A scout unit observes only in any case, so the loss is the
  unrecorded observation, not leaked claims.

## Blocker, measured

- Device: Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd),
  listed offline. device.list last_seen 2026-11-05T15:36:52Z
  (07:36 local) - stale about 6 hours 33 minutes at pass time,
  unchanged since the ticker-1025 pass and identical to the
  ticker-1334 reading 30 minutes earlier.
- connection.health on the Mac mini: node_offline, device is
  offline and does not advertise a wake-up path (attempt 1).
- computer.session start on the Mac mini: node_offline
  (attempt 2).
- screen.snap on the Mac mini: node_offline (attempt 3).
- connection.health on the recovery device
  (endo-recovery-8a2744fe-3281-4d50-a6d1-0ad28e99c05c):
  node_invoke_timeout after 25000ms (attempt 4).
- Four attempts, zero responses. This meets the standing
  retry rule of at least 3 attempts before recording a unit
  as access-failed.

## Repeated failure mode

- This is the same blocker already filed as GitHub Issue #284
  (label tooling, still open at this pass): the forty-eighth
  consecutive pass with a Mac device-access blocker was
  ticker-1334 (scout-midday unit, 13:34 local), and this pass
  is the forty-ninth, tenth in the worsened zero-response
  form. The form has worsened since the afternoon of 2026-11-04
  from capture failure (OFF_SCREEN_WINDOW) to a fully offline
  device with a stalled invoke channel; the ticker-1025 pass
  classified it CHANNEL_STALL and noted recovery needs the
  Mac-side agent gateway restart before re-probing, and
  re-probing is owed only after device.list last_seen
  refreshes. That condition is not met - last_seen is still
  15:36:52Z - so no further probe was run this pass. This
  pass commented on #284 instead of filing a duplicate.
  Until the Mac gateway recovers, further ticker passes will
  fail their first unit the same way; the inbox held 42 units
  at this pass.

## Other pass steps

- Own PRs checked first: the live records PR for today is
  PR 310 (records/2026-11-05), verified MERGEABLE and CLEAN
  by the integrator at the 11:45 non-batch pass and awaiting
  the 15:00 batch; the newest comments are status notes from
  the ticker-1304, ticker-1334 and planner-1340 passes, no
  question addressed to this job, so nothing was owed before
  game work.
- Sync: reaped 0, expired 3 (harvest, survivors and training
  2026-11-05-1003), due 23, produced 6 units (harvest, radar,
  survivors, training, donations, arms-race 2026-11-05-1403);
  17 due regulars already queued. Zombie seeding skipped:
  zombie chain zombie-2026-10-28 closed with unit 066 on
  2026-10-30 (event ended about the 19:00 reset 2026-10-30,
  no Zombie tab in the Events hub), and the seeding rule
  forbids a fresh chain until a Zombie Invasion tab is seen
  live again.
- Pool note: this pass measured the pool on the
  records/2026-11-05 branch (inbox 42 units, done 850 at
  sync time). The main working tree's pool reads inbox 75 /
  done 925, but that tree sits on the stale
  work/ops-execution-records branch (queue state from
  2026-11-03) and holds another job's in-flight state - so
  the "pool inbox 75" figure was measured against that stale
  pool, not the records-branch pool. The records branch is
  the authoritative pool for ticker passes.
- No successor unit is enqueued from this unit - the chain's
  remainder is unchanged by a pass that read nothing, and a
  successor would hit the same stalled channel.
- Tracker untouched: a failed unit does not mark the
  regular, so the next tick re-produces the scout-midday
  unit.
- Delivery note: the local working tree sits on branch
  work/ops-execution-records and holds another job's
  in-flight state (unrelated modifications and deletions),
  so this pass's outputs were delivered through a temporary
  worktree onto the records/2026-11-05 branch, leaving that
  state undisturbed.

## Outcome

Failed. No surface walked or observed, no diamonds, money,
speedups or other spending. No alliance diplomacy, no
assembly, no teleport.

## Result stats

- target 1, achieved 0, resources_gained none, costs
  no_game_input, verified no, blocker_category e,
  device_takeovers 0, capture_attempts 4, issue 284
