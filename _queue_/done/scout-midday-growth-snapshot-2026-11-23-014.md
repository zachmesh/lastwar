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
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T10:40:34Z
lease_until: 2026-11-23T11:00:34Z
result:
  status: partial
  started_at: 2026-11-23T10:40:34Z
  finished_at: 2026-11-23T10:46:30Z
  duration_seconds: 356
  executor: operator
  summary: Decoration Gallery read D1b, runs 20261123T104131Z-52ba72, 20261123T104303Z-7dbea4 and 20261123T104439Z-1ab817 (claude-gateway/claude-sonnet-5-5, 16 steps; claimed 10:40:34Z after registering the read receipt for the 2234 ticker record): gallery entry NOT found - the left-edge bubble (93,339) opens nothing, the left-column vehicle icon (107,580) opens the Trucks screen, the orange card bubble (437,296) opens the Cosmetics, Coupon and Crystal STORE (Coupon Store 150 coupons, Crystal Shop 4,442 crystals and 213.2K of a second item selling Gold Brick, Silver Brick, vouchers, 100 Diamonds, 1h Speed-up, restocks on the 1st); Overview, tabs, levels and costs unread. Read-only, nothing bought, no Upgrade.
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/perception-scout/1040-d1b-decor.md and _records_/2026-11-22/growth/1040-d1b-decor.csv; runs 20261123T104131Z-52ba72, 20261123T104303Z-7dbea4, 20261123T104439Z-1ab817
  follow_up: find the Decoration Gallery entry (try the Heroes screen, the HQ radial menu, Base customization); read the Crystal Shop prices (100 Diamonds for crystals would be an earned source); the orange card bubble is the store, not the gallery
  stats:
    target: read the Decoration Gallery Overview, every tab, levels and next-level costs
    achieved: gallery not reached; the store behind the orange bubble read for the Strategist
    resources_gained: none (observe-only)
    points: 0
    costs: model 0.233759 USD in three runs; nothing spent
    verified: yes
    blocker_category: c
    run_id: 20261123T104439Z-1ab817
    run_steps: 16
    actions_done: 24
    actions_refused: 0
    model_s_per_step: 5.8
    cost_usd: 0.233759
    device_takeovers: 0
    rules_used: R1,R2,R3
    rule_failed: R2
    rule_gap: Digest names left-edge entry only; the stored points now open a store or nothing, gallery location unknown.
  stats_missing: []
  stats_warnings: []
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
