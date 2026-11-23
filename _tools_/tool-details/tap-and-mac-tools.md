---
title: Tap and Mac tools
created: 2026-11-23T04:53:59Z
modified: 2026-11-23T04:53:59Z
version: 1.0.0
description: Verbatim index rows for tapcal.py, mac_capture_probe.py, mac_window_open.py
---

# Tap and Mac tools

Moved verbatim from the former `_tools_/INDEX.md` table; only link destinations are adjusted for this folder. Back to the [tool index](../INDEX.md).

| Tool | Purpose | Data |
|---|---|---|
| [tapcal.py](../tapcal.py) | Score tap logs (first-try rate, miss vectors), calibrate a session offset from anchor observations, compensate aim points, keep per-activity visual anchors, and decide one step of the tap-verify loop for a single target (issue #123); tap and anchor records may name the window geometry so a fullscreen-only shift is never averaged away (issue #475); a tap landing exactly on target with no state change is named input-blocked instead of retried (issue #575); per-control first-try tap variant (top-bar icons unsnapped, Collect buttons snapped) with a variant-flip retry when an on-target tap changes nothing and the other variant is untried (issue #646, provisional, one unit of evidence); narrow-control compensation decision: a session offset that meets or exceeds a control's half-extent means compensate first, and a compensation from another session or geometry is refused (issue #652); panel-close ladder decision: a tap sent while another surface is selected is named wrong-surface (it passes through to the base view and spends no method budget), and a close target escalates tap -> double-tap -> long-press -> click-element (only when ocr_number is named) -> relaunch with two no-change taps per method under R2, ending exhausted instead of a fourth identical attempt (issue #854) | executor tap logs and anchor stores |
| [mac_capture_probe.py](../mac_capture_probe.py) | Classify Mac screen-capture failure evidence into a diagnosis (issue #284): OFF_SCREEN_WINDOW, CAPTURE_STREAM_DOWN, CHANNEL_STALL, DEVICE_OFFLINE, or ZOOMED_WINDOW_INPUT_BLOCKED when the window sits in Zoom to Fit (1920x1080, not the windowed 642x951) and is not frontmost so the canvas takes no input (issue #648); ignored taps while frontmost are an offset miss (#652), not blocked input, so a zoomed-frontmost pass proceeds with the offset-compensation note (1.4.0, issue #648 follow-up); exit 0 HEALTHY, 1 UNKNOWN, 10/11/12/13/14 by diagnosis; never click the green zoom button as an activation step | device evidence JSON |
| [mac_window_open.py](../mac_window_open.py) | Decide the session-open step from list_windows evidence (issue #822): OPEN_APP only when no LastWar window exists, ACTIVATE_EXISTING with raise=true for the single window, ACTIVATE_LIVE_DUPLICATE for the focused window when two or more exist (the newer duplicate is a dead input target - close it or ignore it, never send canvas input to it); ignored taps with a duplicate name the duplicate as the likely cause, so the exit is retried on the live window instead of concluding the control is unresponsive (R2); DUPLICATE_UNKNOWN_LIVE stops the pass when no focus signal names the live window; exit 0 decided, 1 UNKNOWN, 2 duplicate with unknown live | device evidence JSON |
