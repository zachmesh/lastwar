---
unit: scout-midday-growth-snapshot-2026-11-23-009
regular: scout-midday
activity: perception-scout
segment: 2
priority: 2
created_at: 2026-11-23T07:49:08Z
expires_at: 2026-11-23T13:30:00Z
planned_for:
not_before: 2026-11-23T09:05:00Z
window: growth snapshot H2 read only never press Upgrade
est_minutes: 10
serves: snapshot (Story 868)
chain_id: growth-snapshot-2026-11-23
chain_seq: 9
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
---

# scout-midday

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

## Brief (planner, growth snapshot H2, Story 868, from the scout protocol)

serves: snapshot (Story 868)

Read-only unit H2, order 9. Question: What are stars, skill levels, weapon level, gear and tier of Squad 1 heroes one and two?

Route: Hero List, card, detail, then the section routes H1 recorded; back.

Read: Level, EXP stock over cost, power, Attack, HP, Defense, March Size, stars, skill levels, exclusive weapon level, gear, tier or specialization.

Budget: at most 8 steps and 10 minutes. Notes: Four steps per hero. Pick Squad 1 from the squad panel or the five highest power cards, and say which. Depends on H1.

Rules: stop rules R1 to R7 in `_records_/2026-11-22/perception-scout/2345-snapshot-protocol.md`; red lines and the snap command in `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`. Snap takes only K or M numbers: write 1.1G as 1100M. Do not enqueue a chain successor.

Cost cap, stated: 0.60 USD (the harness stops near 0.36 of it).
