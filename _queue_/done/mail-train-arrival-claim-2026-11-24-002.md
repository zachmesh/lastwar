---
unit: mail-train-arrival-claim-2026-11-24-002
regular: mail
activity: mail-rewards
segment: 2
priority: 2
created_at: 2026-11-24T15:48:42Z
expires_at: 2026-11-24T17:15:00Z
planned_for:
not_before: 2026-11-24T15:48:00Z
window: claim the train arrival reward mail once retry after the alert
est_minutes: 4
serves: upkeep
chain_id: train-arrival-claim-2026-11-24
chain_seq: 2
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T15:57:41Z
lease_until: 2026-11-24T16:17:41Z
result:
  status: done
  started_at: 2026-11-24T15:57:41Z
  finished_at: 2026-11-24T15:59:56Z
  duration_seconds: 135
  executor: operator
  summary: The Event mail 'Train arrival reward!' claimed once by its own Claim: two orange medal items (2.5K labels), blue chests x100 and a green triangle item 2.5K (HUD unchanged; no chest opened); Claim All and Delete All not pressed; tram badge none; drags 0
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/mail-rewards/1557-queue-run.md and 1557-queue-run.csv; run 20261124T155742Z-1e6311
  follow_up: the blue chests x100 (two of 50) wait in the stock unopened
  stats:
    target: claim the Train arrival reward mail once
    achieved: claimed once
    resources_gained: two orange medal items; blue chests x100; a green triangle item 2.5K
    points: 0
    costs: none spent; model 0.198192 USD
    verified: yes
    run_id: 20261124T155742Z-1e6311
    run_steps: 15
    actions_done: 14
    actions_refused: 0
    cost_usd: 0.198192
    device_takeovers: 0
    claims: 1
    tram_badge: none
    drags_tried: 0
    rules_used: 1,3,5
  stats_missing: []
  stats_warnings: []
---

# mail

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: upkeep

## Brief (definition pointer, from the roster)

This unit is the regular `mail`: Mail - check every category and Claim All. Its definition is the activity folder `_activities_/mail-rewards/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, THE TRAIN ARRIVAL REWARD MAIL, retry after the macOS alert of 15:36Z: one plain claim, WAITING FOR STEER A)

serves: upkeep

Steer A approved this unit 15:32Z (a plain mail claim under the mail rule).
Record `_records_/2026-11-22/mail-rewards/1521-queue-run.md`: the Event mail list holds a 'TRAIN ARRIVAL REWARD!' mail with a GREEN Claim and five attachments (two 2.5K items and two 50-count chests): the alliance train's arrival reward for our boarding of 09:57Z. The digest: claiming reward attachments is in scope; Delete All is never pressed. 5 steps:
(1) Open Mail; take the Event category; the TIPS 'Enable notifications' dialog if it shows: a frame, identify Cancel by its text, one tap, never Enable Now.
(2) Open that mail; READ in a frame BEFORE any tap each attachment's name and quantity.
(3) Tap that mail's green Claim ONCE (not 'Claim All'); read what it paid (items, quantities) and the HUD deltas. The two 50-count chests are NOT opened: they join the stock.
(4) Never a diamond or price line; any app or dialog that is not the TIPS 'Enable notifications' (Cancel only): touch nothing, take the frame, STOP, tell the Coordinator. Delete All is never pressed.
Verify each HUD icon by its label or glyph before the tap. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.30 USD.
