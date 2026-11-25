---
unit: secrets-refugee-claim-2026-11-25-001
regular: secrets
activity: secret-missions
segment: 2
priority: 2
created_at: 2026-11-25T03:16:31Z
expires_at: 2026-11-25T04:29:00Z
planned_for:
not_before: 2026-11-25T04:21:00Z
window: claim the refugee task and re-deploy, ends before the 04:30z calm window
est_minutes: 6
serves: PL-17
chain_id: refugee-claim-2026-11-25
chain_seq: 1
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
---

# secrets

Serves: PL-17

## Brief (definition pointer, from the roster)

This unit is the regular `secrets`: Secret missions - claim finished (one Claim takes all), Mega Deploy the rest (UR Only off; on duel UR days Mega Refresh first), check Reward Recovery. Its definition is the activity folder `_activities_/secret-missions/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, CLAIM the refugee task and re-deploy, ends before the 04:30Z calm window, PL-17)

serves: PL-17

The SSR PROTECT REFUGEE CAMP Lv.5 task ends 04:12:51Z (the operator's interim read, frame 03:14:07.3Z). The unit must END BEFORE 04:29Z. Verify the title SECRET COMMAND POST before any tap. Read each card's timer to the second with the UTC time. Claim ONLY with the in-game Claim button (one tap claims every finished task); if a task is not finished, claim nothing and write the time left. Then re-deploy with Mega Deploy (its toast 'no tasks available for dispatch' means nothing is pending). Write each card, the rewards with counts, the new timers and the UTC time of the claim. No diamond or item spend, no Mega Refresh; Plunder Others is PvP: never tapped. No Backpack or box-count read.
CLOSE by `_records_/2026-11-22/queue-planning/3170-closing-rule-done-and-partial.md`: DONE for a taken claim (state after, in the summary) or a verified nothing-to-do state with a `state_read: <what was read> | <frame> | <HH:MM:SSZ>` line; else PARTIAL; `--state-change yes` if a claim was taken.
FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Safe tap: the bare spot (310,660), not (400,640) after a camera shift (WORLD then BASE first). Verify each HUD icon by its label first.
Cost cap, stated: 0.40 USD.
