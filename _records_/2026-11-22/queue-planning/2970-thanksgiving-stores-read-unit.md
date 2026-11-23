---
title: Queue Planning The Thanksgiving Event Stores Read Unit 2970 2026-11-23
created: 2026-11-23T09:45:00-08:00
modified: 2026-11-23T09:45:00-08:00
level: L0
version: 1.0.0
description: Planner pass staging a read-only unit for the three Thanksgiving Event tabs that spend earned free event currencies, so the Strategist can rank them against the other free-currency stores
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-0945-thanksgiving-read
trigger: coordinator message 17:36Z, operator record 1731
started_at: 2026-11-23T09:38:00-08:00
finished_at: 2026-11-23T09:45:00-08:00
verified: the operator record read for the tab names and the finding that the three tabs sit inside the Thanksgiving Event; word count under 450; validate exit 0
grounded_in:
  - source: _records_/2026-11-22/event-claims/1731-queue-run.md
---

# The Thanksgiving Event stores read unit, 2970

`events-thanksgiving-read-2026-11-23-001` (priority 3, 17:50Z to 2026-11-24T01:00Z, serves PL-06, up to two runs) reads the Store, the Lottery and the Gift of Thanks tabs of the Thanksgiving Event, which is reached by its own icon on the base and not through the eight-tab events hub; the Login tab is already read. It writes the event's end timer first (the deadline for spending), then per Store item the name, price in tickets or ingredients, bought over limit, any timer and what it gives; for the Lottery the draw buttons, costs, balance, free draw, prize list and any odds or pity counter; for the Gift of Thanks what the turkey is, its cost, who receives it and what the pot pays. It presses nothing: no Buy, Redeem, Draw, Send, Claim or Go, and any banner, link or payment surface stops the run under the standing rule. I used PL-06 as the coordinator allowed; if the Strategist names another store-ranking item, the serves line is a one-line edit. The ranking, the decision whether to draw and its cap, and the spending unit that follows are the Strategist's: a spending unit would reach Buy and Draw buttons and needs the exit plan stated before I mint it.
