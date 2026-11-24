---
unit: secrets-assist-allies-2026-11-24-001
regular: secrets
activity: secret-missions
segment: 2
priority: 2
created_at: 2026-11-24T11:11:15Z
expires_at: 2026-11-24T14:00:00Z
planned_for:
not_before: 2026-11-24T11:12:00Z
window: assist allies one press only if free and no hero or squad locked
est_minutes: 4
serves: PL-17
chain_id: assist-allies-2026-11-24
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T11:14:08Z
lease_until: 2026-11-24T11:34:08Z
result:
  status: done
  started_at: 2026-11-24T11:14:08Z
  finished_at: 2026-11-24T11:19:31Z
  duration_seconds: 323
  executor: operator
  summary: One Assist press at 11:17:05.552Z (free, no picker, price or item): Assist Allies 0/5 to 1/5, reward Mystery Supply Box x6, Hero EXP 412.8K, iron 324.9K, food 324.9K; the card consumed, badge 5 to 4; March Queues 0/3 and Squad 1 (five Lv.150 heroes) unchanged; tram badge none; drags 0
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/secret-missions/1114-queue-run.md and 1114-queue-run.csv; run 20261124T111629Z-ad852b
  follow_up: four ally cards remain with Assist buttons (Assist Allies 1/5): a follow-up unit may press once more under the same read-first; the Assist never touched the march queue or Squad 1
  stats:
    target: press Assist once if free, read the squad and march effects
    achieved: one free Assist, no squad or march effect
    resources_gained: none
    points: 0
    costs: none spent; model 0.405 USD
    verified: yes
    run_id: 20261124T111629Z-ad852b
    run_steps: 32
    actions_done: 42
    actions_refused: 0
    cost_usd: 0.405
    device_takeovers: 0
    assist_count_before: 0
    assist_count_after: 1
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

## Brief (planner, ASSIST ALLIES: one bounded press, Steer A's rule of 11:10Z)

serves: PL-17

The Secret Command Post 'Ally Tasks' tab (badge 5) shows FOUR UR ally cards with a blue Assist button, 'Assist Allies 0/5' (record `_records_/2026-11-22/secret-missions/1101-queue-run.md`). Steer A: yes, with a READ FIRST. Verify the title SECRET COMMAND POST before any tap. 4 steps, ONE press at most.

(a) READ: the card's text, the Assist button's label, any cost or requirement line, the reward line, the count 0 of 5; and BEFORE the press the march queues (World map, 'March Queues x/3') and the heroes' state of Squad 1.
(b) PRESS ASSIST ONCE only if it reads free with NO price, NO diamond, NO item spent, and NO hero or squad assigned or locked. If it asks to choose a hero or a squad: STOP, do not choose, tell the Coordinator.
(c) AFTER the press read what changed: the count, the reward, the card's state, and that Squad 1 is still available (the march queues and the heroes' state, before and after).
(d) If anything else shows (a confirm with a price, a hero picker, another app): STOP and tell the Coordinator. No second press in this unit; no Mega Refresh; no diamond or item spend; Plunder Others never tapped.
Verify each HUD icon by its label or glyph before the tap. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.30 USD.
