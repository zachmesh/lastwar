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
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T11:01:29Z
lease_until: 2026-11-23T11:21:29Z
result:
  status: partial
  started_at: 2026-11-23T11:01:29Z
  finished_at: 2026-11-23T11:05:59Z
  duration_seconds: 270
  executor: operator
  summary: B1 read, run 20261123T110221Z-eec05f (claude-gateway/claude-sonnet-5-5, max-steps 14, 14 steps, claimed 11:01:29Z inside the 11:02Z window): Headquarters Lv.30 read (tag Headquarters Lv.30; Building Details has no power line, two hero entries); Tech Center and Builders Hut NOT found among eight buildings tapped; tag index: Emergency Center Lv.20, Gear Factory Lv.20, Food Warehouse Lv.24, Component Factory Lv.20 (two), Training Base Lv.26, Ginkgo Tree Lv.1; the red and white building opens the store. Read-only, nothing pressed beyond Details, HUD unchanged.
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/perception-scout/1101-b1-hq-tech-hut.md and _records_/2026-11-22/growth/1101-b1-hq-tech-hut.csv; run 20261123T110221Z-eec05f
  follow_up: find the Tech Center and the Builders Hut (try the right-hand buildings near the clock tower and beyond the left edge after a pan); read the Builders Hut Details (builder count, banked speed-up time); a 116min bubble appeared at the lower left
  stats:
    target: read HQ, Tech Center and Builders Hut levels and the hut bank
    achieved: HQ Lv.30 and Details read; Tech Center and Builders Hut not found; seven other building tags read
    resources_gained: none (observe-only)
    points: 0
    costs: model 0.217060 USD; nothing spent
    verified: yes
    blocker_category: c
    run_id: 20261123T110221Z-eec05f
    run_steps: 14
    actions_done: 44
    actions_refused: 0
    model_s_per_step: 8.0
    cost_usd: 0.217060
    device_takeovers: 0
    rules_used: R1,R6
    rule_failed: none
    rule_gap: No base building index exists; Tech Center and Builders Hut positions unknown, so tag-by-tag search costs about 14 turns.
  stats_missing: []
  stats_warnings: []
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

Tag text: beside every number from a building panel write its tag text (name and level above the building after the tap; `_records_/2026-11-22/coach/0255-tag-text-check.md`); none means [G]. Add a tag_text column.
Cost cap, stated: 0.60 USD (the harness stops near 0.36 of it).
