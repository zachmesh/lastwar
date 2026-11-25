---
unit: secrets-refugee-claim-b-2026-11-25-001
regular: secrets
activity: secret-missions
segment: 2
priority: 9
created_at: 2026-11-25T03:16:34Z
expires_at: 2026-11-25T06:02:38Z
planned_for:
not_before: 2026-11-25T04:46:00Z
window: fallback refugee claim and re-deploy
est_minutes: 6
serves: PL-17
chain_id: refugee-claim-b-2026-11-25
chain_seq: 1
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
result:
  status: expired
  started_at:
  finished_at: 2026-11-25T06:02:38Z
  duration_seconds: 
  executor:
  summary: retired by the planner: the 04:21Z refugee claim ran (record secret-missions/0421); the fallback is moot
  claimed: []
  claimed_count: 0
  evidence: 
  follow_up: none
  stats:
  stats_missing: [target, achieved, resources_gained, costs, verified]
  stats_warnings: []
---

# secrets

Serves: PL-17

## Brief (definition pointer, from the roster)

This unit is the regular `secrets`: Secret missions - claim finished (one Claim takes all), Mega Deploy the rest (UR Only off; on duel UR days Mega Refresh first), check Reward Recovery. Its definition is the activity folder `_activities_/secret-missions/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, FALLBACK refugee claim, PL-17)

serves: PL-17

DISPATCH ONLY WHEN NAMED: only if the 04:21Z claim unit did not run; else it expires unrun. The SSR PROTECT REFUGEE CAMP Lv.5 task ended 04:12:51Z. Verify the title SECRET COMMAND POST before any tap. Read each card's timer to the second with the UTC time. Claim ONLY with the in-game Claim button (one tap claims every finished task); a task not finished: claim nothing, write the time left. Read the claim POPUP FROM ITS TOP (a frame before any scroll, one after: rows above may be missing); write every row with its count; quote the SECRET TASK REPORT lines (who as shown, when, what: plunder and ally help; the owner's own name never). Then re-deploy with Mega Deploy ('no tasks available for dispatch' = nothing pending); write the new timers and the claim time. No diamond or item spend, no Mega Refresh; Plunder Others is PvP: never tapped. No Backpack or box-count read.
CLOSE by `_records_/2026-11-22/queue-planning/3170-closing-rule-done-and-partial.md`: DONE for a taken claim (state after, in the summary) or a verified nothing-to-do state with a `state_read: <what was read> | <frame> | <HH:MM:SSZ>` line; else PARTIAL; `--state-change yes` if a claim was taken.
FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Safe tap: the bare spot (310,660), not (400,640) after a camera shift (WORLD then BASE first). Verify each HUD icon by its label first.
Cost cap, stated: 0.40 USD.
