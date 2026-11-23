---
unit: trucks-plunder-2026-11-23-002
regular: trucks
activity: truck-plunder
segment: 3
priority: 2
created_at: 2026-11-23T12:47:25Z
expires_at: 2026-11-24T01:30:00Z
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
---

# trucks

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: activity: trade truck plunder, owner order OD-20261123-20

## Brief (planner, trade truck plunder with the casualty guard, session 2, owner order OD-20261123-20)

serves: PL-18

Order `_records_/retro/owner-decisions-log/od-20261123-20.md`: plunder is re-enabled for TRADE TRUCKS ONLY. The Arena, gold-trophy fights, rallies, General's Trial and attacks on bases stay forbidden. Procedure and target rule: `_activities_/truck-plunder/how-it-p1-2.md`; entry as in `_records_/2026-11-22/truck-plunder/0953-queue-run.md` (Intercity Trade, the left-column vehicle icon). Today's Plunder Count read 0/4; it resets at 02:00Z. No purchase, no diamonds, no refresh unless it is labelled Free. If a TIPS dialog says another device is active, STOP and report; never Confirm.

CASUALTY GUARD. First read the Hospital: tap it in the fresh base frame (base map `_records_/2026-11-22/growth/1030-base-map.md`: tent E, about (678,510); record its tag text, the tag may read Hospital Lv.20 or Lv.25) and read healed, wounded and capacity, so free room is capacity minus healed minus wounded (about 5,306 healed and 364 wounded of 7,999 is about 2,300 free). Never press Collect, Heal or Speed Up. STOP the session if free room is under 1,000, or if two fights in a row each wound more than 100 troops.

TARGETS. Others' Trucks: tap the centre of the truck body; the card shows level, guard power, countdown, rarity and cargo. Take only a gold (UR) or purple (SSR) truck carrying UR shard stacks (the purple 500-point badge), a guard weaker than Squad 1 (24.96M, lower is better), the shard on the right side of the cargo row. No suitable target: refresh only if the button reads Free, at most three times, then stop and record.

FIGHT. Use Quick Plunder (fights on the spot with the preset squad) and press Battle once on the preparation screen; at most two fights this unit. After each fight read troops wounded, coin and shards won, and Total Power. Do not write player names; write rarity, level, guard power and cargo.

Tag text: the Hospital tag text beside its numbers; none means [G]. Rules and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`. No chain successor.
Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`; stop with one named reason, never improvise.
Cost cap, stated: 0.90 USD (the harness stops near 0.36 of it).
