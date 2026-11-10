---
title: Radar queue run 1934
created: 2026-11-07T03:40:00Z
modified: 2026-11-07T03:40:00Z
level: L0
version: 1.0.0
description: Ticker-1934 radar unit, failed on Mac mini offline with no wake-up path, same blocker as Issue 284
status: unverified
---

# 1934 queue run - Radar

Executor: ticker-1934. Unit: radar-2026-11-06-1803.
Session window about 19:34 to 19:45 America/Los_Angeles.

## Not performed

- No game screen was ever read and no game input was dispatched.
  Every device invoke to the Mac mini returned node_offline, and
  the recovery channel timed out, so no radar task was executed,
  nothing was claimed, and no map pin was inventoried. The loss
  is the unexecuted radar slot for this cycle.
- Live duel posture from tools/duel.py at 19:38 local: duel day
  6, Enemy Buster, radar posture stack (day ends 2026-11-07
  18:00 local, 22.4 hours left). The unit window stamp reads
  "duel day 5 - radar release" - stale: the duel rolled over at
  about 18:00 local (02:00 UTC). Had the device been reachable,
  this unit would have run as a stack unit (complete, do not
  claim, keep headroom), not a release unit. The stamp staleness
  is a production-window artefact, not a schedule error.

## Blocker, measured

- Device: Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd),
  listed offline. device.list last_seen 2026-11-05T15:36:52Z
  (07:36 local Nov 5) - stale about 36 hours at the 19:38
  re-check, unchanged since the ticker-1025 pass on 2026-11-05.
  The last_seen value is known-stale (it did not move while
  ticker passes played the game on 2026-11-05), so it is
  reported as the listed value only, not as the outage start.
- Seven substantive device invokes, zero responses:
  - Mac mini connection.health, node_offline.
  - Mac mini connection.repair (web), node_offline.
  - Mac mini computer.session start, node_offline.
  - Mac mini computer.control activate LastWar, node_offline.
  - Mac mini computer.observe compact, node_offline.
    All five with "device is offline and does not advertise a
    wake-up path".
  - Recovery device (endo-recovery-8a2744fe-3281-4d50-a6d1-0ad28e99c05c):
    connection.health timed out after 25 seconds.
  - Recovery device: connection.repair (native) timed out
    after 25 seconds. The recovery channel is not usable either.
- This meets the standing retry rule of at least 3 attempts
  before recording a unit as access-failed, and it is not the
  unreliable "lacks owner-authorized device access" error:
  the error is node_offline on the transport, with no wake-up
  path advertised.
- The unit's expires_at (2026-11-07T06:03:00Z) had not passed;
  the unit was claimed at 03:37Z, well before expiry.

## Repeated failure mode

- This is the same blocker already filed as GitHub Issue #284
  (label tooling, still open at this pass): the eighty-eighth
  recorded consecutive pass with a Mac device-access blocker,
  forty-ninth in the worsened zero-response form. The last
  recorded one was ticker-1904, the eighty-seventh and
  forty-eighth. This pass commented on #284 instead of filing
  a duplicate. Until the Mac gateway recovers, further ticker
  passes will fail their first unit the same way; the inbox
  held 65 units at this pass's close.

## Pre-reset zero sweep

- Already recorded in the ticker-1904 record: both pre-reset
  zero-sweep units for the 2026-11-06 reset day expired
  unexecuted in that pass's sync, and the 19:00 reset passed
  with no zero sweep of the daily collection ledger. Nothing
  new to add this pass; the miss stands.

## Other pass steps

- Own PRs checked first: PR 374 (records/2026-11-06, the live
  records PR for today) is open, mergeable, CLEAN, with zero
  comments - nothing addressed to this job, no action needed.
  The other open records PRs (351, 350, 301, 265, 256) name
  lastwar-pr-integrator as Owner, not this job.
- Sync: reaped 0, expired 0, due 22, produced 0 new units;
  the 22 due regulars were already queued.
- No zombie seeding: zombie chain zombie-2026-10-28 closed
  with unit 066 on 2026-10-30 (event ended about the 19:00
  reset 2026-10-30, no Zombie tab in the Events hub), and the
  seeding rule forbids a fresh chain until a Zombie Invasion
  tab is seen live again.
- Tracker untouched: a failed unit does not mark the regular,
  so the next tick re-produces the radar unit.
- Delivery note: the local working tree sits on branch
  work/ops-execution-records and holds another job's
  in-flight state (unrelated modifications and deletions),
  so this pass's outputs were delivered through a temporary
  worktree onto the records/2026-11-06 branch, leaving that
  state undisturbed.
