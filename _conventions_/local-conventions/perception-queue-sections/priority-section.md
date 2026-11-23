---
title: Priority
created: 2026-11-23T09:03:33Z
modified: 2026-11-23T09:03:33Z
version: 0.1.0
sequence: 14
description: Produced units are ordered by a score, not by the slot that bore them -
---
### Priority

Produced units are ordered by a score, not by the slot that
bore them -

```text
priority score = deadline pressure x value / expected duration
```

- **Deadline pressure** rises as the time left before the
  item deadline approaches one unit duration plus one retry -
  inside that band the unit is priority 1, expiry-critical.
  Items with no deadline carry the lowest pressure.
- **Value** is what the item visibly carries - duel or phase
  score first on scoring days, then resources, then progress -
  read from the observation, never assumed.
- **Expected duration** is the profile learned estimate, so a
  cheap quick claim outranks a long grind of equal value.
- Dependencies and cooldowns gate before the score applies - a
  unit whose precondition is unmet (no empty truck slot, a drill
  ground still full) is not produced until the observation shows
  the precondition met, and a profile inside its cooldown does
  not refire.
- The score maps onto the queue priority classes of the queue
  design (1 expiry-critical, 2 windowed, 3 standard, 4
  background); ties break by deadline, then by age, exactly as
  the executor pick already does.

