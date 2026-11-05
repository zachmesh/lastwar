---
title: Training queue run 1146
created: 2026-11-02T19:46:00Z
modified: 2026-11-02T19:46:00Z
version: 1.0.0
description: Ticker training unit, Lv.24 batch queued, Lv.20 panel not reached
status: partial
grounded_in:
  - source: game screen on the owner Mac mini 2026-11-02 11:36 to 11:46 PST
---

# Training queue run 1146

Unit: training-2026-11-02-1003, executor ticker-1134, status
partial. Session window 11:36 to 11:46 PST on the owner Mac mini.
One batch was queued, nothing else was claimed, and the tracker
is left untouched, so the next tick re-produces the regular and
the work resumes as a fresh unit.

## What was done

- Base screen read live at unit start: food 390.2M, iron 580.0M,
  coin 52.8M, diamonds 2,336, total power 149,311,528. No
  different-device dialog appeared in this unit.
- Barracks Lv.24 selected by tapping a tent at norm (806,581).
  Its action row was re-grounded fresh from a cropped band:
  paw about norm (670,584), pistol about norm (794,605),
  green up arrow about norm (930,584). These differ materially
  from the coordinates inherited from the 0811 unit (pistol
  763,510): the row sits about 90 pixels lower in this view.
  Tapping the freshly grounded pistol opened TRAIN UNITS.
- TRAIN UNITS panel for Lv.24, read live: tier Lv.8 selected,
  Power 1063, Morale 520.63, Squad Load Capacity 1800,
  Unit HP 3527.4, Unit Attack 28.37, Unit Defense 5.72,
  count at cap 666, cost 2.9M food and 2.9M iron,
  time 1d 04:20:26. The panel shows no Drill Ground figure
  and no queue-progress line.
- Train taps at norm (561,715), (561,720) and the lower edge
  (561,740), plus a 1 second long-press at (561,715), all
  produced no change and no toast. The system click guidance
  after the second tap suggested background clicks do not
  reach some controls. Those points were NOT the button:
  visual grounding of the panel screenshot put the blue
  Train button at norm (628,793), about 70 pixels below
  the estimated centre. Tapping (628,793) closed the panel
  and moved resources live: food 390.2M to 387.2M, iron
  580.0M to 577.0M, matching the panel cost of 2.9M each
  at HUD rounding. Batch queued: Lv.24, T8 x666.
  Lesson for the next unit: never estimate the Train button
  centre from the displayed panel proportions - ground it
  with the visual grounding tool (or an equivalent fresh
  measurement) before tapping, because the earlier estimate
  missed low by about 70 pixels.
- No Drill Ground Full toast appeared on the successful
  Train tap, and no Drill Ground figure was read live in
  this unit. The 2026-10-31 Drill Ground Full blocker is
  therefore neither confirmed nor re-read here; the
  successful Lv.24 queue is evidence against a universal
  block, but it is not a Drill Ground read.
- Barracks Lv.20 selected by tapping a tent at norm
  (857,531). Its action row was re-grounded from a cropped
  band: paw about norm (704,552), pistol about norm
  (829,575), green up arrow about norm (942,549). Two
  pistol taps - the visual-grounding point (818,584) and
  the crop-measured centre (829,575) - both only cleared
  the selection and returned to the base screen; neither
  opened TRAIN UNITS. Per queue rule R2 the pistol route
  for this barracks ends here inside this unit. A clock
  badge above the Lv.20 tents was visible in the selected
  screenshot but was not read, so no claim is made that
  Lv.20 is already training.
- Barracks Lv.27 and Lv.30 were not inspected in this unit.

## Why partial, not done

- Only 1 of 4 barracks was queued (Lv.24). Lv.20 was
  selected but its TRAIN UNITS panel was not reached, and
  Lv.27 and Lv.30 were not inspected. The unit cap was
  reached with that work outstanding.
- Tracker untouched, per the rule for partial units.

## Follow-up

- Comment on issue #150 with the Lv.24 success coordinates
  (tent 806,581; pistol 794,605; Train 628,793), the
  Train-button mis-estimate lesson, and the Lv.20 pistol
  failure at both (818,584) and (829,575), so the next
  unit does not repeat the Lv.20 pistol route and instead
  tries a different entry route for Lv.20 (for example a
  long-press variant on the selected tent, or the paw
  Details route with freshly grounded coordinates).
- Next unit: re-ground every button fresh, never reuse the
  (561,715) Train estimate, and read the Drill Ground
  screen live first if a panel route to it is found.

## Closing figures

- Batches queued: 1 (Lv.24, T8 x666, 2.9M food, 2.9M iron,
  1d 04:20:26), verified by the live resource drop.
- Barracks checked: 2 of 4 (Lv.24 queued, Lv.20 selected
  only). Drill Ground count: not read.
- Device takeovers in this unit: 0.

## Red lines

- No diamonds or money spent, no paid button tapped, no
  Renew, Finish Now, Legendary Claim All or Battle Pass paid
  unlock touched. Finish Now was visible in the panel and
  was not tapped. No upgrade shortcut tapped, no building
  started, no base move, no Assemble, no teleport.
