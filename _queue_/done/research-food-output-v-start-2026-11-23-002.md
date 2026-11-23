---
unit: research-food-output-v-start-2026-11-23-002
regular: research
activity: research-queue
segment: 1
priority: 1
created_at: 2026-11-23T13:00:50Z
expires_at: 2026-11-23T12:00:00Z
planned_for:
not_before: 2026-11-23T13:00:00Z
window: lab 1 starts food output v fallback window to 0200Z if the first unit did not run
est_minutes: 10
serves: capacity source: Food Output V, the first Base Expansion path node
chain_id: food-output-v-start-2026-11-23
chain_seq: 2
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
result:
  status: expired
  started_at:
  finished_at: 2026-11-23T13:45:49Z
  duration_seconds: 
  executor:
  summary: retired by the planner: both labs were already running Food Output V and Coin Output V from the other device
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

Serves: capacity source: Food Output V, the first Base Expansion path node

## Brief (planner, lab 1 starts Food Output V, Steer A decisions on the Base Expansion path)

serves: capacity source: Food Output V, the first Base Expansion path node

FALLBACK for unit -001: if Food Output V already runs in a lab, start nothing and stop. Otherwise LAB 1 STARTS FOOD OUTPUT V (the Base Expansion path), not a Special Forces node. Run after the Age of Oil survey unit; Base Expansion is the owner's research priority (`_records_/retro/owner-decisions-log/od-20261123-19.md`). A TIPS dialog about another device: STOP and report, never Confirm.

1. Flask icon: read BOTH lab slots first (tag text and timers) and use the idle one. Read the oil counter and coin.
2. Open Food Output V and READ its preview: coin, iron, food, oil, BASE time, EFFECTIVE time, power. Write them with the tag text.
3. Coin by the fewest fixed UR Coin Chests: N = ceil((node coin + 10M floor - coin now) / 2.4364M); skip if N is 0 or less; STOP above 40. HAZARD: the Resources tab opens with the 5,000 Diamonds x16 tile SELECTED and a live Use: tap the Coin Chest UR first and confirm the tile name; read the number field AND the Total line in a frame before Use. Read coin after.
4. Press Research once; read the new timer to the second.
5. Then TECH speed-up items first, only if the Speed-up panel shows a gain (stock at least 15,360 minutes): read the panel first, reduce a defaulted quantity before pressing, write the minutes used, the new finish time and the oil at that moment. The weekly budget while the chain is time-bound is up to 30 percent of the general stock (about 105,000 minutes), and KEEP AT LEAST 100,000 general minutes in reserve until the multiplier M is read. Never Finish Now. Stop using speed-ups on any level whose wait is oil-bound.

Up to two runs, 10 steps each. Rules: `_records_/2026-11-22/queue-planning/2430-conversion-rules.md`. Tag text beside every number; none means [G]. Nothing past Food Output V is staged. No chain successor.
Cost cap, stated: 0.90 USD per run (the harness stops near 0.36 of it).
