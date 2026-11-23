---
unit: scout-midday-growth-snapshot-2026-11-23-030
regular: scout-midday
activity: perception-scout
segment: 2
priority: 1
created_at: 2026-11-23T12:22:25Z
expires_at: 2026-11-25T20:00:00Z
planned_for:
not_before: 2026-11-23T12:55:00Z
window: H1b UR hero star reads store ranking v1 read only
est_minutes: 10
serves: PL-06
chain_id: growth-snapshot-2026-11-23
chain_seq: 30
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T18:58:49Z
lease_until: 2026-11-23T19:18:49Z
result:
  status: done
  started_at: 2026-11-23T18:58:49Z
  finished_at: 2026-11-23T19:00:32Z
  duration_seconds: 103
  executor: operator
  summary: UR heroes 4 to 6: Lucius (4 stars) counters 683/96, 4/4, 4/100 gain HP +11,721 Attack +177 Defense +44; Schuyler (4 stars) 683/24, 76/76, 76/100 gain HP +5,394 Attack +309 Defense +39; Kimberly 5 stars no shard bar; shards live on the Tier tab below 5 stars
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/perception-scout/1858-queue-run.md and 1858-queue-run.csv; run 20261123T185849Z-8087c6
  follow_up: 683 read as the held UR universal pieces (inferred); no power gain figure on screen; heroes 7 to 9 next
  stats:
    target: star panels of UR heroes 4 to 6, one panel each
    achieved: 3 of 3 panels read
    resources_gained: none
    points: 0
    costs: none spent; model 0.140626 USD
    verified: yes
    run_id: 20261123T185849Z-8087c6
    run_steps: 10
    actions_done: 25
    actions_refused: 0
    cost_usd: 0.140626
    device_takeovers: 0
    panels_read: 3
    rules_used: 1
  stats_missing: []
  stats_warnings: []
---

# scout-midday

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: store ranking v1 weapon and hero reads

## Brief (planner for the Strategist, store ranking v1, H1b: UR heroes, UR heroes 4 to 6, read-only)

serves: PL-06

Source: `_records_/2026-11-22/strategy/0147-store-ranking-v1.md` and buys sheet `0147-store-buys.csv` (the buys wait for these reads). Read only; the Thursday hero-item window (server 2026-11-26T02:00Z to 2026-11-27T02:00Z) comes after.

Route: HEROES button (bottom bar, left), the Hero List, open one hero detail, the star and shard section (the section route is in the old H1 notes in `_records_/2026-11-22/perception-scout/2345-snapshot-protocol.md`). Use the same UR hero order as W1a and H1a (the Hero List, UR cards, left to right, top to bottom); if fewer remain, say so and stop. Per hero in this unit, one panel: the tag text (name as shown), stars, shards held, the COST of the next star (shards needed) and its POWER GAIN from the star preview (preview only; never Promote or Upgrade).

PRIMARY, the unit is DONE when it is read: the star panels of UR heroes 4 to 6, one panel each; nothing else.

Up to three runs, 10 steps each.

Hazards: close menus with the bare spot (310,660) (not (400,640) after a camera shift); never tap WORLD (660,940) with a menu open low. In the Backpack the Resources tab opens with the 5,000 Diamonds x16 tile SELECTED and a live Use: select nothing, press nothing. Never press Use, Open, Convert, Sell, Buy, Upgrade, Unlock, Promote, Equip, Recruit or any shard control. Stop at a price or diamond.

Tag text: write each number's tag text beside it (name shown on the screen; for a building, name and level) and add a tag_text column; none means [G]. Write the frame time per row. Rules and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md` (K or M numbers only: write 1.1G as 1100M). Do not enqueue a chain successor.
Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`; stop with one named reason, never improvise.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.60 USD per run (the harness stops near 0.36 of it).
