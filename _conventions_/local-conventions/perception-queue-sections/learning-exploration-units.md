---
title: Learning - exploration units
created: 2026-11-23T08:37:03Z
modified: 2026-11-23T08:37:03Z
version: 0.1.0
sequence: 16
description: A candidate gets exploration units, ahead of any execution -
---
### Learning - exploration units

A candidate gets exploration units, ahead of any execution -

- The first exploration unit is read-only about the task
  itself - it enters by the discovered surface, and learns and
  records the entry point, the mechanism, the rewards, the
  cost, the cycle, the deadline shape, whether it scores
  anywhere, and the live read that would verify it.
- Where acting on the candidate would touch a price, diamonds,
  or any red line - or where the rules are still unclear after
  the read - exploration stays learn-only. The candidate is
  named in that day round summary for the owner, and no
  execution unit is produced until the mechanism is clear.
- A candidate that one exploration pass cannot resolve stays
  `exploring` and is re-perceived on the next pass - it does not
  age in silence (rule R5 applies from its first day).

