---
title: Survivor Intake
created: 2026-10-25T21:55:00Z
modified: 2026-11-01T20:40:00Z
version: 1.8.0
description: Collecting the survivors who queue at the base front gate - recruit cards, dialog survivors and their building posts
grounded_in:
  - source: task named by the owner on 2026-10-25 - the line at the front door
  - source: in-game screens observed on the owner Mac mini, 2026-10-25
  - source: in-game screens observed on the owner Mac mini, 2026-11-01 (1017 survivors diagnostic unit)
  - source: in-game screens observed on the owner Mac mini, 2026-11-01 (1159 survivors unit)
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
