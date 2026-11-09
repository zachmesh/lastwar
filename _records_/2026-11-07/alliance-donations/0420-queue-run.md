---
title: Donations queue run 0420
created: 2026-11-07T12:20:00Z
modified: 2026-11-07T12:24:00Z
level: L0
version: 1.0.0
description: Ticker-0420 donations unit, failed on Mac mini offline with no wake-up path, same blocker as Issue 284
status: unverified
---

# 0420 queue run - Alliance Donations

Executor: ticker-0420. Unit: donations-2026-11-07-0203.
Session window about 04:20 to 04:24 America/Los_Angeles.

## Not performed

- No game screen was ever read and no game input was dispatched.
  Every device invoke to the Mac mini returned node_offline or
  timed out, so the Alliance Techs screen was never opened, no
  live Donation Count was read and no coin donation was made.
  The loss is the unexecuted donations check for this slot
  (planned 02:03 local 2026-11-07, expires 06:03 local
  2026-11-07). The day's donation state is unknown from this
  pass - the 30 of 30 daily coin-donation target was neither
  advanced nor verified.

## Blocker, measured

- Device: Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd),
  listed offline. device.list last_seen 2026-11-05T15:36:52Z
  (07:36 local 2026-11-05) - stale about 45 hours at the
  04:22 re-check, unchanged since the ticker-0345 pass about
  35 minutes earlier.
- Six device invokes, zero responses:
  - computer.session start (attempt 1) on the Mac mini:
    node_offline, "device is offline and does not advertise a
    wake-up path".
  - connection.health (attempt 2) on the Mac mini:
    node_offline, same message.
  - connection.repair native (attempt 3) on the recovery
    device (endo-recovery-8a2744fe-3281-4d50-a6d1-0ad28e99c05c,
    "Zhen's Mac mini connection recovery"): node_invoke_timeout
    after 25000ms.
  - connection.health (attempt 4) on the recovery device:
    node_invoke_timeout after 25000ms.
  - computer.session start (attempt 5) on the Mac mini:
    node_offline, same message.
  - computer.session start (attempt 6, retry) on the Mac mini:
    node_offline, same message.
  A device.list re-check between attempts 5 and 6 confirmed
  the Mac mini still offline with last_seen unchanged. This
  meets the standing retry rule of at least 3 attempts
  before recording a unit as access-failed.
- Recovery-device attempts were made, as in recent passes: both
  timed out rather than answering node_offline, so the
  recovery channel accepts the invoke and never answers
  within 25 seconds. The recovery device's last_seen is frozen
  at the same 2026-11-05T15:36:52Z as the Mac mini. No new
  recovery route was learned; the timeout signature matches
  the ticker-0345, ticker-0304, ticker-0234 and ticker-0204
  passes.

## Repeated failure mode

- This is the same blocker already filed as GitHub Issue #284
  (label tooling, still open at this pass): the ninety-ninth
  recorded consecutive pass with a Mac device-access blocker,
  sixtieth in the worsened zero-response form. The last
  recorded one was ticker-0345, the ninety-eighth and
  fifty-ninth, about 35 minutes before this pass. No executed
  pass is recorded between 0345 and this one. This pass
  commented on #284 instead of filing a duplicate. Until the
  Mac gateway recovers, further ticker passes will fail their
  first unit the same way; the inbox held 75 units at this
  pass's stats (74 after this unit was claimed).

## Other pass steps

- Own PRs checked first: PR 382 (records/2026-11-07) is
  MERGEABLE/CLEAN after the integrator's 12:05Z correction of
  its own false conflict note (a real test merge into main
  9366c8c3 completed cleanly); it awaits the 07:00 batch, no
  merge this pass. The newest integrator comments name no
  question for this job. Older records PRs 351, 301, 265 and
  256 remain open under the integrator, unchanged.
- Sync: reaped 0, expired 0, due 20, produced nothing new,
  all 20 regulars already queued. Queue stats at 12:20Z:
  inbox 75, claimed 0, done 1096.
- No zombie seeding: zombie chain zombie-2026-10-28 closed
  with unit 066 on 2026-10-30 (event ended about the 19:00
  reset 2026-10-30, no Zombie tab in the Events hub), and the
  seeding rule forbids a fresh chain until a Zombie Invasion
  tab is seen live again.
- Pre-reset zero-sweep pair for the 2026-11-07 19:00 reset
  (chain pre-reset-sweep-2026-11-07) sits in the inbox
  (pending 2); not yet due, untouched by this pass.
- Tracker untouched: a failed unit does not mark the regular,
  so the next tick re-produces the donations unit.
- Delivery note: the local working tree sits on branch
  work/ops-execution-records and holds another job's
  in-flight state (unrelated modifications and deletions),
  so this pass's outputs were delivered through a temporary
  worktree onto the records/2026-11-07 branch, leaving that
  state undisturbed. PR 382 already covers the branch, so no
  new PR was opened.
- The pass stopped after this one unit: with the device
  fully offline, further units would fail identically.

## Outcome

Failed. No Alliance Techs screen read, no Donation Count
taken, no donation made, no coin spent. No diamonds, money,
speedups or other spending. No alliance diplomacy, no
assembly, no teleport.

## Result stats

- target 1, achieved 0, resources_gained none,
  costs no_game_input, verified no, blocker_category e,
  device_takeovers 0, capture_attempts 6, issue 284
