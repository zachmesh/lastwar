---
title: Queue Run 1839 Perception Scout Station and Wars Dot
created: 2026-11-09T02:45:00Z
modified: 2026-11-09T02:45:00Z
level: L0
version: 1.0.0
description: Scout unit scout-scout-2026-11-02-015, done - station re-check, Wars dot present with a rally waiting then cleared on return, fullscreen tap failure found
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-11-08 about 18:33-18:39 America/Los_Angeles
---

# 1839 queue run - perception scout station and Wars dot (scout-scout-2026-11-02-015)

- Unit: scout-scout-2026-11-02-015, executor ticker-1822.
  Status: done - both halves of the window were read live:
  the two train-preparation signals were checked (both
  absent) and the Wars dot was checked on the Alliance
  panel, in the Wars tabs, and again on return (present
  with a rally waiting, cleared after its timer expired).
  Observe-only; nothing claimed, fought, dispatched or
  purchased. Tracker untouched (scout is a perception
  regular; the tracker records no completion for it).
- Session: computer sessions cc-147 and cc-148 on the owner
  Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd). Session
  cc-147 dropped once mid-unit (describe returned
  observation_unavailable); cc-148 was started and
  LastWar re-selected, no game state lost. No
  device-access error, no different-device dialog, no
  login demanded. LastWar was already running.
  One control call failed first on a missing
  observation_id (stale_observation); retried with the
  returned observation_id, no input lost.
- Evidence: the appended section in
  `_records_/2026-11-08/perception-scout/observation.md`
  ("Station panel re-check and Wars dot PRESENT with a
  rally waiting, read live about 18:33-18:39 local").

## What was read, live in this unit

- Base screen about 18:33 local: power 149,209,253
  (unchanged from the 17:06 zero-sweep read; the 641,100
  step-down from the 16:58 read was already recorded by
  that unit, cause unexplained); food 490.8M, iron
  816.9M, coin 15.9M; diamonds 13.22K; cart 4,417;
  stamina 120; Season II 6d 23:23:04, VS timer 23:23:03.
  Left column: avatar Lv.30, hammer 2/4, flask 2/2,
  green face 6.5C, radio badge 4, white truck, survivor
  portrait badge 10, megaphone badge 4. Right column:
  Events badge 3 (was x2 at 17:04), VS, Season II,
  Alliance with a red dot, Mail, Inventory with a red
  dot, WORLD; 99+ badge. Wanted Boss badge 2 (was 1),
  timer 00:00:46. Furnace toast recurring, not read in
  full this unit.
- Both train-preparation signals absent: no train icon in
  the left column; no "Boarding closes in" banner under
  the resource bar - the banner area shows the Breaking
  News line and a Tactical Master Supply Box rumor ticker
  instead. No train is preparing in this window; the
  STATION PLATFORM screen has no live state to read.
  Fourteenth same-day no-train confirmation (thirteenth
  in chain scout-2026-11-02). The platform stays a
  preparation-only surface, carried not closed.
- Fullscreen tap failure, new method finding: this unit
  entered fullscreen (1920x1080) via the green zoom button
  first. Five taps on the Alliance button and its label
  in fullscreen (norm 699,701; 698,694; 635,694 twice;
  699,730) never opened the Alliance panel - each
  reported change_observed with a new surface but the
  panel never appeared on screen. The same button in the
  642x951 windowed geometry (after View menu, Exit Full
  Screen) opened at once at norm 896,702. Background
  input plus fullscreen geometry is the standing
  hypothesis for the mismatch; do NOT enter fullscreen
  for tap work until this is resolved. Filed as tooling
  Issue #475 by this unit.
- Alliance panel about 18:40 local: [AP3x] The Apex,
  Overall Rating 5.0, Leader Abŷss Apex, Power
  13,310,720,664, Members 95/100, Language English.
  Panel dots: Alliance Wars PRESENT (first time today
  since the 11:41 read), Help, Alliance Gifts, Alliance
  Techs. NO dot on Members, Alliance Store, Assemble,
  Strength Ranking, Alliance Events or Alliance City.
  "Important: President" banner at the top right,
  truncated and unread.
- Alliance Wars about 18:41 local: Rally Intel tab holds
  ONE rally - [AP3x]Kkkayyyyy, "Waiting for allies...",
  timer 00:00:39, Count/Limit (2/5), target Lv.30 CL-7
  Victim, 46km away. Achievements 8/16 Completed. No
  rally joined. Individual Intel tab reads "There are no
  ongoing Alliance Wars currently."
- Return-pass dot re-check about 18:43 local: Alliance
  Wars has NO dot; Help, Alliance Gifts and Alliance
  Techs still dotted. The rally's 39-second timer had
  expired by the return, so the dot clears when the rally
  leaves the waiting state.
- Unexplained floating text, observed only: "Allies are
  very grateful for your assistance" appeared twice in
  the mid-screen toast position after map taps at norm
  (635,694) in fullscreen. It may be a periodic alliance
  ticker rather than caused by the taps; no Help action
  was taken and nothing was claimed.
- Back-arrow grounding re-confirmed: the Wars page back
  arrow grounds at norm (62, 920) and the Alliance panel
  back arrow at (132, 936) on this 642x951 window; both
  returned at once. No back-arrow point is standing
  across screens or window sizes; re-ground fresh per
  screen.
- Resource bubbles standing on many buildings, observed
  only, not collected; the harvest regular owns
  collection.

## Red dot accounting

- Seen in this unit's window: Help, Alliance Gifts,
  Alliance Techs, Wars (present, then cleared on return
  - explained by the rally waiting, then expired).
  Explained 4, unexplained 0 for this unit's window.
  Other dots noted in passing, outside this unit's scope
  and previously explained to their owning regulars:
  Events badge 3 (up from x2 at 17:04; the 1646 unit left
  one count of the x2 unexplained and the third count is
  likewise open for the events unit, whose 1857 unit is
  queued), Mail, Inventory, Season II, 99+, hammer,
  radio 4, white truck, survivor 10, megaphone 4, Wanted
  Boss 2.
- Unknown items 2: the "Allies are very grateful" toast
  trigger, and the truncated "Important: President"
  banner on the Alliance panel.

## Carried forward

- Seventh same-day datapoint for Issue #212 (dot present
  11:41 with two rallies rallying; dot absent 08:44,
  12:42, 15:48, 16:15 with the list empty; dot present
  now with one rally waiting; dot cleared on return after
  its timer expired). It does NOT settle #212: on
  2026-11-03 the dot was present while both Wars tabs
  read empty. Issue #212 stays open; closure belongs to
  the daily retro, with evidence. Commented on Issue #212
  by this unit.
- Successor enqueued from this unit:
  scout-scout-2026-11-02-016, same window (station panel
  only, train entry and preparation state; Wars dot Issue
  #212). The station remainder stays carried for the
  next scout-alliance unit, which re-checks the two
  preparation signals first.
- Game left on the base screen, windowed 642x951 (exited
  fullscreen via View menu, Exit Full Screen).
