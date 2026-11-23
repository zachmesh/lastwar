---
unit: scout-midday-growth-snapshot-2026-11-23-010
regular: scout-midday
activity: perception-scout
segment: 2
priority: 2
created_at: 2026-11-23T07:49:10Z
expires_at: 2026-11-23T13:30:00Z
planned_for:
not_before: 2026-11-23T09:05:00Z
window: growth snapshot H3 read only never press Upgrade
est_minutes: 10
serves: snapshot (Story 868)
chain_id: growth-snapshot-2026-11-23
chain_seq: 10
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
---

# scout-midday

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

## Brief (planner, growth snapshot H3, Story 868, from the scout protocol)

serves: snapshot (Story 868)

Read-only unit H3, order 10. Question: The same fields for the other three Squad 1 heroes.

Route: As H2.

Read: As H2; plus Squad 1 power if the squad panel is reachable.

Budget: at most 8 steps and 10 minutes. Notes: Whatever a hero cannot finish in three steps carries to the next weekly run. Heroes six and beyond wait for the ranking.

Rules: stop rules R1 to R7 in `_records_/2026-11-22/perception-scout/2345-snapshot-protocol.md`; red lines and the snap command in `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`. Snap takes only K or M numbers: write 1.1G as 1100M. Do not enqueue a chain successor.

Cost cap, stated: 0.60 USD (the harness stops near 0.36 of it).
