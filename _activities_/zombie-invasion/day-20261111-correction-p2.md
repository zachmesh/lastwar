---
title: Correction 2026-11-11 - Zoom to Fit canvas input lands, the stop-rule is withdrawn part 2
created: 2026-11-23T06:53:20Z
modified: 2026-11-23T06:53:20Z
version: 0.1.0
sequence: 78
description: The mechanism is now measured (ticker-1408 pass, tooling Issue 652) - in this 1920x1080 fullscreen window
---
- The mechanism is now measured (ticker-1408 pass, tooling Issue #652): in this 1920x1080 fullscreen window background canvas taps land about (-23 x, +10 y) normalized from the specified point, so narrow controls miss while wide controls land - the leading explanation for the 1259-vs-1340 difference; the exact per-control hit/miss arithmetic is not settled. The 1259 unit's evidence stands as its own unit's record; only its blanket generalisation is withdrawn. The same correction is applied to radar-tasks and survivor-intake in this run; the cross-profile carry in knowledge Issue #650 must use the corrected wording.

