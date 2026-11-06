---
title: Daily Missions Queue Run
created: 2026-11-05T17:40:00-08:00
modified: 2026-11-05T17:42:00-08:00
version: 1.0.0
description: Daily missions unit daily-missions-2026-11-04-1800 executed by ticker-1734, failed on Mac mini offline with no wake-up path, fifty-sixth consecutive pass with a Mac device-access blocker
status: failed
grounded_in:
  - source: Mac mini device channel responses on 2026-11-05 about 17:38 to 17:42 local
---

# Daily missions 2026-11-05, ticker-1734

Unit daily-missions-2026-11-04-1800, failed. No game screen was ever
read and no game input was dispatched: the Mac mini is offline
with no wake-up path and the recovery device timed out, so no
mission list was read, no completed task was claimed, and no
activity chest was claimed. This was a stale unit from the
2026-11-04 18:00 slot (planned_for 2026-11-05T02:00:00Z, expires
2026-11-06T02:00:00Z); on a working screen it would have opened
Mission from the orange terminal on the base screen, claimed each
completed task individually with a list re-check after each
claim, and claimed the activity chests whose thresholds were
reached, per the daily-missions metadata.

## Attempts

- device.list reports the Mac mini
  1c817413-83e2-0545-cb90-36d5e096a6bd offline, last_seen
  2026-11-05T15:36:52Z (07:36 local) - stale about 10 hours
  at pass time, unchanged since the ticker-1025 pass. The recovery device
  (endo-recovery-8a2744fe-3281-4d50-a6d1-0ad28e99c05c) also
  reports offline with the same stale last_seen.
- computer.session start (task: claim the completed daily
  missions and activity chests) on the Mac mini failed at once,
  three times: node_offline, device offline and does not advertise
  a wake-up path.
- connection.health on the Mac mini failed at once:
  node_offline, no wake-up path.
- connection.repair (target web) on the Mac mini failed at once:
  node_offline, no wake-up path.
- connection.repair (target native) on the recovery device
  timed out: node_invoke_timeout after 25 seconds.
- connection.health on the recovery device timed out:
  node_invoke_timeout after 25 seconds.
- Total invoke attempts: 7, across two devices and four
  distinct commands, zero responses. This meets the
  standing at-least-3-attempts retry rule.
- No blind taps were dispatched: without an observation, any
  tap could land on the wrong control, so the unit stops here
  under the check-first rule. No different-device dialog was
  observed (no screen was ever captured) and no device
  takeover was needed.

## Outcome

- Status failed, blocker category e (repeated blocker,
  Issue 284). This is the fifty-sixth consecutive ticker
  pass with a Mac device-access blocker (fifty-fifth was
  ticker-1704, survivors unit survivors-2026-11-05-1403),
  seventeenth in the worsened zero-response form.
- No mission list read, no task claimed, no activity chest
  claimed. Tracker untouched, so the next tick re-produces
  the daily-missions regular and the line is re-read then.
- The pass stopped after this one unit: a second unit would
  hit the same dead channel.
- Re-probing is owed only after device.list last_seen
  refreshes. Recovery still needs the Mac back online
  first, then the Mac-side agent gateway restart if invokes
  still stall. Commented on Issue 284.
- Sync at pass start produced 5 new units (passes, secrets,
  treasures, trucks, events for the 1457 slot); 18 due
  regulars were already queued. The Zombie Invasion chain
  stays closed: the event ended 2026-10-30 about 19:00 and
  no Zombie Invasion tab has been seen in the Events hub
  since, so no fresh chain was seeded. The pre-reset
  zero-sweep pair for tonight's 19:00 reset (chain
  pre-reset-sweep-2026-11-05) is staged in the inbox
  (units 001 and 002).
