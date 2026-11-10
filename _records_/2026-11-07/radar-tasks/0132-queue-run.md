---
title: Radar Tasks queue run 0132
created: 2026-11-07T09:32:00Z
modified: 2026-11-07T09:32:00Z
level: L0
version: 1.0.0
description: Ticker-0127 radar unit, failed on Mac mini offline with no wake-up path, same blocker as Issue 284
status: unverified
---

# 0132 queue run - Radar Tasks

Executor: ticker-0127. Unit: radar-2026-11-06-2203.
Session window about 01:27 to 01:33 America/Los_Angeles.

## Not performed

- No game screen was ever read and no game input was dispatched.
  Every device invoke to the Mac mini returned node_offline, so
  the Radar screen was never opened, no radar task was read or
  claimed, and no duel-day radar release was collected. The loss
  is the unexecuted radar check for this slot (duel day 6,
  planned 22:03 local 2026-11-06, expires 2026-11-07 02:03
  local).

## Blocker, measured

- Device: Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd),
  listed offline. device.list last_seen 2026-11-05T15:36:52Z
  (07:36 local 2026-11-05) - stale about 41 hours 57 minutes
  at the 01:32 re-check, unchanged since the ticker-0011 pass.
- Six device invokes, zero responses:
  - computer.session start (attempt 1) on the Mac mini:
    node_offline, "device is offline and does not advertise a
    wake-up path".
  - connection.repair (attempt 2) on the recovery device
    (endo-recovery-8a2744fe-3281-4d50-a6d1-0ad28e99c05c,
    "Zhen's Mac mini connection recovery") with target "web":
    invalid_command_params, expected one of native - the
    recovery device's schema differs from the Mac mini's own,
    which lists "web".
  - connection.repair (attempt 2 corrected, target "native")
    on the recovery device: node_invoke_timeout after 25000ms.
  - connection.health (attempt 3) on the recovery device:
    node_invoke_timeout after 25000ms.
  - computer.session start (attempt 4, retry) on the Mac mini:
    node_offline, same message.
  - computer.session start (attempt 5, retry) on the Mac mini:
    node_offline, same message.
  This meets the standing retry rule of at least 3 attempts
  before recording a unit as access-failed.
- The recovery device's last_seen is frozen at the same
  2026-11-05T15:36:52Z as the Mac mini. No new recovery route
  was learned; the timeout signature matches the ticker-0011,
  ticker-2257 and ticker-2134 passes.

## Repeated failure mode

- This is the same blocker already filed as GitHub Issue #284
  (label tooling, still open at this pass): the ninety-fourth
  recorded consecutive pass with a Mac device-access blocker,
  fifty-fifth in the worsened zero-response form. The last
  recorded one was ticker-0011, the ninety-third and
  fifty-fourth. No executed pass is recorded between 0011 and
  this one. This pass commented on #284 instead of filing
  a duplicate. Until the Mac gateway recovers, further ticker
  passes will fail their first unit the same way; the inbox
  held 75 units at this pass's stats (77 after the sweep pair
  below was staged, 76 after this unit was claimed).

## Other pass steps

- Own PRs checked first: no open PR names this job as Owner.
  Records PR 382 (records/2026-11-07) is open under Owner
  lastwar-pr-integrator, mergeable and clean, with no comments;
  nothing addressed to this job was open, so no branch-side
  reconciliation was attempted. Older records PRs 381, 351,
  350, 301, 265 and 256 remain open under the integrator.
- Sync: reaped 0, expired 0, due 20, produced nothing new, all
  20 regulars already queued. Queue stats at 09:29:51Z: inbox
  75, claimed 0, done 1078, upcoming 49.
- No zombie seeding: zombie chain zombie-2026-10-28 closed
  with unit 066 on 2026-10-30 (event ended about the 19:00
  reset 2026-10-30, no Zombie tab in the Events hub), and the
  seeding rule forbids a fresh chain until a Zombie Invasion
  tab is seen live again. No zombie unit sits in inbox or
  claimed.
- Pre-reset zero-sweep pair for the 2026-11-07 19:00 reset was
  NOT staged: no chain pre-reset-sweep-2026-11-07 existed in
  the pool. This pass enqueued the pair per the queue design
  section 12 (chain pre-reset-sweep-2026-11-07, priority 1,
  est 15 minutes): unit 001 not_before 2026-11-08T01:30:00Z
  (17:30 local), unit 002 not_before 2026-11-08T02:30:00Z
  (18:30 local), both expiring at the 2026-11-08T03:00:00Z
  reset.
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

## Branch state note

- This unit was executed against the main working tree's
  queue mirror, which still held radar-2026-11-06-2203 in
  inbox. The records/2026-11-07 branch already carries the
  same unit completed as failed by ticker-0011 (evidence
  0011-queue-run.md, 4 invokes, 93rd consecutive pass), so
  this pass's re-attempt does not overwrite that completion:
  the branch keeps the 0011 done file, and this record file
  is the evidence of the re-attempt. The stale-mirror
  divergence is the known working-tree divergence already
  named in the 2026-11-06 retro; the integrator's merge
  reconciliation keeps the branch's true failed outcomes
  over main's stale re-creations.

## Outcome

Failed. No Radar screen read, no radar task claimed, no
duel-day release collected. No diamonds, money, speedups or
other spending. No alliance diplomacy, no assembly, no
teleport.

## Result stats

- target 1, achieved 0, resources_gained none,
  costs no_game_input, verified no, blocker_category e,
  device_takeovers 0, capture_attempts 6, issue 284
