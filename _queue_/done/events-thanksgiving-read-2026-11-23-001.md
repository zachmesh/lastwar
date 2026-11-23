---
unit: events-thanksgiving-read-2026-11-23-001
regular: events
activity: event-claims
segment: 3
priority: 3
created_at: 2026-11-23T17:38:49Z
expires_at: 2026-11-24T01:00:00Z
planned_for:
not_before: 2026-11-23T17:50:00Z
window: read only thanksgiving event store lottery and gift of thanks nothing pressed
est_minutes: 10
serves: PL-06
chain_id: thanksgiving-read-2026-11-23
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T17:56:26Z
lease_until: 2026-11-23T18:16:26Z
result:
  status: done
  started_at: 2026-11-23T17:56:26Z
  finished_at: 2026-11-23T17:58:29Z
  duration_seconds: 123
  executor: operator
  summary: Thanksgiving read-only: tickets 6, lottery tickets 10, turkeys 7, ingredients 30; event tabs end 2026-11-30T02:00:00Z, Store ends 2026-12-01T02:00:00Z; Store rows priced 100, 100, 10, 1 tickets; nothing pressed
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/event-claims/1756-queue-run.md and 1756-queue-run.csv; run 20261123T175626Z-8a6e59
  follow_up: strategist: lottery Draw x1 costs 1 ticket and x10 costs 10 (10 tickets on hand); the trophy row costs 1 ticket with limit 600; the Store runs to 2026-12-01T02:00Z
  stats:
    target: read the end timer first, then the Store, Lottery and Gift of Thanks tabs, nothing pressed
    achieved: end timers, balances, prices and limits read on five pages
    resources_gained: none
    points: 0
    costs: none spent; model 0.113882 USD
    verified: yes
    run_id: 20261123T175626Z-8a6e59
    run_steps: 9
    actions_done: 13
    actions_refused: 0
    cost_usd: 0.113882
    device_takeovers: 0
    event_end_utc: 2026-11-30T02:00:00Z
    store_end_utc: 2026-12-01T02:00:00Z
    thanksgiving_tickets: 6
    lottery_tickets: 10
    rules_used: 6,8
  stats_missing: []
  stats_warnings: []
---

# events

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: PL-06

## Brief (definition pointer, from the roster)

This unit is the regular `events`: Event claims - claim every earned reward on the Events screen and inside each event, including Battle Pass daily login, Halloween check-in while it runs and all Arms Race rewards; finish only after a final sweep shows no bouncing chest or reward red dot remains; never grind, never buy. Its definition is the activity folder `_activities_/event-claims/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, READ-ONLY: the Thanksgiving Event store, lottery and Gift of Thanks)

serves: PL-06

The events sweep (`_records_/2026-11-22/event-claims/1731-queue-run.md`) found the Thanksgiving Event's tabs Store (red dot 3), Lottery, Gift of Thanks (red dot 1) and Login: every control spends event tickets or ingredients, sends a turkey to allies, or is a Go. The Strategist ranks them, so this unit only READS. Route: the Thanksgiving icon on the base, then its tabs.

1. Read the event's end timer to the second, with the UTC time: it sets the spending deadline.
2. Store: per item the name, the price (tickets or ingredients, and which), bought over per-person limit, any timer, what it gives; and every event currency balance.
3. Lottery: the draw buttons, each cost and currency, the balance, any free draw, the prize list, any odds or pity counter. DO NOT DRAW.
4. Gift of Thanks: what the turkey is, its cost, who receives it (no player names), what the pot pays, why the red dot shows. DO NOT SEND.
5. Press NOTHING that buys, redeems, draws, sends, claims or goes. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if one opens, STOP and touch nothing. A TIPS dialog about another device: STOP, report.

Up to two runs, 10 steps each. Tag text beside every number; none means [G]; one frame per tab. Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`.
Cost cap, stated: 0.40 USD per run (the harness stops near 0.36 of it).
