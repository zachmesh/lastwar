---
title: Queue Run 0706 Alliance Donations Re-read
created: 2026-11-08T15:22:00Z
modified: 2026-11-08T15:22:00Z
level: L0
version: 1.0.0
description: Donations unit donations-2026-11-08-1346, re-read after cooldown, partial - three donations verified live, final tap unverified behind a 19m33s timer, count replenishment observed
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-11-08 about 07:06-07:22 America/Los_Angeles
---

# 0706 queue run - alliance donations re-read (donations-2026-11-08-1346)

- Unit: donations-2026-11-08-1346, executor ticker-0704.
  Status: partial - three coin donations verified live by
  the Donation Count, but the closing count cannot be
  read: it sits behind a 00:19:33 cooldown timer, so the
  unit closes unverified per the hard closing rule in the
  alliance-donations metadata (rule R1). Tracker
  untouched; a named re-read unit is enqueued for after
  the cooldown (not-before 2026-11-08T15:40:00Z).
- Session: computer sessions cc-94 and cc-95 on the owner
  Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd).
  Session cc-94 dropped mid-unit during the cooldown
  wait (observe returned observation_unavailable); cc-95
  was started and LastWar re-selected with no game state
  lost. No device-access error, no different-device
  dialog, no login demanded.
- Entry route: the Alliance shield icon was tapped at its
  fresh measured centre on the live screenshot (937,725
  normalized) - the menu opened first try, no Drill
  Ground detour. The R2-changed route holds.

## What was read and done, live in this unit

- Alliance menu: [AP3x] The Apex, Overall Rating 5.0,
  Leader Abyss Apex, Power 13,393,268,780, Members 96/100,
  Language English. Tiles: Alliance Wars, Help (red dot),
  Alliance Gifts (red dot), Members, Alliance Store,
  Alliance Techs (red dot). Alliance Star (Event 40),
  Time Left 10:41:09.
- ALLIANCE TECHS, Development tab: Auto Rally Max Level,
  Quick Construction 8/10 (recommended marker), Great
  Helper Max Level, one node below at 2/10 (partially
  visible). Footer at entry: Tech Donation Today 4050.
- Quick Construction panel (recommended node): "Increased
  Building Speed for Allies", Donation Reward +20%, Tech
  EXP Required 1.3M/6.0M, Current +20%, Next Level
  +22.5%, Donation Reward EXP 50 + badge 50.
- Donation Count read live at entry: **4/30** (remaining).
  This is NOT the 0/30 the 0546 unit's arithmetic implied:
  the 0546 unit read 1/30, donated once, and left the
  count hidden behind its timer. The count ROSE from 1/30
  (0546, about 05:47) to 4/30 (this unit, about 07:08) -
  see the replenishment finding below.
- Three coin donations made and verified live, green
  Donate button, 900 coins each: count 4/30 to 3/30 to
  2/30 to 1/30, each step read live on its own
  screenshot. The diamond Donate button (2 diamonds) was
  not used. HUD badge count moved 302.0K to 302.3K
  across the three verified donations.
- Fourth tap: the coin button greyed immediately with a
  **00:05:07** cooldown timer and the badge moved to
  302.4K, but after the timer expired the count read
  **1/30** again - the tap did NOT land. Button-grey
  plus badge move is NOT landing evidence (same signature
  the 0546 unit relied on). The 5:07 wait fit inside the
  unit; the count was re-read live after it.
- Fifth tap (at 1/30, button green and active): the coin
  button greyed again with a **00:19:33** timer and the
  badge moved to 302.6K. The count is hidden behind this
  timer, which outruns the unit's remaining budget, so
  whether this tap landed is UNVERIFIED. No arithmetic
  final is claimed as the closing count.
- Alternative-surface re-read: Tech Donation Today footer
  read live at close: **4400** (entry 4050, delta +350).
  The delta does not reconcile with 50 points per coin
  donation over this unit's five taps, so the footer is
  NOT used as a count proxy - it is recorded only as an
  observed figure. The badge HUD (302.0K to 302.6K) is
  likewise recorded, not used as landing evidence.

## Findings (filed as a knowledge Issue, see below)

- Donation Count replenishes during the day. Evidence:
  the 0546 unit read 1/30 live at about 05:47 and made
  one donation (the footer moved 4000 to 4050 between the
  units, one donation's worth at 50 points, so that
  donation landed and the count went 1 to 0); this unit
  read 4/30 live at about 07:08. The count rose by at
  least 3 in about 80 minutes. The metadata's "day is
  done only when it reads 0 remaining" model does not
  cover a refilling count: a 0/30 read may be followed by
  more available donations later in the day. The
  replenishment rate and whether the 30 is a daily cap or
  a burst cap are still open.
- A greyed coin button with a cooldown timer, and a HUD
  badge move, do NOT prove a donation landed: this unit's
  fourth tap produced both and the count was unchanged
  (1/30) when the timer cleared. The 0546 unit's "landing
  verified" line used exactly that evidence and is
  therefore suspect, though the footer delta between the
  units supports its donation having landed.
- The burst pattern from 2026-10-26 repeats: after a few
  rapid donations the button greys with a timer (5:07,
  then 19:33 here) while the count is still above zero.
  Timer lengths vary and are not yet modelled.

## Follow-up

- Re-read unit donations-2026-11-08-1523 enqueued,
  not-before 2026-11-08T15:40:00Z (after the 00:19:33
  cooldown): it reads the Donation Count live and, if it
  still shows 1 remaining, donates once more; if 0, the
  day is done and the tracker is marked.
- Knowledge Issue #450 filed for the count-replenishment
  and grey-button evidence findings (see unit result).
- Tracker untouched (partial/unverified unit).
- No diamonds spent, no purchase tapped, no red line
  crossed.
