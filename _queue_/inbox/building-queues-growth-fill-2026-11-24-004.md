---
unit: building-queues-growth-fill-2026-11-24-004
regular: building-queues
activity: building-queues
segment: 1
priority: 2
created_at: 2026-11-23T07:55:32Z
expires_at: 2026-11-24T10:35:00Z
planned_for:
not_before: 2026-11-24T10:20:00Z
window: growth read then fill idle slots window 11-24T09:55Z
est_minutes: 10
serves: fill idle slot
chain_id: growth-fill-2026-11-24
chain_seq: 4
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
---

# building-queues

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

## Brief (planner, growth read-then-fill, decision record 2350, strategy v2.0)

serves: fill idle slot

Rules, reserves, red lines and the snap command are in `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`. Reserves: food 100M, iron 150M, coin 10M, diamonds untouched, duel-day reservation. Snap takes only K or M numbers: write 1.1G as 1100M.

Read the builders, then the labs, then the training queues. Fill ONLY idle slots, each start costing at most one third of EACH needed stock and leaving the reserves. Never cancel, replace or reorder a running item. No speed-up, Finish Now, purchase or diamond spend. An idle slot at the read is a MISS: record the slot and the time.

COIN HOLD LIFTED for ranked sinks. The builders freeing at 2026-11-24T09:20Z belong to the conversion-and-spend units `building-queues-growth-convert-2026-11-24-001` and `-002` (from 09:22Z): this fill reads the builders, presses COMPLETE, collects finished batches when slots open, and records any builder idle for more than one pass as a MISS with the time. It converts nothing and starts nothing.

PRESS COMPLETE the moment a research or a build finishes: a finished research neither banks its power nor frees the lab until then.

When a builder is idle and released: Drill Ground lowest first, then barracks Lv.24 to 27 (Lv.30 only for tier unlocks), then Oil Well levels 1 to 9 (food and iron only; collect the oil twice a day). Age of Oil and HQ 31 stay off. Labs: one on Special Forces VIII or IX, the other on the node the Strategist names (Drill Ground Expansion is [G], never seen on screen; Extra Barracks is MAX), then Coin Output V, Garage 1, the Alliance Duel tree; never cancel a running one.

TRAIN: never retry the Hospital Collect; it is all-or-nothing, needs at least 5,306 free slots at once and only repeats the toast. When Drill Ground slots open, collect finished batches, then fill with new T10 from surplus food and iron. No fights that wound troops while full.

Run one growth unit at a time. Do not enqueue a chain successor.

Tag text: beside every number from a building panel write its tag text (name and level above the building after the tap; `_records_/2026-11-22/coach/0255-tag-text-check.md`); none means [G]. Add a tag_text column.
Cost cap, stated: 0.60 USD (the harness stops near 0.36 of it).
