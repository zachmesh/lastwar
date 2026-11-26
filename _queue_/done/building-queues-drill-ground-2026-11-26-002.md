---
unit: building-queues-drill-ground-2026-11-26-002
regular: building-queues
activity: building-queues
segment: 1
priority: 1
created_at: 2026-11-26T08:59:57Z
expires_at: 2026-11-27T02:00:00Z
planned_for:
not_before: 2026-11-26T10:06:00Z
window: drill ground hand-off re-staged with the r5 coin exception (steer a 08:57z)
est_minutes: 15
serves: PL-08
chain_id: drill-ground-2026-11-26
chain_seq: 2
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-26T10:07:30Z
lease_until: 2026-11-26T10:27:30Z
result:
  status: done
  started_at: 2026-11-26T10:07:30Z
  finished_at: 2026-11-26T10:28:19Z
  duration_seconds: 1249
  executor: operator
  summary: Drill Ground Lv.27 to 28 started on the right ground (Upgrade once at 10:25:52.0Z; ends about 2026-12-10T07:24:19Z; timer 13d 20:57:28 at 10:26:51.1Z, 23,519 s under the preview's 14d 03:30:26) after a preconvert: Food Chest (UR) x36 (+146.1M food); Coin Chest (UR) x10, (SSR) x6, (SR) x138 and the coin items 30.0K x50, 6.0K x58 and 600 x6,757 (+49.1M coin); the R5 exception: UR choice chests x9 for Coin Chest (UR) items opened for +21.9M coin (of the 40M cap); costs coin 83.3M, iron 102.0M, food 314.5M paid, floors held (coin 11.1M, iron 677.7M, food 43.5M after); cost 1.64 USD against the cap 1.50 (over by 0.14, disclosed). state_change: yes
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/building-queues/1007-queue-run.md and 1007-queue-run.csv; run 20261126T100730Z-6f2dee
  state_change: yes
  follow_up: the builders are 4/4; the Drill Ground ends about 2026-12-10T07:24:19Z; R5 UR choice chests left 595
  stats:
    target: upgrade the Lv.27 Drill Ground to 28 with a preconvert
    achieved: Upgrade pressed once; timer running
    resources_gained: food +146.1M and coin +71.0M converted; paid coin 83.3M, iron 102.0M, food 314.5M
    points: 0
    costs: none spent; model 1.640479 USD
    verified: yes
    run_id: 20261126T100730Z-6f2dee
    run_steps: 120
    actions_done: 70
    actions_refused: 0
    cost_usd: 1.640479
    device_takeovers: 0
    claims: 1
    uses: 9
    r5_coin_used_m: 21.9
    upgrade_end_utc: 2026-12-10T07:24:19
    speed_factor: 2.17
    tram_badge: red dot at 10:09:14Z
    drags_tried: 3
    rules_used: 1,2
  stats_missing: []
  stats_warnings: [duration exceeds 15-minute unit cap]
---

# building-queues

Serves: PL-08

## Brief (definition pointer, from the roster)

This unit is the regular `building-queues`: Building queues - read the four build queues, record running upgrades and idle slots; read-only, never start builds. Its definition is the activity folder `_activities_/building-queues/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, the Drill Ground's next level, preconvert and the R5 coin exception, PL-08)

serves: PL-08

The finished Lv.27 ground has an IDLE builder. Next: Lv.27 to 28. RIGHT GROUND: tag 'Drill Ground Lv.27', no upgrade timer, else STOP. RULES: `_records_/2026-11-22/queue-planning/2542-drill-ground-preconvert-rules.md`, `_records_/2026-11-22/queue-planning/2545-r5-coin-exception.md`, sheets 2540, 2541. DISPATCH ONLY WHEN NAMED (from 10:06Z if no veto; it must end before 11:25Z).
(1) FIRST the builders panel (hammer opens nothing: routes table, builders row, never a fourth tap) and the chest counts, then the Upgrade preview: every cost row within 1 percent of 83.3M coin, 102.0M iron, 314.5M food, else STOP. FLOORS after cost: iron at least 100M, food at least 30M, coin at least 10M.
(2) PRECONVERT, fixed chests only: food UR then SSR; coin UR, SSR, SR, then the coin items; then ONLY the coin shortfall left, from UR choice chests (CAP 40M coin, about 17 chests: sheet 2545). Each Use (sheet 2542): the tab opens with the 5,000 Diamonds x16 tile SELECTED and a LIVE Use: NEVER tap that tile; select the chest by icon and count tag, read its NAME and count, set the smaller of the need and the count, read the field in a frame, Use; the HUD must rise by quantity times value within 1 percent or STOP. The rest of R5 is NEVER TOUCHED; any diamond line or price: STOP.
(3) Press Upgrade ONCE; write its end UTC.
Up to SIXTEEN runs of 12 steps. Cost cap: 1.50 USD.
CLOSE by `_records_/2026-11-22/queue-planning/3170-closing-rule-done-and-partial.md`: DONE for the Upgrade pressed or a verified nothing-to-do (`state_read:` line); `--state-change yes` if pressed.
FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
