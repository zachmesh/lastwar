---
title: Radar 2026-11-15 ticker-1802 failed, Mac mini offline
created: 2026-11-16T02:06:00Z
modified: 2026-11-16T02:06:00Z
version: 1.0.0
description: Radar unit radar-2026-11-15-1403 failed, Mac mini unreachable
status: failed
grounded_in:
  - source: device.list and device.describe on 1c817413-83e2-0545-cb90-36d5e096a6bd, 2026-11-16T02:00Z to 02:05Z
  - source: device.invoke connection.health on 1c817413-83e2-0545-cb90-36d5e096a6bd, 2026-11-16T02:04Z and 02:05Z
  - source: GitHub connector open-PR list for zachmesh/lastwar, 2026-11-16T02:00Z
  - source: VPS SSH probe, 2026-11-16T01:57Z
---

# Radar 2026-11-15 ticker-1802 failed, Mac mini offline

- Executor: ticker-1802
- Unit: radar-2026-11-15-1403, regular radar, activity radar-tasks, priority 2, est 5 minutes
- Session window: 18:02-18:06 local, token held 18:02-18:17 local
- Status: failed, blocker_category f (missing precondition - device transport down)

## Own PRs first

- Open PRs re-checked live this pass via the GitHub connector
  read tool (the VPS gh route is down, SSH Permission denied,
  verified this pass): #711 knowledge (head
  work/ko-1132-lock-1047), #708 records 2026-11-12, #425 tools
  (head work/log-append-delivery-gate). None is owned by this job
  and nothing in them is addressed to it. No PR exists for
  records/2026-11-15. The connector's get_issue tool is not
  advertised and issue_read needs write-capable approval, so
  per-PR comments could not be read this way; the
  pr-integration job re-verified the same three PRs read-only
  at 17:38 PT today with no new review or comment noted. No
  action required from this pass.

## Sync and seed

- `queue.py sync`: reaped 0, expired 1, due 22, produced 0 (all due
  regulars already queued). One unit skipped as already closed:
  harvest-2026-11-15-1403 (completion marker in another
  worktree). Branch reconcile warning persists
  (records/2026-11-15 has no remote ref; issue #446). Roster
  stale warning persists (building-queues, research; issue #198).
- Zombie seeding: no-op - the Zombie Invasion event ended
  (unit zombie-2026-11-10-037, 2026-11-14 18:35 PT: Glacieradon
  ended, no Zombie Invasion tab in the Events hub, chain
  zombie-2026-11-10 closed, no successor). No zombie-invasion
  unit sits in inbox or claimed. No fresh chain seeded.

## What was attempted

- Token acquired by ticker-1802 until 2026-11-16T02:17:44Z. Next unit picked:
  radar-2026-11-15-1403 (regular radar, activity radar-tasks -
  the 14:03 cycle radar stack for duel day 7, window
  22:03-02:03Z). The unit expired at 02:03:00Z, seconds before
  the claim landed at about 02:03:20Z; the claim was accepted
  and the unit is failed on the device precondition, not on
  expiry - the stale unit sat unexecuted all day because the
  Mac has been offline since 05:19 PT.
- Device probe, 5 attempts, all failed with node_offline:
  1. device.list - offline, last seen 2026-11-15T13:19:56Z
  2. device.describe - offline, last seen 2026-11-15T13:19:56Z
  3. connection.health invoke - node_offline, no wake-up path
  4. device.list again - offline, last seen unchanged
  5. connection.health invoke again - node_offline, no wake-up path
- device.list confirms Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd)
  offline, last seen 2026-11-15T13:19:56Z (05:19 PT today), and
  does not advertise a wake-up path. Last seen is unchanged since
  the ticker-1634 pass about 80 minutes ago. No game state
  observable, no input sent, no radar task executed, nothing spent.

## Result

- No radar tasks executed, no claims, nothing spent. This is NOT the
  outcome_unknown control-lock (Issue 689), so no blocker_overlay
  recorded; the next tick will probe again.
- Tracker untouched (failed unit). The radar regular stays due;
  the next tick re-produces it for the next slot.
- The pass stops after this unit rather than cascading failed
  units through the pool: every remaining inbox unit needs the
  same offline device, and each failed claim would burn one of
  its 3 attempts for nothing. This follows the ticker-1634 pass
  80 minutes ago and the ticker-0504 pattern of 2026-11-12.

## Chain continuation

- None. Radar is not a chain regular.

## Batch note

- The delivery route is still down: VPS SSH Permission denied
  (publickey), verified this pass, so this pass's commit stays on
  the local records/2026-11-15 branch and no PR for
  records/2026-11-15 can be opened. records/2026-11-14 likewise
  never reached the remote. The 19:00 PT integrator batch is the
  next batch point; 19 batches have been missed so far.
- No unit has executed since 18:35 PT on 2026-11-14 (the
  ticker-1804 zombie unit). The Mac mini has now been offline
  for about 12 hours 45 minutes (last seen 05:19 PT), and the VPS
  SSH break is about 76 hours 45 minutes old; the owner chose the
  IONOS-console recovery on 2026-11-14 and it is not yet verified
  done, about 24 hours later.
- The 19:00 PT reset is about 55 minutes away. The VIP freebie,
  the 17:30 zero sweep (zero-sweep-2026-11-15-1730, still inbox)
  and the daily-missions units for this reset day cannot be
  claimed while the Mac stays offline; the VIP and sweep units
  expire at the reset.
