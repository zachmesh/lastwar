---
unit: secrets-oil-depot-claim-2026-11-24-001
regular: secrets
activity: secret-missions
segment: 2
priority: 1
created_at: 2026-11-24T03:38:42Z
expires_at: 2026-11-24T07:40:00Z
planned_for:
not_before: 2026-11-24T07:35:30Z
window: claim the oil depot one run must end before 0758z
est_minutes: 8
serves: PL-17
chain_id: oil-depot-claim-2026-11-24
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T07:35:49Z
lease_until: 2026-11-24T07:55:49Z
result:
  status: partial
  started_at: 2026-11-24T07:35:49Z
  finished_at: 2026-11-24T07:37:41Z
  duration_seconds: 112
  executor: operator
  summary: One Claim tap at 07:36:13.243Z claimed the finished UR Oil Depot: oil as five 6.0K items (30K), iron 3.2M, food 3.2M, Hero EXP 4.1M; the oil counter stayed 675.1K (the oil is in the Inventory as items); Mega Deploy opened no popup so there are no new timers; drags 0
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/secret-missions/0735-queue-run.md and 0735-queue-run.csv; run 20261124T073549Z-ce533c
  follow_up: the 30K oil waits as items in the Inventory (a Use is not authorized); the next card pair at the 4-hour start
  stats:
    target: claim the Oil Depot with the in-game Claim, write the reward and the oil counter before and after, then Mega Deploy
    achieved: claimed; oil as items; nothing to deploy
    resources_gained: none
    points: 0
    costs: none spent; model 0.130912 USD
    verified: yes
    run_id: 20261124T073549Z-ce533c
    run_steps: 10
    actions_done: 9
    actions_refused: 0
    cost_usd: 0.130912
    device_takeovers: 0
    claim_utc: 07:36:13.243
    oil_counter_before: 675.1K
    oil_counter_after: 675.1K
    drags_tried: 0
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

## Brief (planner, CLAIM the Oil Depot, one run, PL-17)

serves: PL-17

The Oil Depot was deployed at 03:35:16.130Z (card 04:00:10 left at 03:35:36.5Z, operator record `secret-missions/0334`): its claim is due about 07:35:46Z. Verify the title SECRET COMMAND POST before any tap. Read the card timer first, to the second with the UTC time. Claim ONLY with the in-game Claim button once the timer is done; write the reward (oil and anything else, with counts) and the oil counter before and after.

THE CLAIM AND ANYTHING AFTER IT MUST END BY 07:44Z: the cu helper install starts at 07:45Z and holds the lock, and the operator presses nothing from 07:45Z to 08:25Z (a claim after 07:44Z is refused by the lock). If it cannot END by 07:44Z, do not start; the card keeps and the claim waits for 08:25Z. Re-deploy with Mega Deploy only if it still ends by 07:44Z.
HUD taps: verify each HUD icon by its label or glyph in a frame before the tap.
Cost cap, stated: 0.40 USD.
