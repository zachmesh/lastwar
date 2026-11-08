---
title: Radar Tasks queue run 0304
created: 2026-11-07T11:04:00Z
modified: 2026-11-07T11:13:00Z
level: L0
version: 1.0.0
description: Ticker-0304 radar unit, failed on Mac mini offline with no wake-up path, same blocker as Issue 284; PR 382 conflict resolved first by union-merge
status: unverified
---

# 0304 queue run - Radar Tasks

Executor: ticker-0304. Unit: radar-2026-11-07-0203.
Session window about 03:04 to 03:13 America/Los_Angeles.

## Not performed

- No game screen was ever read and no game input was dispatched.
  Every device invoke to the Mac mini returned node_offline, so
  the radar was never opened, no stored task was Quick Executed
  and no map pin was worked. The loss is the unexecuted radar
  check for this slot (planned 02:03 local 2026-11-07, duel day
  6 radar stack window, expires 06:03 local 2026-11-07).

## Blocker, measured

- Device: Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd),
  listed offline. device.list last_seen 2026-11-05T15:36:52Z
  (07:36 local 2026-11-05) - stale about 43.5 hours at the
  03:10 re-check, unchanged since the ticker-0234 pass 30
  minutes earlier.
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
  the ticker-0234, ticker-0204 and ticker-0127 passes.

## Repeated failure mode

- This is the same blocker already filed as GitHub Issue #284
  (label tooling, still open at this pass): the ninety-seventh
  recorded consecutive pass with a Mac device-access blocker,
  fifty-eighth in the worsened zero-response form. The last
  recorded one was ticker-0234, the ninety-sixth and
  fifty-seventh, 30 minutes before this pass. No executed pass
  is recorded between 0234 and this one. This pass commented
  on #284 instead of filing a duplicate. Until the Mac gateway
  recovers, further ticker passes will fail their first unit
  the same way; the inbox held 72 units at this pass's stats
  (71 after this unit was claimed).

## Other pass steps

- Own PRs checked first: PR 382 (records/2026-11-07) was in
  CONFLICT with main 2d36115cd4 after the batch merged
  records PRs 350 and 381, single conflicting file
  _logs_/repo-actions/action-log.jsonl (append-append
  collision). This pass resolved it before any game work by
  union-merging main into records/2026-11-07 in worktree
  ticker-0304-1107: main's version kept whole including its
  line-join fix, the branch-only 9 lines appended, no line
  dropped (1016 lines, set-wise verified), committed as
  87ef39a4c4. The PR carries to the 07:00 batch. Older
  records PRs 351, 301, 265 and 256 remain open under the
  integrator, unchanged.
- Sync: reaped 0, expired 4 (events, secrets, treasures and
  trucks, all 2026-11-06-2257 slot), due 20, produced nothing
  new, all 20 regulars already queued. Queue stats at 11:08Z:
  inbox 72, claimed 0, done 1094.
- No zombie seeding: zombie chain zombie-2026-10-28 closed
  with unit 066 on 2026-10-30 (event ended about the 19:00
  reset 2026-10-30, no Zombie tab in the Events hub), and the
  seeding rule forbids a fresh chain until a Zombie Invasion
  tab is seen live again.
- Pre-reset zero-sweep pair for the 2026-11-07 19:00 reset
  (chain pre-reset-sweep-2026-11-07) sits in the inbox
  (pending 2); not yet due, untouched by this pass.
- Tracker untouched: a failed unit does not mark the regular,
  so the next tick re-produces the radar unit.
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

Failed. No radar screen read, no task executed or claimed.
No diamonds, money, speedups or other spending. No alliance
diplomacy, no assembly, no teleport.

## Result stats

- target 1, achieved 0, resources_gained none,
  costs no_game_input, verified no, blocker_category e,
  device_takeovers 0, capture_attempts 5, issue 284
