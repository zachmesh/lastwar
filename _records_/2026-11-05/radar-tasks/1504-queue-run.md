---
title: Radar tasks queue run 1504
created: 2026-11-05T23:04:00Z
modified: 2026-11-05T23:15:00Z
level: L0
version: 1.0.0
description: Ticker-1504 radar unit, failed on Mac mini offline with no wake-up path, same blocker as Issue 284
status: unverified
---

# 1504 queue run - radar tasks

Executor: ticker-1504. Unit: radar-2026-11-05-1403.
Session window about 15:04 to 15:15 America/Los_Angeles.

## Not performed

- No game screen was ever read and no game input was dispatched.
  Every device invoke to the Mac mini returned node_offline or
  timed out, so the radar screen could not be entered or
  verified, no stored task count, stamina figure or pin
  inventory was read, no Quick Execute batch was run and
  nothing was claimed. This was a stack-posture unit (duel
  day 4, window "duel day 4 - radar stack", radar_posture
  stack confirmed by tools/duel.py at 15:06): on a stack day
  nothing is claimed in any case, so the loss is the
  unexecuted ordinary tasks and the missing closing reads,
  not leaked claims.

## Blocker, measured

- Device: Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd),
  listed offline. device.list last_seen 2026-11-05T15:36:52Z
  (07:36 local) - stale about 7 hours 30 minutes at pass
  time, unchanged since the ticker-1025 pass.
- connection.health on the Mac mini: node_offline, device is
  offline and does not advertise a wake-up path (attempt 1).
- connection.health on the recovery device
  (endo-recovery-8a2744fe-3281-4d50-a6d1-0ad28e99c05c):
  node_invoke_timeout after 25000ms (attempt 2).
- connection.repair on the recovery device: first call
  rejected client-side (invalid_command_params, target "web"
  not accepted, expected "native" - my parameter error, no
  channel response); retried with target "native":
  node_invoke_timeout after 25000ms (attempt 3).
- connection.health on the Mac mini again: node_offline
  (attempt 4).
- Four channel attempts, zero responses. This meets the
  standing retry rule of at least 3 attempts before recording
  a unit as access-failed.

## Repeated failure mode

- This is the same blocker already filed as GitHub Issue #284
  (label tooling, still open at this pass): the fiftieth
  consecutive pass with a Mac device-access blocker was
  ticker-1434 (passes unit, 14:34 local), and this pass
  is the fifty-first. The form is unchanged since the
  afternoon of 2026-11-04 - a fully offline device with a
  stalled invoke channel; the ticker-1025 pass classified it
  CHANNEL_STALL and noted recovery needs the Mac-side agent
  gateway restart before re-probing, and re-probing is owed
  only after device.list last_seen refreshes. That condition
  is not met - last_seen is still 15:36:52Z - so no further
  probe was run this pass. This pass commented on #284
  instead of filing a duplicate. Until the Mac gateway
  recovers, further ticker passes will fail their first unit
  the same way; the inbox held 73 units at this pass.

## Other pass steps

- Own PRs checked first: the live records PR for today is
  PR 310 (records/2026-11-05), verified MERGEABLE and CLEAN
  by the integrator at the 11:45 non-batch pass and awaiting
  the 15:00 batch; the earlier action-log conflicts were
  already reconciled branch-side (ticker-0704, ticker-1134,
  planner-1140) and later passes advanced the branch head
  only. No question addressed to this job, so nothing was
  owed before game work.
- Sync: reaped 0, expired 4, due 21, produced nothing new,
  all 21 regulars already queued.
- No zombie seeding: zombie chain zombie-2026-10-28 closed
  with unit 066 on 2026-10-30 (event ended about the 19:00
  reset 2026-10-30, no Zombie tab in the Events hub), and the
  seeding rule forbids a fresh chain until a Zombie Invasion
  tab is seen live again.
- Tracker untouched: a failed unit does not mark the
  regular, so the next tick re-produces the radar unit.
- Delivery note: the local working tree sits on branch
  work/ops-execution-records and holds another job's
  in-flight state (unrelated modifications and deletions),
  so this pass's outputs were delivered through a temporary
  worktree onto the records/2026-11-05 branch, leaving that
  state undisturbed.

## Outcome

Failed. No radar task executed or claimed, no diamonds, money,
speedups or other spending. No alliance diplomacy, no
assembly, no teleport.

## Result stats

- target 12, achieved 0, resources_gained none, costs
  no_game_input, verified no, blocker_category e,
  device_takeovers 0, capture_attempts 4, issue 284
