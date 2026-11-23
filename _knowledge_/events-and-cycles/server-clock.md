---
title: Server Clock
created: 2026-11-23T06:15:40Z
modified: 2026-11-23T06:15:40Z
level: L1
version: 1.0.0
description: Server time is UTC minus 2 hours, exact to the second, read from the To-do List header against capture stamps; server midnight is the 0200Z reset
status: unverified
grounded_in:
  - source: _records_/2026-11-22/perception-scout/2205-queue-run.md, two To-do List header reads against capture stamps on 2026-11-23, 0405 server time at 0605Z
  - source: _records_/2026-11-22/queue-planning/2205-zombie-siege.md, archived server clock readings of 2026-11-08 and 2026-11-21 and the 0200Z reset anchor
---

# Server clock

Server time is UTC minus 2 hours, exact to the second.

- Verified in game on 2026-11-23: the To-do List header read Server Time 04:05:26 on a capture stamped 06:05:26.78Z, and 04:05:34 on a capture stamped 06:05:34.78Z. Both reads differ from UTC by 2 hours and under one second (`_records_/2026-11-22/perception-scout/2205-queue-run.md`).
- Consistent with the archived readings: 10:17:10 server at about 12:18Z on 2026-11-08, with the weekly refresh 13:43:38 away at that read, and a header of 12:09:10 on 2026-11-21 whose labels the record notes ran 4 to 7 minutes late (`_records_/2026-11-22/queue-planning/2205-zombie-siege.md`).
- Consistent with the daily reset at 02:00Z, which is server midnight (same record, and the duel-day boundary in [Events and cycles](INDEX.md)).
- The planner's own prediction, 04:05 server at 06:05Z, was the check that could have failed; the scout read it.

To convert: UTC is server time plus 2 hours; Pacific is server time minus 6 hours while Pacific is on standard time. Zombie Siege at 23:15 server is 01:15Z and 17:15 PT (scout record).

Residual, unverified: two Wanted Boss countdowns to server 00:00 ending at 01:00Z would imply UTC minus 1 (`2205-zombie-siege.md`, row 7). The direct header reads above do not support it; it stays open.

Evidence note: both records were untracked in the live checkout when this was written, so the citations resolve there until the records are delivered to a branch.
