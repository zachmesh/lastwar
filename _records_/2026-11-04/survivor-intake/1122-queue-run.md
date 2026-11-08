---
title: Survivor Intake Queue Run
created: 2026-11-04T19:22:00Z
modified: 2026-11-04T19:22:00Z
---

# Survivor intake, ticker-1104, 11:04 to 11:22 local

Unit survivors-2026-11-04-1003, status partial. The 15 minute unit
cap was reached mid-work. No survivor was recruited, no card was
opened, Quick Dispatch did not run, and the regulars tracker is
untouched, so the next tick re-produces this regular as a fresh
unit.

## What was verified live

- The gate line exists and holds waiting survivors. After dragging
  the base view, three question mark bubbles stood in a row above
  three small survivor figures on the road in front of the gate
  wall, seen clearly in a fullscreen screenshot and in a 4x crop
  of the cluster.
- No recruit card, dialog, or visitor dialog was opened in this
  unit, so recruits equal 0 by live read, not by assumption.
- The game window was left in native fullscreen (entered via the
  green zoom button during this unit). The next unit inherits
  fullscreen geometry. Taps dispatch in fullscreen, so no restore
  was attempted inside the unit cap.

## Method changes in this unit (rule R2)

- Windowed background taps on bubble points missed twice with no
  screen change, and a WORLD calibration tap also showed no
  change, so the method changed: the game was moved to native
  fullscreen and the survivor figures were re-grounded from a 4x
  crop of the cluster instead of inherited points.
- The crop-grounded figure tap did dispatch (the observation
  reported a visual change over the survivor area), but no card
  opened, and the view afterwards showed a panned base with no
  dialog. A focus guard blocked one tap while Google Chrome was
  frontmost, and the computer session dropped twice mid-unit
  (cc-449, cc-450) with recovery and no game state lost.
- The next unit must change method again before repeating this
  one: try the question mark bubble itself in fullscreen, or a
  long-press on a grounded figure, and re-ground from a fresh
  screenshot immediately before tapping, since the figures may
  shift between screenshots.

## Pass-level notes (ticker-1104)

- Own PRs checked first: records PR 273 for records/2026-11-04
  is MERGEABLE and CLEAN with no comments, so nothing was owed
  on it. Older records PRs 187, 256 and 265 name Owner
  lastwar-pr-integrator, not this job, and still conflict on the
  single file _logs_/repo-actions/action-log.jsonl
  (append-append at the tail); the integrator's own re-check
  notes leave them awaiting branch-side resolution, and main
  keeps advancing past them at each batch merge, so no
  resolution was attempted inside this ticker pass.
- Zombie Invasion was not seeded: the chain zombie-2026-10-28
  closed with unit 066 on 2026-10-30, the Events hub has no
  Zombie Invasion tab since, and the activity metadata forbids
  seeding a fresh chain until such a tab is seen live again.
- No diamonds, money, price tags, paid buttons, speedups,
  research, buildings, assembly or teleport were touched.
  Nothing was claimed.
