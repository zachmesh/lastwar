---
unit: building-queues-growth-fill-2026-11-23-004
regular: building-queues
activity: building-queues
segment: 1
priority: 1
created_at: 2026-11-23T07:49:16Z
expires_at: 2026-11-23T10:35:00Z
planned_for:
not_before: 2026-11-23T10:05:00Z
window: growth read then fill idle slots under the 3x rule window 10:05Z
est_minutes: 10
serves: fill idle slot
chain_id: growth-fill-2026-11-23
chain_seq: 4
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T10:25:13Z
lease_until: 2026-11-23T10:45:13Z
result:
  status: partial
  started_at: 2026-11-23T10:25:13Z
  finished_at: 2026-11-23T10:28:20Z
  duration_seconds: 187
  executor: operator
  summary: Growth read run 20261123T102543Z-fa696e (claude-gateway/claude-sonnet-5-5, max-steps 11, 10 steps, claimed 10:25:13Z inside the 10:35Z window): builders 4 of 4 busy (Training Base to Lv.25, 22:54:22 to 22:54:32 left, finish about 2026-11-24T09:20:13Z), labs 2 of 2 busy (Unlock Oil Well 01:16:54 left, frees about 11:42:54Z; Defense Training VIII 2d 20:53:01), no COMPLETE button; nothing idle, nothing started; barracks training queues not read (tents tagged Lv.30, Lv.20, Lv.20; Lv.24 and the Lv.27 clock-bubble tents not found); no pistol tapped, nothing spent.
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/building-queues/1026-queue-run.md and 1026-queue-run.csv; run 20261123T102543Z-fa696e
  follow_up: first free lab about 11:43Z belongs to research-growth-convert-2026-11-23-001, first free builder 2026-11-24T09:20Z to the 2026-11-24 fills; training queue read needs a fixed route to the Lv.24 and Lv.27 barracks
  stats:
    target: read builders, labs and training queues, fill only idle slots
    achieved: builders and labs read, all busy, nothing to fill; training queues not read
    resources_gained: none (observe-only)
    points: 0
    costs: model 0.163455 USD; nothing spent or started
    verified: yes
    blocker_category: c
    slots_idle: 0
    slots_filled: 0
    run_id: 20261123T102543Z-fa696e
    run_steps: 10
    actions_done: 19
    actions_refused: 0
    model_s_per_step: 8.2
    cost_usd: 0.163455
    device_takeovers: 0
    rules_used: R1,R4,R5,R7
    rule_failed: none
    rule_gap: No rule identifies which tent is which barracks; the camera drifts and tags show only after a tap.
  stats_missing: []
  stats_warnings: []
---

# building-queues

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

## Brief (planner, growth read-then-fill, decision record 2350, strategy v2.0)

serves: fill idle slot

Rules, reserves, red lines and the snap command are in `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`. Reserves: food 100M, iron 150M, coin 10M, diamonds untouched, duel-day reservation. Snap takes only K or M numbers: write 1.1G as 1100M.

Read the builders, then the labs, then the training queues. Fill ONLY idle slots, each start costing at most one third of EACH needed stock and leaving the reserves. Never cancel, replace or reorder a running item. No speed-up, Finish Now, purchase or diamond spend. An idle slot at the read is a MISS: record the slot and the time.

COIN HOLD LIFTED for ranked sinks (coordinator, inventory read 0009), but only the conversion-and-spend units convert and spend: this fill converts nothing and starts nothing coin-costly. The first free lab (about 11:43Z) belongs to unit `research-growth-convert-2026-11-23-001` and the first free builder (2026-11-24T09:20Z) to the 2026-11-24 fills: start nothing in them. Shards, medals, ore, blueprints and chests stay untouched.

PRESS COMPLETE the moment a research or a build finishes: a finished research neither banks its power nor frees the lab until then.

When a builder is idle and released: Drill Ground lowest first, then barracks Lv.24 to 27 (Lv.30 only for tier unlocks), then Oil Well levels 1 to 9 (food and iron only; collect the oil twice a day). Age of Oil and HQ 31 stay off. Labs: one on Special Forces VIII or IX, the other on Drill Ground Expansion, then Extra Barracks (only if fewer than four), Coin Output V, Garage 1, the Alliance Duel tree; never cancel a running one.

TRAIN: never retry the Hospital Collect; it is all-or-nothing, needs at least 5,306 free slots at once and only repeats the toast. When Drill Ground slots open, collect finished batches, then fill with new T10 from surplus food and iron. No fights that wound troops while full.

Run one growth unit at a time. Do not enqueue a chain successor.

Cost cap, stated: 0.60 USD (the harness stops near 0.36 of it).
