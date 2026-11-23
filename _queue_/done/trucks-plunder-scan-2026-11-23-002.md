---
unit: trucks-plunder-scan-2026-11-23-002
regular: trucks
activity: truck-plunder
segment: 3
priority: 2
created_at: 2026-11-23T14:39:41Z
expires_at: 2026-11-23T15:50:00Z
planned_for:
not_before: 2026-11-23T15:20:00Z
window: one plunder scan twenty minutes apart casualty guard owner order od 20
est_minutes: 6
serves: PL-18
chain_id: plunder-scan-2026-11-23
chain_seq: 2
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T15:20:01Z
lease_until: 2026-11-23T15:40:01Z
result:
  status: done
  started_at: 2026-11-23T15:20:01Z
  finished_at: 2026-11-23T15:27:24Z
  duration_seconds: 443
  executor: operator
  summary: One fight (experiment, either half qualifies): SSR Lv.24 truck guard 8.2M with 500-badge UR shard stacks x3 in slots 2 and 3 only (left half); Quick Plunder once, Battle once, Squad 1 25.61M against 8.29M: Mission Completed, loot UR shard x3, iron 492.5K, food 492.5K, coin 311.2K; hospital before 364 wounded and free room 2,329, after unchanged (0 wounded); plunder count 1/4 to 2/4; a left-half stack pays shards
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/truck-plunder/1523-queue-run.md and 1523-queue-run.csv; runs 20261123T152013Z-d1c935, 20261123T152224Z-8c6e56, 20261123T152522Z-14a11b
  follow_up: count 2/4, 2 left today; the scribe may relax digest rule 9 from the right-half rule on this one trial; (400,640) is not safe after a camera shift: WORLD then BASE first or tap a bare spot
  stats:
    target: one Others' Trucks scan, guard first, one fight on a qualifying truck (a 500-badge stack in either half)
    achieved: 1 fight, victory, loot shard x3 iron 492.5K food 492.5K coin 311.2K, 0 wounded, count 2/4
    resources_gained: UR shard x3; iron 492.5K; food 492.5K; coin 311.2K
    points: 0
    costs: none spent; model 0.387681 USD
    verified: yes
    run_id: 20261123T152224Z-8c6e56
    run_steps: 25
    actions_done: 40
    actions_refused: 0
    cost_usd: 0.387681
    device_takeovers: 0
    rules_used: 9,10
    rule_failed: 9
    rule_gap: right-half rule: a stack in the left half paid shards
  stats_missing: []
  stats_warnings: []
---

# trucks

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: PL-18

## Brief (planner, ONE plunder scan, 20 minutes apart, coordinator 14:37Z)

serves: PL-18

Owner order OD-20261123-20 (`_records_/retro/owner-decisions-log/od-20261123-20.md`) re-enables plunder for TRADE TRUCKS ONLY; the Arena, gold-trophy fights, rallies, General's Trial and attacks on bases stay forbidden. Procedure: `_activities_/truck-plunder/how-it-p1-2.md`. The list reshuffles on every entry: look ONCE, never loop. Plunder Count: read it first, stop at 4 of 4 (1 of 4 after the 14:25Z victory).

1. Open Intercity Trade (route card), Others' Trucks. Read the list ONCE with no refresh (a refresh only if its button reads Free, at most one). Write the trucks seen and why each was skipped.
2. A TARGET is a gold (UR) or purple (SSR) truck carrying UR shard stacks with a guard under Squad 1 (25.61M at the last fight) and the shard on the right side of the cargo row. ONE-FIGHT EXCEPTION, this unit only (`_records_/2026-11-22/queue-planning/2850-plunder-left-half-experiment.md`): the UR Lv.30 truck, guard 18.9M, two 500-badge x3 stacks in slots 3 and 4 (the LEFT half), arriving about 16:00Z, qualifies if still listed, under Squad 1 and over 30 minutes out; fight by 15:30Z. Record each slot's cargo before and the loot after. Open the card (tap the truck body centre); the card decides, not the list.
3. Only if there is a target: CASUALTY GUARD first. Read the Hospital Lv.25 figures behind the orange middle button of its tag (free room = 7,999 minus 'Severely Wounded Units' minus 'Completed'; 2,329 at 14:25Z); STOP if it is under 1,000 and write 'blocked by capacity: hospital room'. Never Collect, Heal or Speed Up. Then Quick Plunder once and press Battle once: ONE fight at most per unit.
4. After a fight write troops wounded, coin, iron, food and shards won, the count and Total Power. If two fights in a row each wounded over 100, write a stop for the series.

No player names: rarity, level, guard power, cargo only. Write the scan's UTC time. The 'too soon' skip does NOT apply here: the experiment must start by 15:30Z.
Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`; the safe empty-ground tap is (400,640). A TIPS dialog about another device: STOP, report, never Confirm. No purchase, diamond spend or speed-up. Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.
Cost cap, stated: 0.40 USD (the harness stops near 0.36 of it).
