---
title: Harvest queue run 0704
created: 2026-11-07T15:04:00Z
modified: 2026-11-07T15:15:00Z
level: L0
version: 1.0.0
description: Ticker-0704 harvest unit, failed on Mac mini offline with no wake-up path, same blocker as Issue 284
status: unverified
---

# 0704 queue run - Resource Collection

Executor: ticker-0704. Unit: harvest-2026-11-07-0603.
Session window about 07:04 to 07:15 America/Los_Angeles.

## Not performed

- No game screen was ever read and no game input was dispatched.
  Every device invoke to the Mac mini returned node_offline or
  timed out, so the base screen was never opened, no output
  bubble was collected and no Armed Truck loot was claimed.
  The loss is the unexecuted harvest check for this slot
  (planned 06:03 local 2026-11-07, expires 10:03 local
  2026-11-07). Whether any bubble sat full and stalled
  production is unknown from this pass - no bubble was read
  live and no collection happened.

## Blocker, measured

- Device: Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd),
  listed offline. device.list last_seen 2026-11-05T15:36:52Z
  (07:36 local 2026-11-05) - stale about 47.5 hours at the
  07:14 re-check, unchanged since the ticker-0633 pass about
  30 minutes earlier.
- Four device invokes, zero responses:
  - computer.session start (attempt 1) on the Mac mini:
    node_offline, "device is offline and does not advertise a
    wake-up path".
  - connection.health (attempt 2) on the Mac mini:
    node_offline, same message.
  - computer.session start (attempt 3) on the Mac mini:
    node_offline, same message.
  - connection.health (attempt 4) on the recovery device
    (endo-recovery-8a2744fe-3281-4d50-a6d1-0ad28e99c05c,
    "Zhen's Mac mini connection recovery"): node_invoke_timeout
    after 25000ms.
  A device.list re-check between attempts confirmed the Mac
  mini still offline with last_seen unchanged. This meets the
  standing retry rule of at least 3 attempts before recording
  a unit as access-failed.
- Recovery-device attempt was made, as in recent passes: it
  timed out rather than answering node_offline, so the
  recovery channel accepts the invoke and never answers
  within 25 seconds. The recovery device's last_seen is frozen
  at the same 2026-11-05T15:36:52Z as the Mac mini. No new
  recovery route was learned; the timeout signature matches
  the ticker-0633, ticker-0526, ticker-0420, ticker-0345,
  ticker-0304 and ticker-0234 passes.

## Repeated failure mode

- This is the same blocker already filed as GitHub Issue #284
  (label tooling, still open at this pass): the one-hundred-second
  recorded consecutive pass with a Mac device-access blocker,
  sixty-third in the worsened zero-response form. The last
  recorded one was ticker-0633, the one-hundred-first and
  sixty-second, about 30 minutes before this pass. No executed
  pass is recorded between 0633 and this one. This pass
  commented on #284 instead of filing a duplicate. Until the
  Mac gateway recovers, further ticker passes will fail their
  first unit the same way; the inbox held 69 units at this
  pass's stats (68 after this unit was claimed).

## Other pass steps

- Own PRs checked first: the four older open records PRs
  (351 for 2026-11-05, 301 for 2026-11-04, 265 for
  2026-11-02, 256 for 2026-11-03) are all MERGEABLE/CLEAN
  against current main dc94999c at this pass's check, so the
  action-log conflict the integrator noted at the 03:00 batch
  no longer stands and no branch-side reconciliation is owed
  by this job; the newest integrator comments name no
  question for this job. The four PRs await the 07:00 batch
  (integrator's merge, not this pass's). No open PR exists for
  records/2026-11-07 (PR 382 was merged into main at
  dc94999c); this pass opens a fresh one for the branch
  after pushing.
- Sync: reaped 0, expired 6, due 22, produced one new unit
  (duel-score-2026-11-07-0630), all other due regulars
  already queued. Queue stats at 15:06Z: inbox 69, claimed 0,
  done 1049.
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
  state undisturbed.
- The pass stopped after this one unit: with the device
  fully offline, further units would fail identically.

## Outcome

Failed. No base screen read, no bubble collected, no truck
loot claimed. No diamonds, money, speedups or other spending.
No alliance diplomacy, no assembly, no teleport.

## Result stats

- target 1, achieved 0, resources_gained none,
  costs no_game_input, verified no, blocker_category e,
  device_takeovers 0, capture_attempts 4, issue 284
