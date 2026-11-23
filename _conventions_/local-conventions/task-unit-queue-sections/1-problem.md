---
title: 1. Problem
created: 2026-11-23T08:37:05Z
modified: 2026-11-23T08:37:05Z
version: 0.1.0
sequence: 2
description: The 3 segment schedules work, but each segment run is one long subagent session, and the
---
## 1. Problem

The 3 segment schedules work, but each segment run is one long subagent
session, and the evidence of 2026-10-27 and 2026-10-28 shows the cost.

- Segment runs take 37 to 50 minutes of wall time (segment 1 of
  2026-10-27 22:03 finished at 22:40, segment 3 of 18:57 at about
  19:46). One window, one game - the whole routine serializes behind
  whichever run is active.
- Segment 2 of 2026-10-28 02:30 found a separate owner-directed Zombie
  Invasion session controlling the same Mac window and had to stand
  down, deferring mail, gifts, VIP, train and star-ceremony to the next
  cycle. Contention is handled by surrender, not by queueing.
- Expiring work has no way to jump the queue. On 2026-10-27 the owner
  had to ask manually at 18:43 because a free shop pack and the VIP
  freebie were about to lapse at the 19:00 reset while the long runs
  were still blocked or busy.
- A dead executor strands its work. The outcome_unknown control lock of
  2026-10-26 to 2026-10-27 froze 18 consecutive segment runs; inside a
  long run, a mid-run death loses the whole segment, not one item.

