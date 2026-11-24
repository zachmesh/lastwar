---
unit: events-thanksgiving-badge-2026-11-24-001
regular: events
activity: event-claims
segment: 3
priority: 2
created_at: 2026-11-24T18:48:03Z
expires_at: 2026-11-24T20:30:00Z
planned_for:
not_before: 2026-11-24T18:48:00Z
window: read the thanksgiving event badge items and claim only a plain free claim steer a 18:45z
est_minutes: 5
serves: upkeep
chain_id: thanksgiving-badge-2026-11-24
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T19:04:06Z
lease_until: 2026-11-24T19:24:06Z
result:
  status: done
  started_at: 2026-11-24T19:04:06Z
  finished_at: 2026-11-24T19:05:42Z
  duration_seconds: 96
  executor: operator
  summary: Thanksgiving badge read-only look: the badge read 5 then 2 with nothing pressed; the badge items are the Store (Go Obtain at 6/100, 6/100, 6/10 tickets and a Redeem at 6/1, limit 600) and the Gift of Thanks (Gift Turkey, a cooking pot): no plain free Claim; both are the excluded categories (they spend event tickets or send a turkey); nothing pressed but one tab; HUD unchanged; drags 0. state_change: no. state_read: Thanksgiving Store dot 3 (Go Obtain at 6/100, 6/100, 6/10 tickets; Redeem 6/1), Gift of Thanks dot 1 (Gift Turkey), Lottery no dot: no plain free Claim | step 3 | 19:04:29Z
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/event-claims/1904-queue-run.md and 1904-queue-run.csv; run 20261124T190407Z-a510f9
  state_read: Thanksgiving Store dot 3 (Go Obtain at 6/100, 6/100, 6/10 tickets; Redeem 6/1), Gift of Thanks dot 1 (Gift Turkey), Lottery no dot: no plain free Claim | step 3 | 19:04:29Z
  state_change: no
  follow_up: Steer A's call: whether the Redeem at 6/1 tickets (limit 600) joins the events unit; the Lottery tab was not opened
  stats:
    target: what the badge-5 items are and whether one is an excluded claim
    achieved: items named; both are excluded categories; no free claim
    resources_gained: none
    points: 0
    costs: none spent; model 0.112894 USD
    verified: yes
    run_id: 20261124T190407Z-a510f9
    run_steps: 8
    actions_done: 3
    actions_refused: 0
    cost_usd: 0.112894
    device_takeovers: 0
    badge_before: 5
    badge_after: 2
    claims: 0
    tram_badge: icon not drawn
    drags_tried: 0
    rules_used: 1
  stats_missing: []
  stats_warnings: []
---

# events

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: upkeep

## Brief (definition pointer, from the roster)

This unit is the regular `events`: Event claims - claim every earned reward on the Events screen and inside each event, including Battle Pass daily login, Halloween check-in while it runs and all Arms Race rewards; finish only after a final sweep shows no bouncing chest or reward red dot remains; never grind, never buy. Its definition is the activity folder `_activities_/event-claims/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, THE THANKSGIVING EVENT BADGE: a read-only look, Steer A 18:45Z)

serves: upkeep

The Thanksgiving badge rose 2, 4, 5 with no refresh while the events unit closed 'nothing to claim' four times; its rules exclude the event's Store, Lottery and Gift of Thanks (they spend event currency, send a turkey or go). THE QUESTION: what the badge-5 items are, and whether one is a claim those rules exclude. Open the events hub by the route in `_activities_/event-claims/`, then the Thanksgiving event. 5 steps:
(1) For EACH item the badge counts: write its NAME, button label (Claim, Go, Draw, Buy, Exchange), any price or gem icon and ticket count, with the UTC time.
(2) PRESS only a plain free CLAIM, once each. A draw or lottery with a FREE TICKET already held: once per ticket count read, and reported (never a price, never a diamond, never 'Buy tickets'). A store: read only. A turkey send or Gift of Thanks: not pressed.
(3) Any diamond or price line or purchase surface: STOP, touch nothing.
(4) The result says whether a badge item is a claim the events unit's rules exclude and WHY (what the page says). Close with the back arrow. Complete with `--state-change yes` if a claim paid, else `no` with a `state_read:` line. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.50 USD.
