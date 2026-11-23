---
title: Queue Planning Other Wording And The Units With No Serves Line 2960 2026-11-23
created: 2026-11-23T09:20:00-08:00
modified: 2026-11-23T09:20:00-08:00
level: L0
version: 1.0.0
description: Planner answer to the toolsmith's honest counting - the staged units checked for other wording, and where the fourteen executed units with no serves line came from
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-0920-serves-wording
trigger: coordinator message 17:12Z
started_at: 2026-11-23T09:12:00-08:00
finished_at: 2026-11-23T09:20:00-08:00
verified: the inbox (87 units) and the done folder (76 units executed in 12 hours) read with the tool's own unit list and forecast_class; the commit log read for the dates of the serves changes
grounded_in:
  - source: _tools_/queue.py list_units and forecast_class
---

# Other wording and the units with no serves line, 2960

## Staged units

None of the 87 units in the inbox has other wording or no serves line: every serves is exactly upkeep, a plan item id with a ledger row, or the fill idle slot phrase. The 21 executed units with other wording were mine: 14 read 'snapshot (Story 868)', 2 'baseline Age of Oil research tree' and the rest 'baseline coin conversion' and similar, all written before I learned that the exact words are the rule. Any note belongs in the body of the unit, never in serves; from now on I write exactly snapshot, baseline, a plan item id, or upkeep. The 22:03Z wave is not minted yet; until the roster branch lands, every unit it mints is checked and remapped by hand.

## The 14 executed units with no serves line

Both causes pre-date the requirement. Five were minted by plan or sync on 2026-11-22 (scout-midday 03:41Z, daily-missions, vip and scout 14:42Z, events 15:43Z), when the roster had no serves default: the first unit that carries a serves line was created at 22:43Z. Nine were enqueued by hand on 2026-11-23 between 06:56Z and 08:08Z, before the enqueue command refused a unit without serves: arms-race, secrets, donations, passes, building-queues, a midday scout, and three scout read units of the growth-snapshot chain (002, 004 and 011). Eight of the nine had no chain id; no live path produces one now, since enqueue refuses and the roster default exists.
