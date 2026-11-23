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
serves: store ranking v1 weapon and hero reads
chain_id: growth-snapshot-2026-11-23
chain_seq: 29
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
---

# scout-midday

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: store ranking v1 weapon and hero reads

## Brief (planner for the Strategist, store ranking v1, H1a: UR heroes, the roster and UR heroes 1 to 3, read-only)

serves: store ranking v1 weapon and hero reads

Source: `_records_/2026-11-22/strategy/0147-store-ranking-v1.md` and buys sheet `0147-store-buys.csv` (the buys wait for these reads). Read only; the Thursday hero-item window (server 2026-11-26T02:00Z to 2026-11-27T02:00Z) comes after.

Route: HEROES button (bottom bar, left), the Hero List, open one hero detail, the star and shard section (the section route is in the old H1 notes in `_records_/2026-11-22/perception-scout/2345-snapshot-protocol.md`). First list every UR hero on the Hero List cards (UR rarity): tag text (name), level, stars, shard bar owned over needed, power if shown, and the roster count of UR heroes. Also read the held count of UR Hero Universal Shards (Backpack, Inventory in the bottom bar, the Special or Hero tab): exact count with the tab name. Per hero in this unit, one panel: the tag text (name as shown), stars, shards held, the COST of the next star (shards needed) and its POWER GAIN from the star preview (preview only; never Promote or Upgrade).

Up to three runs, 10 steps each.

Hazards: close menus with an empty-ground tap such as (200,610); never tap WORLD (660,940) with a menu open low. In the Backpack the Resources tab opens with the 5,000 Diamonds x16 tile SELECTED and a live Use: select nothing, press nothing. Never press Use, Open, Convert, Sell, Buy, Upgrade, Unlock, Promote, Equip, Recruit or any shard control. Stop at a price or diamond.

Tag text: write each number's tag text beside it (name shown on the screen; for a building, name and level) and add a tag_text column; none means [G]. Write the frame time per row. Rules and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md` (K or M numbers only: write 1.1G as 1100M). Do not enqueue a chain successor.
Cost cap, stated: 0.60 USD per run (the harness stops near 0.36 of it).
