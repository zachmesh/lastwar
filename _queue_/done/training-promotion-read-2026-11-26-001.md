---
unit: training-promotion-read-2026-11-26-001
regular: training
activity: troop-training
segment: 1
priority: 1
created_at: 2026-11-26T15:30:07Z
expires_at: 2026-11-27T02:00:00Z
planned_for:
not_before: 2026-11-26T15:42:00Z
window: promotion read, read only (watchdog 15:28z, h13 h14 h15 h37)
est_minutes: 10
serves: PL-09
chain_id: promotion-read-2026-11-26
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-26T15:47:47Z
lease_until: 2026-11-26T16:07:47Z
result:
  status: done
  started_at: 2026-11-26T15:47:47Z
  finished_at: 2026-11-26T15:52:38Z
  duration_seconds: 291
  executor: operator
  summary: Promotion read: the Lv.30 barracks' pistol only toasts 'Drill Ground Full: Unable to add more units.'; the Lv.27 barracks opened Train Units (Lv.7 1,116 and Lv.8 2,415 with green up-arrow badges, Lv.9 2,604, Lv.10 locked 34.3K; 726 troops max costs 4.1M food and 4.1M iron, no coin; Train and Finish Now 1d 10:19:35); no tab or control named Promote (an unnamed grey up-arrow button beside the cost row, not pressed): the panel's text is the result; HUD food 46.6M, iron 643.2M, coin 11.5M unmoved; nothing pressed beyond opening and closing; drags 0. state_change: no. state_read: Train Units panel of the Lv.27 barracks; no Promote tab; Lv.30 barracks toast Drill Ground Full | step 13 | 15:51:16Z
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/troop-training/1547-queue-run.md and 1547-queue-run.csv; run 20261126T154921Z-8456e8
  state_read: Train Units panel of the Lv.27 barracks; no Promote tab; Lv.30 barracks toast Drill Ground Full | step 13 | 15:51:16Z
  state_change: no
  follow_up: the grey up-arrow button beside the cost row is unnamed (the possible promote shortcut: a named read needs Steer A's word); the Lv.30 barracks is Full
  stats:
    target: read the Promote view costs and tiers
    achieved: read the panel: no Promote tab exists
    resources_gained: none
    points: 0
    costs: none spent; model 0.33975 USD
    verified: yes
    run_id: 20261126T154921Z-8456e8
    run_steps: 24
    actions_done: 11
    actions_refused: 0
    cost_usd: 0.33975
    device_takeovers: 0
    claims: 0
    lv27_lv7: 1116
    lv27_lv8: 2415
    lv27_lv9: 2604
    max_batch: 726
    food_cost_max: 4.1M
    iron_cost_max: 4.1M
    tram_badge: not read
    drags_tried: 0
    rules_used: 1,2
  stats_missing: []
  stats_warnings: []
---

# training

Serves: PL-09

## Brief (definition pointer, from the roster)

One-off promotion read, NOT a training run. Definition `_activities_/troop-training/` (its `rule-digest.md` first); routes `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`.

## Brief (planner, PROMOTION READ: watchdog 15:28Z, register H13, H14, H15, H37; plan reason: the 2.75M power lever)

serves: PL-09

READ ONLY: NO press of any Promote, Train, Heal, Collect, speed-up or buy button.
Route: the `barracks` row of `_records_/2026-11-22/queue-planning/2700-routes.csv`: ONE barracks per fresh frame, the Lv.30 barracks first (the T10 one), then at most ONE other. BUTTON ROW HAZARD as the route says: verify the pistol glyph in a frame before the tap (a stray tap once opened Building Details and another the world map: close by the back arrow or X, and write it); NEVER the green up arrow (the upgrade shortcut).
Press the pistol ONCE. Write the toast if any ('Drill Ground Full' = a finished batch waits: the Full state). If the Train Units panel opens: look for a tab or control NAMED 'Promote' (read the word in a frame) and tap it ONCE; if none is named Promote: write the panel's text and STOP. In the Promote view write: the troop counts by tier (T1 to T10); which tier each promotion goes to; DRAG THE COST LIST until EVERY row is visible and write every cost row (food, iron, coin, any other) for ONE troop and for the largest batch offered; whether the view opens while the Drill Ground is Full and the barracks is busy (H13, H14); any capacity, slot or idle-barracks line. Close by the X or back arrow: NEVER a Promote confirm.
Write the HUD food, iron and coin before and after: they must not move.
CLOSE by `_records_/2026-11-22/queue-planning/3170-closing-rule-done-and-partial.md`: DONE for the panels read (`--state-change no`, a `state_read:` line); else PARTIAL.
FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.80 USD.
