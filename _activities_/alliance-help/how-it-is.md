---
title: How it is done
created: 2026-11-23T07:24:24Z
modified: 2026-11-23T07:24:24Z
version: 0.1.0
sequence: 3
description: Open Alliance, then the Help page.
---
## How it is done

- Open Alliance, then the Help page.
- Press Help All. Individual helps are used only if Help All is not offered.
- Foreground precondition, recorded by the retro of 2026-10-31 -
  the 2026-10-31 1030 unit never opened the Alliance panel
  because Chrome stayed frontmost and background taps did not
  reach the Alliance button. Two no-change taps end the
  background-input method inside the unit under queue rule R2 -
  bring the game window to the foreground and re-observe before
  tapping again. The same-day later units recovered, so this
  blocker is transient, not a dead entry route.
- Fullscreen Alliance-button failure, 2026-11-09 1019: in fullscreen 1920x1080 the Alliance shield button did not respond to six background taps in four variants (coordinate clicks, hold, second window), while the green menu arrow at (484,975) did respond to background input - background clicks reach some controls and not others in fullscreen. Two LastWar windows exist (489932 titled "Last War", 508052 empty title); the duplicate window may be part of the blocker. Changed method for the next unit: exit fullscreen to the native 642x951 window and retry the Alliance tap there, or find a click_element route if an Alliance label element appears in the observation. Do NOT repeat the fullscreen background-click sequence. (CORRECTION 2026-11-11 1410: the "exit fullscreen" changed method is SUPERSEDED for this button - in the same fullscreen 1920x1080 window the Alliance button DID open: taps at (633,715) and (633,712) did nothing, but a tap at the re-grounded centre (652,711) with snap off opened the panel at once. click_element with label "Alliance" fails - the game is a canvas, no such control exists. The mechanism is measured in the same pass (tooling Issue #652): background canvas taps in this fullscreen window land about (-23 x, +10 y) normalized from the specified point, so narrow controls miss while wide controls land - the Alliance button needs its fresh centre plus snap off, not a window change. The Help dialog X is the same class: three taps at (568,211) did not respond, and the dialog was closed with the panel back arrow instead; per R2 the X was not tapped a fourth time. The Alliance panel back arrow likewise ignored three taps at its measured centre (328,951), then closed on a compensated tap at (351,941) (Issue #652, same pass). Receipt lesson from the same unit: the help-bubble tile tap at (602,712) read no-change on its receipt, but the toast "Allies are very grateful for your assistance" and the tile gone on the next observation prove the tap delivered - verify by observation, not by receipt alone.)

