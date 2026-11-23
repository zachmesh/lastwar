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
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
---

# trucks

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: PL-18

## Brief (planner, ONE plunder scan, 20 minutes apart, coordinator 14:37Z)

serves: PL-18

Owner order OD-20261123-20 (`_records_/retro/owner-decisions-log/od-20261123-20.md`) re-enables plunder for TRADE TRUCKS ONLY; the Arena, gold-trophy fights, rallies, General's Trial and attacks on bases stay forbidden. Procedure: `_activities_/truck-plunder/how-it-p1-2.md`; reference run `_records_/2026-11-22/truck-plunder/1405-queue-run.md`. The list RESHUFFLES on every entry, so this unit looks ONCE and never loops; the next scan is a separate unit 20 minutes later. Plunder Count was 1 of 4 after the 14:25Z victory; read it first, stop at 4 of 4.

1. Open Intercity Trade (the left-column vehicle icon), Others' Trucks. Read the list ONCE with no refresh (a refresh only if its button reads Free, at most one). Write the trucks seen by rarity and why each was skipped.
2. A TARGET is a gold (UR) or purple (SSR) truck carrying UR shard stacks with a guard under Squad 1 (25.61M at the last fight) and the shard on the right side of the cargo row. Open the card by tapping the centre of the truck body; the opened card decides, not the list.
3. Only if there is a target: CASUALTY GUARD first. The Hospital Lv.25 figures sit behind the orange middle button of its tag ('Severely Wounded Units' 364/7999 and 'Completed' 5306 at 14:25Z, free room 2,329): free room = 7,999 minus both; STOP if it is under 1,000 and write 'blocked by capacity: hospital room'. Never Collect, Heal or Speed Up. Then Quick Plunder once and press Battle once: ONE fight at most per unit.
4. After a fight write troops wounded, coin, iron, food and shards won, the count and Total Power. If two fights in a row each wounded over 100, write a stop for the series.

No player names: rarity, level, guard power and cargo only. Write the UTC time of the scan. If another scan unit finished under 15 minutes ago, close this one skipped with the words 'too soon': the list reshuffles and scans closer than that only repeat each other.
Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `2700-routes.csv`); the safe empty-ground tap is (400,640). A TIPS dialog about another device: STOP, report, never Confirm. No purchase, diamond spend or speed-up. Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`. No chain successor.
Cost cap, stated: 0.40 USD (the harness stops near 0.36 of it).
