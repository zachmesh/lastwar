---
unit: scout-midday-backpack-names-2026-11-24-001
regular: scout-midday
activity: perception-scout
segment: 2
priority: 2
created_at: 2026-11-24T16:12:07Z
expires_at: 2026-11-24T17:15:00Z
planned_for:
not_before: 2026-11-24T16:18:00Z
window: select at most four tiles on the special tab to read their names never use held for steer a
est_minutes: 6
serves: snapshot
chain_id: backpack-names-2026-11-24
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T16:19:11Z
lease_until: 2026-11-24T16:39:11Z
result:
  status: done
  started_at: 2026-11-24T16:19:11Z
  finished_at: 2026-11-24T16:22:20Z
  duration_seconds: 189
  executor: operator
  summary: Backpack Special tab names: the purple question-mark chest x387 is the Mystery Supply Box ('said to contain Universal UR Shards and 5,000 Diamonds'), the gold question-mark chest x350 is Violet's Loot (a chance of a Violet Shard or 2500 Alliance Contribution Points), the chest VII x1 is the Nameplate Choice Chest VII; selecting changed no state, nothing used; tram badge none. state_read: Mystery Supply Box x387; Violet's Loot x350; Nameplate Choice Chest VII x1 (panels quoted) | step 5 and step 9 frames of run 20261124T161911Z-6b7838, step 5 frame of run 20261124T162055Z-ca6b46 | 16:21:35Z. state_change: no
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/perception-scout/1619-queue-run.md and 1619-queue-run.csv; run 20261124T161911Z-6b7838
  follow_up: the item names for the Coach's pricing: Mystery Supply Box x387 is the large stock
  stats:
    target: read the names of three Special tiles by selecting them, never using
    achieved: three panels read
    resources_gained: none
    points: 0
    costs: none spent; model 0.246848 USD
    verified: yes
    run_id: 20261124T161911Z-6b7838
    run_steps: 20
    actions_done: 20
    actions_refused: 0
    cost_usd: 0.246848
    device_takeovers: 0
    tiles_selected: 3
    tram_badge: none
    drags_tried: 0
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

## Brief (planner, THE BACKPACK NAMES: select at most FOUR Special tiles, NEVER use, approved by Steer A 16:17Z)

serves: snapshot

Record 1601 (perception-scout): the grid shows icons and counts only; a name appears only in the panel of a SELECTED tile (the 11-23 read named its stacks so: six runs, never used, no incident). THE WHOLE PERMISSION, ON THE SPECIAL TAB ONLY, never Resources (its pre-selected 5,000 Diamonds x16 tile has a LIVE Use):
(1) Bottom bar Inventory (opens on Special): a frame; write the selected tile and read its open panel (the Emote Choice Chest II): no tap.
(2) Select a tile by ONE tap on the tile BODY, in this order: the PURPLE question-mark chest (x387), the GOLD question-mark chest (x350), the chest VII (x1): THREE tiles (a fourth only if the Coordinator names it), no fifth. After each tap a frame: quote the panel's NAME, description and quantity. Clear the selection by the back arrow or a tap on the panel's own close.
(3) NEVER tap Use, Open, Sell, Merge, Split, a Details button that opens a purchase surface, or the quantity slider; a button that says Open on a chest: not pressed; a dialog with a price: STOP. Anything but the panel opening: touch nothing, take the frame, STOP.
(4) Close with the back arrow. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.30 USD.
