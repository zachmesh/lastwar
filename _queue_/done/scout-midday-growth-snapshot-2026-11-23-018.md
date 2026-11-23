---
unit: scout-midday-growth-snapshot-2026-11-23-018
regular: scout-midday
activity: perception-scout
segment: 2
priority: 2
created_at: 2026-11-23T08:17:23Z
expires_at: 2026-11-23T09:38:00Z
planned_for:
not_before: 2026-11-23T09:05:00Z
window: growth snapshot BM1 read only nothing bought
est_minutes: 10
serves: snapshot (Story 868)
chain_id: growth-snapshot-2026-11-23
chain_seq: 18
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T09:28:53Z
lease_until: 2026-11-23T09:48:53Z
result:
  status: done
  started_at: 2026-11-23T09:28:53Z
  finished_at: 2026-11-23T09:31:14Z
  duration_seconds: 141
  executor: operator
  summary: Black Market BM1 read, run 20261123T092921Z-181b74 (claude-gateway/claude-sonnet-5-5, max-steps 8, completed in 5 steps), read-only: cash 10,350, timer 20d 16:30:28, top row three tiles sold out, bottom row three tiles at 500 cash each availability 1 (orange IV item x5, purple chest x1, blue-silver chest x6), Refresh free 62/62, Quick Buy unticked; Challenge Earned today 550/600, timer 6d 16:30:20, Radar Task, Secret Mobile Squad (outside the cap), Doom Elite 5, Zombie 0; no Bingo tab visible. Nothing bought, refreshed, claimed or tapped on a tile.
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/perception-scout/0929-bm1-black-market.md and _records_/2026-11-22/growth/0929-bm1-black-market.csv; run 20261123T092921Z-181b74
  follow_up: Bingo final reward still unverified (no tab visible); the bottom-row blue-silver chest x6 name unread; spending BM cash on the 500-cash tiles needs the owner's word
  stats:
    target: read the Black Market page and Challenge page, nothing bought
    achieved: Black Market and Challenge read in full, Bingo not visible
    resources_gained: none (observe-only)
    points: 0
    costs: model 0.079503 USD; nothing spent, bought or refreshed
    verified: yes
    run_id: 20261123T092921Z-181b74
    run_steps: 5
    actions_done: 8
    actions_refused: 0
    model_s_per_step: 4.9
    cost_usd: 0.079503
    device_takeovers: 0
  stats_missing: []
  stats_warnings: []
---

# scout-midday

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

## Brief (planner, growth snapshot BM1, Story 868, from the scout's unit table)

serves: snapshot (Story 868)

Read-only unit BM1. Queue placement: After the capacity reads and D1, ahead of the routine claims. Read-only: nothing bought.

Question: What does the Black Market sell, in which currency, at what price and limit, and how is its cash earned?

Route: Base right-edge column, Events icon; the hub opens on some tab. Earlier frame tabs: (271,155) Arms Race, (421,155) Black Market, (570,155) Black Market Challenge; re-ground, drag the tab bar if one is cut off. Black Market page: cash balance, timer, every tile, Refresh and Quick Buy controls, any Rules or info icon. Challenge tab: Earned today, each source row, scroll. Bingo Task tab: final reward line. Back arrow (about 175,930).

Read: Cash balance; timer; per tile item, quantity, currency icon (cash, diamond, real money, free), price, availability, sold out or not; Refreshes today and the Refresh cost; Quick Buy state; Pack button label; any pool list with item, currency, price; Challenge Earned today over cap, each Go To row with drop type and count, its timer; Bingo final reward.

Budget: at most 8 steps and 10 minutes. Notes: Output _records_/<date>/growth/<HHMM>-bm1-black-market.csv, schema k_market. Also never tap Buy, Confirm, Quick Buy, Refresh, Pack, Go To or Claim. Copy the currency as the icon shows it; a diamond or real-money price is read and left alone. Tap a tile only if its icon cannot be read and only while Quick Buy is unticked (ticked means one tap buys), then Cancel or X. Read both rows in full now, they change at refresh. Seen at 05:41Z 2026-11-23: cash 10,030 (7,190 and 7,240 earlier, the jump is unexplained; Bingo final reward pays 1.5K, unverified), bottom row 500 cash each, top row sold out, Challenge 470 of 600 a day. No shard choice chest seen yet. Timer 20d 20:19:07 puts the end near 2026-12-14T02:00Z, the 18:00 PT reset on 12-13.

Rules: stop rules R1 to R7 in `_records_/2026-11-22/perception-scout/2345-snapshot-protocol.md`; red lines and the snap command in `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`. Snap takes only K or M numbers: write 1.1G as 1100M. Buy nothing, open nothing, press no Claim. Do not enqueue a chain successor.

Cost cap, stated: 0.60 USD (the harness stops near 0.36 of it).
