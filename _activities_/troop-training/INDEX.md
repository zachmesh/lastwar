---
title: Troop Training
created: 2026-10-25T20:12:00Z
modified: 2026-11-08T01:32:17Z
level: L1
version: 1.25.0
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
  - source: troop-training execution record 2026-11-02 0811 queue run (ticker-0804 unit, partial, action-row taps switched to the world map)
  - source: troop-training execution record 2026-11-02 1146 queue run (ticker-1134 unit, partial, Lv.24 batch queued, Lv.20 pistol route retired)
  - source: troop-training execution record 2026-11-02 1723 queue run (ticker-1703 unit, partial, Lv.24 panel not opened from inherited points)
  - source: troop-training execution record 2026-11-02 1949 queue run (ticker-1934 unit, partial, drag blocked by open radial)
  - source: troop training execution record 2026-11-02 2255 queue run
  - source: ticker-0234 troop-training execution record 2026-11-03 0252 queue run (partial, road drag pans, centre drag does not, no tent)
  - source: ticker-0634 troop-training execution record 2026-11-03 0647 queue run (partial, no tent in four framings, road drags pan)
  - source: ticker-1034 troop-training execution record 2026-11-03 1051 queue run (partial, three framings no tent, road drag pans where centre drag does not, Issue 150)
  - source: ticker-1534 troop-training execution record 2026-11-03 1552 queue run (partial, Lv.27 T9 batch queued and HUD-verified, tent blocker breakthrough, Issue 150)
  - source: ticker-2134 troop-training execution record 2026-11-03 2144 queue run (partial, production grid is factories not tents, 1552 point selects Factory No.3 in this framing, Issue 150)
  - source: ticker-0134 troop-training execution record 2026-11-04 0143 queue run (partial, factories confirmed again, 1552 tent point not re-tried, Tank Base Lv.28 to 29 upgrade in progress, Issue 150)
  - source: ticker-0434 troop-training execution record 2026-11-04 0440 queue run (partial, tent point 585,548 selects Barracks Lv.24, Drill Ground Full confirmed live again, Training Count +666, Issue 150)
  - source: ticker-0804 troop-training execution record 2026-11-04 0814 queue run (partial, 0440 tent point selects Arena in this framing, Lv.20 verified via Details, framing instability measured, Drill Ground Full neither reconfirmed nor cleared, Issue #150 comment deferred)
  - source: ticker-1134 troop-training execution record 2026-11-04 1147 queue run (partial, fullscreen framing mismatch, four grounded tent taps opened no panel, centre drag moved no view, session drop reopened, Issue 150)
  - source: ticker-1734 troop-training execution record 2026-11-04 1734 queue run (failed, Mac screen-capture failure on every attempt, no game screen read, no input dispatched, eleventh consecutive ticker pass to fail this way, Issue 284)
  - source: ticker-0534 troop-training execution record 2026-11-05 0534 queue run (failed, Mac screen-capture failure on every attempt, no game screen read, no input dispatched, thirty-fourth consecutive pass, probe classification OFF_SCREEN_WINDOW, Chrome observes normally in the same session, Issue 284)
  - source: ticker-1655 troop-training execution record 2026-11-07 1655 queue run (partial, Lv.27 T9 x726 and Lv.30 T10 x793 requeued at cap, 9.6M food plus 9.6M iron, two upper-right barracks unchecked, Drill Ground Full not seen; record commit 514e333e5b on records/2026-11-07)
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
- A row of round buttons appears under the selected tent: paw,
  pistol and green up arrow. The green up arrow is the upgrade
  shortcut - do not tap it. The paw-to-Details and pistol-to-TRAIN-UNITS mapping is camera-position dependent, not dead: the 0811 suspension is LIFTED IN PART 2026-11-02 (1146 unit), which re-grounded the Lv.24 row fresh (paw about 670,584; pistol 794,605; green up arrow 930,584) and opened TRAIN UNITS with the pistol tap. The 0811 world-map result and the 0322 upgrade-panel result do not carry across camera views. The standing rule is fresh grounding of the whole row in every unit's own view, never inherited coordinates. The 1552 unit extends the lifted-in-part pistol route to Lv.27 in its view: tent grounded at norm (630,592), pistol re-grounded at norm (612,608) before tapping, TRAIN UNITS opened with Lv.9 preselected. QUALIFIED 2026-11-03 (2144 unit): that same tent point (630,592), re-tried after a rightward drag re-framing, selected Titanium Alloy Factory No.3 Lv.30 in the 2144 framing, not a barracks tent - so the point is framing-bound, not a portable tent coordinate. Re-grounding in the unit's own view is mandatory, and a factory selection must never be re-tapped as if it were a tent. The Lv.20 pistol route is separately RETIRED 2026-11-02 (1146 unit): two fresh pistol points (818,584 and 829,575) both only cleared the selection, so the next Lv.20 attempt tries a different entry route (a long-press variant on the selected tent, or the paw Details route with freshly grounded coordinates).
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
  load 2000, HP 4121.49, attack 33.13, defense 6.67.
- Lv.24 barracks - T8, count 666, cost 2.9M food and 2.9M iron, time
  1 day 4 hours 20 minutes. T8 stats - power 1063 in game (one web
  table says 800 - the in-game figure governs), morale 520.63 (2026-11-02 live read, superseding the 2026-10-25 figure 510.01), load 1800, HP 3527.4, attack 28.37, defense 5.72 (superseding 5.65).
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


## What the 2026-11-02 0811 unit added

- Unit training-2026-11-02-0603 by ticker-0804, session 08:05
  to 08:11, status partial. No batch was queued and no
  training state was verified. The tracker is left untouched,
  so the next tick re-produces the regular and the work
  resumes as a fresh unit. Evidence in
  `_records_/2026-11-02/troop-training/0811-queue-run.md`.
- Barracks located in this unit's camera view by visual
  inspection of a cropped lower band: three tents in the
  lower-middle base area. Tapping the upper-right tent at
  norm (825, 578) selected Barracks Lv.24, with the
  three-button action row under its label: blue paw circle
  at about norm (623, 499), orange pistol circle at about
  norm (763, 510), green up-arrow circle at about norm
  (903, 494). The green arrow was not tapped, per the red
  lines.
- Entry failure, both routes: the pistol tap switched to the
  world map (radar fan, Radar Task restore countdown), not
  TRAIN UNITS and not an upgrade panel; Home at norm
  (903, 941) returned to base. The paw tap on the
  re-selected tent gave the same world-map switch, not
  Building Details. Re-tapping the tent body only re-showed
  the same action row; no panel opened. The action-row
  mapping is therefore suspended in How to enter above -
  it is unstable across camera positions, not merely stale
  in one direction, since the 0322 pistol tap opened the
  upgrade panel instead.
- TRAIN UNITS was not reached, so no barracks queue state
  was read, no idle barracks was requeued, and the Drill
  Ground state was not read. The other three barracks were
  not inspected. Drill Ground Full is therefore carried
  forward unverified an eighth consecutive unit (0322 was
  the seventh). The record commented on Issue #150 with
  the measured tent coordinate, action-row coordinates and
  the world-map result for both taps, so the next unit does
  not repeat the action-row route; no new issue is filed
  here.
- One different-device takeover, handled under the owner
  rule: the dialog appeared at unit start, Confirm was
  tapped once, the app exited as expected, and it was
  relaunched and back at the base screen with no login or
  verification demanded. No second dialog appeared.


## What the 2026-11-02 1146 unit added

- Unit training-2026-11-02-1003 by ticker-1134, session 11:36
  to 11:46, status partial: 1 of 4 barracks queued (Lv.24),
  Lv.20 selected only, Lv.27 and Lv.30 not inspected. The
  tracker is left untouched, so the next tick re-produces
  the regular. Evidence in
  `_records_/2026-11-02/troop-training/1146-queue-run.md`.
- Entry mapping re-established for Lv.24, suspension
  lifted in part: the Lv.24 tent was selected at norm
  (806,581) and its action row re-grounded fresh (paw
  about 670,584; pistol 794,605; green up arrow 930,584)
  - the row sits about 90 pixels lower than the 0811
  row, so the 0811 world-map result does not carry to
  this camera view. The pistol tap opened TRAIN UNITS.
  The 0811 suspension's own condition is therefore met
  for Lv.24: a fresh, verified mapping reproduced a
  panel opening. The standing rule is now fresh
  grounding in every unit's own view, never inherited
  coordinates - the mapping is camera-position
  dependent, not dead.
- Lv.20 pistol route retired inside the unit per queue
  rule R2: the Lv.20 tent was selected at norm (857,531)
  and its row re-grounded (paw about 704,552; pistol
  829,575; green 942,549), but two pistol taps - the
  visual-grounding point (818,584) and the crop-measured
  centre (829,575) - both only cleared the selection and
  returned to the base screen; neither opened TRAIN
  UNITS. The next Lv.20 attempt tries a different entry
  route (a long-press variant on the selected tent, or
  the paw Details route with freshly grounded
  coordinates) and does not repeat the pistol taps. A
  clock badge above the Lv.20 tents was visible but not
  read, so no claim is made that Lv.20 is already
  training.
- Train button lesson, measured: taps at the estimated
  centre (561,715), (561,720) and (561,740), plus a
  1-second long-press at (561,715), all produced no
  change; visual grounding put the blue Train button at
  norm (628,793), about 70 pixels below the estimate.
  Never estimate the Train button centre from panel
  proportions - ground it fresh before tapping. The
  (628,793) tap queued the batch.
- Batch queued, verified by the live resource drop: Lv.24,
  T8 x666, 2.9M food and 2.9M iron, 1d 04:20:26, matching
  the profile cost and time; food 390.2M to 387.2M and
  iron 580.0M to 577.0M at HUD rounding. The panel shows
  no Drill Ground figure and no queue-progress line.
- Drill Ground Full, ninth consecutive unit without a
  live read, but now with counter-evidence: no Drill
  Ground Full toast appeared on the successful Train
  tap, no Drill Ground figure was read live, and the
  successful Lv.24 queue is evidence against a
  universal block - but it is not a Drill Ground read,
  so the 39,460 of 39,460 figure remains a 2026-10-31
  read, neither confirmed nor cleared here. The next
  unit still reads the Drill Ground screen live first
  if a panel route to it is found.
- The recurrence was commented onto Issue #150 by the
  executor (Lv.24 success coordinates, the Train-button
  mis-estimate lesson, the Lv.20 pistol failure), so no
  duplicate comment is filed here.


## What the 2026-11-02 1723 unit added

- Unit training-2026-11-02-1403 by ticker-1703, session
  about 17:19 to 17:23, inside the pass budget, status
  partial. No batch was queued. The tracker is left
  untouched, so the next tick re-produces the regular.
  Evidence in
  `_records_/2026-11-02/troop-training/1723-queue-run.md`.
- Inherited 1146 points did not reproduce in this camera
  view: the Lv.24 tent point from the 1146 unit, norm
  806,581, was tapped and no selection label or action
  row was visible on the next screenshot; the Lv.24
  pistol point from the 1146 unit, norm 794,605, was
  tapped and the control reported only a small visual
  change in the tent area, with no TRAIN UNITS panel
  opened and the base screen otherwise unchanged. This
  is the standing fresh-grounding rule cutting both
  ways: the 1146 pistol entry was verified only in the
  1146 camera view, and its coordinates are not a
  reusable shortcut in any later view. The next unit
  re-grounds the tent and the whole action row fresh
  before tapping either point, and does not re-tap the
  1146 points on a guess.
- No training state was verified: Lv.24 was queued at
  11:34 today for T8 x666 with a 1 day 4 hour timer, so
  it is expected to still be busy, but its panel was
  not read live in this unit and that is not claimed
  as a verified state. Lv.27 and Lv.30 were not
  inspected. No Drill Ground figure was read live in
  this unit.
- Drill Ground Full carried forward unverified a tenth
  consecutive unit without a live read (1146 was the
  ninth): no barracks was reached, so the 39,460 of
  39,460 figure remains a 2026-10-31 read, neither
  confirmed nor cleared here, and the 1146 successful
  queue remains the counter-evidence against a
  universal block, not a Drill Ground read.
- HUD measured 2026-11-02 in this unit: food 387.7M,
  iron 577.5M, coins 54.0M - matching the 1520 harvest
  unit's HUD snapshot the same day, a consistent
  stock picture, not a unit result. Base screen
  confirmed live at entry; game left safe on the base
  screen. No diamonds or money spent, no Finish Now,
  no upgrade shortcut. The recurrence is a further
  data point for open Issue #150, commented there by
  the executor, so no duplicate comment is filed here.

## What the 2026-11-02 1949 unit added

- Unit training-2026-11-02-1803 by ticker-1934, session
  about 19:48 to 19:49, inside the pass budget, status
  partial. No batch was queued. The tracker is left
  untouched, so the next tick re-produces the regular.
  Evidence in
  `_records_/2026-11-02/troop-training/1949-queue-run.md`.
- Entry state: the squad-vehicle selection radial left
  open by the previous survivors unit was still showing
  on the base view at entry - a cross-unit handover
  confirmed on screen.
- New failure mode: an upward drag (norm 500,600 to
  500,300) to expose the lower-middle barracks tents
  did not pan the view at all; the screenshot after
  the drag was unchanged, so no barracks tent was
  brought into view and no tent point was tapped in
  this unit. The drag may have been intercepted by
  the open selection radial. Next-unit rule: close or
  deselect any open selection radial before attempting
  a pan drag; a drag that leaves the screenshot
  unchanged is a blocked drag, not a "no tents here"
  result.
- No training state was verified: 0 barracks checked,
  no TRAIN UNITS panel opened, no Drill Ground figure
  read live in this unit. Lv.24 queued at 11:34 today
  for T8 x666 per the 1723 record is carried as
  expectation only, not a live read here.
- Drill Ground Full carried forward unverified an
  eleventh consecutive unit without a live read (1146
  was the ninth, 1723 the tenth): no barracks was
  reached, so the 39,460 of 39,460 figure remains a
  2026-10-31 read, neither confirmed nor cleared here,
  and the 1146 successful queue remains the
  counter-evidence against a universal block, not a
  Drill Ground read.
- HUD measured in this unit: food 227.1M, iron 561.8M,
  coins 5.9M - matching the 1945 harvest snapshot in
  the same pass, a consistent stock picture, not a
  unit result. Base screen confirmed live at entry;
  game left safe on the base screen with the squad
  radial still open; no action was taken from it.
- The recurrence is a further data point for open
  Issue #150, commented there by the executor, so no
  duplicate comment is filed here.


## What the 2026-11-02 2255 unit added

- Unit training-2026-11-02-2203 by ticker-2234,
  session about 22:52 to 22:55, status partial: 0
  barracks verified, 0 batches queued, tracker
  untouched, so the next tick re-produces this
  regular. Evidence in
  `_records_/2026-11-02/troop-training/2255-queue-run.md`.
- Base screen confirmed live at entry; HUD food
  230.0M, second top-bar 564.7M, coins 5.9M,
  second-row first resource 18.7M, matching the
  2247 harvest close. An "Alliance Gifts received!"
  toast was visible at entry; it belongs to the
  gifts regular and was not acted on from this
  training unit.
- Dragged the base view upward (500,700 to 500,400)
  to expose the lower-middle barracks tents, per the
  1949 unit's attempt. Unlike 1949, the drag did move
  the view this time: the central cluster shifted to
  the top of the screen and the lower area showed
  empty snow, with no barracks tent brought into
  view. No tent point was therefore tapped, and no
  TRAIN UNITS panel was opened. Dragged back
  (500,400 to 500,700) to restore the starting view.
  Game left safe on the base screen.
- No Drill Ground figure was read live in this unit,
  and no Drill Ground Full state is claimed. The
  2026-10-31 Drill Ground blocker in the activity
  metadata is therefore neither confirmed nor
  cleared here, and is carried unverified a twelfth
  consecutive unit. The Lv.24 batch queued at 11:34
  today (T8 x666, 1 day 4 hours, per the 1146 and
  1723 records) is not a live read in this unit and
  is not claimed as a verified busy state.
- Why partial, not done: no barracks queue was
  verified and no idle barracks was requeued, so the
  "keep every barracks busy" standard is unmet. The
  matching open issue is #150; this unit's
  drag-moved-but-no-tent result is a further data
  point for that issue, not a new issue.


## What the 2026-11-03 0252 unit added - road drags pan, centre drags sometimes do not, still no tent

- Unit training-2026-11-03-0203 by ticker-0234, about
  02:52 local, status partial. Evidence in
  `_records_/2026-11-03/troop-training/0252-queue-run.md`.
- Entered from the survivors unit's top-edge panned view
  (gate and formation slots 1/2/3 in frame). A centre
  vertical drag (500,650 to 500,300), intended to return
  to the central view, moved nothing: the next screenshot
  kept the identical top-edge framing. A second vertical
  drag on the left road surface (200,600 to 200,300) did
  move the view, restoring the central cluster framing
  (furnace centre, houses, same as the harvest unit's
  start view). Drag-pan responsiveness therefore varies
  by start surface: road drags pan, centre drags over
  buildings or fields sometimes do not. This is a
  further data point for Issue #150, not a new issue,
  and it is commented onto #150 by this run.
- The restored central view shows no barracks tent: the
  lower-middle area holds the furnace and the house
  cluster, with snow below. No tent point was therefore
  tapped, and no TRAIN UNITS panel was opened.
- No Drill Ground figure was read live in this unit,
  and no Drill Ground Full state is claimed. The
  2026-10-31 Drill Ground blocker in the activity
  metadata is therefore neither confirmed nor cleared
  here, now a thirteenth consecutive unit without a live
  Drill Ground read.
- The pass budget (about 25 minutes from the 02:35
  token) ended during this unit, so the search for the
  tents stops here rather than consuming another unit's
  budget.
- Result stats: target 4, achieved 0, verified no,
  blocker category c. Partial: 0 barracks verified, 0
  batches queued, tracker untouched, so the next tick
  re-produces this regular.

## What the 2026-11-03 0647 unit added - four framings, no tent, road drags pan again

- Ticker-0634, unit training-2026-11-03-0603, about
  06:47 local, status partial. Evidence in
  `_records_/2026-11-03/troop-training/0647-queue-run.md`.
- Tent search, four framings, no tent tapped: from the
  survivors unit's upper view, a left-road drag
  (200,600 to 200,300) restored the central view; a road
  drag down (200,300 to 200,650) returned to the upper
  view; two more road drags up (200,600 to 200,300,
  twice) returned to the central view; a horizontal drag
  (300,500 to 700,500) reached the right-side view (own
  blue-roofed buildings on the left, neighbouring bases
  on the right). No barracks tent was identified in any
  framing: the central lower-middle holds the furnace
  and the house cluster, the upper view holds the
  Capitol pyramid and pink buildings, and the right-side
  view holds tower and house buildings - none presented
  as a barracks tent, and no TRAIN UNITS panel was
  opened.
- Drag-surface distinction re-confirmed, consistent
  with the 0252 unit: road drags pan while centre
  drags over buildings sometimes do not. This is a
  further data point for Issue #150, commented onto
  #150 by this run.
- The 2026-10-25 "lower middle" tent description does
  not match the current framings: the central
  lower-middle now reads as furnace and house cluster,
  not tents. The description is marked stale for the
  current layout as of 2026-11-03, not deleted from
  history; the next unit re-grounds the four tent
  positions on the current base layout before any tap.
- No batch was queued, no barracks queue state was
  verified, and no Drill Ground figure was read live in
  this unit, so the 2026-10-31 Drill Ground Full blocker
  is neither confirmed nor cleared here, now a
  fourteenth consecutive unit without a live Drill
  Ground read.
- Result stats: target 4, achieved 0, verified no.
  Partial: 0 barracks verified, 0 batches queued,
  tracker untouched, so the next tick re-produces this
  regular. Follow-up: re-ground the four tent positions
  on the current base layout before any tap, and read
  the Drill Ground screen live first if a panel opens.

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

- 1.9.0 (2026-11-02): Lv.24 tent selected at 825,578 with the action row measured (paw 623,499, pistol 763,510, up arrow 903,494), both action-row taps switching to the world map so the pistol/paw mapping is suspended, not merely disputed, Drill Ground Full carried unverified an eighth consecutive unit, and the recurrence commented onto Issue #150, folded from the 0811 training unit; the How to enter pistol-to-TRAIN-UNITS claim is corrected to suspended, not silently kept.

- 1.10.0 (2026-11-02): Lv.24 pistol entry re-established with a fresh-grounded row (tent 806,581; pistol 794,605) so the 0811 suspension is lifted in part for Lv.24, the Lv.20 pistol route retired after two fresh-point failures, the Train button grounded at 628,793 against a 70-pixel-low estimate, the Lv.24 T8 batch queued and verified by the live resource drop, and Drill Ground Full carried unverified a ninth consecutive unit with a successful queue as counter-evidence, folded from the 1146 training unit.

- 1.11.0 (2026-11-02): inherited 1146 Lv.24 points (tent 806,581, pistol 794,605) failing to open any panel in this camera view, so the fresh-grounding rule is re-affirmed against reusing a verified entry, Lv.24 busy status carried as expectation only with no live panel read, Lv.27 and Lv.30 not inspected, Drill Ground Full carried unverified a tenth consecutive unit without a live read, and the HUD stock snapshot (food 387.7M, iron 577.5M, coins 54.0M) matching the 1520 harvest read, folded from the 1723 training record.

- 1.12.0 (2026-11-02): upward drag (500,600 to 500,300) not panning at all with the screenshot unchanged, so the drag was likely intercepted by the squad-vehicle radial left open by the previous survivors unit, close-or-deselect-before-drag next-unit rule, 0 barracks checked with no TRAIN UNITS panel, Drill Ground Full carried unverified an eleventh consecutive unit, Lv.24 busy carried as expectation only, HUD matching the 1945 harvest snapshot, and the recurrence commented onto Issue #150 by the executor, folded from the 1949 training unit.

- 1.13.0 (2026-11-02): upward drag (500,700 to 500,400) moved the view this time unlike 1949 but brought no barracks tent into view, only empty snow below the shifted central cluster, so 0 barracks checked with no TRAIN UNITS panel, Drill Ground Full carried unverified a twelfth consecutive unit, Lv.24 busy carried as expectation only with no live panel read, HUD matching the 2247 harvest close, and the recurrence commented onto Issue #150 by this run, folded from the 2255 training unit.

- 1.14.0 (2026-11-03): centre vertical drag (500,650 to 500,300) moving nothing while the left-road drag (200,600 to 200,300) restored the central cluster, so drag-pan responsiveness varies by start surface, no barracks tent in the restored central view with no TRAIN UNITS panel, Drill Ground Full carried unverified a thirteenth consecutive unit, pass budget ending mid-unit, and the recurrence commented onto Issue #150 by this run, folded from the 0252 training unit.

- 1.15.0 (2026-11-03): no barracks tent in four framings (central, upper, right-side) with no TRAIN UNITS panel, road drags panning again consistent with 0252 as a further Issue #150 data point commented by this run, 2026-10-25 "lower middle" tent description marked stale for the current layout (furnace and house cluster, not tents) without deleting history, Drill Ground Full carried unverified a fourteenth consecutive unit, 0 barracks verified and 0 batches queued, folded from the 0647 training unit.


- 1.17.0 (2026-11-03): tent-blocker breakthrough (1552 unit, fresh grounding returning three tent points, Lv.27 tent tap at (630,592) selecting Barracks Lv.27 with its label and button row confirmed, pistol re-grounded at (612,608) opening TRAIN UNITS, Lv.9 batch of 726 queued and verified by the live food and iron drop, Drill Ground Full block not presenting at this barracks, other three barracks not reached so partial), T9 defense corrected 6.6 to 6.67 per the live panel read, and the breakthrough commented onto Issue #150 by this run, folded from the 1552 training record.

- 1.18.0 (2026-11-03): production-grid buildings tapped building by building are Titanium Alloy Factories No.1, No.2 and No.3 (all Lv.30), each showing only an info button and small icons, never a TRAIN UNITS row; green military structures on the grid's right side are not selectable (three direct taps, no selection, no panel); the 1552 tent point (630,592) QUALIFIED as framing-bound after it selected Factory No.3 Lv.30 in the 2144 framing, so the How to enter proven-entry claim now carries the framing bound; a centre double-click produced no zoom change; Drill Ground Full neither confirmed nor cleared (no barracks reached, no Drill Ground figure read live); HUD stock snapshot (food 275.0M, iron 612.5M, coins 34.2M, power 149,948,901); the next-unit rule (different base area or pinch-zoom framing before tapping, never re-tap the factory row as tents) and the recurrence commented onto Issue #150, folded from the 2144 training unit.

- 1.24.0 (2026-11-05): 0534 training unit folded (failed, thirty-fourth consecutive screen-capture failure, no game screen read, no input dispatched, probe OFF_SCREEN_WINDOW, Chrome observes normally in the same session, inbox 70, tracker untouched); CORRECTION - the 1734 "running fullscreen 1920x1080" wording and the 1147 "fullscreen framing" wording are superseded, the window is windowed on an inactive Space (0134 View-menu read, re-confirmed by 0204, agreed by the 0534 probe), and the unblock is getting the window back onto the active Space (owner Dock-icon click); the thirty-fourth occurrence commented onto Issue #282 by this run. (1.19.0 through 1.23.0 carry sections without changelog lines; the numbering is preserved, not rewritten.)

- 1.25.0 (2026-11-07): 1655 training unit folded (partial, Lv.27 T9 x726 at cap and Lv.30 T10 x793 at cap requeued and HUD-verified, 9.6M food plus 9.6M iron spent, two upper-right barracks unchecked so the keep-every-barracks-busy aim is not fully met, Drill Ground Full not seen but not closed with no live Drill Ground read, Lv.30 tap-the-body-not-the-circle entry lesson, white '?' bubble at (113,582) handed to the next survivors unit), folded from the 1655 training record.

## What the 2026-11-03 1051 unit added - three framings, still no tent, road drag pans where centre drag does not

- Ticker-1034, unit training-2026-11-03-1003, about
  10:50 to 10:51 local, status partial. Evidence in
  `_records_/2026-11-03/troop-training/1051-queue-run.md`.
- Tent search, three framings, no tent tapped: from
  the survivors unit upper view, a reverse centre
  drag (500,700 to 500,300) produced no visible view
  change; a road drag (200,600 to 200,300) restored
  the central view. The central lower-middle holds
  the furnace and the house cluster, the upper view
  holds the Capitol pyramid and pink buildings -
  neither framing presented a barracks tent, and no
  TRAIN UNITS panel was opened. The drag contrast
  matches the 0647 unit: road drags pan, centre
  drags sometimes do not.
- No batch was queued, no barracks queue state was
  verified, and no Drill Ground figure was read live
  in this unit, so the 2026-10-31 Drill Ground Full
  blocker is neither confirmed nor cleared here.
  No new Issue was filed: this is the known tent
  and Drill Ground blocker already tracked as Issue
  150; this unit adds only the framing data point
  above.
- Why partial, not done: 0 of 4 barracks verified and
  0 batches queued, so the keep-every-barracks-busy
  standard is unmet. Tracker untouched, per the rule
  for partial units.
- Follow-up for the next training unit: re-ground
  the four tent positions on the current base layout
  before any tap, rather than working from the
  2026-10-25 lower-middle description, which does
  not match the current framings; read the Drill
  Ground screen live first if a panel opens. No
  earlier claim superseded.

## What the 2026-11-03 1552 unit added - tent blocker broken, Lv.27 T9 batch queued and HUD-verified

- Ticker-1534, unit training-2026-11-03-1403, about
  15:43 to 15:52 local, status partial. Evidence in
  `_records_/2026-11-03/troop-training/1552-queue-run.md`.
- Breakthrough on the standing tent blocker (Issue
  150): fresh visual grounding on the live central
  base frame returned three barracks tent points, and
  the tap at norm (630,592) selected Barracks Lv.27,
  confirmed by its on-screen label and button row
  (paw Details, orange pistol Train, green upgrade
  arrow untouched). The Lv.27 tent point (630,592)
  is a proven entry but must still be re-grounded,
  never inherited blindly.
- The pistol button was re-grounded at norm
  (612,608) before tapping, so the green upgrade
  shortcut was never at risk. TRAIN UNITS opened
  with Lv.9 preselected, count slider at the cap
  726, cost 4.1M food and 4.1M iron, time 1d
  10:19:35 - matching the Lv.27 T9 archive (power
  1352, HP 4121.49, attack 33.13, defense 6.67, Lv.10
  locked). The profile's T9 defense figure is
  corrected 6.6 to 6.67 on this live panel read.
- Train tapped (blue button, norm (630,778)).
  Finish Now was never tapped. The panel closed with
  no error and no Drill Ground block shown, so the
  2026-10-31 Drill Ground Full blocker did not
  present at this barracks. This is counter-evidence
  against the carried block, not a clearance claim:
  the other barracks were not reached and no Drill
  Ground panel was read live.
- Queue verified live from the HUD, not assumed
  from the panel close: food 251.1M to 247.0M (minus
  4.1M) and iron 592.7M to 588.5M (minus about 4.1M
  at displayed 0.1M precision). One T9 batch of 726
  is now training in the Lv.27 barracks.
- Why partial, not done: the other three barracks
  were not reached in this unit, so the
  keep-every-barracks-busy standard is unmet.
  Tracker untouched for the unreached barracks.
- Follow-up for the next training unit: the tent
  grounding works - re-ground the tents on the live
  frame and work the remaining three barracks the
  same way (tent tap, pistol tap, Train tap, HUD
  verification). Issue #150 is commented with this
  breakthrough by this run, not closed here -
  closure belongs to the daily retro.

## What the 2026-11-03 2144 unit added - production grid is factories, 1552 point does not transfer across framings

- Ticker-2134, unit training-2026-11-03-1803, about
  21:34 to 21:44 local, status partial. Evidence in
  `_records_/2026-11-03/troop-training/2144-queue-run.md`.
- Changed method versus the 0252, 0647 and 1051 units
  (queue rule R2): instead of only re-framing, this
  unit systematically tapped the production grid
  building by building on the live frame, and
  re-tried the proven 1552 point after re-framing.
- Results on the live frame: the dark-roofed
  buildings in the grid are Titanium Alloy
  Factories, not barracks - taps selected Factory
  No.1 Lv.30, No.2 Lv.30 and No.3 Lv.30 in turn,
  each showing only its info button and small
  icons, never a TRAIN UNITS button row. The
  green military structures on the right side of
  the grid are not selectable: direct taps on
  three of them produced no selection and no
  panel. The barracks tents are not in the
  production grid reached here.
- CONTRADICTION RESOLVED, in favour of the newest
  verified record, by QUALIFICATION (not erasure):
  the proven 1552 point norm (630,592), re-tried
  after a rightward drag re-framing, selected
  Factory No.3 Lv.30 in this framing, not a
  barracks tent. The 1552 frame therefore used a
  different zoom or a different base area than
  the framing reached here; its point does not
  transfer to this framing. The 1552 event stands
  as history - a Lv.27 T9 batch was queued and
  HUD-verified in that frame - but the point is
  now framing-bound, and the How to enter section
  carries that bound. A double-click at the grid
  centre produced no zoom change.
- Drag-pan notes, consistent with earlier units:
  road and open-snow drags pan; centre drags
  over buildings sometimes do not. Drags used:
  down, up, rightward and leftward, all
  dispatched.
- HUD resources at start: food 275.0M, iron
  612.5M, coins 34.2M, power 149,948,901 - read
  from the base screen, unchanged by this unit.
- No batch was queued, no barracks queue state
  was verified, and no Drill Ground figure was
  read live in this unit, so the 2026-10-31
  Drill Ground Full blocker is neither confirmed
  nor cleared here.
- Why partial, not done: 0 of 4 barracks verified
  and 0 batches queued, so the
  keep-every-barracks-busy standard is unmet.
  Tracker untouched, per the rule for partial
  units; the next tick re-produces training and
  resumes the search.
- Follow-up for the next training unit, from the
  record under rule R2: the barracks tents are
  not in the production grid reached here. Try
  a different base area or a pinch-zoom framing
  before tapping, and do not re-tap the factory
  row as if it were tents. No new issue filed:
  this is the known tent blocker already tracked
  as Issue #150; this run comments the recurrence
  onto #150.

## What the 2026-11-04 0143 unit added - factories confirmed again, 1552 tent point not re-tried, Tank Base upgrade in progress

- Unit training-2026-11-03-2203 by ticker-0134,
  about 01:43 local, status partial. The "active on
  a different device" dialog appeared on entry;
  Confirm was tapped once per the owner rule (kick
  1 of this pass), the app exited as usual, and it
  was reopened and reached the base screen.
- Tank Base Lv.28 selected on the central frame
  (607,468): its button row shows the green upgrade
  arrow (never tapped) and a red-panda Details
  button. The Details panel confirms an upgrade
  Lv.28 to 29 in progress with 21:17:49 remaining,
  cost line iron 922,228/1.7M, and a Finish Now
  price of 2,032 diamonds - none of these were
  tapped. Panel closed with X.
- Tent search: fresh visual grounding on the live
  central frame returned points that selected
  Titanium Alloy Factories, not barracks - norm
  (389,463) gave Factory No.1 Lv.30, norm (504,626)
  gave Factory (Weekly Pass) Lv.30. This confirms
  2144: the dark-roofed grid buildings are
  factories. Grounding on the upper-base frame
  converged on norm (938,240) at the far right
  edge; the tap produced only an Alliance Gifts
  toast, no selection.
- Pans used: one upward drag reached empty snow
  below the grid, one downward drag reached the
  formation parking areas above, one upward drag
  returned the view to the central frame. Game left
  on the central base view.
- Not re-tried: the 1552 tent point (630,592) was
  not re-tried in this unit's framings. Follow-up
  stands: re-ground the tents on the live frame
  first, and do not re-tap the factory row as if it
  were tents. Known blocker Issue #150; this run
  comments the recurrence onto #150.
- HUD resources at end, unchanged by this unit:
  food 391.8M, iron 727.5M, coins 548.9K, power
  150,028,269. No batch was queued, 0 of 4 barracks
  verified, and no Drill Ground figure was read
  live in this unit, so the 2026-10-31 Drill Ground
  Full blocker is neither confirmed nor cleared
  here.

## What the 2026-11-04 0440 unit added - tent point resolved for Lv.24, Drill Ground Full confirmed live again, clearing method still open

- Unit training-2026-11-04-0203 by ticker-0434, about 04:40 local, status partial. No "active on a different device" dialog appeared.
- Tent search resolved on this framing: visual grounding on the live central frame returned a tent point at norm (585,548), and the tap selected Barracks Lv.24 with its button row (paw Details, pistol Train Units, green upgrade arrow never tapped). This point is distinct from the factory-row points that misled the 0143 unit and from the 1552 point (630,592). The next unit starts from (585,548). (2026-11-04 0814 correction: (585,548) selected Arena Lv.1 in the 0814 framing, not a barracks - the point is framing-bound like the 1552 point and must not be carried as a standing tent coordinate; re-ground the tent on the live frame in every unit.)
- Train attempt: the pistol button, grounded on the live frame at norm (544,580), was tapped and the game answered with the toast "Drill Ground Full: Unable to add more units" - no Train Units panel opened. The 2026-10-31 Drill Ground Full blocker is therefore CONFIRMED live again at this barracks, by the Train tap itself, not assumed from an earlier unit. An earlier mis-aimed tap at norm (465,505) landed on the world map instead of the button row; it was undone with the home button and no world action was taken. Do not re-aim at (465,505).
- Preparatory read, per the activity metadata: the Lv.24 barracks Details panel was opened (paw button, norm (468,580) by offset from the grounded pistol point). It reads Training Count +666, matching the T8 count in the activity metadata, with instructors Maria, Hannah, James and Christopher assigned, and no training timer shown in Details. The panel was closed with X; nothing was queued, dispatched or spent.
- HUD resources at end, unchanged by this unit: food 397.0M, iron 732.0M, coins 3.1M, power 150,028,269 - consistent with the 0413 harvest and 0416 reads, not a contradiction. 0 of 4 barracks queued, 1 of 4 verified (Lv.24, blocked by Drill Ground Full); the other three barracks remain unverified this unit. Tracker untouched, per the rule for partial units.
- Open question carried, not closed: the clearing method for a full Drill Ground is still unknown - no clearing method was found or claimed in this unit. The 0143 follow-up (re-ground the tents first) is satisfied for Lv.24 on this framing by the (585,548) point; the blocker that remains is the Drill Ground itself. Evidence commented onto Issue #150 by the ticker unit, fold noted here.

## What the 2026-11-04 0814 unit added - 0440 tent point selects Arena in this framing, Lv.20 verified via Details, framing instability, Drill Ground Full neither reconfirmed nor cleared, partial

- Unit training-2026-11-04-0603 by ticker-0804, about 08:14 local, status partial. Sessions cc-435 and cc-436 (the first session closed mid-unit and was restarted; no device contention). No 'active on a different device' dialog appeared on entry; no takeover was needed. Evidence in `_records_/2026-11-04/troop-training/0814-queue-run.md`.
- Method changed versus the 0440 unit (queue rule R2): inherited points were NOT trusted. The 0440 tent point (585,548) was tried once and selected Arena Lv.1 in this framing, not a barracks, proving again that tent points do not transfer across camera framings (see the correction in the 0440 section). The grounded Drill Ground candidate (722,610) produced no panel. Every later tap was grounded fresh on the live frame of that moment.
- Barracks verified, 1 of 4: after a drag-pan down (drag from (300,500) to (300,300) on the base screen, which moved the view down to the tent row), a fresh-grounded tent tap selected Barracks Lv.20 with its button row (paw, pistol, green upgrade arrow never tapped). Its middle button opened the Building Details panel, not a Train Units panel: Training Count +613, matching the T7 count in the activity metadata for the fourth barracks, instructors Alexis, Joe, Jolene and Anthony, no training timer shown in Details. This button mapping differs from the 0440 record (paw Details, pistol Train Units); in this frame the middle button behaved as Details. The panel was closed with its X; nothing was queued, dispatched or spent.
- Framing instability, measured: closing the Details panel returned the camera to a different framing, so re-tapping the same tent point (660,893) opened the chat panel instead of the tent. The chat panel was closed at once with its back arrow; nothing was typed, sent, opened or acted on there, and no chat content is recorded here. A second drag-pan down restored the tent row, but two further fresh taps on tent candidates ((467,727) grounded, and (592,831) read off the live frame) selected nothing, and the unit's time was then spent.
- HUD resources at end, unchanged by this unit: food 415.2M, iron 745.8M, coins 15.2M, power 150,028,269 - consistent with the 0755 harvest gains, not a contradiction. No batch was queued and no Train Units panel was reached, so the Drill Ground Full toast was neither reconfirmed nor cleared in this unit; the 0440 live confirmation still stands as the latest Drill Ground read. 0 of 4 barracks queued, 1 of 4 verified (Lv.20 Details only), so the 'keep every barracks busy' standard is unmet. Tracker untouched, per the rule for partial units; the next tick re-produces training and resumes from the findings below.
- Follow-up for the next training unit, in order: (1) which button in the current framing actually opens Train Units, since the middle button opened Details here; (2) the Drill Ground clearing method, still unknown. This is the known tent / Drill Ground blocker already tracked as Issue #150; no new issue filed. The framing-instability comment onto #150 is DEFERRED by this run: the 0814 record names it as a comment only if the next unit confirms it again, so no #150 comment is made here.
- Red lines: nothing spent at all; no Train button completed a queue, no Finish Now, no green upgrade shortcut, no building started, no squad dispatched, no other activity's work done, no chat message sent.

## What the 2026-11-04 1147 unit added - fullscreen framing mismatch, four grounded tent taps no panel, centre drag no view move, Issue 150 repeat, partial

- Unit training-2026-11-04-1003 by ticker-1134, about 11:47 local, status partial. Sessions cc-453 then cc-454 (the first session dropped mid-unit and was reopened; no data was lost - a control-channel recovery repeat of the 0917 and 0814 pattern, not a game-state event). No "active on a different device" dialog appeared. Chrome was the frontmost app on the Mac during this unit; background input to the Last War window still dispatched.
- Tent search, no panel reached: four grounded taps on the live fullscreen base frame - norm (368,545), norm (435,465), norm (555,460) and norm (438,545) - each dispatched, but no building label and no button row (paw Details, pistol Train, green upgrade arrow) appeared in the following screenshots, so no TRAIN UNITS panel was ever reached. One drag (norm start (450,550) to (650,350)) did not move the base view; the framing stayed identical across screenshots. The centre-drag no-move is consistent with the 0252 and 0647 reads (road drags pan, centre drags do not), not a new drag rule.
- Framing mismatch, qualified not contradicted: the fullscreen 1920x1080 framing does not match the 2026-11-03 success frame, where a grounded tap at norm (630,592) selected Barracks Lv.27. This does not contradict the standing rule - the 2144 section already qualified (630,592) as framing-bound (it selected Titanium Alloy Factory No.3 in the 2144 framing) - so the mismatch is the framing-bound rule playing out again in a fullscreen framing, not a portable coordinate failing.
- Focus refusals, retried not recorded as access failures: one early click was refused for focus reasons ("user working in another window") and one click was refused for a stale observation; both were retried and the following taps dispatched. Neither refusal is an access failure.
- Follow-up from the record itself: the next unit re-grounds on its own live frame rather than reusing any point from this unit, and tries the windowed (non-fullscreen) Last War window if the fullscreen frame keeps refusing to select a tent.
- No barracks queue state was verified, no batch was queued, and no Drill Ground figure was read live in this unit, so the 0440 live Drill Ground Full confirmation still stands as the latest Drill Ground read - neither reconfirmed nor cleared here. This is the known tent blocker already tracked as Issue #150; no new issue was filed, and this run comments the fullscreen-framing recurrence onto #150.

## What the 2026-11-04 1734 unit added - screen-capture failure, eleventh consecutive pass, nothing read

- Unit training-2026-11-04-1403 by ticker-1734, about 17:34 to 17:46 local, status failed. Evidence in `_records_/2026-11-04/troop-training/1734-queue-run.md`. No barracks was opened, no batch was collected or requeued, and no training count was verified.
- No game screen was ever read and no game input was dispatched. The Mac screen-capture stream failed on every attempt across two computer sessions: session cc-473 open_app LastWar returned outcome_unknown, then computer.observe (compact) failed; session cc-474 observe (compact) failed, computer.control activate selected the LastWar window for background input but captured no observation, observe (compact) failed again, observe (image) failed, and a final observe (compact) failed after a healthy connection repair check, all with "Failed to start stream due to audio/video capture failure". The control channel itself was reachable (computer.control list_apps confirmed LastWar running and selected as target); the capture stream was not. The device connection health was healthy on both native and web transports, LastWar (com.lastwar.ios, pid 59735) was running fullscreen 1920x1080, and Google Chrome was frontmost. Screen-recording permission is granted on the device.
- No blind taps were dispatched: without an observation, any tap could land on the wrong control, so the unit stops here under the check-first rule. The pass stopped after this unit rather than failing further units identically, since every further unit needs the same capture channel.
- Recurrence, not a new failure class: this is the eleventh consecutive ticker pass to fail on this exact blocker (ticker-1224 help 1235, ticker-1327 mail 1333, ticker-1340 star-ceremony 1344, ticker-1404 train 1404, ticker-1434 passes 1434, ticker-1504 donations 1504, ticker-1534 radar 1534, ticker-1604 arms-race 1604, ticker-1634 harvest 1634, ticker-1704 survivors 1707, ticker-1734 training 1734), now across eleven activities. The blocker is filed as Issue #284 (tooling, filed by the ticker-1340 pass) alongside the knowledge Issue #282 filed by the 1332 organizer run; this pass commented on #284 (comment 6647208826) instead of filing a duplicate, and this run comments the eleventh and twelfth occurrences onto #282.
- Reading warning: this failed unit gives zero evidence about training state. It must NOT be read as "no batch due" or as a queue state - the 0440 live Drill Ground Full confirmation still stands as the latest Drill Ground read, and the 1147 framing findings stand; this unit rests on no read at all. The Drill Ground clearing method remains unknown, carried forward from Issue #150, not closed.
- Tracker untouched for failed, per the queue rules; the next tick re-produces this regular.

## Correction 2026-11-05 - the game window is windowed on an inactive Space, not in native fullscreen

- Source: the 0134 survivors record (`_records_/2026-11-05/survivor-intake/0134-queue-run.md`, ticker-0134, twenty-sixth consecutive capture failure), re-confirmed by the 0204 gifts record (`_records_/2026-11-05/alliance-gifts/0204-queue-run.md`, ticker-0204, twenty-seventh). The View menu lists "Enter Full Screen" (read from the menu-action error listing in session cc-505, repeated probe in cc-508 with the menu unchanged), so the app is NOT in native fullscreen: it is a windowed window on an inactive Space, and the capture failure is the pixel stream of an off-screen window, not a broken screen-recording permission (Chrome windows observe normally in the same sessions). The 0534 troop-training pass agrees: its probe classifies OFF_SCREEN_WINDOW at high confidence, and the window is listed as 2560x1440 at (0,360) - a windowed geometry, not a fullscreen frame.
- Superseded in this profile: the "running fullscreen 1920x1080" wording in the 1734 section above, and the "fullscreen framing" wording in the 1147 section above. The 1147 framing findings stand unchanged - the tent points are framing-bound, and the mismatch is the framing-bound rule playing out, not a portable coordinate failing. The 1147 follow-up (try the windowed Last War window) already points at the corrected model.
- Follow-up set: no unblock was stated in the 1734 section; the standing unblock is now getting the window back onto the active Space, and the owner clicking the LastWar Dock icon once is the known reliable step (or run `_tools_/mac_lastwar_front.sh` in Terminal, then re-probe). Background-sent Space keys do not switch Spaces, set_window_frame is gated by the stale-observation rule, Cmd+Tab is blocked by the tool, and list_windows needs the exact app name "LastWar". Never use Control-Command-F or Escape on this app (both crash it).
- This correction does not change the training state: the 0440 live Drill Ground Full confirmation still stands as the latest Drill Ground read; no barracks, batch or Drill Ground figure was read in the failed passes and none is asserted here. The thirty-fourth occurrence is commented onto Issue #282 by this run; Issue #284 already tracks the blocker.

## What the 2026-11-05 0534 unit added - screen-capture failure, thirty-fourth consecutive pass, nothing read

- Unit training-2026-11-05-0203 by ticker-0534, about 05:34 to 05:45 local, status failed. Evidence in `_records_/2026-11-05/troop-training/0534-queue-run.md`. No barracks was opened, no batch was collected or requeued, and no training count was verified. On a working screen this unit would have checked the four barracks and requeued any idle batch, and would have read the Drill Ground screen live first under the standing third-strike blocker note (Drill Ground Full, 39,460 of 39,460).
- No game screen was ever read and no game input was dispatched. The Mac screen-capture stream failed on every attempt in computer session cc-522: computer.control activate selected the LastWar window for background input but captured no observation, computer.observe (compact) failed three times with the same error (a 10 second wait between attempts 1 and 2 changed nothing), and computer.control open_app LastWar returned outcome_unknown with no verifiable launch result and the window still listed under the same pid, all with "Failed to start stream due to audio/video capture failure". The capture pipeline itself works: a Chrome window observed normally in the same session (the Coordinator harness tab, full accessibility tree), so the fault is specific to the LastWar window. LastWar (bundle com.lastwar.ios, pid 59735) is running, a 2560x1440 window at (0,360) on an inactive Space, window_id 160366; Google Chrome was frontmost at session start, Keychain Access frontmost at the close of the probe. `activate` reports `window_on_screen: false` and `brought_to_front: false`.
- Probe classification: `_tools_/mac_capture_probe.py` (tool version 1.0.0) classifies OFF_SCREEN_WINDOW (high confidence), stop_pass yes, exit code 10. The LastWar window sits on an inactive Space, so its pixel stream cannot start.
- Recovery still needs the one owner step: click the LastWar Dock icon once on the Mac mini (or run `_tools_/mac_lastwar_front.sh` in Terminal), then re-probe. No background control route moves the window - Space keys sent in the background do not switch Spaces, open_app returns outcome_unknown, and set_window_frame needs a fresh observation, which is exactly what the failure prevents. Never use Control-Command-F or Escape on this app (both crash it).
- Recurrence, not a new failure class: this is the thirty-fourth consecutive ticker pass to fail on this exact blocker (ticker-0504 the thirty-third). The blocker is filed as Issue #284 (tooling) alongside the knowledge Issue #282; this pass commented on #284 (comment IC_kwDOVXE0ls8AAAABjO5-yA) instead of filing a duplicate, and this run comments the thirty-fourth occurrence onto #282.
- Reading warning: this failed unit gives zero evidence about training state. It must NOT be read as "no batch due" or as a queue state - the 0440 live Drill Ground Full confirmation still stands as the latest Drill Ground read, and the 1147 framing findings stand; this unit rests on no read at all. The Drill Ground clearing method remains unknown, carried forward from Issue #150, not closed.
- The pass stopped after this one unit - every further unit needs the same game screen, and the probe says to stop. The inbox held 70 units at this pass. No other unit was attempted. No different-device dialog was observed (no screen was ever captured) and no device takeover was needed.
- Tracker untouched for failed, per the queue rules; the next tick re-produces this regular.

## What the 2026-11-07 1655 unit added - Lv.27 T9 and Lv.30 T10 requeued, two barracks unchecked, Drill Ground Full not seen, partial

- Unit training-2026-11-07-1403 by ticker-1655, about 17:08 to 17:12 local, status partial. Evidence in `_records_/2026-11-07/troop-training/1655-queue-run.md` (commit 514e333e5b on records/2026-11-07). Computer session cc-19, LastWar already running on the Mac mini.
- Lv.27 barracks (center tent, timer bubble now above it): TRAIN UNITS panel read Power 1352, Morale 625.0, Squad Load 2000, Unit HP 4121.49, Attack 33.5, Defense 6.74; Lv.9 selected, count 726 at cap, cost 4.1M food plus 4.1M iron, time 1d 10:19:35. Train tapped; panel closed and the HUD moved food 486.5M to 482.3M and iron 810.0M to 805.9M. Batch started. (726 at cap matches the 1552 batch - the cap is stable.)
- Lv.30 barracks (tent below-right of the first; its portrait circle overlaps the tent body - tap the body, not the circle): TRAIN UNITS panel read Power 1647, Morale 750.0, Squad Load 2200, Unit HP 4726.34, Attack 38.45, Defense 7.7; Lv.10 selected, count 793 at cap, cost 5.5M food plus 5.5M iron, time 1d 17:14:37. Train tapped; panel closed and the HUD moved food 482.3M to 476.8M and iron 805.9M to 800.4M. Batch started.
- Total spent in this unit: 9.6M food and 9.6M iron for 726 T9 plus 793 T10 troops. Both requeued barracks now carry a clock timer bubble. Finish Now was never tapped.
- The other two barracks (upper-right tents) were not checked in this unit, so the "keep every barracks busy" aim is not fully met. The next training unit starts with those two. Tracker untouched, per the partial rule; the next tick re-produces the training regular.
- The Drill Ground Full blocker from the 2026-10-31 retro was not seen: both Train taps succeeded and no capacity message appeared. No Drill Ground screen was read live in this unit, so the blocker is not closed, only not encountered - it is carried forward, not cleared.
- Handover observation for the next survivors unit: a white "?" speech bubble stands at the left edge near the front gate (norm about 113,582) in the closing screenshots of this unit - a waiting survivor may have arrived after the survivors unit closed unverified minutes earlier.
- Figures read live: food 486.5M at entry, 482.3M after the first batch, 476.8M at close; iron 810.0M, 805.9M, 800.4M; coin 5.7M; stone 25.0M; 922.2K; power 149,850,353. No diamonds, money, speedups or paid buttons were used. No login or verification was demanded, and no different-device dialog appeared.
