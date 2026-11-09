---
title: Queue Run 2119 Troop Training Partial
created: 2026-11-09T05:19:00Z
modified: 2026-11-09T05:19:00Z
level: L0
version: 1.0.0
description: Training unit training-2026-11-08-1803, Lv.27 verified busy, Lv.20 Drill Ground Full re-confirmed live, partial
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-11-08 about 21:01-21:19 America/Los_Angeles
---

# 2119 queue run - troop training (training-2026-11-08-1803)

- Unit: training-2026-11-08-1803, executor ticker-2058.
  Status: partial - 2 of 4 barracks verified live (Lv.27 busy,
  Lv.20 blocked by Drill Ground Full), 0 batches queued, the
  other two barracks not reached inside the unit cap. Tracker
  untouched.
- Session: computer session cc-167 on the owner Mac mini
  (1c817413-83e2-0545-cb90-36d5e096a6bd); cc-167 dropped
  mid-unit (observe returned observation_unavailable with no
  session open) and session cc-168 was started, LastWar
  re-selected, and no game state was lost. No device-access
  error, no different-device dialog, no login demanded.
  Nothing bought, no speedup used, no Finish Now tapped.
- Session window: 21:01-21:19 local, about 18 minutes
  (over the 15 minute unit cap by about 3 minutes; the
  closing pistol tap and its toast read ran past the cap
  and the unit was closed immediately after).

## What was read and done

- Base HUD at entry: food 499.1M, iron 821.2M, coin 15.8M,
  total power 149,209,253, diamonds 4,467 (gold 13.22K per
  the 1350 unit), unchanged at close. Stamina 120 at the
  lightning icon.
- Barracks Lv.27, verified busy live: tent tap at norm
  (610, 580) selected Barracks Lv.27 with its three-button
  action row; the pistol tap at freshly grounded norm
  (602, 632) opened TRAIN UNITS. Panel read live: Power
  1352, Morale 625.0, Squad Load Capacity 2000, Unit HP
  4121.49, Unit Attack 33.5, Unit Defense 6.74, Lv.9
  selected (1,152), Lv.10 locked (36.5K), a Lv.9 batch of
  726 already training with 06:26:20 left. No Train was
  tapped and no Speed Up was tapped; the panel was closed
  with its X. Note: Morale 625.0, Attack 33.5 and Defense
  6.74 differ slightly from the profile's 600.01 / 33.13 /
  6.67 - the live values govern and the profile's T9 line
  needs a correction (tier-2, left for the knowledge
  flow, not edited here).
- Barracks Lv.20, two findings: (a) the paw Details route
  WORKS for Lv.20 - tent tap at norm (362, 588) selected
  Barracks Lv.20, the paw tap at freshly grounded norm
  (285, 606) opened Building Details, read live:
  Training Count +613, Survivors Instructors Alexis, Joe,
  Jolene and Anthony, Quick Dispatch button at the panel
  bottom NOT tapped (unverified effect, left for an owner
  decision per the activity metadata). The Details panel
  shows no batch timer, so busy/idle is not readable
  from it. (b) The pistol tap at freshly grounded norm
  (396, 634) in the same framing produced the live toast
  "Drill Ground Full: Unable to add more units" - the
  first live re-confirmation of the standing Drill Ground
  Full blocker since the 2026-10-31 read, and proof the
  Lv.20 pistol route reaches the train attempt in this
  framing (it neither cleared the selection as in 1146
  nor opened the upgrade panel as in 0322). No batch was
  queued: the game refused on the full Drill Ground, not
  on an idle barracks. The toast is transient and had
  cleared by the next screenshot; the game was left on
  the base screen with the selection cleared.
- Lv.20 long-press variant, DANGEROUS, do not repeat: a
  1-second long-press on the selected Lv.20 tent body at
  norm (848, 453) entered building-move mode (red X and
  green check buttons at the screen centre, view panned)
  instead of opening TRAIN UNITS. It was cancelled at
  once with the red X at norm (413, 610); no building
  was moved and the HUD was unchanged after. The
  long-press route for Lv.20 is retired on this evidence.
- Wrong-building tap: a visual-grounding point for a
  tent at norm (535, 455) in the panned framing selected
  Hospital Lv.20 instead; it was left untouched (no
  button tapped) and deselected with a tap on empty
  ground. Grounding points for tents must be verified
  against the selection label before any action-row tap.
- Lv.30 and Lv.24 were not reached in this unit. Lv.30
  was verified busy by the 1350 unit (Lv.10 batch 793
  with 20:47:28 left at 13:37) and is still expected
  busy; that is expectation, not a live read here.
- The Drill Ground panel itself was not opened and no
  39,460 of 39,460 figure was read live; the toast is
  the live re-confirmation, not a count.

## Tracker and follow-up

- Tracker untouched (partial). The next training unit
  resumes from: Lv.27 busy until about 03:27 (06:26 left
  at 21:04), Lv.20 blocked by Drill Ground Full (the
  block, not the barracks, is the work - clearing the
  Drill Ground needs an owner decision or a learn-first
  exploration unit; Quick Dispatch stays untapped),
  Lv.30 and Lv.24 still to check.
- Result stats: target 4 barracks, achieved 0 batches
  queued (2 barracks states verified live), verified yes
  for the Lv.27 busy read and the Lv.20 toast read,
  blocker category e (repeated blocker, Drill Ground
  Full re-confirmed live).
- Issue #150 commented by this run with the live toast
  re-confirmation, the working paw Details route, the
  retired long-press route and the Hospital mis-tap.
