---
unit: training-room-collect-2026-11-25-001
regular: training
activity: troop-training
segment: 2
priority: 2
created_at: 2026-11-25T00:24:18Z
expires_at: 2026-11-27T02:00:00Z
planned_for:
not_before: 2026-11-25T13:35:00Z
window: room read and collect of finished batches after the lv 26 ground completes 11-25
est_minutes: 12
serves: PL-09
chain_id: room-collect-2026-11-25
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-26T08:52:13Z
lease_until: 2026-11-26T09:12:13Z
result:
  status: done
  started_at: 2026-11-26T08:52:13Z
  finished_at: 2026-11-26T08:55:47Z
  duration_seconds: 214
  executor: operator
  summary: Partial collect test: no wrapped gift box showing; the Lv.30 and Lv.24 barracks pistols each pressed once and both refused with 'Drill Ground Full: Unable to add more units.' (outcome B); Lv.20 not pressed (no room); ready bubbles about 793, 248 and 310 (6x crop, low confidence); no Unit Count X of Y line on the tags; Total Power 151,680,155 before and after; nothing collected or trained; drags 0. state_change: no. state_read: Lv.30 and Lv.24 barracks pistols both refused: 'Drill Ground Full: Unable to add more units.'; Total Power unchanged | step 7 | 08:54:46Z
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/troop-training/0852-queue-run.md and 0852-queue-run.csv; run 20261126T085213Z-cfe852
  state_read: Lv.30 and Lv.24 barracks pistols both refused: 'Drill Ground Full: Unable to add more units.'; Total Power unchanged | step 7 | 08:54:46Z
  state_change: no
  follow_up: the finished batches (about 793, 248, 310) stay waiting: the Drill Ground capacity is full
  stats:
    target: the partial collect test: Lv.30 then Lv.24 pistols
    achieved: outcome B: both refused
    resources_gained: none
    points: 0
    costs: none spent; model 0.254083 USD
    verified: yes
    run_id: 20261126T085213Z-cfe852
    run_steps: 21
    actions_done: 10
    actions_refused: 0
    cost_usd: 0.254083
    device_takeovers: 0
    claims: 0
    outcome: B both refused
    power: 151680155
    tram_badge: bare
    drags_tried: 0
    rules_used: 1,2
  stats_missing: []
  stats_warnings: []
---

# training

Serves: PL-09

## Brief (definition pointer, from the roster)

This unit is the regular `training`: Troop training - requeue any finished barracks at its highest tier. Its definition is the activity folder `_activities_/troop-training/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, ROOM READ AND COLLECT after the Lv.26 ground completes, PL-09)

serves: PL-09

DISPATCH ONLY WHEN NAMED. The Lv.26 ground ended 2026-11-25T13:38:36Z and the phone continued it (Lv.27, days left): do NOT release for its timer.

1. A finished ground completes by TAPPING THE WRAPPED GIFT BOX on it (no Complete button): if one still shows, tap it ONCE; none shows: the phone took it.
2. THE PARTIAL COLLECT TEST. FIRST read 'Unit Count X of Y' (the free room). Write the READY BUBBLE AND ITS DIGITS beside each tent, cropped from the SAVED frame at 6x, never a zoom action. Highest power per troop first: press the Lv.30 pistol ONCE, then the Lv.24 pistol ONCE whatever Lv.30 did, then Lv.20 ONLY IF room remains; each press with 'Unit Count X of Y' before and after. Registered: (A) ramp: Lv.30 collects 200 T10 (+329,400), Lv.24 refused 'Drill Ground Full'; (B) both refused; (C) Lv.30 refused, Lv.24 collects 200 (+212,600). Record each toast EXACTLY and Total Power before and after. An empty barracks (Lv.27) opens its Train Units panel with no toast: close it.
3. Never Train, Heal, Collect at the Hospital, speed up or buy. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
CLOSE by `_records_/2026-11-22/queue-planning/3170-closing-rule-done-and-partial.md`: DONE for a taken action or a verified nothing-to-do (`--state-change no`, a `state_read:` line); else PARTIAL.
BUTTON ROW: the buttons under a tent are small: verify the pistol glyph in a frame before each tap (a stray tap once opened Building Details, another the world map): back arrow or X, and write it; never the green up arrow (the upgrade shortcut).
FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
Cost cap, stated: 0.50 USD.
