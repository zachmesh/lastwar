---
unit: scout-midday-growth-snapshot-2026-11-23-028
regular: scout-midday
activity: perception-scout
segment: 2
priority: 1
created_at: 2026-11-23T12:22:18Z
expires_at: 2026-11-25T20:00:00Z
planned_for:
not_before: 2026-11-23T12:55:00Z
window: W1b exclusive weapons reads store ranking v1 read only
est_minutes: 10
serves: PL-06
chain_id: growth-snapshot-2026-11-23
chain_seq: 28
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T18:48:17Z
lease_until: 2026-11-23T19:08:17Z
result:
  status: done
  started_at: 2026-11-23T18:48:17Z
  finished_at: 2026-11-23T18:52:40Z
  duration_seconds: 263
  executor: operator
  summary: Weapons 4 to 6: Rocket Shadow (Kimberly) Lv.2 unlocked, Magnetic Expert (Tesla) Lv.1 unlocked, Thunder (Swift) locked needing Hero Tier 5 Stars; next-level gains and counters read; read-only
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/perception-scout/1848-queue-run.md and 1848-queue-run.csv; run 20261123T184818Z-a83077
  follow_up: six weapons now known: Carlie Lv.10, DVA Lv.10, Murphy Lv.3, Kimberly Lv.2, Tesla Lv.1, Swift locked; cards 4 5 8 to 13 have no weapon tab
  stats:
    target: exclusive weapons 4 to 6, one panel each
    achieved: 3 of 3 panels read (the third locked)
    resources_gained: none
    points: 0
    costs: none spent; model 0.342974 USD
    verified: yes
    run_id: 20261123T184818Z-a83077
    run_steps: 26
    actions_done: 62
    actions_refused: 0
    cost_usd: 0.342974
    device_takeovers: 0
    weapons_read: 3
    rules_used: 1
  stats_missing: []
  stats_warnings: []
---

# scout-midday

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: store ranking v1 weapon and hero reads

## Brief (planner for the Strategist, store ranking v1, W1b: exclusive weapons, weapons four to six, read-only)

serves: PL-06

Source: `_records_/2026-11-22/strategy/0147-store-ranking-v1.md` and buys sheet `0147-store-buys.csv` (the buys wait for these reads). Read only; the Thursday hero-item window (server 2026-11-26T02:00Z to 2026-11-27T02:00Z) comes after.

The account has six exclusive weapons (a guide lists Kimberly, DVA, Tesla, Murphy, Carlie and Swift, unverified, so use the screen). Route: HEROES button (bottom bar, left), the hero list, the heroes that show an exclusive weapon in list order (left to right, top to bottom), the hero detail, its exclusive weapon section. This unit reads weapons four to six in that order; if fewer exist, say so and stop. Per weapon, one panel, three steps: the tag text (weapon and hero name as shown), unlocked or locked, the level, the NEXT-level SHARD COST (named shards owned over needed, and whether universal shards can fill it) and the POWER GAIN the preview shows for that next level (preview only; never Upgrade or Unlock). 

PRIMARY, the unit is DONE when it is read: exclusive weapons 4 to 6, one panel each; nothing else. A missing panel because fewer weapons exist is DONE.

Up to three runs, 10 steps each.

Hazards: close menus with the bare spot (310,660) (not (400,640) after a camera shift); never tap WORLD (660,940) with a menu open low. In the Backpack the Resources tab opens with the 5,000 Diamonds x16 tile SELECTED and a live Use: select nothing, press nothing. Never press Use, Open, Convert, Sell, Buy, Upgrade, Unlock, Promote, Equip, Recruit or any shard control. Stop at a price or diamond.

Tag text: write each number's tag text beside it (name shown on the screen; for a building, name and level) and add a tag_text column; none means [G]. Write the frame time per row. Rules and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md` (K or M numbers only: write 1.1G as 1100M). Do not enqueue a chain successor.
Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`; stop with one named reason, never improvise.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.60 USD per run (the harness stops near 0.36 of it).
