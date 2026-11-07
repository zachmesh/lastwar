---
title: Arms Race queue run 1734
created: 2026-11-07T01:56:00Z
modified: 2026-11-07T01:56:00Z
level: L0
version: 1.0.0
description: Ticker-1734 arms-race unit, failed on Mac mini offline with no wake-up path, same blocker as Issue 284
status: unverified
---

# 1734 queue run - Arms Race

Executor: ticker-1734. Unit: arms-race-2026-11-06-1403.
Session window about 17:34 to 17:56 America/Los_Angeles.

## Not performed

- No game screen was ever read and no game input was dispatched.
  Every device invoke to the Mac mini returned node_offline, so
  the Arms Race phase was never opened, no phase or score was
  read, no tier-3 target was worked toward, and no chest was
  claimed. The loss is the unexecuted arms-race check for this
  slot (duel day 5, planned 14:03 local 2026-11-06, expires
  18:03 local 2026-11-06).

## Blocker, measured

- Device: Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd),
  listed offline. device.list last_seen 2026-11-05T15:36:52Z
  (07:36 local 2026-11-05) - stale about 34 hours at the
  17:47 re-check, unchanged since the ticker-0741 pass.
- Six device invokes, zero responses:
  - computer.session start (attempt 1) on the Mac mini:
    node_offline, "device is offline and does not advertise a
    wake-up path".
  - connection.health (attempt 2) on the Mac mini:
    node_offline, same message.
  - computer.session start (attempt 3) on the Mac mini:
    node_offline, same message.
  - computer.session start (attempt 4, after a 45 second wait)
    on the Mac mini: node_offline, same message.
  - connection.repair web (attempt 5) on the Mac mini:
    node_offline, same message.
  - connection.health (attempt 6) on the recovery device
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
  the ticker-1704 pass's earlier recovery attempt.

## Repeated failure mode

- This is the same blocker already filed as GitHub Issue #284
  (label tooling, still open at this pass): the eighty-fifth
  recorded consecutive pass with a Mac device-access blocker,
  forty-sixth in the worsened zero-response form. The last
  recorded one was ticker-1704, the eighty-fourth and
  forty-fifth. No executed pass is recorded between 1704 and
  this one. This pass commented on #284 instead of filing a
  duplicate. Until the Mac gateway recovers, further ticker
  passes will fail their first unit the same way; the inbox
  held 77 units at this pass's stats.

## Other pass steps

- Own PRs checked first: PR 369 (records/2026-11-06,
  post-1500 batch) has no comments, is mergeable and CLEAN,
  Owner lastwar-pr-integrator; nothing addressed to this job
  was open. Older records PRs 351, 350, 301, 265 and 256 remain
  open under the integrator, unchanged.
- Sync: reaped 0, expired 0, due 20, produced nothing new, all
  20 regulars already queued. Queue stats at 01:47Z: inbox 77,
  claimed 0, done 1043, upcoming 52.
- No zombie seeding: zombie chain zombie-2026-10-28 closed
  with unit 066 on 2026-10-30 (event ended about the 19:00
  reset 2026-10-30, no Zombie tab in the Events hub), and the
  seeding rule forbids a fresh chain until a Zombie Invasion
  tab is seen live again.
- Pre-reset zero-sweep pair for the 2026-11-06 19:00 reset
  (chain pre-reset-sweep-2026-11-06) sits in the inbox
  (pending 2); the 17:30 sweep is due but needs the same
  offline device, so it was left untouched for the next tick.
- Tracker untouched: a failed unit does not mark the regular,
  so the next tick re-produces the arms-race unit.
- Delivery note: the local working tree sits on branch
  work/ops-execution-records and holds another job's
  in-flight state (unrelated modifications and deletions),
  so this pass's outputs were delivered through a temporary
  worktree onto the records/2026-11-06 branch, leaving that
  state undisturbed. PR 369 already covers the branch, so no
  new PR was opened.
- The pass stopped after this one unit: with the device
  fully offline, further units would fail identically.

## Outcome

Failed. No Arms Race screen read, no phase worked, no rewards
claimed. No diamonds, money, speedups or other spending. No
alliance diplomacy, no assembly, no teleport.

## Result stats

- target 1, achieved 0, resources_gained none,
  costs no_game_input, verified no, blocker_category e,
  device_takeovers 0, capture_attempts 6, issue 284
