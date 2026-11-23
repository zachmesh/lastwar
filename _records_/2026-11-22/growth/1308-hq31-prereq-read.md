---
title: HQ 31 prerequisite read
created: 2026-11-23T13:20:00Z
modified: 2026-11-23T13:20:00Z
version: 1.0.0
description: The Headquarters Lv.30 to 31 preview names ONE unmet prerequisite, the Base Expansion research Lv.1; the Tech Center, Barracks and Centers are already at Lv.30 or more; the other device used the Backpack oil and coin tiles and about 3,960 minutes of blue-disc speed-ups
status: done
grounded_in:
  - source: cu_bridge runs 20261123T130521Z-e29a2e, 20261123T130659Z-7636b4 (frame step-0003), 20261123T130851Z-d2a82d (frames step-0005, step-0006) and 20261123T131057Z-238700, 2026-11-23T13:05Z to 13:12Z
  - source: coordinator assignment A-20261123-1300-operator and its Backpack additions of 13:08Z and 13:10Z
---

# HQ 31 prerequisite read

Rows in [1308-hq31-prereq-read.csv](1308-hq31-prereq-read.csv). No different-device dialog in any no-click first frame; nothing pressed.

- **Headquarters Lv.30 to 31** (tag "Headquarters Lv.30", green arrow of the radial menu): Power **388,300 to 452,000 (+63,700)**, Hero Level Cap 150 to 155.
  Costs: oil 647,039 of **1.2M**, iron 1.0G of **1.3G**, food 653.9M of **1.3G**, coin 55,963 of **433.5M** (all red); time **52d 14:17:16** effective
  (111d 18:21:40 original); Finish Now 1,847,528 diamonds, not pressed.
- **Prerequisites:** only **"Lv.1 Base Expansion"** (a research node, red, button Research) is unmet. "Lv.30 Any Tech Center", "Lv.30 Barracks" and
  "Lv.30 Any Tank, Missile Vehicle, or Aircraft Center" show **green checks**, so the building search for them is not needed (their exact levels stay unread).
  No Go button exists; the cost list scrolls with a drag from the left of a row.
- **Hazard.** The "empty ground" tap (200,610) hit a **Gold Mine Lv.28** and opened its menu; (400,640) is empty (added to `tag-index.csv`).
- **Oil tiles (13:09Z).** The Resources tab no longer holds the 3.0K x6 and 6.0K x32 oil barrels nor the coin tiles 6.0K x174 and 600 x5,713; SR Coin
  Chests went 122 to 40. The oil counter rose 434.1K to **647.0K** (+212.9K): the other device used the 210K barrels and the counter includes them.
- **Speed-ups (13:11Z against 11:26Z).** General 351,687 min (was 351,647) and construction 167,895 (was 167,760): only small gains, none used. The blue-disc
  type (probably research) fell **8h 16 to 8 and 1h 128 to 126 = 3,960 minutes used**, consistent with a speed-up on the new research.
- **Run.** `claude-gateway/claude-sonnet-5-5`, 6 + 10 + 11 + 8 steps, 0 refused, no `local_input` pause, 0.088826, 0.129278, 0.137145 and 0.103050 USD (0.458299 in all).
- Closing state: the base, no panel, token released.
