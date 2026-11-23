---
unit: research-growth-convert-2026-11-23-002
regular: research
activity: research-queue
segment: 1
priority: 2
created_at: 2026-11-23T08:25:37Z
expires_at: 2026-11-23T12:48:00Z
planned_for:
not_before: 2026-11-23T12:15:00Z
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

## Brief (planner, the idle lab slot, coordinator order 12:13Z)

serves: capacity source: the idle lab slot, Special Forces node by power per effective day, else survey

NODE: Special Forces, best power per effective day by preview. The Strategist's pick by tag text, if it arrives first, overrides this line.

Facts [M], `_records_/2026-11-22/research-queue/1144-queue-run.md`: Unlock Oil Well was completed at 11:53Z; a lab slot has been idle since 11:42:55Z. Special Forces measures about +15,000 power and about 3 days a level. Units and Special Forces hold no Drill Ground or Unit Count node; Load Training IV is load capacity. Rules: `_records_/2026-11-22/queue-planning/2430-conversion-rules.md`; `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

1. Flask icon: read both labs by tag text with the time left. If a Special Forces node already runs in a lab (the operator may have started it), start nothing, record its timer to the second and stop. If no lab is idle, write the time left with the UTC time and stop.
2. Open the Special Forces tree and read each node's preview by tag text (effect, power gain, coin, iron, food, effective time). Pick the best power gain per effective day; write the top two. Convert only the coin it lacks with the FEWEST UR Coin Chests (7 chests, 17.05M, cover a 20M node; the 59 UR for tomorrow stay untouched, 87 minus 7 is 80; keep the 10M coin floor). HAZARD: the Resources tab opens with the 5,000 Diamonds x16 tile SELECTED and a live Use: tap the intended tile first, confirm its name in a frame, never Use with another tile selected, and read the number field AND the Total line in a frame before Use; no choice chests. Read coin after, press Research once, read the timer to the second, then snap. No speed-up.
3. If the tree cannot be read or no node fits, start nothing and continue the read-only survey of trees the newest research-queue record has not covered.

Tag text: beside every number from a node panel write its tag text; none means [G].

15 minutes, 10 steps. Never convert hero levers; no speed-ups, stamina or diamond items. No chain successor.
Cost cap, stated: 0.90 USD (the harness stops near 0.36 of it).
