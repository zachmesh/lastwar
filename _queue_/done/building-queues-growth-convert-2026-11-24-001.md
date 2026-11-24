---
unit: building-queues-growth-convert-2026-11-24-001
regular: building-queues
activity: building-queues
segment: 1
priority: 1
created_at: 2026-11-23T08:27:06Z
expires_at: 2026-11-24T01:20:00Z
planned_for:
not_before: 2026-11-23T23:20:15Z
window: convert coin, start the lowest Drill Ground and apply bounded speed-ups when the builders free
est_minutes: 15
serves: PL-08
chain_id: growth-convert-2026-11-24
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T23:20:33Z
lease_until: 2026-11-23T23:40:33Z
result:
  status: done
  started_at: 2026-11-23T23:20:33Z
  finished_at: 2026-11-23T23:26:37Z
  duration_seconds: 364
  executor: operator
  summary: Lv.26 to 27 and Lv.27 to 28 Drill Grounds started (Upgrade once each); both previews show a food row (221.0M and 314.5M); coin 272.5M to 129.7M, food 674.4M to 138.9M; builders end 2026-12-03T19:20:37Z and 2026-12-07T20:21:48Z
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/building-queues/2320-queue-run.md and 2320-queue-run.csv; run 20261123T232106Z-f3d598
  follow_up: food row shown: the food conversion unit is needed (food 138.9M); the third ground needs more food; builders 3 and 4 idle
  stats:
    target: Lv.26 to 27 and Lv.27 to 28 Drill Ground starts with every cost row read
    achieved: 2 of 2 starts, all rows read, food row shown
    resources_gained: coin -142.8M; food -535.5M; iron -173.6M
    points: 0
    costs: none spent; model 0.388 USD
    verified: yes
    run_id: 20261123T232106Z-f3d598
    run_steps: 29
    actions_done: 55
    actions_refused: 0
    cost_usd: 0.388
    device_takeovers: 0
    slots_idle: 2
    coin_before: 272.5M
    coin_after: 129.7M
    food_before: 674.4M
    food_after: 138.9M
    food_row_shown: yes
    rules_used: 1
  stats_missing: []
  stats_warnings: []
---

# building-queues

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: PL-08

## Brief (planner, builders at 23:20Z, funding (a) and steps 1 and 2 of 3, decision 2603)

serves: PL-08

Decision `_records_/2026-11-22/team-operations/2603-first-builder-decision.md` (Strategist veto until 20:00Z today; a veto note here governs). Plan, tap points, previews, hazards: `_records_/2026-11-22/queue-planning/2540-drill-ground-sheet.md`; conversion procedure: `_records_/2026-11-22/queue-planning/2541-conversion-and-speedup-sheet.md`; follow both. Rules: `_records_/2026-11-22/queue-planning/2430-conversion-rules.md`, `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`. The owner plays by hand: start only on IDLE builders, never touch his queue; never press Obtain, Finish Now or buy.

HAZARD: the Resources tab opens with the 5,000 Diamonds x16 tile SELECTED and a live Use: tap the intended tile first, confirm its name in a frame, never Use with another tile selected.

Run 1, first the finished upgrades: hammer icon; press the button each finished Training Base entry shows, Complete or Collect (verb unverified [G], record its text; never Speed Up or Finish Now); Total Power before and after, since power registers only on Complete; note idle builders, or if none read the earliest time left and stop. Coin: read it. The conversion was done by the two units `building-queues-growth-preconvert-2026-11-23-001` and `-002`; if coin is below the cost of the starts still to do plus 10M, stop and record the shortfall, do not convert here.

Run 2, the starts: first idle builder, the Lv.26 ground (59.5M coin, 74.8M iron): read its tag and Upgrade preview INCLUDING the troop capacity line (current and next), the Details figure and the free room, read EVERY cost row of the preview, scrolling to its end if it scrolls, and write each row (name, value, visible without a scroll yes or no) in the unit note as [M] (the 11-10 preview of Lv.25 to 26 read iron 56.9M, food 170.0M; the 20:16Z previews showed no food row): write 'food row shown' or 'no food row after scrolling'; a short row stops this start with 'blocked by prerequisite: <resource>'; press Upgrade once, read the timer. Next idle builder, the Lv.27 ground (83.3M, 102.0M) the same way. Speed-ups: unit 003.

Tag text beside every number; none means [G]; add a tag_text column.

Two runs, 10 steps each. No hero-lever conversion.
Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`.
Quiet-window margin: this start (23:21Z trigger) is 8 h 39 min before the daily 08:00-08:25Z window; see `_records_/2026-11-22/queue-planning/2830-quiet-window-margins.md`.
Cost cap, stated: 0.90 USD (the harness stops near 0.36 of it).
