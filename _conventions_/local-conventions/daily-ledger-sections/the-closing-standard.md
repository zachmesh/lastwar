---
title: The closing standard
created: 2026-11-23T08:37:49Z
modified: 2026-11-23T08:37:49Z
version: 0.1.0
sequence: 2
description: Every line closes on a live read from that day - a counter, a balance, a
---
## The closing standard

- Every line closes on a live read from that day - a counter, a
  balance, a panel state seen on screen in the unit that closes
  it. Silence is not a close. A line that cannot be read closes
  as unverified and is named in the round summary, under rule R1
  of the [task unit queue design](task-unit-queue-design.md).
- A line with no producing unit is flagged unscheduled in the
  round summary, never silently absent (audit rule 4).
- The pre-reset zero sweep (queue design section 12) walks this
  ledger item by item twice before each reset, at about 17:30
  and about 18:30 local. A line not at zero gets a priority 1
  unit of its own type enqueued before the sweep closes, named
  in the sweep record.

