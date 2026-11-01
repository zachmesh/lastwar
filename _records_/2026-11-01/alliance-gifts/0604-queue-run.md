---
title: Alliance gifts queue run 0604
created: 2026-11-01T14:04:00Z
modified: 2026-11-01T14:04:00Z
version: 1.0.0
description: Alliance gifts unit gifts-2026-11-01-0230 executed by ticker-0604
status: not performed
grounded_in:
  - source: device channel probe results on the owner Mac mini, 2026-11-01
---

# Alliance gifts — execution, 2026-11-01 0604 queue unit

A single task unit, executed by executor ticker-0604 under
the task unit queue. Unit gifts-2026-11-01-0230, priority 3,
expires 06:30 America/Los_Angeles. Session window about
06:04 to 06:15 America/Los_Angeles. Status — not performed:
the device channel was offline, so no game screen was ever
reached. No other regular was merged into this unit.

## Own PR first

Before game work, this pass checked the open pull requests
for zachmesh/lastwar on the VPS (gh pr list, zachmesh login):
no open PRs at all, so there was no records PR of this job
sitting in conflict and no unanswered question addressed to
this job. Nothing to resolve before the pass.

## What was done

- Sync reaped 0 and expired 0; all 20 due regulars were
  already queued, so no new unit was produced. No zombie
  chain was seeded: the Zombie Invasion event ended at
  about the 19:00 reset on 2026-10-30 and the Events hub
  has no Zombie page.
- Device token acquired by ticker-0604; unit
  gifts-2026-11-01-0230 claimed (the earliest-expiry due
  unit, expiring 06:30 local).
- Mac mini (device 1c817413-83e2-0545-cb90-36d5e096a6bd)
  device channel offline across three computer.session
  starts (node_offline, no wake-up path advertised), plus
  a failed connection.health probe and one timed-out
  connection.repair attempt on the recovery channel.
  Last seen 01:47 local, unmoved across the pass.
- No screen read, no Alliance panel opened, no Regular
  or Premium gift count observed, nothing claimed,
  nothing spent. Tracker untouched, as required for a
  failed unit.

## Result statistics

- target: 1
- achieved: 0
- resources_gained: none
- costs: 0
- verified: no
- blocker_category: f

## Close

- Eighth consecutive access-failed pass after the 02:34,
  03:04, 03:34, 04:04, 04:34, 05:04 and 05:34 passes; the
  channel has been down since 01:47 local. The next pass
  should retry the channel as usual and, if it stays
  down, keep the failure visible rather than re-attempting
  the same unit type blindly: the gifts unit itself is
  unexpired work, and the blocker is the channel, not
  the gift entry route.
- Zombie Invasion seeding was not done: the event
  ended 2026-10-30 about 19:00 and the Events hub
  has no Zombie page, so no zombie unit was seeded.
