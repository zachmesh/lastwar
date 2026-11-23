---
title: Per-unit measurement
created: 2026-11-23T08:37:05Z
modified: 2026-11-23T08:37:05Z
version: 0.1.0
sequence: 36
description: Every unit already closes with a structured result (section 5).
---
### Per-unit measurement

Every unit already closes with a structured result (section
5). The retro mechanism fixes the `result.stats` keys every
task type must fill, so outcomes are comparable across units
and days -

| Key | Meaning |
|---|---|
| `target` | the quantity this unit set out to reach - a count, a quota, a threshold |
| `achieved` | the quantity actually reached, read live in the same unit (rule R1) |
| `resources_gained` | what the unit gained, itemised by resource type as displayed |
| `points` | score gained, for scoring types (duel, Arms Race, radar) |
| `costs` | what the unit spent - its duration, stamina, items consumed |
| `verified` | whether the closing figures are same-unit live reads - yes or no |
| `blocker_category` | when the unit did not reach its target, the miss audit root cause class - a window closure, b crowding out, c tap method, d inference over live read, e repeated blocker, f missing precondition, g true red-line miss, h by-design partial, i owner-named without escalation |

`duration_seconds`, `attempts` and the `claimed` list are
already core result fields and are not repeated in stats. A
unit that closes without its required stats keys is counted as
unverified in the retro aggregation, exactly as a unit whose
`verified` reads no - producing the numbers is part of the
work, not paperwork after it.

