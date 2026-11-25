---
unit: building-queues-duel-speedup-2026-11-24-001
regular: building-queues
activity: building-queues
segment: 2
priority: 1
created_at: 2026-11-24T23:09:17Z
expires_at: 2026-11-25T01:15:00Z
planned_for:
not_before: 2026-11-24T23:50:00Z
window: speed up the lv 26 drill ground for the duel personal chest held for the strategist yes steer a 23:07z
est_minutes: 12
serves: PL-08
chain_id: duel-speedup-2026-11-24
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T23:52:14Z
lease_until: 2026-11-25T00:12:14Z
result:
  status: partial
  started_at: 2026-11-24T23:52:14Z
  finished_at: 2026-11-25T00:09:29Z
  duration_seconds: 1035
  executor: operator
  summary: Duel speed-up PARTIAL: blocked by prerequisite: the Speed Up panel has no slider, plus button or typed field (steps 1 and 2 read: total 7,017,000, the 7,200,000 chest closed, the Lv.26 Drill Ground ends 2026-11-26T11:08:37.4Z; 5m Construction Own 24,489); nothing used; Steer A approved the Own-count route as a new unit at 00:08Z; the tram icon not drawn; drags 0. state_change: no
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/building-queues/2352-queue-run.md and 2352-queue-run.csv; run 20261124T235215Z-11ab2d
  state_change: no
  follow_up: the new unit building-queues-duel-speedup-own-count-2026-11-24-001 carries the Own-count route
  stats:
    target: speed up the Lv.26 Drill Ground with construction 5-minute tiles for the duel chest
    achieved: steps 1 and 2 read; the guard blocked step 3; nothing used
    resources_gained: none
    points: 0
    costs: none spent; model 0.165611 USD
    verified: yes
    run_id: 20261124T235215Z-11ab2d
    run_steps: 13
    actions_done: 6
    actions_refused: 0
    cost_usd: 0.165611
    device_takeovers: 0
    claims: 0
    own_5m: 24489
    blocker_category: prerequisite: no quantity control
    tram_badge: icon not drawn
    drags_tried: 0
    rules_used: 1
  stats_missing: []
  stats_warnings: [blocker_category not in enum a-i, duration exceeds 15-minute unit cap]
---

# building-queues

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: PL-08

## Brief (definition pointer, from the roster)

This unit is the regular `building-queues` run as a planner-briefed speed-up (`_activities_/building-queues/`: THIS BRIEF OVERRIDES its read-only rule); a step neither covers: stop, 'blocked by prerequisite'.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, DUEL SPEED-UPS: construction 5-minute tiles only, GO, Steer A 23:49Z)

serves: PL-08

Facts: the page scores 'Use 1-min CONSTRUCTION Speed-up +150': only construction tiles, NEVER a general tile. Target 7,200,000 (was 7,017,000). Done by 01:15Z; claim by 01:45Z.
(1) VS panel first: the total and the 7,200,000 chest's state.
(2) Builders panel: the Drill Ground Lv.26 row, its end time to the second, its Speed Up panel; each item's NAME and MINUTES in a frame first.
(3) CHECK: the construction 5-minute tile to EXACTLY 10 (slider to 1, the plus button, the field read in a frame before the Use tap: not 10: DO NOT press), Use ONCE; the VS total before, at once after and again after about 30 seconds: expected +7,500, within 1,000. NOT MOVED (both reads flat): STOP and report; nothing more used.
(4) MOVED: the rest, 248 tiles (258 in all: 1,290 minutes, 193,500 points) in batches by the plus-button route, the field read in a frame before EACH Use tap, the total read after each batch; STOP at 7,200,000 or more. Never beyond 258 tiles (cap 31,500 minutes). No other item, no Max.
(5) The Drill Ground's end time after (nominal, effective fall).
(6) At 7,200,000 or more: ONE plain Claim tap on the 7,200,000 chest ONLY; read the popup by TEXT, every reward row shown (item NAME, QUANTITY; no pan); close it by its X, or Confirm ONLY a plain 'Congratulations' with NO price. NEVER a Claim on anything with a price, never Buy, Go or Draw.
(7) NEVER Finish Now or a diamond line; any price, diamond count or purchase confirm: STOP. `--state-change yes`, a `state_read:` line. FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.80 USD.
