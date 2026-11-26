---
title: Pool Note After The 1001Z Plan 3202 2026-11-26
created: 2026-11-26T02:02:36-08:00
modified: 2026-11-26T02:02:36-08:00
level: L0
version: 1.0.0
description: The plan run of 2026-11-26 10:01Z after the third takeover held - 16 units reaped, 20 minted for the 14:03Z wave and groups, three retirements, the harvest unit set to the 16:22Z slot, one hour edge moved, the held units read back and the units available at five answer times
status: done
activity: queue-planning
run_id: queue-planning-2026-11-26-1001-plan
trigger: coordinator ping 10Z
started_at: 2026-11-26T02:00:36-08:00
finished_at: 2026-11-26T02:02:36-08:00
verified: queue.py plan --hours 5 output, full before and after snapshots of all 61 units, validate, the forecast check over all units, the window and on-the-hour scans, the standing-line, front-clause and avatar scans, units counted as available at five answer times, a pick simulation from 10:06Z
grounded_in:
  - source: _records_/2026-11-22/queue-planning/3120-next-plan-specifics.md
  - source: _records_/2026-11-22/queue-planning/3125-plan-times-and-checks.md
  - source: _records_/2026-11-22/queue-planning/3201-pool-note-0601z-plan.md
---

# Pool note, 1001Z plan, 3202

## The reaping

The plan expired 16 units that ended 06:03Z to 06:57Z, before or behind the chain: the 02:03Z wave 6, the 02:30Z group 6 and the 02:57Z group 4. It reaped none.

## The held units

Full snapshots before and after: the 45 carried units kept every expiry, priority and floor, and the plan shortened nothing. Read back: the Drill Ground hand-off -002 opens 10:06Z and ends 11-27T02:00Z; cycle H -005 opens 13:30Z and ends 11-27T02:00Z; the daily-missions unit ends 11-27T02:00Z; harvest 0203 runs 10:06Z to 14:06Z for the 12:22Z read; the Oil Well hand-off -006 ends 19:09Z; the oil and defense lab completes end 11-28T05:20Z and 11-29T18:40Z; the train batch opens 11-27T00:30Z; the Hospital read ends 11-27T00:55Z. The takeover, ghost-ops and VIP login units are done.

## What the plan did

It minted 20 units: the 14:03Z wave 8, the 14:30Z group 6, the 14:57Z group 5 and a scout-midday unit. I retired the roster donations and trucks units and the passes unit (the check is folded into the daily-missions unit, Steer A 09:43Z). The 16 roster bodies were copied from the current-wave siblings (-0203, -0230, -0257), so each carries every current ruling. The new harvest unit is set to the 16:22Z slot (the 4.0 h read of the cap test), ending 20:22Z, without the Farmland paragraph (the 12:22Z visit only). The scout-midday unit opened exactly 15:00Z: it now opens 15:06Z. The wave opens 14:03Z, off the hour and outside every window, so no other move was needed.

## Units the owner's answer would find available

Live now 62 of 62. Available, opened and not expired: at 10:30Z 23 (1 at priority 1); 12:22Z 23 (1); 14:30Z 23 (2); 16:22Z 24 (2); 18:00Z 24 (2). Four priority-3 units of the 06:03Z wave (building-queues, research, survivors, training) end 10:06Z unrun behind the chain: the 14:03Z wave replaces them.

## Checks

Validate 'pool valid', none at or over 450 words; the forecast gate refused none; the standing line and front clause in all 62; no avatar coordinate without a ban. Nothing opens or expires in 02:58Z-03:02Z, 08:00Z-08:25Z, 09:58Z-10:05Z or 11:25Z-11:40Z (the 04:30Z window is dropped), and no unit opens on the hour. A pick simulation from 10:06Z of 45 roster-class units (the harvest units are fixed items) runs 41 at est+1 and 40 at est+2, ending 15:17Z and 15:31Z. The next plan is the 14Z ping.
