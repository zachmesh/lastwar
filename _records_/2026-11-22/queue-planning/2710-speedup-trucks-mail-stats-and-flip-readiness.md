---
title: Queue Planning Speed Up Trucks Mail Exact Stats And Flip Readiness 2710 2026-11-23
created: 2026-11-23T05:52:00-08:00
modified: 2026-11-23T05:52:00-08:00
level: L0
version: 1.0.0
description: Planner pass at 13:44Z to 13:50Z - the Coin Output V tech speed-up staged with a fallback, the trucks settle unit and the Train arrival reward mail put first, the exact idle-slot stat names applied, and the inbox cleaned for the forecast refusal at 2026-11-24T00:05Z
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-0552-speedup-trucks-flip
trigger: coordinator messages at 13:43Z and 13:44Z with the speed-up go, the trucks and mail items, and the exact stat names
started_at: 2026-11-23T05:42:00-08:00
finished_at: 2026-11-23T05:52:00-08:00
verified: unit files read back; the tool's forecast_class run on every inbox unit before and after; one expired unit closed first and its result file inspected; validate exit 0
grounded_in:
  - source: coordinator messages 13:43Z and 13:44Z
  - source: _records_/2026-11-22/strategy/plan-of-record.csv row PL-04
---

# Speed-up, trucks, mail, stats and flip readiness, 2710

## 1. The speed-up

`research-speedup-coin-v-2026-11-23-001` (window 13:45Z to 14:02Z, so it ranks right after the mail unit and before the 14:03Z wave) with a fallback `-002` (to 2026-11-24T08:00Z, which first checks whether Iron Output V already runs in lab 2). Run 1 reads both labs, opens the Speed Up of slot 2 (Coin Output V, about 25.3 h or 1,518 minutes left), uses TECH items only (8h x8 and 1h x126, 11,400 minutes), reads the item name and quantity in a frame before each press, largest first, one press at a time. Arithmetic: 8h x3 is 1,440 minutes and leaves 78; one 1h item leaves 18, under the 60-minute stop, so run 2 does the Complete and starts Iron Output V once the remainder has run out. The 14:59:30Z Complete unit is now the fallback, and the 17:30:10Z unit completes every finished node, including lab 2's Iron Output V if its speed-up aligns it. The Iron Output V speed-up is a separate unit that needs the real timer after its start.

## 2. Trucks and mail

`trucks-settle-2026-11-23-001` (14:20Z to 16:00Z): settle, claim Reward Recovery, re-dispatch, no Plunder, a contract floor of 200 (266 held, so at most about 66 refreshes). `mail-2026-11-23-0230` now expires 13:58Z so it goes first, with the Train arrival reward paragraph (the train shortcut badge '1' since 13:38Z).

## 3. Exact stat names

The slot-read units and the route card (now 1.1.0) use `--stat slots_blocked_by_capacity=<N> --stat capacity_blocker="Drill Ground Full"` as the toolsmith's exemption reads them, not `slots_blocked_capacity`; my note 2690 still shows the old name and is superseded here.

## 4. Flip readiness

All 14 expired units were closed with `queue.py complete --status expired` and a real summary each (the first one tested and its result file read), so no expired unit with an old serves sits in the inbox. Two live units have no plan row: the Researcher's T2 and T3, expiring 14:45Z and 15:45Z; I close them after expiry if they have not run. Units that `plan` and `sync` mint carry the roster default upkeep, and units I mint after 00:05Z carry plan item ids or an exempt word; `--no-require-forecast` is the emergency override.
