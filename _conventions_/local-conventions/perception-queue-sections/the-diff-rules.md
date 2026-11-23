---
title: The diff rules
created: 2026-11-23T08:37:03Z
modified: 2026-11-23T08:37:03Z
version: 0.1.0
sequence: 12
description: After each pass, the observation is diffed against three references - the regulars, the daily collection
---
### The diff rules

After each pass, the observation is diffed against three
references - the regulars, the daily collection ledger, and the
pool in all three states.

- **Known item, triggered.** When a trigger from the list above
  fires for a profiled item, a unit of its regular is produced
  through the shared (regular, planned_for) invariant - already
  queued, claimed or done for that trigger window means no
  duplicate. When the same item is already queued and a later
  observation raises its deadline pressure, the queued unit is
  raised in priority instead of duplicated - priority 2
  normally, priority 1 inside the expiry band of the priority
  formula.
- **Known item, already done.** When the observation shows a
  modelled line already satisfied - collected, claimed, boarded -
  no unit is produced, and the observation stands as the day
  evidence for that ledger line.
- **Unknown item.** An item whose suggested_unit is `new` enters
  the discovery protocol of section 6 - it is filed as a
  candidate and gets its exploration unit from there, never an
  execution unit directly. No unknown item ages unnamed - rule
  R5 applies to it from its first day.
- **Modelled but absent.** When the models expect something the
  screen does not have - an activity that has ended, a tab that
  is gone, a pass that expired - the diff closes the expectation
  instead of staging empty units against it. The closure is
  recorded in the observation and in the activity metadata, so
  the next planner run stops producing for a dead surface.
- **Contradiction.** When the screen contradicts a standing
  record - a count, a mechanism, a state the metadata asserts -
  the screen wins, the observation records the contradiction,
  and the metadata is corrected in the same session. Perception
  never defers to the file against the game.

