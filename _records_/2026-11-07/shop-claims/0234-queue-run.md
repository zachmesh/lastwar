---
title: Shop Claims queue run 0234
created: 2026-11-07T10:34:00Z
modified: 2026-11-07T10:47:00Z
level: L0
version: 1.0.0
description: Ticker-0234 passes unit, failed on Mac mini offline with no wake-up path, same blocker as Issue 284
status: unverified
---

# 0234 queue run - Shop Claims

Executor: ticker-0234. Unit: passes-2026-11-06-2257.
Session window about 02:34 to 02:47 America/Los_Angeles.

## Not performed

- No game screen was ever read and no game input was dispatched.
  Every device invoke to the Mac mini returned node_offline, so
  the shop was never opened, no free pack or pass daily gift was
  claimed. The loss is the unexecuted passes check for this slot
  (planned 22:57 local 2026-11-06, expires 02:57 local
  2026-11-07).

## Blocker, measured

- Device: Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd),
  listed offline. device.list last_seen 2026-11-05T15:36:52Z
  (07:36 local 2026-11-05) - stale about 43 hours at the 02:46
  re-check, unchanged since the ticker-0204 pass 30 minutes
  earlier.
- Five device invokes, zero responses:
  - connection.health (attempt 1) on the Mac mini:
    node_offline, "device is offline and does not advertise a
    wake-up path".
  - connection.repair web (attempt 2) on the Mac mini:
    node_offline, same message.
  - computer.session start (attempt 3) on the Mac mini:
    node_offline, same message.
  - computer.session start (attempt 4, retry) on the Mac mini:
    node_offline, same message.
  - connection.health (attempt 5) on the recovery device
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
  the ticker-0204, ticker-1235 and ticker-1104 passes.

## Repeated failure mode

- This is the same blocker already filed as GitHub Issue #284
  (label tooling, still open at this pass): the ninety-sixth
  recorded consecutive pass with a Mac device-access blocker,
  fifty-seventh in the worsened zero-response form. The last
  recorded one was ticker-0204, the ninety-fifth and
  fifty-sixth, 30 minutes before this pass. No executed pass
  is recorded between 0204 and this one. This pass commented
  on #284 instead of filing a duplicate. Until the Mac gateway
  recovers, further ticker passes will fail their first unit
  the same way; the inbox held 66 units at this pass's stats
  (65 after this unit was claimed).

## Other pass steps

- Own PRs checked first: PR 382 (records/2026-11-07) has no
  comments and no reviews, Owner lastwar-pr-integrator;
  nothing addressed to this job was open. Older records PRs
  381, 351, 350, 301, 265 and 256 remain open under the
  integrator, unchanged.
- Sync: reaped 0, expired 4 (help, mail, star-ceremony and
  train, all 2026-11-06-2230 slot), due 20, produced nothing
  new, all 20 regulars already queued. Queue stats at 10:34Z:
  inbox 66, claimed 0, done 1089.
- No zombie seeding: zombie chain zombie-2026-10-28 closed
  with unit 066 on 2026-10-30 (event ended about the 19:00
  reset 2026-10-30, no Zombie tab in the Events hub), and the
  seeding rule forbids a fresh chain until a Zombie Invasion
  tab is seen live again.
- Pre-reset zero-sweep pair for the 2026-11-07 19:00 reset
  (chain pre-reset-sweep-2026-11-07) sits in the inbox
  (pending 2); not yet due, untouched by this pass.
- Tracker untouched: a failed unit does not mark the regular,
  so the next tick re-produces the passes unit.
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

Failed. No shop screen read, no free pack or pass gift claimed.
No diamonds, money, speedups or other spending. No alliance
diplomacy, no assembly, no teleport.

## Result stats

- target 1, achieved 0, resources_gained none,
  costs no_game_input, verified no, blocker_category e,
  device_takeovers 0, capture_attempts 5, issue 284
