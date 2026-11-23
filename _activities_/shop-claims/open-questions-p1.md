---
title: Open questions part 1
created: 2026-11-23T07:18:19Z
modified: 2026-11-23T15:29:30Z
version: 0.2.0
sequence: 25
description: Whether the free Hot Deals pack rotates its contents by day.
---
## Open questions

- Whether the free Hot Deals pack rotates its contents by day.
- What the dark rock item in the Season Weekly Pass pickup is -
  coal or titanium alloy; the tile only showed 10.0K.
- Monthly Pass Days Left boundary: the 0538 read of 13 at 05:36 local follows the 0407 read of 14 at 04:07 local the same day - the decrement falls between 04:07 and 05:36, so the daily boundary for the Monthly Pass is unread; the next Mall re-read must record Days Left with its time. (2026-11-09 0447 update: Days Left read 13 at 02:18 and 12 at 04:47 inside the SAME reset day, so the counter ticked between 02:18 and 04:47 local with no reset between - the decrement is a time-of-day tick, not a reset-day tick. Combined with the 2026-11-08 window (04:07 to 05:36), the boundary narrows to between 04:07 and 04:47 local IF it is a fixed time of day; that fixed-time reading is an inference from two days, not a verified exact time. No cause is asserted for the tick.) (2026-11-10 0440 update: Days Left 12 at 02:14 to 11 at 04:40 inside the same 18:00 cycle, and Rewards Left 12 to 11 with it; the tick falls inside the 04:07-04:47 window again, consistent with the fixed-time inference; cause still unmeasured, recorded as observed, not attributed.) (2026-11-11 0656 update: Days Left 11 at 02:49 to 10 at 06:56, Rewards Left 11 to 10 with it - the tick falls inside the 04:07-04:47 window a third time, consistent with the fixed-time inference; cause still unmeasured, recorded as observed, not attributed.) (2026-11-11 1531 update: Days Left 10 and Rewards Left 10 at 15:31, unchanged from the 0656 read at 06:56 - no further tick intraday, consistent with a single early-morning tick.) (2026-11-22 update: CLOSED by expiry - the Monthly Pass is NOT owned as of the 0234/1059 reads (see the 2026-11-22 section below); no Days Left countdown exists to track until a pass is bought again.)
- Shop check-in banner free gift: entry unproven. The HOT DEALS carousel banner 2 offers a FREE GIFT ("Claim your ... today!") and FREE TOMORROW (x5, x5, x5, "Randomly obtain one"); one Go tap produced no navigation in both the 1449 unit (three taps) and the 2212 unit (one tap). The Events-hub route is a dead end (1500 events unit: no check-in tab in the hub). The remaining idea is a foreground-click attempt on the shop Go button. Tracked on Issue #553 (knowledge).

2026-11-23: answered, and never to be tested again - one click on Go opened the web store in Chrome and paid nothing (`_records_/2026-11-22/shop-claims/1511-queue-run.md`); never click Go; see the [rule digest](rule-digest.md) rule 9.
