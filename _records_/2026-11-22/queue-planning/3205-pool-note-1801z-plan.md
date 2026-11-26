---
title: Pool Note And Duration Medians At 1801Z 3205 2026-11-26
created: 2026-11-26T10:03:50-08:00
modified: 2026-11-26T10:03:50-08:00
level: L0
version: 1.0.0
description: The plan run of 2026-11-26 18:01Z - 9 units expired, 19 minted for the 22:03Z wave and groups, three retirements, the held units read back, today's helmet look, gifts result dialog, duel Route A, events tab bar and daily barrel step copied into the roster bodies, the pool counted and the duration medians of 62 units set against their estimates
status: done
activity: queue-planning
run_id: queue-planning-2026-11-26-1801-plan
trigger: coordinator ping 18Z
started_at: 2026-11-26T10:00:57-08:00
finished_at: 2026-11-26T10:03:50-08:00
verified: queue.py plan --hours 5 output, full before and after snapshots, validate, the forecast check over all units, the window and on-the-hour scans, the standing-line and front-clause scans, units counted as available at four times, a pick simulation from 18:10Z, durations computed from the started_at and finished_at of the done folder
grounded_in:
  - source: _records_/2026-11-22/queue-planning/3120-next-plan-specifics.md
  - source: _records_/2026-11-22/queue-planning/3125-plan-times-and-checks.md
  - source: _records_/2026-11-22/queue-planning/3204-pool-note-1401z-plan.md
---

# Pool note and duration medians, 1801Z plan, 3205

## The reaping and the held units

The plan expired 9 units that ended 14:06Z to 14:57Z (nine of the 14:03Z wave and groups ran behind the chain) and reaped none. Of 32 units in the inbox before it, 23 were carried and none changed an expiry, priority or floor. Read back at 18:03Z: promotion batch 2 opens 20:16Z (ends 22:30Z); harvest 1003 20:25Z (ends 00:25Z); donations pm 21:04Z (ends 23:50Z); the siege read 11-27T00:25Z (ends 00:55Z); the train batch 11-27T00:30Z; harvest 1403 11-27T00:25Z (ends 04:25Z); Oil Well -008 11-28T02:52Z, -009 11-30T22:28Z, -010 12-04T16:17Z; the lab completes 11-27T23:20Z and 11-29T12:39Z.

## What the plan did

It minted 19 units (the 22:03Z wave 8, the 22:30Z group 6, the 22:57Z group 5) and I retired the roster donations, trucks and passes units. The 16 roster bodies came from the current-wave siblings, with today's new work: the harvest unit keeps the helmet look and opens 00:25Z (4 hours after the 20:25Z read); gifts carry the Claim All result-dialog procedure; duel-score carries Route A (the cyan left arrow near (167,463), three plain taps, never a swipe or page dot); events carry the tab-bar drag with the eight tab names; secrets carry the daily barrel Use (the whole stack at quantity N). The train batch has no room to train into (the ground is full): it is flagged, not retired.

## Not carried

The standing UserNotificationCenter rule (the tool and the single kill) is not in any sheet I can read: the template holds the front rule only. Batch 3 (about 23:55Z) and batch 4 (237 troops, about 03:20Z) are staged from batch 2's record, not now.

## Availability and checks

Live 39 of 39. Available at 18:30Z 10, 20:25Z 15, 22:30Z 17, 00:30Z 18. Validate 'pool valid'; the forecast gate refused none; no unit opens on the hour or in a calm window; the standing line and front clause are in all 39. A pick simulation from 18:10Z of 28 roster-class units runs 28 at est+1 and est+2, ending 23:12Z and 23:24Z.

## Duration medians, 62 units since 06:00Z

The table is `3205-duration-medians-2026-11-26-1800z.csv`. Median minutes against the estimate: trucks 8.2 against 15; building-queues 10.7 (max 43.9) against 12; harvest 7.0 against 12 (it now carries the helmet look); training 4.8 against 10; duel-score 7.9 against 2 (the carousel); scout-midday 3.0 against 7; secrets 2.2 against 5; mail 5.0 against 4. The next plan is the 22Z ping.

## Correction

The nine expired units belonged to the 10:03Z wave and its groups (ids -0203, -0230 and -0257, which ended 14:06Z to 14:57Z), not to a 14:03Z wave as the first section says.
