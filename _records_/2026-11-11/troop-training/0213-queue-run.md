---
title: Troop training queue run 0213
created: 2026-11-11T10:13:00Z
modified: 2026-11-11T10:13:00Z
version: 1.0.0
description: Ticker-0155 training unit - Lv.30 barracks pistol and paw taps close the button row with no panel and no power change, Drill Ground screen still not located live, partial
status: unverified
grounded_in:
  - source: live game screen on the owner Mac mini, 2026-11-11 01:56-02:13 PT
---

# Troop training queue run 0213 (ticker-0155)

Unit: training-2026-11-10-2203. Status: partial.
Activity: troop-training. Computer session cc-536.

## Entry

- The game was left on the Alliance Techs screen by the
  donations unit of this pass (Tech Donation Today 2600,
  Quick Construction 8/10). Closed the Techs panel (X) to
  the Alliance menu, then the back arrow to the base
  screen.
- Base screen at entry: food 666.0M, iron 988.7M, coin
  117.4M, gold 13.22K, diamonds 6,287, Total Power
  149,218,973, stamina 26, VS timer 16:02:28.

## Lv.30 barracks - two pistol taps, one paw tap, no panel

- The four tents were re-grounded fresh from the current
  screenshot (visual grounding points): (399,815),
  (523,853), (664,781), (740,726). A first tap at
  (505,857) selected "Barracks Lv.30" with the button
  row (blue paw, orange pistol, green up arrow).
- Pistol tap 1 at (318,885): the button row closed, no
  TRAIN UNITS panel opened, no toast captured in the
  screenshot after the tap, Total Power unchanged at
  149,218,973. No finished batch collected.
- A re-tap at (607,857) missed between tents (no
  selection); re-grounded and re-tapped the tent at
  (523,853), which selected Lv.30 again.
- Pistol tap 2 at (318,885): identical outcome - the
  button row closed, no panel, no toast captured, Total
  Power still 149,218,973. Per queue rule R2 the pistol
  method ends for this barracks after two no-change taps.
- Pivot to the paw button (Building Details): re-selected
  the tent, tapped the paw at (263,850). The button row
  closed again with no Details panel opening. No live
  read of the barracks training timer was obtained from
  any of the three taps.

## Drill Ground screen - still not read live

- The standing instruction from the 2146 unit was that
  this unit's first action is to read the Drill Ground
  screen live. That read was not achieved: the Drill
  Ground building was not located on the base screen in
  this unit, and the barracks button row - the only
  entry tried - never opened a panel from which the
  Drill Ground could be reached. The two pistol taps
  behaving exactly as the 2146 unit's Drill Ground Full
  toast case (row closes, no panel) is consistent with
  the blocker still being live, but the toast itself was
  not captured live in this unit, so that is an
  inference, not a live read, and is not claimed as one.
- The next training unit must locate the Drill Ground
  building first - by name on the base screen or via a
  troop overview entry - before tapping any barracks
  button again. This is the fourth consecutive unit
  closing on the same blocker (third-strike rule R2
  already triggered in 2146); the blocker now needs a
  changed entry route, not another pistol tap.

## Other barracks - unchecked

- Lv.24: not checked in this unit; known running from
  the 1229 unit, due for requeue about 16:49 on
  2026-11-11. Lv.27: not checked; its batch was
  collected at 21:46 on 2026-11-10 and its requeue was
  blocked by Drill Ground Full then. Fourth barracks:
  not checked.
- Side observation during this unit: a "Boarding closes
  in" banner appeared at the top of the base screen
  (00:02:51 at first sight, 00:02:38 at the paw tap) -
  the alliance train is boarding now. That is the train
  regular's work, not this unit's; it is noted here so
  the next unit in this pass can pick the train unit up.

## Close

- Partial. One barracks checked (Lv.30); no batch
  collected, no batch requeued, no TRAIN UNITS or
  Details panel opened, Drill Ground screen not read
  live. The tracker stays untouched, so the next tick
  re-produces the training regular and the work resumes
  as a fresh unit.
- No diamonds or money spent. No Finish Now button and
  no upgrade shortcut tapped. No login or verification
  demanded. No "active on a different device" dialog
  appeared. The game was left on the base screen.

## Result stats

- target check all 4 barracks, requeue any idle one at
  its highest tier
- achieved 1 of 4 barracks checked (Lv.30); no batch
  collected; no batch requeued; Drill Ground screen
  not read live
- resources_gained none
- points 0
- costs about 17 minutes, no items spent, no
  food or iron spent (no batch queued)
- verified yes (power 149,218,973 read live before and
  after; no change)
- blocker_category e
- barracks_checked 1, batches_collected 0,
  batches_requeued 0, drill_ground_full inferred-not-read,
  drill_ground_screen_read no,
  power_before 149218973, power_after 149218973,
  train_boarding_seen yes (closes 00:02:51 at first sight),
  device_takeovers 0
