---
unit: scout-midday-growth-snapshot-2026-11-23-014
regular: scout-midday
activity: perception-scout
segment: 2
priority: 2
created_at: 2026-11-23T08:08:27Z
expires_at: 2026-11-23T10:54:00Z
planned_for:
not_before: 2026-11-23T09:05:00Z
window: growth snapshot D1b read only never press Upgrade
est_minutes: 10
serves: snapshot (Story 868)
chain_id: growth-snapshot-2026-11-23
chain_seq: 14
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
---

# scout-midday

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

## Brief (planner, growth snapshot D1b, Story 868, from the scout's updated unit table)

serves: snapshot (Story 868)

Read-only unit D1b. Queue placement: Decorations; after the routine claims, ahead of P1.

Question: What are the decoration levels and collection, and what does the next decoration step cost?

Route: Decoration Gallery from the base screen left-edge icons (the entry is unreliable and one stored point opened a paid offer, so ground fresh and never tap a point that opens a purchase surface); Overview tab, then every other tab; blue back arrow.

Read: Collection progress by rarity, Total Decor Combat Power, the seven bonuses, tab names, level of each decoration, next-level cost (Decor Component, Universal Decor Component), power gain if shown.

Budget: at most 8 steps and 10 minutes. Notes: Output _records_/<date>/growth/<HHMM>-d1b-decor.csv, schema g_decor. Decorations and Building Stats is 7,376,484 of Hero Power, up 111,808 since 2026-11-08, and the Overview read 6,160,413 combat power with UR 18 of 39, SSR 7 of 19, SR 4 of 4 on 2026-11-09, so decorations may be the cheapest large line; tabs beyond Overview were never read. If a pack or offer opens, close by X and end the unit (S2). Never press Upgrade, Unlock, Buy or Use.

Rules: stop rules R1 to R7 in `_records_/2026-11-22/perception-scout/2345-snapshot-protocol.md`; red lines and the snap command in `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`. Snap takes only K or M numbers: write 1.1G as 1100M. Do not enqueue a chain successor.

Cost cap, stated: 0.60 USD (the harness stops near 0.36 of it).
