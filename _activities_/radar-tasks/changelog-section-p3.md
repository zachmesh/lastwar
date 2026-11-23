---
title: Changelog part 3
created: 2026-11-23T06:25:33Z
modified: 2026-11-23T06:25:33Z
version: 0.1.0
sequence: 64
description: 1.95.0, 2026-11-21 - 0201 radar unit folded (ticker-0159, FAILED, duel day 6 stack; the LastWar window
---
- 1.95.0, 2026-11-21 - 0201 radar unit folded (ticker-0159, FAILED, duel day 6 stack; the LastWar window sits in native fullscreen 1920x1080 on its own Space and the control channel refuses every pointer-input route - coordinate click refused "Pointer input requires the window on the Space the user is looking at", menu View -> Exit Full Screen refused, activate raise brings the window forward about 9.7 s then it switches back, activate+click batching rejected by the tool schema; screenshots still read live, so capture works while input is refused - a NEW failure mode, distinct from the 1340/1347 Zoom-to-Fit framing where canvas taps landed and from the Issue #282 capture-failure form; no radar entry, no Quick Execute, no claims, no stamina spent, stack-day standard met on no line; blocker_category f; retry only if the window state changes to windowed 642x951 on the main Space, owner unblock is switching to the game window or exiting fullscreen on the Mac; a GitHub Issue for this failure mode is owed at gh-route recovery. Renumbered from 1.92.0 to 1.95.0 per the 2026-11-21 KO reconciliation (ko-radar-reconciliation.md): follows the #711 line 1.91.0/1.92.0 (PR #719), the 2104 fold 1.93.0 and the 0101 fold 1.94.0. The WINDOW-STATE PRECONDITION open question is qualified: the withdrawn stop-rule covers only the framing where taps land, not this refused-input state).

