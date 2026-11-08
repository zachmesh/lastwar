---
title: Harvest queue run 1904
created: 2026-11-07T03:14:00Z
modified: 2026-11-07T03:15:00Z
level: L0
version: 1.0.0
description: Ticker-1904 harvest unit, failed on Mac mini offline with no wake-up path, same blocker as Issue 284
status: unverified
---

# 1904 queue run - Harvest

Executor: ticker-1904. Unit: harvest-2026-11-06-1803.
Session window about 19:04 to 19:15 America/Los_Angeles.

## Not performed

- No game screen was ever read and no game input was dispatched.
  Every device invoke to the Mac mini returned node_offline or
  timed out, so no resource bubble was collected, no edge drag
  was attempted, and the Armed Truck loot state was not checked.
  The loss is the unexecuted resource-collection sweep for this
  slot. The full-map zero-remaining acceptance is still unmet
  since the 2026-11-01 15:34 close, and the Armed Truck state
  is unknown since then.

## Blocker, measured

- Device: Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd),
  listed offline. device.list last_seen 2026-11-05T15:36:52Z
  (07:36 local Nov 5) - stale about 35 hours 37 minutes at the
  19:14 re-check, unchanged since the ticker-1827 pass. The
  last_seen value is known-stale (it did not move while
  ticker passes played the game on 2026-11-05), so it is
  reported as the listed value only, not as the outage start.
- Five device invokes, zero responses:
  - computer.session start, two attempts, both node_offline
    with "device is offline and does not advertise a wake-up
    path".
  - connection.health on the Mac mini, node_offline.
  - Recovery device (endo-recovery-8a2744fe-3281-4d50-a6d1-0ad28e99c05c):
    connection.repair (native) timed out after 25 seconds.
  - Recovery device: connection.health timed out after
    25 seconds. The recovery channel is not usable either.
- This meets the standing retry rule of at least 3 attempts
  before recording a unit as access-failed, and it is not the
  unreliable "lacks owner-authorized device access" error:
  the error is node_offline on the transport, with no wake-up
  path advertised.
- The unit's expires_at (2026-11-07T06:03:00Z) had not passed;
  the unit was claimed at 03:10Z, well before expiry.

## Repeated failure mode

- This is the same blocker already filed as GitHub Issue #284
  (label tooling, still open at this pass): the eighty-seventh
  recorded consecutive pass with a Mac device-access blocker,
  forty-eighth in the worsened zero-response form. The last
  recorded one was ticker-1827, the eighty-sixth and
  forty-seventh. This pass commented on #284 instead of filing
  a duplicate. Until the Mac gateway recovers, further ticker
  passes will fail their first unit the same way; the inbox
  held 67 units at this pass's close.

## Pre-reset zero sweep missed

- Both pre-reset zero-sweep units for the 2026-11-06 reset day
  expired unexecuted in this pass's sync:
  zero-sweep-pre-reset-sweep-2026-11-06-001 (17:30 slot) and
  -002 (18:30 slot). The 19:00 reset has now passed with no
  zero sweep of the daily collection ledger, so no ledger line
  was verified at zero for this reset day. The other six units
  expired in the same sync were duel-score-2026-11-06-1430,
  events-2026-11-06-1457, passes-2026-11-06-1457,
  secrets-2026-11-06-1457, treasures-2026-11-06-1457 and
  trucks-2026-11-06-1457.

## Other pass steps

- Own PRs checked first: PR 369 (records/2026-11-06, the live
  records PR for today) carries no comments. The other open
  records PRs (351, 350, 301, 265, 256) name
  lastwar-pr-integrator as Owner, not this job, and the
  integrator's own re-check comments note they are still
  conflicting on _logs_/repo-actions/action-log.jsonl; the
  pr-integration 1845 pass already re-verified that scope
  unchanged, so no PR action was needed this pass.
- Sync: reaped 0, expired 8, due 22, produced 4 new units
  (vip-2026-11-06-1800, daily-missions-2026-11-06-1800,
  duel-score-2026-11-06-1830, scout-2026-11-06-1800); the
  other 18 due regulars were already queued.
- No zombie seeding: zombie chain zombie-2026-10-28 closed
  with unit 066 on 2026-10-30 (event ended about the 19:00
  reset 2026-10-30, no Zombie tab in the Events hub), and the
  seeding rule forbids a fresh chain until a Zombie Invasion
  tab is seen live again.
- Tracker untouched: a failed unit does not mark the regular,
  so the next tick re-produces the harvest unit.
- Delivery note: the local working tree sits on branch
  work/ops-execution-records and holds another job's
  in-flight state (unrelated modifications and deletions),
  so this pass's outputs were delivered through a temporary
  worktree onto the records/2026-11-06 branch, leaving that
  state undisturbed.
