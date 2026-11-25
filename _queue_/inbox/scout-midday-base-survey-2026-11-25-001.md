---
unit: scout-midday-base-survey-2026-11-25-001
regular: scout-midday
activity: perception-scout
segment: 2
priority: 2
created_at: 2026-11-25T05:38:41Z
expires_at: 2026-11-25T17:30:00Z
planned_for:
not_before: 2026-11-25T05:48:00Z
window: base survey by the composed pan read only owner instruction 05:37z
est_minutes: 12
serves: snapshot
chain_id: base-survey-2026-11-25
chain_seq: 1
attempts: 0
max_attempts: 2
claimed_by:
claimed_at:
lease_until:
---

# scout-midday

Serves: snapshot

## Brief (definition pointer, from the roster)

This unit is the regular `scout-midday`: Scout - midday perception pass (floor anchor); re-walk the interface for state-dependent availability (trains, phase rotations, market refreshes); full passes also fire on detected state change between anchors. Its definition is the activity folder `_activities_/perception-scout/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, THE BASE SURVEY, read only, owner instruction OD-20261125-05 and Steer A 05:37Z, PL none)

serves: snapshot

The owner asked us to scroll the screen to see all areas: this maps the base. NOTHING IS TAPPED except the WORLD and BASE corner button; no building, bubble, icon, banner or the avatar.
(1) FIRST frame: the standard base frame. Find a BLANK GROUND START POINT: at least 60 px from any building, bubble, icon or HUD element; write its coordinates. This is a NEW PAGE: name the margin and start point BEFORE the first pan.
(2) THE PAN, ONE message: mouse_move to the start point; left_mouse_down; wait 1 s; ONE move of about 175 px; wait 1 s; left_mouse_up; the screenshot after. AT MOST EIGHT PANS: left, right, up, down, each followed by its return pan or by WORLD then BASE (one tap each). A pan that FLINGS (the view jumps) or moves nothing: STOP and report.
(3) Save a frame at the start point and at EACH pan's end; for every frame write the camera offset from a landmark (the HQ or the Alliance shield) so the frames assemble into one base map, the buildings, bubbles, icons and labels with positions, and any object not in the standard base frame.
(4) End with WORLD then BASE and a frame check.
Cost cap, stated: 0.80 USD.
CLOSE by `_records_/2026-11-22/queue-planning/3170-closing-rule-done-and-partial.md`: DONE if the survey ran, with ONE `state_read:` line; `--state-change no`.
FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Verify each HUD icon by its label first.
