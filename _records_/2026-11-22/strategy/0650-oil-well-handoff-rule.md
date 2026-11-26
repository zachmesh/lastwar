---
title: Oil Well hand-off rule
created: 2026-11-23T22:30:00Z
modified: 2026-11-26T13:35:00Z
version: 1.0.0
level: L3
description: The rule for re-ranking builder 1 at each Oil Well level hand-off, with the oil date each level moves, the power per builder-day on two assumptions and the coin test
status: proposed
grounded_in:
  - source: Steer A message of 2026-11-23 22:29Z
  - source: _records_/2026-11-22/strategy/oil-well-levels.csv and decision 08
---

# Oil Well hand-off rule

At each hand-off (a level completes, the next starts) the unit note records three numbers for the next level and for the best alternative, and the choice follows them. Table in [oil-well-levels.csv](oil-well-levels.csv).

## Timing and the time factor (11-25)

The Lv.24 start (17:31:42Z, record 1731) read factor 0.4301 (0.4706 at Lv.23); the flat 23,520 s held a seventh time. The Lv.24 build then finished before 05:25Z, not by us (the owner was playing 04:53Z to 05:14Z), 1.6 h or more ahead of 07:11:20Z. From a Lv.25 start at about 05:41Z at factor 2.325 (read at each start): Lv.25 ends 11-26T03:26Z, Lv.26 11-27T12:37Z, Lv.27 11-29T13:30Z, Lv.28 12-02T12:40Z, Lv.29 12-06T11:00Z, Lv.30 12-11T15:40Z.

## The three numbers

1. **Power per builder-day.** Lv.21 is 10.8K [M]. Later gains are unread: the sheet's increments rise (4.9K, 5.4K, 6.0K for Lv.22 to 24), so I extrapolate +0.6K a level; Steer A's floor holds +4.2K flat. Lv.25 is 5.1K or 3.3K, Lv.27 3.1K or 1.7K, Lv.29 2.0K or 0.9K.
2. **The oil date it moves.** A level adds 1,440 oil a day (+60 an hour). Moved dates, with oil at 0.90 of the sheet [G]: Lv.21 to 24 about 0.7 days on the research path and 0.9 to 1.0 on HQ 31; Lv.25 to 27 0.5 to 0.6 and 0.8 to 0.9; Lv.30 0.3 and 0.5. Per builder-day, HQ 31's oil date moves 2.5 days (Lv.21), 0.7 (Lv.25), 0.3 (Lv.27) and 0.1 (Lv.30).
3. **The coin on the panel.** The Lv.21 panel is iron only (8.5M). The sheet adds coin from Lv.21 (1.8M rising to 33M at Lv.30); read the cost rows at every start (H116).

## Rule (11-26, all three cost rows)

Price every level from the table's three columns at 0.85 first, then compare the preview with every row dragged into view; a missing row is not an absent cost (H116 reopened: the Lv.26 to 27 level cost iron 56.1M, food 18.7M and coin 11.9M). The well is not coin-free. By power per million coin it still beats the ground (365) and the path (214): Lv.27 891, Lv.28 741, Lv.29 626, Lv.30 529 (+10,600, +12,600, +14,900, +17,500 [S1 table; Lv.25 to 26 measured +9,300]). By power per builder-day it falls to 5.0K, 3.6K, 3.2K and 2.9K (times 2.1, 3.5, 4.6 and 6.0 days at 2.125), below the Training Base (4.6K), Gear Factory (4.2K) and Iron Mine (3.9K) after Lv.27, and its oil date moves under 0.3 days per builder-day from Lv.28. So the stop point is after the running Lv.26 to 27 level (ends about 11-28T19:37Z): the builder then takes the Training Base Lv.26 to 27, then the Gear Factory. Levels 28 to 30 would add about 74M coin the 2.15B bill omits.

## Oil model

Income now 58.8K a day (1,200 an hour plus the depot), 66K at Lv.25, 73K at Lv.30. The research oil cost factor is about 0.89 (H112).
