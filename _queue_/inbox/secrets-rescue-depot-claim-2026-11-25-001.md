---
unit: secrets-rescue-depot-claim-2026-11-25-001
regular: secrets
activity: secret-missions
segment: 2
priority: 1
created_at: 2026-11-25T03:16:37Z
expires_at: 2026-11-27T02:00:00Z
planned_for: 2026-11-25T10:01:28Z
not_before:
window: claim the rescue and oil depot tasks and re-deploy, after the oil well hand-off
est_minutes: 8
serves: PL-17
chain_id: rescue-depot-claim-2026-11-25
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

## Brief (planner, CLAIM the rescue and oil depot tasks, right after the Oil Well hand-off, PL-17)

serves: PL-17

The UR RESCUE TEST SUBJECT Lv.5 ends 07:13:02Z and the UR CAPTURE THE OIL DEPOT Lv.5 07:13:06Z: ONE claim takes both. A finished secret task is exposed to plunder from its end (04:16Z on 11-25): CLAIM FIRST, redeploy after. Opens 07:13:30Z, p1; Avoid 08:00Z-08:25Z and 09:58Z-10:05Z. Verify the title SECRET COMMAND POST before any tap. Read each card's timer to the second with the UTC time. Claim ONLY with the in-game Claim button (one tap claims every finished task); a task not finished: claim nothing, write the time left. Read the claim POPUP FROM ITS TOP (a frame before any scroll, one after: rows above may be missing); write every row with its count; quote the SECRET TASK REPORT lines (who as shown, when, what: plunder and ally help; the owner's own name never). Then re-deploy with Mega Deploy; write the new timers and the claim time. No diamond or item spend, no Mega Refresh; Plunder Others is PvP: never tapped. No Backpack or box-count read.
CLOSE by `_records_/2026-11-22/queue-planning/3170-closing-rule-done-and-partial.md`: DONE for a taken claim (state after, in the summary) or a verified nothing-to-do state with a `state_read: <what was read> | <frame> | <HH:MM:SSZ>` line; else PARTIAL; `--state-change yes` if a claim was taken.
FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Safe tap: the bare spot (310,660), not (400,640) after a camera shift (WORLD then BASE first).
Cost cap, stated: 0.40 USD.
