---
unit: trucks-plunder-scan-2026-11-23-003
regular: trucks
activity: truck-plunder
segment: 3
priority: 2
created_at: 2026-11-23T14:39:41Z
expires_at: 2026-11-23T16:40:00Z
planned_for:
not_before: 2026-11-23T15:40:00Z
window: one plunder scan twenty minutes apart casualty guard owner order od 20
est_minutes: 6
serves: PL-18
chain_id: plunder-scan-2026-11-23
chain_seq: 3
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T15:59:36Z
lease_until: 2026-11-23T16:19:36Z
result:
  status: done
  started_at: 2026-11-23T15:59:36Z
  finished_at: 2026-11-23T16:04:34Z
  duration_seconds: 298
  executor: operator
  summary: One fight: SSR Lv.30 truck guard 22.2M with two 500-badge x3 stacks in slots 2 and 3 (left half); Quick Plunder once, Battle once, Squad 1 25.61M against 22.29M: Mission Completed, loot iron 761.5K, food 761.5K, coin 486.2K, purple chest, two puzzle pieces, NO 500-badge shard (0 of 6); hospital before 364 wounded and free room 2,329, after unchanged (0 wounded); plunder count 2/4 to 3/4; the same left-half layout paid shard x3 in fight 2, so the half does not decide the shard payout
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/truck-plunder/1600-queue-run.md and 1600-queue-run.csv; runs 20261123T155946Z-369d6d, 20261123T160041Z-3a91df, 20261123T160327Z-a12f73
  follow_up: count 3/4, one fight left today; scribe: shard payout varies with the same layout (fight 2 paid x3 of 6, fight 3 paid 0 of 6), keep the rule 'either half qualifies' but expect variance; the base is panned by the fight run: next run restores with WORLD then BASE
  stats:
    target: one Others' Trucks scan, guard first, one fight on a truck with a 500-badge stack in either half, most shards preferred
    achieved: 1 fight, victory, loot iron 761.5K food 761.5K coin 486.2K chest and 2 puzzle pieces, 0 shards, 0 wounded, count 3/4
    resources_gained: iron 761.5K; food 761.5K; coin 486.2K; purple chest x1; puzzle piece x2
    points: 0
    costs: none spent; model 0.350671 USD
    verified: yes
    run_id: 20261123T160041Z-3a91df
    run_steps: 22
    actions_done: 34
    actions_refused: 0
    cost_usd: 0.350671
    device_takeovers: 0
    rules_used: 9,10
    rule_failed: none
    rule_gap: shard payout varies with the same left-half layout
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
