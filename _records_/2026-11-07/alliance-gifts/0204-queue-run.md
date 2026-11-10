---
title: Alliance Gifts queue run 0204
created: 2026-11-07T10:12:00Z
modified: 2026-11-07T10:12:00Z
level: L0
version: 1.0.0
description: Ticker-0204 gifts unit, failed on Mac mini offline with no wake-up path, same blocker as Issue 284
status: unverified
---

# 0204 queue run - Alliance Gifts

Executor: ticker-0204. Unit: gifts-2026-11-06-2230.
Session window about 02:04 to 02:12 America/Los_Angeles.

## Not performed

- No game screen was ever read and no game input was dispatched.
  Every device invoke to the Mac mini returned node_offline, so
  the Alliance panel was never opened, no Regular or Premium gift
  tab was claimed, and no gift level progress was read. The loss
  is the unexecuted gifts check for this slot (planned 22:30
  local 2026-11-06, expires 2026-11-07 02:30 local).

## Blocker, measured

- Device: Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd),
  listed offline. device.list last_seen 2026-11-05T15:36:52Z
  (07:36 local 2026-11-05) - stale about 42 hours 35 minutes
  at this pass, unchanged since the ticker-0011 pass.
- Five device invokes, zero responses:
  - computer.session start (attempt 1) on the Mac mini:
    node_offline, "device is offline and does not advertise a
    wake-up path".
  - computer.session start (attempt 2, retry) on the Mac mini:
    node_offline, same message.
  - connection.health (attempt 3) on the Mac mini:
    node_offline, same message.
  - connection.health (attempt 4) on the recovery device
    (endo-recovery-8a2744fe-3281-4d50-a6d1-0ad28e99c05c,
    "Zhen's Mac mini connection recovery"):
    node_invoke_timeout after 25000ms.
  - computer.session start (attempt 5, retry) on the Mac mini:
    node_offline, same message.
  This meets the standing retry rule of at least 3 attempts
  before recording a unit as access-failed.
- The recovery device's last_seen is frozen at the same
  2026-11-05T15:36:52Z as the Mac mini. No new recovery route
  was learned; the timeout signature matches the ticker-0127,
  ticker-0011 and ticker-2257 passes.

## Repeated failure mode

- This is the same blocker already filed as GitHub Issue #284
  (label tooling, still open at this pass): the ninety-fifth
  recorded consecutive pass with a Mac device-access blocker,
  fifty-sixth in the worsened zero-response form. The last
  recorded one was ticker-0127, the ninety-fourth and
  fifty-fifth. No executed pass is recorded between 0127 and
  this one. This pass commented on #284 instead of filing
  a duplicate. Until the Mac gateway recovers, further ticker
  passes will fail their first unit the same way; the inbox
  held 71 units at this pass's stats (70 after this unit was
  claimed).

## Other pass steps

- Own PRs checked first: no open PR names this job as Owner.
  Records PR 382 (records/2026-11-07) is open under Owner
  lastwar-pr-integrator, mergeable and clean, with no comments;
  nothing addressed to this job was open, so no branch-side
  reconciliation was attempted. Older records PRs 381, 351,
  350, 301, 265 and 256 remain open under the integrator.
- Sync: reaped 0, expired 5, due 20, produced nothing new, all
  20 regulars already queued. Queue stats at 10:05:45Z: inbox
  71, claimed 0, done 1084.
- The sync's 5 expirations are the unexecuted 2203-slot units
  (arms-race, donations, harvest, survivors, training, all
  expired 10:03:00Z). Four of them (arms-race, donations,
  survivors, training) are delivered here as inbox to done
  moves. Harvest is NOT delivered as expired: the branch
  already holds it failed by ticker-2257 (evidence
  _records_/2026-11-06/resource-collection/2257-queue-run.md),
  and that failed version is kept over this pass's stale-mirror
  expiration, the same reconciliation the ticker-0127 pass
  applied to radar-2026-11-06-2203.
- No zombie seeding: zombie chain zombie-2026-10-28 closed
  with unit 066 on 2026-10-30 (event ended about the 19:00
  reset 2026-10-30, no Zombie tab in the Events hub), and the
  seeding rule forbids a fresh chain until a Zombie Invasion
  tab is seen live again. No zombie unit sits in inbox or
  claimed.
- Pre-reset zero-sweep pair for the 2026-11-07 19:00 reset was
  already staged by ticker-0127 (chain
  pre-reset-sweep-2026-11-07, first pass not_before 17:30
  local, final pass 18:30 local); this pass staged nothing
  further.
- Tracker untouched: a failed unit does not mark the regular,
  so the next tick re-produces the gifts unit.
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

Failed. No Alliance screen read, no gift claimed, no gift
level progress read. No diamonds, money, speedups or other
spending. No alliance diplomacy, no assembly, no teleport.

## Result stats

- target 2, achieved 0, resources_gained none,
  costs no_game_input, verified no, blocker_category e,
  device_takeovers 0, capture_attempts 5, issue 284
