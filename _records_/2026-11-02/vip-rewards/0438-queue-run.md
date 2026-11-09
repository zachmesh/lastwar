---
title: Queue Run 0455 VIP Rewards
created: 2026-11-02T12:38:00Z
modified: 2026-11-02T12:38:00Z
level: L0
version: 1.0.0
description: VIP unit partial - login chest claimed 200 points, Daily Freebie Claim button unresponsive
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-11-02
---

# 0455 queue run - VIP rewards (partial)

Unit vip-2026-11-01-1900, executor ticker-0434, session
cc-152 on the Mac mini, LastWar window 137757, about 04:36 to 04:38 America/Los_Angeles. Status partial: the login
chest was claimed, the Daily Freebie was not. No different-
device dialog, no login demand, nothing spent, no diamonds,
no paid button tapped (VIP Exclusive $99.99 untouched).

## Entry

- From the base screen, the commander avatar at norm
  [60,85] opened MY PROFILE (Lv.30 [AP3x]Bears Lair,
  likes 1,797, up from 1,796 on 2026-10-31; no popularity
  popup this time). The VIP13 badge at norm [514,352],
  carrying a red dot, opened the VIP screen.

## VIP state read live

- VIP13, logged in 56 days in a row, 200 VIP points
  tomorrow, points 1,585,960 of 2,000,000 toward VIP 14
  on entry.
- Daily Freebie contents shown: puzzle piece x2, food
  crate x13, iron crate x13, coin crate x13, with a
  green Claim button.

## Login chest - claimed, live points read before and after

- The login chest at the top right, at norm [833,195],
  was tapped once: CONGRATULATIONS popup at once -
  Today's VIP Points 200, Consecutive Login Days 56,
  Next Day's VIP Points 200. Points after: 1,586,160,
  exactly +200, and the chest red dot cleared on the
  closing screenshot. This proves background input does
  reach VIP-screen controls in this session.
- Popup dismissal, method note: two taps on the popup
  X at norm [802,384] and [799,382] (the second a double
  tap) left the popup open; a tap on the dimmed area
  outside the popup at norm [120,700] dismissed it at
  once. Next units dismiss this popup via the dimmed
  area, not the X.

## Daily Freebie - Claim button unresponsive, button-specific

- Two single taps on the freshly grounded Claim button
  centre, at norm [818,631] and [825,628], each verified
  by a following screenshot: the button stayed green,
  points stayed 1,586,160, no popup appeared. Per queue
  rule R2 the Claim method ends inside this unit after
  two no-change taps; no further variants were burned.
- This is the same blocker as the 2026-10-31 VIP unit,
  but the evidence now narrows it: the login chest on
  the same screen, in the same session, via the same
  background input, worked at once. The failure is
  specific to the Daily Freebie Claim button, not a
  general background-input failure. That distinction is
  new in this unit and should be carried into the next
  VIP attempt (and into the activity metadata by the
  knowledge organiser, not by this executor).
- The freebie (puzzle x2, food x13, iron x13, coin
  x13) remains unclaimed for the current reset day and
  is the pre-reset sweep's item; the next tick
  re-produces this regular.

## Outcome

- Status: partial. Claimed in this unit: login points
  200 (points 1,585,960 to 1,586,160). Not claimed:
  Daily Freebie contents above.
- Tracker untouched (partial units do not mark the
  tracker). Game left on the VIP screen.
- Red lines: nothing spent, no diamonds, no paid button.
