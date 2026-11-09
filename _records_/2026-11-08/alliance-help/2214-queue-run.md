---
title: Alliance help queue run 2214
created: 2026-11-09T06:14:00Z
modified: 2026-11-09T06:14:00Z
level: L0
version: 1.0.0
description: Ticker-2201 help unit, Help All pressed twice, points 100 to 360
status: unverified
---

# 2214 queue run - Alliance help

Executor: ticker-2201. Unit: help-2026-11-08-1830.
Session window about 22:04 to 22:14 America/Los_Angeles.

## Performed

- Base screen at entry: no help bubble visible, but the Alliance
  button carried a red dot, so the Help page was opened via
  Alliance, Help (red dot on the Help entry).
- HELP popup read live at entry: "Today's points gained from
  Alliance Help: 100/1,000". The four visible rows were only
  this account's own requests (Bears Lair - Missile Mastery II
  research, Lv.27 Drill Ground, Defense Training VIII
  research, Lv.30 Aircraft Center), each already at 30/30.
- Help All pressed: the game answered "Allies are very
  grateful for your assistance!". The header still read
  100/1,000 in the same open session.
- Help page closed and reopened: header now read live
  340/1,000, a gain of 240 points from the first Help All.
- Scrolling the list down revealed a fifth row below the fold:
  Abyss Apex, "Need help with building Lv.28 Oil Well",
  shown white with no "Time reduced" label - still pending
  after the first press. This corrects the 1413 record's claim
  that the list does not scroll: the list does scroll and an
  ally request can sit below the fold.
- Help All pressed a second time: the toast fired again. The
  header still read 340/1,000 in-session, and the Abyss Apex
  row was gone from the list on the next scroll check.
- Help page closed and reopened a second time: header now
  read live 360/1,000, a further gain of 20 points.
- Closing state verified live: points 360/1,000, only the
  four own 30/30 rows remain in the list, no pending ally
  request visible. No diamonds, money, speedups or other
  spending. No alliance diplomacy, no assembly, no teleport.

## Note - counter lag

- The points header does not update inside one open Help
  session: after each Help All press it still showed the
  pre-press value until the page was closed and reopened.
  This explains the 1413 record's 0/1,000 anomaly - that
  unit read the counter only in-session. Closing figures for
  help units must be read after a page reopen.

## Closing reads

- Help All pressed twice, toast confirmed both times, points
  100/1,000 to 360/1,000 (plus 260), own requests 30/30,
  no pending ally request left.

## Outcome

Done. All waiting ally help requests were pressed.

## Correction (same pass, before commit)

- The session window above is wrong: the unit ran 22:03 to
  22:09 America/Los_Angeles (unit duration_seconds 334, about
  6 minutes), not 22:04 to 22:14. The costs line should read
  6m_wall_no_stamina. The closing figures (points 100 to 360)
  are unaffected.

## Result stats

- target 1, achieved 1, resources_gained 260 Alliance Help points,
  costs 6m_wall_no_stamina, verified yes, blocker_category none,
  points_before 100, points_after 360, points_gained 260,
  helps_pressed unverified_count, help_red_dot_cleared true,
  device_takeovers 0
