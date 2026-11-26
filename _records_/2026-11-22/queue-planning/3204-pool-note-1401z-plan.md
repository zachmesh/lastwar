---
title: Pool Note And Duration Medians At 1401Z 3204 2026-11-26
created: 2026-11-26T06:08:11-08:00
modified: 2026-11-26T06:08:11-08:00
level: L0
version: 1.0.0
description: The plan run of 2026-11-26 14:01Z - 12 units reaped, 19 minted for the 18:03Z wave and groups, three retirements, the held units read back, the helmet ruling written into the template and build units, the pool counted and the duration medians of 44 units set against their estimates
status: done
activity: queue-planning
run_id: queue-planning-2026-11-26-1401-plan
trigger: coordinator ping 14Z
started_at: 2026-11-26T06:01:09-08:00
finished_at: 2026-11-26T06:08:11-08:00
verified: queue.py plan --hours 5 output, full before and after snapshots, validate, the forecast check over all units, the window and on-the-hour scans, the standing-line and front-clause scans, units counted as available at four times, a pick simulation from 14:10Z, durations computed from the started_at and finished_at of the done folder
grounded_in:
  - source: _records_/2026-11-22/queue-planning/3120-next-plan-specifics.md
  - source: _records_/2026-11-22/queue-planning/3125-plan-times-and-checks.md
  - source: _records_/2026-11-22/queue-planning/3202-pool-note-1001z-plan.md
---

# Pool note and duration medians, 1401Z plan, 3204

## The reaping and the held units

The plan expired 12 units that ended 10:06Z to 10:57Z (the 10:03Z wave, the 10:30Z and 10:57Z groups: they ran behind the chain, four of the wave's units unrun) and reaped none. Full snapshots before and after: the 36 carried units kept every expiry, priority and floor. Read back at 14:07Z: Oil Well -008 opens 11-28T13:46Z (ends 11-29T09:46Z), -009 12-01T20:06Z, -010 12-06T04:21Z; cycle J 14:18Z; the Backpack unit 14:10Z; harvest 0603 16:22Z (ends 20:22Z, the 4.0 h read at about 16:25Z); donations pm 21:04Z (ends 23:50Z); the lab completes 11-27T23:20Z and 11-29T12:39Z; the train batch 11-27T00:30Z. The helmet unit is claimed.

## What the plan did

It minted 19 units: the 18:03Z wave 8, the 18:30Z group 6, the 18:57Z group 5. I retired the roster donations, trucks and passes units. The 15 roster bodies came from the current-wave siblings (-0603, -0630, -0657; the mail and treasures ones from their done siblings, so they carry Steer A's event-list pan, the Claim All ban and the three-dig rule). The new harvest unit opens 20:25Z (four hours after the 16:25Z read, to re-time at the 18Z plan) without the 4.0 h test.

## The helmet ruling (Steer A 14:04Z)

The white round bubble with a green helmet is the help request: one press on the 13-day ground gave 13 helps in 100 seconds, each taking 0.5 percent of the time left. Written into the unit template, sheets 2541 and 3125, the routes table and Oil Well units -008 to -010 (est 12, cap 0.90 USD, 449 words): a 6x crop after the press, ONE press, end times before, at +1 and +10. The lab completes carry nothing yet (a helmet over the Tech Center is unverified): the 22Z plan adds it.

## Availability and checks

Live 46 of 51. Available at 14:30Z 15 (1 at priority 1), 16:25Z 17, 18:30Z 18, 20:25Z 19. Validate 'pool valid'; the forecast gate refused none; no unit opens on the hour or in a calm window; the standing line and front clause are in all 51. A pick simulation from 14:10Z of 39 roster-class units runs 34 at est+1 and est+2, ending 19:12Z and 19:25Z; five of the 10:06Z wave end 14:06Z unrun.

## Duration medians, 44 units since 11-25T14:00Z

The table is `3204-duration-medians-2026-11-26-1400z.csv` (one to seven runs a regular). Median minutes against the estimate: trucks 8.2 against 15; building-queues 8.9 (max 20.8) against 12; harvest 3.5 against 4; secrets 2.3 against 6.5; training 3.6 against 12; mail 5.0 against 4; daily-missions 17.6 against 10; scout-midday 6.0 against 6. The next plan is the 18Z ping.
