---
title: Queue run 1100 - zombie-invasion unit 034 access failed
created: 2026-11-14T19:08:43Z
executor: ticker-1100
unit: zombie-invasion-zombie-2026-11-10-034
status: failed
---

# Queue run 1100 - zombie-invasion unit 034 (failed, Mac mini offline)

- Session window: 11:00-11:08 PT, 2026-11-14. Executor ticker-1100.
- Unit: zombie-invasion-zombie-2026-11-10-034, chain zombie-2026-11-10, seq 34,
  priority 4, est 12 minutes. Claimed 11:04 PT, lease to 11:24 PT.
- Result: failed. No game state was observable, no input was sent, no
  attacks, no kills, no claims. Blocker category f (missing precondition -
  device transport down).

## Device access - 4 attempts, all failed

Mac mini (device 1c817413-83e2-0545-cb90-36d5e096a6bd, Zhen's Mac mini)
is offline, last seen 2026-11-12T17:52:28Z - about 41 hours before this
pass. No wake-up path is advertised.

1. computer.session start - node_offline.
2. computer.session start (reopen and retry) - node_offline.
3. connection.health - node_offline.
4. connection.repair via the recovery device (Zhen's Mac mini connection
   recovery, target native) - node_invoke_timeout after 25 s.

This is the same failure mode as the previous zombie units in this
chain (030, 031) and the same outage that has blocked all game
execution since 2026-11-12 12:08 PT. It is NOT the outcome_unknown
control-lock (Issue 689): the device reports offline, not a stuck
session. No blocker_overlay is recorded; the next tick probes again.

## Pass context

- Own PRs first: open PRs re-checked read-only via the public API
  (VPS gh route down) - #711 knowledge (head e3c3dfd0, updated
  2026-11-12T20:04:57Z), #708 records 2026-11-12 (head 2f59c270,
  0 comments), #425 tools (head 4f41cdd6). Newest comment on #711 is
  still 2026-11-12T19:55:59Z (zachmesh); #708 has no comments. None
  is owned by this job and nothing is addressed to it. No
  records/2026-11-14 PR exists yet.
- Sync: reaped 0, expired 5, due 22, produced 0 (all already queued).
  Pool after sync: inbox 96, claimed 0, done 1962. Zombie seeding:
  no-op - unit 034 was already in inbox.
- Branch reconcile warning persists (records/2026-11-14 has no remote
  ref; issue #446). Roster stale warning persists (building-queues,
  research, zombie-invasion; issue #198).

## Chain continuation

Successor unit 035 in chain zombie-2026-11-10 is enqueued to start
now (cleared false - no zombies were observed, because no game state
was observable). The chain rule requires a successor after every
completed zombie unit.

## Batch note

PR #708 is still open, so the 07:00 PT batch point on 2026-11-14 is
the 11th consecutive missed batch (11-12: 3, 11-13: 6, 11-14 03:00
and 07:00). The 11:00 PT batch point falls inside this pass and
cannot merge either while the delivery route is down.

## Delivery

VPS SSH still Permission denied (publickey), verified this pass -
the bundle push route is down and no PR for records/2026-11-14 can
be opened. This record, the completed unit file and the successor
unit are committed on the local records/2026-11-14 branch only;
push and PR are owed once the VPS route recovers. A second delivery
blocker stands: the Muse GitHub App has no write permission on
zachmesh/lastwar since the 2026-10-31 transfer (403 on issue,
comment and push).
