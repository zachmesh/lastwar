---
unit: research-growth-convert-2026-11-23-002
regular: research
activity: research-queue
segment: 1
priority: 2
created_at: 2026-11-23T08:25:37Z
expires_at: 2026-11-23T12:00:00Z
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
result:
  status: expired
  started_at:
  finished_at: 2026-11-23T13:45:50Z
  duration_seconds: 
  executor:
  summary: retired by the planner: the Special Forces fill was withdrawn and the labs are full
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

Serves: capacity source: Drill Ground Expansion (lab at about 11:43Z)

## Brief (planner, the idle lab slot, Age of Oil research priority, owner orders OD-18 and OD-19)

serves: capacity source: the idle lab slot, first node of the Age of Oil critical path

NODE: the node the Strategist names; none named = a read-only survey of the Age of Oil tree. The Special Forces fill is withdrawn. Both labs go to the Age of Oil critical path (Base Expansion is its last node) in dependency order from the real previews; the running Defense Training VIII is never cancelled.

Facts: a lab slot has been idle since 11:42:55Z. Coin is near zero (55.9K at 12:36Z), so convert only just-in-time under the formula. A TIPS dialog about another device means STOP and report; never Confirm.

1. Flask icon: READ BOTH LAB SLOTS FIRST by tag text with the time left. If slot 2 is busy, start NOTHING: record its tag text and timer to the second and stop.
2. If NODE names a node: open it by tag text, read the preview (effect, coin, iron, food, oil, time, prerequisite met or not). Read coin, then convert only what it lacks: N = ceil((node coin + 10M - coin now) / 2.4364M) UR Coin Chests, checking the Total line against the need before Use; skip if N is 0 or less; STOP and record if N would exceed 24 (87 minus the 63 kept for tomorrow's grounds). HAZARD: the Resources tab opens with the 5,000 Diamonds x16 tile SELECTED and a live Use: tap the intended tile first, confirm its name, never Use with another selected; read the number field AND the Total line in a frame before Use; no choice chests. Read coin after, press Research once, read the timer to the second, snap.
3. If NODE names none: start nothing; if a newer Age of Oil survey record exists in `_records_/2026-11-22/research-queue/` stop, otherwise read the tree as unit `research-age-of-oil-survey-2026-11-23-001` says.

Rules: `_records_/2026-11-22/queue-planning/2430-conversion-rules.md`. Tag text beside every node-panel number; none means [G].

15 minutes, 10 steps. No hero levers, stamina or diamond items. No chain successor.
Cost cap, stated: 0.90 USD (the harness stops near 0.36 of it).
