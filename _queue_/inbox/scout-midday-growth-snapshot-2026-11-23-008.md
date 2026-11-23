---
unit: scout-midday-growth-snapshot-2026-11-23-008
regular: scout-midday
activity: perception-scout
segment: 2
priority: 2
created_at: 2026-11-23T07:49:06Z
expires_at: 2026-11-23T13:30:00Z
planned_for:
not_before: 2026-11-23T09:05:00Z
window: growth snapshot H1 read only never press Upgrade
est_minutes: 10
serves: snapshot (Story 868)
chain_id: growth-snapshot-2026-11-23
chain_seq: 8
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
---

# scout-midday

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

## Brief (planner, growth snapshot H1, Story 868, from the scout protocol)

serves: snapshot (Story 868)

Read-only unit H1, order 8. Question: How many heroes are there and what do the list cards show; where do stars, skills, weapon, gear and tier live?

Route: HEROES button (bottom bar, left); scroll the Hero List to the end, class tab filters allowed; open one hero detail and page through every tab or section; back arrow twice.

Read: Every card level, class, rarity, stars and power if shown; roster count; names of all detail sections and fields for one hero.

Budget: at most 8 steps and 10 minutes. Notes: Hero detail tap failed in 2026-11-04; if two taps fail, try a class tab or a different card, then stop. Never press Upgrade, Promote, Skill Up, Equip, Recruit or any shard control.

Rules: stop rules R1 to R7 in `_records_/2026-11-22/perception-scout/2345-snapshot-protocol.md`; red lines and the snap command in `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`. Snap takes only K or M numbers: write 1.1G as 1100M. Do not enqueue a chain successor.

Cost cap, stated: 0.60 USD (the harness stops near 0.36 of it).
