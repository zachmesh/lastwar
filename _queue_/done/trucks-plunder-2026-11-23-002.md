---
unit: trucks-plunder-2026-11-23-002
regular: trucks
activity: truck-plunder
segment: 3
priority: 2
created_at: 2026-11-23T12:47:25Z
expires_at: 2026-11-23T12:00:00Z
planned_for:
not_before: 2026-11-23T18:00:00Z
window: trade truck plunder session two casualty guard before the 0200Z reset
est_minutes: 15
serves: PL-18
chain_id: plunder-2026-11-23
chain_seq: 2
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
result:
  status: expired
  started_at:
  finished_at: 2026-11-23T16:33:39Z
  duration_seconds: 
  executor:
  summary: retired by the planner: the Plunder Count reached 4 of 4 today (18 shards in four fights: 9, 3, 0 and 6; no troops wounded); it resets at 02:00Z
  claimed: []
  claimed_count: 0
  evidence: 
  follow_up: none
  stats:
  stats_missing: [target, achieved, resources_gained, costs, verified]
  stats_warnings: []
---

# trucks

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: activity: trade truck plunder, owner order OD-20261123-20

## Brief (planner, trade truck plunder with the casualty guard, session 2, owner order OD-20261123-20)

serves: PL-18

Order `_records_/retro/owner-decisions-log/od-20261123-20.md`: plunder is re-enabled for TRADE TRUCKS ONLY. The Arena, gold-trophy fights, rallies, General's Trial and attacks on bases stay forbidden. Procedure and target rule: `_activities_/truck-plunder/how-it-p1-2.md`. Plunder Count was 2 of 4 after the 15:23Z fight (two fights left today); it resets at 02:00Z. No purchase, no diamonds, no refresh unless it is labelled Free. A TIPS dialog about another device: STOP, report, never Confirm.

CASUALTY GUARD. First read the Hospital: tap it in the fresh frame (tent E about (678,510), base map `_records_/2026-11-22/growth/1030-base-map.md`; record its tag text, Lv.20 or Lv.25) and read healed, wounded and capacity, so free room is capacity minus healed minus wounded (5,306 and 364 of 7,999: 2,329 free at 15:23Z). Never press Collect, Heal or Speed Up. STOP the session if free room is under 1,000, or if two fights in a row each wound more than 100 troops.

TARGETS. Others' Trucks: tap the centre of the truck body; the card shows level, guard power, countdown, rarity and cargo. Take only a gold (UR) or purple (SSR) truck carrying a UR 500-badge shard stack in EITHER half of the cargo row (measured: right half paid 9 shards, left half 3), a guard weaker than Squad 1 (25.61M) and an arrival more than 30 minutes away. PREFER the card showing the MOST shards. No suitable target: refresh only if the button reads Free, at most three times, then stop.

FIGHT. Use Quick Plunder and press Battle once on the preparation screen; at most two fights this unit. After each fight record: the shards won; for each item the share of the cargo taken (loot over the cargo shown); the card's shard count (shards shown on the card) and the slot numbers of its stacks; troops wounded; the count; Total Power. No player names: rarity, level, guard power, cargo.

Tag text beside the Hospital numbers. Rules and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.
Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`. HAZARD: the safe empty-ground tap is the bare spot (310,660), not (400,640) after a camera shift (it selected a Barracks): WORLD then BASE first.
Cost cap, stated: 0.90 USD (the harness stops near 0.36 of it).
