---
title: Training 2026-11-09 ticker-2040 partial, barracks tent tap no-change
created: 2026-11-10T05:03:00Z
modified: 2026-11-10T05:03:00Z
version: 1.0.0
description: Troop training unit training-2026-11-09-1803, tent tap method failed in this session, Drill Ground not read
status: unverified
---

# Training 2026-11-09 21:03 PT, ticker-2040, partial

- Unit: training-2026-11-09-1803, claimed 20:56:46 PT, closed 21:03 PT.
- Session: computer session cc-343 dropped mid-pass (observation
  unavailable); cc-344 started, LastWar re-selected. The window
  came up covered - activate reported brought_to_front false.
- One barracks tent was grounded fresh on the live screenshot
  (top-row blue tent, 283, 230) and tapped three times: the first
  tap showed a "+45" float and a small portrait marker at the tent
  (200, 215), but no row of round buttons and no TRAIN UNITS panel
  appeared; the second tap at (283, 245) and a third at (283, 230)
  after a title-bar click to bring the window forward both
  reported no change. The control's own guidance on the second tap
  says background clicks do not reach some controls and suggests
  click_element or the keyboard instead.
- Drill Ground not read live in this unit: no barracks panel opened,
  so the standing Drill Ground Full blocker (39,460 of 39,460) could
  neither be confirmed nor cleared, and no batch was requeued.
- No diamonds or money spent. No Train, Finish Now or upgrade
  shortcut tapped. Nothing bought, nothing deleted.
- Next unit of this type must change the entry route before tapping
  a tent again (R2): try click_element on the tent control, a
  foreground click with the window truly frontmost, or a different
  barracks tent - the same background-click point must not be
  repeated. The tap-method failure here is distinct from the
  Drill Ground Full blocker recorded by the retro.
- Result stats: target requeue idle barracks, achieved 0 of 4
  barracks checked, resources gained none, verified yes (no-change
  reads are live reads), blocker_category c (tap method).
