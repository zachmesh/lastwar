---
title: How to enter
created: 2026-11-23T07:18:19Z
modified: 2026-11-24T11:59:07Z
version: 0.3.0
sequence: 3
description: Base screen cart icon opens the shop on the HOT DEALS tab row.
---
## How to enter

- Base screen cart icon opens the shop on the HOT DEALS tab row.
- The Weekly Pass tab lists the Free Supply chest, the Legendary
  bundle row, and every weekly pass card, owned and for sale mixed.
- The Super Monthly Pass tab holds the monthly pass and its daily gift.
- COORDINATE CALIBRATION (measured 2026-11-10 1836): computer.control
  coordinates are normalized 0-1000 on BOTH axes. Convert screenshot
  pixels as x/642*1000 and y/951*1000 in the 642x951 window. The shop
  back arrow's measured centre is (168,917) - taps at (168,872)
  failed three times with no change. The HELP dialog X closes at
  (841,200). Press-drag (500,750) to (500,300) is the confirmed
  list-scroll method for the Weekly Pass page; scroll_amount 5 does
  not move the list.
- Entry, 2026-11-10 2256: from the Alliance Techs tree, the panel X closed to the Alliance menu, the menu back arrow returned to the map, and the cart icon at (903,63) opened the shop on HOT DEALS, first try each. The cart point (903,63) is confirmed again as the shop entry.

2026-11-23: the cart now opens on Official Event and the tab row has no Hot Sale Packs tab; see [shop state](shop-state.md).

2026-11-24: the press-drag from (500,750) above starts on a card and is not the method: three drags that started on cards did not move the Weekly Pass page. One drag from the blank right margin, (685,650) to (685,400), moved it a long way and over-scrolled it (`_records_/2026-11-22/shop-claims/1150-queue-run.md`); Page Down did nothing. So: a drag that starts on a card is read as a card gesture and moves nothing; start on the blank right margin (x about 685), short (60 to 80 px), one drag, a frame after; an over-scroll is corrected by one short drag back (20 to 40 px).
