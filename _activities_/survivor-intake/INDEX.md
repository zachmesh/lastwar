---
title: Survivor Intake
created: 2026-10-25T21:55:00Z
modified: 2026-11-05T10:38:30Z
version: 1.29.0
description: Collecting the survivors who queue at the base front gate - recruit cards, dialog survivors and their building posts
grounded_in:
  - source: task named by the owner on 2026-10-25 - the line at the front door
  - source: in-game screens observed on the owner Mac mini, 2026-10-25
  - source: in-game screens observed on the owner Mac mini, 2026-11-01 (1017 survivors diagnostic unit)
  - source: in-game screens observed on the owner Mac mini, 2026-11-01 (1159 survivors unit)
  - source: in-game screens observed on the owner Mac mini, 2026-11-01 (1644 survivors unit)
  - source: survivor-intake execution record 2026-11-01 2048 queue run (ticker-2034 unit, partial, gate line unverified)
  - source: survivor-intake execution record 2026-11-02 0016 queue run (ticker-0004 unit, partial, gate line unverified)
  - source: survivor-intake execution record 2026-11-02 0320 queue run (ticker-0308 unit, partial, gate line unverified, Issue #168)
  - source: survivor-intake execution record 2026-11-02 0747 queue run (ticker-0734 unit, partial, gate line unverified, Polar Guest dialog)
  - source: survivor-intake execution record 2026-11-02 1107 queue run (ticker-1104 unit, partial, gate line unverified, drag-pan retired)
  - source: survivor-intake execution record 2026-11-02 1640 queue run (ticker-1631 recovery unit, partial, gate point no-change, recovery-written)
  - source: survivor-intake execution record 2026-11-02 1718 queue run (ticker-1703 unit, partial, 89,722 radar-entry correction)
  - source: survivor-intake execution record 2026-11-02 1948 queue run (ticker-1934 unit, partial, figure taps select squad vehicle)
  - source: survivor intake execution record 2026-11-02 2252 queue run
  - source: ticker-0234 survivor-intake execution record 2026-11-03 0247 queue run (partial, bubble change not intake proof, re-ground before every tap)
  - source: ticker-0634 survivor-intake execution record 2026-11-03 0644 queue run (partial, gate line unverified, two grounding points rejected)
  - source: ticker-1034 survivor-intake execution record 2026-11-03 1050 queue run (partial, gate line not found, grounding timed out twice, no tap on unidentified markers)
  - source: survivor-intake execution record 2026-11-03 1543 queue run (ticker-1534 unit, partial, gate-cluster grounding, no verified recruit)
  - source: ticker-2104 survivor-intake execution record 2026-11-03 2112 queue run (partial, gate line unverified, thirteenth distinct partial since the 1644 done)
  - source: ticker-0104 survivor-intake execution record 2026-11-04 0110 queue run (partial, contested, different-device dialog after two kick takeovers, server maintenance at entry)
  - source: ticker-0404 survivor-intake execution record 2026-11-04 0416 queue run (partial, gate still not located, tent/parking-area re-read named)
  - source: ticker-0734 survivor-intake execution record 2026-11-04 0757 queue run (partial unverified, gate sign never pinned, grounding candidates untapped, center-view re-read named)
  - source: ticker-1104 survivor-intake execution record 2026-11-04 1122 queue run (partial, gate line verified live with 3 question-mark survivors, fullscreen method change, figure tap dispatched but no card opened)
  - source: ticker-1704 survivor-intake execution record 2026-11-04 1707 queue run (failed, Mac screen-capture failure on every attempt, no game screen read, no input dispatched, tenth consecutive ticker pass to fail this way, Issue 284)
  - source: ticker-2134 survivor-intake execution record 2026-11-04 2135 queue run (failed, Mac screen-capture failure on every attempt, no game screen read, no input dispatched, next ticker pass after 2104 known to fail identically, Issue 284)
  - source: ticker-0134 survivor-intake execution record 2026-11-05 0134 queue run (failed, Mac screen-capture failure on every attempt, no game screen read, no input dispatched, twenty-sixth consecutive ticker pass to fail this way, new diagnosis - windowed on an inactive Space, not fullscreen, Issue 284)
---


# Survivor intake

## What this activity is

Survivors arrive at the base and wait in a line at the front gate.
Each one has to be taken in by hand. This folder accumulates intake
knowledge - how the line works, what the recruits bring, and where
they end up working. The owner named this as task 9 on 2026-10-25.
Executions are recorded in `_records_/<date>/survivor-intake/`, one file per execution.

## How to enter

Measured on 2026-10-25.

- On the base screen, find the front gate - the walled entrance on
  the right side of the base, signed Zombies. The waiting survivors
  stand in a line in front of it, each with a question mark bubble.
- Tap a survivor figure to open their card or dialog. Tapping the
  bubble alone can miss; the figure is the reliable target, and
  visual grounding found them reliably when taps drifted.
- Look-alikes measured 2026-11-01 (0913 unit): a centre-right
  circular icon is a pet icon, not a question-mark bubble -
  grounding had misread it as one - and the left-edge green
  0 degree button is a temperature control, not a smiley
  bubble. An icon read alone never verifies a survivor; the
  figure is the target.
- A bubble with an exclamation mark is a visitor, not a recruit -
  one opened a Friendly Visitor dialog asking to enable
  notifications. Cancel left it untouched; nothing was enabled.

## How a recruit is taken in

- Named survivors open a New Survivor Incoming card showing their
  name, their role, the building they belong to and one trait.
  Press Recruit; the card advances to the next survivor in line.
- Other survivors only speak a line when tapped - one handed over
  supplies ("I found some supplies, hope they're useful to you"),
  another remarked on the extreme weather - and then walk in.
- A processed survivor's bubble turns into a smiley face and they
  walk to their post. The line is clear when no question mark
  bubbles remain at the gate.

## Cadence

- Survivors accumulate while the game is away; a line of about
  eight was waiting at the first check. Work the line every round.

## Scope and availability

- Recruiting is free. No card showed a cost, a cap or a reject
  choice worth using - take everyone in.
- Recruits take building posts with their trait attached. After
  the first intake, the Lv.27 Iron Mine survivor list read Taylor,
  Harry, Samantha and Javier as Miners - Harry had been recruited
  minutes earlier with Boost Iron Output plus 24 percent, and a
  Javier with a Barracks instructor trait appears in the same list
  as a Miner, so assignment looks automatic rather than chosen.
- Quick Dispatch is a standing owner instruction, set on
  2026-10-25 (evening) and reversing the earlier never-press
  caution in this file - whenever new survivors have been taken
  in, always run Quick Dispatch in the building panel afterwards
  so the newcomers are posted, autonomously, without asking the
  owner first. Reading a building panel is fine; the Lv.27 Iron
  Mine reads Output per hour plus 133,128 and Max Production Time
  11 hours 36 minutes.
- Quick Dispatch lives at the bottom of a Building Details panel -
  tap the building, then the paw (details) button, and the panel
  shows output rate, max production time, the posted survivor list
  and the blue Quick Dispatch button. On the evening of 2026-10-25
  the Iron Mine Lv.27 and Farmland Lv.28 panels were opened after
  the second intake; both survivor lists already showed full posts
  with no newcomer waiting, so nothing changed there. The Iron
  Mine output rate read plus 114,551 and later plus 126,936 the
  same evening against plus 133,128 earlier in the day - the rate
  moves with active buffs, so treat single readings as snapshots.

## Recruits measured on 2026-10-25

- A Scientist for the Research Center - Research Speed plus
  16.00 percent. Name not captured.
- ELINA, Keeper, Warehouse - Increase Food Protection plus
  5.00 percent.
- DAVID, Hunter - increases the time armed truck loot can
  accumulate by 1 hour 30 minutes.
- HARRY - Boost Iron Output plus 24.00 percent.
- JAVIER, Instructor, Barracks - Unit Training Cap plus
  3.20 percent.
- DAVID, Attendant, Tavern - Free Hero Recruitment cooldown
  reduced by 3 hours.
- A Mechanic for the Factory - Crafting Speed plus 4.80 percent.
  Recruited in the evening second intake, with one dialog survivor
  taken in alongside. Name not captured. Whether the radar
  Distressed Survivor reward of the same evening is one of these
  two is unconfirmed.

## Standing blocker recorded by the retro of 2026-10-31

- Queue era 2026-10-28 to 2026-10-31 - 22 of 22 survivor units
  closed partial, 0 done. Quick Dispatch did not run in any of
  them. This is a third-strike blocker under queue rule R2, and
  the fourth identical partial is a process failure to be
  reported to the owner, not a result.
- The repeated failure modes are a gate line not found or not
  verified, and control channel stalls. The next unit starts at
  the gate with a fresh grounding, verifies a survivor figure
  before any tap, and closes unverified with a named re-read
  unit if the line cannot be verified, instead of closing on a
  presumed line state.

## What the 2026-11-01 early unit added

- The streak continues past the retro's window: the first
  2026-11-01 survivors unit (0016, ticker-0004) also closed
  partial, gate line never verified, nothing recruited, tracker
  untouched - 23 consecutive queue-era partials on the 0016
  record's own count (22 through 2026-10-31, plus this unit).
- Background input is control-dependent, measured 0016: a
  title-bar click did not bring the game forward (Speedtest
  stayed frontmost) but that was not the blocker - an
  Events-icon tap reached the game in background, while two
  Events back-arrow taps produced no change. Do not read a
  failed bring-to-front as total input blockage. This matches
  the truck profile's standing "not reliably" framing; no
  profile claim is superseded.
- Escape re-confirmed, 0016: an Escape key press quit Last War
  outright (the same crash behaviour already recorded for Esc)
  - recovered by relaunch straight to the base with no login
  or device dialog, HUD unchanged. Never Escape. The relaunch
  reset the camera to a wider winter view; the record's
  proposed next method is a slow manual drag or a scroll
  zoom-out starting from that wider view rather than
  re-entering the zoomed pad view - proposed, not verified.
  The same zoomed central-pad view could not be panned in
  this unit either (one drag, 500,500 to 200,500, no change),
  matching the 2343 harvest unit's three failed drags.

## What the 2026-11-01 0041 unit added

- Duplicate re-run, not a new distinct partial: the 0041 unit
  re-ran unit survivors-2026-10-31-2203, already completed
  partial by ticker-0004 (the 0016 record), because the local
  working tree still carried it in inbox while the records
  branch had it done. The queue-state divergence between the
  working tree and the records branch is an open process item
  for the next queue review, not a game-state change. The
  distinct-unit streak therefore stays at 23 consecutive
  queue-era partials; 0041 must not be counted as a 24th.
- Gate search, four pans, three counted: the opening pan showed
  the central base with production houses carrying resource
  bubbles and no question-mark survivor line; a drag from norm
  400,600 to 650,350 moved the view to the headquarters corner;
  a drag from 623,736 to 389,526 moved it to the outer snow
  field, where enlarged crops of the left edge and the
  top-right road showed turrets, a STOP sign and formation
  vehicles, but no gate line and no question-mark bubbles. A
  fourth drag from 350,350 to 600,600 moved nothing after
  focus was lost again and is not counted as a searched pan.
- Grounding gap: a visual-grounding call for the survivor line
  timed out without a result and was not retried, so every
  conclusion in the 0041 record rests on the screenshots and
  crops read directly, not on grounding output.
- Focus recurrence, same fix: the game was not frontmost at the
  start (UserNotificationCenter was) and background pans did
  not move the view until a title-bar left-segment tap at norm
  274,18, clear of the green zoom button, brought the game
  forward; focus loss recurred later in the pass and was fixed
  the same way. The window stayed in window mode throughout.
- Claim discipline: the unit does not claim the gate is empty,
  only that no waiting line was found in the pans searched; no
  survivor figure was tapped, no recruit card or dialog was
  opened, Quick Dispatch did not run, and the tracker is
  untouched, so the next tick re-produces this regular.

## What the 2026-11-01 0913 unit added

- Distinct-unit streak reaches 24: this unit
  (survivors-2026-11-01-0603, ticker-0904) is the 24th
  consecutive distinct queue-era partial, counting only
  distinct units as the 0041 accounting does - the
  access-failed 0504 unit is a failure, not a partial, and
  does not extend the streak. Gate line never verified,
  nothing recruited, tracker untouched.
- Look-alike corrections, measured in the restored base view
  with enlarged crops: the bottom-left crop shows only the
  STOP road barrier, cannons and a tree, with no
  question-mark bubble and no survivor figure - a tap at
  norm 293,648 near the barrier produced no change on a
  second observation, so that point was not a survivor.
  The centre-right circular icon is a pet icon, which the
  grounding had misread as a question-mark bubble, and the
  left-edge green 0 degree button is a temperature control,
  not a smiley bubble. Neither is a survivor or a bubble to
  tap.
- Claim discipline re-affirmed: the unit does not claim the
  gate is empty, only that no waiting line was found in
  the pans searched; Quick Dispatch was not run, because
  no named recruit was taken in during this unit, and
  running it without an intake would not satisfy the
  standing blocker.



## What the 2026-11-01 1017 diagnostic unit added

- Diagnostic unit survivors-diagnostic-001 (ticker-1004,
  session about 10:05 to 10:17, status partial): the gate was
  not located and Quick Dispatch was not located. This
  diagnostic partial is counted separately from the
  regular-unit streak - the regular streak stays at 24
  distinct partials from the 0913 unit; this is the first
  diagnostic-unit partial under the 2026-10-31 retro
  method-change decision, not a 25th regular partial.
- Verified negative, measured 1017: the Titanium Alloy
  Factory No.1 Lv.30 Building Details panel carries NO
  Quick Dispatch and NO survivor list. Panel read verbatim:
  "TITANIUM ALLOY FACTORY NO.1", "Lv.30", "Power 36,900",
  "Output/hr 21,600", "Max Production Time 1d 00:00:00",
  "Maximum Level Reached", and "This building will
  disappear when the season ends". This refines the
  standing "Quick Dispatch lives at the bottom of a Building
  Details panel" claim: it holds for survivor-post panels
  (Iron Mine, Farmland), not for every panel. The next
  attempt must try a survivor-post building specifically,
  not a seasonal factory.
- Entry path measured fresh in this unit (no coordinate
  copied from an earlier unit): a map drag pan from norm
  600,600 to 300,400, reversed 300,400 to 600,600,
  restoring the original base view, both pans visibly
  shifting the map; a resource house tapped at norm
  144,295 in the panned view selected Titanium Alloy
  Factory No.1 Lv.30; its orange info "i" button at norm
  111,329 opened the panel above; the panel closed with
  the X at norm 900,186 and the base screen returned,
  verified on a second observation. A second selection in
  the original view, centre resource house at norm
  472,448 then central tower at norm 478,438, selected
  High-heat Furnace Lv.30; its flame button at about norm
  459,448 and info "i" button at about norm 524,448 are
  measured points for the next unit only - the furnace
  panel was NOT opened in this unit (unit time cap), so
  those points are not a verified panel.
- Gate line: NOT READ. The signed "Zombies" front gate
  itself was not located, so no gate line can be quoted
  verbatim and the gate is NOT claimed empty. Areas
  inspected: the original base view centre resource row
  (small houses with 286.4K resource bubbles, a helicopter
  vehicle, a green turret building; no question-mark bubble,
  no survivor figure); the bottom-left STOP road barrier
  area (STOP sign, cannons, a tree, a brown circular ground
  mark; no bubble, no figure); the top-left road in an
  enlarged crop (a zombie figure with red splatter and a
  small walking figure near the headquarters; no bubble,
  no survivor line); and the panned view (same resource row
  and snow area; no bubble, no line).
- Session-drop recovery, same pattern as the 0917 training
  unit: one computer session drop mid-unit (cc-4 lost,
  cc-5 restarted, LastWar re-selected, no game state lost).
  Session window signed in as HidingAnt504, HUD power read
  148,957,193 in this unit.
- Side-effect discipline: a tap at norm 472,448 collected a
  resource bubble as a side effect of selecting a building
  (iron read 16.7M before, 18.1M after in the HUD); that
  collection is not claimed as survivor work. No survivor
  was tapped, no recruit card or dialog was opened, no live
  Quick Dispatch was completed, 0 recruited, 0 dispatched.

## What the 2026-11-01 1159 unit added

- Regular-unit partial streak reaches 25: this unit
  (survivors-2026-11-01-1003, ticker-1151) is the 25th
  consecutive distinct regular-unit partial by the 0041
  and 0913 counting rule - the 1017 diagnostic partial
  is counted separately and does not extend the regular
  streak, and the access-failed 0504 unit is a failure,
  not a partial. No survivor was verified, tapped as a
  recruit, or taken in; no Quick Dispatch ran; the
  tracker is untouched, so the next tick re-produces
  this regular.
- Entry path measured fresh in this unit (no coordinate
  copied from an earlier unit): base screen in window
  mode (763 by 1050), HUD power 148,957,193, food
  289.2M, iron 477.2M, coin 10.6M, second-row resource
  18.2M. Centre base view showed the resource-house row
  with ready bubbles, a helicopter vehicle, a green
  turret building and the large gift box; no
  question-mark bubble and no survivor figure verified
  in this view.
- Opposite-direction pan, a changed method versus the
  1017 diagnostic (which panned base-to-top-left): a
  drag from norm 300,400 to norm 650,650 shifted the view
  only slightly (about 3 percent changed area) and
  returned essentially the same centre base view. The
  bottom-right outside the wall now showed a small
  walking figure near a bare tree, with no question-mark
  bubble visible over it. One fresh tap probe on that
  newly revealed figure, at norm 620,670, produced no
  change - no card or dialog opened. Per rule R2 the
  method ends there for this unit; the same point was
  not tapped again.
- Gate line: NOT READ. The signed "Zombies" front gate
  itself was not located in this unit, so no gate line
  can be quoted verbatim and the gate is NOT claimed
  empty. Claim discipline holds: the unit claims only
  that no waiting line was found in the pans searched.
- Next-unit instruction, from the record itself, with a
  process warning attached: the next survivors unit must
  change the entry route again before repeating this work
  (rule R2) - the concrete untried variant is a zoom-out
  to read the full base perimeter and locate the signed
  gate first, rather than another centre-view pan or
  single-figure tap. A further identical partial is a
  process failure to be reported to the owner, not a
  result. Quick Dispatch is recorded as not located in
  this unit, never inferred from the older metadata
  description.

## What the 2026-11-01 1644 unit added

- Regular-unit partial streak BROKEN at 25: this unit
  (survivors-2026-11-01-1403, ticker-1638, session about
  16:38 to 16:44) closed done - the first done survivors
  unit of the queue era after 25 consecutive distinct
  regular-unit partials (0016 through 1159, counted per
  the 0041 rule). The standing blocker section's 22-of-22
  retro count and the 25-streak count are now history,
  not the current state; the next unit starts from a
  done, not from a streak.
- Entry path measured fresh in this unit, in the 642 by
  951 window: base screen read live food 341.3M, iron
  528.8M, coin 17.6M, diamonds 2,396. Fresh visual
  grounding located the gate survivor at the bottom
  centre of the base - question-mark bubble at norm
  460,632, survivor figure at norm 458,678, in front of
  the signed gate. The gate reads bottom-centre in this
  window framing; the 2026-10-25 "right side of the
  base" description is a different framing, not a
  contradiction to overwrite.
- Figure tap, not bubble tap: one tap on the figure at
  norm 458,678 (after an initial stale-observation retry
  that sent nothing) turned the question-mark bubble
  into a smiley bubble at the gate, and a second
  screenshot showed no question-mark bubble anywhere at
  the gate and the processed survivor already walked in.
  Gate line clear by the activity standard. This
  confirms the profile's figure-is-the-reliable-target
  rule and the smiley-means-processed rule with a live
  done.
- Dialog-type survivor, no post, no Quick Dispatch gap:
  no recruit card appeared, so this was a dialog-type
  survivor, not a named recruit with a building post;
  no card, no reward line, no claimed item, no
  resources gained. Quick Dispatch was not run, and
  that is not a gap here - the standing Quick Dispatch
  instruction applies to new survivors taken in with
  posts, and this survivor took none. This refines, not
  contradicts, the Quick Dispatch rule: run it after an
  intake with posts, not after every dialog survivor.
- No different-device dialog, no login or verification
  demanded, no diamonds or money spent, no paid button
  tapped. Tracker marked done for this regular.

## What the 2026-11-01 2034 unit added

- First regular-unit partial since the 1644 done: unit
  survivors-2026-11-01-1803 by ticker-2034, session about
  20:35 to 20:48, status partial. No survivor was processed,
  no recruit card or dialog was opened, and Quick Dispatch
  did not run - correctly, since no intake with a post took
  place. Tracker untouched, so the next tick re-produces
  this regular. This is a single partial after a done, not a
  new streak count: the 25-partial streak ended at the 1644
  done and is not resumed by counting this unit.
- Close discipline held, as the 2026-11-01 retro's A3
  verification asks: the gate line at close is explicitly
  unverified, not claimed clear and not claimed occupied.
  The unit claims only that no question-mark bubble and no
  survivor line was visible in the views it searched.
- Entry snapshot, read live on the opening base screen:
  food 353.1M, iron 543.9M, coin 30.1M, diamonds 2,396,
  total power 149,288,895, window 642 by 951. No
  different-device dialog, no login or verification
  demanded, no diamonds or money spent, no paid button
  tapped.
- Gate search by panning, after a visual-grounding call on
  the opening base screenshot timed out at 180 seconds
  with no result: one horizontal drag produced no view
  change; two vertical drags panned south past the base
  edge into empty snow and rock; a partial drag back
  showed the south-west wall; a diagonal drag panned
  north-east to the built area's east wall and fence
  corner; a further diagonal drag in the same direction
  hit the pan limit with no view change; a return drag
  south-west also produced no view change. The
  north-east direction was the wrong way: the re-read
  pointer below says the gate sits at the bottom centre.
- New look-alike, measured 2034: a small round world icon
  at norm 249,641 (pixel about 160,610) is not a tappable
  survivor figure - one tap produced no change and no
  dialog, and it was left alone after that single tap.
  It joins the pet icon, the temperature button and the
  STOP-barrier point as icons that are not survivors.
- Re-read pointer for the next unit, from the same day's
  successful 1644 run: that unit located the gate survivor
  fresh by visual grounding at question-mark bubble norm
  460,632 and survivor figure norm 458,678, in front of
  the signed gate at the bottom centre of the base. The
  next unit should start from the opening base view and
  pan toward the base's bottom centre, not north-east,
  and should ground the gate figure before any tap.
  Evidence in `_records_/2026-11-01/survivor-intake/2048-queue-run.md`;
  the executor commented this unit's evidence onto open
  Issue #123 (tap calibration), so no duplicate comment
  was left here.


## What the 2026-11-02 0016 unit added

- Second regular-unit partial since the 1644 done, not a
  streak resumption: unit survivors-2026-11-01-2203 by
  ticker-0004, session about 00:05 to 00:16, status
  partial. No survivor was processed, no recruit card or
  dialog was opened, and Quick Dispatch did not run -
  correctly, since no intake with a post took place.
  Tracker untouched, so the next tick re-produces this
  regular. The 25-partial streak ended at the 1644 done
  and is not resumed by counting this unit, the same
  discipline the 2034 section records.
- Close discipline held: the gate line at close is
  explicitly unverified, not claimed clear and not
  claimed occupied. The unit claims only that no
  question-mark bubble and no survivor line was visible
  in the views it searched.
- Gate search: one tap on a visual-grounding box at norm
  207,556 produced no change and no dialog - that box
  did not resolve to a survivor figure. Two further
  visual-grounding calls on fresh base screenshots
  returned unreliable boxes (top-left UI icons, and a
  vehicle parking area), so no tap was taken from them.
  Lesson: a grounding box that resolves to UI chrome or
  a parking area is not a survivor figure; tap only a
  box that resolves to a figure.
- Panning: a horizontal drag moved the view north-east
  and a reverse drag returned it to the opening view; a
  vertical drag produced no view change. No
  question-mark bubble and no survivor line was visible
  in any view. The computer session dropped once
  mid-unit and was restarted; the game window was
  re-selected and the base screen re-read live after
  the restart.
- The 1644 pointer tested, not tapped on a guess: in
  this unit's opening view, norm 458,678 showed only
  snow, a bare tree and a wall corner - no survivor
  figure - so the pointer was not tapped. Rule restated:
  the 1644 coordinates (bubble 460,632, figure 458,678)
  are a re-read pointer for the bottom-centre gate
  area, never a fixed tap point; the next unit
  re-grounds the gate figure fresh before any tap.
- Entry snapshot, read live on the opening base screen:
  food 362.4M, iron 555.0M, coin 36.7M, diamonds 2,476,
  total power 149,198,310, window 642 by 951. No
  different-device dialog, no login or verification
  demanded, no diamonds or money spent, no paid button
  tapped.
- No new issue filed: this is the known repeated gate
  verification failure mode already recorded as a
  standing blocker in this profile and in Issue #123
  (screenshot-grounded tap calibration), not a new gap.
  Evidence in `_records_/2026-11-02/survivor-intake/0016-queue-run.md`.

## What the 2026-11-02 0320 unit added

- Third regular-unit partial since the 1644 done (after the
  2034 and 0016 units), not a streak resumption: unit
  survivors-2026-11-02-0203 by ticker-0308, session about
  03:17 to 03:31, status partial. No survivor was recruited.
  Tracker untouched, so the next tick re-produces this
  regular. Evidence in
  `_records_/2026-11-02/survivor-intake/0320-queue-run.md`.
- Close discipline held: the gate line at close is
  explicitly unverified, not claimed clear and not claimed
  occupied. No intake and no Quick Dispatch ran -
  correctly, since no line state was verified.
- Gate search: a grounded tap on a candidate figure at norm
  (770, 840) opened the Hero Recruit panel, not a survivor
  card. It was closed with the back arrow untouched:
  nothing recruited, nothing bought, hero recruitment is
  another activity. A tap on a ground figure beside the
  tents at norm (522, 499) produced no panel and then the
  view switched to the world map; the unit returned home
  with the Home button, leaving the game on the base
  screen. Lesson: a candidate figure tap can resolve to
  the Hero Recruit panel - a figure-looking tap target is
  not a survivor figure; only a question-mark survivor
  card tap counts as a gate hit.
- The computer session dropped once mid-unit and was
  restarted before continuing; no action was lost to the
  drop.
- Issue #168 filed by the record (play class): pin the gate
  position with a screenshot-anchored location, or confirm
  whether the line is currently empty, so the next unit
  can verify the line state instead of closing unverified
  again. No duplicate issue is filed here; the gap is
  tracked on #168, and the next unit's instruction is the
  record's follow-up. The 1644 pointer (458, 678) was not
  re-tested in this unit.


## What the 2026-11-02 0747 unit added

- Fourth regular-unit partial since the 1644 done (after the
  2034, 0016 and 0320 units): unit survivors-2026-11-02-0603
  by ticker-0734, session 07:43 to 07:47, status partial.
  No survivor was recruited. Tracker untouched, so the next
  tick re-produces this regular. Evidence in
  `_records_/2026-11-02/survivor-intake/0747-queue-run.md`.
- Close discipline held: the gate line at close is
  explicitly unverified, not claimed clear and not claimed
  occupied - 4 question-mark bubbles remained visible in
  the panned-down view after the one dialog survivor, and
  the last tap produced no dialog.
- Gate search: panning the base down to the front-gate area
  shows a line of question-mark bubbles along the left
  fence in that panned-down view, with small survivor
  figures below the bubbles. The re-read pointer for the
  next unit is that view: drag from norm 400,700 to norm
  400,400 on empty road, then re-ground the next figure
  fresh before tapping - no grounding point here is a fixed
  tap point.
- One dialog survivor processed: a tap at norm 132,336 in
  the panned-down view opened the POLAR GUEST dialog
  ("Amazing! This place feels just like home." then "Can I
  stay here forever."), advanced with two dialog taps, and
  closed back to the base. No recruit card appeared, so no
  Recruit button was pressed and no building post was
  assigned - a dialog-type survivor with no post, as in the
  1644 unit, so no Quick Dispatch gap arises from this
  unit and the standing Quick Dispatch blocker is unchanged
  by it, not repeated by it.
- Non-hits, recorded so the next unit does not re-try them
  as gate hits: a tap at norm 150,712 in the starting view
  did nothing; a tap at norm 234,321 selected the Wall
  Lv.26 and was deselected with an empty-road tap; a tap
  at norm 347,378 produced no dialog.
- The computer session dropped once mid-unit and was
  restarted, and the base screen was re-read live after the
  restart; no action was lost to the drop.
- Issue #168 (gate line not verifiable) is not resolved by
  this unit - the line still closes unverified - but the
  panned-down left-fence view and the 132,336 dialog tap
  are commented there as a location lead for the next unit,
  so the gap is tracked on #168 and no duplicate issue is
  filed here.

## What the 2026-11-02 1107 unit added

- Fifth regular-unit partial since the 1644 done (after the
  2034, 0016, 0320 and 0747 units), not a streak resumption:
  unit survivors-2026-11-02-1003 by ticker-1104, session
  11:07 to 11:22, status partial. No survivor was processed:
  0 dialogs opened, 0 recruit cards, 0 recruits taken in.
  Tracker untouched, so the next tick re-produces this
  regular. Evidence in
  `_records_/2026-11-02/survivor-intake/1107-queue-run.md`.
- Close discipline held: the gate line at close is
  explicitly unverified, not claimed clear and not claimed
  occupied. A mid-unit visual-grounding call to recount the
  line timed out, so no recount figure is claimed.
- Gate grounding, fresh in this unit's starting view:
  question-mark bubble at norm 72,662 and a survivor figure
  at norm 70,692. A tap at 70,692 changed the gate corner
  (the question-mark bubble cleared and a small portrait
  icon appeared at about norm 69,715) but opened no
  survivor dialog and no recruit card. A second tap at
  70,692 again changed only the gate corner region and
  switched the base view to a wider framing with the left
  menu rail visible (Events, Capitol, VS, Season II,
  Alliance, Mail, Inventory, WORLD, HEROES); still no
  dialog and no recruit card. Lesson: a tap that only
  changes the gate corner is not a gate hit - the figure
  remains the target, and the next unit grounds the figure
  fresh again and taps the figure itself rather than the
  bubble point.
- Drag-pan method RETIRED inside this unit, per queue rule
  R2: two drags meant to pan the base down (norm 400,700
  to 400,400, then norm 350,650 to 350,350) produced no
  view change at all, so the method was ended inside the
  unit, not repeated. This retires the 0747 section's
  re-read pointer drag (400,700 to 400,400) as a carried
  instruction: the next unit must not reuse that drag
  unchanged. The 0747 panned-down left-fence view itself
  is not disproven - only the drag route to it failed
  here - but it is no longer the standing route to that
  view.
- Quick Dispatch was not run: no recruit-card survivor was
  taken in during this unit, so no newcomer building post
  was created to dispatch. This does not change the
  standing Quick Dispatch blocker, and it is not a further
  identical partial on that blocker: the failure here is
  dialog-opening at a grounded gate point, after the
  drag-pan method was retired inside the unit.
- Closing HUD reading, not a unit result: Total Power
  149,311,528 visible in the closing wide view. No
  resources gained.
- Issue #168 (gate line not verifiable) is not resolved by
  this unit - the line still closes unverified - but the
  executor commented this unit's evidence there, so the
  gap is tracked on #168 and no duplicate issue is filed
  here.

## What the 2026-11-02 1640 unit added

- Sixth regular-unit partial since the 1644 done (after the
  2034, 0016, 0320, 0747 and 1107 units), not a streak
  resumption: unit survivors-2026-11-02-1403 by ticker-1631,
  session 16:40 to 16:57, status partial. No survivor was
  processed: 0 dialogs opened, 0 recruit cards, 0 recruits
  taken in. Tracker untouched, so the next tick
  re-produces this regular. Evidence in
  `_records_/2026-11-02/survivor-intake/1640-queue-run.md`.
- Recovery provenance, stated plainly: the ticker-1631 pass
  timed out before writing its record or releasing the
  device token, so this record was written by the recovery
  pass from the timed-out pass's own report, its claimed
  unit file and its session screenshots - not from a fresh
  game session, and no game was operated during recovery.
  The claim had expired by recovery time, so the unit was
  reaped back to inbox unclaimed (attempt 1 of 3) and
  remains available for the next ticker pass to resume.
- Gate point, same norm as 1107, different outcome: the
  gate corner was grounded fresh in this unit in the norm
  70,692 area, and taps there produced no survivor dialog
  and no recruit card, with the screen unchanged across
  two attempts. In the 1107 unit, taps at 70,692 changed
  the gate corner region. The two readings do not
  contradict: the same norm point behaves differently
  across camera views, so 70,692 is a re-read pointer
  for the gate-corner area, never a fixed gate hit, and
  the next unit still grounds the figure fresh before
  any tap. The retired drag-pan method was not reused
  here.
- Close discipline held: the gate line at close is
  explicitly unverified, not claimed clear and not
  claimed occupied. Quick Dispatch did not run -
  correctly, since no recruit-card survivor was taken
  in. No different-device dialog appeared; the game was
  live on the Mac for the whole unit. No Upgrade, no
  Finish Now, no speedup, nothing bought, no harvest
  bubble tapped.
- Issue #168: the record states its evidence is commented
  there, but no 1640 comment was found on #168 at the
  1732 organizer pass, so this run left the 1640 comment
  itself rather than assuming the record's claim.

## What the 2026-11-02 1718 unit added

- Second attempt at the same unit, not a new distinct
  partial: unit survivors-2026-11-02-1403 by ticker-1703,
  session about 17:03 to 17:18, status partial. This unit
  was already attempted in this cycle by ticker-1631
  (the 1640 record, partial, 0 processed); it was reaped
  after its lease expired and re-claimed in this pass.
  By the 0041 counting rule, the distinct-unit count
  since the 1644 done stays at six - 1718 is a
  re-attempt of the 1403 unit, not a seventh distinct
  partial. No survivor was processed: 0 dialogs opened,
  0 recruit cards, 0 Quick Dispatch runs. Tracker
  untouched, so the next tick re-produces this regular.
  Evidence in
  `_records_/2026-11-02/survivor-intake/1718-queue-run.md`.
- Changed methods under queue rule R2, not a repeat of
  the 70,692 starting-view tap: a drag pan from norm
  400,700 to norm 400,400 on the road produced no view
  change - a further confirmation of the drag-pan
  retirement from the 1107 unit, not a new route. A tap
  at norm 89,722, estimated from a cropped enlargement
  as the survivor figure below the question-mark bubble,
  opened the radar world map instead (13/40 tasks, Quick
  Execute button); no radar work was done, and HOME at
  norm 925,945 returned the game safely to the base
  screen. Correction for the next unit: norm 89,722 is
  a radar entry point, not the survivor figure. A tap
  at norm 109,626 on the question-mark bubble itself
  produced no change and no dialog.
- Grounding discipline: a mid-unit visual-grounding call
  made to recount the line timed out after 180 seconds;
  that tool is not a useful recount route inside a
  15-minute unit - the same timeout already recorded in
  the 1107, 2034 and 0041 units.
- Close discipline held: the gate line at close is
  explicitly unverified, not claimed clear and not
  claimed occupied. Issue #168 (gate line not
  verifiable) is not resolved by this unit, but the
  executor commented this unit's findings there, so no
  duplicate comment was left here.

## What the 2026-11-02 1948 unit added

- Unit survivors-2026-11-02-1803 by ticker-1934, session
  about 19:46 to 19:48, status partial. Seventh distinct
  partial since the 1644 done by the 0041 counting rule
  (1718 was a re-attempt of the 1403 unit, not a
  distinct one). No survivor was processed: 0 dialogs
  opened, 0 recruit cards, 0 Quick Dispatch runs.
  Tracker untouched, so the next tick re-produces this
  regular. Evidence in
  `_records_/2026-11-02/survivor-intake/1948-queue-run.md`.
- Gate figure: a single question-mark bubble over a
  small figure at the gate entrance, bottom centre of
  the dragged base view (bubble about norm 490,650,
  figure just below it).
- Figure taps select a squad vehicle, not a survivor:
  taps at norm 485,680 and norm 490,690 both selected
  "1st Squad Lv.20" (tank and up-arrow radial), no
  survivor card opened, no dialog, no recruit. Per
  queue rule R2, the method ended inside the unit
  after two no-change taps; no further tap was made
  at the same point. Correction for the next unit:
  the figure point below the gate bubble is a
  squad-vehicle selection point in this view, not a
  recruit tap point.
- Deselect hazard: an empty-ground tap at norm 750,500
  to deselect selected a Farmland Lv.28 building
  instead (paw and up-arrow radial) - deselect taps can
  land on buildings. No action was taken from any
  selection radial.
- Close discipline held: the squad-vehicle selection
  radial was left open on the base view at close, and
  the next unit screenshots first (the 1949 training
  unit confirms the radial still open at its entry).
  The gate line at close is explicitly unverified,
  not claimed clear and not claimed occupied: whether
  more survivors wait behind the one figure, and
  whether that figure is a recruit or a visitor, is
  unknown.
- Named re-read for the next survivors unit: start at
  the gate with a fresh grounding, verify a survivor
  figure before any tap, and try a different entry
  variant (the bubble centre itself, or the gate from
  an undragged base view) instead of repeating the
  figure taps used here.
- Issue #168 (gate line not verifiable) is not
  resolved by this unit; its evidence is commented
  there by this run, since the record itself does not
  claim a comment, so no duplicate comment is left
  here.


## What the 2026-11-02 2252 unit added

- Unit survivors-2026-11-02-2203 by ticker-2234,
  session about 22:47 to 22:52, status partial: 0
  survivors processed, gate line unverified, tracker
  untouched, so the next tick re-produces this
  regular. This is the eighth distinct partial since
  the 1644 done, by the 0041 counting rule
  (re-attempts of one unit do not add to the count).
  No Quick Dispatch ran, since no intake happened.
  Evidence in
  `_records_/2026-11-02/survivor-intake/2252-queue-run.md`.
- Method change under rule R2, following the 1948
  unit's named re-read on open issue #168: instead
  of repeating the figure taps that selected a squad
  vehicle in 1948, this unit tried the bubble centre
  itself, on the undragged restored base view left by
  the harvest unit in the same pass.
- Visual grounding on that base screenshot returned
  a survivor figure at norm (448,580) and a
  question-mark bubble at norm (447,550). The
  bubble-centre tap at (447,550) selected Titanium
  Alloy Factory No.3 Lv.30 (orange info button,
  building label), not a survivor card, dialog or
  recruit. The grounding point was a building area
  mislabelled as a survivor, the same mislabelling
  class as the 0636 radar grounding notes.
- Per rule R2 the method at this point ends inside
  the unit: no second tap was made at (447,550). An
  empty-ground tap at norm (750,800) deselected the
  building; no Upgrade, no panel action, nothing
  bought, nothing dispatched from any selection.
- What was not done, named re-read for the next
  survivors unit: the gate line was not verified,
  whether survivors wait at the gate and whether any
  figure seen is a recruit or a visitor is unknown.
  Do not reuse the (447,550) bubble point or the
  (448,580) figure point - both resolve to the
  Titanium Alloy Factory No.3 area on this camera
  view - and do not reuse the 1948 dragged-view
  figure points (485,680 / 490,690), which select a
  squad vehicle. The next unit must ground the gate
  line fresh on its own screenshot and verify a
  survivor figure before any tap.
- Issue handling: no new issue filed. This is the
  known gate-verification failure mode already open
  as issue #168; this unit's bubble-centre evidence
  is commented there by the executor, not filed anew.


## What the 2026-11-03 0247 unit added - bubble change is not intake proof, re-ground before every tap

- Unit survivors-2026-11-03-0203 by ticker-0234, about
  02:47 local, status partial. Evidence in
  `_records_/2026-11-03/survivor-intake/0247-queue-run.md`.
- Entered from the harvest unit's top-edge panned view:
  the front gate (walled entrance with the yellow sign,
  top-centre of the view) was already in frame. Fresh
  visual grounding counted 3 survivor figures with
  question-mark bubbles at the gate, at norm (475,384),
  (506,378) and (535,372).
- Tap 1 at the first grounded figure (475,384): no card
  or dialog opened. The next screenshot showed two
  smiley-face bubbles where question marks had been, and
  a re-ground counted 1 question-mark bubble left at
  (450,330). No name, role or recruit card was read for
  any survivor, so no intake is claimed as verified from
  the bubble change alone: the bubble state moved, but
  the intake itself was never confirmed on a card. This
  is the standing proof rule, re-confirmed: a
  question-mark to smiley change without a card is not
  an intake.
- Tap 2 at the estimated figure point under the last
  question mark (450,375): misfired. It selected the 1st
  Squad Lv.20 map marker instead and opened its squad
  controls (tank icon and green arrow). The point was
  stale: the view had shifted slightly between the
  grounding screenshot and the tap, and the figure
  estimate was never re-grounded on the current frame.
  Nothing was dispatched from the squad controls; an
  empty-ground tap at (600,700) deselected them cleanly.
  The lesson is now absolute for this activity:
  re-ground the gate figures fresh on the current
  screenshot before EVERY tap, never reuse a figure
  point across screenshots, because the map drifts
  between frames.
- Closing gate state, unverified: the closing screenshot
  shows no question-mark bubbles at the gate itself, but
  a grounding pass on it returned one ambiguous
  question mark at (638,693), away from the gate and not
  identifiable as a gate survivor, so it is not counted
  as a remaining line member. The line is therefore
  neither confirmed clear nor confirmed staffed.
- Quick Dispatch did not run: with no verified intake
  and no building panel opened, there was nothing to
  post, and the unit budget was spent. It stays as
  follow-up for the next unit if an intake is verified
  there.
- Result stats: target 3, achieved 0, verified no,
  blocker category c. Tracker untouched, per the rule
  for partial units; the next tick re-produces survivors
  and resumes at the gate. Follow-up: re-ground fresh
  before every tap, tap figures only, and if a card
  opens, record the name, role and trait before Recruit.
  This unit's evidence is commented onto Issue #168 by
  this run; the issue stays open.

## What the 2026-11-03 0644 unit added - tenth distinct partial since the 1644 done, two grounding points rejected

- Ticker-0634, unit survivors-2026-11-03-0603, about
  06:44 local, status partial. Evidence in
  `_records_/2026-11-03/survivor-intake/0644-queue-run.md`.
- Computer session cc-316 (carried from the radar and
  harvest units in this pass) dropped between units;
  session cc-318 was started, LastWar re-selected, and
  no game state was lost. Transient, as in other units
  this pass.
- Gate search: from the central base view, dragged to
  the upper base area twice ((500,300 to 500,650), then
  (500,250 to 500,700)); the second drag reached the
  upper view with the Capitol pyramid at top-right, the
  pink central building and the parked helicopter. No
  front-gate line with question-mark bubbles was
  identified in the central view or in the upper view.
- Grounding rejections, do not reuse: a
  visual-grounding pass on the upper view returned a
  survivor figure at norm 498,674 and a gate at norm
  70,125; both are rejected as unreliable - the first
  point sits on a small map marker by the gold building,
  not on a verified gate figure, and the second sits in
  the top bar. Neither point was tapped: the 0247 unit's
  stale-figure tap misfired onto a squad marker, and
  tapping an unidentified marker risks a dispatch.
- No survivor card or dialog was opened, no recruit was
  taken in, no building panel was opened, and Quick
  Dispatch did not run (nothing verified to post).
  Tracker untouched, per the rule for partial units.
- Count: this is the tenth distinct partial since the
  1644 done (ninth was 0247). The standing blocker
  stands: gate line not found or verified, and the unit
  closes unverified with a named re-read instead of
  closing on a presumed line state.
- Follow-up for the next survivors unit: start at the
  gate with a fresh grounding on the live frame, and
  verify a survivor figure before any tap; if the line
  still cannot be verified, close unverified again with
  this blocker named. This unit's evidence is commented
  onto Issue #168 by this run; the issue stays open.

## Open questions

- Where the Factory building sits on the base, so the Mechanic
  post can be verified after intake.
- How fast the line refills and whether it has a cap.
- Whether a recruit can be moved to a different building by hand,
  and what the second David means - names repeat across roles.
- The three document icon bubbles over the headquarters area
  buildings open the Status Overview when tapped - what they are
  is unconfirmed; they are not collected like output bubbles.
- Do-not-reuse points (2252): bubble (447,550) and figure
  (448,580) on the undragged restored base view resolve to
  Titanium Alloy Factory No.3, not a survivor; the 1948
  dragged-view figure points (485,680 / 490,690) select a
  squad vehicle. Ground the gate line fresh each unit.
- Do-not-reuse points (2112): centre-view grounding point
  (505,590) is a building bubble, not a survivor figure
  (tap produced no change); (545,740) is empty snow and
  wall, rejected pre-tap from an enlarged crop. The 1644
  re-read pointer (bubble 460,632, figure 458,678) shows
  buildings, not a gate line, in the 2112 current view -
  the pointer is qualified, not erased, and the next unit
  grounds fresh rather than navigating to it.

## Changelog

- 1.29.0 (2026-11-05): 0134 survivors unit folded (failed, twenty-sixth consecutive screen-capture failure, no game screen read, no input dispatched, tracker untouched); NEW DIAGNOSIS from the on-screen View-menu read - the game window is windowed 1920x1080 on an inactive Space, not in native fullscreen (menu lists Enter Full Screen), so the capture failure is the pixel stream of an off-screen window, not a broken screen-recording permission; background Space keys do not switch Spaces, set_window_frame is gated by the stale-observation rule, list_windows needs the exact app name "LastWar"; CORRECTION - the 1707/2135 "running fullscreen" wording and the 1122 "left in native fullscreen" carry-forward are superseded, and the standing permission/pipeline-restart follow-up is replaced by the window-back-on-active-Space unblock (owner Dock-icon click); same correction applied to resource-collection, perception-scout, radar-tasks, arms-race and alliance-gifts in this run; evidence commented on Issue #284 by the ticker pass, twenty-sixth and twenty-seventh occurrences commented onto Issue #282 by this run. (1.27.0 and 1.28.0 carry the 1707 and 2135 sections without changelog lines; the numbering is preserved, not rewritten.)

- 1.26.0 (2026-11-04): gate line verified live (three question-mark bubbles above three survivor figures on the road in front of the gate wall, fullscreen screenshot and 4x crop), moving the blocker from line-not-found to taps-not-opening-cards; method change per rule R2 (windowed background taps and WORLD calibration both no-change, so native fullscreen via the green zoom button plus crop-grounded figure taps, which dispatched a visual change but opened no card); focus guard blocking one tap while Chrome was frontmost; session dropped twice mid-unit (cc-449, cc-450) with recovery and no state lost; window left in native fullscreen for the next unit; next unit must try the question-mark bubble itself in fullscreen or a long-press on a freshly grounded figure, re-grounding from a fresh screenshot immediately before tapping; 0 recruited by live read, Quick Dispatch not run, tracker untouched; folded from the 1122 survivors record, evidence already commented on Issue #168 by the ticker pass so no duplicate comment here; no earlier claim superseded. (1.24.0 and 1.25.0 carry the 0416 and 0757 sections without changelog lines; the numbering is preserved, not rewritten.)

- 1.23.0 (2026-11-04): contested stop after two kick takeovers (0110 unit, first recorded instance of the owner two-kick rule firing, no third takeover, tracker untouched so the next tick re-produces the regular), server maintenance at entry matching the 0034 harvest unit and cleared by about 01:04 (maintenance Confirm dismissing to the loading screen, distinguished from the disconnected-dialog crash path), gate line NOT READ and not claimed empty, glimpsed power figure explicitly not used as a closing figure, folded from the 0110 survivors record; no earlier claim superseded.

- 1.22.0 (2026-11-03): thirteenth distinct partial since the
  1644 done (2112 unit, gate line explicitly unverified,
  close discipline held), 1644 re-read pointer (460,632 /
  458,678) now showing buildings not a gate line in the
  current view so qualified not erased, centre-view point
  (505,590) rejected as a building bubble after a no-change
  tap, (545,740) rejected pre-tap as empty snow via crop,
  single-drag pan moving about 1 percent abandoned, slow
  pans to the south tip and east mountains finding no gate
  and no survivor line, west-wall STOP sign seen but not
  verified as the Zombies gate, window 642 by 951
  re-confirmed, and Issue #168 evidence commented by this
  run, folded from the 2112 survivors record. (1.20.0
  carries the 1050 section without a changelog line; the
  numbering is preserved, not rewritten.)

- 1.4.0 (2026-11-01): streak carried past the retro window
  (0016 partial), background-input control dependence, Escape
  re-confirmation, and the pan failure shared with the 2343
  harvest unit, folded from the 0016 survivors unit; the
  transient Arms Race side observation in that record (a live
  Hero Advancement phase score) was deliberately not folded -
  it belongs to the queued arms-race unit.

- 1.5.0 (2026-11-01): duplicate re-run disclosure (0041 re-ran
  the 0016 unit id through working-tree/records divergence;
  distinct-unit partial streak stays 23), the four-pan search
  with only three pans counted, the unretried grounding
  timeout, and the focus-loss recurrence with the same
  274,18 title-bar fix, folded from the 0041 survivors unit.

- 1.6.0 (2026-11-01): distinct-unit partial streak reaches
  24, and the look-alike corrections (pet icon misread as a
  question-mark bubble, green temperature button misread
  as a smiley bubble, STOP-barrier tap point with no
  change), folded from the 0913 survivors unit.

- 1.8.0 (2026-11-01): distinct regular-unit partial streak
  reaches 25, the opposite-direction pan with only about
  3 percent view shift, the no-change tap probe at
  620,670 on the bottom-right walking figure, the gate
  line still not read and not claimed empty, and the
  zoom-out-to-the-perimeter-first next-unit instruction
  with its process-failure warning, folded from the 1159
  survivors unit. (1.7.0 carried the 1017 diagnostic
  section without a changelog line; the numbering is
  preserved, not rewritten.)

- 1.9.0 (2026-11-01): partial streak broken at 25 by the
  1644 done (fresh grounding in the 642 by 951 window,
  figure tap at 458,678, question-mark to smiley, gate
  line clear), and the dialog-type survivor with no post
  so no Quick Dispatch gap, folded from the 1644
  survivors unit.

- 1.10.0 (2026-11-01): first regular-unit partial since the 1644 done (2034 unit, gate line explicitly unverified, close discipline held), the failed pan sequence that went north-east instead of toward the bottom-centre gate, the non-tappable world icon at 249,641 as a new look-alike, and the 1644 re-read pointer (bubble 460,632, figure 458,678) for the next unit, folded from the 2048 survivors record.

- 1.11.0 (2026-11-02): second regular-unit partial since the 1644 done (gate line explicitly unverified, close discipline held), the unreliable grounding boxes (UI icons, parking area) not tapped, and the 1644 pointer tested but not tapped on a guess at 458,678, folded from the 0016 survivors record.

- 1.12.0 (2026-11-02): third regular-unit partial since the 1644 done (gate line explicitly unverified, close discipline held), the candidate-figure tap resolving to the Hero Recruit panel as a new look-alike, the tents-figure tap switching to the world map, and Issue #168 filed by the record, folded from the 0320 survivors record.

- 1.14.0 (2026-11-02): fifth regular-unit partial since the 1644 done (gate line explicitly unverified, close discipline held), fresh gate grounding at bubble 72,662 and figure 70,692 with taps changing only the gate corner and opening no dialog, the drag-pan method retired inside the unit per rule R2 (which retires the 0747 drag pointer as a carried instruction), no Quick Dispatch gap since no recruit was taken in, and Issue #168 commented by the executor, folded from the 1107 survivors record.

- 1.13.0 (2026-11-02): fourth regular-unit partial since the 1644 done (gate line explicitly unverified, close discipline held), the panned-down left-fence gate line with the 132,336 Polar Guest dialog tap and no recruit card so no Quick Dispatch gap, the three non-hit taps, and Issue #168 commented with the location lead, folded from the 0747 survivors record.

- 1.15.0 (2026-11-02): sixth regular-unit partial since the 1644 done (1640 unit, recovery-written after the ticker pass timed out, gate-corner taps at the 70,692 area changing nothing unlike the 1107 corner change, so the point is a re-read pointer not a fixed hit, unit reaped to inbox unclaimed attempt 1 of 3), the 1718 re-attempt of the same 1403 unit (not a seventh distinct partial by the 0041 rule, drag-pan re-confirming its 1107 retirement, 89,722 corrected to a radar entry point not a survivor figure, bubble tap at 109,626 with no change, 180-second grounding recount timeout), and the #168 comment gap for 1640 closed by this run, folded from the 1640 and 1718 survivors records.

- 1.16.0 (2026-11-02): seventh distinct partial since the 1644 done (1803 unit, gate line explicitly unverified, close discipline held), figure taps at 485,680 and 490,690 selecting the 1st Squad Lv.20 vehicle instead of a survivor card so the figure point is a squad-vehicle selection in this view, deselect tap at 750,500 selecting a Farmland Lv.28 building, squad radial left open at close, fresh-grounding plus different-variant re-read named, and Issue #168 evidence commented by this run, folded from the 1948 survivors record.

- 1.17.0 (2026-11-02): eighth distinct partial since the 1644 done (2252 unit, gate line explicitly unverified, close discipline held), rule R2 bubble-centre method tried and failed with (447,550) and (448,580) resolving to Titanium Alloy Factory No.3, no second tap per rule R2, deselect at (750,800), do-not-reuse list extended with both points, and Issue #168 evidence commented by the executor, folded from the 2252 survivors record.

- 1.18.0 (2026-11-03): ninth distinct partial since the 1644 done (0247 unit, gate line explicitly unverified, close discipline held), bubble change to smiley without a card explicitly not counted as an intake, stale figure point (450,375) selecting the 1st Squad Lv.20 vehicle so re-grounding before every tap is now absolute, ambiguous question mark at (638,693) away from the gate not counted, Quick Dispatch not run with no verified intake, and Issue #168 evidence commented by this run, folded from the 0247 survivors record.

- 1.19.0 (2026-11-03): tenth distinct partial since the 1644 done (0644 unit, gate line explicitly unverified, close discipline held), upper-view grounding points (498,674) and (70,125) rejected as unreliable (map marker by the gold building, top bar) and neither tapped, session drop cc-316 to cc-318 transient with no state lost, Quick Dispatch not run with no verified intake, and Issue #168 evidence commented by this run, folded from the 0644 survivors record.


- 1.21.0 (2026-11-03): twelfth distinct partial since the 1644 done (1543 unit, bottom-left gate cluster grounded in the central view at (103,665) and (135,655), tap changing only the gate region with no card so no verified recruit under rule R1, out-of-cluster re-ground point (235,615) rejected untapped, diamond counter 2,836 to 2,841 recorded unattributed with no popup), folded from the 1543 survivors record; Issue #168 evidence commented by this run.

## What the 2026-11-03 1050 unit added - gate line not found again, grounding timed out twice, no tap on unidentified markers

- Ticker-1034, unit survivors-2026-11-03-1003, about
  10:45 to 10:50 local, status partial. Evidence in
  `_records_/2026-11-03/survivor-intake/1050-queue-run.md`.
- Session: computer session cc-337 dropped between
  units (observation unavailable); session cc-339 was
  started, Last War re-selected, no game state lost,
  base view intact. No different-device dialog.
- Gate search: from the central base view, dragged to
  the upper base area twice ((500,300 to 500,650)
  with no visible view change, then (500,250 to
  500,700)); the second drag reached the upper view
  with the railway at top, the Capitol pyramid at
  top-right, the pink central building and the parked
  helicopter - the same upper view the 0644 unit
  reached. No front-gate line with question-mark
  bubbles was identified in the central view or in
  the upper view. An orange sign near the top-centre
  fenced enclosure was visible but not readable as a
  gate sign on this frame, and no survivor figure
  with a question-mark bubble was verified.
- Grounding lesson, re-confirmed: visual grounding
  was attempted twice on the live frames (once on
  the central view, once on the upper view); both
  attempts timed out at the tool level with no points
  returned. Per the 0644 lesson, no unidentified
  marker was tapped: the 0247 unit stale-figure tap
  misfired onto a squad marker, and tapping an
  unverified point risks a dispatch. No survivor card
  or dialog was opened, no recruit was taken in, no
  building panel was opened, and Quick Dispatch did
  not run (nothing verified to post).
- Why partial, not done: gate line not found or
  verified in this unit, the standing blocker in this
  profile (queue era 2026-10-28 to 2026-10-31: 22 of
  22 survivor units partial; today 0247 and 0644 also
  partial, now joined by 1050). Per this profile
  rule, the unit closes unverified with a named
  re-read instead of closing on a presumed line
  state. Tracker untouched.
- Follow-up for the next survivors unit: start at
  the gate with a fresh grounding on the live frame,
  and verify a survivor figure before any tap; if
  the line still cannot be verified, close unverified
  again with this blocker named. No earlier claim
  superseded.

## What the 2026-11-03 1543 unit added - gate cluster grounded in the central view, no verified recruit, out-of-cluster point rejected

- Ticker-1534, unit survivors-2026-11-03-1403, about
  15:36 to 15:43 local, status partial. Evidence in
  `_records_/2026-11-03/survivor-intake/1543-queue-run.md`.
- Gate cluster confirmed in the central base view, no
  pan needed: fresh visual grounding on the live frame
  found two survivor points at the bottom-left gate
  cluster, norm (103,665) and (135,655), in the region
  of the question-mark bubbles at the left fence edge.
  This supports the 1050 follow-up: start at the gate
  with a fresh grounding, and do not pan to the upper
  view first, where the 0644 unit found no verifiable
  line.
- Tap 1 at the first grounded point (103,665):
  dispatched, with a measured visual change in the
  gate region [46,600,156,725]. No survivor card,
  dialog, name, role or Recruit button was read after
  the tap, so no recruit is claimed as verified. Bubble
  change alone is not an intake under rule R1, as in
  the 0247 unit.
- Re-grounding on the post-tap frame returned a single
  point at norm (235,615), which does not sit on the
  bottom-left gate cluster and was rejected as
  unreliable. No second tap was made: the 0247 unit's
  stale-figure tap misfired onto a squad marker, and
  tapping an unidentified marker risks a dispatch. The
  reject-out-of-cluster discipline from the 0644 unit
  is re-affirmed here.
- HUD note, unattributed: the top-right diamond
  counter read 2,836 before the tap and 2,841 after
  it. No reward popup was read, so this change is
  recorded as observed only and is NOT attributed to
  the tap. A counter delta without a popup is never a
  verified gain.
- Quick Dispatch did not run: nothing verified to
  post. No building panel was opened, no purchase
  tapped, no other activity's work done.
- Why partial, not done: twelfth distinct partial
  since the 1644 done (0247 ninth, 0644 tenth, 1050
  eleventh, this unit twelfth), gate line explicitly
  unverified, close discipline held. Tracker
  untouched.
- Follow-up for the next survivors unit: start at the
  gate with a fresh grounding on the live frame and
  verify a survivor figure before any tap; if the
  grounding returns a point outside the gate cluster,
  reject it and close unverified with this blocker
  named, rather than tapping it. No earlier claim
  superseded.

## What the 2026-11-03 2112 unit added - thirteenth distinct partial, 1644 pointer now shows buildings, two more rejected points

- Ticker-2104, unit survivors-2026-11-03-1803, about
  21:05 to 21:12 local, status partial. Evidence in
  `_records_/2026-11-03/survivor-intake/2112-queue-run.md`.
- Session: LastWar already open on the Mac mini,
  window 642 by 951, re-confirmed. No
  different-device dialog, no login or verification
  demanded. Base screen read live at entry: food
  275.0M, iron 612.5M, coin 34.2M, power 149,948,901,
  diamonds 2,841.
- Gate line: NOT READ. The signed "Zombies" front
  gate itself was not located in this unit, so no gate
  line can be quoted verbatim and the gate is NOT
  claimed empty. Close discipline held.
- Grounding rejections, do not reuse: fresh visual
  grounding on the centre base view first pointed at
  a building output bubble near norm 505,590. One tap
  there produced no change, and an enlarged crop
  showed it was a building bubble, not a survivor
  figure, so that point was rejected, not a survivor.
  A second grounding round pointed at empty snow near
  norm 545,740; an enlarged crop showed only wall and
  snow, so that point was rejected before any tap.
- Pan method: the single drag action moved the view
  by only about 1 percent, so it was abandoned. A
  slow drag up panned past the base into empty snow;
  a partial drag back showed the base south tip and
  its wall, with no question-mark bubbles and no
  survivor line at the south tip. A slow drag
  leftwards panned east past the base into mountains,
  again with no gate and no survivor line. A reverse
  drag moved the view back west before closing.
- STOP sign, not a gate: the STOP sign on the west
  wall was seen in the south panned crop, but it was
  not verified as the Zombies gate and no survivor
  figure stood by it, so it is not recorded as the
  gate.
- 1644 pointer qualified, not erased: the gate was
  located once on 2026-11-01 at norm 460,632 (bubble)
  and 458,678 (figure), bottom centre, but that point
  in this unit's current view shows buildings, not a
  gate line. The 1644 event stands as history; the
  pointer no longer navigates the next unit, which
  starts from a fresh full-perimeter read rather than
  re-tapping the rejected points in this record.
- No survivor was processed, no recruit card
  appeared, no Quick Dispatch ran (nothing verified
  to post). No diamonds or money spent, no paid
  button tapped. Tracker untouched, per the rule for
  partial units, so the next tick re-produces this
  regular.
- Why partial, not done: thirteenth distinct partial
  since the 1644 done (0247 ninth, 0644 tenth, 1050
  eleventh, 1543 twelfth, this unit thirteenth),
  gate line explicitly unverified, close discipline
  held. Blocker category e (repeated blocker).
- Follow-up for the next survivors unit: start from a
  fresh full-perimeter read, verify a survivor figure
  before any tap, and do not re-tap (505,590),
  (545,740) or the 1644 pointer as a location. If the
  line still cannot be verified, close unverified
  again with this blocker named. No earlier claim
  superseded; the 1644 pointer is qualified as above.

## What the 2026-11-04 0110 unit added - contested stop after two kick takeovers, maintenance cleared mid-pass

- First recorded contested stop in this profile: the ticker-0104 pass met the different-device dialog, tapped Confirm twice (each kick exited the app, per the owner kick rule), and met the same dialog a third time, so the pass stopped with no third takeover, per the owner rule that two kicks in one pass followed by a returning dialog means the owner is likely playing on another device. No survivor was processed, no recruit card appeared, no Quick Dispatch ran, tracker untouched so the next tick re-produces this regular.
- Entry carried the same server-maintenance state as the 0034 harvest unit: a TIPS dialog "The server is under maintenance. Please wait a moment, we'll be back with you shortly!" over the login screen with a "Login failed. Please retry or contact support." toast. Confirm on the maintenance dialog dismissed it to the loading screen, and the base was then reached behind the different-device dialog - so the maintenance had lifted by about 01:04, roughly half an hour after it blocked the 0034 pass outright. The maintenance dialog's Confirm is not the crash path: the 0034 record distinguishes it from the "Server disconnected" dialog, whose Confirm quits the app.
- Nothing from this unit is a closing figure: the base was never reached interactively, the gate line was NOT READ and is not claimed empty, and the power figure glimpsed behind the dialog (150,013,787) is explicitly not used - the record marks the unit unverified, blocker category f. The previous unit's rejected points (505,590) and (545,740) were not re-tapped.
- No earlier claim superseded; no new issue filed - the contested stop is the owner rule working as written, and the maintenance episode resolved within the pass.

## What the 2026-11-04 0416 unit added - gate still not located, re-read named

- Partial, unverified, ticker-0404, unit survivors-2026-11-04-0203 (game work about 04:12 to 04:16 local). Base entered cleanly with no different-device dialog (contrast the contested ticker-0104 unit). HUD read live: food 397.0M (consistent with the 0413 harvest +2.0M), iron 732.0M, coin 3.1M, second row 21.0M and 922.2K, total power 150,028,269.
- The base was panned across the full width - left-edge iron-mine row, center-right HQ and tent area, far-right decoration and radar area, bottom snow edge with the Season 2 troop area - and no Zombies gate sign was seen in any of these views.
- Visual grounding on the center-right view returned candidate points (front gate 511,728; survivor line 668,789; survivor figure 744,852), but on the restored view those points fall on the tent and parking area and no survivor figure or question-mark bubble could be verified there at this screenshot resolution, so none of them was tapped as a survivor: a parking area is not a survivor figure.
- 0 survivors processed, no recruit card appeared, no Quick Dispatch ran. The gate line is NOT READ and is NOT claimed clear or empty: the gate was never located, so the line state is unverified, not empty. This continues the standing survivor blocker (Quick Dispatch never run); tracker untouched, so the next tick re-produces this regular.
- Named re-read for the next survivors unit: start from the center-right view, check the tent and parking-area figures first, and pin the Zombies gate sign before any intake tap. (2026-11-04 0757 correction: the view prescription is corrected to the center view - the 0757 unit entered on a top-edge view and its reverse drag (500,600) to (500,300) did not restore the center view; pin the 'Zombies' sign text on a screenshot before any intake tap, and treat the 0757 candidates (118,285) and (272,412) as unverified until that pin exists.)
- No earlier claim superseded; no new issue filed - the gate-location blocker is already the standing R2 item for this regular.

## What the 2026-11-04 0757 unit added - gate sign never pinned, candidates untapped, center-view re-read named, partial unverified

- Unit survivors-2026-11-04-0603 by ticker-0734, about 07:54 to 07:57 local, status partial unverified. Session cc-431 (same session as the harvest unit). No different-device dialog appeared. Evidence in `_records_/2026-11-04/survivor-intake/0757-queue-run.md`.
- Entry framing: the base view at entry was the top-edge view left by the harvest unit (hero statues, Eiffel Tower, ferris wheel). A reverse drag (500,600) to (500,300), intended to restore the center view, left the framing essentially unchanged (still top-edge on the closing screenshot) - that drag does not restore the center view.
- Grounding candidates on the top-edge screenshot, NONE tapped: front gate (118,285), survivor figure with question-mark bubble (272,412), survivor line (185,350). Per queue rule R2 and the 0416 precedent, no intake tap was made on an unpinned grounding point: the 0416 unit already showed grounding candidates falling on tent and parking area with no verifiable figure there, and this unit's candidates are in the same unverified class.
- What was not done: no survivor was processed, no recruit card appeared, no Quick Dispatch ran. The gate line is NOT claimed clear and no survivor count is reported: the 'Zombies' gate sign was never pinned - no 'Zombies' text is readable on the top-edge screenshot - so the line state is unverified, not empty. This continues the standing survivor blocker (queue-era units partial, Quick Dispatch never run). Tracker untouched, per the rule for partial units, so the next tick re-produces this regular.
- Named re-read for the next survivors unit, correcting the 0416 re-read's view prescription (see the qualification in that section): start from the center view (not the top edge), pin the 'Zombies' gate sign text on a screenshot before any intake tap, and treat the (118,285) and (272,412) candidates above as unverified until that pin exists.
- No earlier claim superseded; no new issue filed - the gate-location blocker is already the standing R2 item for this regular. No diamonds, money, speedup or paid button touched; no assembly, no teleport; no notification dialog enabled (no visitor dialog was opened).

## What the 2026-11-04 1122 unit added - gate line verified live (3 question-mark survivors), fullscreen method change, figure tap dispatched but no card, partial

- Unit survivors-2026-11-04-1003 by ticker-1104, about 11:04 to 11:22 local, status partial. The 15 minute unit cap was reached mid-work. No survivor was recruited, no card was opened, Quick Dispatch did not run, and the tracker is untouched, so the next tick re-produces this regular as a fresh unit. Evidence in `_records_/2026-11-04/survivor-intake/1122-queue-run.md`.
- Gate line VERIFIED live: after dragging the base view, three question-mark bubbles stood in a row above three small survivor figures on the road in front of the gate wall, seen clearly in a fullscreen screenshot and in a 4x crop of the cluster. This moves the standing blocker past its line-not-found form: the line exists and holds waiting survivors, and the blocker is now taps-not-opening-cards. This evidence was already commented on Issue #168 by the ticker pass, so no duplicate comment is made here. No recruit card, dialog, or visitor dialog was opened in this unit, so recruits equal 0 by live read, not by assumption.
- Method changes in this unit (rule R2): windowed background taps on bubble points missed twice with no screen change, and a WORLD calibration tap also showed no change, so the method changed: the game was moved to native fullscreen (entered via the green zoom button during this unit) and the survivor figures were re-grounded from a 4x crop of the cluster instead of inherited points. The crop-grounded figure tap did dispatch (the observation reported a visual change over the survivor area), but no card opened, and the view afterwards showed a panned base with no dialog. A focus guard blocked one tap while Google Chrome was frontmost, and the computer session dropped twice mid-unit (cc-449, cc-450) with recovery and no game state lost.
- Window state carried forward: the game window was left in native fullscreen. The next unit inherits fullscreen geometry. Taps dispatch in fullscreen, so no restore was attempted inside the unit cap.
- Follow-up for the next survivors unit: the next unit must change method again before repeating this one - try the question-mark bubble itself in fullscreen, or a long-press on a grounded figure, and re-ground from a fresh screenshot immediately before tapping, since the figures may shift between screenshots.
- No diamonds, money, price tags, paid buttons, speedups, research, buildings, assembly or teleport were touched. Nothing was claimed. No earlier claim superseded; no new issue filed - the gate-location blocker is already the standing R2 item for this regular, now in its taps-not-opening-cards form.

## What the 2026-11-04 1707 unit added - screen-capture failure, tenth consecutive pass, nothing read

- Unit survivors-2026-11-04-1403 by ticker-1704, about 17:04 to 17:07 local, status failed. Evidence in `_records_/2026-11-04/survivor-intake/1707-queue-run.md`. No survivor was recruited, no card was opened, Quick Dispatch did not run, and the tracker is untouched, so the next tick re-produces this regular as a fresh unit.
- No game screen was ever read and no game input was dispatched. Every screen-capture attempt failed with the same device-channel error, "Failed to start stream due to audio/video capture failure": five attempts across two computer sessions (cc-471: activate, observe, activate again; cc-472: activate, observe in image mode). The Mac mini was online and the LastWar window was running fullscreen (pid 59735, 1920x1080, window "Last War").
- No blind taps were made: without a single screenshot the gate line could not be grounded, so no game input was sent and no game state was changed. The pass stopped after this unit rather than failing further units identically, since every further unit needs the same capture channel.
- Recurrence, not a new failure class: this is the tenth consecutive ticker pass to fail on this exact blocker (ticker-1224 help 1235, ticker-1327 mail 1333, ticker-1340 star-ceremony 1344, ticker-1404 train 1404, ticker-1434 passes 1434, ticker-1504 donations 1504, ticker-1534 radar 1534, ticker-1604 arms-race 1604, ticker-1634 harvest 1634, ticker-1704 survivors 1707), now across ten activities. The blocker is filed as Issue #284 (tooling, filed by the ticker-1340 pass) alongside the knowledge Issue #282 filed by the 1332 organizer run; this pass commented on #284 (comment 6646759476) instead of filing a duplicate, and this run comments the ninth and tenth occurrences onto #282.
- Reading warning: this failed unit gives zero evidence about the survivor line state. It must NOT be read as "no survivors waiting" - the 1122 close (gate line verified live with 3 question-mark survivors, taps-not-opening-cards blocker) rests on a live read and stands as the last live read; this unit rests on no read at all. The 1122 follow-up (try the question-mark bubble itself in fullscreen, or a long-press on a grounded figure, re-grounded from a fresh screenshot immediately before tapping) is carried forward, not closed.
- Follow-up, carried forward: the blocker is now ten passes old and needs an owner-side or Mac-side fix (screen recording permission or capture pipeline restart on the Mac mini); ticker passes cannot work around it without an observation channel. No new issue filed: Issue #284 already tracks it and was commented.

## What the 2026-11-04 2135 unit added - screen-capture failure, next consecutive pass after 2104, nothing read

- Unit survivors-2026-11-04-1803 by ticker-2134, about 21:35 to 21:36 local, status failed. Evidence in `_records_/2026-11-04/survivor-intake/2135-queue-run.md`. No survivor was recruited, no card was opened, Quick Dispatch did not run, and the tracker is untouched, so the next tick re-produces this regular as a fresh unit.
- No game screen was ever read and no game input was dispatched. Every screen-capture attempt failed with the same device-channel error, "Failed to start stream due to audio/video capture failure": five attempts across two computer sessions (cc-488, cc-489) - computer.observe compact twice, computer.observe image once, computer.control activate twice - and a session restart did not clear it. The Mac mini was online and the LastWar window was running fullscreen (pid 59735, 1920x1080), Google Chrome frontmost.
- No blind taps were made: without a single screenshot the gate line could not be verified, so no game input was sent and no game state was changed. The pass stopped after this unit rather than failing further units identically, since every further unit needs the same capture channel.
- Recurrence, not a new failure class: this is the next consecutive ticker pass to fail on this exact blocker after ticker-2104. The blocker is filed as Issue #284 (tooling, filed by the ticker-1340 pass) alongside the knowledge Issue #282 filed by the 1332 organizer run; this pass commented on #284 instead of filing a duplicate, and this run comments this occurrence onto #282.
- Reading warning: this failed unit gives zero evidence about the survivor line state. It must NOT be read as "no survivors waiting" - the 1122 close (gate line verified live with 3 question-mark survivors, taps-not-opening-cards blocker) rests on a live read and stands as the last live read; this unit rests on no read at all. The 1122 follow-up (try the question-mark bubble itself in fullscreen, or a long-press on a grounded figure, re-grounded from a fresh screenshot immediately before tapping) is carried forward, not closed.
- Follow-up, carried forward: the blocker needs an owner-side or Mac-side fix (screen recording permission or capture pipeline restart on the Mac mini); ticker passes cannot work around it without an observation channel. No new issue filed: Issue #284 already tracks it and was commented.

## What the 2026-11-05 0134 unit added - screen-capture failure, twenty-sixth consecutive pass, windowed on an inactive Space (not fullscreen)

- Unit survivors-2026-11-04-2203 by ticker-0134, about 01:34 to 01:57 local, status failed. Evidence in `_records_/2026-11-05/survivor-intake/0134-queue-run.md`. No survivor was recruited, no card was opened, Quick Dispatch did not run, and the tracker is untouched, so the next tick re-produces this regular as a fresh unit.
- No game screen was ever read and no game input was dispatched. Every screen-capture attempt failed with the same device-channel error, "Failed to start stream due to audio/video capture failure": session cc-505 (fresh pivots after the 25 identical failures) - computer.observe compact twice, computer.control activate three times, open_app once, menu once - all with the same error wherever evidence was requested. The Mac mini was online and the device connection was healthy on both transports (native lastResponseAgeSeconds 0, web 4); this is not a connectivity problem and not an authorization problem (no "active on a different device" dialog appeared, no fresh login or verification code was demanded).
- New diagnosis, narrowing the fault - the game window is WINDOWED on an inactive Space, not in native fullscreen: list_windows with the correct app name "LastWar" (earlier passes used "Last War" and read 0 windows) confirms the window exists, 1920x1080 at (0,0), window_id 160366; a menu action on View failed with "Exit Full Screen" not there, and the error listed the View menu contents - Landscape Orientation, Portrait Orientation, Zoom to Fit, Enter Full Screen. "Enter Full Screen" being present means the app is NOT in native fullscreen. The capture failure is the pixel stream of an off-screen window, not a broken screen-recording permission: Chrome windows observe normally in the same sessions. open_app for LastWar returned outcome_unknown and a following list_windows showed the window unchanged.
- Background-sent Space keys do not switch Spaces: Ctrl+Right, Ctrl+Left and Ctrl+Up (Mission Control) all dispatched with input_dispatched true while Chrome was selected and observed, but the frontmost app stayed Chrome and the game window stayed off-screen after each. Computer control sends input in the background and never brings apps to the front, so system Space shortcuts do not fire from it. set_window_frame on the game window is gated by the stale-observation rule: it needs an observation_id from an observation of that window, which is exactly what the capture failure prevents, so no input was sent. inspect_menu for the Window menu failed with stale_observation: the app menu is not bound to the selected main window.
- Recurrence, not a new failure class: this is the twenty-sixth consecutive ticker pass to fail on this exact blocker (ticker-0104 at 01:04 was the twenty-fifth). The blocker is filed as Issue #284 (tooling, filed by the ticker-1340 pass) alongside the knowledge Issue #282 filed by the 1332 organizer run; this pass commented on #284 with this new diagnosis instead of filing a duplicate, and this run comments the twenty-sixth and twenty-seventh occurrences onto #282.
- CORRECTION - superseded claims: the "running fullscreen" wording in the 1707 and 2135 sections above, and the 1122 section's "window left in native fullscreen" carry-forward, are superseded by this on-screen read - the window is windowed on an inactive Space, and the "left in native fullscreen" state did not survive to this pass. The standing follow-up is corrected with it: the blocker is NOT a screen-recording permission or capture-pipeline fault (the pipeline observes Chrome normally), and the unblock is getting the window back onto the active Space - the owner clicking the LastWar Dock icon once is the known reliable step - or a control route that can switch Spaces, which the background channel does not have: no key, menu or frame action available to it moves the window across Spaces without a fresh observation of the window itself. The same correction is applied to the capture-failure sections of resource-collection, perception-scout, radar-tasks, arms-race and alliance-gifts in this run.
- Reading warning: this failed unit gives zero evidence about the survivor line state. It must NOT be read as "no survivors waiting" - the 1122 close (gate line verified live with 3 question-mark survivors, taps-not-opening-cards blocker) rests on a live read and stands as the last live read; this unit rests on no read at all. The 1122 follow-up (try the question-mark bubble itself, or a long-press on a freshly grounded figure, re-grounded from a fresh screenshot immediately before tapping) is carried forward, not closed - it now waits on the window returning to the active Space first.
- Follow-up, carried forward: the blocker is now twenty-six passes old and needs the window back on the active Space (owner Dock-icon click, the known reliable step); ticker passes cannot work around it without an observation channel. No new issue filed: Issue #284 already tracks it and was commented.
