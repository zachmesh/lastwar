---
title: Alliance Gifts Execution 2026-10-31 1105 Queue Run
created: 2026-10-31T18:27:00Z
modified: 2026-10-31T18:27:00Z
level: L0
version: 0.1.0
description: Gifts queue unit gifts-2026-10-31-1030 - partial, Alliance panel never opened, no gifts claimed, tracker untouched
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-31
  - source: owner directions of 2026-10-25, 2026-10-26 and 2026-10-28 - the standing routine, Mac control authorization and the task unit queue ticker
---

# Alliance gifts — execution, 2026-10-31 1105 queue unit

A single task unit, executed by executor ticker-1104 under the
task unit queue. Unit gifts-2026-10-31-1030, priority 3.
Session window about 11:05 to 11:27 America/Los_Angeles.
Status — performed in part: the Alliance panel was never
opened and no gift was claimed, so the tracker is
untouched and the next tick re-produces this regular.

## What was done

- Computer sessions cc-642 then cc-643 after a mid-pass
  session drop (observe returned observation_unavailable);
  the drop lost no game state and the game was
  re-selected cleanly. No different-device dialog
  appeared, no login or verification was demanded.
- The game was on the base screen in window mode
  (642x951). A tap at norm 932,720 opened the Drill
  Ground upgrade panel (Lv.25 to 26) instead of the
  Alliance panel, because the map view at that moment
  had the Drill Ground building under that point. The
  panel was closed untouched with its X button; no
  Finish Now, no Upgrade, no diamond or money spent.
- After the panel closed, the base view showed the
  right column clearly: Alliance (blue shield) above
  Mail and Inventory. Alliance taps at norm 935,670
  and 920,685 produced no panel and no observed
  change; the control guidance said background clicks
  do not reach some controls, the same failure mode
  as unit gifts-2026-10-30-2230.
- Title-bar fronting taps at norm 80,17 and at the
  documented title-text point 176,17 both failed to
  make LastWar the frontmost app; frontmost_app
  still read Google Chrome after each tap. Computer
  control sends background input and never brings an
  app to the front, so the Alliance button remained
  unreachable by background clicks in this pass.
  No title-bar tap entered fullscreen and no Esc or
  Return key was used.
- The game was left in window mode on the plain base
  view. No other regular was merged into this unit.
- Nothing else spent — no diamonds, no money, no
  speedup items burned, no building or research
  started, no Alliance Store purchase, no Assemble.

## Result statistics

- regular_claimed: 0
- premium_claimed: 0

## Close

- Next gifts unit should first get LastWar actually
  frontmost (for example by moving or minimising the
  covering Chrome window) before tapping Alliance,
  since background taps on that button repeatedly
  produced no change in this unit and in unit
  gifts-2026-10-30-2230, while map-figure taps did
  reach the game.
