---
unit: training-train-batch-2026-11-26-001
regular: training
activity: troop-training
segment: 2
priority: 2
created_at: 2026-11-24T03:59:35Z
expires_at: 2026-11-26T14:00:00Z
planned_for:
not_before: 2026-11-26T11:20:00Z
window: train one batch with the free drill ground room after the collect
est_minutes: 14
serves: PL-09
chain_id: train-batch-2026-11-26
chain_seq: 1
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
---

# training

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: PL-09

## Brief (definition pointer, from the roster)

This unit is the regular `training`: Troop training - requeue any finished barracks at its highest tier. Its definition is the activity folder `_activities_/troop-training/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, TRAIN one batch with the free Drill Ground room, Steer A's order, PL-09)

serves: PL-09

DISPATCH ONLY WHEN NAMED, after the room collect unit `training-room-collect-2026-11-26-001` (about 11:20Z on 2026-11-26; the ground ends 11:08:36.6Z; the cu nightly gate run about 11:25Z to 11:35Z may delay a claim 2.4 minutes: not a fault): train only if the free room is above 10 after the collect (the Lv.26 ground added +200 room). Steer A's order: train with the free slots, the cheapest power on the board; a finished batch that fits whole first. THE SPEND: Train uses coin, food and iron: RE-READ coin, food and iron in a fresh frame (the account moves when the owner's phone moves), and write which resources and amounts from the Total cost line BEFORE pressing; a short row, a price, a diamond or an item: STOP.

Barracks order (tap points in `_records_/2026-11-22/growth/tag-index.csv`): Lv.27 (T9, 1,352 power a troop), Lv.24 (T8, 1,063), then the first idle Lv.20 where Train can be pressed.

ONE batch only: open the pistol; read 'Unit Count X of Y' IMMEDIATELY BEFORE setting the batch size (free room = Y minus X); set the quantity to that room minus 10 (less if a resource row is short); read the Total cost and time lines; press Train ONCE; write the number trained, tier, resources before and after, Total Power. NO speed-up, NO Finish Now, no Use, no Buy. A confirm dialog: Confirm only if it shows just the resource cost already read; a price, diamond, item or other app: stop.

May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.60 USD.
