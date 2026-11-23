---
unit: scout-midday-growth-snapshot-2026-11-23-020
regular: scout-midday
activity: perception-scout
segment: 2
priority: 2
created_at: 2026-11-23T08:27:08Z
expires_at: 2026-11-23T09:45:00Z
planned_for:
not_before: 2026-11-23T09:05:00Z
window: growth snapshot ST1 read only nothing bought
est_minutes: 10
serves: snapshot (Story 868)
chain_id: growth-snapshot-2026-11-23
chain_seq: 20
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T09:38:37Z
lease_until: 2026-11-23T09:58:37Z
result:
  status: partial
  started_at: 2026-11-23T09:38:37Z
  finished_at: 2026-11-23T09:43:42Z
  duration_seconds: 305
  executor: operator
  summary: Store read ST1 over three runs (20261123T093837Z-368305, 20261123T094011Z-2eaf5c, 20261123T094139Z-750ba2; claude-gateway/claude-sonnet-5-5; 25 steps): balances Honor 130.1K, alliance currency 81,010, Campaign stars 1,260; Honor, Alliance and Campaign tiles with prices, stock and refresh lines read (Honor in full to Emote: Victory Fest); unread: Campaign prices of Universal Exclusive Weapon Shard, Skill Chip Chest (SSR) and Upgrade Ore, three Alliance last-row prices, the Season, Coupon Store and Crystal Shop tabs. Read-only; nothing bought, refreshed, claimed or tapped on a tile.
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/perception-scout/0938-st1-stores.md and _records_/2026-11-22/growth/0938-st1-stores.csv; runs 20261123T093837Z-368305, 20261123T094011Z-2eaf5c, 20261123T094139Z-750ba2
  follow_up: one short read for the Campaign weapon-shard, Skill Chip Chest SSR and Upgrade Ore prices and the Season tab; Alliance last-row prices; the profile popup 'You're very popular!' covers the profile and costs a turn (tap Awesome! once)
  stats:
    target: read the Honor, Alliance and Campaign stores: balance, tiles, prices, limits, refresh
    achieved: three balances and about 35 priced tiles read; 3 Campaign prices, 3 Alliance prices and the Season tab unread
    resources_gained: none (observe-only)
    points: 0
    costs: model 0.326752 USD in three runs; nothing spent
    verified: yes
    blocker_category: c
    run_id: 20261123T094139Z-750ba2
    run_steps: 25
    actions_done: 41
    actions_refused: 0
    model_s_per_step: 5.1
    cost_usd: 0.326752
    device_takeovers: 0
  stats_missing: []
  stats_warnings: []
---

# scout-midday

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: snapshot (Story 868)

## Brief (planner, growth snapshot ST1, Story 868, from the scout's unit table)

serves: snapshot (Story 868)

Read-only unit ST1. Queue placement: after the capacity reads, D1, BM1 and SC1, ahead of the routine claims.

Question: What is the balance of each store currency, and what do the Honor, Alliance and Campaign stores sell, in which currency, at what price and limit?

Route: Avatar (about 110,100) opens MY PROFILE, the gold VIP badge (about 404,360) opens the VIP screen, the cart icon at the top right of that screen opens the STORE (verified 2026-11-08). Never the cart on the base screen: it opens the paid Mall. Tab strip: VIP, Alliance, Honor, Campaign, Season, Cosmetics and a cut-off tab. Open Honor, Alliance, Campaign in turn; read the balance chip, every tile and the refresh line, scroll the grid. Back arrows (about 175,930) and the profile X (about 627,77) in the last step.

Read: Per tab: balance and its name; per tile item, quantity, currency icon, price, stock over limit, sold out or not, red price (above balance); refresh text and timer.

Budget: at most 8 steps and 10 minutes. Notes: Output _records_/<date>/growth/<HHMM>-st1-stores.csv, schema m_store. Read prices from the tiles. Tap no tile, Buy, Confirm or Refresh, and nothing priced in red gems or money (VIP tab, VIP exclusive offer, Pack buttons, weekly passes, Glittering Market). The profile screen shows the account name and IDs: do not record or save them (S7). Earlier reads, probably stale: Honor 101.1K (monthly refresh 00:00 on the 1st, server time), Alliance 301.3K (Alliance Contribution read 347.9K on 2026-11-22), Campaign stars 1,260 (weekly refresh Monday). Honor tab on 2026-11-03 sold Universal Exclusive Weapon Shard 25 at 2,500 each, UR Hero Universal Shard 10 at 3,000, Resource Choice Chest UR 100 at 4,000, Decoration Chest 1 at 50,000, Universal Decor Component 150 at 200; Alliance tab Mason Shard 30 at 1,000 on 2026-11-08. Re-read all of it, stock changes at refresh.

Rules: stop rules R1 to R7 in `_records_/2026-11-22/perception-scout/2345-snapshot-protocol.md`; red lines and the snap command in `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`. Snap takes only K or M numbers: write 1.1G as 1100M. Buy nothing, open nothing, press no Claim. Do not enqueue a chain successor.

Cost cap, stated: 0.60 USD (the harness stops near 0.36 of it).
