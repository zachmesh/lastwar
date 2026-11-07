---
title: Arms Race queue run 0858
created: 2026-11-07T16:58:00Z
modified: 2026-11-07T17:00:00Z
level: L0
version: 1.0.0
description: Ticker-0858 arms-race unit, failed on Mac mini offline with no wake-up path, same blocker as Issue 284
status: unverified
---

# 0858 queue run - Arms Race

Executor: ticker-0858. Unit: arms-race-2026-11-07-0603.
Session window about 08:58 to 09:00 America/Los_Angeles.

## Not performed

- No game screen was ever read and no game input was dispatched.
  Every device invoke to the Mac mini returned node_offline or
  timed out, so the Arms Race phase was never read, no live score
  was taken, no scoring action was done, no chest was claimed.
  The loss is the unexecuted arms-race unit for this slot
  (planned 06:03 local 2026-11-07, expires 10:03 local
  2026-11-07, window duel day 6). Whether the live phase's top
  chest threshold stood met or short is unknown from this pass -
  nothing was read live and nothing was executed or claimed.

## Blocker, measured

- Device: Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd),
  listed offline. device.list last_seen 2026-11-05T15:36:52Z
  (07:36 local 2026-11-05) - stale about 48 hours at the
  09:00 re-check, unchanged since the ticker-0804 pass about
  30 minutes earlier.
- Six device invokes, zero responses:
  - computer.session start (attempt 1) on the Mac mini:
    node_offline, "device is offline and does not advertise a
    wake-up path".
  - computer.session start (attempt 2) on the Mac mini:
    node_offline, same message.
  - computer.session start (attempt 3) on the Mac mini:
    node_offline, same message.
  - connection.health (attempt 4) on the Mac mini:
    node_offline, same message.
  - connection.repair web (attempt 5) on the Mac mini:
    node_offline, same message.
  - connection.health (attempt 6) on the recovery device
    (endo-recovery-8a2744fe-3281-4d50-a6d1-0ad28e99c05c,
    "Zhen's Mac mini connection recovery"): node_invoke_timeout
    after 25000ms.
  A device.list re-check between attempts confirmed the Mac
  mini still offline with last_seen unchanged. This meets the
  standing retry rule of at least 3 attempts before recording
  a unit as access-failed.
- The recovery-device attempt was made, as in recent passes:
  it timed out rather than answering node_offline, so the
  recovery channel accepts the invoke and never answers
  within 25 seconds. The recovery device's last_seen is frozen
  at the same 2026-11-05T15:36:52Z as the Mac mini. No new
  recovery route was learned; the timeout signature matches
  the ticker-0804, ticker-0734, ticker-0704, ticker-0633,
  ticker-0526, ticker-0420 and ticker-0345 passes.

## Repeated failure mode

- This is the same blocker already filed as GitHub Issue #284
  (label tooling, still open at this pass): the one-hundred-fifth
  recorded consecutive pass with a Mac device-access blocker,
  sixty-sixth in the worsened zero-response form. The last
  recorded one was ticker-0804, the one-hundred-fourth, about
  30 minutes before this pass. No executed pass is recorded
  between 0804 and this one. This pass commented on #284
  instead of filing a duplicate. Until the Mac gateway recovers,
  further ticker passes will fail their first unit the same way;
  the inbox held 77 units at this pass's stats (77 after this
  unit was claimed, 76 once it completes as failed).

## Other pass steps

- Own PRs checked first: PR 392 (records/2026-11-07) is open,
  MERGEABLE, CLEAN, 0 comments - nothing addressed to this job.
  Older records PRs 351, 301 and 256 remain open under the
  integrator, unchanged.
- Sync: reaped 0, expired 0, due 20, produced nothing new,
  all 20 regulars already queued. Queue stats at 16:58Z:
  inbox 77, claimed 0, done 1113.
- No zombie seeding: zombie chain zombie-2026-10-28 closed
  with unit 066 on 2026-10-30 (event ended about the 19:00
  reset 2026-10-30, no Zombie tab in the Events hub), and the
  seeding rule forbids a fresh chain until a Zombie Invasion
  tab is seen live again.
- Pre-reset zero-sweep pair for the 2026-11-07 19:00 reset
  (chain pre-reset-sweep-2026-11-07) sits in the inbox
  (pending 2); not yet due, untouched by this pass.
- Tracker untouched: a failed unit does not mark the regular,
  so the next tick re-produces the arms-race unit.
- Delivery note: the local working tree sits on branch
  work/ops-execution-records and holds another job's
  in-flight state (unrelated modifications and deletions),
  so this pass's outputs were delivered through a temporary
  worktree onto the records/2026-11-07 branch, leaving that
  state undisturbed. PR 392 already covers the branch, so no
  new PR was opened.
- The pass stopped after this one unit: with the device
  fully offline, further units would fail identically.

## Outcome

Failed. No Arms Race screen read, no score taken, no action
done, no chest claimed. No diamonds, money, speedups or other
spending. No alliance diplomacy, no assembly, no teleport.

## Result stats

- target 1, achieved 0, resources_gained none,
  costs no_game_input, verified no, blocker_category e,
  device_takeovers 0, capture_attempts 6, issue 284
