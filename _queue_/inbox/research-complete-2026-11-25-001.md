---
unit: research-complete-2026-11-25-001
regular: research
activity: research-queue
segment: 1
priority: 1
created_at: 2026-11-23T15:09:24Z
expires_at: 2026-11-25T04:30:00Z
planned_for:
not_before: 2026-11-25T02:39:30Z
window: lab 2 iron output v completion about 0239z fallback if not moved by the speed up
est_minutes: 10
serves: PL-04
chain_id: complete-2026-11-25
chain_seq: 1
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
---

# research

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: PL-04

## Brief (planner, lab 2 Iron Output V completion, 2026-11-25T02:39Z)

serves: PL-04

Iron Output V (lab 2) was started 2026-11-23T14:00:54Z for 131,879 s and ends about 2026-11-25T02:38:53Z, unless the 17:30Z unit's tech spend moved it to about 17:30Z on 11-24. Power registers only on Complete. Quiet-window margin: 5 h 21 min before the daily 08:00Z window; see `_records_/2026-11-22/queue-planning/2830-quiet-window-margins.md`. A TIPS dialog about another device: STOP, report, never Confirm. Routes and stop reasons, with the Age of Oil tree route (the running node's icon at (456,925), never (603,925)): `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`.

1. Flask icon: read BOTH labs (tag text, timers to the second). If Iron Output V is already completed and lab 2 runs something, start nothing and stop.
2. Press COMPLETE on Iron Output V, never Finish Now; Total Power before and after.
3. If lab 1 is idle because Oil Output I was not started at 17:30Z, start Oil Output I level 1 there: it needs Food, Iron and Coin Output V at level 1 and 60,000 oil; preview iron 3.7M, food 3.7M, coin 11.2M; coin N = ceil((node coin + 10M floor - coin now) / 2.4364M) UR chests, STOP above 40; the Resources tab opens with the 5,000 Diamonds x16 tile SELECTED, so confirm the tile name; read the Finish Now clock, not the Research button.
4. Otherwise start in lab 2 a Special Forces +15K node with no speed-up (the Strategist names it; if none is named, read the candidates, start nothing and say so).
5. No other speed-ups. Read the oil counter.

Up to two runs, 12 steps each. Tag text beside every number; none means [G].
Cost cap, stated: 0.90 USD per run (the harness stops near 0.36 of it).
