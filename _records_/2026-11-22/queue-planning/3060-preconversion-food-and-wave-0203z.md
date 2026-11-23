---
title: Queue Planning The Pre-Conversion Food Step And The 02:03Z Wave 3060 2026-11-23
created: 2026-11-23T14:45:00-08:00
modified: 2026-11-23T14:45:00-08:00
level: L0
version: 1.0.0
description: Planner pass after Decision 08 - the coin pre-conversion aligned to the decision, a separate food conversion unit, the food check in the ground units, the evidence that the measured previews show no food row, and the 02:03Z wave minted
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-1445-food-and-wave
trigger: coordinator message 22:31Z and the 22:30Z ping
started_at: 2026-11-23T14:31:00-08:00
finished_at: 2026-11-23T14:45:00-08:00
verified: Decision 08 read; the capacity read result and records 2015 and 2212 read for the preview cost rows; the inbox checked for the forecast flip, the quiet window and stale times; validate exit 0
grounded_in:
  - source: _records_/2026-11-22/strategy/dec-20261123-08.md
  - source: _records_/2026-11-22/building-queues/2015-queue-run.md and 2212-queue-run.md
---

# The pre-conversion food step and the 02:03Z wave, 3060

## Pre-conversion

`building-queues-growth-preconvert-2026-11-23-001` is now the COIN unit, aligned to Decision 08: T = 271.8M from the 87 UR Coin Chests first, then about 50 SSR Coin Chests (value read from the item panel), the high grades first; the plain Resource Chests are not used and stay for the choice-chest policy; if T is not reached after the SSR chests it stops and records the shortfall. `-003` is the FOOD unit: food T = 1,077.5M (the three starts 977.5M plus the 100M floor) from the typed UR Food Chests (value read from the item panel, about 4.06M, about 103 owned). Both open 22:35Z, are claimable until 22:55Z and 22:56Z, and end by 23:09Z; with the owner-idle wait at 0 they can run back to back. The ground units read every cost row of the preview before each Upgrade and stop on a short row.

## The evidence the decision should weigh

The previews read at 20:16Z (records 2015 and 2212) show, for Lv.26 to 27 and Lv.28 to 29, coin (short), iron (met), Unit Count +200, power and effective time, and no food row. My own panel read at 08:35Z said the same at Lv.28 to 29, and only Lv.30 to 31 shows food (671.5M, short). Decision 08's 221M, 314.5M and 442M therefore look like guide estimates, not measured rows. The food unit is separate for that reason: converting is low regret (a typed Food Chest gives only food, and HQ 31 needs 1.3G of it later), and the preview check at 23:21Z catches a real food row.

## The wave

`plan --hours 4` minted 17 units: the 02:03Z wave (arms-race, building-queues PL-08, donations, harvest PL-16, radar PL-17, research PL-04, survivors, training PL-09), the 02:30Z group (duel-score, gifts, help, mail, star-ceremony, train) and the daily-reset units at 02:00Z (daily-missions, vip, scout PL-07). The roster donations unit was closed as expired; the passes are the schedule. The specifics were added to the 16 others. All 80 units in the inbox pass the forecast check, none has a window inside 08:00Z to 08:40Z on 11-24 to 11-26, and one old midday scout unit (expiring 02:00Z) would expire unrun in a simulation at five minutes a unit.
