---
unit: research-speedup-coin-v-2026-11-23-002
regular: research
activity: research-queue
segment: 1
priority: 1
created_at: 2026-11-23T13:43:44Z
expires_at: 2026-11-23T12:00:00Z
planned_for:
not_before: 2026-11-23T13:45:00Z
window: fallback window to 0800z if the first unit did not run lab 2 coin output v speed up
est_minutes: 12
serves: PL-04
chain_id: speedup-coin-v-2026-11-23
chain_seq: 2
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
  summary: retired by the planner: the Coin Output V speed-up unit -001 completed the chain (Coin Output V completed, Iron Output V started 14:00:54Z)
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

Serves: PL-04

## Brief (planner, Coin Output V tech speed-up then Iron Output V, plan PL-04, Steer A's three conditions)

serves: PL-04
FALLBACK for unit -001: if Coin Output V is already completed and Iron Output V is running in lab 2, start nothing, read the labs and stop.

Steer A approved PL-04 with three conditions; a stop note in this unit governs. A TIPS dialog about another device: STOP and report, never Confirm. Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`. The full order with every rule is `_records_/2026-11-22/queue-planning/2720-coin-output-v-chain-order.md`: follow it. In short, one run chain, and never leave lab 2 idle after the Complete:

1. Read both labs (tag text, timers to the second), coin, oil and the Speed-up tab counts.
2. FIRST convert the coin Iron Output V needs (plan on 6.2M): N = ceil((6.2M + 10M floor - coin now) / 2.4364M) UR chests, STOP above 40; the Resources tab opens with the 5,000 Diamonds tile SELECTED: confirm the tile name.
3. THEN the tech speed-up on Coin Output V: TECH items only; item name and quantity read before each press; largest first, one at a time; stop when it completes or under 60 minutes remain; inventory counts before and after.
4. THEN COMPLETE (+3,900 expected).
5. THEN read Iron Output V's panel BEFORE Start: effective time with no speed-up, original time, coin, iron, food, oil, power. It is the first clean read of the research speed: write it at once.
6. START Iron Output V in lab 2; read the timer and the oil. Never Finish Now.

Up to three runs, 12 steps each. Tag text beside every number; none means [G].
Cost cap, stated: 0.90 USD per run (the harness stops near 0.36 of it).
