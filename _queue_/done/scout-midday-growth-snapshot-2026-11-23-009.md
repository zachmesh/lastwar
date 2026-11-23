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
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T13:15:05Z
lease_until: 2026-11-23T13:35:05Z
result:
  status: done
  started_at: 2026-11-23T13:15:05Z
  finished_at: 2026-11-23T13:17:51Z
  duration_seconds: 166
  executor: operator
  summary: H2 Squad 1 heroes, run 20261123T131526Z-7a9697 (claude-gateway/claude-sonnet-5-5, 14 steps; claimed 13:15:05Z): no different-device dialog; Squad 1 = badge 1 on five cards, first two read: Carlie (UR aircraft, Lv.150, power 3,964,558, Attack 49.0K, HP 3.3M, Defense 13.7K, March Size 453, gear Lv.20/40/40/40, Tier 5 Stars, exclusive weapon Lv.10) and DVA (UR aircraft, Lv.150, power 3,682,929, Attack 70.5K, HP 2.2M, Defense 12.5K, March Size 453, gear Lv.40 x4, Tier 5 Stars, exclusive weapon Lv.10); nothing pressed.
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/perception-scout/1315-h2-squad1-heroes.md and _records_/2026-11-22/growth/1315-h2-squad1-heroes.csv; run 20261123T131526Z-7a9697
  follow_up: both heroes are at the Lv.150 cap (HQ 31 raises it to 155); skill counters 10721/26000 and 10721/28000, weapon counters 441/45 and 441/60 are the upgrade costs; the other three Squad 1 cards unread
  stats:
    target: read stars, skill levels, weapon level, gear and tier of two Squad 1 heroes
    achieved: two Squad 1 heroes read through four tabs each
    resources_gained: none (observe-only)
    points: 0
    costs: model 0.176355 USD; nothing spent
    verified: yes
    run_id: 20261123T131526Z-7a9697
    run_steps: 14
    actions_done: 24
    actions_refused: 0
    model_s_per_step: 6.5
    cost_usd: 0.176355
    device_takeovers: 0
    rules_used: R1,R6
    rule_failed: none
    rule_gap: The Attributes tab shows no star row; stars live on the Tier tab.
  stats_missing: []
  stats_warnings: []
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
