---
title: Queue Planning Serves Flip Plan Mapping Slot Reads And Route Card 2690 2026-11-23
created: 2026-11-23T05:41:00-08:00
modified: 2026-11-23T05:41:00-08:00
level: L0
version: 1.0.0
description: Planner pass on Steer A's flip plan - every live unit's serves mapped to a plan item or an exempt word, the units without a ledger row listed, three night reads staged with a named capacity blocker, the Coach's top partial causes answered with a route card, and the stale Gold Mine figure corrected
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-0541-flip-plan
trigger: coordinator message with Steer A's flip plan and the C1 coin sink previews
started_at: 2026-11-23T05:28:00-08:00
finished_at: 2026-11-23T05:41:00-08:00
verified: the tool's own forecast_class run on every inbox unit before and after; plan rows read from plan-of-record.csv; word counts under 450; validate exit 0
grounded_in:
  - source: _records_/2026-11-22/strategy/plan-of-record.csv and forecast-ledger.csv
  - source: _records_/2026-11-22/coach/0501-conformance-report-2.md
  - source: _records_/2026-11-22/perception-scout/1323-c1-coin.md
---

# Serves flip plan, mapping and slot reads, 2690

## 1. Mapping

The tool accepts a `serves` part only if it is exactly upkeep, snapshot or baseline, a 'fill idle slot' phrase, or a plan item id with a forecast ledger row; free text such as 'snapshot (Story 868)' fails. Before: 38 inbox units not ok. Rewritten, 22 live units: the oil well and Oil Depot units (7) to PL-17; the weapon and hero reads (5) to PL-06; the three builder units to PL-08; the two Complete units to PL-04; the two plunder units to PL-18; the two power units and the collect unit to PL-07. After: 16 not ok, of which 14 are expired units still in the inbox awaiting sync (the retired T1, Food Output V, B2, lab and snapshot units) and 2 are live with NO PLAN ROW: `donations-playbook-t2-2026-11-23-001` and `passes-playbook-t3-2026-11-23-001`, the Researcher's falsification tests. The Strategist must add a row for them or retire them. The store buys, not yet staged, have no plan id either.

## 2. A plan conflict fixed

The plan of record (PL-04, PL-10, PL-16, decision 06) puts lab 2 on Iron Output V after Coin Output V and lab 1 at 17:30Z on Oil Output I level 1 if all three Output V are done, else a Special Forces +15K node with no speed-up. My Complete units said Research Enhancement V and Iron Output V. Their NODE lines now follow the plan; the windows are unchanged. PL-04 also proposes about 1,540 tech minutes on Coin Output V now to free lab 2; no unit exists for that and it needs Steer A's approval.

## 3. Idle slot reads

`building-queues-slot-read-2026-11-24-001`, `research-slot-read-labs-2026-11-24-001` and `training-slot-read-barracks-2026-11-24-001`, window 02:10Z to 04:30Z, read-only, serving PL-08, PL-04 and PL-09. An idle barracks is read without pressing Train; the blocker is written exactly 'blocked by capacity: Drill Ground Full' with the building's tag text, and counted in a new stat `slots_blocked_capacity`, apart from `slots_idle`, so the tool can subtract it. The tool has no such exemption yet.

## 4. Partials

The Coach's report names two growth causes: the tap method (10 of 12 growth partials) and a missing precondition (2). The fix is the route card [2700](2700-route-card-and-stop-reasons.md): verified routes, the safe point (400,640), one building per fresh frame, and six stop reasons. It is pointed to from 29 live units and the unit template, which now also demands an exact serves value and a precondition. The 11-24 fills had stale lines (Age of Oil off, Special Forces labs, oil twice a day); they are corrected.

## 5. Stale figure

The C1 brief and the scout's unit table said 'Gold Mine to Lv.30 cost 1.9M coin for +14,800 power'. Measured: Lv.28 to 29 costs 23.8M coin and 73.1M iron for +14,800 power in 4d 14:20:24, 622 power per million coin and about 3,200 per builder-day; the Farmland is the same time for +14,900 and 626. The 1.9M figure has no source I can find. The ledger carries the measured rows.
