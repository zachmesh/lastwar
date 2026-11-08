---
title: Trucks queue run 2347
created: 2026-11-02T23:47:00-08:00
unit: trucks-2026-11-02-2257
executor: ticker-2334
---

# Trucks - 2026-11-02 23:47 local

Unit: trucks-2026-11-02-2257 (regular trucks, activity truck-plunder).
Session: Mac mini Last War window; computer session cc-273
dropped mid-pass and was restarted as cc-274 with no game
state lost. No "active on a different device" dialog appeared.
No diamonds, no Trade Contracts, no paid button, no plunder.

## Duel posture

- Duel day 2, Base Expansion, from tools/duel.py at unit start.
  UR truck dispatches score (Handbook 100,000 each); trucks go
  UR today, contracts permitting. Radar posture stack.

## Entry failure - station route did not reproduce

- The 21:20 unit entered Intercity Trade by tapping the
  station building at norm [491,195]. This unit tried that
  exact tap twice (once before and once after a title-bar
  focus tap as the foreground pivot) - both no-change.
- A visually grounded station box (norm 395-860 x 120-355)
  was tapped at its centre [627,237]: it selected a squad
  parking slot ("2nd Squad Lv.20") and opened a two-button
  popup (vehicle icon, up arrow) with no labels. Neither
  button was tapped - the popup's meaning was not
  established and a wrong tap could march a squad. The
  popup was dismissed by tapping empty ground; the base
  view returned unchanged.
- A further tap at [662,163] (upper station structure) was
  also no-change. That is two no-change entry taps, so the
  background-input method was ended inside this unit under
  queue rule R2; the title-bar focus pivot did not change
  the outcome for the [491,195] tap.
- Counters were NOT read this unit - entry never reached
  the trade screen, so no counter values are asserted here.
  Last read counters (21:20 unit): Trade 4/5, Plunder 4/4,
  with the first return due about 22:10 local. A return and
  settlement may therefore be pending, but that is the
  21:20 read, not a fresh observation.

## Outcome

- Status: partial, entry failed, dispatch shortfall carried
  forward (not a miss: the trade day runs to 19:00 local
  2026-11-03, and later trucks units keep trying entry).
- Claimed in this unit: none.
- No dispatch, no plunder, no settlement performed.
- Next trucks unit: retry entry first. Do not re-tap the
  left-column points or the [491,195] / [662,163] points
  blindly - re-ground the station hotspot on the live base
  framing first, and treat the squad-slot popup (vehicle
  icon, up arrow) as unidentified until a labelled read
  proves what it opens. If entry still fails, the
  foreground variant to try next is moving the covering
  Chrome window aside before tapping, which this unit did
  not attempt.
- blocker_category: f (missing precondition - trade screen
  entry not reached)
- Game left on the base screen.
