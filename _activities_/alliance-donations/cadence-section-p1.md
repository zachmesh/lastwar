---
title: Cadence part 1
created: 2026-11-23T06:11:49Z
modified: 2026-11-23T06:11:49Z
version: 0.1.0
sequence: 13
description: Every four hour run (owner instruction, 2026-10-26, replacing the earlier daily cadence).
---
## Cadence

- Every four hour run (owner instruction, 2026-10-26, replacing the
  earlier daily cadence). The coin button allows 30 donations a day. (2026-11-22 update, Issue #813: the flat '30 donations a day, burn them down early' model is superseded - the count is a regenerating pool capped at 30, refilling about 1 per 20 minutes on a clock-anchored cycle; a unit that finds 30/30 late in the day is not seeing a fresh day. The quota checkpoints of rule R3 are read against a refilling count, not a fixed daily 30.)
- The screen footer tracks Tech Donation Today in contribution points,
  with a daily reward at 1000 points. Five coin donations earned 300
  points on 2026-10-25, so a coin donation is worth 60 points and the
  1000 point reward sits beyond the 5 donations the daily mission asks
  for.
- CORRECTION, 2026-11-10 (Issue #558): the Tech Donation Today footer is not account-attributable - it aggregates alliance-wide or other sources - so its delta cannot verify the personal Donation Count. The footer stays a display read only, never a closing figure and never a re-read surface; the Donation Count read is the only closing figure, and the Strength Ranking Donation tab is the remaining candidate surface to test. (2026-11-10 1734 update: the footer moved 7600 to 9300, +1700, over exactly 17 own coin donations in this unit - 100 per donation by arithmetic if the delta is solely own. The per-donation point value is not settled in the records (50 and 60 both appear in older notes), and the footer aggregates alliance-wide, so this does not settle the value and does not close the count; the footer stays disqualified as a closing figure. The re-read unit donations-2026-11-11-0122 reads the Donation Count live after the cooldown. (2026-11-10 1919 update: the footer reset mid-unit, 9300 at entry to 550 at close, between about 19:24 and 19:34 PST - the footer cannot derive this unit's final count either; it stays disqualified. The reset instant is tracked on Issue #599.) (2026-11-10 2015 update: footer 550 at entry - the same value the 1919 unit read after the mid-unit reset, so no points accrued between 19:35 and 20:10 - re-read 700 after the unit's taps, +150 for 1 confirmed + 1 unknown tap. Two donations at 50 points each would be +100, so the footer points per donation are not stable (60 on 2026-10-25, 50 on 2026-10-26, 100 by arithmetic on the 1734 +1700, +150 here) and the footer cannot derive the count - the 1913 conclusion stands. The top-bar badge item count read 404.9K at entry and 405.1K after tap 2 (+200);