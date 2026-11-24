---
unit: secrets-refugee-claim-2026-11-24-001
regular: secrets
activity: secret-missions
segment: 2
priority: 2
created_at: 2026-11-24T03:38:42Z
expires_at: 2026-11-24T06:36:00Z
planned_for:
not_before: 2026-11-24T04:36:00Z
window: claim the refugee tasks and redeploy
est_minutes: 8
serves: PL-17
chain_id: refugee-claim-2026-11-24
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T04:38:13Z
lease_until: 2026-11-24T04:58:13Z
result:
  status: partial
  started_at: 2026-11-24T04:38:13Z
  finished_at: 2026-11-24T04:40:00Z
  duration_seconds: 107
  executor: operator
  summary: One Claim tap claimed the four finished SSR refugee tasks (Hero EXP 13.6M, Upgrade Ore 720, Skill Medal 2.1K and more); Mega Deploy opened no popup (nothing to deploy), so no new timers; UR Rescue Missing Agent claim about 05:36:07Z and UR Oil Depot about 07:35:46Z; the TIPS dialog was cancelled once first
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/secret-missions/0438-queue-run.md and 0438-queue-run.csv; run 20261124T043814Z-d5c254
  follow_up: claim the UR Rescue Missing Agent about 05:36:07Z and the UR Oil Depot about 07:35:46Z; the next card pair after the 4-hour start
  stats:
    target: claim the refugee tasks with the in-game Claim, then Mega Deploy, write the new timers
    achieved: claimed; nothing to deploy
    resources_gained: none
    points: 0
    costs: none spent; model 0.115749 USD
    verified: yes
    run_id: 20261124T043814Z-d5c254
    run_steps: 9
    actions_done: 8
    actions_refused: 0
    cost_usd: 0.115749
    device_takeovers: 0
    claim_utc: 04:38:36.403
    blocker_category: f missing precondition (nothing to deploy after the claim: Mega Deploy greyed)
    rules_used: 1
  stats_missing: []
  stats_warnings: []
---

# secrets

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: PL-17

## Brief (definition pointer, from the roster)

This unit is the regular `secrets`: Secret missions - claim finished (one Claim takes all), Mega Deploy the rest (UR Only off; on duel UR days Mega Refresh first), check Reward Recovery. Its definition is the activity folder `_activities_/secret-missions/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, CLAIM the refugee tasks and re-deploy, PL-17)

serves: PL-17

The refugee tasks come due about 04:35Z (the operator's times from the secrets read, record `secret-missions/0334`). Verify the title SECRET COMMAND POST before any tap. Read each card's timer to the second with the UTC time. Claim ONLY with the in-game Claim button (one tap claims all finished tasks); if a task is not finished, claim nothing and write the time left. Then re-deploy with Mega Deploy (its toast 'no tasks available for dispatch' means nothing is pending). Write each card, the reward with counts, the new timers and the UTC time of the claim, so the next claim time is known. No diamond or item spend, no Mega Refresh, and Plunder Others is PvP: never tapped. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if one opens, STOP and touch nothing. Safe tap: the bare spot (310,660), not (400,640) after a camera shift (WORLD then BASE first).
Cost cap, stated: 0.40 USD.
