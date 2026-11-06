---
title: Radar queue run 0741
created: 2026-11-06T15:52:00Z
modified: 2026-11-06T15:52:00Z
level: L0
version: 1.0.0
description: Ticker-0741 radar unit, failed on Mac mini offline with no wake-up path, same blocker as Issue 284
status: unverified
---

# 0741 queue run - Radar

Executor: ticker-0741. Unit: radar-2026-11-06-0603.
Session window about 07:41 to 07:52 America/Los_Angeles.

## Not performed

- No game screen was ever read and no game input was dispatched.
  Every device invoke to the Mac mini returned node_offline, so
  the radar release was never opened, no radar tasks were read,
  and nothing was claimed. The loss is the unexecuted radar
  release-day check for this slot (duel day 5, planned 06:03
  local 2026-11-06, expires 10:03 local 2026-11-06).

## Blocker, measured

- Device: Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd),
  listed offline. device.list last_seen 2026-11-05T15:36:52Z
  (07:36 local 2026-11-05) - stale about 24 hours 10 minutes at
  the 07:47 re-check, unchanged since the ticker-0704 pass.
- Five device invokes, zero responses:
  - computer.session start (attempts 1 and 2) on the Mac mini:
    node_offline, "device is offline and does not advertise a
    wake-up path".
  - connection.health (attempt 3) on the Mac mini: node_offline,
    same message.
  - connection.health (attempt 4) on the recovery device
    (endo-recovery-8a2744fe-3281-4d50-a6d1-0ad28e99c05c,
    "Zhen's Mac mini connection recovery"): node_invoke_timeout
    after 25000ms.
  - connection.repair native (attempt 5) on the recovery
    device: node_invoke_timeout after 25000ms.
  This meets the standing retry rule of at least 3 attempts
  before recording a unit as access-failed.
- Recovery-device attempts WERE made in this pass, unlike the
  ticker-0342 pass: both timed out rather than answering
  node_offline, so the recovery channel is not dead-quiet - it
  accepts the invoke and never answers within 25 seconds. The
  recovery device's last_seen is frozen at the same
  2026-11-05T15:36:52Z as the Mac mini. No new recovery route
  was learned; the timeout signature matches the ticker-0234
  pass's earlier recovery attempt.

## Repeated failure mode

- This is the same blocker already filed as GitHub Issue #284
  (label tooling, still open at this pass): the seventy-fourth
  recorded consecutive pass with a Mac device-access blocker,
  thirty-fifth in the worsened zero-response form. The last
  recorded one was ticker-0704, the seventy-third and
  thirty-fourth. No executed pass is recorded between 0704 and
  this one: the latest executed failure in the pool is the
  0704 harvest unit (finished 15:14:39Z). This pass commented on #284 instead of filing a
  duplicate. Until the Mac gateway recovers, further ticker
  passes will fail their first unit the same way; the inbox
  held 79 units at this pass's stats.

## Other pass steps

- Own PRs checked first: PR 359 (records/2026-11-06,
  post-0700 batch) has no comments and Owner
  lastwar-pr-integrator; PRs 360 and 361 are knowledge folds
  owned by the ko-0732 job, not this ticker. Nothing addressed
  to this job was open.
- Sync: reaped 0, expired 6, due 20, produced nothing new, all
  20 regulars already queued. Queue stats at 15:43Z: inbox 79,
  claimed 0, done 1009, upcoming 53.
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
  state undisturbed. PR 359 already covers the branch, so no
  new PR was opened.
- The pass stopped after this one unit: with the device
  fully offline, further units would fail identically.

## Outcome

Failed. No radar screen read, no tasks run, no rewards claimed.
No diamonds, money, speedups or other spending. No alliance
diplomacy, no assembly, no teleport.

## Result stats

- target 1, achieved 0, resources_gained none,
  costs no_game_input, verified no, blocker_category e,
  device_takeovers 0, capture_attempts 5, issue 284
