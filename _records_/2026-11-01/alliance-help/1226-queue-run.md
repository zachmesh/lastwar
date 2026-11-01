---
title: Alliance help queue run
created: 2026-11-01T20:26:00Z
modified: 2026-11-01T20:26:00Z
version: 1.0.0
description: Help unit help-2026-11-01-1030 executed by ticker-1204, partial, Help entry route unresponsive to background taps in this session
status: partial
---

# Alliance help queue run 2026-11-01 about 12:26 PDT

- Unit: help-2026-11-01-1030, executor ticker-1204, status partial.
- What happened: alliance-help metadata read before acting. The
  game was already on the Alliance panel from the gifts unit,
  and the Help entry carried a red dot, so waiting requests
  were present.
- Help entry route, failed in this session: the Alliance panel
  Help button was tapped three times with no change - twice at
  the start of the unit (norm 629,467 and 695,471) and once
  more after re-entering the Alliance panel (695,471). The
  base-screen help bubble tile left of the Alliance shield
  button was tapped twice with no change either (norm 819,667
  and 819,675); the tile stayed visible and no "Allies are
  very grateful" toast appeared. The control layer itself
  advised after the second bubble tap that background clicks
  do not reach some controls and suggested a foreground
  element click or keyboard instead; the game canvas exposes
  no accessibility element for these controls, and a
  LastWar open_app request returned outcome unknown with no
  verified change, so no further identical tap was made.
- Changed method, per queue rule R2: after the two no-change
  Help taps the unit switched entry route to the base-screen
  bubble tile, and after that route also failed twice it
  re-entered the Alliance panel for one final Help tap
  instead of repeating the bubble tap. No Help All press
  happened, so no help count or points figure is reported.
- This is not a third consecutive partial for help: the
  previous help unit of the day (help-2026-11-01-0630)
  closed done, so no metadata rewrite is triggered by this
  unit under rule R2. The blocker is named here for the
  next unit: Help controls need a verified foreground
  session before tapping, since background input reached
  every other control used in this pass (Alliance, Gifts,
  Claim All, tabs, back arrows) but not Help.
- Tracker untouched (partial unit), per the queue rules: the
  next tick re-produces this regular.
- No different-device dialog, no login or verification
  demanded. No diamonds, money, speedups or paid buttons
  were used. The game was left on the Alliance panel.

## Result statistics

- helps_pressed: 0
- help_all_pressed: 0
- target: Help All pressed for waiting alliance requests
- achieved: 0
- resources_gained: none
- costs: about 4 minutes, no items consumed
- verified: no
- blocker_category: c
