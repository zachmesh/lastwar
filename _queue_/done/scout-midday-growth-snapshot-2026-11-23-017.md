---
unit: scout-midday-growth-snapshot-2026-11-23-017
regular: scout-midday
activity: perception-scout
segment: 2
priority: 2
created_at: 2026-11-23T08:08:28Z
expires_at: 2026-11-23T12:00:00Z
planned_for:
not_before: 2026-11-23T11:45:00Z
window: growth snapshot A1 read only never press Upgrade
est_minutes: 10
serves: snapshot (Story 868)
chain_id: growth-snapshot-2026-11-23
chain_seq: 17
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
  summary: retired by the planner: A1 not wanted by the Strategist
  claimed: []
  claimed_count: 0
  evidence: 
  follow_up: none
  stats:
  stats_missing: [target, achieved, resources_gained, costs, verified]
  stats_warnings: []
---

# scout-midday

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

## Brief (planner, growth snapshot A1, Story 868, from the scout's updated unit table)

serves: snapshot (Story 868)

Read-only unit A1. Queue placement: Not before 11:45Z: Unlock Oil Well frees about 11:43Z and the Age of Oil nodes read locked until then.

Question: What are the HQ and Tech Center levels, how far is Special Forces, and what do the first Age of Oil nodes really cost and take?

Route: Base screenshot first: read the Oil Well banner text. Flask icon (about 110,262) opens the RESEARCH QUEUE or a tree; back arrow to the TECH hub; scroll to the Special Forces row (cut off on 2026-11-11) and read its percent; open the Age of Oil row or tree, tap the first node, read the preview panel, X; second node the same. HQ and Tech Center bodies, label only.

Read: Special Forces percent; Valor Badge stock; per node name, level, cost lines (food, iron, coin, Valor), time, power gain, prerequisite lines with check marks, Research button state (read, never press); slot 1 time left on Unlock Oil Well; Oil Well banner text; HQ and Tech Center levels, copied from B1 rows if filed.

Budget: at most 8 steps and 10 minutes. Notes: Output _records_/<date>/growth/<HHMM>-a1-oil-gate.csv, schema c_oil_gate. Start no earlier than 11:45Z: Unlock Oil Well frees about 11:43Z and Age of Oil nodes may stay hidden or locked until then; run earlier and the nodes read locked. If steps run out keep this order: Special Forces percent, node 1, banner, node 2, HQ and Tech Center labels. Never press Research or Speed Up; a node panel with a Research button is a preview, close by X. Banner tap optional and once: if a Build or Construct panel opens read cost, time, power and prerequisites, close by X, never press Build.

Rules: stop rules R1 to R7 in `_records_/2026-11-22/perception-scout/2345-snapshot-protocol.md`; red lines and the snap command in `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`. Snap takes only K or M numbers: write 1.1G as 1100M. Do not enqueue a chain successor.

Tag text: beside every number from a building panel write its tag text (name and level above the building after the tap; `_records_/2026-11-22/coach/0255-tag-text-check.md`); none means [G]. Add a tag_text column.
Cost cap, stated: 0.60 USD (the harness stops near 0.36 of it).
