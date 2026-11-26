---
unit: scout-midday-base-survey-2026-11-25-001
regular: scout-midday
activity: perception-scout
segment: 2
priority: 2
created_at: 2026-11-25T05:38:41Z
expires_at: 2026-11-27T02:00:00Z
planned_for:
not_before: 2026-11-25T05:48:00Z
window: base survey by the composed pan read only owner instruction 05:37z
est_minutes: 12
serves: snapshot
chain_id: base-survey-2026-11-25
chain_seq: 1
attempts: 1
max_attempts: 2
claimed_by: operator
claimed_at: 2026-11-26T11:43:05Z
lease_until: 2026-11-26T12:03:05Z
result:
  status: done
  started_at: 2026-11-26T11:43:05Z
  finished_at: 2026-11-26T11:46:15Z
  duration_seconds: 190
  executor: operator
  summary: Base survey: start point (330,640) on blank road ground (margin about 80 px); four composed pans (about 170 px: left, right, up, down) each followed by WORLD then BASE, none refused or flung; the base mapped (HQ (570,380) at home, Alliance shield (670,705)) with the standard frame's tents, bubbles and HUD plus the areas beyond it (golden monuments and a ferris wheel on the left; blue-roof houses, a glass-dome library, an aircraft field and five question-mark bubbles on the right; a parking area with pads 2 and 3 above; a gold pyramid, statue rows and copper domes below); the tram icon bare before and after; nothing tapped but WORLD and BASE; drags 4. state_change: no. state_read: base survey ran: four pans mapped the base; tram icon bare before and after; start point (330,640) | step 8 | 11:44:58Z
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/perception-scout/1143-queue-run.md and 1143-queue-run.csv; run 20261126T114305Z-cc94b0
  state_read: base survey ran: four pans mapped the base; tram icon bare before and after; start point (330,640) | step 8 | 11:44:58Z
  state_change: no
  follow_up: the question-mark bubbles with figures on the right of the base are unread (read only)
  stats:
    target: map the base by four pans
    achieved: survey ran
    resources_gained: none
    points: 0
    costs: none spent; model 0.225428 USD
    verified: yes
    run_id: 20261126T114305Z-cc94b0
    run_steps: 10
    actions_done: 12
    actions_refused: 0
    cost_usd: 0.225428
    device_takeovers: 0
    claims: 0
    pans: 4
    start_point: 330,640
    margin_px: 80
    tram_badge: bare before and after
    drags_tried: 4
    rules_used: 1,2
  stats_missing: []
  stats_warnings: []
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
