---
title: Alliance Train
created: 2026-10-25T20:12:00Z
modified: 2026-11-09T10:32:17Z
level: L1
version: 1.34.0
description: Boarding the alliance train at the station for carriage rewards, one activity folder for train knowledge
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-25
  - source: in-game Train Operation Guidelines text, read 2026-10-25
  - source: owner task request naming a train task, 2026-10-25
  - source: in-game screens observed on the owner Mac mini, 2026-11-01 (1325 train unit)
  - source: in-game screens observed on the owner Mac mini, 2026-11-01 (1813 train unit)
  - source: ticker-2142 train execution record 2026-11-01 2149 queue run
  - source: ticker-0034 train execution record 2026-11-02 0044 queue run (checked only, no train read, superseded same-pass by the 0047 sighting)
  - source: ticker-0334 alliance-train execution record 2026-11-02 0348 queue run (done, checked only)
  - source: ticker-0704 alliance-train execution record 2026-11-02 0715 queue run (done, checked only)
  - source: ticker-0834 alliance-train execution record 2026-11-02 0844 queue run (done as checked only, third Secret Command Post wrong-tap instance, station empty)
  - source: ticker-1234 alliance-train execution record 2026-11-02 1246 queue run (done as checked only, station empty)
  - source: ticker-2034 alliance-train execution record 2026-11-02 2045 queue run (done, station check corrected, already aboard carriage 2)
  - source: alliance train execution record 2026-11-02 2320 queue run
  - source: ticker-0034 alliance-train execution record 2026-11-03 0035 queue run (partial, left-column mapping measured, no station view)
  - source: ticker-0304 alliance-train execution record 2026-11-03 0315 queue run (partial, 52,548 no-pan repeat, grounding mislabels Secret Command Post)
  - source: ticker-1104 alliance-train execution record 2026-11-03 1124 queue run (partial, fourth same-blocker partial today, banner absent, station not viewed, Issue 205)
  - source: ticker-1334 perception-scout execution record 2026-11-03 1345 queue run (partial, station preparation-only surface, LOOT box located on the world map)
  - source: ticker-1734 alliance-train execution record 2026-11-03 1742 queue run (partial, fifth check-only outcome today, banner absent, station not viewed)
  - source: ticker-0204 alliance-train execution record 2026-11-04 0217 queue run (partial, sixth check-only outcome in a row, banner absent, station not viewed)
  - source: ticker-0504 alliance-train execution record 2026-11-04 0509 queue run (partial, seventh check-only outcome in a row, grounding mislabel at 55,563 opened the truck screen)
  - source: ticker-0834 alliance-train execution record 2026-11-04 0839 queue run (partial, check-only, no boarding banner, no train icon, station not viewed)
  - source: ticker-1404 alliance-train execution record 2026-11-04 1404 queue run (failed, Mac screen-capture failure on every capture step, no game input dispatched, fourth consecutive ticker pass to fail this way, Chrome-window observation succeeded in the same session so the fault is specific to the Last War fullscreen window, Issue 284)
  - source: ticker-1818 alliance-train execution record 2026-11-07 1826 queue run (check-only partial, ninth in a row, no banner, station not viewed)
  - source: ticker-2134 perception-scout execution records 2026-11-07 2140/2153 queue runs (partial, station panel re-checked, third no-train confirmation in one pass, check-signals-first entry route; record commit fe5a1e7fd3 on records/2026-11-07)
  - source: ticker-2304 perception-scout execution records 2026-11-07 2311/2317 queue runs (partial, station panel re-checked, fifth no-train confirmation in one pass, Train Conductor appointments in the Record Event tab; record commit 03dc69e0c on records/2026-11-07)
  - source: ticker-0004 perception-scout execution record 2026-11-08 0022 queue run (partial, midday remainder, station panel re-checked, fourth no-train confirmation, no train preparing; record commit e6192726d1 on records/2026-11-08)
  - source: ticker-0104 perception-scout execution record 2026-11-08 0118 queue run (partial, alliance remainder station check, sixth no-train confirmation in the scout-mid-2026-10-31 chain, no train preparing; record commit 33bb20050a on records/2026-11-08)
  - source: ticker-0434 perception-scout execution record 2026-11-08 0440 queue run (partial, station re-check, both preparation signals absent, record commit caa661bab on records/2026-11-08)
  - source: ticker-0434 perception-scout execution record 2026-11-08 0447 queue run (done, alliance remainder, Train Conductor appointments, record commit caa661bab on records/2026-11-08)
  - source: ticker-2201 alliance-train execution record 2026-11-08 2211 queue run (partial, checked only, both preparation signals absent, no train preparing; record commit 8960535c on records/2026-11-08)
  - source: ticker-0204 alliance-train execution record 2026-11-09 0215 queue run (partial, checked only, both preparation signals absent, banner-only check, 37 seconds; record commit facef628c on records/2026-11-09)
---

# Alliance train

## What this activity is

The alliance runs trains from the base station. A member's part is to
board - pick one of the four carriages of a train in preparation and
take a seat before it departs. Each carriage carries different
rewards. This folder accumulates train knowledge. Executions are
recorded in `_records_/<date>/alliance-train/`, one file per
execution.

Naming note - the owner named a train task on 2026-10-25 alongside a
truck task. Troop training is registered separately as
[`troop-training`](../troop-training/INDEX.md). This folder covers the
literal train, so both readings of the request are in the system.

## How to enter

- On the base screen, the left icon column carries a train icon. It
  pans the camera to the station at the base edge.
- Entry-icon correction, 2026-10-28 and 2026-11-01: in the
  default column set there is no separate train icon (2026-10-28
  1903: construction, research, season, chat, truck with badge 9,
  radar and hammer), and the 1813 tap on the supposed train icon
  opened the trucks view instead. The train-head entry worked in
  the 0110 unit while a train was in preparation. Treat the icon
  as set- and state-dependent: always verify the screen that
  actually opened before tapping further, the same rule as
  truck-plunder.
- Measured column map, 2026-11-03 0035: on that unit's base
  screenshot (52,508) opened the temperature panel, (52,567)
  opened the truck screen and (52,626) opened Secret Command
  Post. None of them is the train entry; do not reuse any of
  them as one. Detail in the 0035 section below.
- Failed routes, 2026-11-03 0752: the Accessibility tree was
  read first and carries no icon labels for this game (one
  iOS content group only), so it cannot ground the train
  entry - do not spend a unit on it again. A tap at
  (903,750), the Alliance icon position on the opening
  screenshot, opened MY PROFILE instead of the Alliance
  panel, so right-side icon positions on a screenshot do
  not map to taps the way the left-column positions were
  assumed to; the Alliance route is not a working train
  entry from this view. Ground taps on the
  alliance-territory map are not safe probes: taps meant
  for empty ground opened other players' profile cards
  (PrincessEsra, Amarky257), closed only by a drag from
  (500,500) to (700,700), which also panned the camera.
  Detail in the 0752 section below.
- Tap a carriage plus bubble at the station, or the train itself, to
  open the STATION PLATFORM screen - the train from top to bottom,
  its conductor, its Train Rating, the departure countdown, and four
  carriage cards each showing occupancy and its reward set.
- The i button at the top opens the Train Operation Guidelines.
- Boarding window entry, found 2026-10-25 late evening - while a
  train is in preparation, the base screen carries a top banner
  reading Boarding closes in HH:MM:SS under the resource bar, and the
  system chat announces the conductor train. Tapping the banner
  opens MY PROFILE, and the train icon at the top right of that
  screen opens the STATION PLATFORM directly. The window is short -
  the banner showed 00:02:57 on first sight - so go straight there.
  That evening the account was already aboard carriage 2, so no
  boarding action was needed or taken; how the seat was taken (the
  owner phone is the likely actor) is unobserved.

## How it is done

- Tap the plus on the carriage to board. Boarding opens a THANK THE
  CONDUCTOR dialog.
- Standing owner instruction, set on 2026-10-25 (evening) - always
  board the 2nd section (carriage 2), and always use 3 Trade
  Contracts for the ticket in the conductor dialog, autonomously.
  This supersedes the first execution, which boarded carriage 1
  with the free Like and Thank and gifted nothing.
- Gift flow, observed 2026-10-26 in the first execution of the
  standing rule - the THANK THE CONDUCTOR dialog carries a
  quantity slider starting at 1 with minus and plus buttons, a
  stock readout (143 Trade Contracts at the time), a blue Like
  and Thank button and a green Gift Contract button. Set the
  quantity to 3 with the plus button, read it back, then tap
  Gift Contract. The dialog closes, occupancy rises by one and
  the carriage plus is replaced by the own avatar. What the
  paid ticket changes over the free Like and Thank is still
  unobserved.
- Boarded state shows as the own avatar inside the carriage and the
  occupancy count rising by one.
- The THANK THE CONDUCTOR dialog does not reopen, learned
  2026-10-27 - once it is closed (or the seat is otherwise
  already held), tapping the own avatar opens MY PROFILE, the
  carriage reward card only shows item tooltips, and the
  conductor avatar opens the conductor profile. The gift
  choice is made in the boarding moment or not at all, so
  verify the carriage on the platform BEFORE tapping its plus
  whenever the entry path allows it.
- After the ride, the carriage reward arrives as an Event category
  mail titled Train arrival reward, with a Claim button on the mail.
  Claim it there - the reward does not credit silently. Claiming
  briefly opens the train DETAILS screen under a congratulations
  banner listing the granted items. Departure and arrival also
  generate plain notice mails about the conductor train in the same
  Event category, with no attachments.
- Historical note - on the first boarding (2026-10-25 midday, before
  the standing rule) the carriage was picked by its reward set and
  occupancy; carriage 1 held the richest set and the fewest riders,
  2 of 7 before boarding. The standing rule above now fixes the
  choice at carriage 2.

## Cadence

- Per train, not per day directly. The alliance can send out 1 regular
  train and 2 Mega Express Trains daily, per the in-game guidelines.
  A member can only board while a train is in preparation, so check
  the station during the daily round and board whatever is preparing.

## Scope and availability

- From the in-game Train Operation Guidelines, read 2026-10-25 -
  the alliance must have at least 20 members; the member must have
  unlocked the train station and been in the alliance over 24 hours;
  only alliances in the top 50 of the server ranking get a regular
  train each day; a regular train needs an R4 or R5 member to assign a
  conductor before it enters preparation; when no train is being
  prepared, the commander can summon a Mega Express Train and becomes
  its conductor automatically; the train has four carriages numbered
  1 to 4 from top to bottom, each carrying different rewards.
- This account - the alliance has 91 of 100 members and a 5.0 rating, and a
  train was in preparation at midday, so the alliance is active in
  this system. Whether the boarded train was regular or Mega Express
  was not displayed on the screens seen.
- Season scope - the station and its snowy platform are part of the
  Season 2 map as observed. Whether the train system persists beyond
  Season 2 is unverified.

## What is known from 2026-10-25

Observed in game on this account, first execution 2026-10-25.

- A train was in preparation with conductor another commander of the alliance, Train
  Rating 82,650, and about 3 hours 20 minutes to departure.
- Carriage occupancy before boarding - carriage 1 at 2 of 7, carriage
  2 at 3 of 7, carriage 3 at 7 of 7, carriage 4 at 12 of 7 as
  displayed, which suggests the denominator is not a hard cap.
- Boarded carriage 1 with Like and Thank. Occupancy rose to 3 of 7 and
  the own avatar appeared in the carriage. No contract was gifted -
  the account held 127 Trade Contracts at the time.
- Carriage 1 reward set as displayed - a Lv.5 chest, two chest stacks
  of 50, a badge stack, a gold chest stack of 20 and a 100 ruby item.
  When and how carriage rewards pay out was not observed - the train
  had not departed when the round ended.
- Evening follow up (about 18:12 to 19:10) - the reward arrived as
  the Event mail Train arrival reward at about 17:57 local and was
  claimed free. Granted - a Lv.3 chest (the mail grid showed it at
  Lv.3 although the platform card had shown a Lv.5 chest), crates
  100 in total, a badge 2.5K, a gold chest stack of 20, a red gem
  item of 100, and about twenty 5 minute speedups across several
  kinds. The mail Claim button was gone on recheck. Detail in the
  1812 reward claim execution record.

## What is known from 2026-11-01

Measured in the 0110 train unit (ticker-0104, window mode
642x951, no different-device dialog).

- No boarding banner on the base screen, so the station was
  checked directly: the left-column train-head icon panned the
  camera to the station, where a train is in preparation with
  conductor Missile Apex and a 00:58:50 countdown.
- A carriage plus bubble on the world view opened a departure
  animation, skipped with one tap, landing on STATION PLATFORM
  with a THANK THE CONDUCTOR dialog at quantity 1 and a 156
  Trade Contract stock readout. That dialog was closed with its
  X without gifting: the carriage tapped on the world view had
  not been verified as carriage 2, and no contract is spent on
  an unverified carriage. This is the 2026-10-27 discipline in
  action - verify the carriage on the platform BEFORE tapping
  its plus whenever the entry path allows it.
- Platform verified, top to bottom: conductor Missile Apex,
  Train Rating 59,350, countdown 00:57:56. Carriage 1 at 3/7
  with a plus, carriage 2 at 7/7 holding a portrait with a
  "Bears Lair - Oops, you stepped on me!" tooltip, carriage 3
  at 4/7 with a plus, carriage 4 at 10/7 with a plus. The
  account already holds its seat in carriage 2, the
  standing-rule carriage, so no boarding action was needed or
  taken, and no second carriage was boarded. Backed out to the
  station view, train still in preparation at 00:57:35. No
  Trade Contracts spent.
- Carriage 4 at 10/7 repeats the 2026-10-25 observation that
  the denominator is not a hard cap.


## Limits

- The standing ticket is exactly 3 Trade Contracts for carriage 2,
  pre-approved by the owner instruction above. Any amount beyond
  the 3, or any other contract spending, still needs the owner
  approval first.
- Conductors are assigned by alliance officers. Nothing here authorises
  summoning a train or taking the conductor role.


## What the 2026-11-01 1325 unit added

- Unit train-2026-11-01-1030 by ticker-1304, session
  about 13:22 to 13:23, status done as checked only.
- Base screen inspected: no "Boarding closes in" banner
  under the resource bar. The lines under the bar were
  a treasure announcement and the furnace overdrive
  line, plus the breaking-news ticker, so no train is
  in preparation at this check, matching the
  2026-10-31 checks.
- No station panel was opened and no carriage state
  was verified beyond the banner check. Nothing
  boarded, no Trade Contracts spent, no train summoned,
  no conductor role taken, no other task type touched.
- Precision qualification, recorded against the unit's
  own conclusion: banner absence alone does NOT prove
  no train is in preparation. The 0110 unit found no
  banner yet a train in preparation at the station
  (conductor Missile Apex, 00:58:50 countdown), so a
  banner-only check is a banner-only check, not a
  station-verified no-train finding. The next train
  unit that needs certainty must open the station panel
  (left-column train-head icon) rather than closing on
  the banner alone. The 2026-10-31 banner-only checks
  stand as banner-only checks under this same reading.

## What the 2026-11-01 1813 unit added

- Unit train-2026-11-01-1430 by ticker-1804, session about
  18:05 to 18:13, status done as checked only.
- Base screen inspected: no "Boarding closes in" banner
  under the resource bar. The lines under the bar were the
  furnace overdrive line and the breaking-news ticker, plus
  a President announcement, so no train is in preparation
  at this check, matching the 2026-10-31 and 1325 checks.
  Precision note, per the 1325 qualification: banner
  absence alone does NOT prove no train is in preparation,
  and this unit's station-direct attempt did not verify
  the station either (see below), so this check stands as
  banner-only plus a failed station attempt, not as a
  station-verified no-train finding.
- Station direct check attempted and corrected: the
  left-column icon tapped as a supposed train icon opened
  the trucks view instead, confirming the 2026-10-28 record
  that the left column carries a truck icon and no separate
  train icon in this set. No truck was dispatched,
  plundered or touched beyond opening that view. The view
  read Today's Trade Count 0/5 incidentally; that read is
  NOT adopted as a quota update, because it conflicts with
  the trucks 1352 close the same trade day (dispatch 4 of
  5, plunder 1 of 4) and no trucks unit ran between the two
  reads. The next trucks unit's live trade-screen read
  governs (see truck-plunder 1.12.0).
- Return navigation from the trucks view did not succeed
  in background mode: back-area clicks, an empty-area tap
  and a map drag all showed no change, so the game was
  left in the trucks view at unit close. The next executor
  should expect to start from the trucks view, not the base
  screen.
- Nothing boarded, no Trade Contracts spent, no train
  summoned, no conductor role taken, no other task type
  touched.



## What the 2026-11-01 2149 unit added

- Unit train-2026-11-01-1830 by ticker-2142, session about
  21:43 to 21:49, status done as checked and already boarded.
- Base screen inspected: no "Boarding closes in" banner under
  the resource bar, and the station check was still made -
  reinforcing the 1325 qualification that banner absence
  alone does not prove no train is in preparation.
- Left-column train icon tapped: the camera panned to the
  station at the base edge, showing a yellow train with a
  plus bubble and a station countdown of 00:20:42 at first
  sight. This qualifies the 1813 note: in the 1813 no-train
  state the left-column tap opened the trucks view, while
  here, with a train in preparation, the train icon entry
  reached the station - so the entry icon's presence follows
  the train state, and a no-train tap result does not rule
  out a train-icon entry when a train is preparing.
- The map plus bubble was tapped, which played a train
  animation ("Tap the screen twice to skip"); skipping it
  opened the STATION PLATFORM with a THANK THE CONDUCTOR
  dialog already open (quantity 1, Trade Contract stock
  163). No button of that dialog was tapped: it was closed
  with its X, so no contract was gifted and no seat was
  taken by this unit.
- Platform read live: departure countdown 00:19:30 falling
  to 00:16:09 during the check, Train Rating 70,850. No
  conductor name is recorded for this train in the unit
  record. Carriage occupancies top to bottom: carriage 1
  at 9/7 with a plus button, carriage 2 at 21/7 with no
  plus button, carriage 3 at 13/7 with a plus button,
  carriage 4 at 15/7 with a plus button. All four
  occupancies exceed the 7 denominator, strengthening the
  standing note that the denominator is not a hard cap
  (previously carriage 4 at 10/7 in the 0110 unit).
- Carriage 2 verified as the account's own seat by a new
  check: where the other carriages carry a plus button,
  carriage 2 carries a framed scenic picture, and tapping
  the small round avatar badge at that picture's lower
  right opened MY PROFILE for Lv.30 [AP3x]Bears Lair
  (149.2M power, VIP 13, [AP3x]The Apex). The
  avatar-badge-to-own-profile tap is now the verified
  boarded-state check, stronger than the 0110 portrait
  tooltip. No second boarding was attempted, and no
  carriage other than 2 was touched.
- MY PROFILE was closed with its X and the platform back
  arrow returned the game to the base screen, verified by
  the resource bar and total power 149,288,895.
- Nothing boarded, no Trade Contracts spent, no train
  summoned, no conductor role taken.

## What the 2026-11-02 0044 unit added - and its same-pass correction

- Unit train-2026-11-01-2230 by ticker-0034, session about
  00:42 to 00:44, status done as checked only - no train
  in preparation, as first read. Base screen inspected
  first: no "Boarding closes in" banner under the
  resource bar. Station check: the left-column train
  icon (visually grounded at norm 52,548 on this unit's
  base screenshot) panned the camera to the base edge.
  The station area showed no yellow train, no plus
  bubble and no station countdown - unlike the
  2026-11-01 21:43 check, which found a train in
  preparation with a 00:20:42 countdown and has since
  departed. The camera was dragged back toward the base
  after the check; the final view showed the base edge
  with Titanium Alloy Factory No.3 and still no train.
  Nothing boarded, no Trade Contracts spent.
- Contradiction resolved in favour of the newest verified
  same-pass record: the star-ceremony unit later in this
  same pass (0047, below in alliance-duel) incidentally
  saw, while restoring the camera, a train in
  preparation at the station (conductor Missile Apex,
  countdown about 01:39). That sighting supersedes this
  unit's no-train read - the 0044 check missed a train
  that was in preparation. Lesson: a station check made
  from a base-edge pan can miss a train in preparation;
  a "no train" close is provisional, and a later
  same-pass sighting of a train overrides it. The
  correction is handled as its own train unit (staged
  as train-2026-11-02-0847); no carriage was tapped and
  no boarding was attempted in the 0047 unit.
  Evidence in `_records_/2026-11-02/alliance-train/0044-queue-run.md`
  and `_records_/2026-11-02/alliance-duel/0047-queue-run.md`.

## What the 2026-11-02 0348 unit added - prior point beats fresh grounding, still no train

- Unit train-2026-11-02-0230 by ticker-0334, session
  about 03:45 to 03:48, status done as checked only.
  Base screen inspected first: no "Boarding closes
  in" banner under the resource bar. Station check:
  the left-column train icon, measured at normalized
  (52,548) from the 0044 unit's record, panned the
  camera to the base edge. The station area showed no
  yellow train, no plus bubble and no station
  countdown - the same empty state as the 0044 first
  read, and unlike the 2026-11-01 21:43 check, which
  found a train in preparation that has since
  departed. Nothing boarded, no Trade Contracts spent,
  no train summoned, no conductor role taken.
- Entry lesson, second instance this day (see also
  the trucks 0416 entry correction): two wrong taps
  in this unit, both recovered without action. A tap
  at (53,630) opened the Secret Command Post panel
  (closed with its back arrow, no Claim tapped -
  secrets are another unit's work), and a fresh visual
  grounding put the train icon at (52,650), which is
  the same wrong icon. The correct train icon point
  is (52,548), taken from the 0044 unit's record.
  Rule restated: re-grounding is not always right; a
  prior unit's measured point beats a fresh guess.
  Re-ground fresh only after the proven point fails,
  not instead of it.
- Proximity note, carried as an open question below:
  the trucks 0416 trade-entry icon grounds at
  [52,552], 4 pixels from this station point. The
  0348 station pan and the 0416 trade open differ,
  so whether these are the same column slot acting
  differently by context or two neighbouring icons is
  unresolved.
  Evidence in `_records_/2026-11-02/alliance-train/0348-queue-run.md`.


## What the 2026-11-02 0715 unit added - staged correction now moot, station panel still unopened

- Unit train-2026-11-02-0847 by ticker-0704, session about
  07:06 to 07:15, status done as checked only. No
  different-device dialog, no login demand, nothing spent,
  no carriage tapped, no train summoned, no conductor role
  taken. Evidence in
  `_records_/2026-11-02/alliance-train/0715-queue-run.md`.
- Why this unit exists: unit train-2026-11-01-2230
  (ticker-0034, 0044) read no train in preparation, but the
  star-ceremony unit later in the same pass (0047)
  incidentally saw a train in preparation at the station
  (conductor Missile Apex, countdown about 01:39 at about
  00:47). That sighting superseded the 0044 read, and this
  unit was staged to correct it. No carriage was tapped and
  no boarding was attempted in the 0047 unit either.
- The staged purpose is now moot for boarding: the 00:47
  train carried a countdown of about 01:39, so it departed
  at about 02:26, long before this 07:06 check. Whether the
  account boarded carriage 2 on that train before departure
  was never verified by any unit; if it was aboard, its
  arrival reward will surface as an Event mail for a mail
  unit to claim, and that mail is the only remaining
  evidence for that train.
- Entry and state read live: game opened on the world map
  left by the radar unit (0634), showing the
  contested-radar toast. A tap at norm 52,548 returned the
  view to the base screen (resource bar food 383.9M, iron
  574.0M, coin 48.7M, diamonds 2,526, total power
  149,296,925, March Queues 0/4). No "Boarding closes in"
  banner under the resource bar. The lines under the bar
  were the furnace overdrive line and the breaking-news
  ticker, as in the 1325 and 1813 checks.
- Misfire, grounding failure not a train finding:
  left-column icon tap at norm 54,645 opened the Secret
  Command Post screen (Secret Mobile Squad, Assist Allies
  5/5, Plunder Others 0/3, four SSR task rows). Nothing on
  that screen was tapped, claimed, dispatched or refreshed;
  it was left at once via the bottom-left back arrow at
  norm 132,936, back on the base screen. The visual
  grounding tool labelled the secrets icon as a train icon,
  and its second grounding (locomotive at 48,860) pointed
  at the lower column chest area, which was not tapped. Per
  rule R2 no further blind column-icon taps were made in
  this unit. Note the context dependence: the (52,548) tap
  from the world map returned to the base, while the same
  point from the base in the 0044 and 0348 units panned to
  the station - the point's effect differs by starting view.
- Pivot method: the BASE button at norm 903,967 recentred
  the camera on the own base, showing the base interior
  (buildings, resource tiles, survivors, no station, no
  yellow train, no plus bubble). The left column in this
  view carries hammer 2/4, flask 2/2, weather, chat badge
  2, truck, radar dish, magnifier, hero portrait and chest
  icons, and no visible train-head icon.
- Outcome and qualification, stated plainly: no train in
  preparation found by banner, by BASE-recentred base view,
  or by left-column scan. Nothing boarded, no Trade
  Contracts spent. The station panel itself was NOT opened,
  so this is not a station-verified no-train finding. It
  stands at the same level as the 1325 and 1813
  banner-only checks, strengthened only by the BASE view
  and the column scan. A later same-pass sighting of a
  train in preparation would supersede it, as 0047
  superseded 0044.
- Tracker: marked done for train by this pass, on the
  checked-only basis above, with this qualification in the
  record.

## What the 2026-11-02 0844 unit added - third wrong-icon instance, station empty again

- Unit train-2026-11-02-0630 by ticker-0834, session about
  08:41 to 08:44, status done as checked only. No train in
  preparation. Evidence in
  `_records_/2026-11-02/alliance-train/0844-queue-run.md`.
- Base screen inspected first: no "Boarding closes in"
  banner under the resource bar.
- Wrong-tap recovery, third instance this day after the
  0348 and 0715 units: a tap at norm (53,638) opened the
  Secret Command Post panel (Secret Mobile Squad). No
  Claim, Mega Refresh or Mega Deploy was tapped there -
  secrets are another unit's work. The panel's back arrow
  was re-grounded visually at norm (160,945) after taps
  at norm (65,946) and norm (65,955) hit the small avatar
  circle beside it and produced no change; the corrected
  tap closed the panel back to the base screen.
- Station check: the left-column train icon, measured at
  normalized (52,548) from the 0044 unit's record, panned
  the camera to the base edge. The station area showed no
  yellow train, no plus bubble and no station countdown -
  the same empty state as the 0348 check. The prior
  measured point worked again, corroborating the 0348
  rule: a prior unit's measured point beats a fresh
  guess.
- Nothing boarded, no Trade Contracts spent, no train
  summoned, no conductor role taken.

## What the 2026-11-02 1246 unit added - station empty again

- Unit train-2026-11-02-1030 by ticker-1234, session
  about 12:41 to 12:42, status done as checked only. No
  train in preparation. Evidence in
  `_records_/2026-11-02/alliance-train/1246-queue-run.md`.
- Base screen inspected first: no "Boarding closes in"
  banner under the resource bar.
- Station check: the left-column train icon, measured
  at normalized (52,548) from earlier units, panned the
  camera to the base edge. The station area showed no
  yellow train, no plus bubble and no station countdown
  - the same empty state as the 0348 and 0844 checks.
  The prior measured point worked again.
- Qualification, as with the earlier checked-only
  units: the station panel itself was NOT opened, so
  this is a banner-plus-station-view check, not a
  station-verified no-train finding.
- Nothing boarded, no Trade Contracts spent, no train
  summoned, no conductor role taken.

## What the 2026-11-02 2045 unit added - station check corrected, already aboard carriage 2

- Unit train-2026-11-02-1830 by ticker-2034, session
  about 20:38 to 20:45, status done. The account is
  already aboard carriage 2, the standing-rule
  carriage, so no boarding action was needed and
  none was taken. Evidence in
  `_records_/2026-11-02/alliance-train/2045-queue-run.md`.
- Base screen inspected first: no "Boarding closes
  in" banner under the resource bar.
- Station-check correction, in favour of the newest
  verified record: tapping the left-column train
  icon at normalized (52, 548), the point measured
  by earlier units, panned the camera to a base-edge
  view (4th Squad area) that showed no train, no
  plus bubble and no station countdown. That view
  alone would have concluded no train. Dragging the
  camera toward the station building then revealed a
  yellow train at the base edge, with conductor
  label KpyKat and a countdown near 01:22:57. A
  preparing train was therefore present, and the pan
  point alone is not a sufficient station check; the
  next train unit must drag toward the station
  building and look for the yellow train before
  concluding none is preparing. This qualifies, not
  erases, the 0348, 0844 and 1246 checked-only
  empties, which used the pan view only - their
  no-train readings carry that qualification.
- Tapped the train. A train cinematic played ("Tap
  the screen twice to skip"). Double-tapping to skip
  opened MY PROFILE, consistent with the metadata
  note that tapping the own avatar opens MY PROFILE.
  Closing MY PROFILE with its X revealed the
  STATION PLATFORM screen.
- STATION PLATFORM, read live: departure countdown
  01:21:39 falling to 01:20:07 by the end of the
  unit, Train Rating 86,000, conductor KpyKat.
  Carriage occupancy top to bottom: carriage 1 at
  12/7 with a plus button, carriage 2 at 10/7
  showing the own avatar (the starry landscape
  profile photo, confirmed on zoom), carriage 3 at
  16/7 with a plus button, carriage 4 at 23/7 with a
  plus button.
- No Trade Contracts spent, no train summoned, no
  conductor role taken. The platform back arrow
  returned the view to the base world at the station
  area, train and station building visible,
  countdown 01:20:07.
- Note for the open question below: the platform
  screen opened by the train tap is the station
  verification surface; the station-verified
  no-train read is still owed on a checked-only
  (empty) unit, where no train exists to tap.


## What the 2026-11-02 2320 unit added - entry drift, 2045 pan point no longer pans, filed as Issue #205

- Unit train-2026-11-02-2230 by ticker-2304, session
  about 23:20 to 23:24, status partial. No station
  view was achieved, so no preparing train was
  confirmed and none was ruled out beyond the absent
  banner. No boarding action was taken, no Trade
  Contracts spent, no train summoned, no conductor
  role taken. Tracker untouched, so the next tick
  re-produces this regular. Evidence in
  `_records_/2026-11-02/alliance-train/2320-queue-run.md`.
- Base screen inspected first: no "Boarding closes
  in" banner under the resource bar.
- First entry attempt, wrong icon: a tap at (35,675)
  in the left column opened Secret Command Post
  (Secret Mobile Squad), not the station. Nothing
  inside it was tapped: no task, no Mega Deploy, no
  refresh. Exited by the visually grounded back point
  (158,945) back to the base.
- Second entry attempt, stale point, in favour of
  the newest verified record over the 2045 section:
  the 2045 record's left-column train icon point
  (52,548) produced no camera pan this time; the
  base view was unchanged on screenshot. The 2045
  pan point is therefore NOT a stable entry point -
  it worked at 1246 and 2045 and failed at 2320, so
  the next train unit must re-ground the icon from
  its own base screenshot before tapping, and must
  fall back to the 2045 station-drag route (drag
  toward the station building and look for the
  yellow train) rather than trusting the pan point.
  This qualifies, not erases, the 2045 station-check
  correction: the drag route stands, the pan point
  does not.
- Third entry attempt, mislabelled grounding:
  visual grounding on the base screenshot labelled
  the point (53,576) as the train icon, but tapping
  it opened the truck screen ("Today's Trade Count:
  4/5", "Your Truck" tab, a yellow truck labelled
  [AP3x]KpyKat). Nothing on that screen was tapped:
  no dispatch, no plunder, no tab change beyond the
  view itself. Returned to the base with the back
  tile point (82,930). Lesson: the truck screen is
  not the station, and a grounding label calling a
  left-column point the train icon must be verified
  by the screen it opens before any action is taken
  on that screen.
- Incidental observation, explicitly NOT trucks-unit
  data: the truck screen read "Today's Trade Count:
  4/5" while passing through. It was read outside
  the trucks unit, so the trucks unit must re-read
  its own counter live in its own unit; this figure
  must never be quoted as a trucks-unit closing
  count.
- Gap found, filed as GitHub Issue #205, class
  knowledge, by the executor: re-ground the train
  icon point from a current base screenshot, update
  this entry section, record a station-drag route
  that does not depend on the stale point, and note
  the truck-icon confusion explicitly. This run
  folds the drift evidence and the truck-confusion
  warning into this section; the re-grounding itself
  is still owed by a future train unit, and Issue
  #205 stays open - closure belongs to the daily
  retro, with evidence.

## What the 2026-11-03 0035 unit added - column map measured, no station view

- Unit train-2026-11-02-0847 by ticker-0034, session about
  00:35 to 00:44, status partial. No station view was achieved,
  so no preparing train was confirmed and none was ruled out
  beyond the absent banner. No boarding action was taken, no
  Trade Contracts spent, no train summoned, no conductor role
  taken. Tracker untouched, so the next tick re-produces this
  regular. Evidence in
  `_records_/2026-11-03/alliance-train/0035-queue-run.md`.
- Base screen inspected first: no "Boarding closes in" banner
  under the resource bar.
- Empirical left-column mapping, measured live in this unit,
  the second grounding-label instance after the 2320 unit:
  visual grounding labelled (52,567) as the train icon, but
  tapping it opened the truck screen ("Your Truck" tab).
  Nothing on that screen was tapped: no dispatch, no plunder,
  no tab change. Returned to the base with the back point
  (82,930). Two further probes: (52,626) opened Secret
  Command Post (Secret Mobile Squad), exited with the blue
  back arrow measured fresh at (160,945) - an earlier tap
  at (55,930) missed that arrow and left the screen
  unchanged - and (52,508) opened the temperature panel
  (base temperature 6.5 degrees C, Permafrost Area,
  Alliance Furnace, High-Heat Furnace lines), closed with
  its X at (850,137). No furnace was turned on or off and
  no temperature setting was changed. None of the three
  points is the train entry, and none may be reused as one.
- Hypothesis, unproven, carried for the next unit: the
  train icon may only appear while a train is preparing.
  That would explain both the 2320 no-pan at (52,548)
  and this unit's neighbour hits, since no banner showed
  and no train was confirmed in either unit. The 2045
  pan at (52,548) worked while a train was preparing
  (conductor KpyKat, countdown near 01:22:57).
- Drag route, qualified: dragging the camera from
  (600,600) to (300,300) reached empty snow southwest of
  the base, with no train, no station building and no
  plus bubble. Reversing the drag and a further diagonal
  drag returned the view to the base centre, and a final
  drag from (300,300) to (600,600) produced no view
  change. The 2045 drag route therefore needs the station
  building in view first; a drag from the base centre is
  not a station check, and a base-centre-only view is not
  a completed station check.
- Warning restated: the 2026-11-02 0044 correction stands
  here - a single pan view once missed a preparing train
  that a later camera restore revealed - so this unit's
  no-train read is banner-only, not station-verified.
- Pass-through rule restated: nothing read on the truck
  or Secret Command Post screens in this unit is that
  activity's data; the trucks and secrets units must
  re-read their own counters live in their own units.
- Gap, already filed: the executor commented this mapping
  on GitHub Issue #205, class knowledge. The re-grounding
  itself is still owed by a future train unit, and Issue
  #205 stays open - closure belongs to the daily retro,
  with evidence. Next train unit method, from the record:
  probe the remaining left-column icons one at a time
  from a fresh screenshot, or wait for a "Boarding closes
  in" banner, and do not reuse (52,508), (52,567) or
  (52,626) as the train entry.


## What the 2026-11-03 0315 unit added - (52,548) no-pan repeat, (53,637) Secret Command Post repeat

- Ticker-0304, unit train-2026-11-03-0230, about 03:15
  local, status partial. Tracker untouched: a partial
  unit does not mark the tracker, so the next tick
  re-produces this regular. Evidence in
  `_records_/2026-11-03/alliance-train/0315-queue-run.md`.
- Base screen inspected first: no "Boarding closes in"
  banner under the resource bar.
- Wrong tap, recovered without action: a fresh visual
  grounding put the train icon at (53,637), but tapping
  it opened the Secret Command Post (Secret Mobile
  Squad). Nothing inside it was tapped: no task, no Mega
  Deploy, no Mega Refresh. It was closed with its back
  arrow at (157,946), back to the base. This repeats the
  (53,630) mislabelling already recorded in the
  2026-11-02 0348 unit; grounding must not be trusted
  for this icon.
- Measured tap: (52,548), the point taken from the
  2026-11-02 0044 and 0348 records, was tapped on a fresh
  base screenshot. The camera did not pan: the view
  stayed on the base centre, with no station, no train,
  no plus bubble and no station countdown in view. This
  matches the 2026-11-03 0035 unit, which also got no pan
  from the neighbouring points and closed partial. The
  (52,548) pan successes at 1246 and 2045 now stand
  against failures at 2320 and 0315 plus the 0035
  neighbour misses, so the 2045 pan point is confirmed
  not stable and the 0035 hypothesis gains another
  no-banner instance: the train icon may only appear
  while a train is preparing.
- No station view was achieved in this unit, so no
  preparing train was confirmed and none was ruled out
  beyond the absent banner. No boarding action was
  taken, no Trade Contracts spent, no train summoned, no
  conductor role taken.
- The Secret Command Post screen was only passed
  through; nothing read on it is this unit's data, and
  the secrets unit must re-read its own counters live.
- Gap: already tracked as GitHub Issue #205 (class
  knowledge). The executor commented this repeat onto
  #205, and this run comments the fold (profile version
  and the no-pan count) onto #205 as well; the issue
  stays open, and the re-grounding of the train icon
  point itself is still owed.

## What the 2026-11-03 0752 unit added - third consecutive entry partial, new routes fail, partial

- Ticker-0734, unit train-2026-11-03-0630, about 07:52
  local, status partial. Tracker untouched: a partial
  unit does not mark the tracker, so the next tick
  re-produces this regular. Evidence in
  `_records_/2026-11-03/alliance-train/0752-queue-run.md`.
- Base screen inspected first: no "Boarding closes in"
  banner under the resource bar, on the opening view and
  on every later view in this unit.
- Changed method, failed: under queue rule R2, after the
  0035 and 0315 partials with the same blocker, the
  Accessibility tree was read first instead of trusting
  visual grounding. It carries no icon labels for this
  game - one iOS content group only - so it cannot ground
  the train entry point. This method is retired for this
  activity; do not spend another unit on it.
- New entry route, failed: a tap at (903,750), the
  Alliance icon position on the opening screenshot,
  opened MY PROFILE instead of the Alliance panel.
  Nothing in the profile was tapped. This shows the
  right-side icon positions on a screenshot do not map
  to taps the way the left-column positions were
  assumed to, and the Alliance route is not a working
  train entry from this view. Do not reuse (903,750) as
  an Alliance-panel entry.
- Profile-card confusion, recovered without action: a tap
  meant for empty ground opened another player's profile
  card (PrincessEsra), and a second ground tap opened a
  further player's card (Amarky257). Nothing inside
  either card was tapped - no Like, no Set Off, no share,
  no favourite. A short drag (500,500) to (700,700)
  closed the card and panned the camera. The
  alliance-territory map is dense with player bases, so
  ground taps are not a safe way to close cards or to
  probe for the station.
- Final view after the drag: alliance territory, no
  "Boarding closes in" banner, no station building, no
  train, no plus bubble, no station countdown in view.
  The left column on this view shows temperature, the
  Secret Command Post badge (4), trucks, search (11),
  the plus and radar - no train icon. This matches the
  standing hypothesis that the train icon appears only
  while a train is preparing, but the station itself was
  not viewed, so a preparing train is neither confirmed
  nor ruled out beyond the absent banner.
- No boarding action was taken, no Trade Contracts spent,
  no train summoned, no conductor role taken, no furnace
  change, no assembly. The player profile cards were only
  passed through; nothing read on them is this unit's
  data, and nothing read on them is counted for any other
  regular.
- Rule R2 third partial: this is the third consecutive
  train partial with the same entry-point blocker (0035,
  0315, this unit). The blocker is recorded here in the
  activity metadata, as the record directs.
- Gap: already tracked as GitHub Issue #205 (class
  knowledge). The executor commented this repeat onto
  #205, and this run comments the fold onto #205 as
  well; the issue stays open, and the re-grounding of
  the train icon point itself is still owed.

## Open questions

- What the 3 Trade Contract ticket improves over the free Like
  and Thank (seat, reward share, rating) - the dialog takes a
  quantity (observed 2026-10-26), but the benefit of the paid
  ticket is still unobserved.
- How the reward split among riders works - the claimed set matched
  the carriage 1 card in kind, so a rider appears to receive the
  carriage set as displayed, but whether occupancy dilutes it is
  unobserved.
- What the Train Rating means and what sets it. The arrival mail
  showed a figure of 116,361,444 under the train icon on the
  account card, distinct from base power - possibly the summed
  rider power the rating derives from, unverified.
- Whether a member can board more than one train per day.
- Whether the station icon (52,548) and the trucks trade-entry icon [52,552] are the same column slot - the 0348 station pan and the 0416 trade open differ, unresolved (2026-11-02 0348 unit). (2026-11-02 1325 update: the trucks unit grounded the trade entry at (52,553), 5 pixels from this point, and the 1246 station pan at (52,548) worked again - the near-coincidence now has three instances, but the tap outcomes still differ by context, so the identity stays unresolved.) (2026-11-02 2320 update: the (52,548) tap produced no pan at all, so entry instability now outranks the identity question - re-ground the icon fresh each unit and use the station-drag route; see Issue #205.) (2026-11-03 0035 update: the neighbours are now measured - (52,508) temperature, (52,567) trucks, (52,626) Secret Command Post - so the train entry is none of the three probed neighbours; the 0035 unit's hypothesis is that the train icon only appears while a train is preparing, which would explain both the 2320 no-pan and these neighbour hits. The re-grounding owed by Issue #205 is still owed. (2026-11-03 0315 update: (52,548) again produced no pan on a fresh base screenshot with no boarding banner, and fresh grounding at (53,637) again opened Secret Command Post, repeating the 0348 (53,630) mislabelling.) (2026-11-03 0752 update: third consecutive partial with the same blocker; the Accessibility tree carries no icon labels and cannot ground the entry, (903,750) opens MY PROFILE not the Alliance panel, and ground taps on the alliance-territory map open player profile cards instead of probing the station; the final left column shows temperature, Secret Command Post badge (4), trucks, search (11), plus and radar with no train icon, consistent with the icon-only-while-preparing hypothesis. The re-grounding owed by Issue #205 is still owed.) (2026-11-08 0512 update: the bus icon at grounded norm (49,575) is tap-verified Trucks a third time and the white truck icon at (50,641) is the Secret Command Post entry, so neither is the train icon; the icon-only-while-preparing hypothesis stands and the (52,548) vs (52,552) identity question is superseded by the measured neighbours. See the 0440 and 0512 sections below.)
- Station-panel verification owed: the 0715 check never opened the station panel, so a station-verified no-train read is still owed on a checked-only unit; banner plus BASE view plus column scan is a strengthened banner-only check, not a station verification. (2026-11-03 0035 note: a drag from the base centre, (600,600) to (300,300), reached empty snow southwest of the base with no station building in view, so a base-centre drag is not a station check either - the 2045 drag route needs the station building in view first.)


## What the 2026-11-03 1124 unit added - fourth same-blocker partial today, banner absent, station not viewed

- Ticker-1104, unit train-2026-11-03-1030, about
  11:18 to 11:19 local, status partial. Evidence in
  `_records_/2026-11-03/alliance-train/1124-queue-run.md`.
- Base screen inspected on entry: no Boarding closes
  in banner under the resource bar, and the left icon
  column (temperature, Secret Command Post badge 1,
  trucks, search 11, plus, radar) shows no train icon.
  This is the same blocker as the 0035, 0315 and 0752
  units today - the fourth consecutive same-blocker
  partial of the day.
- No boarding action was taken, no Trade Contracts
  spent, no train summoned, no conductor role
  touched. The station itself was not viewed, so a
  preparing train is neither confirmed nor ruled out
  beyond the absent banner - the same honest caveat
  as the 0752 unit, which already tried the changed
  method (the Alliance route) and found it does not
  open the station from this view. No ground taps
  were used to probe for the station (the 0752 unit
  showed ground taps open other players profile cards
  on this map).
- Tracker untouched, per the rule for partial units;
  the next tick re-produces train and resumes the
  check. The re-grounding owed by Issue 205 is still
  owed. No earlier claim superseded.

## What the 2026-11-03 1742 unit added - fifth check-only outcome today, banner absent, station not viewed

- Ticker-1734, unit train-2026-11-03-1430, about
  17:41 to 17:42 local, status partial. Evidence in
  `_records_/2026-11-03/alliance-train/1742-queue-run.md`.
- Left the Mail category list with its back arrow at
  grounded (62,952) and inspected the live base view.
  No "Boarding closes in" banner under the resource
  bar, and the left icon column (temperature, Secret
  Command Post badge 1, trucks, radar, hammer) shows
  no train icon. This is the same state as the 0035,
  0315, 0752 and 1124 train units today, the fifth
  such check-only outcome of the day.
- No boarding action was taken, no Trade Contracts
  spent, no train summoned, no conductor role
  touched. The station itself was not viewed, so a
  preparing train is neither confirmed nor ruled out
  beyond the absent banner - the same honest caveat
  as the earlier units today. Ground taps were not
  used to probe for the station, per the 0752 lesson
  that they open other players' profile cards on this
  map.
- No new Issue was filed for this repetition: the
  blocker is a missing boarding window (trains run
  1 regular plus 2 Mega Express per day with short
  windows), not a tap-method failure, so rule R2's
  method-escalation ladder does not apply; the
  repetition is named here and in the pass note for
  the retro instead. Tracker untouched, per the rule
  for partial units; the next tick re-produces train
  and resumes the check. Game left on the base view.
  No earlier claim superseded.

## What the 2026-11-03 1345 scout unit added - station panel is a preparation-only surface, LOOT located (scout read, not a train execution)

- Scout unit scout-midday-scout-mid-2026-10-31-006 by
  ticker-1334, about 13:36 to 13:44 local, observe-only.
  Evidence in
  `_records_/2026-11-03/perception-scout/1345-queue-run.md`,
  folded in full into perception-scout. This section
  carries only the train-relevant findings; claiming
  the LOOT rows belongs to the gifts regular, not to
  this activity.
- Station panel, preparation-only surface: the unit
  closed the panels to a clean base view,
  screenshot-read the left icon column, and checked
  the two train-preparation signals before any pan -
  no train icon in the left column, no "Boarding
  closes in" banner under the resource bar. With
  neither signal present, no train is preparing in
  this window, so the STATION PLATFORM screen has no
  live state to read. The platform screen itself
  remains unlocated, and it is a preparation-only
  surface, not a standing panel: it can only be read
  when a train is preparing. Successor scout unit
  scout-midday-scout-mid-2026-10-31-007 carries the
  station panel only, to be re-checked when a train is
  preparing; the successor should re-check the two
  preparation signals first rather than re-panning the
  base edge.
- LOOT box, located on the world map (cross-ref, not a
  train claim): on the world map centred on the own
  base with March Queues 0/4, one east drag pan, then
  a grounded tap on the left-edge gift icon at
  [311,237] opened the panel titled LOOT, with three
  Lv.60 Doom Elite Member rows unclaimed (Claim All
  observed only, never tapped). The world-map gift
  badge was 3 at entry, matching the three rows. The
  gifts units queued for 14:30 should claim them, or a
  diff should raise them if the gifts regular does not
  cover LOOT.

## What the 2026-11-04 0217 unit added - sixth check-only outcome in a row, station still not viewed

- Unit train-2026-11-03-2230 by ticker-0204,
  about 02:16 to 02:17 local, status partial. No
  "active on a different device" dialog appeared.
- Inspected the live base view. No "Boarding
  closes in" banner under the resource bar, and
  the left icon column (temperature, trucks, radar
  with a red dot, hammer) shows no train icon.
  This is the same state as the 0035, 0315, 0752,
  1124 and 1742 train units of 2026-11-03, the
  sixth such check-only outcome in a row.
- No boarding action was taken, no Trade
  Contracts spent, no train summoned, no
  conductor role touched. The station itself was
  not viewed, so a preparing train is neither
  confirmed nor ruled out beyond the absent
  banner - the same honest caveat as the earlier
  units. Ground taps were not used to probe for
  the station, per the 0752 lesson that they open
  other players' profile cards on this map.
- No new Issue was filed for this repetition: the
  blocker is a missing boarding window (trains run
  1 regular plus 2 Mega Express per day with short
  windows), not a tap-method failure, so rule R2's
  method-escalation ladder does not apply; the
  repetition is named here and in the pass note
  for the retro instead.
- Tracker untouched, per the rule for partial
  units; the next tick re-produces train and
  resumes the check. Game left on the base view.

## What the 2026-11-04 0509 unit added - seventh check-only outcome in a row, grounding mislabel opens truck screen

- Unit train-2026-11-04-0230 by ticker-0504, about 05:05 to 05:09 local, status partial. No "active on a different device" dialog appeared. Evidence in `_records_/2026-11-04/alliance-train/0509-queue-run.md`.
- Inspected the live base view. No "Boarding closes in" banner under the resource bar, and the left icon column shows no train icon. This is the same state as the 0217 train unit today and the six check-only units of 2026-11-03, the seventh such check-only outcome in a row.
- One wrong tap, recovered without action: a visual grounding put a train icon at (55, 563), but tapping it opened the truck screen instead. Nothing inside it was tapped - no dispatch, no plunder, no Mega Mode - and it was closed with its back arrow back to the base view. Nothing read on the truck screen is this unit's data, and the trucks unit must re-read its own counters live. This repeats the standing lesson that visual grounding must not be trusted for the left-column icons, and is further evidence for Issue #205 (left-column mapping and the train icon appearing only while a train is preparing); the ticker already commented this unit onto #205.
- No boarding action was taken, no Trade Contracts spent, no train summoned, no conductor role touched. The station itself was not viewed, so a preparing train is neither confirmed nor ruled out beyond the absent banner - the same honest caveat as the earlier units. No further ground taps were used to probe for the station, per the 0752 lesson that they open other players' profile cards on this map.
- No new Issue was filed for this repetition: the blocker is a missing boarding window (trains run 1 regular plus 2 Mega Express per day with short windows), not a tap-method failure, so rule R2's method-escalation ladder does not apply; the repetition is named here and in the pass note for the retro instead.
- Tracker untouched, per the rule for partial units; the next tick re-produces train and resumes the check. Game left on the base view.

## What the 2026-11-04 0839 unit added - eighth check-only outcome in a row, station still not viewed

- Unit train-2026-11-04-0630 by ticker-0834, about 08:39 local, status partial. Evidence in `_records_/2026-11-04/alliance-train/0839-queue-run.md`. No different-device dialog appeared.
- Inspected the live base view. No "Boarding closes in" banner under the resource bar, and the left icon column (hammer 2/4, trucks, radar with a red dot, phone with a red dot) shows no train icon. This is the same state as the 0217 and 0509 train units today and the check-only units of 2026-11-03, the eighth such check-only outcome in a row.
- No boarding action was taken, no Trade Contracts spent, no train summoned, no conductor role touched. The station itself was not viewed, so a preparing train is neither confirmed nor ruled out beyond the absent banner - the same honest caveat as the earlier units. Ground taps were not used to probe for the station, per the 0752 lesson that they open other players' profile cards on this map, and the 0509 lesson that the left-column icon at (55, 563) opens the truck screen, not the train.
- No new Issue was filed for this repetition, for the same reason as the 0509 section: the blocker is a missing boarding window (trains run 1 regular plus 2 Mega Express per day with short windows), not a tap-method failure, so rule R2's method-escalation ladder does not apply; the repetition is named here and in the pass note for the retro instead.
- Tracker untouched, per the rule for partial units; the next tick re-produces train and resumes the check. Game left on the base view.

## What the 2026-11-04 1404 unit added - screen-capture failure, fourth consecutive pass, fault narrowed to the game window

- Unit train-2026-11-04-1030 by ticker-1404, about 14:04 to 14:10 local, status failed (the record frontmatter says unverified while its Outcome section says failed - the body outcome is followed). Evidence in `_records_/2026-11-04/alliance-train/1404-queue-run.md`. No different-device dialog appeared.
- No game screen was ever read and no game input was dispatched. computer.control activate selected the LastWar window for background input but reported it not on screen and captured no observation ("Failed to start stream due to audio/video capture failure"); computer.observe (compact) failed with the same error twice across two computer sessions (cc-460, then cc-461); computer.control describe on the LastWar window failed with the same error. computer.control open_app returned outcome_unknown; a re-list showed LastWar still running under the same pid (59735), so no restart or duplicate launch happened and the launch was not repeated.
- Narrowing, the point of this fold: control observation of the Google Chrome window succeeded in the same session (the Gmail inbox tree was read), so the control channel itself works and the failure is specific to the Last War fullscreen window, not a whole-device outage. This qualifies the Issue #282 framing ("device-channel fault"): the fault is the capture stream for the game window, not a device-wide capture outage. The qualification is commented on #282 by this run; the tooling tracker is Issue #284, where the ticker pass already commented this unit's evidence, so no duplicate issue is filed here.
- Recurrence: this is the fourth consecutive ticker pass to fail on this exact blocker (ticker-1224 help 1235, ticker-1327 mail 1333, ticker-1340 star-ceremony 1344, ticker-1404 train 1404), now across four activities. Until the Mac screen-recording stream recovers for the game window, further ticker passes will fail their first unit the same way.
- No blind taps were dispatched, under the check-first rule. No train boarding check was performed, no seat taken, no Trade Contracts spent, no train summoned. Unlike the eight check-only units above, this unit is NOT a check-only outcome: the station was not even attempted, because no observation existed to check from - so it gives zero evidence about whether a train is preparing, and it does not extend the check-only streak count (which stays at eight).
- Tracker untouched, per the failed-unit rule; the next tick re-produces the train unit. The inbox held 65 units at this pass. The unit file sits in `_queue_/done/` with result status failed - the unit file's lifecycle state after execution, not a tracker marking; the regular remains due.

## What the 2026-11-07 1826 unit added - ninth check-only outcome in a row, banner absent, station not viewed

- Unit train-2026-11-07-1430 by ticker-1818, about 18:21 to 18:26 local, status partial (check-only). Evidence in `_records_/2026-11-07/alliance-train/1826-queue-run.md` (commit f04c2b11d on records/2026-11-07). Computer session cc-30, LastWar already running on the Mac mini, base screen live.
- No "Boarding closes in" banner under the resource bar, and the left icon column (hammer 2/4, flask 2/2, blue truck icon, survivor "?" bubble, truck with a red dot, satellite, wrench) shows no train icon. This is the same state as the check-only train units of 2026-11-03 and 2026-11-04.
- No boarding action was taken, no Trade Contracts spent, no train summoned, no conductor role touched. The station itself was not viewed, so a preparing train is neither confirmed nor ruled out beyond the absent banner - the same honest caveat as the earlier units.
- Ground taps were not used to probe for the station, per the 2026-11-04 lesson that they open other players' profile cards on this map, and the 0509 lesson that the left-column icon at (55, 563) opens the truck screen, not the train.
- Recurrence: this is the ninth check-only outcome in a row (the 1404 failure does not extend the streak, per its section). No other task type was executed in this unit. No login or verification was demanded, and no different-device dialog appeared.
- Figures read live: power 149,850,353; food 476.8M, iron 800.4M, coin 5.7M. No diamonds, money, speedups or paid buttons were used.
- Tracker untouched; the next tick re-produces the train unit.

## What the 2026-11-07 2140 and 2153 scout units added - station panel re-checked, no train preparing, third confirmation in one pass

- Scout units scout-midday-scout-mid-2026-10-31-007 (ticker-2134, session cc-51, about 21:37 to 21:40 local) and scout-midday-scout-mid-2026-11-02-006 (ticker-2134, session cc-54, about 21:48 to 21:53 local), both status partial. Evidence in `_records_/2026-11-07/perception-scout/2140-queue-run.md` and `_records_/2026-11-07/perception-scout/2153-queue-run.md` (commit fe5a1e7fd3 on records/2026-11-07). Observe-only; no boarding action, no Trade Contracts spent, no train summoned.
- Preparation signals, both absent in both units: no train icon in the left icon column (avatar Lv.30, hammer 2/4, flask 2/2, green face 6.5C, white truck, radar, wrench) and no Boarding closes in banner under the resource bar. No train is preparing in this window, so the STATION PLATFORM screen has no live state to read. This is the third independent confirmation of this state inside the ticker-2134 pass (the 2145 base-group unit also read no signals), and the third consecutive partial of the scout-mid-2026-10-31 chain on the same blocker (units 005, 006, 007).
- Entry route, as changed by the 2140 pass under design rule R2: check the two preparation signals first on a clean base view; if neither is present, close the unit partial without panning the base edge, and re-check only when a train is preparing. The 2140 unit followed the changed route (no pan made). The substance of this rule is already in this profile since the 1345 section (station panel is a preparation-only surface, check signals first) - the 2140 pass's working-tree metadata change (1.5.0 to 1.6.0 on a stale base) carried no new rule text, so nothing is reworded here; only the confirmation count is added. Do not treat the unlocated platform as a missing panel.
- Building countdown read 03:38 at 21:39, 03:42 at 21:44, 03:48 at 21:49 - RISING across the three reads; the count direction is recorded as observed, not interpreted. The building's identity and what the timer counts are unknown items, carried in perception-scout 1.27.0. It is not a train signal.
- Streak note: the 1826 train unit was the ninth check-only outcome in a row for train units. These two scout re-checks are not train-unit outcomes and do not extend that streak count - they are recorded here as scout confirmations, not train checks. Successor scout units are enqueued under both chains for the remaining groups. Game left on the own base screen.

## What the 2026-11-07 2311 and 2317 scout units added - station panel re-checked, no train preparing, fifth confirmation in one pass; Train Conductor appointments in the logs

- Scout units scout-midday-scout-mid-2026-11-02-006 (ticker-2304, about 23:05 to 23:15 local) and scout-midday-scout-mid-2026-10-31-008 (ticker-2304, about 23:16 to 23:17 local), both status partial. Evidence in `_records_/2026-11-07/perception-scout/2311-queue-run.md` and `_records_/2026-11-07/perception-scout/2317-queue-run.md` (commit 03dc69e0c on records/2026-11-07). Observe-only; no boarding action, no Trade Contracts spent, no train summoned.
- Preparation signals, both absent in both units: no train icon in the left icon column (avatar Lv.30, hammer 2/4, flask 2/2, green face 6.5C, white truck, radar, wrench) and no Boarding closes in banner under the resource bar. No train is preparing in this window, so the STATION PLATFORM screen has no live state to read. This is the fifth independent confirmation of this state inside the ticker-2304 pass (units 2140, 2145, 2153, 2311, 2317) and the 2317 unit closed partial without panning, per the check-signals-first entry route. March Queues 0/4 on the world map at 23:12.
- Train Conductor appointments, read live in the Record Event tab (a new read source for the conductor role): Texan Apex appointed Roronoa zo as the Train Conductor, 2026-11-8 00:05:53; Nd45pd4 appointed LAMP 1 as the Train Conductor, 2026-11-7 00:05:12. The conductor is an officer-appointed role; no member action follows from the appointment alone.
- Streak note: the 1826 train unit was the ninth check-only outcome in a row for train units. These two scout re-checks are not train-unit outcomes and do not extend that streak count - they are recorded here as scout confirmations, not train checks. Successor scout unit 007 is enqueued under chain scout-2026-11-02 for the remaining alliance surfaces. Game left on the own base screen.

## What the 2026-11-08 0022 scout unit added - station panel re-checked, no train preparing, fourth consecutive confirmation

- Scout unit scout-midday-scout-mid-2026-11-04-002 by ticker-0004, about 00:13 to 00:22 local, status partial (midday remainder). Evidence in `_records_/2026-11-08/perception-scout/0022-queue-run.md` (commit e6192726d1 on records/2026-11-08). Observe-only; no boarding action, no Trade Contracts spent, no train summoned.
- Preparation signals, both absent: no train icon in the left icon column (avatar Lv.30, hammer 2/4, flask 2/2, green face 6.5C, white truck, radar, wrench) and no Boarding closes in banner under the resource bar. No train is preparing in this window, so the STATION PLATFORM screen has no live state to read. This is the fourth consecutive confirmation of this state in the record's frame (units 005, 006, 007 of chain scout-mid-2026-10-31, and this unit); the 2311/2317 section counts five confirmations inside the ticker-2304 pass under a different frame, so the two counts are not directly comparable. The check stopped at the signals per the R2-hardened entry route (alliance-train metadata 1.6.0): no pan of the base edge, no station platform visit.
- Streak note: the 1826 train unit was the ninth check-only outcome in a row for train units. This scout re-check is not a train-unit outcome and does not extend that streak count - it is recorded here as a scout confirmation, not a train check. Successor scout unit seq 003 is enqueued under chain scout-mid-2026-11-04 for the remaining store tabs. Game left on the own base screen.

## What the 2026-11-08 0118 scout unit added - station panel re-checked, no train preparing, sixth confirmation in the scout-mid-2026-10-31 chain

- Scout unit scout-midday-scout-mid-2026-10-31-008 by ticker-0104, about 01:08 to 01:12 local, status partial (alliance remainder station check). Evidence in `_records_/2026-11-08/perception-scout/0118-queue-run.md` (commit 33bb20050a on records/2026-11-08) and the appended section of `_records_/2026-11-08/perception-scout/observation.md`. Observe-only; nothing claimed, fought, dispatched, donated, dug or bought.
- Preparation signals, both absent: no train icon in the left icon column (hammer 2/4 with a red dot, flask 2/2, weather face 6.5C, radio with a red dot, truck with a red dot, radar dish, hammer) and no "Boarding closes in" banner under the resource bar. No train is preparing in this window. The unit closed partial without panning, per its window instruction.
- Count note: this is the sixth no-train confirmation in this chain's station-panel checks (after 1345, the 2140/2153 third and the 2311/2317 fifth). The 0022 re-check's "fourth consecutive confirmation" counts a different chain (scout-mid-2026-11-04: units 005, 006, 007 of scout-mid-2026-10-31 plus itself), so the two counts are not directly comparable - no reconciliation is claimed. The station panel is a preparation-only surface: it has no live state to read while no train is preparing.
- Streak note: the 1826 train unit was the ninth check-only outcome in a row for train units. This scout re-check is not a train-unit outcome and does not extend that streak count - it is recorded here as a scout confirmation, not a train check. Successor scout unit seq 009 is enqueued under chain scout-mid-2026-10-31 for the station panel re-check. Game left on the base screen.


## What the 2026-11-08 0440 scout unit added - station panel re-checked, no train preparing, seventh confirmation in the chain

- Scout unit scout-midday-scout-mid-2026-10-31-009 by ticker-0434, about
  04:36-04:44 local, status partial per the unit window instruction.
  Evidence in `_records_/2026-11-08/perception-scout/0440-queue-run.md`
  (commit caa661bab on records/2026-11-08). Observe-only; nothing
  claimed, fought, dispatched, donated, boarded or bought.
- Preparation signals, both absent: no separate train icon in the left
  icon column, and no "Boarding closes in" banner under the resource
  bar. No train is preparing in this window. The unit closed partial
  without panning, per its window instruction and the R2-hardened
  entry route (alliance-train metadata 1.6.0).
- Count note: this is the seventh no-train confirmation in the
  scout-mid-2026-10-31 chain's station-panel checks (seq 009), after
  1345, the 2140/2153 third, the 2311/2317 fifth and the 0118 sixth.
  The station panel is a preparation-only surface: it has no live
  state to read while no train is preparing.
- Icon identity: the 0440 record's blue vehicle icon disagreement
  (Trucks per the 0404 tap read, radar per the 0022 read) is settled
  by the 0512 unit in favour of Trucks - the 0022 "radar" read is
  superseded. The train icon is state-dependent: it appears in the
  column only while a train is preparing, consistent with the 0035
  hypothesis in the open questions below.
- Train Conductor appointments from the 0447 logs: Texan Apex
  appointed Roronoa zo as the Train Conductor, 2026-11-8 00:05:53;
  Nd45pd4 appointed LAMP 1 as the Train Conductor, 2026-11-7
  00:05:12.
- No successor unit is enqueued from this unit: the station re-check
  recurs with the current reset day's scout pass, whose head
  scout-midday-2026-11-08-0700 is already in inbox. Chain
  scout-mid-2026-10-31 is spent with this unit.
- Game left on the base screen.

## What the 2026-11-08 2211 unit added - checked only, no train preparing, banner-only signals check

- Unit train-2026-11-08-1830 by ticker-2201, about 22:09 to 22:11 local, status partial (checked only). Evidence in `_records_/2026-11-08/alliance-train/2211-queue-run.md` (commit 8960535c on records/2026-11-08).
- Returned to a clean base view and checked the two preparation signals from the activity metadata: no train icon in the left icon column (chat, truck, radar, hammer only) and no "Boarding closes in" banner under the resource bar.
- No train is in preparation. Per the activity metadata the unit closes partial without panning to the station, and the train is re-checked only when a train is preparing. No boarding, no conductor action, no spending.
- Note: this is a banner-only signals check, not a station-panel verification - the unit did not pan to the station. It does not advance the scout-chain station-panel no-train count (seventh confirmation at the 0440 scout unit). The next train unit re-checks the two signals first.
- Result stats: target 1, achieved 0, resources_gained none, costs 2m_wall_no_stamina, verified yes, blocker_category h, train_preparing false, device_takeovers 0.

## What the 2026-11-09 0215 unit added - checked only, no train preparing, banner-only signals check

- Unit train-2026-11-08-2230 by ticker-0204, 02:12:29 to 02:13:06 local (37 seconds; the 0215 file heading is the estimate at writing time), status partial (checked only). Evidence in `_records_/2026-11-09/alliance-train/0215-queue-run.md` (commit facef628c on records/2026-11-09). Computer session cc-209, same session as the gifts unit of this pass. The game was on the base screen; no different-device dialog appeared.
- Preparation signals, both absent: base screen read live, total power 149,209,253. No train icon in the left icon column (chat with red dot, truck, radar, hammer only). No "Boarding closes in" banner under the resource bar. No train is in preparation.
- What was not done: no station panel was opened and no carriage state was read; this is a banner-only signals check, not a station-panel verification, as in the 2211 unit. It does not advance the scout-chain station-panel no-train count. A further same-day no-train signal, not counted in the chain. No boarding, no conductor action, no spending.
- Result stats: target 1, achieved 0, resources_gained none, costs 37 seconds, no items spent, verified yes, blocker_category h, train_preparing false, device_takeovers 0.
