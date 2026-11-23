---
unit: building-queues-growth-fill-2026-11-23-002
regular: building-queues
activity: building-queues
segment: 1
priority: 1
created_at: 2026-11-23T07:49:13Z
expires_at: 2026-11-23T09:35:00Z
planned_for:
not_before: 2026-11-23T09:05:00Z
window: growth read then fill idle slots under the 3x rule window 09:05Z
est_minutes: 10
serves: fill idle slot
chain_id: growth-fill-2026-11-23
chain_seq: 2
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T09:07:35Z
lease_until: 2026-11-23T09:27:35Z
result:
  status: partial
  started_at: 2026-11-23T09:07:35Z
  finished_at: 2026-11-23T09:09:04Z
  duration_seconds: 89
  executor: operator
  summary: Run 20261123T090741Z-a98618 (claude-gateway/claude-sonnet-5-5, max-steps 8, completed in 5 steps), read-only. Builders 4 of 4 busy: Lv.25 Training Base x4, 1d 00:12:24 to 1d 00:12:35 left at 09:07:54Z (finish 2026-11-24T09:20:18Z to 09:20:29Z). Labs 2 of 2 busy: Unlock Oil Well Lv.0 02:34:56 left (finish about 11:43:02Z) and Defense Training VIII Lv.7 2d 22:11:03 left (finish about 2026-11-26T07:19:09Z). No Complete button, no idle builder or lab. Training queues from the 08:06Z and 08:26Z reads: Lv.30 busy (ends 2026-11-24T11:18:31Z), Lv.27 busy (ends 19:56:34Z), Lv.24 idle but Drill Ground Full blocks training (MISS, not fillable); this run's barracks read stopped when the tent tapped read Barracks Lv.20. Nothing started. HUD food 641.3M, iron 1.0G, coin 9.7M, diamonds 11,136, Total Power 150,211,809, snapshot taken. 5 steps, 12 actions done, 0 refused, 6.2 s model time per step, 0.104995 USD. No takeover. Game on the base.
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/building-queues/0107-queue-run.md and sidecar 0107-queue-run-detail.md; run 20261123T090741Z-a98618
  follow_up: first free lab about 11:43Z belongs to research-growth-convert-2026-11-23-001, first free builder 2026-11-24T09:20Z to the 2026-11-24 fills; Lv.24 slot idle but blocked by Drill Ground Full
  stats:
    target: read builders, labs and training queues, fill only idle slots under the 3x rule
    achieved: builders and labs read, all busy, nothing idle to fill; training queues taken from earlier reads, Lv.24 idle blocked by Drill Ground Full
    resources_gained: none (observe-only)
    points: 0
    costs: model 0.104995 USD; nothing spent, nothing started
    verified: yes
    blocker_category: f
    slots_idle: 1
    slots_filled: 0
    run_id: 20261123T090741Z-a98618
    run_steps: 5
    actions_done: 12
    actions_refused: 0
    model_s_per_step: 6.2
    cost_usd: 0.104995
    device_takeovers: 0
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
