---
title: Harvest 2026-11-15 ticker-1713 failed, Mac mini offline
created: 2026-11-16T01:22:00Z
modified: 2026-11-16T01:22:00Z
version: 1.0.0
description: Harvest unit harvest-2026-11-15-1403 failed, Mac mini unreachable
status: failed
grounded_in:
  - source: device.list and device.describe on 1c817413-83e2-0545-cb90-36d5e096a6bd, 2026-11-16T01:18Z
  - source: device.invoke connection.health and connection.repair, 2026-11-16T01:19Z to 01:21Z
  - source: public GitHub API open-PR list for zachmesh/lastwar, 2026-11-16T01:14Z
  - source: VPS SSH probe, 2026-11-16T01:13Z
---

# Harvest 2026-11-15 ticker-1713 failed, Mac mini offline

- Executor: ticker-1713
- Unit: harvest-2026-11-15-1403, regular harvest, activity resource-collection, priority 3, est 9 minutes
- Session window: 17:13-17:22 local, token held 17:13-17:33 local
- Status: failed, blocker_category f (missing precondition - device transport down)
- Known failure mode: Issue #284 (Mac device-access blocker, long-running; this pass adds one more occurrence, no new issue filed)

## Own PRs first

- Open PRs re-checked live this pass via the unauthenticated public
  GitHub API (the VPS gh route is down, SSH Permission denied,
  verified this pass): #711 knowledge (head
  work/ko-1132-lock-1047), #708 records 2026-11-12, #425 tools
  (head work/log-append-delivery-gate). None is owned by this job
  and nothing in them is addressed to it. No PR exists for
  records/2026-11-15. No action required from this pass.

## Sync and seed

- `queue.py sync`: reaped 0, expired 0, due 24, produced 2
  (research-2026-11-15-1403, building-queues-2026-11-15-1403).
  One completion marker reaped: zero-sweep-2026-11-15-1630.
  Branch reconcile warning persists (records/2026-11-15 has no
  remote ref; issue #446). Roster stale warning persists (live
  pool holds zombie-invasion units missing from the roster;
  issue #198).
- Zombie seeding: no-op - the Zombie Invasion event ended
  (Glacieradon; chain zombie-2026-11-10 closed, per the
  ticker-1634 record 30 minutes ago). No zombie-invasion unit
  sits in the live inbox or claimed. Note: the worktree snapshot
  inbox still holds the stale file
  zombie-invasion-zombie-2026-11-10-028.md, but the live pool
  does not - snapshot-only, not live state. No fresh chain
  seeded until a Zombie Invasion tab is seen live in the Events
  hub again.

## What was attempted

- Token acquired by ticker-1713 until 2026-11-16T01:33:32Z. Next unit picked:
  harvest-2026-11-15-1403 (regular harvest, activity
  resource-collection - collect building output bubbles and
  truck loot; planned for 22:03Z, expires 2026-11-16T02:03:00Z).
- Claimed by ticker-1713 at 2026-11-16T01:18:55Z, lease until 01:38:55Z.
- Device probes, all failed:
  1. device.list - Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd)
     offline, last seen 2026-11-15T13:19:56Z (05:19 PT today),
     no wake-up path advertised
  2. device.describe - offline, same last seen
  3. connection.health on the Mac mini - node_offline, device
     offline and does not advertise a wake-up path
  4. connection.health on the Mac mini connection recovery
     device - node_invoke_timeout after 25s
  5. connection.repair (target native) on the recovery device -
     node_invoke_timeout after 25s
- Last seen is unchanged since the ticker-1634 pass 30 minutes
  ago and the ticker-1604 pass before it. No game state
  observable, no input sent, nothing collected, nothing spent.
  This is the same outage as the 1634 pass, not a new blocker.

## Result

- No harvest, no claims, nothing spent. This is NOT the
  outcome_unknown control-lock (Issue 689), so no blocker_overlay
  recorded; the next tick will probe again.
- Tracker untouched (failed unit). The harvest regular stays due;
  the next tick re-produces it.
- The pass stops after this unit rather than cascading failed
  units through the pool: every remaining inbox unit needs the
  same offline device, and each failed claim would burn one of
  its 3 attempts for nothing. This follows the 2026-11-12
  ticker-0504 pattern and the ticker-1634 pass 30 minutes ago.

## Chain continuation

- None. Harvest is not a chain regular.

## Batch note

- The delivery route is still down: VPS SSH Permission denied
  (publickey), verified this pass, so this pass's commit stays on
  the local records/2026-11-15 branch and no PR for
  records/2026-11-15 can be opened. records/2026-11-14 likewise
  never reached the remote. The 19:00 PT integrator batch is the
  next batch point; the 15:00 batch was already counted as the
  nineteenth missed batch at the 1542 pass.
- No unit has executed since 18:35 PT on 2026-11-14 (the
  ticker-1804 zombie unit). The Mac mini has now been offline
  for about 12 hours (last seen 05:19 PT), and the VPS SSH break
  is about 76 hours old; the owner chose the IONOS-console
  recovery on 2026-11-14 and it is not yet verified done.
- The 17:30 pre-reset zero sweep (zero-sweep-2026-11-15-1730,
  chain pre-reset-sweep-2026-11-15 seq 2) sits in the live inbox
  with not_before 17:30 local; if the Mac stays offline it will
  expire unexecuted at the 19:00 reset like its 16:30 sibling.
