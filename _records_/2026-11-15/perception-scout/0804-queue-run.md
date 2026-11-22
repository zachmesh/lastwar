---
title: Scout 2026-11-15 ticker-0804 failed, Mac mini offline again
created: 2026-11-15T16:40:00Z
modified: 2026-11-15T16:40:00Z
version: 1.0.0
description: Perception scout unit scout-scout-2026-11-10-017 failed, Mac mini unreachable
status: failed
grounded_in:
  - source: device.list and device.describe on 1c817413-83e2-0545-cb90-36d5e096a6bd, 2026-11-15T16:31Z
  - source: device.invoke connection.health, computer.session, connection.repair, screen.snap, 2026-11-15T16:31Z
---

# Scout 2026-11-15 ticker-0804 failed, Mac mini offline again

- Executor: ticker-0804
- Unit: scout-scout-2026-11-10-017, chain scout-2026-11-10, seq 17
- Session window: 08:04-08:40 local, token held 08:30-08:45 local
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
  zombie-invasion-zombie-2026-11-10-037. Branch reconcile warning
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

- Token acquired by ticker-0804 until 16:45:00Z. Next unit picked:
  scout-scout-2026-11-10-017 (chain scout-2026-11-10, seq 17;
  the post-reset scout pass for reset date 2026-11-10, whose
  surface group remains unwalked after units 015 and 016 failed
  on the same outage).
- Device probe, 4 attempts, all failed identically:
  1. connection.health - node_offline
  2. computer.session start - node_offline
  3. connection.repair (target web) - node_offline
  4. screen.snap - node_offline
- device.list confirms Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd)
  offline, last seen 2026-11-15T13:19:56Z (05:19 PT today), and
  does not advertise a wake-up path. The Mac was reachable
  yesterday evening (ticker-1804 played at about 18:33 PT on
  2026-11-14) and was last seen this morning at 05:19 PT; it has
  gone offline again since. No game state observable, no input
  sent, no observation made, no claims.

## Result

- No surfaces walked, no items observed, no red dots seen or
  explained. The scout observation file for 2026-11-10 is
  unchanged.
- This is NOT the outcome_unknown control-lock (Issue 689), so no
  blocker_overlay recorded; the next tick will probe again.
- Tracker untouched (failed unit).

## Chain continuation

Successor unit 018 in chain scout-2026-11-10 enqueued to start now,
following the pattern of the 09:34, 11:00, 12:04, 13:28, 15:34 and
17:12 passes on 2026-11-14, each of which recorded one failed unit
against the same outage and enqueued its successor.

## Batch note

- The delivery route is still down: VPS SSH Permission denied
  (publickey), verified this pass, so this pass's commit stays on
  the local records/2026-11-15 branch and no PR for
  records/2026-11-15 can be opened. records/2026-11-14 likewise
  never reached the remote (git ls-remote shows only
  records/2026-11-12 on the remote). The pr-integrator's 08:00
  run today also failed on the same VPS SSH denial.
- No unit has executed since 18:35 PT on 2026-11-14 (the
  ticker-1804 zombie unit). The 2026-11-15 0203/0230/0257 unit
  sets expired unexecuted, per the planner's 06:40 and 07:40
  records.
