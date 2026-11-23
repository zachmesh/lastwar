---
title: Queue Planning Store Ranking Reads Staged And The Buy Units Pending 2620 2026-11-23
created: 2026-11-23T04:27:00-08:00
modified: 2026-11-23T04:27:00-08:00
level: L0
version: 1.0.0
description: Planner pass on store ranking v1 - five read-only units staged for the exclusive weapons and the UR heroes, the superseded S1b retired, the pool simulated, and the design of the buy units that wait for the reads
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-0427-store-reads
trigger: coordinator message with store ranking v1 and the buys sheet
started_at: 2026-11-23T04:20:00-08:00
finished_at: 2026-11-23T04:27:00-08:00
verified: ranking, buys sheet and Black Market policy read in full; pool simulated with the five units under three expiry choices; word counts under 450; validate exit 0
grounded_in:
  - source: _records_/2026-11-22/strategy/0147-store-ranking-v1.md and 0147-store-buys.csv
  - source: _records_/2026-11-22/strategy/0133-black-market-policy-v1.md
---

# Store reads staged, buys pending, 2620

## 1. Staged

All priority 1, read-only, 10 minutes, up to three runs, window 12:55Z today to 2026-11-25T20:00Z, `serves: store ranking v1 weapon and hero reads`. W1a (`scout-midday-growth-snapshot-2026-11-23-027`): the first three exclusive weapons in hero-list order, plus the held Universal Exclusive Weapon Shards. W1b (`-028`): weapons four to six. H1a (`-029`): the UR hero roster and the held UR Hero Universal Shards, plus UR heroes 1 to 3. H1b (`-030`): heroes 4 to 6. H1c (`-031`): heroes 7 to 9 and any left. Per row: tag text, unlocked or locked and level (weapons), stars and shards held (heroes), the next step's cost, and its power gain from the preview only, never Upgrade, Unlock, Promote or Use. Hazards are in every brief. The earlier S1b weapon read (`-015`) is superseded and retired, its expiry set past; the old H1, H2 and H3 stay, since they read the roster layout and the Squad 1 stats.

## 2. Order

The queue orders by expiry, so the long window ranks these after every routine unit. Simulated from 12:46Z at 5 minutes per read, they run at about 14:16Z to 14:36Z and no other unit expires; a literal window and staggered expiries to 14:40Z or 16:40Z gave the same result. The risk is the 14:03Z wave: once staged its units rank ahead and may push the reads later. I check at the daily pass; a tighter expiry is a one-line edit.

## 3. Buy units, not yet staged

They wait for W1 and H1 and are staged before 2026-11-26T01:00Z, as the buys sheet says: honor (Universal Exclusive Weapon Shard x25 for 62,500, UR Hero Universal Shard x10 for 30,000, each only if a read shows something that can take it), Campaign stars (Universal Exclusive Weapon Shard x4 at 300, hero shards x6 at 200 only if no weapon takes them), Black Market tiles by policy 0133 (read every tile, buy ranked tiles with cash first, then Free refreshes only, at most 10 a day), and the held rows only if their read condition is met. Every buy unit reads balances before and after, confirms only on listed rows with exact quantities, and never touches the paid refresh, diamonds, weekly passes, cash packs, the Glittering Market, Resource Choice Chests, Hero Recruitment Tickets or 50 Stamina.
