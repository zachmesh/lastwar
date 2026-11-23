---
unit: scout-midday-growth-snapshot-2026-11-23-029
regular: scout-midday
activity: perception-scout
segment: 2
priority: 1
created_at: 2026-11-23T12:22:22Z
expires_at: 2026-11-25T20:00:00Z
planned_for:
not_before: 2026-11-23T12:55:00Z
window: H1a UR hero star reads store ranking v1 read only
est_minutes: 10
serves: PL-06
chain_id: growth-snapshot-2026-11-23
chain_seq: 29
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T18:53:09Z
lease_until: 2026-11-23T19:13:09Z
result:
  status: done
  started_at: 2026-11-23T18:53:09Z
  finished_at: 2026-11-23T18:57:37Z
  duration_seconds: 268
  executor: operator
  summary: 16 UR cards read (Lv.150 x13, 145, 133, 125; stars 3 to 5; squads 1 to 3); heroes 1 to 3 at 5 stars show no shard bar or next-star cost; list cards carry no shard bar; Backpack universal shard count not found
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/perception-scout/1853-queue-run.md and 1853-queue-run.csv; run 20261123T185309Z-a636cc
  follow_up: a star shard bar may exist only below 5 stars: 030 and 031 test heroes 4, 5, 6 and 7 to 9; 441 on the weapon tab is the only universal-shard figure
  stats:
    target: the UR roster on the Hero List cards; extras: star panels 1 to 3, UR Hero Universal Shards
    achieved: roster of 16 UR cards read, star panels 1 to 3 read, Backpack count not found
    resources_gained: none
    points: 0
    costs: none spent; model 0.328692 USD
    verified: yes
    run_id: 20261123T185309Z-a636cc
    run_steps: 26
    actions_done: 45
    actions_refused: 0
    cost_usd: 0.328692
    device_takeovers: 0
    ur_heroes: 16
    rules_used: 1
  stats_missing: []
  stats_warnings: []
---

# scout-midday

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: store ranking v1 weapon and hero reads

## Brief (planner for the Strategist, store ranking v1, H1a: UR heroes, the roster and UR heroes 1 to 3, read-only)

serves: PL-06

Source: `_records_/2026-11-22/strategy/0147-store-ranking-v1.md` and buys sheet `0147-store-buys.csv` (the buys wait for these reads). Read only.

Route: HEROES button (bottom bar, left), the Hero List, open one hero detail, the star and shard section (the section route is in the old H1 notes in `_records_/2026-11-22/perception-scout/2345-snapshot-protocol.md`). First list every UR hero on the Hero List cards (UR rarity): tag text (name), level, stars, shard bar owned over needed, power if shown, and the roster count of UR heroes. Also read the held count of UR Hero Universal Shards (Backpack, Inventory in the bottom bar, the Special or Hero tab): exact count with the tab name. Per hero in this unit, one panel: the tag text (name as shown), stars, shards held, the COST of the next star (shards needed) and its POWER GAIN from the star preview (preview only; never Promote or Upgrade).

PRIMARY, the unit is DONE when it is read: the UR roster on the Hero List cards (one surface). EXTRAS, optional and in this order: the star panels of UR heroes 1 to 3; the held count of UR Hero Universal Shards (the Backpack, a second surface). A missing extra does not make the unit PARTIAL.

Up to three runs, 10 steps each.

Hazards: close menus with the bare spot (310,660) (not (400,640) after a camera shift); never tap WORLD (660,940) with a menu open low. In the Backpack the Resources tab opens with the 5,000 Diamonds x16 tile SELECTED and a live Use: select nothing, press nothing. Never press Use, Open, Convert, Sell, Buy, Upgrade, Unlock, Promote, Equip, Recruit or any shard control. Stop at a price or diamond.

Tag text: write each number's tag text beside it (name shown on the screen; for a building, name and level) and add a tag_text column; none means [G]. Rules and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md` (K or M numbers only: write 1.1G as 1100M).
Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.60 USD per run (the harness stops near 0.36 of it).
