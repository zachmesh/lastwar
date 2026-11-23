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
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T12:59:56Z
lease_until: 2026-11-23T13:19:56Z
result:
  status: done
  started_at: 2026-11-23T12:59:56Z
  finished_at: 2026-11-23T13:02:34Z
  duration_seconds: 158
  executor: operator
  summary: H1 hero roster, run 20261123T130013Z-a04ef8 (claude-gateway/claude-sonnet-5-5, 12 steps; claimed 12:59:56Z): no different-device dialog; Hero List holds 31 heroes (16 UR, 12 SR, 4 R; tabs All, Tank, Missile, Aircraft); one UR hero detail paged through (Attributes, Skills, Tier, Exclusive Weapons tabs; power 3,964,558); stars on the Tier tab, skills on the Skills tab, gear on the Attributes tab; nothing pressed (no Upgrade, Skill Up, Recruit, Preview, Go).
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/perception-scout/1301-h1-heroes.md and _records_/2026-11-22/growth/1301-h1-heroes.csv; run 20261123T130013Z-a04ef8
  follow_up: the Tier tab Go button leads toward the Wall of Honor (unverified); half-stars and class icons approximate
  stats:
    target: read the hero roster and one hero detail
    achieved: 31 heroes counted with level and stars; one detail read
    resources_gained: none (observe-only)
    points: 0
    costs: model 0.176318 USD; nothing spent
    verified: yes
    run_id: 20261123T130013Z-a04ef8
    run_steps: 12
    actions_done: 22
    actions_refused: 0
    model_s_per_step: 7.0
    cost_usd: 0.176318
    device_takeovers: 0
    rules_used: R1,R6
    rule_failed: none
    rule_gap: Hero cards show no name or power; the Tier tab note points to the Wall of Honor.
  stats_missing: []
  stats_warnings: []
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
