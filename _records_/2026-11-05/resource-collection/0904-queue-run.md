---
title: Resource Collection Queue Run
created: 2026-11-05T09:04:00-08:00
modified: 2026-11-05T09:22:00-08:00
version: 1.0.0
description: Harvest unit harvest-2026-11-05-0603 executed by ticker-0904, failed on Mac device invoke channel stall, fortieth consecutive pass with a Mac device-access blocker
status: failed
grounded_in:
  - source: Mac mini device channel responses on 2026-11-05 about 09:04 to 09:22 local
---

# Resource collection 2026-11-05, ticker-0904

Unit harvest-2026-11-05-0603, failed. No game screen was ever
read and no game input was dispatched: every device invoke to
the Mac mini timed out, so no bubble count was read, no bubble
was collected, and the Armed Truck state is unread. This was a
segment 1 unit (planned_for 2026-11-05T14:03:00Z, expires
18:03:00Z); on a working screen it would have swept the base
for ready output bubbles per the 2026-11-01 full-sweep rule,
tapping each bubble centre and verifying the resource totals
moved.

## Attempts

- Mac mini 1c817413-83e2-0545-cb90-36d5e096a6bd reported
  online by device.list, last_seen 2026-11-05T15:36:52Z
  (07:36 local) - stale about 1 hour 40 minutes at pass
  time. The recovery device
  (endo-recovery-8a2744fe-3281-4d50-a6d1-0ad28e99c05c) also
  reported online with the same stale last_seen.
- computer.session start (task: collect base resource
  bubbles) timed out twice, node_invoke_timeout after
  120 seconds each.
- computer.control list_apps timed out, node_invoke_timeout
  after 120 seconds.
- connection.health on the Mac mini timed out,
  node_invoke_timeout after 25 seconds.
- connection.repair (target web) on the Mac mini timed out,
  node_invoke_timeout after 25 seconds.
- connection.repair (target native) on the recovery device
  failed: "timeout: Connection recovery could not complete."
- connection.health on the recovery device failed with the
  same timeout.
- computer.session end (to clear any session the earlier
  passes left open) timed out, node_invoke_timeout after
  120 seconds.
- Total invoke attempts: 8, across two devices and five
  distinct commands, zero responses. This meets and exceeds
  the standing at-least-3-attempts retry rule.
- No blind taps were dispatched: without an observation, any
  tap could land on the wrong control, so the unit stops here
  under the check-first rule. No different-device dialog was
  observed (no screen was ever captured) and no device
  takeover was needed.

## How this differs from Issue 284

Issue 284's signature is a capture failure WITH responses:
the 0804 pass got list_apps results, activate calls returning
the stream error, and a working Chrome observation. This pass
got no response to any invoke at all - the device gateway /
transport itself is stalled, not just the LastWar window
stream. The previously suggested owner step (click the
LastWar Dock icon once) addresses the window-stream fault,
not a stalled invoke channel; if the next pass still times
out on every invoke, the Mac-side agent gateway likely needs
a restart. Commented on Issue 284 with this evidence.

## Outcome

- Status failed, blocker category e (repeated blocker,
  Issue 284). This is the fortieth consecutive ticker pass
  with a Mac device-access blocker (thirty-ninth was
  ticker-0834, donations unit donations-2026-11-03-1241).
- No bubble count read, no bubble collected, no Armed Truck
  claim. Tracker untouched.
- The pass stopped after this one unit: a second unit would
  hit the same stalled channel.
- Tier-2 note: the working tree held a pre-existing
  modification to _activities_/alliance-donations/INDEX.md
  (not this pass's change, not staged or committed here) and
  modified tools/state files for other dates; both were left
  exactly as found, per the recording rules. This pass changed
  no tracker state and no tier-2 file.

## Correction

- The unit result's costs string first read "duration 16m";
  the measured duration_seconds is 742 (about 12 minutes),
  so the string was corrected to "duration 12m" in the done
  unit file in the same pass. No other figure changed.
