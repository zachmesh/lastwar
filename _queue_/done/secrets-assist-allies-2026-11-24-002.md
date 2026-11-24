---
unit: secrets-assist-allies-2026-11-24-002
regular: secrets
activity: secret-missions
segment: 2
priority: 2
created_at: 2026-11-24T11:21:26Z
expires_at: 2026-11-24T14:00:00Z
planned_for:
not_before: 2026-11-24T11:20:00Z
window: assist allies the four remaining ur cards one press per card clean free presses only
est_minutes: 6
serves: PL-17
chain_id: assist-allies-2026-11-24
chain_seq: 2
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T11:22:07Z
lease_until: 2026-11-24T11:42:07Z
result:
  status: done
  started_at: 2026-11-24T11:22:07Z
  finished_at: 2026-11-24T11:27:16Z
  duration_seconds: 309
  executor: operator
  summary: Four Assist presses (11:23:35.1Z to 11:25:28.3Z), one per card, each free (no picker, confirm, price or item): Assist Allies 1/5 to 5/5, each reward iron 324.9K, Mystery Supply Box x6, food 324.9K, Hero EXP 412.8K; March Queues 0/3 and Squad 1 unchanged at start and end; tram badge none; drags 0
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/secret-missions/1122-queue-run.md and 1122-queue-run.csv; run 20261124T112451Z-0d0f50
  follow_up: the cap 5/5 is reached; a pressed card reappeared at the bottom with a 5m timer tile (unexplained); the next Assist after the daily reset
  stats:
    target: press Assist on each of the four remaining cards after reading it
    achieved: four free presses, count 5/5
    resources_gained: none
    points: 0
    costs: none spent; model 0.447 USD
    verified: yes
    run_id: 20261124T112451Z-0d0f50
    run_steps: 34
    actions_done: 32
    actions_refused: 0
    cost_usd: 0.447
    device_takeovers: 0
    assist_presses: 4
    assist_count_after: 5
    march_queues: 0/3
    tram_badge: none
    drags_tried: 0
    rules_used: 1,2
  stats_missing: []
  stats_warnings: []
---

# secrets

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: PL-17

## Brief (definition pointer, from the roster)

This unit is the regular `secrets`: Secret missions - claim finished (one Claim takes all), Mega Deploy the rest (UR Only off; on duel UR days Mega Refresh first), check Reward Recovery. Its definition is the activity folder `_activities_/secret-missions/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, ASSIST ALLIES: the four remaining UR cards, Steer A's rule met)

serves: PL-17

Verify the title SECRET COMMAND POST before any tap. ASSIST ALLIES (measured 11:17Z, record `_records_/2026-11-22/secret-missions/1114-queue-run.md`): one press on a UR ally card paid MYSTERY SUPPLY BOX x6, HERO EXP 412.8K, IRON 324.9K, FOOD 324.9K, was free (no picker, confirm, price, diamond or item), moved the count 0/5 to 1/5 and left Squad 1 and the march queues unchanged. Press Assist on EACH of the FOUR remaining UR cards: ONE PRESS PER CARD, AFTER reading that card's text. STOP on anything but a clean free press: a picker, a price, a diamond, an item cost, a hero or squad line, any other dialog. After EACH press record the count (x/5), the reward (supply boxes, hero EXP, iron, food), the badge, and that Squad 1 and the march queues are unchanged. If the tab shows a timer, write it (the cards' refresh cadence is unread). Never Plunder Others, never Mega Refresh, no diamond or item spend. 6 steps.
Verify each HUD icon by its label or glyph before the tap. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.40 USD.
