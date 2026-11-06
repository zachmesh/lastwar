---
title: Radar Tasks Queue Run
created: 2026-11-05T19:34:00-08:00
modified: 2026-11-05T19:40:00-08:00
version: 1.0.0
description: Radar unit radar-2026-11-05-1803 executed by ticker-1933, failed on Mac mini offline with no wake-up path, fifty-ninth consecutive pass with a Mac device-access blocker
status: failed
grounded_in:
  - source: Mac mini device channel responses on 2026-11-05 about 19:34 to 19:40 local
  - source: tools/duel.py live posture at 19:35 local, duel day 5 Total Mobilization, radar release
---

# Radar tasks 2026-11-05, ticker-1933

Unit radar-2026-11-05-1803, failed. No game screen was ever
read and no game input was dispatched: the Mac mini is offline
with no wake-up path and the recovery device timed out, so no
radar screen was entered, nothing was executed and nothing was
claimed. This was a stack-window unit (window text "duel day 4
- radar stack", planned_for 2026-11-06T02:03:00Z, expires
2026-11-06T06:03:00Z); the live posture at entry governs and
it is release, not stack: tools/duel.py at 19:35 local reads
duel day 5, Total Mobilization, radar_posture release, day
ends 2026-11-06 18:00 local. On a working screen this unit
would have entered the radar, run Quick Execute batches and
claimed the stack built on day 4, then worked the map pins
to a closing read each, per the radar-tasks metadata release
standard. None of that happened; the day 4 stack sits
unclaimed and the release window still runs until
2026-11-06 18:00 local, so a later pass with a live Mac can
still claim it.

## Attempts

- device.list reports the Mac mini
  1c817413-83e2-0545-cb90-36d5e096a6bd offline, last_seen
  2026-11-05T15:36:52Z (07:36 local) - stale about 12 hours
  at pass time, unchanged since the ticker-1025 pass. The
  recovery device
  (endo-recovery-8a2744fe-3281-4d50-a6d1-0ad28e99c05c) also
  reports offline with the same stale last_seen.
- computer.session start (task: execute the radar release
  claims in Last War) on the Mac mini failed at once, twice:
  node_offline, device offline and does not advertise
  a wake-up path.
- connection.repair (target web) on the Mac mini failed at
  once: node_offline, no wake-up path.
- connection.health on the Mac mini failed at once:
  node_offline, no wake-up path.
- connection.health on the recovery device timed out:
  node_invoke_timeout after 25 seconds.
- Total invoke attempts: 5, across two devices and three
  distinct commands, zero responses. This meets the
  standing at-least-3-attempts retry rule.
- No blind taps were dispatched: without an observation, any
  tap could land on the wrong control, so the unit stops here
  under the check-first rule. No different-device dialog was
  observed (no screen was ever captured) and no device
  takeover was needed.

## Outcome

- Status failed, blocker category e (repeated blocker,
  Issue 284). This is the fifty-ninth consecutive ticker
  pass with a Mac device-access blocker (fifty-eighth was
  ticker-1834, scout unit scout-scout-2026-11-02-005) and
  the twentieth in the worsened zero-response form (five
  invokes, zero responses). Commented on Issue 284.
- Tracker untouched for failed, per the queue rules. The
  radar regular stays due and the next tick re-produces it.
- No diamonds or money spent, no price tag tapped, no other
  activity worked from this unit.
