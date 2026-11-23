---
unit: scout-midday-growth-snapshot-2026-11-23-024
regular: scout-midday
activity: perception-scout
segment: 2
priority: 1
created_at: 2026-11-23T10:41:22Z
expires_at: 2026-11-23T11:30:00Z
planned_for:
not_before: 2026-11-23T10:41:00Z
window: F1b drill ground re-read both grounds read only never press Upgrade
est_minutes: 10
serves: baseline Drill Ground
chain_id: growth-snapshot-2026-11-23
chain_seq: 24
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T10:47:31Z
lease_until: 2026-11-23T11:07:31Z
result:
  status: done
  started_at: 2026-11-23T10:47:31Z
  finished_at: 2026-11-23T10:53:19Z
  duration_seconds: 348
  executor: operator
  summary: Drill Ground re-read F1b, runs 20261123T104804Z-ddd02d (a Tavern Lv.20 tapped, nothing pressed) and 20261123T105007Z-a1ecef (claude-gateway/claude-sonnet-5-5, 13 steps): FOUR Drill Grounds read as parade fields: Lv.26, Lv.28, Lv.30, Lv.27; the Lv.28 ground exists (about 580,800 in the fresh frame). Lv.28 Building Details: Unit Count +9211, four officer slots filled. Upgrade preview Lv.28 to 29: Unit Count +7,600 to +7,800, power 165,800 to 196,200 (+30,400), coin 14.4M of 119.0M (short), iron 1.0G of 144.5M (met), Lv.29 Headquarters (met), original 39d 01:53:19, effective 18d 09:21:34. Nothing pressed (Upgrade, Finish Now, Obtain untouched).
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/growth/1047-f1b-drill-ground.md and 1047-f1b-drill-ground.csv; runs 20261123T104804Z-ddd02d and 20261123T105007Z-a1ecef
  follow_up: details and preview of the Lv.26, Lv.27 and Lv.30 grounds not opened; the Lv.28 to 29 upgrade needs 104.6M more coin and a builder (free 2026-11-24T09:20Z)
  stats:
    target: read each Drill Ground tag, Building Details and Upgrade preview, report whether any reads Lv.28
    achieved: four tags read; Lv.28 Details and preview read; Lv.26, 27 and 30 not opened
    resources_gained: none (observe-only)
    points: 0
    costs: model 0.251264 USD in two runs; nothing spent
    verified: yes
    run_id: 20261123T105007Z-a1ecef
    run_steps: 19
    actions_done: 34
    actions_refused: 0
    model_s_per_step: 6.6
    cost_usd: 0.251264
    device_takeovers: 0
    rules_used: R1,R6
    rule_failed: none
    rule_gap: Drill Grounds are parade fields tapped on a soldier, not buildings; the digest and base map assumed buildings.
  stats_missing: []
  stats_warnings: []
---

# scout-midday

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: baseline Drill Ground

## Brief (planner, F1b Drill Ground re-read, coordinator instruction, read-only)

serves: baseline Drill Ground

Source: operator record `_records_/2026-11-22/growth/1030-base-map.md`. The base map shows TWO Drill Grounds, both off-screen right of the fresh base frame, so one pan (one drag) is needed: Lv.30 (orange, about (740,880)) and Lv.27 (purple crystal, about (855,790)). The earlier reads of a Drill Ground Lv.28 (Unit Count +9,211; Lv.28 to 29 at 119.0M coin, 18d 09h) cannot be attributed: the Lv.28 building at (260,545) is the Farmland. Yet those preview numbers match the guide's Drill Ground Lv.28 to 29 row exactly (power +30,400), not the Farmland's. Read each tag carefully and report whether any ground reads Lv.28.

For EACH Drill Ground: read the tag (name and level); open Building Details with the paw button, read only, and record Level, Unit Count (+N) and the officer slots; then open the Upgrade PREVIEW with the green arrow and record the cost in coin and iron (and food if shown), original and effective time, the Unit Count change, and the prerequisite lines with check marks. NEVER tap Upgrade, Finish Now, Speed Up or Obtain; press nothing else; close panels with their X.

HAZARD: close a radial menu with an empty-ground tap such as (200,610). NEVER tap the WORLD button at (660,940) while a menu is open low on the screen: the green Upgrade arrow can sit there. Restore the fresh frame with WORLD then BASE only after every menu is closed.

At most two runs, 10 minutes. Write what each building reads, with the frame time. Rules and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md` (K or M numbers only: write 1.1G as 1100M). Do not enqueue a chain successor.
Cost cap, stated: 0.60 USD (the harness stops near 0.36 of it).
