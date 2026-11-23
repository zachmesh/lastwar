---
unit: trucks-plunder-2026-11-23-001
regular: trucks
activity: truck-plunder
segment: 3
priority: 2
created_at: 2026-11-23T12:47:23Z
expires_at: 2026-11-23T18:00:00Z
planned_for:
not_before: 2026-11-23T13:30:00Z
window: trade truck plunder session one casualty guard owner order OD 20
est_minutes: 15
serves: PL-18
chain_id: plunder-2026-11-23
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T14:05:02Z
lease_until: 2026-11-23T14:25:02Z
result:
  status: partial
  started_at: 2026-11-23T14:05:02Z
  finished_at: 2026-11-23T14:30:58Z
  duration_seconds: 1556
  executor: operator
  summary: Trade truck plunder session 1, seven runs (claude-gateway/claude-sonnet-5-5; claimed 14:05:02Z): hospital treatment panel (tag Hospital Lv.25) 364 wounded, 5,306 completed, capacity 7,999, free room 2,329 before and after; one fight at 14:25:40Z on a UR Lv.30 truck (guard 21.0M, UR shard stacks in the right half): Squad 1 25.61M against 21.06M, Quick Plunder once and Battle once, Mission Completed: iron +951.8K, food +951.8K, coin +607.5K, UR shard x9, no troops wounded, plunder count 1/4; at 14:29Z five more gold and purple trucks all failed a check, so no second fight; no Collect or Heal; no player names recorded.
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/truck-plunder/1405-queue-run.md and 1405-queue-run.csv; growth/ledger.csv row 14:25:40Z; runs 20261123T140502Z-37b59f, 20261123T141548Z-ab7c4d, 20261123T141932Z-100841, 20261123T142109Z-6f85a6, 20261123T142249Z-62e6dc, 20261123T142439Z-807dc6, 20261123T142807Z-1a0e07
  follow_up: a second plunder session after the truck list reshuffles (count 1/4, unit window to 18:00Z); the guard stands (stop under 1,000 free room or two fights each wounding over 100)
  stats:
    target: trade truck plunder with the casualty guard, at most two fights
    achieved: one fight won (victory, 0 troops wounded); no second target passed
    resources_gained: iron +951.8K, food +951.8K, coin +607.5K, UR shard x9
    points: 0
    costs: model 1.112144 USD in seven runs; no troops wounded; no resources spent
    verified: yes
    blocker_category: c
    run_id: 20261123T142439Z-807dc6
    run_steps: 94
    actions_done: 120
    actions_refused: 0
    model_s_per_step: 6.5
    cost_usd: 1.112144
    device_takeovers: 0
    rules_used: R1,R9,R10
    rule_failed: none
    rule_gap: The hospital figures sit behind the orange middle button of Hospital Lv.25, not Building Details; the truck list reshuffles on every entry.
  stats_missing: []
  stats_warnings: [duration exceeds 15-minute unit cap]
---

# trucks

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: activity: trade truck plunder, owner order OD-20261123-20

## Brief (planner, trade truck plunder with the casualty guard, session 1, owner order OD-20261123-20)

serves: PL-18

Order `_records_/retro/owner-decisions-log/od-20261123-20.md`: plunder is re-enabled for TRADE TRUCKS ONLY. The Arena, gold-trophy fights, rallies, General's Trial and attacks on bases stay forbidden. Procedure and target rule: `_activities_/truck-plunder/how-it-p1-2.md`; entry as in `_records_/2026-11-22/truck-plunder/0953-queue-run.md` (Intercity Trade, the left-column vehicle icon). Today's Plunder Count read 0/4; it resets at 02:00Z. No purchase, no diamonds, no refresh unless it is labelled Free. If a TIPS dialog says another device is active, STOP and report; never Confirm.

CASUALTY GUARD. First read the Hospital: tap it in the fresh base frame (base map `_records_/2026-11-22/growth/1030-base-map.md`: tent E, about (678,510); record its tag text, the tag may read Hospital Lv.20 or Lv.25) and read healed, wounded and capacity, so free room is capacity minus healed minus wounded (about 5,306 healed and 364 wounded of 7,999 is about 2,300 free). Never press Collect, Heal or Speed Up. STOP the session if free room is under 1,000, or if two fights in a row each wound more than 100 troops.

TARGETS. Others' Trucks: tap the centre of the truck body; the card shows level, guard power, countdown, rarity and cargo. Take only a gold (UR) or purple (SSR) truck carrying UR shard stacks (the purple 500-point badge), a guard weaker than Squad 1 (24.96M, lower is better), the shard on the right side of the cargo row. No suitable target: refresh only if the button reads Free, at most three times, then stop and record.

FIGHT. Use Quick Plunder (fights on the spot with the preset squad) and press Battle once on the preparation screen; at most two fights this unit. After each fight read troops wounded, coin and shards won, and Total Power. Do not write player names; write rarity, level, guard power and cargo.

Tag text: the Hospital tag text beside its numbers; none means [G]. Rules and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`. No chain successor.
Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`; stop with one named reason, never improvise.
Cost cap, stated: 0.90 USD (the harness stops near 0.36 of it).
