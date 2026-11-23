---
unit: trucks-plunder-scan-2026-11-23-004
regular: trucks
activity: truck-plunder
segment: 3
priority: 2
created_at: 2026-11-23T14:39:43Z
expires_at: 2026-11-23T17:00:00Z
planned_for:
not_before: 2026-11-23T16:00:00Z
window: one plunder scan twenty minutes apart casualty guard owner order od 20
est_minutes: 6
serves: PL-18
chain_id: plunder-scan-2026-11-23
chain_seq: 4
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T16:22:22Z
lease_until: 2026-11-23T16:42:22Z
result:
  status: done
  started_at: 2026-11-23T16:22:22Z
  finished_at: 2026-11-23T16:27:23Z
  duration_seconds: 301
  executor: operator
  summary: One fight: SSR Lv.29 truck guard 13.8M with three 500-badge x3 stacks (slots 1, 3, 5); Quick Plunder once, Battle once, Squad 1 25.61M against 13.84M: Mission Completed, loot shard x6 of 9, iron 598.7K, food 598.7K, coin 381.1K, scroll x1; 0 wounded; count 4/4
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/truck-plunder/1623-queue-run.md and 1623-queue-run.csv; runs 20261123T162225Z-59f1b2, 20261123T162319Z-7e8103, 20261123T162536Z-6524f5
  follow_up: plunder closed for today (4/4); scribe: four fights paid x9, x3 of 6, 0 of 6, x6 of 9, the half does not decide the payout; hospital 364/7999 unchanged after four fights
  stats:
    target: one Others' Trucks scan, guard first, one fight on a truck with a 500-badge stack in either half, most shards preferred
    achieved: 1 fight, victory, shard x6 of 9, iron 598.7K food 598.7K coin 381.1K scroll x1, 0 wounded, count 4/4
    resources_gained: 500-badge shard x6; iron 598.7K; food 598.7K; coin 381.1K; scroll x1
    points: 0
    costs: none spent; model 0.311920 USD
    verified: yes
    run_id: 20261123T162319Z-7e8103
    run_steps: 22
    actions_done: 40
    actions_refused: 0
    cost_usd: 0.311920
    device_takeovers: 0
    rules_used: 9,10
  stats_missing: []
  stats_warnings: []
---

# trucks

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: PL-18

## Brief (planner, ONE plunder scan, 20 minutes apart, coordinator 14:37Z)

serves: PL-18

Order OD-20261123-20 re-enables plunder for TRADE TRUCKS ONLY; the Arena, gold-trophy fights, rallies, General's Trial and attacks on bases stay forbidden. Procedure: `_activities_/truck-plunder/how-it-p1-2.md`. The list reshuffles on every entry: look ONCE, never loop. Plunder Count: read it first, stop at 4 of 4.

1. Open Intercity Trade, Others' Trucks. Read the list ONCE with no refresh (a refresh only if its button reads Free, at most one). Write the trucks seen by rarity and why each was skipped.
2. A TARGET is a gold (UR) or purple (SSR) truck carrying a UR 500-badge shard stack in EITHER half of the cargo row (measured: right half paid 9 shards, left half 3), with a guard under Squad 1 (25.61M) and an arrival more than 30 minutes away. PREFER the card showing the MOST shards. Open the card (tap the truck body centre); the card decides, not the list.
3. Only if there is a target: CASUALTY GUARD first. Read the Hospital Lv.25 figures behind the orange middle button of its tag (free room = 7,999 minus 'Severely Wounded Units' minus 'Completed'; 2,329 at 15:23Z); STOP if it is under 1,000 and write 'blocked by capacity: hospital room'. Never Collect, Heal or Speed Up. Then Quick Plunder once and press Battle once: ONE fight at most per unit.
4. Per fight record: the shards won; for each item the share of the cargo taken (loot over the cargo shown); the card's shard count (shards shown on the card) and the slot numbers of its stacks; troops wounded; the count; Total Power. If two fights in a row each wounded over 100, write a stop for the series.

No player names: rarity, level, guard power and cargo only. Write the scan's UTC time. If another scan unit finished under 15 minutes ago, close this one skipped: 'too soon'.
Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`; the safe empty-ground tap is the bare spot (310,660), not (400,640) after a camera shift (it selected a Barracks): WORLD then BASE first. A TIPS dialog about another device: STOP, report, never Confirm. No purchase, diamond spend or speed-up. Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.
Cost cap, stated: 0.40 USD (the harness stops near 0.36 of it).
