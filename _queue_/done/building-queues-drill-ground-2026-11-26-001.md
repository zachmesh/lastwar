---
unit: building-queues-drill-ground-2026-11-26-001
regular: building-queues
activity: building-queues
segment: 1
priority: 1
created_at: 2026-11-26T04:47:08Z
expires_at: 2026-11-27T02:00:00Z
planned_for:
not_before: 2026-11-26T04:47:00Z
window: drill ground hand-off re-staged, lv.27 to 28 (coach 04:46z)
est_minutes: 15
serves: PL-08
chain_id: drill-ground-2026-11-26
chain_seq: 1
attempts: 2
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-26T08:36:09Z
lease_until: 2026-11-26T08:56:09Z
result:
  status: partial
  started_at: 2026-11-26T08:36:09Z
  finished_at: 2026-11-26T08:46:53Z
  duration_seconds: 644
  executor: operator
  summary: Drill Ground stopped before any Use: the coin shortfall for Lv.27 to 28 is 78.5M (83.3M by the sheet plus the 10M floor, 14.8M held) and every coin chest gives only 43.18M (UR 10 x 2.43M, SSR 6 x 812.16K, SR 138 x 101.52K; coin items 5.90M): the chests cannot cover it; one builder idle; iron chests UR 289 (4.06M), SSR 1,428, SR 8,702; food chests SSR 1,428, SR 8,726, an orange 73; nothing used; the different-device dialog never showed; cost 0.51 USD of 1.20; drags 3. state_change: no
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/building-queues/0436-queue-run.md and 0436-queue-run.csv; run 20261126T083609Z-bb02cf
  state_change: no
  follow_up: the idle builder needs coin: 78.5M short for the Drill Ground; the coin chests give 43.18M
  stats:
    target: preconvert fixed chests and upgrade the Lv.27 Drill Ground
    achieved: stopped before any Use: the chests cannot cover the coin shortfall
    resources_gained: none
    points: 0
    costs: none spent; model 0.509718 USD
    verified: yes
    run_id: 20261126T083609Z-bb02cf
    run_steps: 45
    actions_done: 15
    actions_refused: 0
    cost_usd: 0.509718
    device_takeovers: 0
    claims: 0
    blocker_category: supply: coin chests cannot cover the shortfall
    coin_chest_total: 43180000
    coin_shortfall: 78500000
    slots_idle: 1
    tram_badge: not read
    drags_tried: 3
    rules_used: 1,2
  stats_missing: []
  stats_warnings: [blocker_category not in enum a-i]
---

# building-queues

Serves: PL-08

## Brief (definition pointer, from the roster)

This unit is the regular `building-queues`: Building queues - read the four build queues, record running upgrades and idle slots; read-only, never start builds. Its definition is the activity folder `_activities_/building-queues/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, the Drill Ground's next level with a preconvert, PL-08)

serves: PL-08

The ground that finished Lv.26 on 11-25 at 13:38:36Z is Lv.27 with an IDLE builder. Next: Lv.27 to 28. RIGHT GROUND: tag 'Drill Ground Lv.27', no upgrade timer, else STOP. RULES: `_records_/2026-11-22/queue-planning/2542-drill-ground-preconvert-rules.md`, sheets 2540, 2541. After the harvest unit and the room collect (Steer A 04:43Z); a WRAPPED GIFT BOX still on it: tap ONCE.
(1) FIRST the builders panel (hammer opens nothing: routes table, builders row, never a fourth tap) and the chest counts, then the Upgrade preview: every cost row. FLOORS after cost: iron at least 100M, food at least 30M, coin at least 10M.
(2) If any resource would fall under cost plus floor: PRECONVERT FIRST, fixed chests only: UR food, then SSR food; UR coin, then SSR coin; the shortfall plus about 10 percent, highest tier first. Each Use: the Resources tab opens with the 5,000 Diamonds x16 tile SELECTED and a LIVE Use: NEVER tap that tile; select the chest tile by icon and count tag, read its NAME and the count, set the smaller of the needed quantity and the count with the plus button, read the field in a frame, Use; the HUD must rise by quantity times value within 1 percent or STOP. THE RESERVE R5 IS NEVER TOUCHED; any diamond line or price: STOP.
(3) Press Upgrade ONCE; write the timer and end UTC.
Up to FOURTEEN runs of 12 steps. Cost cap: 1.20 USD.
CLOSE by `_records_/2026-11-22/queue-planning/3170-closing-rule-done-and-partial.md`: DONE for the Upgrade pressed or a verified nothing-to-do (`state_read:` line); `--state-change yes` if pressed.
FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
