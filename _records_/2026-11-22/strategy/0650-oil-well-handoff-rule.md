---
title: Oil Well hand-off rule
created: 2026-11-23T22:30:00Z
modified: 2026-11-23T22:30:00Z
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

## The three numbers

1. **Power per builder-day.** Lv.21 is 10.8K [M]. Later gains are unread: the sheet's increments rise (4.9K, 5.4K, 6.0K for Lv.22 to 24), so I extrapolate +0.6K a level; Steer A's floor holds +4.2K flat. Lv.25 is 5.1K or 3.3K, Lv.27 3.1K or 1.7K, Lv.29 2.0K or 0.9K.
2. **The oil date it moves.** A level adds 1,440 oil a day (+60 an hour). Moved dates, with oil at 0.90 of the sheet [G]: Lv.21 to 24 about 0.7 days on the research path and 0.9 to 1.0 on HQ 31; Lv.25 to 27 0.5 to 0.6 and 0.8 to 0.9; Lv.30 0.3 and 0.5. Per builder-day, HQ 31's oil date moves 2.5 days (Lv.21), 0.7 (Lv.25), 0.3 (Lv.27) and 0.1 (Lv.30).
3. **The coin on the panel.** The Lv.21 panel is iron only (8.5M). The sheet adds coin from Lv.21 (1.8M rising to 33M at Lv.30); read the cost rows at every start (H116).

## Rule

Keep B1 on the well while the level is coin-free and beats the best free alternative on power per builder-day or moves HQ 31's oil date by at least 0.3 days per builder-day. If a panel shows coin, compare power per million coin: the ladder is 5.9K, Gold Mine 622, and Lv.28 on the sheet's coin about 500. Every alternative costs coin (Gold Mine 23.8M, Hut 18.7M, Barracks 49.3M), so the well is the only coin-free builder job. Likely stop point: Lv.27 to 28, or earlier if coin appears. Oil only matters while it binds: the path's oil day is 35 to 49 and HQ 31's 50 to 65 [G], against 45 to 60 for the lab chain.

## Oil model

Income now 58.8K a day (1,200 an hour plus the depot), 66K at Lv.25, 73K at Lv.30. The research oil cost factor is unmeasured: 0.90 like the other research costs (0.85 is the construction factor).
