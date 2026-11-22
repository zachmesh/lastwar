---
title: Harvest 2026-11-15 ticker-1202 failed, Mac mini offline
created: 2026-11-15T20:11:00Z
modified: 2026-11-15T20:11:00Z
version: 1.0.0
description: Harvest unit harvest-2026-11-15-1003 failed, Mac mini unreachable
status: failed
grounded_in:
  - source: device.list and device.describe on 1c817413-83e2-0545-cb90-36d5e096a6bd, 2026-11-15T20:03Z
  - source: device.invoke connection.health, environment.describe, computer.session, 2026-11-15T20:07Z
  - source: device.invoke connection.health and connection.repair on the Mac mini connection recovery device, 2026-11-15T20:08Z
---

# Harvest 2026-11-15 ticker-1202 failed, Mac mini offline

- Executor: ticker-1202
- Unit: harvest-2026-11-15-1003, regular harvest, activity resource-collection, priority 3, est 9 minutes
- Session window: 12:02-12:11 local, token held 12:06-12:21 local
- Status: failed, blocker_category f (missing precondition - device transport down)

## Own PRs first

- Open PRs re-checked live this pass via the unauthenticated public
  GitHub API (the VPS gh route is down, SSH Permission denied,
  verified this pass; local gh has no login): #711 knowledge
  (head work/ko-1132-lock-1047), #708 records 2026-11-12, #425
  tools (head work/log-append-delivery-gate). None is owned by
  this job and nothing in the newest comments is addressed to it:
  #708 has no comments and reads mergeable/clean, awaiting the
  integrator batch; #711's newest comment (zachmesh,
  2026-11-12) is a note for the integrator and the next
  knowledge-organizer run about PR #710 having merged after #711
  opened; #425's newest comments are integrator notes, the PR
  still owner-gated on the policy amendment. No PR exists for
  records/2026-11-14 or records/2026-11-15. No action required
  from this pass.

## Sync and seed

- `queue.py sync`: reaped 0, expired 0, due 22, produced 0 (all due
  regulars already queued). One completion marker reaped:
  scout-scout-2026-11-10-018. Branch reconcile warning
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

- Token acquired by ticker-1202 until 20:21:19Z. Next unit picked:
  harvest-2026-11-15-1003 (planned for 10:03 PT, expires 14:03 PT).
- Device probe, 5 attempts, all failed:
  1. connection.health on the Mac mini - node_offline, no wake-up path
  2. environment.describe on the Mac mini - node_offline, no wake-up path
  3. connection.health on the Mac mini connection recovery device - node_invoke_timeout after 25s
  4. connection.repair target native on the recovery device - node_invoke_timeout after 25s
  5. computer.session start on the Mac mini - node_offline, no wake-up path
- device.list confirms Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd)
  offline, last seen 2026-11-15T13:19:56Z (05:19 PT today). This is
  the same last-seen timestamp the 0804, 0934 and 1051 passes
  reported, so the Mac has now been offline about 7 hours with no
  change. The recovery device offers no working path either.

## Outcome

- No game state observable, no input sent, no collection, no
  claims, nothing spent. This is NOT the outcome_unknown control
  lock (Issue #689) - the device transport itself is down - so no
  blocker overlay is recorded and the next tick probes again.
- Tracker untouched (failed unit); the harvest regular stays due
  and the next tick re-produces it.
- Pass stopped after this unit rather than cascading failed units,
  per the established pattern (ticker-0804, ticker-0934,
  ticker-1051 did the same today).
- Stalled priority-1 units remain unexecutable while the Mac is
  down: vip-2026-11-14-1800 (29 hours old), vip-2026-11-15-1800,
  and tonight's pre-reset zero-sweep pair (1630, 1730).
- VPS SSH still Permission denied (publickey), verified this pass,
  so push/PR delivery is impossible; the commit stays local on
  records/2026-11-15 with pr null. The Mac outage and the VPS
  outage are both already tracked (pr-integration runs count the
  consecutive VPS failures); no new Issue filed for either.
