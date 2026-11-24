---
unit: events-thanksgiving-store-read-2026-11-24-001
regular: events
activity: event-claims
segment: 3
priority: 2
created_at: 2026-11-24T19:10:15Z
expires_at: 2026-11-24T21:30:00Z
planned_for:
not_before: 2026-11-24T19:10:00Z
window: read the thanksgiving store rows balances end time and the gift and lottery text redeem nothing steer a 19:09z
est_minutes: 6
serves: upkeep
chain_id: thanksgiving-store-read-2026-11-24
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T19:27:40Z
lease_until: 2026-11-24T19:47:40Z
result:
  status: partial
  started_at: 2026-11-24T19:27:40Z
  finished_at: 2026-11-24T19:35:41Z
  duration_seconds: 481
  executor: operator
  summary: Thanksgiving Store read (6 turkey tickets held; rows 1 to 3 at 100, 100 and 10 tickets not affordable; row 4 a golden trophy x1 for 1 ticket, Limit 600; row 5 clipped, the pan moved 0 px); the Lottery tab tapped once shows only a full-window loading screen for 5 minutes: the Lottery and Gift of Thanks pages are unread: PARTIAL (blocker: a stuck loading screen); nothing pressed on any row; the screen left on the loading screen; tram icon not drawn; drags 1. state_change: no
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/event-claims/1927-queue-run.md and 1927-queue-run.csv; run 20261124T192740Z-6bd54f
  state_change: no
  follow_up: the game sits on the Lottery loading screen: Steer A or the coordinator decides the exit (a blind tap at the back-arrow spot (175,930), a key, or a relaunch); the Lottery and Gift of Thanks reads remain
  stats:
    target: read the Thanksgiving Store, the Lottery and the Gift of Thanks (read only)
    achieved: the Store rows 1 to 4 read; the rest blocked by the loading screen
    resources_gained: none
    points: 0
    costs: none spent; model 0.508827 USD
    verified: yes
    run_id: 20261124T192740Z-6bd54f
    run_steps: 39
    actions_done: 22
    actions_refused: 0
    cost_usd: 0.508827
    device_takeovers: 0
    claims: 0
    tickets_held: 6
    blocker_category: stuck loading screen
    tram_badge: icon not drawn
    drags_tried: 1
    drags_cancelled: 0
    rules_used: 1
  stats_missing: []
  stats_warnings: [blocker_category not in enum a-i]
---

# events

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: upkeep

## Brief (definition pointer, from the roster)

This unit is the regular `events`: Event claims - claim every earned reward on the Events screen and inside each event, including Battle Pass daily login, Halloween check-in while it runs and all Arms Race rewards; finish only after a final sweep shows no bouncing chest or reward red dot remains; never grind, never buy. Its definition is the activity folder `_activities_/event-claims/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, THE THANKSGIVING STORE, a read-only unit, Steer A 19:09Z)

serves: upkeep

THIS UNIT REDEEMS NOTHING: it reads the event Store so the Strategist can rank the rows (tickets may be spent later). Open the events hub by the route in `_activities_/event-claims/`, then the Thanksgiving Store.
(1) Before any pan name the blank right margin of THAT page in a frame.
(2) For EACH row write the item NAME, reward quantity, PRICE in tickets, limit and what is left; the ticket balances (turkey tickets, any other event currency); the event's END TIME. Crop digits at 6x from the SAVED frame. A clipped list: the composed pan, ONE per screen, at most THREE, in ONE MESSAGE: mouse_move to the margin; left_mouse_down; wait 1 (second); ONE move of about 175 px; wait 1 (second); left_mouse_up; a screenshot after. Refused or unmoved: stop.
(3) NOTHING IS REDEEMED (no Go Obtain, Redeem or Buy). A row priced in gems, diamonds or money: STOP.
(4) READ ONLY, NOT PRESSED: the GIFT OF THANKS (what the turkey send and cooking pot send, to whom, cost) and the LOTTERY (tickets, any free ticket held, price per draw).
(5) Any dialog, price line or other app: STOP. Close by the back arrow. `--state-change no`, `state_read:` line. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.60 USD.
