---
unit: secrets-oil-depot-claim-2026-11-24-001
regular: secrets
activity: secret-missions
segment: 2
priority: 1
created_at: 2026-11-24T03:38:42Z
expires_at: 2026-11-24T07:52:00Z
planned_for:
not_before: 2026-11-24T07:35:30Z
window: claim the oil depot one run must end before 0758z
est_minutes: 8
serves: PL-17
chain_id: oil-depot-claim-2026-11-24
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

## Brief (planner, CLAIM the Oil Depot, one run, PL-17)

serves: PL-17

The Oil Depot was deployed at 03:35:16.130Z (card 04:00:10 left at 03:35:36.5Z, operator record `secret-missions/0334`): its claim is due about 07:35:46Z. Verify the title SECRET COMMAND POST before any tap. Read the card timer first, to the second with the UTC time. Claim ONLY with the in-game Claim button once the timer is done; write the reward (oil and anything else, with counts) and the oil counter before and after.

THE CLAIM AND ANYTHING AFTER IT MUST END BEFORE 07:58Z (the cu window starts at 08:00Z): if it cannot, do not start; the card keeps and the claim waits for 08:25Z. Re-deploy with Mega Deploy only if it still ends before 07:58Z. No diamond or item spend, no Mega Refresh, and Plunder Others is PvP: never tapped. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if one opens, STOP and touch nothing. Safe tap: the bare spot (310,660), not (400,640) after a camera shift (WORLD then BASE first).
Cost cap, stated: 0.40 USD.
