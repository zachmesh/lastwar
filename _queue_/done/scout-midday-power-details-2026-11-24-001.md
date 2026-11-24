---
unit: scout-midday-power-details-2026-11-24-001
regular: scout-midday
activity: perception-scout
segment: 2
priority: 1
created_at: 2026-11-24T17:52:07Z
expires_at: 2026-11-24T20:00:00Z
planned_for:
not_before: 2026-11-24T17:52:00Z
window: read only total power by category and the construction and research speed sources steer a 17:50z
est_minutes: 6
serves: snapshot
chain_id: power-details-2026-11-24
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T17:55:21Z
lease_until: 2026-11-24T18:15:21Z
result:
  status: done
  started_at: 2026-11-24T17:55:21Z
  finished_at: 2026-11-24T17:58:58Z
  duration_seconds: 217
  executor: operator
  summary: Total Power breakdown read: Hero 66,391,681, Drone 5,842,475, Building 9,823,925 (Buildings 6,687,800 and Survivor 3,136,125), Unit 63,137,934, Tech 4,907,277, summing to the HUD 150,103,292; against 03:32Z Building is +47,500 (the ~46,000), Hero +1,032, Unit +291,262, Tech +7,800; speed sources not reached; only the figure, two chevrons and the X pressed; tram badge none. state_change: no. state_read: Power Details Hero 66,391,681; Drone 5,842,475; Building 9,823,925; Unit 63,137,934; Tech 4,907,277; sum equals HUD 150,103,292 | step 6 | 17:57:03Z
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/perception-scout/1555-queue-run.md and 1555-queue-run.csv; run 20261124T175624Z-39de6b
  state_read: Power Details Hero 66,391,681; Drone 5,842,475; Building 9,823,925; Unit 63,137,934; Tech 4,907,277; sum equals HUD 150,103,292 | step 6 | 17:57:03Z
  state_change: no
  follow_up: a category read at the next quiet moment would split the +51,432 since 16:09Z; Unit and Tech have no sub-lines
  stats:
    target: read the Total Power breakdown by category
    achieved: five categories read, sum equals the HUD
    resources_gained: none
    points: 0
    costs: none spent; model 0.181152 USD
    verified: yes
    run_id: 20261124T175624Z-39de6b
    run_steps: 14
    actions_done: 18
    actions_refused: 0
    cost_usd: 0.181152
    device_takeovers: 0
    total_power: 150103292
    tram_badge: none
    drags_tried: 0
    rules_used: 1
  stats_missing: []
  stats_warnings: []
---

# scout-midday

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: snapshot

## Brief (definition pointer, from the roster)

This unit is the regular `scout-midday`: Scout - midday perception pass (floor anchor); re-walk the interface for state-dependent availability (trains, phase rotations, market refreshes); full passes also fire on detected state change between anchors. Its definition is the activity folder `_activities_/perception-scout/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, TOTAL POWER BY CATEGORY and the SPEED SOURCES, read only, Steer A 17:50Z)

serves: snapshot

Baseline: the Power Details of 03:32Z (record `_records_/2026-11-22/perception-scout/0330-queue-run.md`: Hero 66,390,649, Drone 5,842,475, Building 9,776,425, Unit 62,846,672, Tech 4,899,477, sum 149,755,698; the 2344 record has every line). It pressed only the HUD Total Power figure, a chevron and the X. THE QUESTION: which category holds about 46,000 unattributed power since 15:56Z, and where the construction speed (factor 2.325) comes from. 6 steps:
(1) The base screen: a frame; write the HUD Total Power and the UTC time.
(2) Tap the HUD Total Power FIGURE (verify it by label in a frame): Power Details opens. Expand each category's chevron ONCE (Hero, Unit, Building, Drone, Tech); read every line, name and number, cropping digits from the SAVED frame at 6x; write the sum against the HUD total.
(3) SPEED SOURCES, only if a panel that lists a construction or research speed by source (VIP, alliance technology, decorations, skills) is reachable by AT MOST TWO plain label taps from here: read each speed line with its source and figure. Press nothing that upgrades, buys, activates, extends, uses or changes anything; no Use, Buy, Extend or Upgrade button. If no such panel is reachable: write 'not reached'.
(4) Close with the X or the back arrow. Any dialog, price line or other app: STOP, touch nothing. Complete with `--state-change no`. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.60 USD.
