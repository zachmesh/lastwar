---
title: Scout 2026-11-14 ticker-1439 failed, Mac mini still offline
created: 2026-11-14T22:43:00Z
modified: 2026-11-14T22:43:00Z
version: 1.0.0
description: Perception scout unit scout-scout-2026-11-10-015 failed, Mac mini unreachable
status: failed
grounded_in:
  - source: device.list and device.describe on 1c817413-83e2-0545-cb90-36d5e096a6bd, 2026-11-14T22:41Z
  - source: device.invoke connection.health, environment.describe, connection.repair, computer.session, 2026-11-14T22:42Z
---

# Scout 2026-11-14 ticker-1439 failed, Mac mini still offline

- Executor: ticker-1439
- Unit: scout-scout-2026-11-10-015, chain scout-2026-11-10, seq 15
- Session window: 14:39-14:44 local, token held 14:41-14:44 local
- Status: failed, blocker_category f (missing precondition - device transport down)

## What was attempted

- Sync at 14:40 local: reaped 0, expired 14, due 22, produced 0
  (all due regulars already queued). Inbox 87, claimed 0, done 1979.
  Zombie seeding no-op - zombie-invasion unit 036 already in inbox.
  Branch reconcile warning persists (records/2026-11-14 has no remote
  ref; issue #446). Roster stale warning persists (building-queues,
  research, zombie-invasion; issue #198).
- Token acquired by ticker-1439 until 22:57:00Z. Next unit picked:
  scout-scout-2026-11-10-015.
- Device probe, 4 attempts, all failed identically:
  1. connection.health - node_offline
  2. environment.describe - node_offline
  3. connection.repair (target web) - node_offline
  4. computer.session start - node_offline
- device.list confirms Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd)
  offline, last seen 2026-11-12T17:52:28Z, unchanged since the 13:33
  pass, and does not advertise a wake-up path. No game state
  observable, no input sent, no observation made, no claims.

## Result

- No surfaces walked, no items observed, no red dots seen or
  explained. The scout observation file for 2026-11-14 is unchanged.
- This is NOT the outcome_unknown control-lock (Issue 689), so no
  blocker_overlay recorded; the next tick will probe again.
- Tracker untouched (failed unit).

## Chain continuation

Successor unit 016 in chain scout-2026-11-10 enqueued to start now,
following the pattern of the 09:34, 11:00, 12:04 and 13:28 passes,
each of which recorded one failed unit against the same outage and
enqueued its successor.

## Batch note

PR #708 is still open (per the 13:33 pass record; the VPS gh route
is down so this pass could not re-check it live). The 15:00 PT
batch point falls after this pass; if the delivery route is still
down then, it will be the 13th consecutive missed batch (11-12: 3,
11-13: 6, 11-14: 03:00, 07:00 and 11:00 so far).

## Delivery

VPS SSH still Permission denied (publickey), verified this pass -
the bundle push route is down and no PR for records/2026-11-14 can
be opened. This record, the completed unit file and the successor
unit are committed on the local records/2026-11-14 branch only;
push and PR are owed once the VPS route recovers. A second delivery
blocker stands: the Muse GitHub App has no write permission on
zachmesh/lastwar since the 2026-10-31 transfer (403 on issue,
comment and push).
