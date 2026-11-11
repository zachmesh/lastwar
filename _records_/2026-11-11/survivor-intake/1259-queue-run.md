---
title: Survivor intake queue run 1259
created: 2026-11-11T21:24:00Z
modified: 2026-11-11T21:24:00Z
version: 1.0.0
description: Ticker-1259 survivors unit - no recruit verified; executor zoom click left the game window in Zoom-to-Fit and the control channel could not tap the canvas or restore the windowed state, gate line never reached, partial
status: unverified
grounded_in:
  - source: live game screen on the owner Mac mini, 2026-11-11 12:59-13:24 PT
---

# Survivor intake queue run 1259 (ticker-1259)

Unit: survivors-2026-11-11-1003. Status: partial.
Activity: survivor-intake.

## What happened - the window, not the gate

- The game was found on the world map, windowed 642x951, LastWar
  window 636402, session cc-606. Chrome was frontmost; the
  activate call selected the game window for background input
  without bringing it to the front.
- Two coordinate taps on the home button in the windowed state
  (590,895 and 588,890) showed no change. The control channel
  then advised that background clicks do not reach some controls.
- The executor clicked the green zoom button (element 4) to
  bring the window forward. That put the window into Zoom to Fit
  at 1920x1080 with the game letterboxed in a 732-wide column
  (capture downsampled to 1280x720). This was the wrong turn:
  from here on no canvas tap produced any change.
- Taps attempted in the zoomed state, all grounded fresh from
  the current screenshot and measured in pixels where stated:
  home button snapped at (645,949), home button unsnapped at
  (645,949), home button long-press 0.6s at (645,940), base
  building at (504,521), home button snapped on the second
  window surface 641257 at (645,949). The home button square
  was measured at capture x 801-852, y 626-706, centre
  (826,666), which maps to normalised (645,925) - the taps were
  on the button, not beside it. Nothing changed on any of them.
- The coordinate mapping was settled by measurement, not
  assumed: the capture is the 1920x1080 screen downsampled by
  2/3, the game column is screen x 565-1297, and the 1233
  radar unit's BASE button (919,962) belongs to the windowed
  642x951 layout, not to this zoomed layout. The mapping is not
  the failure; the canvas simply does not take background input
  in this state.
- Restoration attempts, all failed:
  - View menu Zoom to Fit toggle sent, effect unverified, no
    visible change (background app ignored it; the menu read
    shows Zoom to Fit checked, Enter Full Screen available,
    app_active false).
  - resize_window to 642x951 refused: window did not reach the
    requested frame, still 1920x1080.
  - Cmd-Tab blocked by the channel as a macOS system command.
  - activate on both window surfaces (636402 and 641257)
    selected for background input only, Chrome stayed frontmost.
  - The channel never moves the system cursor, so the Dock
    cannot be hovered or clicked to re-activate the app, and
    the title bar cannot be revealed by hovering the top edge.
- The gate line was never reached: no survivor figure, no
  bubble, no recruit card and no dialog line was ever read.
  Quick Dispatch did NOT run - no recruit was verified.

## Blocker - window state, new failure mode

- This is NOT the standing gate-line blocker of the 2026-10-31
  retro (gate not found / not verified). It is a control-channel
  precondition failure: the game window must be windowed
  642x951 AND frontmost for canvas taps to land, and this pass
  broke the first half with the zoom click and could not repair
  it remotely. The next pass will hit the same wall until the
  window is back windowed and frontmost - that needs a real
  mouse action on the Mac (click the LastWar Dock icon, or
  un-zoom the window), which this channel cannot do.
- The zoom button must not be used as an activation step again:
  it changes the window state instead of bringing the app
  forward. Filed as tooling issue #648; the entry
  route for every unit type needs the window-state
  precondition stated before any tap.
- Issue filed: tooling #648, window zoom breaks the control channel
  (zoom click left the window in Zoom to Fit, canvas taps stop
  landing, no remote restore path); the next pass will hit the
  same wall until the window is back windowed and frontmost.

## Outcome

Partial, unverified. No recruit verified, no Quick Dispatch.
The tracker is left untouched, so the next tick re-produces
the survivors regular and the work resumes as a fresh unit.
No diamonds or money spent. No priced button tapped. No other
activity's rewards touched. Token released at 13:24 PT.
Session cc-606 ended.

## Result stats

- target 1, achieved 0, resources_gained none, costs about 25
  minutes, no game progress, verified no, blocker_category f,
  survivors_recruited 0, survivors_verified 0, bubbles_seen 0,
  bubbles_remaining unknown, quick_dispatch_run no,
  entry_attempts 0, device_takeovers 0
