---
title: Item 7. VIP daily claims, Daily Freebie and login chest
created: 2026-11-23T09:03:19Z
modified: 2026-11-23T09:03:19Z
version: 0.1.0
sequence: 27
description: Verdict - proven complete on 2026-10-30 and proven unclaimed on 2026-10-31, both from live reads.
---
### Item 7. VIP daily claims, Daily Freebie and login chest

Verdict - proven complete on 2026-10-30 and proven unclaimed on
2026-10-31, both from live reads.

- 2026-10-30, unit vip-2026-10-30-1900, done - the Daily Freebie
  was claimed (puzzle times 2, food, iron and coin crates times 13
  each) and the login chest was claimed, with the points bar
  moving live from 1,575,260 to 1,575,460 of 2,000,000, a plus 200
  gain on a 54 day streak
  (`_records_/2026-10-30/vip-rewards/2042-queue-run.md`).
- 2026-10-31, unit vip-2026-10-31-1900, partial - the VIP screen
  was reached (55 day streak, points read 1,577,870 of 2,000,000)
  and the Daily Freebie Claim button did not respond to five input
  variants, each verified by a second screenshot. The login chest
  was then not tapped at all, because the freebie claim had not
  gone through first, so both items closed unclaimed in that unit
  (`_records_/2026-10-31/vip-rewards/2117-queue-run.md`). The
  points difference against the previous day read cannot be
  attributed from the records and is not explained here.

Prevention rule 7 - the VIP unit runs first after the 19:00 reset
and attempts the Freebie and the login chest independently, each
with live points read before and after. One unresponsive button
never skips the other item, and a failed claim re-enters the
master checklist for the pre-reset sweep instead of waiting a
full day.

