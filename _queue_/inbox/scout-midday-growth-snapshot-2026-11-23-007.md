---
unit: scout-midday-growth-snapshot-2026-11-23-007
regular: scout-midday
activity: perception-scout
segment: 2
priority: 2
created_at: 2026-11-23T07:49:05Z
expires_at: 2026-11-23T13:30:00Z
planned_for:
not_before: 2026-11-23T09:05:00Z
window: growth snapshot F2 read only never press Upgrade
est_minutes: 10
serves: snapshot (Story 868)
chain_id: growth-snapshot-2026-11-23
chain_seq: 7
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
---

# scout-midday

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

## Brief (planner, growth snapshot F2, Story 868, from the scout protocol)

serves: snapshot (Story 868)

Read-only unit F2, order 7. Question: What do the lowest barracks and the Tech Center upgrades cost, take and add?

Route: As F1 on the Lv.24 barracks (button row has a green arrow) and the Tech Center.

Read: As F1; for the barracks also the next tier named; for the Tech Center the Special Forces line if any.

Budget: at most 8 steps and 10 minutes. Notes: Same stops as F1. The planner may swap the target after P1 to T2 if a better candidate shows.

Rules: stop rules R1 to R7 in `_records_/2026-11-22/perception-scout/2345-snapshot-protocol.md`; red lines and the snap command in `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`. Snap takes only K or M numbers: write 1.1G as 1100M. Do not enqueue a chain successor.

Cost cap, stated: 0.60 USD (the harness stops near 0.36 of it).
