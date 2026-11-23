---
unit: scout-midday-growth-snapshot-2026-11-23-007
regular: scout-midday
activity: perception-scout
segment: 2
priority: 2
created_at: 2026-11-23T07:49:05Z
expires_at: 2026-11-23T13:30:00Z
planned_for:
not_before: 2026-11-23T09:05:00Z
window: growth snapshot F2 read only never press Upgrade
est_minutes: 10
serves: snapshot (Story 868)
chain_id: growth-snapshot-2026-11-23
chain_seq: 7
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T11:33:03Z
lease_until: 2026-11-23T11:53:03Z
result:
  status: partial
  started_at: 2026-11-23T11:33:03Z
  finished_at: 2026-11-23T11:36:56Z
  duration_seconds: 233
  executor: operator
  summary: F2 read, runs 20261123T113319Z-ae13e7 and 20261123T113521Z-4cff3b (claude-gateway/claude-sonnet-5-5, 13 steps; claimed 11:33:03Z; token released 11:36:22Z before the 11:40Z hard stop): Barracks Lv.24 Building Details (Training Count +666, four Instructor slots) and Upgrade preview Lv.24 to 25 (Unit Training Cap 510 to 520, Power 101,100 to 120,600, coin 14.4M of 49.3M short, iron 1.0G of 119.0M met, HQ Lv.25 met, original 16d 10:22:49, effective 7d 17:35:27, Finish Now 78,498 diamonds not pressed); the Tech Center was not located. Read-only, nothing pressed beyond Details, the green arrow and X.
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/perception-scout/1132-f2-barracks.md and _records_/2026-11-22/growth/1132-f2-barracks.csv; runs 20261123T113319Z-ae13e7 and 20261123T113521Z-4cff3b
  follow_up: locate the Tech Center and read its preview; the barracks upgrade is 49.3M coin (34.9M short) and needs a builder (2026-11-24T09:20Z)
  stats:
    target: read the lowest barracks and the Tech Center upgrade previews
    achieved: Barracks Lv.24 Details and preview read; Tech Center not located
    resources_gained: none (observe-only)
    points: 0
    costs: model 0.200594 USD; nothing spent
    verified: yes
    blocker_category: c
    run_id: 20261123T113521Z-4cff3b
    run_steps: 13
    actions_done: 20
    actions_refused: 0
    model_s_per_step: 6.0
    cost_usd: 0.200594
    device_takeovers: 0
    rules_used: R1,R6
    rule_failed: none
    rule_gap: A second tap on a tent after a camera shift can select another building; read the preview from the first tap.
  stats_missing: []
  stats_warnings: []
---

# scout-midday

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

## Brief (planner, growth snapshot F2, Story 868, from the scout protocol)

serves: snapshot (Story 868)

Read-only unit F2, order 7. Question: What do the lowest barracks and the Tech Center upgrades cost, take and add?

Route: As F1 on the Lv.24 barracks (button row has a green arrow) and the Tech Center.

Read: As F1; for the barracks also the next tier named; for the Tech Center the Special Forces line if any.

Budget: at most 8 steps and 10 minutes. Notes: Same stops as F1. The planner may swap the target after P1 to T2 if a better candidate shows.

Rules: stop rules R1 to R7 in `_records_/2026-11-22/perception-scout/2345-snapshot-protocol.md`; red lines and the snap command in `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`. Snap takes only K or M numbers: write 1.1G as 1100M. Do not enqueue a chain successor.

Tag text: beside every number from a building panel write its tag text (name and level above the building after the tap; `_records_/2026-11-22/coach/0255-tag-text-check.md`); none means [G]. Add a tag_text column.
Cost cap, stated: 0.60 USD (the harness stops near 0.36 of it).
