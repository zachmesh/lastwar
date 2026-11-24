---
unit: secrets-rescue-claim-2026-11-24-001
regular: secrets
activity: secret-missions
segment: 2
priority: 2
created_at: 2026-11-24T03:38:43Z
expires_at: 2026-11-24T07:20:00Z
planned_for:
not_before: 2026-11-24T05:37:00Z
window: claim the Rescue Missing Agent tasks and redeploy
est_minutes: 8
serves: PL-17
chain_id: rescue-claim-2026-11-24
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T05:38:30Z
lease_until: 2026-11-24T05:58:30Z
result:
  status: partial
  started_at: 2026-11-24T05:38:30Z
  finished_at: 2026-11-24T05:40:02Z
  duration_seconds: 92
  executor: operator
  summary: One Claim tap claimed the finished UR Rescue Missing Agent (Hero EXP 4.1M, Upgrade Ore 800, Resource Chest 300, 5m Research Speed-up x50); Mega Deploy opened no popup so there are no new timers; the Oil Depot ends about 07:35:46Z; drags 0
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/secret-missions/0538-queue-run.md and 0538-queue-run.csv; run 20261124T053831Z-a16ad6
  follow_up: claim the Oil Depot about 07:35:46Z (my window to 07:58Z); the next card pair arrives at the 4-hour start
  stats:
    target: claim the Rescue Missing Agent with the in-game Claim, then Mega Deploy, write the new timers
    achieved: claimed; nothing to deploy
    resources_gained: none
    points: 0
    costs: none spent; model 0.116706 USD
    verified: yes
    run_id: 20261124T053831Z-a16ad6
    run_steps: 9
    actions_done: 11
    actions_refused: 0
    cost_usd: 0.116706
    device_takeovers: 0
    claim_utc: 05:38:52.081
    drags_tried: 0
    drags_cancelled: 0
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

## Brief (planner, CLAIM the Rescue Missing Agent tasks and re-deploy, PL-17)

serves: PL-17

The Rescue Missing Agent tasks come due about 05:36Z (the operator's times from the secrets read, record `secret-missions/0334`). Verify the title SECRET COMMAND POST before any tap. Read each card's timer to the second with the UTC time. Claim ONLY with the in-game Claim button (one tap claims all finished tasks); if a task is not finished, claim nothing and write the time left. Then re-deploy with Mega Deploy (its toast 'no tasks available for dispatch' means nothing is pending). Write each card, the reward with counts, the new timers and the UTC time of the claim, so the next claim time is known. No diamond or item spend, no Mega Refresh, and Plunder Others is PvP: never tapped. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if one opens, STOP and touch nothing. Safe tap: the bare spot (310,660), not (400,640) after a camera shift (WORLD then BASE first).
Cost cap, stated: 0.40 USD.
