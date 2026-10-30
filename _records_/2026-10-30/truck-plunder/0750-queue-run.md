---
title: Trucks queue run 0750 entry failed
created: 2026-10-30T14:50:00Z
modified: 2026-10-30T14:50:00Z
version: 1.0.0
description: Ticker pass ticker-0734 trucks unit, partial - Intercity Trade screen never entered
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-30
---

# Trucks queue run, 0750 entry failed

Session window: about 07:44-07:48 PDT, executor
ticker-0734, Mac mini session cc-461, game account
[AP3x]Bears Lair.

Performed in part: trade screen never entered,
tracker untouched, so the next tick re-produces
this regular.

- Duel posture for today (tools/duel.py): Day 5,
  Total Mobilization, ends 19:00, 11.3 hours left.
  Not a UR day, so the applicable rule would have
  been SR or above only, regular dispatch, no Mega
  Mode; plunder UR or SSR trucks only with guard
  below Squad 1 24.96M, to the daily quotas
  (dispatch 5, plunder 4 per the 2026-10-30 rule).
  None of that was reached in this unit.
- Base screen at entry was normal, no "active on a
  different device" dialog, no login demand. HUD:
  coin 142.5M, Total Power 146,850,228.
- Entry attempts, verified by screenshot:
  - The left icon column was read from an enlarged
    crop before tapping: top to bottom - hammer
    2/4, flask 0/2, green face 0C, blue truck-front
    icon with a red badge 1, white pickup truck,
    satellite dish, hammer, walkie-talkie below
    the crop. Per the 2026-10-28 set identification
    the blue truck-front icon with a red badge is
    Intercity Trade, grounded at norm 52,620 on
    this base view.
  - Three taps on that icon (single, single again,
    double) produced no screen change; the second
    tap's guidance noted background clicks do not
    reach some controls and suggested click_element,
    but the game's accessibility tree carries only
    OCR text elements, so no element number exists
    for this icon and click_foreground could not be
    used. No other icon was tapped for trade entry:
    the white pickup is the Secret Command Post and
    the road truck with the "truck is full" bubble
    is the base-gate Armed Truck, neither is trade.
- This matches the 2026-10-30 03:40 and 05:40
  units, where trade entry failed the same way.
  The trade slot may be present but untappable by
  background clicks in this window state, or the
  set may have flipped again; either way no flip
  control was identified in this unit.

Result:

- Settled: 0. Dispatched: 0. Plundered: 0.
- Trade Count, Plunder Count, returned trucks and
  Reward Recovery were not checked because the
  trade screen was never entered.
- No Trade Contracts spent, no diamonds spent, no
  paid buttons tapped.
- Entry lesson carried forward: the next unit
  should try bringing the game window to the front
  before tapping the blue truck-front icon, or find
  an element-based route into Intercity Trade, and
  only then tap; if entry still fails, record the
  same entry failure rather than spending the unit
  hunting.
