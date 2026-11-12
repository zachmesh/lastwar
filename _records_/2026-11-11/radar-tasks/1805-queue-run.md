---
title: Radar queue run 1805
created: 2026-11-12T02:14:00Z
modified: 2026-11-12T02:14:00Z
version: 1.0.0
description: Ticker-1800 radar unit - entry not reached, rotating shortcut slot opened Special Forces and Tech instead; stack posture unexecuted, no tasks completed, nothing claimed
status: unverified
---

# Radar - ticker-1800, 18:05 to 18:13 PST

Unit radar-2026-11-11-1403, executor ticker-1800. Status
partial: the radar screen was never reached, so no radar task
was completed or claimed. Computer session cc-650, windowed
642x951 play throughout. No device dialog, no login demand,
no Touch ID, no password typed.

## Posture

- tools/duel.py --json at 18:04: duel day 4, theme Train
  Heroes, radar_posture stack. On a stack day radar tasks
  are completed but NOT claimed, and map pins stay untapped.
- The unit file's window text still reads "duel day 3 -
  radar release" - stale against the live day-4 stack
  posture. The live duel.py read governs; a release-day
  claim here would have been wrong.

## What happened

- The unit was already past its expiry when claimed
  (expires_at 2026-11-12T02:03:00Z, claimed about 18:05
  PST) - a late start, counted as late in the stats.
- Entry attempt 1: tapped the base left-column slot at
  normalized 47,242. It opened SPECIAL FORCES, not radar
  (squad hex tree, three MAX nodes, 2/10 nodes top row).
- Pivoted per rule R2: read the radar-tasks metadata entry
  section. It names the satellite dish icon in the base
  left icon column, a ROTATING shortcut, grounded at norm
  62,727 on 2026-10-29.
- Entry attempt 2: back to base, then tapped normalized
  62,727. The tap landed inside the Special Forces flow
  (SQUAD 4 screen, then the TECH screen on the next back
  tap) - the slot currently opens Special Forces / Tech,
  not the radar. The rotating shortcut has moved since the
  2026-10-29 grounding.
- Exited cleanly to the base screen with the bottom-left
  back arrow (normalized 163,915). Base HUD re-read on
  exit: food 693.3M, diamonds 13.22K, power about
  149,218,973, task "Build: Oil Well [0/1]".

## Incidental live read

- TECH screen (reached by accident, read only, nothing
  tapped): Development 84%, Economy 98%, Hero 68%, Units
  77%, Squad 1 Max Level, Squad 2 11%, Squad 4 0%,
  Alliance Duel Max Level, Intercity Truck 95%.

## Result stats

- target: radar tasks completed per the stack posture
  (complete, do not claim), stored tasks read
- achieved: 0 tasks - the radar screen was never reached
- resources_gained: none
- points: 0
- costs: about 8 minutes, no items spent
- verified: yes (the entry failure is observed on screen,
  not inferred; no closing figure is claimed)
- blocker_category: c (tap method - the rotating shortcut
  entry point did not open the radar on either attempt)
- follow_up: the next radar unit must re-ground the dish
  icon from a fresh base screenshot and verify the radar
  screen (level and points top left, stored tasks out of
  40) before any work; if the slot still opens Special
  Forces, the entry route changes and the blocker goes
  into the radar-tasks metadata per rule R2
