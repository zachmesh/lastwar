---
unit: research-growth-convert-2026-11-23-002
regular: research
activity: research-queue
segment: 1
priority: 2
created_at: 2026-11-23T08:25:37Z
expires_at: 2026-11-23T13:35:00Z
planned_for:
not_before: 2026-11-23T12:55:00Z
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

NODE: Special Forces, best power per effective day by preview (the Strategist's pick by tag text overrides it).

Facts [M], `_records_/2026-11-22/research-queue/1144-queue-run.md`: Unlock Oil Well completed at 11:53Z; a lab slot idle since 11:42:55Z. Special Forces measures about +15,000 power and 3 days a level. Rules: `_records_/2026-11-22/queue-planning/2430-conversion-rules.md`.

1. Flask icon: READ BOTH LAB SLOTS FIRST by tag text with the time left. If slot 2 is busy (the owner's research, or a Special Forces node already running), start NOTHING: record its tag text and timer to the second and finish the Special Forces survey read-only. If no lab is idle, write the time left and stop.
2. Open the Special Forces tree and read each node's preview by tag text (effect, power gain, coin, iron, food, effective time). Pick the best power gain per effective day; write the top two. Read coin first and convert only what it lacks: N = ceil((node coin + 10M - coin now) / 2.4364M) UR Coin Chests (from 9.8M a 20.1M node needs 9); check the Total line against the need before Use; if N is 0 or less skip, and if N would exceed 28 (87 minus the 59 kept for tomorrow's two grounds) STOP and record. HAZARD: the Resources tab opens with the 5,000 Diamonds x16 tile SELECTED and a live Use: tap the intended tile first, confirm its name in a frame, never Use with another tile selected; read the number field AND the Total line in a frame before Use; no choice chests. Read coin after, press Research once, read the timer to the second, then snap. No speed-up.
3. If the tree cannot be read or no node fits, start nothing; continue the read-only survey of trees not yet covered.

Tag text beside every node-panel number; none means [G].

15 minutes, 10 steps. No hero-lever conversion, speed-ups, stamina or diamond items. No chain successor.
Cost cap, stated: 0.90 USD (the harness stops near 0.36 of it).
