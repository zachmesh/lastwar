---
unit: scout-midday-box-sample-2-2026-11-24-001
regular: scout-midday
activity: perception-scout
segment: 2
priority: 1
created_at: 2026-11-24T16:39:48Z
expires_at: 2026-11-24T17:15:00Z
planned_for:
not_before: 2026-11-24T16:39:00Z
window: second box sample batch eleven mystery supply boxes by one use under steer a box policy r6
est_minutes: 6
serves: snapshot
chain_id: box-sample-2-2026-11-24
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T16:44:54Z
lease_until: 2026-11-24T17:04:54Z
result:
  status: done
  started_at: 2026-11-24T16:44:54Z
  finished_at: 2026-11-24T16:46:49Z
  duration_seconds: 115
  executor: operator
  summary: Second sample of the Mystery Supply Box: ONE Use of exactly 11 boxes opened (stack 387 to 376): payout a blue-frame chest x9, a blue triangle item x100, a grey-white Lv.1 chest x1; no shard, no diamonds, no price or choice; the quantity read 1, 5, 9 and 11 before the Use; diamonds 11,173 unchanged; tram badge none; one slider drag. state_change: yes
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/perception-scout/1644-queue-run.md and 1644-queue-run.csv; run 20261124T164455Z-76a660
  follow_up: n=21 boxes opened in two batches (10 and 11): no shard and no diamonds yet; the nine chests and the Lv.1 chest wait unopened in the stock
  stats:
    target: open exactly 11 Mystery Supply Boxes with one Use and read the full payout
    achieved: 11 boxes opened, payout read
    resources_gained: blue-frame chest x9; blue triangle item x100; Lv.1 chest x1
    points: 0
    costs: none spent; model 0.14622 USD
    verified: yes
    run_id: 20261124T164455Z-76a660
    run_steps: 11
    actions_done: 36
    actions_refused: 0
    cost_usd: 0.14622
    device_takeovers: 0
    boxes_opened: 11
    stack_before: 387
    stack_after: 376
    shards: 0
    diamonds_paid: 0
    tram_badge: none
    drags_tried: 1
    rules_used: 1,2,3
  stats_missing: []
  stats_warnings: []
---

# scout-midday

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: snapshot

## Brief (definition pointer, from the roster)

This unit is the regular `scout-midday`: Scout - midday perception pass (floor anchor); re-walk the interface for state-dependent availability (trains, phase rotations, market refreshes); full passes also fire on detected state change between anchors. Its definition is the activity folder `_activities_/perception-scout/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, THE SECOND BOX SAMPLE: ONE Use of EXACTLY 11 Mystery Supply Boxes, Steer A 16:29Z and 16:40Z)

serves: snapshot

THE WHOLE PERMISSION (batch 1: `_records_/2026-11-22/growth/0913-box-sample-1.md`):
(1) Bottom bar Inventory (opens on Special): THE SPECIAL TAB ONLY, NEVER Resources. Select the purple question-mark chest by ONE tap on the tile body. READ in a frame the TITLE ('Mystery Supply Box') and the STACK COUNT (387).
(2) THE DEFAULT QUANTITY IS THE FULL STOCK. Slide the handle (start ON the handle) to the far left (1), then raise it with the PLUS button (this unit only), READING the quantity field in a frame after every three or four taps, to EXACTLY 11; if it reads more, correct with minus; NEVER the Max control; no typing. The final frame must show 11 BEFORE the Use tap; if it cannot be made 11: STOP 'quantity not 11', do not press.
(3) The Use tap is the single act: Use ONCE (no Open all, no second Use, no Sell, Merge or Split) then a frame: stack count (expected 376).
(4) READ WHAT THE USE PAYS IN FULL: EVERY item name and quantity, any SHARD (which hero) and any DIAMOND amount. The SR choice chests are NOT opened or converted.
(5) A dialog asking to choose or confirm a price, another app, or a local_input pointer event: STOP. Complete with `--state-change yes`, the counts and the payout list. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.80 USD.
