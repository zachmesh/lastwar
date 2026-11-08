---
title: Harvest queue run 0526
created: 2026-11-07T13:26:00Z
modified: 2026-11-07T13:33:00Z
level: L0
version: 1.0.0
description: Ticker-0526 harvest unit, failed on Mac mini offline with no wake-up path, same blocker as Issue 284
status: unverified
---

# 0526 queue run - Resource Collection

Executor: ticker-0526. Unit: harvest-2026-11-07-0203.
Session window about 05:26 to 05:33 America/Los_Angeles.

## Not performed

- No game screen was ever read and no game input was dispatched.
  Every device invoke to the Mac mini returned node_offline or
  timed out, so the base screen was never opened, no output
  bubble was collected and no Armed Truck loot was claimed.
  The loss is the unexecuted harvest check for this slot
  (planned 02:03 local 2026-11-07, expires 06:03 local
  2026-11-07). Whether any bubble sat full and stalled
  production is unknown from this pass - no bubble was read
  live and no collection happened.

## Blocker, measured

- Device: Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd),
  listed offline. device.list last_seen 2026-11-05T15:36:52Z
  (07:36 local 2026-11-05) - stale about 46 hours at the
  05:30 re-check, unchanged since the ticker-0420 pass about
  70 minutes earlier.
- Seven device invokes, zero responses:
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
  - connection.repair web (attempt 6) on the Mac mini:
    node_offline, same message.
  - computer.session start (attempt 7) on the Mac mini:
    node_offline, same message.
  A device.list re-check between attempts confirmed the Mac
  mini still offline with last_seen unchanged. This meets the
  standing retry rule of at least 3 attempts before recording
  a unit as access-failed.
- Recovery-device attempts were made, as in recent passes: both
  timed out rather than answering node_offline, so the
  recovery channel accepts the invoke and never answers
  within 25 seconds. The recovery device's last_seen is frozen
  at the same 2026-11-05T15:36:52Z as the Mac mini. No new
  recovery route was learned; the timeout signature matches
  the ticker-0420, ticker-0345, ticker-0304, ticker-0234 and
  ticker-0204 passes.

## Repeated failure mode

- This is the same blocker already filed as GitHub Issue #284
  (label tooling, still open at this pass): the one-hundredth
  recorded consecutive pass with a Mac device-access blocker,
  sixty-first in the worsened zero-response form. The last
  recorded one was ticker-0420, the ninety-ninth and
  sixtieth, about 70 minutes before this pass. No executed
  pass is recorded between 0420 and this one. This pass
  commented on #284 instead of filing a duplicate. Until the
  Mac gateway recovers, further ticker passes will fail their
  first unit the same way; the inbox held 74 units at this
  pass's stats (73 after this unit was claimed).

## Other pass steps

- Own PRs checked first: PR 382 (records/2026-11-07) is
  MERGEABLE/CLEAN after the integrator's 12:05Z correction of
  its own false conflict note (a real test merge into main
  9366c8c3 completed cleanly); it awaits the 07:00 batch, no
  merge this pass. The newest integrator comments name no
  question for this job. Older records PRs 351, 301, 265 and
  256 remain open under the integrator, unchanged.
- Sync: reaped 0, expired 0, due 20, produced nothing new,
  all 20 regulars already queued. Queue stats at 13:27Z:
  inbox 74, claimed 0, done 1097.
- No zombie seeding: zombie chain zombie-2026-10-28 closed
  with unit 066 on 2026-10-30 (event ended about the 19:00
  reset 2026-10-30, no Zombie tab in the Events hub), and the
  seeding rule forbids a fresh chain until a Zombie Invasion
  tab is seen live again.
- Pre-reset zero-sweep pair for the 2026-11-07 19:00 reset
  (chain pre-reset-sweep-2026-11-07) sits in the inbox
  (pending 2); not yet due, untouched by this pass.
- Tracker untouched: a failed unit does not mark the regular,
  so the next tick re-produces the harvest unit.
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

Failed. No base screen read, no bubble collected, no truck
loot claimed. No diamonds, money, speedups or other spending.
No alliance diplomacy, no assembly, no teleport.

## Result stats

- target 1, achieved 0, resources_gained none,
  costs no_game_input, verified no, blocker_category e,
  device_takeovers 0, capture_attempts 7, issue 284
