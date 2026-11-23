---
unit: research-complete-2026-11-24-001
regular: research
activity: research-queue
segment: 1
priority: 1
created_at: 2026-11-23T13:01:54Z
expires_at: 2026-11-23T12:00:00Z
planned_for:
not_before: 2026-11-24T14:59:30Z
window: lab 2 coin output v completion about 1459z then research enhancement v
est_minutes: 10
serves: PL-04
chain_id: complete-2026-11-24
chain_seq: 1
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
result:
  status: expired
  started_at:
  finished_at: 2026-11-23T14:06:09Z
  duration_seconds: 
  executor:
  summary: retired by the planner: lab 2 already completed Coin Output V today and runs Iron Output V to about 2026-11-25T02:39Z
  claimed: []
  claimed_count: 0
  evidence: 
  follow_up: none
  stats:
  stats_missing: [target, achieved, resources_gained, costs, verified]
  stats_warnings: []
---

# research

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: capacity source: lab 2 Coin Output V completion and Iron Output V

## Brief (planner, lab 2 Coin Output V completion, FALLBACK to the speed-up unit, trigger schedule-22e92ed7)

serves: PL-04

FALLBACK: unit `research-speedup-coin-v-2026-11-23-001` (a tech speed-up, then Complete, then Iron Output V in lab 2) should have run first. If lab 2 already runs Iron Output V, start nothing: read both labs by tag text with the time left and stop. Otherwise Coin Output V finishes at about 2026-11-24T14:59:10Z; power registers only on Complete. A TIPS dialog about another device: STOP and report, never Confirm. Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`.

NODE: Iron Output V (the last Output V node, plan PL-04, decision 06). Oil Output I level 1 comes only when all three Output V nodes are done and oil is at least 60K.

1. Flask icon: read BOTH labs by tag text with the time left. Press COMPLETE on the finished Coin Output V (never Speed Up or Finish Now); Total Power before and after.
2. Read oil and coin. Open Iron Output V by tag text and READ its preview (coin, iron, food, oil, BASE and EFFECTIVE time, prerequisite, power); M is 485,100 s over the effective seconds. If the prerequisite is unmet or oil short, start nothing and say why.
3. Coin: N = ceil((node coin + 10M floor - coin now) / 2.4364M) UR Coin Chests; skip if 0 or less; STOP above 40. HAZARD: the Resources tab opens with the 5,000 Diamonds x16 tile SELECTED and a live Use: tap the Coin Chest UR, confirm the tile name, read the number field AND the Total line in a frame before Use.
4. Press Research once; read the timer to the second and the oil.
5. Speed-ups: TECH items first (read the Backpack first, 11,400 minutes at 13:40Z; the other device also uses them), reduce a defaulted quantity, write minutes used and the new finish time; never Finish Now; stop on an oil-bound level.

Up to two runs, 10 steps each. Tag text beside every number; none means [G].
Cost cap, stated: 0.90 USD per run (the harness stops near 0.36 of it).
