---
title: How it is done part 2
created: 2026-11-23T07:24:27Z
modified: 2026-11-23T07:24:27Z
version: 0.1.0
sequence: 6
description: Closing-boarding rule, learned 2026-11-11 0209 - boarding closes about 5 minutes before departure - the platform
---
- Closing-boarding rule, learned 2026-11-11 0209 - boarding closes about 5 minutes before departure: the platform plus buttons were present at timer 00:05:19 and gone at 00:04:55, and the banner read 00:01:13 at about 02:03:20 for a close about 02:04:30. When the banner is under about 2 minutes, tap the carriage-2 plus FIRST and read the metadata after - the standing rule (carriage 2, 3 Trade Contracts) is already known and the platform screen itself shows the occupancy. A metadata read must never sit between the platform open and the boarding tap while the banner is under about 2 minutes. The 0209 unit lost the boarding to a metadata read in that window; the account missed the train. The queue's pick order does not see the boarding close either - filed as tooling Issue #623.
- After the ride, the carriage reward arrives as an Event category
  mail titled Train arrival reward, with a Claim button on the mail.
  Claim it there - the reward does not credit silently. Claiming
  briefly opens the train DETAILS screen under a congratulations
  banner listing the granted items. Departure and arrival also
  generate plain notice mails about the conductor train in the same
  Event category, with no attachments.
- Historical note - on the first boarding (2026-10-25 midday, before
  the standing rule) the carriage was picked by its reward set and
  occupancy; carriage 1 held the richest set and the fewest riders,
  2 of 7 before boarding. The standing rule above now fixes the
  choice at carriage 2.

