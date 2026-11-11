---
title: Zero sweep 002 2026-11-09 ticker-1734 queue run
created: 2026-11-10T01:48:00Z
modified: 2026-11-10T01:48:00Z
version: 1.0.0
description: Pre-reset zero sweep unit 002 of 2, ticker-1734, zero-sweep-2026-11-09-1730
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-11-09
---

# Zero sweep 002 - 2026-11-09 17:38-17:48 PST (ticker-1734)

Unit: zero-sweep-2026-11-09-1730, chain pre-reset-sweep-2026-11-09.
Status: partial (sweep pair 002 of 2; the walk is not finished - see
unread lines below, each covered by an already-queued unit named
there). Target: 23 ledger lines; 5 read live in this unit, 4 of
them non-zero. Sweep 001 (16:35) read 7 lines; together the pair
read 12 of 23.

## Live reads (17:40-17:46 PT)

Base HUD at entry: food 556.6M, iron 881.6M, coin 53.6M, diamonds
6,137, VIP 13.22K, power 148,140,193, stamina 99, VS timer
00:20:00, Events countdown 6d 00:20:01. Build: Oil Well [0/1];
building queue 1/4; research 1/2. At close: power 147,469,864,
stamina 100, VS 00:15:25, Events 6d 00:15:25.

### Lines read live, not at zero

- **Food bubbles (line 1) - not zero.** Many wheat bubbles stand
  over the farmland, same as at 16:35.
- **Iron bubbles (line 2) - not zero.** Several blue iron bubbles
  stand over the mines.
- **Coin bubbles (line 3) - not zero.** Several gold coin bubbles
  stand on the base.
- **Trucks - dispatch 5 of 5, plunder 4 of 4 (line 18) - not
  zero, short.** Intercity Trade read live: Today's Trade Count
  4/5 (four trucks out on Your Truck tab), Your Plunder Count
  Today 1/4 (Others' Trucks tab). Shortfall with the trade day
  ending at the 19:00 reset: dispatch -1, plunder -3. Fix-up:
  trucks-2026-11-09-1457 raised to priority 1 (expires 18:57);
  the executor runs it next in this pass.

### Lines read live, at zero or absent

- **Events hub tabs - read.** Tabs visible: Winter Battlefield,
  Desert Storm Battlefield (selected), Wanted Boss. No Zombie
  Invasion tab (event still ended, no chain seeded). No Crystal
  or Glittering Market tab in the visible row (the row may scroll;
  absence not confirmed).
- **Desert Storm Battlefield (new event surface).** Registration
  ends in 2d 00:14:37; Battle Day 2026-11-13, 03:00-03:30;
  Participants 20/20; Task Force A (You) vs Task Force B.
  Handed to the events-2026-11-09-1857 unit; no tap made here.

### Lines not read live this unit (handed to queued units)

- EXP bubbles, titanium bubbles, Armed Truck loot - harvest
  unit harvest-2026-11-09-1803 (already priority 1). The 3.9K
  labelled icons visible over the base look like EXP bubbles
  but the type was not individually confirmed - unverified.
- Train station - train-2026-11-09-1430 (due now, expires
  18:30) and train-2026-11-09-1830.
- Arms Race phase - arms-race-2026-11-09-1803.
- Daily missions 160/200 chests - daily-missions-2026-11-09-1800.
- Radar map pins - radar-2026-11-09-1803.
- Alliance Duel daily total vs 3.6M - duel-score-2026-11-09-1830.
- Crystal (R5, age 15 days from 2026-10-25) and Glittering
  Market (R5, age 9 days from 2026-10-31) - still not located
  by any evidence today; no new surface found in this sweep.

## Notes and open items

- **Power falling, cause unverified.** Total Power read
  149,217,331 at 16:35, 148,140,193 at about 17:40 and
  147,469,864 at about 17:45 - down about 1.75M in 70 minutes
  while no battle unit ran (radar 17:07-17:17 and survivors
  17:19-17:29 were both partial, no fights). The system feed
  shows truncated "Mutant Raider has been..." messages. Whether
  mutant raids drain power is unverified; flagged for the daily
  retro, no issue filed on a single observation.
- **Secret Command Post, incidental read.** A tap on the left
  icon column opened the Secret Command Post instead of trade
  (the two shortcut sets share the slot, per the truck-plunder
  metadata). Secret Mobile Squad reads Assist Allies 5/5,
  Plunder Others 0/3, with four SSR task cards all marked
  PERFECT. Handed to secrets-2026-11-09-1803; nothing tapped
  further there.
- **Entry route learned.** In the current icon set the blue
  truck-front icon at norm y about 573 opens Intercity Trade
  directly; the jeep below it is the Secret Command Post.
- A red skull icon with badge 1 and a seconds countdown (00:00:09
  falling to 00:00:04) and a target icon with badge 1 (00:00:25)
  stand at the right edge of the base screen - unidentified,
  recorded unverified, no tap made (same item as sweep 001).
- Donations line (line 17) was not re-read this unit: sweep 001
  found Donation Count 19/30 remaining at 14:13; donations
  units donations-2026-11-09-1403 (priority 1) and
  donations-2026-11-09-1803 cover it.

## Sweep actions taken

One inbox unit raised to priority 1 for a line verified
non-zero: trucks-2026-11-09-1457. Pool validated after the edit.
No new units enqueued - every unread line already has a queued
unit for the 18:00-18:57 slots.

## Close

- Nothing claimed in this unit; the sweep reads only.
- No diamonds or money spent. No speedup or stamina items used.
- Tracker untouched (partial unit). Blocker category: h
  (by-design partial - the pair's walk ends here; the 18:00-18:57
  batch verifies the remaining lines).
- Zombie Invasion: tab still absent from the Events hub; no chain
  seeded, per the standing rule.
