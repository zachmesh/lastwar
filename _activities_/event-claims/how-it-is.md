---
title: How it is done
created: 2026-11-23T07:24:24Z
modified: 2026-11-23T07:24:24Z
version: 0.1.0
sequence: 3
description: Open Events and scan each active event for claim buttons and red dots.
---
## How it is done

- Open Events and scan each active event for claim buttons and red dots.
- Recenter the base view FIRST (2026-11-22 0253): a panned base view hides the top-right Events button from its usual place, and the unit's usual-point tap landed on empty map. Candidate recenter control is the red circular-arrow icon above the green up-arrow (about (753,152)) - untested. Verify the Events button is visible before tapping it. Do NOT tap the green up-arrow at (845,186) as a recenter control - it is a RETRACT control for a placed object ("SPECORA X"): it opens a "DO YOU WANT TO RETRACT THE SPECORA X?" confirmation dialog (Cancel / Confirm / "Don't show me today"). Cancel was tapped immediately at (373,701) in the 0253 unit and nothing was retracted.
- Page through everything - the Events tab bar scrolls sideways, and
  the owner standing direction (evening of 2026-10-25) is to navigate
  through the pages to finish the red dots, not stop at the first
  page. Where a Claim shows, claim it.
- The hub renders slowly - after tapping a tab, wait a couple of
  seconds before reading the screen, or the previous page content
  will mislead the tap.
- Claim milestone and completion rewards that are already earned.
- Treat an animated or bouncing chest on the Events screen, an
  event card or an event detail page as an unclaimed reward until
  it has been opened and inspected. Do not stop at the rewards
  inside the first detail page. After claiming, return to the
  Events screen and scan again - the event sweep is complete only
  when no bouncing chest or reward red dot remains, or a visible
  chest is proven locked and its unlock condition is recorded.
  For Arms Race in particular, the three point chests are only
  one reward set and do not prove that all Arms Race rewards
  have been claimed.
- Record timed stage state without grinding it, unless the owner asked.

