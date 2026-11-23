---
unit: research-complete-2026-11-24-002
regular: research
activity: research-queue
segment: 1
priority: 1
created_at: 2026-11-23T13:01:55Z
expires_at: 2026-11-24T19:00:00Z
planned_for:
not_before: 2026-11-24T17:30:10Z
window: lab 1 food output v completion about 1730z then iron output v
est_minutes: 10
serves: capacity source: lab 1 Food Output V completion and Iron Output V
chain_id: complete-2026-11-24
chain_seq: 2
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
---

# research

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: capacity source: lab 1 Food Output V completion and Iron Output V

## Brief (planner, lab 1 completion and next Base Expansion node, trigger schedule-de14b612)

serves: capacity source: lab 1 Food Output V completion and Iron Output V

Food Output V finishes at about 2026-11-24T17:29:58Z; power registers only on Complete, so leaving it wastes the lab and the power. OD-19. A TIPS dialog about another device: STOP and report, never Confirm.

NODE: Iron Output V (follows Food Output V); Oil Output I level 1 comes only when all three Output V nodes are done and oil is at least 60K. The Strategist may change it by a note here.

1. Flask icon: read BOTH labs by tag text with the time left. Press COMPLETE on the finished Food Output V (never Speed Up or Finish Now) and Total Power before and after.
2. Read oil and coin. Open the NODE by tag text and READ its preview (coin, iron, food, oil, BASE and EFFECTIVE time, prerequisite, power). If the prerequisite is unmet or oil short, start nothing and say why.
3. Convert only the coin it lacks: N = ceil((node coin + 10M floor - coin now) / 2.4364M) UR Coin Chests; skip if 0 or less; STOP above 40. HAZARD: the Resources tab opens with the 5,000 Diamonds x16 tile SELECTED and a live Use: tap the Coin Chest UR first, confirm the tile name, read the number field AND the Total line in a frame before Use.
4. Press Research once; read the timer to the second and the oil.
5. Speed-ups (OD-19): TECH items first if the panel shows a gain (stock at least 15,360 minutes); read the panel first, reduce a defaulted quantity, write minutes used, the new finish time and the oil. Up to 30 percent of the general stock a week (about 105,000 minutes) while the chain is time-bound; keep 100,000 general minutes in reserve until M is read; never Finish Now; stop on an oil-bound level.

Up to two runs, 10 steps each. Tag text beside every number; none means [G]. Rules: `_records_/2026-11-22/queue-planning/2430-conversion-rules.md`.
Cost cap, stated: 0.90 USD per run (the harness stops near 0.36 of it).
