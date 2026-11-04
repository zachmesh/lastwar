---
title: Alliance gifts queue run 1147
created: 2026-11-04T19:47:00Z
executor: ticker-1134
unit: gifts-2026-11-04-1030
status: partial
---

# Alliance gifts - 2026-11-04 11:47 local

Unit: gifts-2026-11-04-1030 (regular gifts,
activity alliance-gifts). Session: Mac mini Last
War window, computer session cc-454. No "active
on a different device" dialog appeared.

## Work done

- Alliance entry attempted twice from the live
  base frame: norm (691,750), then the re-grounded
  Alliance button point norm (640,722). Both taps
  dispatched, but the Alliance panel never opened
  and the following screenshots still show the
  base view, so neither the Regular nor the
  Premium tab was reached and no Claim All was
  tapped.
- This repeats the foreground precondition recorded
  by the retro of 2026-10-31: while Chrome stays
  frontmost on the Mac, background taps do not
  reach the Alliance button. Under queue rule R2
  the two no-change taps end the background-input
  method inside this unit. The game window was
  not forced to the foreground because Chrome is
  the user's active window on the Mac, and
  stealing its focus mid-use would disrupt the
  user; the blocker is transient by the 2026-10-31
  precedent (later units the same day recovered),
  so the next tick retries rather than escalating.
- No gift count was read, no gift was claimed,
  and no red-dot state is claimed for either tab.

## Follow-up for the next gifts unit

- Retry when the game window can be foregrounded
  without disturbing the user's active app, or
  when background input recovers; then Claim All
  on both the Regular and Premium tabs.

## Red lines

Nothing spent, nothing claimed, no other
activity's work done.

## Result stats

- gifts_claimed 0, tabs_claimed 0,
  device_takeovers 0
