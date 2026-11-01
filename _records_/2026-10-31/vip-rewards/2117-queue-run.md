---
title: VIP rewards queue run 2117
created: 2026-10-31T21:17:00-07:00
modified: 2026-10-31T21:17:00-07:00
version: 1.0.0
description: VIP unit vip-2026-10-31-1900 by ticker-2104, partial - Daily Freebie Claim button unresponsive to background input, nothing claimed
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-31
---

# 2117 queue run - VIP rewards (partial)

VIP unit vip-2026-10-31-1900 by ticker-2104,
sessions cc-711 and cc-712 (cc-711 dropped once,
no state lost), window mode 642x951, no
different-device dialog. Google Chrome stayed
the frontmost app throughout.

Performed in part: profile and VIP screen reached,
nothing claimed, nothing spent.

- Entry: from the Hidden Treasures tab, the back
  arrow at norm 162,935 returned to the base
  screen (HUD iron 343.1M, food 531.0M, coin
  177.4M, power 148,947,193, matching the 2048
  trucks reconciliation). The commander avatar
  at norm 60,85 opened MY PROFILE; the "You're
  very popular!" popup ([AP3x]Krazy Sully,
  1 person, likes 1,795 +1) was dismissed with
  its Awesome button at norm 500,663, likes
  then reading 1,796. The VIP13 badge at norm
  514,352, carrying a red dot, opened the VIP
  screen.
- VIP state read: VIP13, logged in 55 days in a
  row, points 1,577,870 of 2,000,000 toward VIP
  14, tomorrow login points 200. Daily Freebie
  contents shown: puzzle piece x2, food crate
  x13, iron crate x13, coin crate x13, with a
  green Claim button.
- Claim failure: the Claim button did not respond
  to five background-input variants, each verified
  by a second screenshot showing the button still
  green, points unchanged at 1,577,870 and no
  CONGRATULATIONS popup: single taps at norm
  813,623 and 790,620, a double tap at 813,623,
  a 1-second long-press at 813,623, and a single
  tap at 760,625. The system guidance on the
  second tap said background clicks do not reach
  some controls and suggested click_element, but
  the game canvas exposes no enabled control
  labeled Claim, so that route was unavailable.
  The login chest at top right was not tapped
  because the freebie claim had not gone through
  first and the unit was closed rather than
  spending further variants on it.
- VIP Exclusive ($99.99 purchase) and the
  points-plus button were not tapped. No diamonds
  or money spent.

## Outcome

Partial. Daily Freebie and login points both
still unclaimed; the Claim button's background
unresponsiveness is the blocker, matching the
Chrome-foreground blocker pattern seen earlier
on 2026-10-31. Tracker untouched; the next tick
re-produces this regular and should retry the
claim, ideally with the game window in the
foreground. Game left on the VIP screen.
