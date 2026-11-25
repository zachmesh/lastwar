---
title: Pool Note After The 2201Z Plan 3199 2026-11-25
created: 2026-11-25T14:30:00-08:00
modified: 2026-11-25T14:30:00-08:00
level: L0
version: 1.0.0
description: The plan run of 2026-11-25 22:01Z during the different-device hold - 36 units minted across the pre-reset set, the zero sweeps, the new-day units and the 02:03Z wave and groups, five retired, one held unit's expiry moved by the plan and restored, and what the pool holds at the 02:00Z reset if the dialog still stands
status: done
activity: queue-planning
run_id: queue-planning-2026-11-25-2201-plan
trigger: coordinator ping 22:03Z
started_at: 2026-11-25T14:00:40-08:00
finished_at: 2026-11-25T14:30:00-08:00
verified: queue.py plan --hours 5 output, the held units read before and after the plan, validate, the forecast check over all units, the window and on-the-hour scans, the standing-line, front-clause, avatar and Lottery scans, the pool counted by expiry against the reset, two pick simulations with the tool's own pick_key and actionable test
grounded_in:
  - source: _records_/2026-11-22/queue-planning/3120-next-plan-specifics.md
  - source: _records_/2026-11-22/queue-planning/3125-plan-times-and-checks.md
  - source: _records_/2026-11-22/queue-planning/3197-pool-note-1801z-plan.md
---

# Pool note, 2201Z plan, 3199

## The held units

Read before and after the plan. The plan moved ONE: the Food Output V lab complete went from 01:50Z to 02:00:42Z, the reset instant, when the Complete tap is worth nothing for the duel. I restored 11-26T01:50Z. The others held: -005, the Drill Ground hand-off, the UR claim, the room collect, the train batch, the base survey and the help gesture 11-26T06:50Z; cycle D and pass 012 01:50Z; the radar units 22:03Z; the duel-score units 22:30Z; the oil lab complete 10:37Z.

## What the plan did

It minted 36 units: the zero sweeps (opening 00:04Z and 01:04Z, off the hour), the pre-reset set at 00:30Z (priority 1, expiring 02:00Z), the new-day units (VIP 02:06Z, daily missions 02:08Z, scout 02:12Z), the 02:03Z wave (8), the 02:30Z group (6) and the 02:57Z group (4, moved to 03:03Z so none runs across the 03:00:04Z event). I retired five: the roster donations (2) and trucks (2) units, and the 00:30Z VIP unit (the freebie is claimable about 02:00Z, so it would only read a state not yet claimable). It expired 15 stale units: the 14:03Z wave (6), the 14:30Z group (5) and the 14:57Z group (4).

## Fixed in the minted units

Sibling blocks copied from the 22:03Z wave. The zero sweeps were over the word gate, so their rules (bubble lines, Main Tasks, VIP, tram) live in the new sheet 2543 and the units point to it. The 00:30Z daily-missions unit lacked the Main Tasks paragraph: added.

## The pool at 02:00Z if the dialog still stands

Live now 77 of 85 (8 past expiry await reaping). OLD DAY, expiring by 02:00Z: 25 units: the pre-reset set and zero sweeps (11), cycle D, pass 012 and the lab complete (3, at 01:50Z), and 11 of the 18:30Z and 18:57Z groups (end 22:30Z and 22:57Z). They expire unrun. The 22:03Z, 22:30Z and 22:57Z wave units outlast the reset by 3 to 57 minutes (02:03Z, 02:30Z, 02:57Z): old day. CARRY, past the reset: the chain at 11-26T06:50Z (-005, the Drill Ground hand-off, the UR claim, the room collect, the train batch, the base survey, the help gesture), the oil lab complete 10:37Z, the Hospital read 11-27T00:55Z, the Oil Well chain -006 to -010 (floors days ahead), and the 26 new-day units opening from 02:00Z.

## Checks

Validate 'pool valid', none at or over 450 words; the forecast gate refused none; the standing line in every unit; the front clause in every unit but pass 012; no avatar coordinate or Lottery tab without a ban. Nothing opens or expires in 02:58Z-03:02Z, 04:30Z-04:45Z, 08:00Z-08:25Z, 09:58Z-10:05Z or 11:25Z-11:40Z, and no opening is on the hour. A pick simulation of the 31 roster units from 00:04Z over five hours runs all 31 and expires none. The dialog still stands. The next plan is the 02Z ping.
