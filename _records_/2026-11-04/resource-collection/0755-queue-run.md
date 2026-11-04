---
title: Harvest queue run 0755
created: 2026-11-04T07:55:00-08:00
modified: 2026-11-04T07:55:00-08:00
version: 1.0.0
description: Ticker unit harvest-2026-11-04-0603, partial, farmland +2.6M and HUD third value +3.0M verified, full sweep incomplete
status: partial
grounded_in:
  - source: live game screens on the owner Mac mini, 2026-11-04 07:43 to 07:55 PST
---

# Harvest queue run 0755

Unit: harvest-2026-11-04-0603, executor ticker-0734.
Session window: 2026-11-04 07:43 to 07:55 PST, device sessions
cc-430 (donations unit, session dropped between units) and
cc-431. Token re-acquired at 07:51 after the first 15 minute
lease expired; no other executor held the token.
No different-device dialog appeared. No diamonds, money,
speedup items or paid button touched. No building or research
started, no assembly, no teleport.

## Entry route - Alliance menu back arrow corrected

- The unit started on the Rallied Attack panel left open by
  the donations unit. Both panel X buttons closed cleanly
  (Alliance Tech panel, then Alliance Techs tree).
- The Alliance menu back arrow did NOT respond at (106,910)
  (two taps, no change) nor at (106,925) (one tap, no change).
  Visual grounding on the menu screenshot placed the arrow
  centre at (161,935); a tap there returned to the base on
  the first try. Next unit: use (161,935) for this back arrow,
  not the left-edge estimate (106,910).

## What was collected - verified by HUD deltas only

- Base HUD at entry (live screenshot reads): first value
  412.6M, second 745.8M, third 12.2M, total power 150,028,269.
- Farmland tap at (364,481): first HUD value 412.6M to
  415.2M (+2.6M) on the next screenshot. Per the standing
  farmland rule one tap collects all farmland bubbles; the
  +2.6M is the verified gain, consistent with the 0413
  unit's +2.0M farmland tap.
- Left-side tap at (88,406): third HUD value 12.2M to 15.2M
  (+3.0M) on the next screenshot, and the left-side buildings
  showed tall orange bars on that same screenshot (normal
  buildings again on the following screenshot). The +3.0M
  HUD delta is verified; the bubble identity behind it is
  NOT separately verified, so no bubble count is claimed
  for it.
- Total HUD-verified gain in this unit: first value +2.6M,
  third value +3.0M.

## What collected nothing (method lesson, Issue #250)

- Tap at (90,448) selected Gold Mine Lv.30 (label and info
  icons shown, HUD unchanged): a building selection, not a
  bubble. This repeats the 0413 pattern - small icons above
  the left-side buildings are building markers at this
  screenshot resolution, not reliably collectible bubbles.
- An empty-ground tap at (500,700) deselected the Gold Mine;
  no panel was opened and nothing was spent.

## Sweep coverage

- Left edge: viewed after a (300,500) to (600,500) drag;
  the two taps above are the only left-side attempts.
- Right side (Capitol, VS, Season II header area): viewed
  after a (600,500) to (300,500) drag; no collectible
  bubbles seen, only building markers and red-dot badges.
- Top edge (hero statues, Eiffel Tower, ferris wheel):
  viewed after a (500,300) to (500,600) drag; no collectible
  bubbles seen.
- Bottom Season 2 zone: NOT swept as main-base harvest,
  per the 2026-11-01 rule (its bubbles are not main-base
  harvest).

## What was not done (partial, tracker untouched)

- The full edge-drag sweep of the 2026-11-01 rule was not
  completed to zero remaining: EXP, screw and drone-component
  bubbles were not located or verified, and the remaining
  left-side bubbles were not distinguished from building
  markers. The next harvest unit resumes from the sweep,
  with the back-arrow correction (161,935) and the
  marker-confusion caution above as its first notes.
- No truck top bubble was claimed; truck work belongs to
  the trucks unit under one-unit-one-type.
- No diamonds, money, speedup, or paid button was touched.
  No Delete All, no assembly, no teleport. No Craft, no
  building, no research was started.

## Evidence and follow-up

- Evidence: this file; base screenshots before and after
  each verified HUD move.
- Follow-up: Issue #250 (tooling, bubble-grounding
  confusion) already covers this failure mode; this unit's
  evidence is noted here and will be commented on #250
  rather than filed as a duplicate.
- Result stats: target full base sweep, achieved 2 HUD-verified
  gains (first value +2.6M, third value +3.0M), verified yes
  for the HUD deltas, blocker_category c (tap method:
  remaining bubbles not distinguished from building markers).
