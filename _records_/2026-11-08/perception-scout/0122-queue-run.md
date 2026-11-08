---
title: Queue Run 0122 - Perception Scout Alliance Remainder Star Settings Record
created: 2026-11-08T09:17:00Z
modified: 2026-11-08T09:17:00Z
level: L0
version: 1.0.0
description: Ticker-0104 scout unit, alliance remainder Alliance Star read, Record button blocked, Settings unwalked, partial observe-only
status: unverified
grounded_in:
  - source: live game screens on the owner Mac mini, 2026-11-08 about 01:13 to 01:22 local
---

# 0122 queue run - perception scout, alliance remainder

Unit scout-scout-2026-11-02-007 by ticker-0104, session
about 01:12 to 01:17 local, status partial, observe-only
throughout: nothing claimed, fought, dispatched, donated,
dug or bought; no ceremony reaction sent. Evidence in this
file and the appended section of the 2026-11-08
observation file.

## Entry

- The game was on the base screen (power 149,850,353,
  unchanged from the 0118 read minutes earlier). The
  Alliance icon tapped at norm 917,705, grounded fresh
  from the screenshot, opened the Alliance panel at once.
  This corrects the 0752 misfire: the icon centre is the
  entry point, not the label row at 903,750, which opened
  MY PROFILE.
- Alliance panel re-read live: [AP3x] The Apex, Power
  13,350,333,388, Members 96/100, red dots on Help and
  Alliance Gifts, Alliance Star (Event 40) Time Left
  16:36:27 falling to 16:35:08 during the unit.

## Record - blocked, first instance of this blocker

- Three background taps on the Record bottom button
  produced no change: 240,935, then 242,920 (icon
  centre), then 242,960 (label). Each observation after
  the tap showed the Alliance panel unchanged except
  for the ticking Star timer.
- The tool's click guidance after the second tap: background
  clicks do not reach some controls; use click_element
  with the control's visible label. click_foreground
  requires an element_number, which the game's
  Accessibility tree does not provide (one iOS content
  group, OCR text only - established by the 0752 unit).
- Per rule R2 the method is exhausted for this control
  inside this unit. This is the first instance of the
  Record-button blocker in this chain. The Record
  Member/Message/Event tabs are unwalked and carried to
  the successor.

## Alliance Star - read live

- The Enter button on the gold banner, tapped at norm
  771,836, opened the ceremony at once: "[AP3X]
  ALLIANCE STAR CEREMONY (EVENT 40)". Stage view with
  the hostess, the audience in blue helmets, a chest icon
  0/1 at top right, numbered tabs 1 to 5 and a gift icon
  at bottom right, a back arrow bottom left and a
  play/pause button bottom right.
- A bottom-left tap advanced the playback to slide 1:
  "S2 Big Shot - Texan Apex - Assist allies in the
  first kill of Doom Elite in S2 20 time(s) this week",
  49 hearts, 5 and 3 reactions; hostess speech "Let's
  leave our encouragement and blessings to the winners!";
  a reaction bar (heart and faces) open below the stage.
  Observed only - no reaction was sent.
- A second bottom-left tap advanced to slide 2 ("Little
  Sun", "Nuna Knuckles" named). Tabs 1 to 6 are visible
  on the slide-1 frame. The bottom-left button advances
  slides; it does not exit the ceremony.
- The chest 0/1 is observed only - claiming belongs to
  the star-ceremony regular, whose unit is already queued.

## Settings - unwalked

- Never reached: the ceremony exit was not found
  inside this unit, and the token window closed before
  a further exit route could be tried. Carried to the
  successor.

## Red dot accounting, this unit's walked surfaces

- Seen 4: panel Help dot, panel Gifts dot, base Alliance
  dot, Events x2 badge.
- Explained 4: Help dot maps to the help regular, Gifts
  dot to the gifts regular, the base Alliance dot is the
  roll-up of the panel dots, Events x2 to the events
  regular; units for all of these are already queued.
- Unexplained 0 in the surfaces actually walked.
- unmatched_labels: none in the surfaces actually walked.

## Unknown items, carried

- Record button unresponsiveness to background taps
  (blocker, first instance in this chain; successor must
  try a changed method - click_element is unavailable
  without an element number, so the next attempt should
  try a long-press or a foreground route if one exists).
- Ceremony exit route (no exit found - the back control
  advances slides; whether the ceremony exits after
  slide 6 or by another control is untested).
- The 13.22K second-row HUD figure identity (carried
  from the 0004 pass's entry read).

## Unwalked, carried to successor seq 008 of chain scout-2026-11-02

- Settings, Record Member/Message/Event tabs, plus the
  0048 remainder: Help page, Alliance Store page
  (read-only), Alliance City page, Wars Individual Intel
  tab, Gifts Premium tab, Assemble and Strength Ranking
  tiles. The station panel stays with the midday chain
  (successor 009, enqueued by the 0118 unit).
- No train summoned, no conductor role taken, no
  different-device dialog, no login demand. Game left
  inside the Star Ceremony playback (slide 2).

## Result statistics

- surfaces_walked 1, items_observed 10, red_dots_seen 4,
  red_dots_explained 4, unexplained_red_dots 0,
  unknown_items 3, target 3 (Alliance Star, Settings,
  Record tabs), achieved 1 (Alliance Star read; Settings
  and Record unwalked), resources_gained none, verified
  yes, blocker_category c (tap method - Record button
  unresponsive to background taps, first instance).
