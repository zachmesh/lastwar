---
title: Harvest 2026-11-15 ticker-0934 failed, Mac mini offline
created: 2026-11-15T17:45:00Z
modified: 2026-11-15T17:45:00Z
version: 1.0.0
description: Harvest unit harvest-2026-11-15-0603 failed, Mac mini unreachable
status: failed
grounded_in:
  - source: device.list and device.describe on 1c817413-83e2-0545-cb90-36d5e096a6bd, 2026-11-15T17:42Z
  - source: device.invoke connection.health, computer.session, connection.repair, screen.snap, 2026-11-15T17:43Z
---

# Harvest 2026-11-15 ticker-0934 failed, Mac mini offline

- Executor: ticker-0934
- Unit: harvest-2026-11-15-0603, regular harvest, activity resource-collection, priority 3, est 9 minutes
- Session window: 09:34-09:50 local, token held 09:42-09:56 local
- Status: failed, blocker_category f (missing precondition - device transport down)

## Own PRs first

- Open PRs re-checked live this pass via the unauthenticated public
  GitHub API (the VPS gh route is down, SSH Permission denied,
  verified this pass; local gh has no login): #711 knowledge
  (head work/ko-1132-lock-1047), #708 records 2026-11-12, #425
  tools (head work/log-append-delivery-gate). None is owned by
  this job and nothing in the newest comments is addressed to it:
  #708 has no comments; #711's newest comment (zachmesh,
  2026-11-12) is a note for the integrator and the next
  knowledge-organizer run about PR #710 having merged after #711
  opened; #425's newest comments are integrator notes about its
  conflict. No PR exists for records/2026-11-14 or
  records/2026-11-15. No action required from this pass.

## Sync and seed

- `queue.py sync`: reaped 0, expired 0, due 22, produced 0 (all due
  regulars already queued). One completion marker reaped:
  scout-scout-2026-11-10-017. Branch reconcile warning
  persists (records/2026-11-15 has no remote ref; issue #446).
  Roster stale warning persists (building-queues, research;
  issue #198).
- Zombie seeding: no-op - the Glacieradon event ended (verified
  live by ticker-1804 at about 18:35 PT on 2026-11-14: Events hub
  holds 6 tabs, no Zombie Invasion tab; chain zombie-2026-11-10
  closed, no successor). Per _activities_/zombie-invasion/INDEX.md,
  do NOT seed a fresh zombie chain until a Zombie Invasion tab is
  seen live in the Events hub again. No zombie-invasion unit sits
  in inbox or claimed.

## What was attempted

- Token acquired by ticker-0934 until 17:56:51Z. Next unit picked:
  harvest-2026-11-15-0603 (planned for 06:03 PT, expires 10:03 PT).
- Device probe, 4 attempts, all failed identically:
  1. connection.health - node_offline
  2. computer.session start - node_offline
  3. connection.repair (target web) - node_offline
  4. screen.snap - node_offline
- device.list confirms Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd)
  offline, last seen 2026-11-15T13:19:56Z (05:19 PT today), and
  does not advertise a wake-up path. Last seen is unchanged since
  the ticker-0804 pass about 1.5 hours ago and the 0932
  knowledge-organizer reading. No game state observable, no input
  sent, no bubbles collected, no Armed Truck loot claimed.

## Result

- No resources collected, no claims, nothing spent. This is NOT
  the outcome_unknown control-lock (Issue 689), so no
  blocker_overlay recorded; the next tick will probe again.
- Tracker untouched (failed unit). The harvest regular stays due
  and the next tick re-produces it.
- The pass stops after this unit rather than cascading failed
  units through the pool: every remaining inbox unit needs the
  same offline device, and each failed claim would burn one of
  its 3 attempts for nothing. This follows the 2026-11-12
  ticker-0504 pattern.

## Chain continuation

- None. Harvest is not a chain unit.

## Batch note

- The delivery route is still down: VPS SSH Permission denied
  (publickey), verified this pass, so this pass's commit stays on
  the local records/2026-11-15 branch and no PR for
  records/2026-11-15 can be opened. records/2026-11-14 likewise
  never reached the remote. The pr-integrator's 08:00 run today
  also failed on the same VPS SSH denial, its 60th consecutive
  failure; the 0840 planner run was the seventh consecutive
  planner delivery failure.
- No unit has executed since 18:35 PT on 2026-11-14 (the
  ticker-1804 zombie unit). The Mac mini has now been offline
  for about 4.5 hours (last seen 05:19 PT), and the VPS SSH
  break is about 93 hours old; the owner chose the IONOS-console
  recovery on 2026-11-14 and it is not yet verified done.
