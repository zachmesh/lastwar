---
unit: scout-midday-growth-snapshot-2026-11-23-027
regular: scout-midday
activity: perception-scout
segment: 2
priority: 1
created_at: 2026-11-23T12:22:14Z
expires_at: 2026-11-25T20:00:00Z
planned_for:
not_before: 2026-11-23T12:55:00Z
window: W1a exclusive weapons reads store ranking v1 read only
est_minutes: 10
serves: PL-06
chain_id: growth-snapshot-2026-11-23
chain_seq: 27
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T18:43:47Z
lease_until: 2026-11-23T19:03:47Z
result:
  status: done
  started_at: 2026-11-23T18:43:47Z
  finished_at: 2026-11-23T18:47:58Z
  duration_seconds: 251
  executor: operator
  summary: Exclusive weapons 1 to 3 read: Scamp (Carlie) Lv.10, Blade Striker (DVA) Lv.10, Unyielding Warrior (Murphy) Lv.3, all unlocked, with next-level stat gains and shard counters (441 shared across all); no power figure on screen; Backpack extra not read
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/perception-scout/1843-queue-run.md and 1843-queue-run.csv; run 20261123T184348Z-041ff8
  follow_up: universal shard count 441 inferred, Backpack read optional; weapon 2 and 3 are short of their own shards; Strategist: no power gain is shown, use the stat gains
  stats:
    target: exclusive weapons 1 to 3, one panel each
    achieved: 3 of 3 panels read
    resources_gained: none
    points: 0
    costs: none spent; model 0.295887 USD
    verified: yes
    run_id: 20261123T184348Z-041ff8
    run_steps: 23
    actions_done: 44
    actions_refused: 0
    cost_usd: 0.295887
    device_takeovers: 0
    weapons_read: 3
    universal_shards_inferred: 441
    rules_used: 1
  stats_missing: []
  stats_warnings: []
---

# scout-midday

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: store ranking v1 weapon and hero reads

## Brief (planner for the Strategist, store ranking v1, W1a: exclusive weapons, the first three weapons, read-only)

serves: PL-06

Source: `_records_/2026-11-22/strategy/0147-store-ranking-v1.md` and buys sheet `0147-store-buys.csv` (the buys wait for these reads). Read only.

The account has six exclusive weapons (use the screen, not a guide list). Route: HEROES button (bottom bar, left), the hero list, the heroes that show an exclusive weapon in list order (left to right, top to bottom), the hero detail, its exclusive weapon section. This unit reads the first three weapons in that order. Per weapon, one panel, three steps: the tag text (weapon and hero name as shown), unlocked or locked, the level, the NEXT-level SHARD COST (named shards owned over needed, and whether universal shards can fill it) and the POWER GAIN the preview shows for that next level (preview only; never Upgrade or Unlock). Also read the held count of Universal Exclusive Weapon Shards (Backpack, Inventory in the bottom bar, the Special or Hero tab; 417 on 2026-11-10): exact count with the tab name. 

PRIMARY, the unit is DONE when it is read: exclusive weapons 1 to 3, one panel each. EXTRA, optional and after the primary: the held count of Universal Exclusive Weapon Shards (a second surface, the Backpack). A missing extra does not make the unit PARTIAL.

Up to three runs, 10 steps each.

Hazards: close menus with the bare spot (310,660) (not (400,640) after a camera shift); never tap WORLD (660,940) with a menu open low. In the Backpack the Resources tab opens with the 5,000 Diamonds x16 tile SELECTED and a live Use: select nothing, press nothing. Never press Use, Open, Convert, Sell, Buy, Upgrade, Unlock, Promote, Equip, Recruit or any shard control. Stop at a price or diamond.

Tag text: write each number's tag text beside it (name shown on the screen; for a building, name and level) and add a tag_text column; none means [G]. Rules and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md` (K or M numbers only: write 1.1G as 1100M).
Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.60 USD per run (the harness stops near 0.36 of it).
