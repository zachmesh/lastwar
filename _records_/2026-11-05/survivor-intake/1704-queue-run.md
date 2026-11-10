---
title: Survivor Intake Queue Run
created: 2026-11-05T17:06:00-08:00
modified: 2026-11-05T17:13:00-08:00
version: 1.0.0
description: Survivors unit survivors-2026-11-05-1403 executed by ticker-1704, failed on Mac mini offline with no wake-up path, fifty-fifth consecutive pass with a Mac device-access blocker
status: failed
grounded_in:
  - source: Mac mini device channel responses on 2026-11-05 about 17:06 to 17:13 local
---

# Survivor intake 2026-11-05, ticker-1704

Unit survivors-2026-11-05-1403, failed. No game screen was ever
read and no game input was dispatched: the Mac mini is offline
with no wake-up path and the recovery device timed out, so no
survivor count was read, no survivor was recruited, and no Quick
Dispatch ran. This was a segment 1 unit (planned_for
2026-11-05T22:03:00Z, expires 2026-11-06T02:03:00Z); on a
working screen it would have worked the front-gate line per the
survivor-intake metadata, tapping each survivor figure, pressing
Recruit, and running Quick Dispatch in a building panel
afterwards.

## Attempts

- device.list reports the Mac mini
  1c817413-83e2-0545-cb90-36d5e096a6bd offline, last_seen
  2026-11-05T15:36:52Z (07:36 local) - stale about 9 hours
  30 minutes at pass time, unchanged since the ticker-1025
  pass. The recovery device
  (endo-recovery-8a2744fe-3281-4d50-a6d1-0ad28e99c05c) also
  reports offline with the same stale last_seen.
- computer.session start (task: collect the survivors at the
  base front gate) on the Mac mini failed at once, three
  times: node_offline, device offline and does not advertise
  a wake-up path.
- connection.health on the Mac mini failed at once:
  node_offline, no wake-up path.
- connection.repair (target web) on the Mac mini failed at
  once: node_offline, no wake-up path.
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
  Issue 284). This is the fifty-fifth consecutive ticker
  pass with a Mac device-access blocker (fifty-fourth was
  ticker-1634, harvest unit harvest-2026-11-05-1403),
  sixteenth in the worsened zero-response form.
- No survivor count read, no survivor recruited, no Quick
  Dispatch. Tracker untouched, so the next tick re-produces
  the survivors regular and the line is re-read then; the
  standing third-strike survivor blocker (22 of 22 partial
  in the queue era) is not advanced by this pass, since no
  screen was ever read.
- The pass stopped after this one unit: a second unit would
  hit the same dead channel.
- Re-probing is owed only after device.list last_seen
  refreshes. Recovery still needs the Mac back online
  first, then the Mac-side agent gateway restart if invokes
  still stall. Commented on Issue 284.
- Sync at pass start produced nothing new (21 due, all
  already queued). The Zombie Invasion chain stays closed:
  the event ended 2026-10-30 about 19:00 and no Zombie
  Invasion tab has been seen in the Events hub since, so no
  fresh chain was seeded. The pre-reset zero-sweep pair for
  tonight's 19:00 reset (chain pre-reset-sweep-2026-11-05)
  is staged in the inbox (units 001 and 002).
- Tier-2 note: the working tree held pre-existing
  modifications to _activities_/alliance-donations/INDEX.md
  and tools/state files for other dates (not this pass's
  changes, not staged or committed here); both were left
  exactly as found, per the recording rules. This pass
  changed no tracker state and no tier-2 file.
