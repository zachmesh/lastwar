---
unit: training-room-collect-2026-11-26-001
regular: training
activity: troop-training
segment: 2
priority: 2
created_at: 2026-11-24T03:59:34Z
expires_at: 2026-11-26T14:00:00Z
planned_for:
not_before: 2026-11-26T11:05:00Z
window: room read and collect of finished batches after the lv 26 ground completes
est_minutes: 12
serves: PL-09
chain_id: room-collect-2026-11-26
chain_seq: 1
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
---

# training

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: PL-09

## Brief (definition pointer, from the roster)

This unit is the regular `training`: Troop training - requeue any finished barracks at its highest tier. Its definition is the activity folder `_activities_/troop-training/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, ROOM READ AND COLLECT after the Lv.26 ground completes, PL-09)

serves: PL-09

DISPATCH ONLY WHEN NAMED, at about 11:09Z on 2026-11-26: the Lv.26 ground ends 2026-11-26T11:08:36.6Z (record building-queues/1606; it read 21:10:37Z before the construction speed factor rose to 2.325). FIRST read the ground's timer: more than 5 minutes left: RELEASE this unit unrun. +200 room, +21,600 power.

1. A finished ground completes by TAPPING THE WRAPPED GIFT BOX on it (no Complete button): if the Lv.26 ground shows one, tap it ONCE; write Total Power before and after.
2. THE PARTIAL COLLECT TEST (Coach's evidence 1215; Steer A 15:08Z). FIRST read 'Unit Count X of Y' (the free room). Write the READY BUBBLE AND ITS DIGITS beside each tent, cropped from the SAVED frame at 6x, never a zoom action (expected: Lv.24 about 249, Lv.30 about 793, Lv.20 probably a finished batch, Lv.27 none). Highest power per troop first: press the Lv.30 pistol ONCE, then the Lv.24 pistol ONCE whatever Lv.30 did, then Lv.20 ONLY IF room remains; each press with 'Unit Count X of Y' before and after. Registered: (A) ramp: Lv.30 collects 200 T10 (+329,400), Lv.24 refused 'Drill Ground Full'; (B) both refused; (C) Lv.30 refused, Lv.24 collects 200 (+212,600). Record each toast EXACTLY and Total Power before and after. An empty barracks (Lv.27) opens its Train Units panel with no toast: close it.
3. Never Train, Heal, Collect at the Hospital, speed up or buy. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.50 USD.
