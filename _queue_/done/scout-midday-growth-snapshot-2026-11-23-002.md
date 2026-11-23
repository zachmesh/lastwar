---
unit: scout-midday-growth-snapshot-2026-11-23-002
regular: scout-midday
activity: perception-scout
segment: 2
priority: 2
created_at: 2026-11-23T07:48:56Z
expires_at: 2026-11-23T08:44:00Z
planned_for:
not_before: 2026-11-23T08:00:00Z
window: growth snapshot T2 read only never press Upgrade
est_minutes: 10
chain_id: growth-snapshot-2026-11-23
chain_seq: 2
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T08:25:45Z
lease_until: 2026-11-23T08:45:45Z
result:
  status: partial
  started_at: 2026-11-23T08:25:45Z
  finished_at: 2026-11-23T08:27:43Z
  duration_seconds: 118
  executor: operator
  summary: Run 20261123T082546Z-831319 (claude-gateway/claude-sonnet-5-5, max-steps 8, completed in 7 steps), read-only. Hospital menu closed with one empty-ground tap; HUD unchanged (food 638.0M, iron 1.0G, coin 9.6M, diamonds 11,136, Total Power 150,211,809). The first tent tapped (upper right) read Barracks Lv.20, so two turns were spent re-picking; the next tent (lower right, no clock bubble) read Barracks Lv.24 and its pistol gave the toast Drill Ground Full: Unable to add more units. with no panel. The red formation read Drill Ground Lv.28. Building Details of the Lv.24 barracks and the Drill Ground were not reached (out of turns); the 07:48Z Drill Ground read stands (Unit Count +9211, four Officers, no next-level text). Nothing pressed that trains, collects, upgrades or spends. 7 steps, 12 actions done, 0 refused, 6.9 s model time per step, 0.094026 USD. No takeover. Game on the base with the Drill Ground radial menu open.
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/perception-scout/0025-queue-run.md and sidecar 0025-queue-run-detail.md; run 20261123T082546Z-831319; frame _tools_/state/cu_growth_t2_0025.png
  follow_up: three-step read of the Lv.24 barracks and Drill Ground Building Details would close the unit; Drill Ground Lv.28 Unit Count +9211 stands from 07:48Z
  stats:
    target: read the Lv.24 barracks fields and the Drill Ground level and Unit Count (T2)
    achieved: Lv.24 pistol toast read, Drill Ground Lv.28 tag read; both Building Details panels not reached, Unit Count cited from 07:48Z
    resources_gained: none (observe-only)
    points: 0
    costs: model 0.094026 USD; nothing spent, nothing pressed
    verified: yes
    blocker_category: c
    surfaces_walked: 2
    items_observed: 10
    run_id: 20261123T082546Z-831319
    run_steps: 7
    actions_done: 12
    actions_refused: 0
    model_s_per_step: 6.9
    cost_usd: 0.094026
    device_takeovers: 0
  stats_missing: []
  stats_warnings: []
---

# scout-midday

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

## Brief (planner, growth snapshot T2, Story 868, from the scout protocol)

serves: snapshot (Story 868)

Read-only unit T2, order 2. Question: What does the Lv.24 barracks hold, and what are the Drill Ground level and Unit Count?

Route: Lv.24 barracks as in T1 (5 steps); then the Drill Ground body tap, paw button for Building Details; read; panel X.

Read: Lv.24 fields as T1; Drill Ground level, Unit Count, used over cap if shown, officers.

Budget: at most 8 steps and 10 minutes. Notes: The Drill Ground screen was last read live 2026-11-07 and the full figure 39,460 on 2026-10-31; read both numbers before anything else. Do not tap Quick Dispatch. Fourth barracks Lv.20 and Hospital go to optional O1. Run right after the regular training work so no finished batch is waiting; a Training complete toast ends the unit, log count and power change.

Rules: stop rules R1 to R7 in `_records_/2026-11-22/perception-scout/2345-snapshot-protocol.md`; red lines and the snap command in `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`. Snap takes only K or M numbers: write 1.1G as 1100M. Do not enqueue a chain successor.
