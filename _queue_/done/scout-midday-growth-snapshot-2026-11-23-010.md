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
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T13:18:25Z
lease_until: 2026-11-23T13:38:25Z
result:
  status: done
  started_at: 2026-11-23T13:18:25Z
  finished_at: 2026-11-23T13:21:51Z
  duration_seconds: 206
  executor: operator
  summary: H3 Squad 1 heroes three to five, run 20261123T131845Z-0bafb8 (claude-gateway/claude-sonnet-5-5, 15 steps; claimed 13:18:25Z): no different-device dialog; Murphy (Tank UR, Lv.150, power 3,528,417, Attack 48.8K, HP 3.1M, Defense 13.0K, March Size 435, Tier 5 Stars, exclusive weapon Lv.3), Lucius (Aircraft UR, Lv.150, power 3,009,670, Tier 4 Stars, no exclusive weapon tab), Schuyler (Aircraft UR, Lv.150, power 2,922,326, Tier 4 Stars, no exclusive weapon tab); the five Squad 1 powers sum to 17,107,900; no squad panel on the list screen; nothing pressed.
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/perception-scout/1319-h3-squad1-heroes.md and _records_/2026-11-22/growth/1319-h3-squad1-heroes.csv; run 20261123T131845Z-0bafb8
  follow_up: Tier 4 to 5 Stars for Lucius (counter 680/96) and Schuyler (680/24) is the cheapest visible hero lever; a red target icon with a 00:00:30 timer appeared at the right of the base (unread)
  stats:
    target: read the other three Squad 1 heroes
    achieved: three heroes read through their tabs; two have no exclusive weapon tab
    resources_gained: none (observe-only)
    points: 0
    costs: model 0.224241 USD; nothing spent
    verified: yes
    run_id: 20261123T131845Z-0bafb8
    run_steps: 15
    actions_done: 26
    actions_refused: 0
    model_s_per_step: 6.5
    cost_usd: 0.224241
    device_takeovers: 0
    rules_used: R1,R6
    rule_failed: none
    rule_gap: The Hero List shows no squad panel or Squad power; heroes at Tier 4 have no exclusive weapon tab.
  stats_missing: []
  stats_warnings: []
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
