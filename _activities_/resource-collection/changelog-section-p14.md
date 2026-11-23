---
title: Changelog part 14
created: 2026-11-23T06:19:33Z
modified: 2026-11-23T06:19:33Z
version: 0.1.0
sequence: 51
description: 1.26.0 (2026-11-05) - Correction from the 0134 survivors and 0204 gifts records - the game window
---
- 1.26.0 (2026-11-05): Correction from the 0134 survivors and 0204 gifts records - the game window is windowed 1920x1080 on an inactive Space, not in native fullscreen (View menu lists Enter Full Screen, read on-screen in session cc-505 and re-confirmed by a repeated probe in cc-508); the capture failure is the pixel stream of an off-screen window, not a broken screen-recording permission; the "running fullscreen" wording in the 1634, 2104 and 0034 sections is superseded, and the 0034 "menu path View -> Exit Full Screen" with it; the permission/pipeline-restart follow-up is replaced by the window-back-on-active-Space unblock (owner Dock-icon click); background Space keys do not switch Spaces, set_window_frame is stale-observation-gated, Cmd+Tab is blocked, list_windows needs the exact app name "LastWar"; the 1101 harvest close stands as the last live read; twenty-sixth and twenty-seventh occurrences commented onto Issue #282 by this run. (1.23.0, 1.24.0 and 1.25.0 carry the 1634, 2104 and 0034 sections without changelog lines; the numbering is preserved, not rewritten.)

- 1.22.0 (2026-11-04): farmland +2.1M food (417.9M to 420.0M) and left-side +1.4M coin (18.0M to 19.4M) verified by HUD deltas, farmland one-tap-clears-all and the 0755 left-side point (88,406) re-confirmed, Alliance back arrow (161,935) and panel X closures (848,213) and (848,150) re-confirmed, donations timer 00:11:45 corroborating the 1046 timer running, right side and top edge unswept and EXP, screw and drone-component bubbles unlocated so the full edge-drag sweep stays incomplete, marker confusion caution (Issue #250) carried with no new failure mode, folded from the 1101 harvest unit; no earlier claim superseded. (1.20.0 and 1.21.0 carry the 0413 and 0755 sections without changelog lines; the numbering is preserved, not rewritten.)

- 1.19.0 (2026-11-04): server maintenance blocking login (0034 unit failed, 0 bubbles, no base view reached), disconnected dialog distinguished from maintenance dialog (disconnected Confirm quits the app, maintenance Confirm safe to retry and login impossible only while maintenance is active), sweep now two units behind after the partial 2034 unit, folded from the 0034 harvest record with the 0110 survivors record as the clearing corroboration; no earlier claim superseded.

- 1.18.0 (2026-11-03): one verified teal-bubble collection
  (+1.6M second-row resource, name unclaimed), factory-top
  grounding confusion at (435,442) and (501,532) selecting
  Titanium Alloy Factory No.1 and No.3 Lv.30 (Issue #250),
  season-entry white bubble at (485,575) toast-only, entry
  Techs-panel closures and the donations-counter attribution
  caution, full edge sweep and armed-truck loot still
  outstanding, partial blocker category b, folded from the
  2034 harvest unit; no earlier claim superseded.

