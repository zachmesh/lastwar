---
title: Store ranking v1
created: 2026-11-23T09:47:00Z
modified: 2026-11-23T17:39:00Z
version: 1.1.0
level: L3
description: The ranking of honor, alliance and Campaign store items by hero value per currency, the exact buys, the holds and reserves, with forecasts
status: unverified
grounded_in:
  - source: scout read _records_/2026-11-22/perception-scout/0938-st1-stores.md and its CSV
  - source: Steer A decision 2410 and the Black Market policy _records_/2026-11-22/strategy/0133-black-market-policy-v1.md
---

# Store ranking v1

Balances at 09:43Z: honor 130.1K, alliance 81,010, Campaign stars 1,260, cash 10,350. Honor limits reset 2026-12-01T02:00Z, alliance and Campaign limits 2026-11-30T02:00Z. A limit is use-it-or-lose-it; a balance probably persists (H59, unread). Exact rows in [the buys table](0147-store-buys.csv).

## First finding: the stock is not the constraint

On 11-10 the account held 417 Universal Exclusive Weapon Shards (441 now) and 680 hero universal shards, and the Exclusive Weapon line stayed 2,182,608 from 11-08 to 11-22 [M]. Shards, 9,521 Skill Medals and hero chests have waited at least 12 days, probably for the Thursday hero-item window (H60). Buying 25 more adds 6 percent to a stock that waits. Use decides, so read first.

## Ranking, best first

1. **Apply what is held** in the Thursday window (server 11-26 02:00Z to 11-27 02:00Z): the weapon with the best power per shard, concentrating on one weapon until a milestone step (Lv.30, Lv.40) is reached; the carry hero with the cheapest star-up.
2. **Buys are on hold.** The Squad 1 reads show 441 weapon and 680 hero universal shards held; the steps need 125 (Carlie 45, DVA 60, Murphy 20) and 120 (Lucius 96, Schuyler 24) [D, pattern H107]. Buy honor Universal Exclusive Weapon Shard x25, honor UR Hero Universal Shard x10 and Campaign stars only when the stock after Thursday is under 200 and 300. Honor 130.1K stays.
3. **Hold, read first:** Mason Shard x30 (30,000 alliance) unless Mason is a top-16 hero short of a star; Gear Blueprint UR, Skill Chip Chest UR, Decoration Chest and Decor Components, Drone Parts and Dielectric Ceramic (after the drone preview); Season tokens 800 (Gear Blueprint MR at 100, UR Hero Badge at 50; they may lapse at Season 3, H63).
4. **Never now:** Resource Choice Chests (coin is not the gate), Hero Recruitment Ticket, 50 Stamina (red line).

## Reserves

Honor 37.6K stays. On the first day of each month buy the full UEWS and URU limits (92,500 honor): read the honor income before the 2026-12-01 reset. Campaign stars: URU limit each Monday. Cash follows the Black Market policy.

## What the operator needs read first

For each of six weapons: unlocked, level, next-level shard cost, power gain; the held counts of universal weapon and UR hero shards; each UR hero's stars and shards held. Names and the weapon order come from those reads.

## Forecasts

F-049 and F-050 (deterministic purchases), F-051 (the 417 still held, p 0.7), F-052 to F-054 (a level-up p 0.8; 10K to 45K power; a milestone p 0.2 for 0.3M), F-055 and F-056 (a star-up p 0.5; 25K to 90K each).

Event stores (Thanksgiving Store, Lottery, Gift of Thanks) are ranked in [the event store ruling](0630-event-store-ruling.md): speed-ups first, shards last, a ten-draw lottery cap.
