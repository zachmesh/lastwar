---
title: Survivor intake queue run 1729
created: 2026-11-10T01:29:00Z
modified: 2026-11-10T01:29:00Z
version: 1.0.0
description: Ticker-1704 survivors unit - gate line not verified, no recruit taken in, R2 third-strike blocker persists
status: partial
grounded_in:
  - source: live game screen on the owner Mac mini, 2026-11-09 17:19-17:29 PT
---

# Survivor intake queue run 1729 (ticker-1704)

Unit: survivors-2026-11-09-1403. Status: partial.
Activity: survivor-intake.

## Entry

- Base screen, panned to the front gate (the walled entrance
  with the Zombies sign, bottom of the base view). Two "?"
  bubbles stand near the gate, just above the "Build: Oil
  Well [0/1]" banner; a third "?" bubble was visible in the
  pre-pan view. No survivor figure was verified before any
  tap - the figures sit in the strip the banner covers, and
  the small-window view is too coarse to pick a figure out
  from its bubble.

## What was done

- Figure tap 1 (small window, norm 257,845, below the middle
  "?" bubble): no change, no card, no dialog.
- Fullscreen attempt: green zoom button entered native
  fullscreen (1920x1080) for a larger view. Figure tap 2
  (norm 406,850) opened the Build menu (Economy tab) instead
  - the tap landed on the "Build: Oil Well" banner hitbox,
  which covers the figure strip. No build was started and
  nothing was spent; the panel was closed with a map tap.
- Bubble tap (norm 395,819, directly on the left "?" bubble):
  no change, no card, no dialog.
- Per rule R2 the tap method ended after the second
  no-change tap on the gate line. No survivor card or dialog
  opened in this unit, so no recruit was taken in and Quick
  Dispatch did not run (there was no intake to dispatch).
- Exited fullscreen via View menu, Exit Full Screen; the
  game is back in its 642x951 window.

## Closing reads

- Gate line: 2 "?" bubbles visible at close, figures
  unverified, recruits taken in 0, line state unverified.
- Resources at close (HUD): food 556.6M, iron 881.6M, coin
  53.6M, diamonds 6,137, stamina 96.

## Outcome

Partial, verified no. The line could not be verified and no
recruit was taken in. This is the same failure mode as the
22-of-22 partial run of 2026-10-28 to 2026-10-31 recorded in
the activity profile (gate line not found or not verified,
Quick Dispatch never run) - the R2 third-strike blocker
persists. The named re-read unit is
survivors-2026-11-09-1803 (not_before 18:03 PT); the
tracker is left untouched so survivors stays due. The
re-read unit should try a different entry route for the
gate figures - the banner-covered strip at the bottom of
the base view is the binding problem, and a camera angle
that puts the gate figures clear of the banner is needed
before tapping again.

## Red lines

- No diamonds or money spent. No build started. No other
  activity's work touched. The Build menu was opened by a
  mis-tap and closed untouched.

## Result stats

- target 1, achieved 0, resources_gained none, costs 0
  stamina plus about 10 minutes, verified no,
  blocker_category e (repeated blocker - gate line not
  verified, same failure mode as the 2026-10-28 to
  2026-10-31 run), survivors_recruited 0, line_verified no,
  quick_dispatch_run no, device_takeovers 0
