---
title: Troop Training
created: 2026-10-25T20:12:00Z
modified: 2026-11-02T11:34:36Z
level: L1
version: 1.8.0
description: Training new troops in the barracks, tier by tier, one activity folder for training knowledge
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-25
  - source: owner task request naming a train task, 2026-10-25
  - source: web guides on barracks and troop tiers, read 2026-10-25
  - source: troop training execution record 2026-11-01 1216 queue run
  - source: troop training execution record 2026-11-01 1651 queue run
  - source: troop-training execution record 2026-11-01 2120 queue run (ticker-2104 unit, partial, barracks tents not located after north and south pans)
  - source: troop-training execution record 2026-11-02 0322 queue run (ticker-0308 unit, partial, pistol tap opened upgrade panel)
---

# Troop training

## What this activity is

Training new troops in the four base Barracks. Each barracks trains one
batch at a time, up to its Training Count, at the highest tier its own
level unlocks. This folder accumulates training knowledge - entry,
costs, timers and tier rules. Executions are recorded in
`_records_/<date>/troop-training/`, one file per execution.

Naming note - the owner named this the train task on 2026-10-25. In
game there is also a separate alliance train at the station, registered
on its own as [`alliance-train`](../alliance-train/INDEX.md). Training
troops and riding the train are different systems and are kept apart.

## How to enter

- On the base screen, tap a Barracks tent. The four tents stand in the
  lower middle of the base in this layout. The tent row's screen
  position is camera-dependent: measure it fresh in the unit's
  own view, never from a pinned coordinate - a reused point has
  selected a wrong building (0917 unit, below).
- A row of round buttons appears under the selected tent. The pistol
  icon button opens the TRAIN UNITS panel. The paw icon opens Building
  Details, and the green up arrow is the upgrade shortcut - do not tap
  it. DISPUTED 2026-11-02 (0322 unit): a pistol tap at norm
  (405, 568) on a re-selected Lv.27 tent opened the Lv.27 to 28
  UPGRADE panel, not TRAIN UNITS - whether the mapping is stale
  or the tap landed on a neighbouring control is unresolved. Until
  a unit re-grounds the action row and reproduces a TRAIN UNITS
  opening, treat the pistol mapping as unconfirmed and re-ground
  the row before tapping.
- In TRAIN UNITS, the tier cards run left to right with the highest
  unlocked tier preselected, the count slider sits at the Training
  Count cap, and the blue Train button starts the batch. The yellow
  Finish Now button is never used, under the recording rules on
  spending.

## How it is done

- Keep every barracks busy. One batch per barracks at its highest
  unlocked tier, count left at the cap, then press Train.
- Queueing a batch costs food and iron only, paid up front. No diamond
  use, no instant finish.
- Training finishing also feeds VS Unit Progression and Arms Race
  points, per the web guides - unverified on this account.

## Cadence

- Continuous. A batch runs from about 23 hours to about 1 day 17 hours
  at this account, so in practice requeue each barracks as its batch
  finishes - check once per daily round and requeue any idle barracks.

## Scope and availability

- Always available, not season specific.
- Four barracks, one batch each. Barracks level gates the tier -
  observed Lv.24 trains up to T8, Lv.27 up to T9, Lv.30 up to T10.
  Guide tables agree (T8 at Lv.24 to 26, T9 at Lv.27 to 29, T10 at
  Lv.30 with Special Forces research), unverified beyond the observed
  three.
- Promotion of lower tier troops exists from Barracks Lv.10 per the
  guides. The promote arrow in the panel did nothing on the observed
  barracks, so its exact conditions are unconfirmed.

## What is known from 2026-10-25

Observed in game on this account, first execution 2026-10-25.

- Lv.30 barracks - T10, count 793, cost 5.5M food and 5.5M iron, time
  1 day 17 hours 14 minutes. T10 panel stats - power 1647, morale
  720.01, load 2200, HP 4726.34, attack 38.03, defense 7.55.
- Lv.27 barracks - T9, count 726, cost 4.1M food and 4.1M iron, time
  1 day 10 hours 19 minutes. T9 stats - power 1352, morale 600.01,
  load 2000, HP 4121.49, attack 33.13, defense 6.6.
- Lv.24 barracks - T8, count 666, cost 2.9M food and 2.9M iron, time
  1 day 4 hours 20 minutes. T8 stats - power 1063 in game (one web
  table says 800 - the in-game figure governs), morale 510.01, load
  1800, HP 3527.4, attack 28.37, defense 5.65.
- Fourth barracks - highest tier T7, count 613, cost 2.0M food and
  2.0M iron, time 23 hours 11 minutes. T7 stats - power 779, morale
  444.01, load 1600, HP 2942.73, attack 23.75, defense 4.7. Its own
  level was not read this round.
- Instructor survivors are assigned per barracks in Building Details.
  Quick Dispatch was not used.
- Guide strategies noted but not adopted - staggered barracks levels
  (the waterfall) and training T1 then promoting up to save resources.
  This account already runs staggered barracks levels by accident of
  its upgrade history.

## Limits

- Never tap Finish Now or the green upgrade shortcut while training.
- Training spends food and iron from stock. The 2026-10-25 round spent
  14.5M of each across four batches, small against roughly 290M stocks.

## Standing blocker recorded by the retro of 2026-10-31

- Queue era 2026-10-28 to 2026-10-31 - 21 of 22 training units
  closed non-done, 19 partial and 2 failed, 1 done. The dominant
  late-window blocker is Drill Ground Full, reading 39,460 of
  39,460, which blocked both collection and requeue in every
  2026-10-31 unit that reached a barracks.
- How a full Drill Ground is cleared is not yet known from a
  live read, and no clearing method is claimed here. The next
  unit reads the Drill Ground screen live first, records what
  controls it actually shows, and spends itself on the nearest
  allowed preparatory action instead of closing as a bare
  blocked read. This is a third-strike blocker under queue
  rule R2.

## What the 2026-11-01 0045 unit added

- Inherited points went stale after camera drift: a tap at norm
  708,602 (the pinned Drill Ground / Lv.30 point from the
  2026-10-31 03:04 and 07:04 units) selected nothing visible in
  this camera view, and a tap at norm 617,570 (the pinned Lv.27
  tent point from the 15:44 unit) likewise selected nothing -
  no label, no button row. The camera had drifted through the
  preceding survivors unit's pans. This is the queue rule R2
  failure mode in miniature: points must be measured fresh in
  the unit's own camera view, never inherited, and this unit
  recorded the miss instead of repeating the taps.
- No ungrounded tap followed: an enlarged crop of the base
  centre in this view showed production houses carrying 59.6K
  resource bubbles, a helicopter pad and a green military
  vehicle, but no barracks tent row that could be grounded
  with confidence, so no TRAIN UNITS panel opened, no Drill
  Ground panel opened, and no toast (including Drill Ground
  Full) was read live in this unit.
- Full-block status carried forward unverified: the standing
  Drill Ground Full block from 2026-10-31 (39,460 of 39,460)
  is carried forward unverified by this unit, not
  re-confirmed and not cleared, because the unit never reached
  a barracks.
- Focus note, shared with the survivors unit in the same pass:
  pans stopped moving the view after a focus loss and resumed
  only after a title-bar left-segment tap at norm 274,18.
- Not attempted: no batch collected or started, no troops
  deployed or dismissed to free drill-ground space (an
  owner-side decision, outside this unit), no Finish Now, no
  green upgrade shortcut, no purchase, no diamond spend, no
  speedup item burned. The game was left on the base screen.

## What the 2026-11-01 0917 unit added

- Pinned-point failure escalated from a miss to a wrong
  building: in this camera position, norm 617,570 (the
  pinned Lv.27 tent point from the 2026-10-31 15:44 unit,
  which merely missed in the 0045 unit) positively
  selected Missile Vehicle Base Lv.10. The other two taps
  in this pan selected Titanium Alloy Factory No.1 Lv.30
  at norm 405,475 and Titanium Alloy Factory No.2 Lv.30
  at norm 330,540 - so the unit was searching a factory
  pan, not the tent row. A reused coordinate therefore
  does not just miss across camera positions; it can
  select a wrong building. Leave any wrongly selected
  building untouched (no upgrade shortcut, no Finish
  Now, no Train pressed) and pan to the tent row first
  rather than repeating taps in the same pan - the
  record's own next-unit instruction.
- Drill Ground Full carried forward unverified a second
  consecutive unit: 0045 and 0917 both never reached a
  barracks, and the Drill Ground panel was not re-read in
  0917, so the 39,460 of 39,460 block remains a
  2026-10-31 read, not a 2026-11-01 re-confirmation, and
  no clearing method is claimed.
- Control-channel recovery: the computer session dropped
  mid-unit; a new session re-selected Last War with no
  game state lost, no different-device dialog, and no
  login demanded.


## What the 2026-11-01 1216 unit added

- Changed method per queue rule R2: instead of repeating
  taps in the factory pan, this unit panned the base view
  in four directions looking for the tent row. The opening
  pan showed the Titanium Alloy Factory cluster in the
  walled compound; one tap at norm 400,535 selected
  Titanium Alloy Factory No.4 Lv.30 and was left untouched
  (no upgrade shortcut, no Train, no Finish Now). Four
  drags then swept the view - up, right, diagonal
  down-left, and up again - showing the HQ and furnace
  sector, the vehicle Formation 2 and 3 parking sector,
  and empty snowfield to the south and east. No barracks
  tent row appeared in any swept pan, so no TRAIN UNITS
  panel was reached, no batch was collected or started,
  and the Drill Ground panel was not re-read in this unit.
- Drill Ground Full carried forward unverified a third
  consecutive unit: 0045, 0917 and now 1216 all never
  reached a barracks, so the 39,460 of 39,460 block
  remains a 2026-10-31 read, not a 2026-11-01
  re-confirmation, and no clearing method is claimed.
- Next-unit instruction, from the record itself: try a
  zoomed-out whole-base view first (the current pans
  cover the compound and the surrounding snowfield but
  never show a tent row), and ground the Drill Ground
  building itself before any further tent taps, since the
  drill-ground gate is the standing blocker and its panel
  has not been read live since 2026-10-31. This is the
  same zoom-out-first variant the 1159 survivors unit
  names for its own gate search - the two searches share
  the method, not the target.
- Not a live read: the chat line visible during the unit,
  "thorsey: need to lose some troops", is consistent with
  a full drill ground but is not a live read of the Drill
  Ground panel and is not used as one. The red target icon
  with a countdown seen at the right edge of the closing
  pan was left untouched: it belongs to another task type,
  not this unit.
- HUD at open: food 289.2M, iron 477.2M, coin 10.6M,
  total power 148,957,193, unchanged at close. No
  diamonds, money, speedups or paid buttons used; the
  tracker is untouched, so the next tick re-produces
  this regular.

## What the 2026-11-01 1651 unit added

- Status partial: unit training-2026-11-01-1403 by
  ticker-1638, session about 16:45 to 16:51. No barracks
  panel opened, no batch queued, no Drill Ground screen
  read, nothing claimed. Tracker untouched; the next
  tick re-produces the regular.
- Centre view, no tent verified: the base screen in the
  642 by 951 window showed the resource-house row, the
  signed front gate and the vehicle formation lots; no
  barracks tent was verified in this view. The profile's
  "four tents stand in the lower middle of the base"
  line is therefore not confirmed in this camera
  framing - it stands as the 2026-10-25 layout
  description, not as a verified point in this unit,
  and no tent point is claimed from it.
- Grounding points NOT tapped: fresh visual grounding
  for a barracks tent returned points that sat on the
  gate road area, not on a verified tent. Those points
  were not tapped: tapping the gate would have repeated
  the survivors unit, a different task type. Ungrounded
  or wrong-target points are not tapped - the same
  discipline as the 0045 and 0917 pinned-point failures.
- South ruled out to the map edge: changed method
  versus earlier units - two upward pans to walk the
  view south. The first pan reached the vehicle depot
  and the Season 2 structures at the map edge; the
  second pan reached the map south edge itself (Season
  2 house cluster, a tank, a STOP sign, formation lots
  2 and 3 at the top of the view). No barracks tent
  appeared in either panned view. Barracks tents are NOT
  south of the vehicle formation lots down to the map
  south edge.
- Next-unit instruction, from the record itself (rule
  R2): start from a zoomed-out full-base view and
  locate the four tents first, or find a building-list
  entry, rather than panning south again or tapping
  grounding points that sit on the gate road. This is
  the zoom-out-first variant the 1216 unit already
  named - still untried, now with the south route
  closed.
- Drill Ground Full carried forward unverified a fourth
  consecutive unit: 0045, 0917, 1216 and now 1651 all
  never reached a barracks, so the 39,460 of 39,460
  block remains a 2026-10-31 read, not a 2026-11-01
  re-confirmation, and no clearing method is claimed.
  This unit differs from the 2026-10-31 Drill Ground
  Full partials: no barracks was reached at all, so the
  blocker was neither confirmed nor cleared here, and
  no Drill Ground figure is claimed.

## What the 2026-11-01 2120 unit added

- Partial, barracks tents still not located: unit
  training-2026-11-01-1803 by ticker-2104, session about
  21:07 to 21:20. No barracks panel was opened, no batch
  was queued, no Drill Ground screen was read, and
  nothing was claimed. Tracker untouched, so the next
  tick re-produces the regular.
- Device takeover handled under the owner rule: the
  "active on a different device" dialog appeared
  mid-unit, Confirm was tapped once, the app exited as
  expected, and it was relaunched and back at the base
  screen with no login or verification demanded. No
  second dialog appeared. HUD after the relaunch read
  food 359.5M, iron 550.3M, coin 34.2M, diamonds 2,416,
  same power 149,288,895 as the unit-start read (food
  353.1M, iron 543.9M, coin 30.1M, diamonds 2,396) -
  production ticks only, no claim made.
- Grounding discipline, measured: a visual-grounding call
  for a barracks tent timed out at 3 minutes with no
  result and was abandoned, not retried - do not repeat
  a grounding call inside a 15-minute unit after a
  timeout. Scroll gestures did nothing to the game view;
  drag pans are the working move, and their mapping is
  now measured: a drag from norm y 300 to y 700 moves
  the view south, the reverse moves it north, and a
  full-length drag crosses most of the base.
- Pan results, both edges ruled out at this zoom level:
  the south pan reached the map south edge again - the
  Season 2 house cluster, a tank, a STOP sign, formation
  lots 2 and 3 at the top - repeating the 1651 south
  route and adding nothing new; the houses there are
  not verified barracks. The north pan reached the map
  north edge - the same house cluster at the top and
  empty snow below, no barracks tent in either edge
  view. A half-length drag back south landed near the
  start view (house cluster top left, cannon and tank,
  empty snow below); the dense red-roofed formation of
  the unit's very first screenshot was not in this view
  either, so it lies further east or north-east of the
  start view, unreached in this unit.
- Next-unit rule, from the record under rule R2: change
  the route again before repeating this work - pan east
  from the start view toward the dense red-roofed
  formation seen in the first screenshot, and only tap
  a tent that is visually verified as a tent, never a
  point that sits on the gate road or the house cluster.
  Do not repeat the south or north pans, and do not
  spend a grounding call inside the unit budget after a
  timeout.
- Drill Ground Full status, fifth consecutive carry
  without a live read: the 2026-10-31 Drill Ground Full
  blocker was neither confirmed nor cleared in this
  unit - no barracks was reached, so no Drill Ground
  figure is claimed here. The profile therefore still
  carries it unverified, now a fifth consecutive unit
  without a live Drill Ground read (1651 was the fourth).
  No diamonds or money spent, no Finish Now, no upgrade
  shortcut. Evidence in
  `_records_/2026-11-01/troop-training/2120-queue-run.md`.


## What the 2026-11-02 0017 unit added

- Unit training-2026-11-01-2203 by ticker-0004, session
  about 00:16 to 00:17, status partial. No barracks panel
  was opened, no batch was queued, no Drill Ground screen
  was read, and nothing was claimed. The tracker is left
  untouched, so the next tick re-produces the regular
  and the work resumes as a fresh unit.
- Changed route taken, per queue rule R2 and the 2120
  next-unit rule: one east pan (drag norm 320,450 to
  120,450) from the opening base view. The resulting view
  shows formation lots 2 and 3, parked tanks and a blue
  structure at the top, and production buildings at the
  left edge - no row of four barracks tents, and no tent
  was visually verified, so no tent was tapped on a
  guess. The east-pan formation-lot view is ruled out as
  the barracks tent row at this camera position.
- Next-unit rule, from the record under rule R2: change
  the route again - pan from the opening view toward the
  lower-middle base area where the pinned coordinates
  were measured (Lv.30 tent at norm 708,602, Lv.27 tent
  at 617,570), and only tap a tent visually verified as
  a tent. Do not repeat the east pan to the formation
  lots, nor the south or north pans.
- Drill Ground Full status, sixth consecutive carry
  without a live read: the 2026-10-31 Drill Ground Full
  blocker was neither confirmed nor cleared in this
  unit - no barracks was reached, so no Drill Ground
  figure is claimed here. The profile therefore still
  carries it unverified, now a sixth consecutive unit
  without a live Drill Ground read (2120 was the fifth).
  This recurrence is the failure open Issue #150 tracks
  (barracks tent rows not located, Drill Ground never
  re-read); the recurrence is commented onto #150, not
  filed as a new issue.
- Base screen read live at unit start: food 362.4M, iron
  555.0M, coin 36.7M, diamonds 2,476, total power
  149,198,310. No different-device dialog, no login or
  verification demanded. No diamonds or money spent, no
  paid button tapped, no Finish Now, no upgrade
  shortcut. Evidence in
  `_records_/2026-11-02/troop-training/0017-queue-run.md`.

## What the 2026-11-02 0322 unit added

- Unit training-2026-11-02-0203 by ticker-0308, session about
  03:22 to 03:30, status partial. No batch was queued and no
  training state was verified. The tracker is left untouched,
  so the next tick re-produces the regular and the work
  resumes as a fresh unit. Evidence in
  `_records_/2026-11-02/troop-training/0322-queue-run.md`.
- Barracks tents grounded on the live base screenshot: norm
  (308, 552), (409, 606), (546, 544), (608, 518). This locates
  the tent rows that Issue #150 records as not located.
- First tent tapped and selection confirmed: Barracks Lv.27
  with the three-button action row - paw (details), pistol
  (train per this profile), green up arrow (upgrade). The
  pistol button tapped at norm (405, 568) opened the Lv.27
  to 28 UPGRADE panel, not TRAIN UNITS: Unit Training Cap
  540 to 550, Unit Training Level 9 to 9, cost coins 43.7M
  of 127.5M and iron 565.3M of 314.5M, Upgrade timer 19d
  14:30:46, Finish Now 187,490. It was closed with the panel
  X. No Upgrade, no Finish Now, no Obtain, no building
  started. Whether the pistol mapping is stale or the tap
  landed on a neighbouring control is unresolved - the
  profile's pistol-to-TRAIN-UNITS claim is therefore
  qualified as disputed above, not silently kept and not
  silently erased.
- Paw button tapped at norm (311, 552) on the re-selected
  tent: no panel opened. Deselected with a tap on empty
  ground, leaving the game on the base screen.
- TRAIN UNITS was not reached, so no barracks queue state
  was read, no idle barracks was requeued, and the Drill
  Ground state was not read. The other three barracks were
  not inspected. Drill Ground Full is therefore carried
  forward unverified a seventh consecutive unit (0017 was
  the sixth). The record commented on Issue #150 with the
  located tent rows and the unresolved TRAIN UNITS entry,
  so the next unit re-grounds the action row before
  tapping; no new issue is filed here.


## Open questions

- The fourth barracks level, and whether raising it to Lv.27 or Lv.30
  is worth a build slot.
- How promotion actually engages, and its cost against training fresh.
- Whether the Lv.30 barracks button row differs - its pistol position
  opened Details twice before the panel opened from another button.

## Changelog

- 1.2.0 (2026-11-01): inherited-point staleness after camera
  drift (708,602 and 617,570 both missed), the no-ungrounded-tap
  rule applied to a crop with no groundable barracks row, the
  Drill Ground Full block carried forward unverified, and the
  shared 274,18 focus fix, folded from the 0045 training unit.

- 1.3.0 (2026-11-01): pinned-point failure escalated to a
  wrong-building selection (617,570 selected Missile
  Vehicle Base Lv.10; factory-pan landmarks Factory No.1
  and No.2 Lv.30 measured), the pan-to-the-tent-row-first
  next-unit rule, Drill Ground Full carried forward
  unverified a second consecutive unit, and the mid-unit
  session-drop recovery, folded from the 0917 training
  unit.

- 1.4.0 (2026-11-01): four-direction pan sweep with no tent
  row (factory cluster, HQ and furnace sector, Formation
  2 and 3 parking, snowfield south and east), Drill Ground
  Full carried forward unverified a third consecutive
  unit, the zoomed-out whole-base view plus ground-the-
  Drill-Ground-first next-unit instruction, and the chat
  line explicitly not a live Drill Ground read, folded
  from the 1216 training unit.

- 1.5.0 (2026-11-01): south of the vehicle lots ruled
  out to the map south edge, gate-road grounding points
  correctly not tapped, the zoom-out-or-building-list
  next-unit rule, and Drill Ground Full carried forward
  unverified a fourth consecutive unit, folded from the
  1651 training unit.

- 1.6.0 (2026-11-01): north and south map edges ruled out at this zoom level, the measured drag mapping (y 300 to 700 moves south, reverse north), the 3-minute grounding timeout abandoned not retried, the device-takeover Confirm once with clean relaunch, the east-toward-the-red-roofed-formation next-unit rule, and Drill Ground Full still carried unverified a fifth consecutive unit, folded from the 2120 training unit.

- 1.7.0 (2026-11-02): east pan to the formation lots ruled out as the barracks tent row, the lower-middle-base next-unit rule, Drill Ground Full carried unverified a sixth consecutive unit, and the recurrence commented onto Issue #150, folded from the 0017 training unit.

- 1.8.0 (2026-11-02): barracks tent rows grounded at four measured points, the pistol tap opening the Lv.27 to 28 upgrade panel instead of TRAIN UNITS so the pistol mapping is now disputed, Drill Ground Full carried unverified a seventh consecutive unit, and the recurrence commented onto Issue #150, folded from the 0322 training unit.
