---
title: Changelog part 13
created: 2026-11-23T06:25:33Z
modified: 2026-11-23T06:25:33Z
version: 0.1.0
sequence: 74
description: 1.78.0, 2026-11-11 - CORRECTION from the ticker-1332 pass (records 1340 training and 1347 arms-race, commit ed2cb2614)
---
- 1.78.0, 2026-11-11 - CORRECTION from the ticker-1332 pass (records 1340 training and 1347 arms-race, commit ed2cb2614): the 1259 "no canvas tap lands in Zoom to Fit" claim is SUPERSEDED - both units ran in the same fullscreen framing (window still in Zoom to Fit, capture 1280x720) and canvas taps DID land (radar-map back arrow (326,948) exits at once, Iron Mine Lv.27 selects at (395,455), Mall opens at (645,62), Mall back arrow (316,952) exits at once); the Home button ((688,958)/(645,950), matching 1259's (645,925)) and the labelled Events icon (707,146) are the controls that do not respond in this framing, not the canvas as a whole; the stop-rule is WITHDRAWN - units proceed in the fullscreen framing on verified working points, re-grounding fresh; the green-zoom-button ban stands; no remote restore path exists and the window is still in Zoom to Fit as of the 1347 close (13:57 PT), but the owner's mouse restore is no longer a blocker for play; the mechanism is now measured (ticker-1408 pass, tooling Issue #652): background canvas taps in this fullscreen window land about (-23 x, +10 y) normalized from the specified point, so narrow controls miss while wide controls land - the leading explanation for the 1259-vs-1340 difference, the exact per-control arithmetic not settled; the 1332 run's Slack message to the owner is corrected by this run; the cross-profile carry in knowledge Issue #650 must use the corrected wording.
