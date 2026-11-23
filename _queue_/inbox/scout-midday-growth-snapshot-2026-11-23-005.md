---
unit: scout-midday-growth-snapshot-2026-11-23-005
regular: scout-midday
activity: perception-scout
segment: 2
priority: 2
created_at: 2026-11-23T07:49:01Z
expires_at: 2026-11-23T11:02:00Z
planned_for:
not_before: 2026-11-23T09:05:00Z
window: growth snapshot B1 read only never press Upgrade
est_minutes: 8
serves: snapshot (Story 868)
chain_id: growth-snapshot-2026-11-23
chain_seq: 5
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
---

# scout-midday

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

## Brief (planner, growth snapshot B1, Story 868, from the scout protocol)

serves: snapshot (Story 868)

Read-only unit B1, order 5. Question: What level are HQ, Tech Center and Builders Hut, and what does the hut bank?

Route: Tap each building body (re-ground fresh), read the name and level label; paw button for Building Details on HQ and Builders Hut; close with the panel X.

Read: HQ level; Tech Center level; Builders Hut level, builder count, banked free speed-up time; power line if Details shows one.

Budget: at most 8 steps and 8 minutes. Notes: Never tap the green arrow here (previews belong to F1 and F2). Do not tap Quick Dispatch. Do not carry any level from older records: they conflict (HQ 26 to 30).

Rules: stop rules R1 to R7 in `_records_/2026-11-22/perception-scout/2345-snapshot-protocol.md`; red lines and the snap command in `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`. Snap takes only K or M numbers: write 1.1G as 1100M. Do not enqueue a chain successor.

Cost cap, stated: 0.60 USD (the harness stops near 0.36 of it).
