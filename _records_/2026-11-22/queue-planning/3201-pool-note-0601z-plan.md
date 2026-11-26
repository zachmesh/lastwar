---
title: Pool Note After The 0601Z Plan 3201 2026-11-26
created: 2026-11-25T22:04:34-08:00
modified: 2026-11-25T22:04:34-08:00
level: L0
version: 1.0.0
description: The plan run of 2026-11-26 06:01Z during the second two-hour stop - 17 units reaped and the Drill Ground claim released, 20 minted for the 10:03Z wave and groups plus ghost-ops, three retirements, two window moves, the held units read back and the units available at five answer times
status: done
activity: queue-planning
run_id: queue-planning-2026-11-26-0601-plan
trigger: coordinator ping 06Z
started_at: 2026-11-25T22:00:55-08:00
finished_at: 2026-11-25T22:04:34-08:00
verified: queue.py plan --hours 5 output, full before and after snapshots of all 72 units, validate, the forecast check over all units, the window and on-the-hour scans, the standing-line, front-clause, avatar and Lottery scans, units counted as available at five answer times, a pick simulation from 07:50Z
grounded_in:
  - source: _records_/2026-11-22/queue-planning/3120-next-plan-specifics.md
  - source: _records_/2026-11-22/queue-planning/3125-plan-times-and-checks.md
  - source: _records_/2026-11-22/queue-planning/3200-pool-note-0201z-plan.md
---

# Pool note, 0601Z plan, 3201

## The reaping

The plan expired 17 units that ended between 02:03Z and 02:57Z during the hold: the 22:03Z wave 7, the 22:30Z group 6 and the 22:57Z group 4. It also reaped 1: the operator's stale claim on the Drill Ground hand-off (attempts 1 of 3). That unit is back in the inbox unrun, and the Coordinator dispatches it by name.

## The held units

Full before and after snapshots of all 72 units: the 54 carried units kept every expiry, priority and floor, and the plan shortened nothing. The chain ends 11-27T02:00Z or later (the Drill Ground, cycles E and F, the room collect, the UR claim and others); the Oil Well chain -006 to -010 keeps its re-timed floors; the oil and defense lab completes end 11-28T05:20Z and 11-29T18:40Z; the Hospital read 11-27T00:55Z; takeover3 11:45Z. I did not extend the 16 routine units of the 02:03Z, 02:30Z and 03:03Z waves that end 06:03Z to 06:57Z (the plan mints fresh ones).

## What the plan did

It minted 20 units: the 10:03Z wave 8, the 10:30Z group 6, the 10:57Z group 5, and ghost-ops (Thursday event day, opening 08:00Z). I retired the roster donations and trucks units and the Food Output V lab complete (the phone restarted both labs). The 17 roster bodies were copied from the current-wave siblings, so each carries the radar and mail rulings, the secrets daily assist and the 3170 closes. Radar stays priority 2 and duel-score 3.

Moves: the 10:03Z wave opened inside the owner's 09:58Z to 10:05Z window, so its seven units open 10:06Z and expire 14:06Z (the 10:30Z and 10:57Z groups stand). Ghost-ops opened and expired exactly 08:00Z, inside the cu window: it now opens 08:26Z and expires 11-27T07:50Z. Its planner block is mine: read first, plunder and the Auto Smart Task Execution tick banned, the surface last seen live 2026-10-25 and every mechanic a guide claim [G]: Steer A's approval is asked, else I retire it.

## Units the owner's answer would find available

Live now 66 of 72 (6 of the 02:03Z wave ended 06:03Z and await the reap). Available, opened and not expired: at 06:30Z 28 (4 at priority 1); 07:50Z 31 (6); 10:30Z 32 (6); 12:00Z 31 (5); 18:00Z 13 (5).

## Checks

Validate 'pool valid', none at or over 450 words; the forecast gate refused none; the standing line and front clause in all 72; no avatar coordinate without a ban; the Lottery tab banned where named. Nothing opens or expires in 02:58Z-03:02Z, 08:00Z-08:25Z, 09:58Z-10:05Z or 11:25Z-11:40Z (the 04:30Z window is dropped), and no unit opens on the hour. A pick simulation from 07:50Z (the stop ends) of 51 roster-class units runs 35, none expiring; the 16 left are the 02:03Z to 03:03Z waves, ending 06:03Z to 06:57Z, before the stop does. The last run ends 11:24Z at est+1 and 11:52Z at est+2. The next plan is the 10Z ping.
