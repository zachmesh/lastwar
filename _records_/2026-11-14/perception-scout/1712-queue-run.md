---
title: Scout 2026-11-14 ticker-1712 failed, Mac mini still offline
created: 2026-11-15T01:19:00Z
modified: 2026-11-15T01:19:00Z
version: 1.0.0
description: Perception scout unit scout-scout-2026-11-10-016 failed, Mac mini unreachable
status: failed
grounded_in:
  - source: device.list and device.describe on 1c817413-83e2-0545-cb90-36d5e096a6bd, 2026-11-15T01:13Z
  - source: device.invoke connection.health, computer.session, screen.snap, connection.repair, 2026-11-15T01:13Z
---

# Scout 2026-11-14 ticker-1712 failed, Mac mini still offline

- Executor: ticker-1712
- Unit: scout-scout-2026-11-10-016, chain scout-2026-11-10, seq 16
- Session window: 17:12-17:19 local, token held 17:13-17:19 local
- Status: failed, blocker_category f (missing precondition - device transport down)

## Own PRs first

- Open PRs could NOT be re-checked live this pass: the VPS gh route is
  down (SSH Permission denied, verified this pass) and the unauthenticated
  public GitHub API is rate-limited (60/hour exhausted on the shared IP,
  reset 2026-11-15T01:42Z, about 25 minutes after this pass). Citing the
  ticker-1534 pass record (15:34 local): #708 records 2026-11-12, #711
  knowledge and #425 tools still open; none is owned by this job and
  nothing is addressed to it. No PR for records/2026-11-14 exists yet,
  and none could be opened this pass. No other job can have pushed since
  15:34 either - the push route is down for everyone - so the cited
  state stands.

## Sync and seed

- `queue.py sync`: reaped 0, expired 0, due 22, produced 0 (all due
  regulars already queued). One completion marker reaped:
  zombie-invasion-zombie-2026-11-10-036. Pool after sync: inbox 101,
  claimed 0, done 1986. Branch reconcile warning persists
  (records/2026-11-14 has no remote ref; issue #446). Roster stale
  warning persists (building-queues, research, zombie-invasion;
  issue #198).
- Zombie seeding: no-op - zombie-invasion-zombie-2026-11-10-037 already
  sits in inbox (successor enqueued by the ticker-1534 pass). The
  Zombie Invasion event (Glacieradon) was verified live by ticker-0004
  at about 00:04 PT with 1 day 17:37 left, so it should still be
  available; whether it is still live cannot be verified without the
  Mac, and the zombie units stay queued for a later tick to probe.

## What was attempted

- Token acquired by ticker-1712 until 01:28:28Z. Next unit picked:
  scout-scout-2026-11-10-016.
- Device probe, 4 attempts, all failed identically:
  1. connection.health - node_offline
  2. computer.session start - node_offline
  3. screen.snap - node_offline
  4. connection.repair (target web) - node_offline
- device.list confirms Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd)
  offline, last seen 2026-11-12T17:52:28Z, unchanged since the 15:34
  pass, and does not advertise a wake-up path. No game state
  observable, no input sent, no observation made, no claims.

## Result

- No surfaces walked, no items observed, no red dots seen or
  explained. The scout observation file for 2026-11-14 is unchanged.
- This is NOT the outcome_unknown control-lock (Issue 689), so no
  blocker_overlay recorded; the next tick will probe again.
- Tracker untouched (failed unit).

## Chain continuation

Successor unit 017 in chain scout-2026-11-10 enqueued to start now,
following the pattern of the 09:34, 11:00, 12:04, 13:28 and 15:34
passes, each of which recorded one failed unit against the same outage
and enqueued its successor.

## Batch note

PR #708 is still open (per the 15:34 pass record; the delivery route
is down so this pass could not re-check it live). The 15:00 PT batch
point has now also been missed - that is the 13th consecutive missed
batch (11-12: 3, 11-13: 6, 11-14: 03:00, 07:00, 11:00 and 15:00). The
next batch point is 19:00 PT; if the delivery route is still down
then, it will be the 14th.

## Delivery

VPS SSH still Permission denied (publickey), verified this pass -
the bundle push route is down and no PR for records/2026-11-14 can
be opened. The public GitHub API is additionally rate-limited until
01:42Z. This record, the completed unit file and the successor
unit are committed on the local records/2026-11-14 branch only;
push and PR are owed once the VPS route recovers. A second delivery
blocker stands: the Muse GitHub App has no write permission on
zachmesh/lastwar since the 2026-10-31 transfer (403 on issue,
comment and push).
