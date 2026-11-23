---
title: How it is done part 1
created: 2026-11-23T06:19:33Z
modified: 2026-11-23T06:19:33Z
version: 0.1.0
sequence: 3
description: Tap each output bubble over the base buildings - and tap the center of the bubble
---
## How it is done

- Tap each output bubble over the base buildings - and tap the
  center of the bubble itself. The owner corrected this on the
  evening of 2026-10-25 after side taps missed; a tap on the edge
  can fall through to the building underneath and open its panel
  instead of collecting. Ground the bubble center visually before
  tapping, and verify the resource total moved afterwards. (2026-11-21 0048 update: re-confirmed - two fall-through taps selected Farmland Lv.28 and Component Factory Lv.20, each re-centring the camera and invalidating the earlier grounding; the re-grounded re-tap at (344,410) still collected nothing verified, so re-grounding alone does not prove a bubble is collectible - verify the HUD after every tap.)
- After a game update, launching the game can show a TIPS dialog 'Update complete, please restart the game.' with a Confirm button - tapping Confirm restarts the game cleanly into the base view, no login demanded and no different-device dialog (measured 2026-11-21, ticker-0048, first launch after about 94 hours offline). Do not confuse it with the 'Server disconnected. Please restart the game.' dialog, whose Confirm quits the app, or with the maintenance TIPS dialog, which blocks login - both are distinguished in the 0034 unit section.
- Panel Collect route (2026-11-10 1210, Issue #585): each resource top-bar icon opens a resource panel with an Available Resources row and a Collect button; tapping Collect takes the whole accumulated building-output pool at once, not just the visible map bubbles - iron panel Owned 939,366,406, Available 2,459,903, Collect took +2,466,821 (panel figure plus production accrued between read and tap), Owned 941,833,227, Available 0; food panel Available 88,117 taken after the farmland bubbles were already tapped (+6.3M). Method: open each resource panel, read Available Resources, tap Collect, verify Owned moved and Available is 0. The map bubbles carry small face values (iron bubbles showed 596 each) while the panel pool held millions, so bubble taps alone under-collect. Bubble-tap hazards from the same unit: a tap on a bubble centre can fall through to the building underneath (first iron tap opened the Aircraft Center Building Queue panel) and can be intercepted by the roaming red-panda pet standing over the mine. The panel route avoids both. (2026-11-10 1531 update: the coin panel is now verified too - Owned 92,648,531, Available 5,236,149, Collect took +5,236,147 exact, Available 0; food panel Available 2,052,949 taken to 0 (Owned 631,359,373) and iron panel Available 1,922,772 taken to 0 (Owned 954,108,872), all in the same unit. All three panels are now verified with exact Collect reads; the coin-panel follow-up from the 1210 unit is closed.