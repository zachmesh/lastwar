---
title: Alliance Donations queue run 1544
created: 2026-11-06T23:44:00Z
modified: 2026-11-06T23:44:00Z
level: L0
version: 1.0.0
description: Ticker-1534 donations unit, failed on Mac mini offline with no wake-up path, same blocker as Issue 284
status: unverified
---

# 1544 queue run - Alliance Donations

Executor: ticker-1534. Unit: donations-2026-11-06-1403.
Session window about 15:34 to 15:44 America/Los_Angeles.

## Not performed

- No game screen was ever read and no game input was dispatched.
  Every device invoke to the Mac mini returned node_offline or a
  timeout, so the Alliance Techs screen was never opened, no
  Donation Count was read, and no coin donation was made. The
  loss is the unexecuted donations check for this slot
  (planned 14:03 local 2026-11-06, expires 2026-11-07 02:03 UTC).

## Blocker, measured

- Device: Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd),
  listed offline. device.list last_seen 2026-11-05T15:36:52Z
  (07:36 local 2026-11-05) - stale about 32 hours at the
  15:41 re-check, unchanged since the ticker-1507 pass.
- Six device invokes, zero responses:
  - computer.session start (attempt 1) on the Mac mini:
    node_offline, "device is offline and does not advertise a
    wake-up path".
  - computer.session start (attempt 2, after a 20 second wait):
    node_offline, same message.
  - computer.session start (attempt 3, after a further 45
    second wait): node_offline, same message.
  - connection.health on the recovery device
    (endo-recovery-8a2744fe-3281-4d50-a6d1-0ad28e99c05c,
    "Zhen's Mac mini connection recovery"):
    node_invoke_timeout after 25000ms.
  - connection.repair (target native) on the recovery device:
    node_invoke_timeout after 25000ms.
  - computer.session start (attempt 4, after the repair
    attempt and a 30 second wait): node_offline, same message.
  This meets the standing retry rule of at least 3 attempts
  before recording a unit as access-failed.
- The recovery device's last_seen is frozen at the same
  2026-11-05T15:36:52Z as the Mac mini. No new recovery route
  was learned; the timeout signature matches the ticker-1235,
  ticker-1349 and ticker-1507 passes.

## Repeated failure mode

- This is the same blocker already filed as GitHub Issue #284
  (label tooling, still open at this pass): the eighty-first
  recorded consecutive pass with a Mac device-access blocker,
  forty-second in the worsened zero-response form. The last
  recorded one was ticker-1507, the eightieth and
  forty-first. No executed pass is recorded between 1507 and
  this one. This pass commented on #284 instead of filing
  a duplicate. Until the Mac gateway recovers, further ticker
  passes will fail their first unit the same way; the inbox
  held 73 units at this pass's stats (72 after this unit was
  claimed and completed as failed).

## Other pass steps

- Own PRs checked first: no open PR names this job as Owner.
  Records PR 369 (records/2026-11-06, post-1500 batch) is open
  under Owner lastwar-pr-integrator, mergeable, awaiting the
  19:00 batch point; PR 365 was merged at the 15:00 batch.
  Older records PRs 351, 350, 301, 265 and 256 remain open
  under the integrator, all still conflicting on the
  action-log append-append; nothing addressed to this job
  was open, so no branch-side reconciliation was attempted.
- Sync: reaped 0, expired 0, due 20, produced nothing new, all
  20 regulars already queued. Queue stats at 23:34Z: inbox 73,
  claimed 0, done 1042, upcoming 48.
- No zombie seeding: zombie chain zombie-2026-10-28 closed
  with unit 066 on 2026-10-30 (event ended about the 19:00
  reset 2026-10-30, no Zombie tab in the Events hub), and the
  seeding rule forbids a fresh chain until a Zombie Invasion
  tab is seen live again.
- Pre-reset zero-sweep pair for the 2026-11-06 19:00 reset
  (chain pre-reset-sweep-2026-11-06) sits in the inbox
  (pending 2); not yet due, untouched by this pass.
- Donations quota risk: the R3 two-hour checkpoint (about
  17:00 local, six hours is 13:00) cannot be read while the
  device is down, and the day's Donation Count is unread, so
  the 30-of-30 daily target is unverified for 2026-11-06.
  The 17:30 zero sweep will face the same blocker unless the
  gateway recovers.
- Tracker untouched: a failed unit does not mark the regular,
  so the next tick re-produces the donations unit.
- Delivery note: the local working tree sits on branch
  work/ops-execution-records and holds another job's
  in-flight state (unrelated modifications and deletions),
  so this pass's outputs were delivered through a temporary
  worktree onto the records/2026-11-06 branch (fast-forwarded
  to the remote tip 38ff3bd530 first; the local branch was
  behind), leaving that state undisturbed. PR 369 already
  covers the branch, so no new PR was opened.
- Note for the integrator: ticker-1507's radar failed-unit
  outputs did land on the branch (commit c4a1290b03) - the
  local branch was simply stale at this pass's first check,
  and the untracked copies in the main working tree are
  leftovers, not a delivery gap.
- The pass stopped after this one unit: with the device
  fully offline, further units would fail identically.

## Outcome

Failed. No Alliance Techs screen read, no Donation Count
read, no coin donation made. No diamonds, money, speedups or
other spending. No alliance diplomacy, no assembly, no
teleport.

## Result stats

- target 1, achieved 0, resources_gained none,
  costs no_game_input, verified no, blocker_category e,
  device_takeovers 0, capture_attempts 6, issue 284
