---
title: Perception scout queue run 1710
created: 2026-11-07T01:10:00Z
modified: 2026-11-07T01:10:00Z
level: L0
version: 1.0.0
description: Ticker-1704 scout unit, failed on Mac mini offline with no wake-up path, same blocker as Issue 284
status: unverified
---

# 1710 queue run - Perception scout

Executor: ticker-1704. Unit: scout-2026-11-05-1800.
Session window about 17:04 to 17:10 America/Los_Angeles.

## Not performed

- No game screen was ever read and no game input was dispatched.
  The scout observes only - it never claims, fights, dispatches or
  buys - and here it observed nothing: zero surfaces walked, zero
  items observed, zero red dots seen or explained, no observation
  appended to the 2026-11-06 day observation file. The loss is the
  unexecuted scout check for this slot (stale unit from the
  2026-11-05 18:00 slot, planned_for 2026-11-06T02:00:00Z,
  expires 2026-11-07T02:00:00Z).

## Blocker, measured

- Device: Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd),
  listed offline. device.list last_seen 2026-11-05T15:36:52Z
  (07:36 local 2026-11-05) - stale about 33 hours 33 minutes at
  the 17:10 check, unchanged since the ticker-1507, ticker-1534,
  ticker-1604 and ticker-1634 passes.
- Seven device invokes, zero responses:
  - computer.session start (attempt 1) on the Mac mini:
    node_offline, "device is offline and does not advertise a
    wake-up path".
  - computer.session start (attempt 2) on the Mac mini:
    node_offline, same message.
  - computer.session start (attempt 3) on the Mac mini:
    node_offline, same message.
  - connection.health on the Mac mini: node_offline, same
    message.
  - connection.repair (target web) on the Mac mini:
    node_offline, same message.
  - connection.repair (target native) on the recovery device
    (endo-recovery-8a2744fe-3281-4d50-a6d1-0ad28e99c05c,
    "Zhen's Mac mini connection recovery"):
    node_invoke_timeout after 25000ms.
  - connection.health on the recovery device:
    node_invoke_timeout after 25000ms.
  This meets the standing retry rule of at least 3 attempts
  before recording a unit as access-failed.
- The recovery device's last_seen is frozen at the same
  2026-11-05T15:36:52Z as the Mac mini. No new recovery route
  was learned; the timeout signature matches the ticker-1235,
  ticker-1349, ticker-1507, ticker-1534, ticker-1604 and
  ticker-1634 passes.

## Repeated failure mode

- This is the same blocker already filed as GitHub Issue #284
  (label tooling, still open at this pass): the eighty-fourth
  recorded consecutive pass with a Mac device-access blocker,
  forty-fifth in the worsened zero-response form. The last
  recorded one was ticker-1634, the eighty-third and
  forty-fourth. No executed pass is recorded between 1634 and
  this one. This pass commented on #284 instead of filing
  a duplicate. Until the Mac gateway recovers, further ticker
  passes will fail their first unit the same way; the inbox
  held 70 units at this pass's stats (69 after this unit was
  claimed and completed as failed).

## Other pass steps

- Own PRs checked first: no open PR names this job as Owner.
  Records PR 369 (records/2026-11-06, post-1500 batch) is open
  and mergeable with no comments; older records PRs 351, 350,
  301, 265 and 256 remain open under the integrator. Nothing
  addressed to this job was open, so no branch-side
  reconciliation was attempted.
- Sync: reaped 0, expired 0, due 22, produced 0 new units, 22
  regulars already queued. Queue stats at 01:07Z: inbox 70,
  claimed 0, done 977, upcoming 53.
- No zombie seeding: zombie chain zombie-2026-10-28 closed
  with unit 066 on 2026-10-30 (event ended about the 19:00
  reset 2026-10-30, no Zombie tab in the Events hub), and the
  seeding rule forbids a fresh chain until a Zombie Invasion
  tab is seen live again.
- Pre-reset zero-sweep pair for the 2026-11-06 19:00 reset
  (chain pre-reset-sweep-2026-11-06) sits in the inbox
  (pending 2); not yet due, untouched by this pass.
- Scout state warning: this failed unit gives zero evidence
  about today's perception state. No observation file exists
  for the 2026-11-06 reset day and none was created - the
  last live scout observation remains the one recorded before
  the outage, and no scout unit has succeeded since the Mac
  went offline.
- Tracker untouched: a failed unit does not mark the regular,
  so the next tick re-produces the scout unit.
- Delivery note: the local working tree sits on branch
  work/ops-execution-records and holds another job's
  in-flight state (unrelated modifications and deletions),
  so this pass's outputs were delivered through a temporary
  worktree (ticker-1704-1106) onto the records/2026-11-06
  branch, leaving that state undisturbed. PR 369 already
  covers the branch, so no new PR was opened.
- The pass stopped after this one unit: with the device
  fully offline, further units would fail identically.

## Outcome

Failed. No game screen read, no observation produced, no
surfaces walked, no items observed. No diamonds, money,
speedups or other spending. No alliance diplomacy, no
assembly, no teleport.

## Result stats

- target 1, achieved 0, resources_gained none,
  costs no_game_input, verified no, blocker_category e,
  device_takeovers 0, capture_attempts 7, issue 284
