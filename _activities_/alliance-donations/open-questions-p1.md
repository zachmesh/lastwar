---
title: Open questions part 1
created: 2026-11-23T06:11:49Z
modified: 2026-11-23T06:11:49Z
version: 0.1.0
sequence: 44
description: Donation Count replenishment mechanism - rate, cap, timer link, and whether the count resets at the
---
## Open questions

- Donation Count replenishment mechanism - rate, cap, timer link,
  and whether the count resets at the trade-day reset or only
  refills (answered in part 2026-11-03 2014: no reset jump,
  see the sixth data point below; the 19:00 phrasing is
  superseded by the 02:00 UTC boundary per the 1932
  correction)
  (GitHub Issue #160; measurement owed: short-interval reads
  across one cooldown cycle). Second confirmation 2026-11-02
  0545: about 8 counts back over about 2 hours 40 minutes after
  an arithmetic 0 at about 02:59, consistent with the roughly
  1-per-20-minutes two-endpoint estimate, NOT a measured rate.
  Third data point 2026-11-02 0719: live 5/30 at 07:19 after
  the 0545 1/30 read, with no donations landed in between
  (0621 made none), about 4 back over about 1 hour 34
  minutes - consistent with the roughly 1-per-20-minutes
  estimate, NOT a measured rate, and this run does not close
  the day on arithmetic.
  Duplicate Issue #174 is noted on #160 for the daily retro to
  consolidate, not self-closed. The re-read rule for a
  replenishing count (re-read after the timer; donate again if
  above zero; a live 0 read closes only that unit, not the day,
  until the model says otherwise) is still unrecorded. Fourth data point 2026-11-03 0621: live 3/30 at entry after the 0521 1/30 close, about 2 back over about 54 minutes, rate still NOT measured. Fifth data point 2026-11-03 0920: live 9/30 at entry after the 0621 1/30 close, about 8 back over about 2 hours 52 minutes, so the allowance regenerates over time and is not a fixed daily 30; the 29/30 throttle hypothesis does not explain a regenerating allowance on its own, and the rate is still NOT measured. Sixth data point 2026-11-03 2014: live 21/30 at entry after the 1322 1/30 close, about 20 back over about 6 hours 50 minutes, about 2.9 per hour, consistent with the roughly 1-per-20-minutes estimate, NOT a controlled rate measurement. The interval straddles the trade-day boundary (about 18:00 local) with no donations landed in between (the 1421 unit made none), and the count read 21/30, not 30/30, so no reset-to-full jump occurred at the boundary: the count only refills. The alliance-wide footer did reset (Tech Donation Today 9000, new trade day, against the 1322 8000), so the footer and the Donation Count follow different boundary rules. Seventh data point 2026-11-03 2340: live 11/30 at entry after the 2014 1/30 close, about 10 back over about 3 hours 20 minutes, about 3 per hour, consistent with the roughly 1-per-20-minutes estimate, NOT a measured rate.