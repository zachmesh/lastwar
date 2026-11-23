---
title: How to enter part 1
created: 2026-11-23T07:24:19Z
modified: 2026-11-23T07:24:19Z
version: 0.1.0
sequence: 3
description: Base screen, Mail button on the right rail (envelope icon).
---
## How to enter

- Base screen, Mail button on the right rail (envelope icon).
- Entry, windowed (2026-11-09 1031): the Mail button tap at the freshly grounded centre (932,791) in windowed 642x951 opened Mail at once - windowed background clicks reach the game, unlike the fullscreen Alliance taps in the sibling 1019 help unit. The point still drifts per session, so re-ground fresh each unit (Issue #230).
- Entry, fullscreen (2026-11-11 1422): the Mail button on the right rail needed two taps - the first at (650,795) did nothing, the second at the envelope centre (656,775) with the click-offset compensation opened Mail. The compensation is about +23 x, -10 y in normalized coordinates, measured in this pass (tooling Issue #652: background canvas taps in the 1920x1080 fullscreen window land about -23 x, +10 y from the specified point). The offset applies to the Mail envelope too.
- Coordinates are 0-1000 normalized, not window pixels (2026-11-11 1029 unit): a click at pixel (599,756) landed at normalized (599,756) = pixel (385,719) and missed Mail. Grounding the Mail button at normalized (931,785) and clicking there opened Mail. All later clicks in the unit used normalized coordinates from screenshots/grounding and worked. Never feed pixel coordinates to computer.control.
- The category rail, top to bottom, reads - Battle Report, Alliance,
  Event, Season, System, Regular, In-app Purchases (corrected
  2026-11-01 by the 1730 unit; the earlier list omitted Event and
  named the last category "Purchases"). The train arrival reward mail of
  the daily round was presented as an Event mail in game. (CORRECTION 2026-11-11 1422: the mail hub now lists Event and Favorite and NO Season row is shown any more; Event is the visible reward-bearing tab and carries the gift icon when claimable. The rail as read live in 1422: Battle Report, Alliance, Event (gift icon - claimable), System, Regular (red dot), In-app Purchases (red dot), Favorite.)
- Every category list ends with Delete All and Claim All buttons.
  Claim All claims every claimable attachment in that category at
  once. Purchases holds receipts only - nothing to claim.
- Favorite row: tapping the row body did not navigate; the row arrow at the right edge did (2026-11-11 1029 unit).
- Dismissing a reward popup: one tap on the dimmed area above the banner closed it (2026-11-11 1029 unit).
