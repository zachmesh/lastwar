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
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
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
