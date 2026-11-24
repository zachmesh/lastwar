---
title: Oil line
created: 2026-11-24T16:44:00Z
modified: 2026-11-24T17:43:00Z
version: 1.0.0
level: L3
description: The measured oil rate, the barrels in the Backpack, the two cases for the HQ 31 and Base Expansion oil, and the one barrel Use that decides between them
status: unverified
grounded_in:
  - source: coach oil-series.csv and oil-gap-scenarios.csv, 2026-11-24 14:53Z
  - source: _records_/2026-11-22/strategy/base-expansion-path.csv
  - source: _records_/2026-11-22/growth/0009-inventory-read.md
---

# Oil line

- **Measured** [M, coach]: HUD oil 647,000 (11-23 12:51Z) to 687,000 (11-24 14:53Z), 1,536 an hour, 36.9K a day: the Lv.22 well's 1,320 an hour plus about 230 an hour from other collected sources. The depot's 30K a day arrives as barrel items, not on the HUD.
- **Barrels held** (11-23 labels, never selected): 3.0K x6 and 6.0K x27 = 180K, plus five 6.0K from the 07:36Z depot claim: about 210K. A barrel's Use adds its label to the HUD [M]: the other device used 210K of barrels on 11-23 and the counter rose by their sum (records 1308, 1327). Those 180K to 210K are therefore gone, not held: the Backpack holds only today's 30K and later depot items (stock unread).
- **Need:** HQ 31 1.2M plus the path 4.08M at the sheet, 3.49M at the 0.855 factor (the Oil Output I start cost 51.3K of its 60K, H112 derived), so 4.69M against 687K held.
- **Case A (verified, no barrel stock beyond 30K):** 36.9K plus the depot's 30K a day and 210K already held: about 66.9K a day, the path's oil done about 2027-01-09 and the earlier ETA stands (2027-01-08 to 01-23).
- **Case B (refuted by the 11-23 episode, kept for the record):** 36.9K a day, rising to about 41K as the well climbs: the path's oil alone takes about 73 days, so Base Expansion slips to about 2027-02-05 and HQ 31, 29 days later, to about 2027-03-06; the labs wait on oil, not time. If the nodes cost no oil (H112 false), only HQ 31's 1.2M binds: the gap of 513K takes 13.9 days at 36.9K a day.
- **No test needed:** the barrel Use is verified by the 11-23 episode (F-202 true by record). Oil items are used just in time, in the HQ 31 start unit's pre-steps; the date is on [the HQ 31 page](0690-hq31-date.md).
- **Lv.23 of the well** (17:27Z) adds 60 an hour.
- **Rows:** F-202 (the barrel Use adds its label), F-203 (HUD oil on 11-26 02:00Z).
