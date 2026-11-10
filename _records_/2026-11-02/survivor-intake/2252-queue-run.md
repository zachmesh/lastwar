---
title: Survivors queue run 2252
created: 2026-11-02T22:52:00-08:00
executor: ticker-2234
unit: survivors-2026-11-02-2203
status: partial
---

# Survivors - 2026-11-02 22:52 queue run (ticker-2234)

## Outcome

Partial: 0 survivors processed, gate line unverified, tracker
untouched, so the next tick re-produces this regular.
No Quick Dispatch ran, since no intake happened.

## What was done

- Changed method under rule R2, following the 1948 unit's
  named re-read on open issue #168: instead of repeating
  the figure taps that selected a squad vehicle in 1948,
  this unit tried the bubble centre itself, on the
  undragged restored base view left by the harvest unit
  in this same pass.
- Visual grounding on that base screenshot returned a
  survivor figure at norm (448,580) and a question-mark
  bubble at norm (447,550). The bubble-centre tap at
  (447,550) selected Titanium Alloy Factory No.3 Lv.30
  (orange info button, building label), not a survivor
  card, dialog or recruit. The grounding point was a
  building area mislabelled as a survivor, the same
  mislabelling class as the 0636 radar grounding notes.
- Per rule R2 the method at this point ends inside the
  unit: no second tap was made at (447,550). An empty-
  ground tap at norm (750,800) deselected the building;
  no Upgrade, no panel action, nothing bought, nothing
  dispatched from any selection.
- No different-device dialog appeared; no login or
  verification was demanded. Computer sessions dropped
  twice in this pass (cc-265, cc-267) and were restarted
  (cc-267, cc-268) without disturbing the game.

## What was not done

- The gate line was not verified: whether survivors wait
  at the gate, and whether any figure seen is a recruit
  or a visitor, is unknown. This unit closes unverified
  on the line state, with a named re-read for the next
  survivors unit: do not reuse the (447,550) bubble
  point or the (448,580) figure point - both resolve to
  the Titanium Alloy Factory No.3 area on this camera
  view - and do not reuse the 1948 dragged-view figure
  points (485,680 / 490,690), which select a squad
  vehicle. The next unit must ground the gate line
  fresh on its own screenshot and verify a survivor
  figure before any tap.
- Issue handling: no new issue filed. This is the known
  gate-verification failure mode already open as issue
  #168; this unit's bubble-centre evidence is commented
  there, not filed anew.

## Red lines

Nothing spent, no paid button tapped, no building
started, no research, no dispatch, no other activity's
rewards claimed.

## Result stats

- target 1, achieved 0, resources_gained none,
  costs 0 stamina, verified no, blocker_category e
- survivors_processed 0, gate_line_verified no,
  device_takeovers 0
