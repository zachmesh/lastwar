---
title: Construction speed sources
created: 2026-11-24T18:00:00Z
modified: 2026-11-24T18:00:00Z
version: 1.0.0
level: L3
description: Where a construction speed bonus can come from, which one fits the +0.200 step seen on 2026-11-24, and the read-only screens that would name it, with the build-start rule that decides whether the ground ends moved
status: unverified
grounded_in:
  - source: https://game8.jp/lastwar-survival/644843
  - source: https://lastwarvault.com/build-time-calculator/
  - source: coach unattributed-window-1556-1731.csv
---

# Construction speed sources

Rule [S1 game8.jp, Nov 2025; community guide, tuning can shift]: build time is the original over (1 plus the total speed bonus); bonuses add. So our factor 2.325 is a bonus of +132.5 percent, up from +112.5 (2.125) and +100 (2.000). The bonus is the sum of: research (the Development tree up to +25, the Age of Oil tree up to +25), the alliance tech Quick Construction (up to +25), VIP benefits (+10 at VIP 3, +20 at 5, +30 at 7, +40 at 9, +50 at 11, once unlocked), occupation skills (Engineer Lv.30 Joint Construction +20, Lv.65 +25, season only), the Eternal Pyramid decoration (+5 to +55), officials and cities.

- **The step fits +20:** the Engineer skill Joint Construction at Lv.30 is exactly +20; a research or alliance step is smaller per level, VIP moves in tens. The earlier +12.5 step fits half of a 25 node. All [G]; nothing names the source yet.
- **Does a running build change?** The same guide says a bonus applies only to builds started after it changes. Our displayed ends fell by one factor on two running builds at 17:04Z, so either this game recomputes or the display lagged. The test is the Lv.26 ground: displayed end about 11-26T11:08Z, old end 21:10:37Z. If it is not complete at 11:15Z, the true end is 21:10Z: check again then, and the room test and the B2 start move to 21:15Z.
- **Read-only screens, cheapest first** [G on the routes]: the Alliance Techs panel (Quick Construction level; the donation unit already opens it), the research tree (Fast Builder V state), the profile or occupation screen (Engineer level), the VIP panel (a purchase surface: needs Steer A's approval and an exit plan), the decoration list.
- **A lever if the source is ours to pull:** each +20 shortens every build and the HQ 31 upgrade by about 7 percent; price it when a source is named.
- **Row:** F-210 (the Lv.26 ground ends by 11:15Z).
