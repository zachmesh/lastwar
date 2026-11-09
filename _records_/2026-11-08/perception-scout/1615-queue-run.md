---
title: Queue Run 1615 Perception Scout Station and Wars Dot
created: 2026-11-09T00:15:00Z
modified: 2026-11-09T00:15:00Z
level: L0
version: 1.0.0
description: Scout unit scout-scout-2026-11-02-014, partial - station panel re-check, twelfth no-train confirmation, Wars dot absent with Rally Intel empty
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-11-08 about 16:09-16:15 America/Los_Angeles
---

# 1615 queue run - perception scout station and Wars dot (scout-scout-2026-11-02-014)

- Unit: scout-scout-2026-11-02-014, executor ticker-1604.
  Status: partial - the station window was fully walked
  observe-only and the Wars dot was read live, but the
  chain continues by design (the station remainder stays
  carried; the successor re-checks the two preparation
  signals first). No claim, fight, dispatch or purchase
  was made. Tracker untouched.
- Session: computer session cc-139 on the owner Mac mini
  (1c817413-83e2-0545-cb90-36d5e096a6bd). No device-access
  error, no different-device dialog, no login demanded.
  No screen-capture failure. One control call failed
  first on a missing observation_id (stale_observation);
  retried with the returned observation_id, no input
  lost. LastWar was already running and selected,
  verified by list_apps and observe before any input.
- Evidence: the appended section in
  `_records_/2026-11-08/perception-scout/observation.md`
  ("Station panel re-check and Wars dot absent, read live
  about 16:09-16:15 local").

## What was read, live in this unit

- Base screen about 16:12 local: power 149,850,353
  (unchanged from the 00:16, 04:16, 04:40, 08:45, 11:38,
  12:42 and 15:44 reads); food 490.8M, iron 813.3M, coin
  12.3M; second row 25.0M, 922.2K; diamonds 13.22K;
  cart 4,397; stamina 119 (was 113 at 15:44); Season II
  7d 01:48:45. Left column: avatar Lv.30, hammer 2/4,
  flask 2/2, green face 6.5C, radio badge 4, white
  truck, question marks, survivor portrait badge 10,
  megaphone badge 4. Right column: Events x2, VS,
  Season II, Alliance with a red dot, Mail, Inventory
  with a red dot, WORLD; 99+ badge. Furnace toast
  recurring, observed only, not read in full this unit
  (text cut at the screen edge in the capture; the
  1545 unit read it in full as [22/60]) - a red-line
  surface never touched.
- Both train-preparation signals absent: no train icon
  in the left column; no "Boarding closes in" banner
  under the resource bar - the banner area shows the
  High-temp Furnace overdrive line and a Breaking News
  line ("Breaking News: Intense battle...") instead. No
  train is preparing in this window; the STATION
  PLATFORM screen has no live state to read. Twelfth
  no-train confirmation in this chain (third 2134,
  fourth 0022, fifth 2304, sixth 0118, seventh 0440
  re-check, eighth 0845, ninth 1131, tenth 1223,
  eleventh 1534, twelfth this unit). The platform stays
  a preparation-only surface, carried not closed; the
  successor re-checks the two preparation signals first
  rather than re-panning.
- Alliance panel about 16:14 local: [AP3x] The Apex,
  Overall Rating 5.0, Leader Abŷss Apex, Power
  13,338,108,353, Members 95/100, Language English.
  Panel dots: Help, Alliance Gifts, Alliance Techs. NO
  dot on Alliance Wars, Members or Alliance Store.
  Assemble and Strength Ranking below the fold.
  Alliance Star (Event 40), Time Left 01:37:41.
  Bottom row: Record, Applicants, Alliance Star,
  Settings.
- Wars dot absent, rally list empty: Alliance Wars
  opened (observe-only) at about 16:15 local - Rally
  Intel tab reads "No Alliance Rally currently." No
  rally joined. This is the sixth same-day datapoint
  for the rally link (dot present 11:41 with two
  rallies rallying; list empty 11:44 after the timers
  expired; dot absent 08:44 with none seen; dot absent
  12:42 with the list empty; dot absent 15:48 with the
  list empty; dot absent now with the list empty). It
  does NOT settle Issue #212: on 2026-11-03 the dot was
  present while both Wars tabs read empty, so a rally
  does not explain the dot by itself. Issue #212 stays
  open; closure belongs to the daily retro, with
  evidence. Commented on Issue #212 by this unit.
- Return-pass dot re-check: after returning from Wars,
  the Alliance panel was read again at about 16:16
  local - Alliance Wars still has NO dot; Help,
  Alliance Gifts and Alliance Techs still dotted;
  Alliance Star Time Left 01:36:08. This closes, for
  this unit's window, the gap the 1131 unit left open
  (no return-pass dot read after the rallies launched).
- Back-arrow grounding re-confirmed: the Wars page back
  arrow grounds at norm (56, 938) and the Alliance
  panel back arrow at (183, 938); both returned at
  once. No back-arrow point is standing across screens;
  re-ground fresh per screen.
- Resource bubbles standing on many buildings, observed
  only, not collected; the harvest regular owns
  collection. Chat ticker lines "SunnySunflower : Lv.7
  [DanG]Roy..." and a Korean line seen, not read in
  full.
- Red dots in this unit's window: Help, Alliance Gifts,
  Alliance Techs explained; Wars absent. Explained 3,
  unexplained 0. Other dots noted in passing, outside
  scope and previously explained: Events x2, Mail,
  Inventory, Season II, 99+, hammer, radio 4, white
  truck, survivor 10, megaphone 4.

## Follow-up

- Successor enqueued from this unit:
  scout-scout-2026-11-02-015, same window (station panel
  only, train entry and preparation state; Wars dot
  Issue #212).
- No diamonds spent, no purchase tapped, no red line
  crossed. Nothing claimed, fought or dispatched.
