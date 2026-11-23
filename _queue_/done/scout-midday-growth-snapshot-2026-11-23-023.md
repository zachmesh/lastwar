---
unit: scout-midday-growth-snapshot-2026-11-23-023
regular: scout-midday
activity: perception-scout
segment: 2
priority: 2
created_at: 2026-11-23T09:39:55Z
expires_at: 2026-11-23T10:20:00Z
planned_for:
not_before: 2026-11-23T09:40:00Z
window: growth snapshot D1 re-minted after the first window expired read only
est_minutes: 10
serves: snapshot (Story 868)
chain_id: growth-snapshot-2026-11-23
chain_seq: 23
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T10:17:25Z
lease_until: 2026-11-23T10:37:25Z
result:
  status: partial
  started_at: 2026-11-23T10:17:25Z
  finished_at: 2026-11-23T10:20:24Z
  duration_seconds: 179
  executor: operator
  summary: Drone and Wall of Honor read D1, run 20261123T101753Z-e9a1c6 (claude-gateway/claude-sonnet-5-5, max-steps 12, 10 steps): base framing restored via WORLD then BASE; Drone Center Lv.1; Tactical Drone Lv.134, level bar 0/1,681,200, drone screen power 5,840,675, Health +2,671,634, Attack +60,910, Defense +11,182, one 5-star skill, resource line 2.88M/93.40K (label unread), Data Training button not pressed; Drone Parts, skill chip stock, Combat Boost tier and next-level cost unread; Wall of Honor not found. Read-only, nothing spent.
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/perception-scout/1017-d1-drone-wall.md and _records_/2026-11-22/growth/1017-d1-drone-wall.csv; run 20261123T101753Z-e9a1c6
  follow_up: D1b: open the Component, Combat Boost and Skill Chip tabs and read the data icon label; find the Wall of Honor tab in a Tank, Aircraft or Missile Center; the train shortcut leaves the camera panned, restore with WORLD then BASE
  stats:
    target: read the Drone Center, drone stocks and Wall of Honor entries and next-step costs
    achieved: Drone Center level, drone level, power and attributes read; stocks by tab, costs and Wall of Honor not read
    resources_gained: none (observe-only)
    points: 0
    costs: model 0.146503 USD; nothing spent
    verified: yes
    blocker_category: c
    run_id: 20261123T101753Z-e9a1c6
    run_steps: 10
    actions_done: 18
    actions_refused: 0
    model_s_per_step: 6.9
    cost_usd: 0.146503
    device_takeovers: 0
    rules_used: R1,R6,R9
    rule_failed: none
    rule_gap: No rule restores a panned base camera; the train shortcut leaves it panned, WORLD then BASE fixed it.
  stats_missing: []
  stats_warnings: []
---

# scout-midday

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: snapshot (Story 868)

## Brief (planner, growth snapshot D1 re-minted, Story 868, from the scout's unit table)

serves: snapshot (Story 868)

Read-only unit D1. The first D1 window (09:05Z to 09:27Z) expired unrun; this one replaces it. Queue placement: after the routine claims, ahead of D1b and the later reads.

Question: What are the drone level and stocks and the Wall of Honor entries, and what do their next steps cost?

Route: Drone Center: tap its body, the plane icon in the radial menu opens the drone screen; read; back. Wall of Honor: the orange medal icon on the base screen, or the Wall of Honor tab inside a Tank, Aircraft or Missile Center, whichever opens; read; back.

Read: Drone Center level, drone level, Drone Parts and Battle Data stock, skill chip stock, Combat Boost tier, next-level cost and power gain if shown; per Wall of Honor entry the hero, level, next shard cost and bonus line; total Wall of Honor power if shown.

Budget: at most 8 steps and 10 minutes. Notes: Output _records_/<date>/growth/<HHMM>-d1-drone-wall.csv, schema g_drone_wall. Power Details on 2026-11-22 reads Drone Level 3,492,600, Drone Component 1,639,876, Skill Chip 708,200, Wall of Honor 127,100; Component and Chip have not moved since 2026-11-08. The Drone Center read Lv.1 once (label, unverified). A tap on the HUD rail Events point selected the Drone Center, so ground fresh. Never press Upgrade, Level Up, Invest or any shard control; one tap there may spend.

Rules: stop rules R1 to R7 in `_records_/2026-11-22/perception-scout/2345-snapshot-protocol.md`; red lines and the snap command in `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`. Snap takes only K or M numbers: write 1.1G as 1100M. Do not enqueue a chain successor.
Cost cap, stated: 0.60 USD (the harness stops near 0.36 of it).
