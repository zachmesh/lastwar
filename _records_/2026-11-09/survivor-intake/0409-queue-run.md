---
title: Survivor intake queue run 0409
created: 2026-11-09T12:09:00Z
modified: 2026-11-09T12:09:00Z
level: L0
version: 1.0.0
description: Ticker-0404 survivors unit, one gate visitor processed, gate line clear on closing read
status: verified
---

# 0409 queue run - Survivor intake

Executor: ticker-0404. Unit: survivors-2026-11-09-0203.
Session window about 04:06 to 04:09 America/Los_Angeles.
Computer session cc-216 on the owner Mac mini.

## Performed

- Entry snapshot, read live on the opening base screen:
  food 540.1M, iron 864.9M, coin 42.9M, diamonds 13.22K,
  total power 149,217,331, window 642 by 951. LastWar
  already frontmost; no different-device dialog, no login
  or verification demanded.
- Fresh grounding on the opening frame located a white
  bubble at norm 540,652 and a small figure below it at
  norm 535,691, at the front gate by the yellow ZOMBIES
  sign. The first click attempt failed before dispatch
  (stale_observation, no input sent); the figure was
  re-grounded on the fresh frame at norm 534,692 and
  tapped there.
- The tap opened a Friendly Visitor dialog, not a recruit
  card: "Commander, we've noticed that your resources
  haven't been collected in time, Please enable
  notifications to reduce possible losses." Cancel was
  tapped at norm 334,762; nothing was enabled and the
  dialog closed back to the base screen. The bubble was
  read as a question mark at this size, but the dialog
  proves a visitor; the mark may have been an exclamation
  mark misread small, matching the profile's
  visitor pattern.
- Closing re-ground of the gate area found no
  question-mark bubble remaining at the gate. One
  remaining white bubble at norm 768,275 sits above the
  Gear Factory in the upper-right built area; its figure
  point at norm 790,335 was tapped once and selected
  Gear Factory Lv.20 (building radial, paw and hammer
  buttons, green up-arrow), opening no card or dialog.
  That bubble is a building bubble, not a survivor. Per
  rule R2 the method at that point ends after the one
  no-change tap; it was not tapped again. An empty-road
  tap at norm 480,700 deselected the building cleanly,
  with no panel opened and no action taken from the
  radial.
- No survivor was recruited and no recruit card opened;
  the one figure processed was a dialog visitor with no
  building post, so no Quick Dispatch gap arises from
  this unit under the 1644 refinement (Quick Dispatch
  follows an intake with posts, not a dialog visitor).
  The truck dialog on screen ("The truck is full,
  waiting for your command", later "Supplies are fully
  loaded, please claim them") is truck work, not this
  unit's type, and was left untouched.

## Closing reads

- Gate line: clear as observed in this view - no
  question-mark bubbles at the gate on the closing
  screenshot, and the one figure seen there this unit
  was processed. Visitors processed 1, recruits 0.

## Outcome

Done. Gate line verified clear in this view; the one
waiting figure was a visitor, handled with nothing
enabled and nothing spent.

## Result stats

- target 1, achieved 1, resources_gained none,
  costs 4m_wall_no_stamina, verified yes,
  recruits 0, gate_line_verified true,
  device_takeovers 0, visitors_processed 1
