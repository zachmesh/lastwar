---
unit: building-queues-duel-speedup-own-count-2026-11-24-001
regular: building-queues
activity: building-queues
segment: 2
priority: 1
created_at: 2026-11-25T00:01:55Z
expires_at: 2026-11-25T01:15:00Z
planned_for:
not_before: 2026-11-25T00:08:00Z
window: duel speed ups by single uses and bubble x10 x100 with the own count as the field held for steer a option a
est_minutes: 12
serves: PL-08
chain_id: duel-speedup-own-count-2026-11-24
chain_seq: 1
attempts: 1
max_attempts: 1
claimed_by: operator
claimed_at: 2026-11-25T00:10:09Z
lease_until: 2026-11-25T00:30:09Z
result:
  status: done
  started_at: 2026-11-25T00:10:09Z
  finished_at: 2026-11-25T00:22:56Z
  duration_seconds: 767
  executor: operator
  summary: Duel speed-up by the Own-count route: 258 five-minute construction tiles on the Lv.26 Drill Ground (Own 24,489 to 24,231; the bubble read before each x100 and x10), the personal total 7,017,000 to 7,210,500 (the ten-tile check +7,500 exactly, 211 tiles 7,175,250); the Lv.26 ground now ends 2026-11-25T13:38:36Z (a fall of 21h 30m); the 7,200,000 chest claimed with one plain tap (seven reward tiles: a golden puzzle piece x1, a scroll card x1, a bar x10, a medal x400, a golden chest x15, a Lv.3 chest x1, a triangle crystal x2.0K); diamonds unchanged; tram icon not drawn; drags 0. state_change: yes. state_read: duel personal total 7,210,500; Own 24,231; Lv.26 Drill Ground 13:18:19 left; 7,200,000 chest claimed | step 2 | 00:20:16Z
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/building-queues/2410-queue-run.md and 2410-queue-run.csv; run 20261125T001009Z-fc193d
  state_read: duel personal total 7,210,500; Own 24,231; Lv.26 Drill Ground 13:18:19 left; 7,200,000 chest claimed | step 2 | 00:20:16Z
  state_change: yes
  follow_up: the Lv.26 Drill Ground completes about 11-25T13:38:36Z; the Oil Well about 07:11:19Z
  stats:
    target: personal total 7,200,000 and the claim
    achieved: 7,210,500 and the chest claimed
    resources_gained: Valor Badge x400; UR Hero Universal Shard x1; Tactical Master Supply Box x15; Lv.3 chest x1; golden scroll card x1; bar x10; triangle crystal x2.0K
    points: 0
    costs: none spent; model 0.728300 USD
    verified: yes
    run_id: 20261125T001009Z-fc193d
    run_steps: 59
    actions_done: 46
    actions_refused: 0
    cost_usd: 0.728300
    device_takeovers: 0
    tiles_used: 258
    own_before: 24489
    own_after: 24231
    total_before: 7017000
    total_after: 7210500
    claims: 1
    tram_badge: icon not drawn
    drags_tried: 0
    rules_used: 1,2,3
  stats_missing: []
  stats_warnings: []
---

# building-queues

Serves: PL-08

## Brief (definition pointer, from the roster)

Regular `building-queues` as a planner-briefed speed-up (`_activities_/building-queues/`): THIS BRIEF OVERRIDES the digest's read-only rule.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, DUEL SPEED-UPS, Own count, held)

serves: PL-08

Facts [M]: the panel has NO slider, plus button or typed field: each row only a blue Use (5m CONSTRUCTION (552,586), 'Own 24,489'; 1m (552,676); 8h general (552,766)); one Use spends one tile, then a bubble offers x10 or x100. Only CONSTRUCTION minutes score (750 a tile).
(1) VS panel first: total, chest state. (2) Builders panel: the Drill Ground Lv.26 row, its nominal and effective end times, its Speed Up panel; each row's NAME and Own tag first.
(3) CHECK: ten single Uses on the 5m CONSTRUCTION row only (or one Use, then the bubble's x10 ONLY if its label reads exactly 'x10' in a frame first), the Own tag read before and after (24,489 to 24,479); the VS total at once and after 30 seconds: +7,500 within 1,000. NOT MOVED: STOP and report.
(4) MOVED: the rest (248 tiles, 258 in all): 2 x 'x100', 4 x 'x10', 8 single Uses; before each Use the bubble's label read in a frame (exactly 'x100' or 'x10'), the Own tag before and after (24,279 after 210 tiles, 24,231 after 258). Read the VS total only after the 10 tiles, after 210 and at the end; after 210 only x10 and singles. STOP at 7,200,000 or more or at 258 tiles; never beyond.
(5) Write the Own tag after the last Use, each end time after, each total with its UTC time.
(6) At 7,200,000 or more: ONE plain Claim tap on the 7,200,000 chest ONLY; read the popup by TEXT (every row); close by its X, or Confirm ONLY a plain 'Congratulations' with NO price.
(7) NEVER the 1m row, the 8h general row, Max, Finish Now, a diamond line or any price: STOP. `--state-change yes`, a `state_read:` line. FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.80 USD.
