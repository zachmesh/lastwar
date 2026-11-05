---
title: Harvest queue run 1101
created: 2026-11-04T11:01:00-08:00
modified: 2026-11-04T11:01:00-08:00
version: 1.0.0
description: Ticker unit harvest-2026-11-04-1003, partial, farmland +2.1M food and left-side +1.4M coin verified, full sweep incomplete at unit cap
status: partial
grounded_in:
  - source: live game screens on the owner Mac mini, 2026-11-04 10:48 to 11:01 PST
---

# Harvest queue run 1101

Unit: harvest-2026-11-04-1003, executor ticker-1034.
Session window: 2026-11-04 10:48 to 11:01 PST, device sessions
cc-446 (donations unit, session dropped between units) and
cc-448. No different-device dialog appeared. No diamonds, money,
speedup items or paid button touched. No building or research
started, no assembly, no teleport.

## Entry route

- The unit started on the Rallied Attack panel left open by the
  donations unit. Both panel X buttons closed cleanly
  (Alliance Tech panel at (848,213), then Alliance Techs tree
  at (848,150)).
- The Alliance menu back arrow responded at (161,935) on the
  first tap, confirming the 0755 unit's correction; the
  left-edge estimate (106,910) was not used.
- Donation panel state at entry, incidental: coin button still
  greyed with a 00:11:45 regen timer (down from 00:16:35 at the
  donations unit's close), consistent with the timer running.

## What was collected - verified by HUD deltas only

- Base HUD at entry (live screenshot reads): food 417.9M,
  iron 749.5M, coin 18.0M, 21.0M, 922.2K, 12.72K,
  total power 150,028,269.
- Farmland tap at (364,481): food 417.9M to 420.0M (+2.1M)
  on the next screenshot, and the farmland cluster's round
  value bubbles cleared. Per the standing farmland rule one
  tap collects all farmland bubbles; the +2.1M is the
  verified gain.
- Left-edge drag (300,500) to (600,500) shifted the camera to
  the left-side buildings. Left-side tap at (88,406): coin
  18.0M to 19.4M (+1.4M) on the next screenshot, food and
  iron unchanged. The +1.4M HUD delta is verified; the
  bubble identity behind it is NOT separately verified, so
  no bubble count is claimed for it. This replicates the
  0755 unit's left-side collection point.
- Total HUD-verified gain in this unit: food +2.1M,
  coin +1.4M.

## Sweep coverage

- Farmland cluster: collected, bubbles cleared.
- Left edge: viewed after the drag; one tap collected.
  Remaining small icons above the left-side buildings were
  not distinguished from building markers and were not
  tapped (the 0755 marker-confusion caution, Issue #250).
- Right side, top edge: NOT swept in this unit.
- Bottom Season 2 zone: NOT swept as main-base harvest,
  per the 2026-11-01 rule (its bubbles are not main-base
  harvest).

## What was not done (partial, tracker untouched)

- The full edge-drag sweep of the 2026-11-01 rule was not
  completed to zero remaining: EXP, screw and drone-component
  bubbles were not located or verified, and the right side
  and top edge were not swept. The unit cap (15 minutes
  from claim) and the mid-pass session drop left only about
  7 minutes of game time in this unit. The next harvest
  unit resumes from the sweep.
- No truck top bubble was claimed; truck work belongs to
  the trucks unit under one-unit-one-type.
- No diamonds, money, speedup, or paid button was touched.
  No Delete All, no assembly, no teleport. No Craft, no
  building, no research was started.

## Evidence and follow-up

- Evidence: this file; base screenshots before and after
  each verified HUD move.
- Follow-up: none new; Issue #250 already covers the
  bubble-grounding confusion, and this unit's left-side tap
  succeeded at the 0755 point rather than adding a new
  failure mode.
- Result stats: target full base sweep, achieved 2
  HUD-verified gains (food +2.1M, coin +1.4M), verified yes
  for the HUD deltas, blocker_category b (unit cap reached
  mid-sweep after the between-unit session drop).
