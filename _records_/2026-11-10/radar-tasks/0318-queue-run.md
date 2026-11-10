---
title: Radar tasks queue run 0318
created: 2026-11-10T11:18:00Z
modified: 2026-11-10T11:18:00Z
version: 1.0.0
description: Ticker-0304 radar unit, duel day 2 stack - entry blocked, dish icon not grounded, partial
status: unverified
grounded_in:
  - source: live game screen on the owner Mac mini, 2026-11-10 03:14-03:18 PT
---

# Radar tasks queue run 0318 (ticker-0304)

Unit: radar-2026-11-10-0203. Status: partial.
Activity: radar-tasks. Posture: stack (duel day 2, Base
Expansion; duel.py radar_posture stack, day ends 18:00 PT).

## Entry - blocked, two attempts, both delivered as map drags

- Attempt 1: visual-grounding point norm 34,324, method
  move, wait 1 second, click (the 2334 R2 pivot method).
  No radar opened. A gate toast appeared bottom-left,
  "...ies are fully loaded, ...e claim them" (the harvest
  gate toast already noted in the 0234 harvest record) -
  the tap landed on a map building/bubble, not the dish.
  The grounding point was a map element, not the dish.
- Attempt 2: the 2334 unit's freshly measured dish centre
  norm 52,694, same move-wait-click method. No radar
  opened. The base camera panned to the 1st Squad area -
  the tap was delivered as a map drag, the same failure
  mode the 2334 unit hit twice before its third attempt
  worked.
- The dish icon was not located on the current base view.
  The left edge strip (x 0-80, y 100-560, enlarged) shows
  only map content - resource bubbles, a red-panda pet
  icon, a chest icon - no UI shortcut column in frame.
  The camera has now panned twice during this unit and
  sits at the 1st Squad area; no further taps were made,
  so the view is left as-is for the next unit.
- R2 note: this is the first radar partial with this
  entry blocker today (the 2334 unit closed done). The
  next radar unit must arrive with a changed method -
  long-press variant, or re-centre the base camera first
  and re-ground the dish fresh - not a repeat of the
  move-wait-click at an inherited coordinate.

## What was done

- Nothing executed, nothing claimed, no pin tapped. No
  free stamina claim taken. No diamonds or money spent.
- The radar screen was never entered, so there are NO live
  reads from this unit: level, stored count, stamina,
  restore line, bar offer and pin inventory are all
  unread. Last-known state from the 2334 close (23:46 PT,
  explicitly not a live read): stored 1/40, pending
  rewards 9, stamina 70, radar points 348, restore 12
  tasks in 05:54:47, bar presenting Claim All with no
  Quick Execute offer. The 9 pending rewards stay stacked
  for the duel day 3 release unit; nothing was claimed
  on this stack day, as required.

## Closing reads

- Radar entered: no. Stored: unread. Pending rewards:
  unread (9 last-known). Stamina: unread (70 last-known).
  Radar points: unread (348 last-known). Restore line:
  unread. Bar offer: unread (Claim All last-known).
  Tasks executed 0, tasks claimed 0, pins inventoried 0,
  pins worked 0, free stamina claims 0.

## Outcome

Partial. The stack-day completion standard is not met -
the radar was never entered and no Quick Execute batch
ran. The tracker is left untouched, so the next tick
re-produces the radar regular and the work resumes as a
fresh unit with a changed entry method.

## Red lines

- No diamonds or money spent. No priced button tapped. No
  Claim All tapped on a stack day. No pin tapped. No other
  activity's rewards touched. The gate toast was observed
  only; no harvest bubble was collected.

## Result stats

- target 1, achieved 0, resources_gained none, costs 0
  stamina plus about 4 minutes, verified no,
  blocker_category c, tasks_executed 0, tasks_claimed 0,
  pins_inventoried 0, pins_worked 0, free_stamina_claims 0,
  device_takeovers 0, entry_attempts 2
