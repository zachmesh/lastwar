---
title: Queue run 1333 - zombie-invasion unit 035 access failed
created: 2026-11-14T21:36:00Z
executor: ticker-1328
unit: zombie-invasion-zombie-2026-11-10-035
status: failed
---

# Queue run 1333 - zombie-invasion unit 035 (failed, Mac mini offline)

- Session window: 13:28-13:36 PT, 2026-11-14. Executor ticker-1328.
- Unit: zombie-invasion-zombie-2026-11-10-035, chain zombie-2026-11-10, seq 35,
  priority 4, est 12 minutes. Claimed 13:33 PT, lease to 13:53 PT.
- Result: failed. No game state was observable, no input was sent, no
  attacks, no kills, no claims. Blocker category f (missing precondition -
  device transport down).

## Device access - 4 attempts, all failed

Mac mini (device 1c817413-83e2-0545-cb90-36d5e096a6bd, Zhen's Mac mini)
is offline, last seen 2026-11-12T17:52:28Z - about 52 hours before this
pass. No wake-up path is advertised.

1. connection.health - node_offline.
2. environment.describe - node_offline.
3. connection.repair (target web) - node_offline.
4. computer.session start - node_offline.

This is the same failure mode as the previous zombie units in this
chain (028-034) and the same outage that has blocked all game
execution since 2026-11-12 12:08 PT. It is NOT the outcome_unknown
control-lock (Issue 689): the device reports offline, not a stuck
session. No blocker_overlay is recorded; the next tick probes again.
This is the 8th consecutive zombie-chain node_offline failure
(028-035) and the 23rd device-offline occurrence recorded by this
queue, the 8th ticker pass today to record the Mac offline (0445,
0604, 0704, 0804, 0934, 1100, 1204, 1328).

## Pass context

- Own PRs first: the VPS gh route is down (SSH Permission denied,
  verified this pass), and the read-only fallback via the public
  GitHub API is rate-limited for this VM's egress IPs this pass,
  so no fresh PR state could be read. Last verified state (13:08 PT
  pr-catchall pass): #711 knowledge (head e3c3dfd0), #708 records
  2026-11-12 (head 2f59c270, 0 comments), #425 tools (head
  4f41cdd6). None is owned by this job and nothing is addressed to
  it. No records/2026-11-14 PR exists yet.
- Sync: reaped 0, expired 0, due 22, produced 0 (all already queued).
  Pool after sync: inbox 101, claimed 0, done 1964. Zombie seeding:
  no-op - unit 035 was already in inbox.
- Branch reconcile warning persists (records/2026-11-14 has no remote
  ref; issue #446). Roster stale warning persists (building-queues,
  research, zombie-invasion; issue #198).

## Chain continuation

Successor unit 036 in chain zombie-2026-11-10 is enqueued to start
now (cleared false - no zombies were observed, because no game state
was observable). The chain rule requires a successor after every
completed zombie unit.

## Batch note

PR #708 is still open, so the 11:00 PT batch point on 2026-11-14 is
the 12th consecutive missed batch (11-12: 3, 11-13: 6, 11-14 03:00,
07:00 and 11:00). The 15:00 PT batch point falls after this pass and
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
