---
unit: scout-midday-growth-snapshot-2026-11-23-031
regular: scout-midday
activity: perception-scout
segment: 2
priority: 1
created_at: 2026-11-23T12:22:28Z
expires_at: 2026-11-25T20:00:00Z
planned_for:
not_before: 2026-11-23T12:55:00Z
window: H1c UR hero star reads store ranking v1 read only
est_minutes: 10
serves: PL-06
chain_id: growth-snapshot-2026-11-23
chain_seq: 31
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T19:00:49Z
lease_until: 2026-11-23T19:20:49Z
result:
  status: done
  started_at: 2026-11-23T19:00:49Z
  finished_at: 2026-11-23T19:07:05Z
  duration_seconds: 376
  executor: operator
  summary: UR heroes 7 to 16 star panels read: Tesla and Mason at 5 stars (none); Violet 147/200, Williams 46/100, McGregor 21/100, Marshall 23/100, Stetmann 2/100, Swift 16/100, Adam 8/60, Morrison 2/60 with next-star stat gains; 683 universal pieces shared; all 16 UR heroes read
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/perception-scout/1900-queue-run.md and 1900-queue-run.csv; run 20261123T190049Z-cda934
  follow_up: no hero is close to its next star (Violet 147/200 nearest); no power gain figure on screen; Strategist can rank hero items by the third counter
  stats:
    target: star panels of UR heroes 7 to 9 and any left, one panel each
    achieved: 10 of 10 panels read (heroes 7 to 16)
    resources_gained: none
    points: 0
    costs: none spent; model 0.456360 USD
    verified: yes
    run_id: 20261123T190049Z-cda934
    run_steps: 35
    actions_done: 72
    actions_refused: 0
    cost_usd: 0.456360
    device_takeovers: 0
    panels_read: 10
    rules_used: 1
  stats_missing: []
  stats_warnings: []
---

# scout-midday

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: store ranking v1 weapon and hero reads

## Brief (planner for the Strategist, store ranking v1, H1c: UR heroes, UR heroes 7 to 9 and any left, read-only)

serves: PL-06

Source: `_records_/2026-11-22/strategy/0147-store-ranking-v1.md` and buys sheet `0147-store-buys.csv` (the buys wait for these reads). Read only; the Thursday hero-item window (server 2026-11-26T02:00Z to 2026-11-27T02:00Z) comes after.

Route: HEROES button (bottom bar, left), the Hero List, open one hero detail, the star and shard section (the section route is in the old H1 notes in `_records_/2026-11-22/perception-scout/2345-snapshot-protocol.md`). Use the same UR hero order as W1a and H1a (the Hero List, UR cards, left to right, top to bottom); if fewer remain, say so and stop. If more than nine UR heroes exist, write how many are left. Per hero in this unit, one panel: the tag text (name as shown), stars, shards held, the COST of the next star (shards needed) and its POWER GAIN from the star preview (preview only; never Promote or Upgrade).

PRIMARY, the unit is DONE when it is read: the star panels of UR heroes 7 to 9 and any left, one panel each; nothing else.

Up to three runs, 10 steps each.

Hazards: close menus with the bare spot (310,660) (not (400,640) after a camera shift); never tap WORLD (660,940) with a menu open low. In the Backpack the Resources tab opens with the 5,000 Diamonds x16 tile SELECTED and a live Use: select nothing, press nothing. Never press Use, Open, Convert, Sell, Buy, Upgrade, Unlock, Promote, Equip, Recruit or any shard control. Stop at a price or diamond.

Tag text: write each number's tag text beside it (name shown on the screen; for a building, name and level) and add a tag_text column; none means [G]. Write the frame time per row. Rules and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md` (K or M numbers only: write 1.1G as 1100M). Do not enqueue a chain successor.
Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`; stop with one named reason, never improvise.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.60 USD per run (the harness stops near 0.36 of it).
