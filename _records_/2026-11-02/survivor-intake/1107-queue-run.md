---
title: Survivors queue run 1107
created: 2026-11-02T19:07:00Z
modified: 2026-11-02T19:07:00Z
version: 1.0.0
description: Ticker survivors unit partial, gate point grounded but no survivor dialog opened
status: partial
grounded_in:
  - source: game screen on the owner Mac mini 2026-11-02 11:07 to 11:22 PST
---

# Survivors queue run 1107

Unit: survivors-2026-11-02-1003, executor ticker-1104, status
partial. Session window 11:07 to 11:22 PST on the owner Mac mini.
No different-device dialog appeared; the game was live on the Mac
for the whole unit.

## What was done

- Opened the base screen and grounded the gate corner fresh in
  this unit: visual grounding put a question-mark bubble at norm
  72,662 and a survivor figure at norm 70,692 in the starting
  view.
- Tapped the grounded figure point norm 70,692. The tap changed
  the gate corner (the question-mark bubble cleared and a small
  portrait icon appeared at about norm 69,715), but no survivor
  dialog and no recruit card opened.
- Tried the 0734 re-read pointer next: two drags meant to pan the
  base down (norm 400,700 to 400,400, then norm 350,650 to
  350,350) produced no view change at all. Per queue rule R2 the
  drag-pan method is ended inside this unit after two no-change
  attempts, not repeated.
- Pivoted back to direct taps: a second tap at norm 70,692 again
  changed only the gate corner region and switched the base view
  to a wider framing with the left menu rail visible (Events,
  Capitol, VS, Season II, Alliance, Mail, Inventory, WORLD,
  HEROES). No survivor dialog and no recruit card opened from
  that tap either.
- No Upgrade, no Finish Now, no speedup, nothing bought, no
  harvest bubble tapped, no other activity worked from this unit.

## Why partial, not done

- No survivor was processed: 0 dialogs opened, 0 recruit cards,
  0 recruits taken in.
- The gate line was not verified clear and its state at close is
  unverified, not claimed clear. A visual-grounding call made
  mid-unit to recount the line timed out, so no recount figure
  is claimed.
- Quick Dispatch was not run: no recruit-card survivor was taken
  in during this unit, so no newcomer building post was created
  to dispatch. This does not change the standing Quick Dispatch
  blocker, and it is not a fourth identical partial on that
  blocker: the failure here is dialog-opening at a grounded gate
  point, after the drag-pan method was retired inside the unit.
- Tracker untouched, per the rule for partial units. The next
  tick re-produces survivors and resumes the gate work.

## Closing figures, read live in this unit

- Survivors processed: 0.
- Dialogs opened: 0. Recruit cards opened: 0.
- Gate line at close: unverified.
- Total Power visible in the closing wide view: 149,311,528
  (HUD reading, not a unit result).
- Resources gained: none observed.

## Re-read pointer for the next unit

- The grounded gate point norm 70,692 in the starting view does
  change the gate corner on tap but opens no dialog; the next
  unit should ground the figure fresh again and try the tap on
  the figure itself rather than the bubble point, and should not
  reuse the drag-pan method that failed twice here.
- The matching open issue is #168 (play): gate position pinning
  / confirming whether the line is currently empty. This unit's
  evidence is commented there, not filed as a new issue.
