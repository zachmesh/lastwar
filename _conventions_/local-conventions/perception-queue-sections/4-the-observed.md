---
title: 4. The observed items schema
created: 2026-11-23T09:03:33Z
modified: 2026-11-23T09:03:33Z
version: 0.1.0
sequence: 10
description: Every signal a scout records is one observed item, written in the day observation file (section
---
## 4. The observed items schema

Every signal a scout records is one observed item, written in
the day observation file (section 8) as a structured block in
the same frontmatter style the queue already uses - values
colon-free except timestamps.

```yaml
observed_items:
  - surface: events/wanted-boss
    label: Wanted Boss Code 39 goals
    state: doable
    deadline: 2026-11-02T03:00:00Z
    est_value_or_score: best hit 1097397868, next goal tier unread
    suggested_unit: events
    redline_check: clear - fighting the boss spends stamina only
  - surface: store/building/crystal-shop
    label: Crystal Shop tab
    state: claimable
    deadline: ""
    est_value_or_score: daily free crystal, amount as displayed
    suggested_unit: new
    redline_check: claim only - any priced exchange stays unpressed
```

| Field | Meaning |
|---|---|
| `surface` | where it was seen, as a path of screen, section and sub-page |
| `label` | the item as the game names it, transcribed |
| `state` | one of claimable, doable, in-progress, locked, info-only |
| `deadline` | the visible expiry or reset it dies at, when the screen shows one |
| `est_value_or_score` | the visible value, amount or score it carries, when shown |
| `suggested_unit` | the regular id that should work it, or `new` when no model owns it |
| `redline_check` | what the red lines say about acting on it - clear, blocked and why, or owner-needed |

State vocabulary -

- **claimable** - a reward or pickup is ready to take now.
- **doable** - work can be done now - a fight, a dispatch, a
  donation, a boarding.
- **in-progress** - under way with a visible state or timer - a
  truck on the road, a train in preparation, a building queue.
- **locked** - visible but not open - level, phase, unlock or
  preparation gates.
- **info-only** - read for the record - a total, a ranking, a
  notice with nothing to claim or do.

