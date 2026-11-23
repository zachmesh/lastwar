---
unit: research-growth-convert-2026-11-23-002
regular: research
activity: research-queue
segment: 1
priority: 2
created_at: 2026-11-23T08:25:37Z
expires_at: 2026-11-23T12:40:00Z
planned_for:
not_before: 2026-11-23T12:10:00Z
window: convert coin for the Drill Ground Expansion node and start it when the lab frees
est_minutes: 15
serves: capacity source: Drill Ground Expansion (lab at about 11:43Z)
chain_id: growth-convert-2026-11-23
chain_seq: 2
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
---

# research

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: capacity source: Drill Ground Expansion (lab at about 11:43Z)

## Brief (planner, conversion-and-spend for the lab, coordinator coin plan)

serves: capacity source: Drill Ground Expansion (the lab freeing about 11:43Z)

Backup unit. First open the labs: if a Drill Ground Expansion research is already running (started by the 11:44Z unit), start nothing, record its timer to the second and stop.

Conversion rules and amounts: `_records_/2026-11-22/queue-planning/2430-conversion-rules.md`; red lines and the snap command: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md` (K or M numbers only: write 1.1G as 1100M).

1. Open the labs with the flask icon. If 'Unlock Oil Well' shows finished, press COMPLETE first, because power registers only on Complete. If no lab is idle, read the time left to the second, write it with the UTC time and stop.
2. Open the Development tree and read the Drill Ground Expansion node preview: next level, coin, food, iron, time and any capacity or slots line. Read the Extra Barracks node the same way, read only. If the Expansion cost cannot be read, start nothing.
3. Convert exactly the node's coin cost by the rules (read Coin Chests first), and no more. Read coin on the HUD before and after. If the node also needs Valor Badges or an item you cannot cover from stock, stop and record it.
4. Press Research once on the Drill Ground Expansion node, read the new timer to the second, then run the snap command.

Budget: 15 minutes, 10 steps. Never convert hero levers; speed-ups, stamina items and diamond items are red lines. Do not enqueue a chain successor.

Cost cap, stated: 0.90 USD (the harness stops near 0.36 of it).
