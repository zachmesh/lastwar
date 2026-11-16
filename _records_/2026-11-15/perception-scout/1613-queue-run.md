---
title: Scout 2026-11-14 ticker-1604 failed, Mac mini offline
created: 2026-11-16T00:13:00Z
modified: 2026-11-16T00:13:00Z
version: 1.0.0
description: Scout unit scout-2026-11-14-1800 failed, Mac mini unreachable
status: failed
grounded_in:
  - source: device.list and device.describe on 1c817413-83e2-0545-cb90-36d5e096a6bd, 2026-11-16T00:06Z
  - source: device.invoke connection.health, computer.session, environment.describe, connection.repair, 2026-11-16T00:06Z to 00:11Z
  - source: public GitHub API open-PR list for zachmesh/lastwar, 2026-11-16T00:05Z
  - source: VPS SSH probe, 2026-11-16T00:04Z
---

# Scout 2026-11-14 ticker-1604 failed, Mac mini offline

- Executor: ticker-1604
- Unit: scout-2026-11-14-1800, regular scout, activity perception-scout, priority 2, est 10 minutes
- Session window: 16:04-16:13 local, token held 16:04-16:20 local
- Status: failed, blocker_category f (missing precondition - device transport down)

## Own PRs first

- Open PRs re-checked live this pass via the unauthenticated public
  GitHub API (the VPS gh route is down, SSH Permission denied,
  verified this pass): #711 knowledge (head
  work/ko-1132-lock-1047), #708 records 2026-11-12, #425 tools
  (head work/log-append-delivery-gate). None is owned by this job
  and nothing in them is addressed to it. No PR exists for
  records/2026-11-15. No action required from this pass.

## Sync and seed

- `queue.py sync`: reaped 0, expired 0, due 22, produced 0 (all due
  regulars already queued). One completion marker reaped:
  vip-2026-11-14-1800. Branch reconcile warning persists
  (records/2026-11-15 has no remote ref; issue #446).
- Zombie seeding: no-op - the Zombie Invasion event ended
  2026-10-30 (unit 066; Events hub holds 6 tabs, no Zombie
  Invasion tab; chain zombie-2026-10-28 closed). Per
  _activities_/zombie-invasion/INDEX.md, do NOT seed a fresh
  zombie chain until a Zombie Invasion tab is seen live in the
  Events hub again. No zombie-invasion unit sits in inbox or
  claimed.

## What was attempted

- Token acquired by ticker-1604 until 2026-11-16T00:20:44Z. Next unit picked:
  scout-2026-11-14-1800 (regular scout, activity perception-scout -
  post-reset full perception pass for the 2026-11-14 reset day).
- Device probe, 5 attempts, all failed with node_offline:
  1. device.describe - offline, last seen 2026-11-15T13:19:56Z
  2. connection.health - node_offline
  3. computer.session start - node_offline
  4. environment.describe - node_offline
  5. connection.repair (target web) - node_offline
- device.list confirms Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd)
  offline, last seen 2026-11-15T13:19:56Z (05:19 PT today), and
  does not advertise a wake-up path. Last seen is unchanged since
  the ticker-1202 pass about 4 hours ago. No game state
  observable, no input sent, no surfaces walked, no observation
  recorded, nothing spent.

## Result

- No observation, no claims, nothing spent. This is NOT the
  outcome_unknown control-lock (Issue 689), so no blocker_overlay
  recorded; the next tick will probe again.
- Tracker untouched (failed unit). The scout regular stays due
  and the next tick re-produces it. The 2026-11-14 post-reset
  scout pass remains unexecuted; its observation file for that
  reset day stays unwritten.
- The pass stops after this unit rather than cascading failed
  units through the pool: every remaining inbox unit needs the
  same offline device, and each failed claim would burn one of
  its 3 attempts for nothing. This follows the 2026-11-12
  ticker-0504 pattern.

## Chain continuation

- None. The scout chain head for 2026-11-14 cannot extend while
  the device is down; the next tick re-produces the scout unit.

## Batch note

- The delivery route is still down: VPS SSH Permission denied
  (publickey), verified this pass, so this pass's commit stays on
  the local records/2026-11-15 branch and no PR for
  records/2026-11-15 can be opened. records/2026-11-14 likewise
  never reached the remote. The 15:00 PT integrator batch is the
  next batch point; 19 batches have been missed so far.
- No unit has executed since 18:35 PT on 2026-11-14 (the
  ticker-1804 zombie unit). The Mac mini has now been offline
  for about 10 hours 54 minutes (last seen 05:19 PT), and the VPS
  SSH break is about 76 hours old; the owner chose the IONOS-console
  recovery on 2026-11-14 and it is not yet verified done.
