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
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
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
