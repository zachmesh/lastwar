---
unit: building-queues-growth-convert-2026-11-24-002
regular: building-queues
activity: building-queues
segment: 1
priority: 1
created_at: 2026-11-23T08:27:07Z
expires_at: 2026-11-24T01:22:00Z
planned_for:
not_before: 2026-11-23T23:20:15Z
window: convert coin, start the lowest Drill Ground and apply bounded speed-ups when the builders free
est_minutes: 15
serves: PL-08
chain_id: growth-convert-2026-11-24
chain_seq: 2
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T23:38:11Z
lease_until: 2026-11-23T23:58:11Z
result:
  status: done
  started_at: 2026-11-23T23:38:11Z
  finished_at: 2026-11-23T23:41:24Z
  duration_seconds: 193
  executor: operator
  summary: Lv.28 Drill Ground to Lv.29 started once at 23:39:45.957Z: coin 119.0M, iron 144.5M, food 442.0M; the builders panel ends it 2026-12-12T02:29:20Z, exactly the preview time minus 6h 32m 00s; all four builders busy
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/building-queues/2338-queue-run.md and 2338-queue-run.csv; run 20261123T233811Z-81bad5
  follow_up: coin 8.8M, food 104.1M, iron 756.3M left; the first builder frees 2026-11-24T02:17:53Z (Oil Well)
  stats:
    target: Lv.28 Drill Ground to Lv.29 start, every cost row read
    achieved: start pressed once, all rows read, flat test passes
    resources_gained: coin -119.0M; food -442.0M; iron -144.5M
    points: 0
    costs: none spent; model 0.229766 USD
    verified: yes
    run_id: 20261123T233811Z-81bad5
    run_steps: 16
    actions_done: 53
    actions_refused: 0
    cost_usd: 0.229766
    device_takeovers: 0
    slots_idle: 0
    coin_after: 8.8M
    food_after: 104.1M
    iron_after: 756.3M
    rules_used: 1
  stats_missing: []
  stats_warnings: []
---

# building-queues

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: PL-08

## Brief (planner, builders at 23:20Z, funding (b), step 3 and the fourth builder, decision 2603)

serves: PL-08

Decision `_records_/2026-11-22/team-operations/2603-first-builder-decision.md` (Strategist veto until 20:00Z today; a veto note here governs). Plan, tap points, previews, hazards: `_records_/2026-11-22/queue-planning/2540-drill-ground-sheet.md`; conversion procedure: `_records_/2026-11-22/queue-planning/2541-conversion-and-speedup-sheet.md`; follow both. Rules: `_records_/2026-11-22/queue-planning/2430-conversion-rules.md`, `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`. The owner plays by hand: start only on IDLE builders, never touch his queue; never press Obtain, Finish Now or buy.

HAZARD: the Resources tab opens with the 5,000 Diamonds x16 tile SELECTED and a live Use: tap the intended tile first, confirm its name in a frame, never Use with another tile selected.

Run 1: hammer icon. Unit 001 completes the finished upgrades first; press Complete or Collect on any still uncollected. Skip any ground already upgrading. Read coin: the pre-conversion units funded the starts; if coin is below the cost of this start plus 10M, stop and record the shortfall.

Run 2, the starts: the next idle builder, the Lv.28 ground (119.0M coin, 144.5M iron): read its tag and preview INCLUDING the troop capacity line (current and next), the Details figure and the free room, read EVERY cost row of the preview, scrolling to its end if it scrolls, and write each row (name, value, visible without a scroll yes or no) in the unit note as [M] (the 11-10 preview of Lv.25 to 26 read iron 56.9M, food 170.0M; the 20:16Z previews showed no food row): write 'food row shown' or 'no food row after scrolling'; a short row stops this start with 'blocked by prerequisite: <resource>' (if it is food, do not retry here: the coordinator names the food unit `building-queues-growth-preconvert-2026-11-23-003`, then `building-queues-growth-convert-2026-11-24-004`, the same start); press Upgrade once, read the timer. The fourth builder is the Oil Well (unit `building-queues-oil-well-2026-11-24-001` runs second): three are free for the grounds; if none is idle, stop. The Strategist's B2 to B4 pick governs.

Tag text beside every number; none means [G]; add a tag_text column.

Two runs, 10 steps each. No hero-lever conversion. No chain successor.
Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`.
Quiet-window margin: this start (23:21Z trigger) is 8 h 39 min before the daily 08:00-08:25Z window; see `_records_/2026-11-22/queue-planning/2830-quiet-window-margins.md`.
Cost cap, stated: 0.90 USD (the harness stops near 0.36 of it).
