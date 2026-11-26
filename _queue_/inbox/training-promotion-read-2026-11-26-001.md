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
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
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
