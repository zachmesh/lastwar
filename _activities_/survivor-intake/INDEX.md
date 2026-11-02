---
title: Survivor Intake
created: 2026-10-25T21:55:00Z
modified: 2026-11-02T11:34:36Z
version: 1.12.0
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


## Open questions

- Where the Factory building sits on the base, so the Mechanic
  post can be verified after intake.
- How fast the line refills and whether it has a cap.
- Whether a recruit can be moved to a different building by hand,
  and what the second David means - names repeat across roles.
- The three document icon bubbles over the headquarters area
  buildings open the Status Overview when tapped - what they are
  is unconfirmed; they are not collected like output bubbles.

## Changelog

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
