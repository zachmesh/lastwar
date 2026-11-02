---
title: Perception Scout
created: 2026-11-01T05:10:00Z
modified: 2026-11-02T22:43:53Z
level: L1
version: 1.5.0
description: The scout passes - walking the whole game interface to observe what is available to do, recording it as observed items, and handing the work to the owning regulars
status: active
grounded_in:
  - source: owner direction of 2026-10-31 - perceive the game first, see what is available, place it into the queue dynamically
  - source: perception-driven queue design in the local conventions
  - source: task unit queue design section 13
  - source: perception-scout execution record 2026-11-01 0215 PST, first day observation
  - source: perception-scout execution record 2026-11-01 1437 queue run
  - source: perception-scout execution records 2026-11-02 0436 0441 0514 queue runs
  - source: perception-scout execution record 2026-11-02 0539 queue run
  - source: ticker-1336 perception-scout execution record 2026-11-02 1357 queue run (base group partial)
---


# Perception scout

## What this activity is

The perception layer of the routine. A scout pass walks the
game interface systematically - base screen, HUD, Events hub,
Store by section, markets, alliance panel and station, mail,
duel and radar, world map, VIP, passes, daily missions - and
records what is actually available to do as structured observed
items. It exists because the miss audit of 2026-10-31 proved
that work no static model named was never done - the scout is
how the day finds out what it contains before the day is worked.

Executions are recorded in `_records_/<date>/perception-scout/`,
one observation file per reset day, appended to by every scout
unit of that day. The full design - traversal checklist,
completeness standard, observed items schema, diff rules - is
the [perception-driven queue](../../_conventions_/local-conventions/perception-driven-queue.md)
document in the local conventions. Section 13 of the task unit
queue design fixes the unit contract.

## The job

1. Walk the surface group the unit owns - scout-base,
   scout-events, scout-store or scout-alliance - opening every
   tab and sub-page in the traversal checklist, re-grounding
   entry points fresh.
2. Record every signal as an observed item in the day
   observation file - surface, label, state, deadline and value
   where visible, the owning regular or `new`, and the red-line
   check.
3. Close no signal on silence. Every red dot or badge resolves
   to an action or to a recorded reason. Unexplained red dots
   close the unit as partial and are named in the round summary.
4. Never do the work. A scout observes only - no claim, fight,
   dispatch, donation or purchase, and no map pin tap on a radar
   stack day. The work belongs to the owning regular own unit,
   produced or raised by the diff.
5. Append, never rewrite. The observation file is append-only
   inside its day - the midday pass adds its sections after the
   post-reset pass, it does not edit them.

## Cadence

Two passes per reset day, both regulars in _tools_/regulars.json -

- `scout` - the post-reset full pass, daily-reset cadence
  anchored at the 19:00 local reset.
- `scout-midday` - the midday full pass, daily-reset cadence
  anchored at 07:00 local, for state-dependent availability the
  morning cannot show.

Each pass is a homogeneous chain of scout units split by surface
group - the staged unit is the chain head, the executor extends
the chain under the queue chain rules.

## What is known from 2026-11-01

First day observation file, from the 0215 unit (ticker-0204,
unit scout-midday-2026-10-31-0700, group scout-base, status
partial). Evidence in `_records_/2026-11-01/perception-scout/`,
observation file plus queue-run file.

- Entry correction, rule R2 - the game was found open on the
  Secret Command Post Hidden Treasure screen, left there by an
  earlier unit, not on the base screen. Two taps near norm 83 to
  86,938 to 941 on the back arrow changed nothing; a third tap at
  norm 112,946, the centre of the blue arrow, returned to the
  base screen. The earlier points had clipped the overlapping
  portrait icon at the arrow left edge. The next unit re-grounds
  the back arrow at norm 112,946, not 83,938. The encountered
  Secret Command Post surface counts as encountered, not as a
  walked group.
- Base screen and HUD read live about 02:15 local - level 30,
  power 148,957,193 as displayed; HUD top row 289.2M, 477.2M,
  10.6M, 2,366 beside the cart icon; second row lightning 135
  and 11.72K with a plus button, labels for the second row not
  legible in the downscaled capture and recorded as displayed
  only, not asserted. Left column top to bottom - zombie face,
  train, truck, radio with red badge 4, magnifier, survivor
  portrait, building icon, HEROES button at the bottom. Right
  column - Halloween Check-In with a 7 badge, Events with an x2
  badge, Faction Duel, VS, Season II, Alliance with a red dot,
  Mail with a red dot, Inventory, BASE. Centre - base with
  aircraft, one building carrying a badge 5. Bottom - a NEW!
  speech bubble over a chest icon with a badge 3, unexplained
  in this unit, not opened.
- Red dot accounting - seen 7, explained 4, unexplained 3.
  Explained - radio badge 4 to the help regular, Mail dot to
  the mail regular, Events x2 to the events regular,
  Halloween Check-In 7 to the check-in surface, with help,
  mail and events units already queued for the current slots.
  Unexplained - Alliance dot, building badge 5, NEW! chest
  badge 3. Unknown items 2 - the furnace overdrive toast line
  ("Furnace total overdrive time (in sec)", furnace observed
  only, never touched, a red-line surface) and the exact
  resource labels of the second HUD row.
- Partial by design, not a failure - the unit cap of 15 minutes
  closed the group with the base screen and HUD read only.
  Unwalked and carried to the successor unit (chain
  scout-mid-2026-10-31) - scout-base remainder (building
  badges building by building, Armed Truck state, gate and
  wall signals, resource bubbles re-read) plus the
  scout-events, scout-store and scout-alliance groups in full.
  Result statistics as written - surfaces walked 1, items
  observed 12, red dots seen 7, explained 4, unexplained 3,
  unknown items 2, resources gained none, observation only.
- Cross-check inside the same pass - the Hidden Treasure read
  on entry matched the treasures unit of ticker-0136 exactly
  (M1 x13, M2 x11, M3 x0, M4 x9, M5 x0, M6 x4, M7 x13,
  chest 1 of 15), and the Rewards Preview panel was read only
  (single dig chest rates UR 10.0 percent, SSR 30.0 percent,
  SR 60.0 percent, panel closed with its X, nothing claimed).
  The treasure counts are therefore confirmed by two live reads
  the same morning; the dig odds confirm the hidden-treasures
  profile figure.
- Staged-unit filing question, left open for the queue rules,
  not decided by this unit - ticker-0136 deliberately left
  this unit unexecuted, reasoning its window belongs to the
  2026-10-31 reset day which closed at 19:00 on 2026-10-31,
  and that a pass then would append current-day observations
  to a closed day file. Ticker-0204 executed it anyway on a
  different filing ground - every observation in the unit is
  a 2026-11-01 early-hours live read, filed under 2026-11-01,
  not under the closed day. Whether stale staged scout units
  should execute or expire is a queue-rule question for the
  queue design owners, recorded here, not settled by a scout
  unit. Resource bubbles - none clearly standing on the base
  in this capture, recorded as none seen, not as none present.

## What the 2026-11-01 1437 unit added

Second base-group pass of the day (ticker-1434, unit
scout-2026-10-31-1900, group scout-base, status partial,
observe-only, nothing claimed). Evidence in
`_records_/2026-11-01/perception-scout/1437-queue-run.md`.

- Back-arrow correction, superseding the 0215 point - a tap
  at norm 112,946 did nothing in this window (it lands on
  the portrait icon overlapping the arrow left edge, not
  the arrow). The arrow was re-grounded by visual
  measurement at bbox x 105 to 222, y 917 to 977, centre
  norm 163,947, and that tap returned to the base screen
  at once. The 112,946 point worked at 02:15 and failed
  at 14:47, so no back-arrow point is standing - every
  unit re-grounds the arrow fresh by visual measurement,
  and 163,947 is the current measured point only, not a
  rule to inherit. This resolves the contradiction in
  favour of the newest verified record.
- Hidden Treasure read on entry, measured about 14:47
  local - treasure progress 2/15 (was 1/15 at the 02:15
  read), map pieces M1 x12, M2 x12, M3 x0, M4 x9, M5 x2,
  M6 x6, M7 x12. The change since 02:15 (M1 13 to 12,
  M2 11 to 12, M5 0 to 2, M6 4 to 6, M7 13 to 12,
  progress 1/15 to 2/15) is consistent with
  treasures-regular digs during the day. This unit dug
  nothing, so the change is not attributed to it.
- Base screen and HUD read live about 14:47 local -
  level 30, power 148,957,193 (unchanged from the 02:15
  read). Top row 312.5M, 500.5M, 22.7M; second row 18.3M,
  8.1K, 11.72K with a plus button; lightning stamina 120
  (was 135 at 02:15); cart 2,366 (unchanged). Left
  column top to bottom - green face icon 0C, radio with
  badge 3 (was 4), truck, magnifier, survivor portrait.
  Right column - home icon 780 km, Events with an x2
  badge, Faction Duel, VS, Season II, Alliance with a
  red dot, Mail with no dot visible in this capture,
  Inventory with a red dot, BASE. Bottom - HEROES,
  megaphone, chat ticker, a 99+ badge above the chat
  area. No building badge 5 and no NEW! chest badge 3
  were visible in this capture, unlike the 02:15 read.
  Recorded as not seen, not as claimed or cleared - the
  two badges stay unexplained, not closed.
- Red dot accounting - seen 5, explained 2, unexplained
  3. Explained - radio badge 3 to the help regular,
  Events x2 to the events regular, with units for both
  already queued for the current slots. Unexplained -
  Alliance dot (alliance group not walked), Inventory
  dot (store group not walked), 99+ badge (chat surface
  not walked). Unknown items carried - the furnace
  overdrive toast line, read again as "Furnace total
  overdrive time (in sec) [22/60]", still unexplained,
  furnace observed only, never switched on or off, a
  red-line surface; and the 780 km home icon meaning,
  Armed Truck state not verified this unit.
- Unwalked, carried to the successor - the scout-events
  group in full (Events hub tabs, duel page, Arms Race
  phase and score, radar), the scout-store group in
  full (Store sections, markets, VIP, passes, daily
  missions, Inventory red dot resolution), the
  scout-alliance group in full (alliance panel and
  station, Alliance dot resolution, 99+ badge
  resolution), and the scout-base remainder (building
  badges building by building, Armed Truck state
  verification, gate and wall signals, resource bubbles
  re-read). Unmatched labels - none in the surfaces
  actually walked; the roster-out scan covers only
  those surfaces, not the unwalked groups. A successor
  scout unit is enqueued for the scout-events group
  under chain scout-2026-10-31. The unit closes
  partial under the zero-unexplained-red-dots closing
  condition.
- The scout-diff outputs filed with this pass read zero
  items observed and zero candidates (see the 1532 run
  record) - they carry no profile knowledge and change
  nothing above; the learnings here come from the
  1437 queue-run record itself.


## What the 2026-11-02 0436 to 0514 units added

- Three scout units, all partial, all observe-only. Evidence in
  `_records_/2026-11-02/perception-scout/0436-queue-run.md`,
  `0441-queue-run.md`, `0514-queue-run.md` and the appended
  sections of `observation.md` for 2026-11-02.
- Slot note (0436) - unit scout-midday-2026-11-01-0700 was
  staged for the 2026-11-01 07:00 midday pass, in the reset day
  that ended 2026-11-01 19:00. It executed late, in the current
  reset day (started 2026-11-01 19:00), so its observation is
  filed in the 2026-11-02 observation file as a read of the
  current game state, not as a read of the old midday window.
  No successor scout unit is enqueued from this unit: the
  post-reset scout head for the current reset day,
  scout-2026-11-01-1900, is already in inbox and will walk the
  remaining groups; enqueuing another scout head would
  duplicate it under the (regular, planned_for) invariant. The
  same stale-chain shape recurs in the 0514 unit (chain
  scout-mid-2026-10-31, head staged 2026-10-31 07:00), which
  enqueues a successor for the alliance group only
  (scout-mid-2026-10-31-002 per the day INDEX).
- Base group (0436) - entry on the Secret Command Post Hidden
  Treasure map tab, read live on entry and matching the 0424
  treasures record exactly: treasure progress 2/15, M1 x13,
  M2 x14, M3 x0, M4 x9, M5 x3, M6 x6, M7 x13. Nothing dug. Back
  navigation: the verified back-arrow tap at norm 163,947
  returned to the base screen at once, confirming the 1437
  grounding again.
- Base HUD read live about 04:36 - account power 149,296,925
  (up from 148,957,193 at the 2026-11-01 14:47 read). Top row
  379.7M, 571.7M, 45.7M; second row power 149,296,925 and
  11.72K with a plus button; cart 2,526 (was 2,366). Left
  column: hammer 2/4, bottle 2/2, truck, radio badge 3,
  survivor portrait. Right column: Events badge 1 (was x2),
  Capitol, VS timer 13:23:53, Season II badge 1, Alliance,
  Mail, Inventory. Bottom: HEROES, chat ticker, 99+ badge,
  WORLD. Resource bubbles: many bubbles visible across the
  left and centre buildings (gold, food and iron bubbles on
  several buildings) - observed only, not collected; the
  harvest regular owns collection and its 0603 unit is already
  queued. Furnace toast again, unchanged: "Furnace total
  overdrive time (in sec) [22/60]". Still unexplained;
  furnace is a red-line surface, observed only. Chat ticker
  top line: a treasure-map congratulation line about digging
  up Golden Mobile Squad units; not attributed to this account
  in this read, recorded as seen only.
- Red dot accounting (0436) - seen 5 badge signals: radio 3,
  Events 1, Season II 1, 99+ badge, plus the Inventory panel
  (no dot verified in this capture - recorded as not seen, not
  as cleared). Explained 2: radio 3 maps to the help regular,
  Events 1 to the events regular; units for both are queued.
  Unexplained 3: Season II badge 1, 99+ badge, and the
  Alliance dot state (alliance group not walked). Unknown
  items carried: furnace overdrive toast, 780 km home icon
  meaning (not re-verified this unit). unmatched_labels: none
  in the surfaces actually walked. Unwalked, carried to the
  post-reset scout head: scout-events group in full,
  scout-store group in full, scout-alliance group in full,
  scout-base remainder.
- Events group (0441) - navigation: VIP screen back arrow at
  norm 162,935 returned to MY PROFILE, and the profile X at
  norm 849,47 returned to base. The base Events icon at norm
  895,142 (badge 1) opened the Events hub. The hub tab strip
  scrolls horizontally: a drag on the strip from norm 800,131
  to 300,131 revealed the Community tab; a drag back revealed
  the Arms Race tab. The strip's leftmost icon tab on entry
  was not separately labelled in captures; on entry the hub
  opened on the Arms Race page, and no page beyond the four
  named below was found.
- Events hub, all four named pages read live - Arms Race:
  current phase Hero Advancement, Contest Segment Lv.29-30,
  timer 01:20:18 remaining, personal score 40,500, rank #2110
  [AP3x]Bears Lair, chest thresholds 2,000 / 4,000 / 12,000
  shown. Observed only - the arms-race regular owns any tier
  work, and its 0603 unit is already queued. No tier claim
  state is asserted beyond the thresholds and score read. (The
  40,500 score matches the 0359 events unit read the same
  morning; no new score knowledge.) Desert Storm Battlefield:
  Registration ends in 2d 13:19:58, Task Force A and Task
  Force B shown, registration limited to Top 32 Power ranked
  Alliances. The Sign Up button was NOT tapped - signing up
  is an execution/alliance act, not observation. Wanted Boss:
  Code 87, appears at server time 00:00, Tank heroes deal 50%
  extra damage on the Wanted Boss, complete 1 attack rewards
  shown (items x6, x6, x6, 5m speedups x5, gem x10), Go button
  timer 12:19:47. The Go button was NOT tapped. Community:
  join-community text, 200 Diamonds visit bonus, 500 Diamonds
  Discord-link bonus after Headquarters Lv.8, the 500 shown as
  Claimed. No social link was tapped (external surfaces, out
  of scope).
- Red dot accounting (0441) - seen 3 badge signals in the hub:
  Arms Race dot, Wanted Boss dot, base Events badge 1.
  Explained 2, with the base badge as the hub-level roll-up of
  the two dots, so no unexplained hub dot remains; the unit
  still closes partial because the duel page and radar panel
  are unwalked. The radar panel is NOT walked here on purpose
  of scope, not by omission alone: on a release day the radar
  regular owns claims, and this scout unit claims nothing.
- Unwalked, carried (0441) - duel page (personal daily total,
  day target gap) and radar panel (task state, claim state,
  stack or release posture on this Radar Training release
  day), carried to scout-midday-2026-11-02-0700, already in
  inbox for the 07:00 pass; no duplicate scout unit is
  enqueued from this unit. Scout-store and scout-alliance
  groups are likewise still unwalked for this reset day and
  belong to that pass.
- Stale-chain remainder (0514) - events tab strip re-verified
  to both ends (Arms Race dot, Desert Battlefield, Wanted
  Boss dot, Community; no fifth page, no Glittering Market
  tab; the four pages were read in full by ticker-0434 at
  04:41 the same morning). Store Mall strip walked in full,
  both ends: Official Event, Weekly Deal, Super Monthly Pass,
  Weekly Pass, Diamond, Gold Brick Mall, Hot Sale Packs; no
  Glittering Market tab and no Crystal Shop tab. Gold Brick
  Mall, opened by tab tap only: paid gold-brick packs (4
  dollars 99 and up); no price tapped. Hot Deals check-in
  banner (FREE GIFT today, FREE TOMORROW row) observed, not
  claimed, left to the shop-claims regular to verify
  (transient same-day signal, not new shop knowledge - the
  banner itself is already in the shop-claims profile).
- Base remainder (0514) - resource bubbles ready on farms,
  iron, stone and gold buildings in both base views (harvest
  regular owns); alliance train visible in the panned view;
  Drill Ground Lv.27; furnace overdrive toast still showing;
  99+ badge still showing.
- Alliance group NOT walked (0514), R2 pivot - the right icon
  column (Events, Capitol, VS, Season II, Alliance, Mail,
  Inventory, WORLD) vanished from the base view after the
  first base pan of this pass and did not return after three
  recovery variants (pan down, pan up, idle wait). The
  Alliance panel entry was not reached and no alliance dot
  state was read. This is the R2 pivot point: method changed
  twice with no effect, so the group is carried, not forced.
  Successor chain unit enqueued for the alliance group only.
- Red dot accounting (0514) - seen 4: Arms Race dot, Wanted
  Boss dot, Season II 1, 99+ badge (base Events badge 1 is
  the roll-up of the two tab dots). Explained 2: the two tab
  dots map to the events and arms-race regulars, both already
  queued. Unexplained 2: Season II badge 1, 99+ badge.
  Unknown: furnace overdrive toast, alliance dot state.
  Observed items: 12.
- Back-arrow rule, strengthened by this window - the 163,947
  point now holds for the treasure-screen and Events-hub back
  arrows across the 1437, 0436 and 0441/0444 reads, but the
  Mission screen back arrow centres at 62,941 (crystal-shop
  0446 unit), where 101,941 and 163,947 both miss. No
  back-arrow point is standing across screens: every unit
  re-grounds the arrow fresh by visual measurement for the
  screen it is on. The 1437 "current measured point only, not
  a rule to inherit" wording is extended from one screen to
  all screens.


## What the 2026-11-02 0539 unit added

- Unit scout-scout-2026-10-31-001 by ticker-0534, session about
  05:35 to 05:39, status done, observe-only. This is the stale
  post-reset pass of 2026-10-31 executed late in the current
  reset day (started 2026-11-01 19:00); its sections land on
  the 2026-11-02 day file, following the ticker-0434 and
  ticker-0504 precedent for stale scout units. Evidence in
  `_records_/2026-11-02/perception-scout/0539-queue-run.md`
  and the appended 2026-11-02 observation sections.
- Entry recovery, rule R2 - the first tap at the 0441 grounding
  [895,142] landed on the Gold Tank building in the panned base
  view (its label appeared) instead of opening the hub, and the
  right UI column was not visible in that view. A tap on empty
  road at [400,700] deselected the building and restored the
  full base UI, after which the Events icon re-grounded at
  [935,168] (badge 1) opened the hub at once. Ground the Events
  icon on the current capture, never on a stale point, when the
  base view has panned.
- Hub entry state - the hub opened on the Community page, the
  page the 0514 pass left it on. A drag on the tab strip from
  [300,131] to [700,131] revealed the left end of the strip.
  The hub back arrow at [163,947] returned to the base screen
  at once, confirming the 1437 grounding again.
- Events hub, all four pages read live - Arms Race: current
  phase Hero Advancement, Contest Segment Lv.29-30, timer
  00:22:12 remaining, personal score 40,500, rank #2110
  [AP3x]Bears Lair, chest thresholds 2,000 / 4,000 / 12,000
  shown. Score and rank are unchanged from the 0441 read at
  04:41 the same morning; the timer is consistent with that
  read (01:20:18 then, about 58 minutes elapsed). Observed
  only - the arms-race regular owns any tier work, and its
  0603 unit is already queued. Desert Storm Battlefield:
  Registration ends in 2d 12:22:01, Task Force A and Task
  Force B shown, registration limited to Top 32 Power ranked
  Alliances. The Sign Up button was NOT tapped. Wanted Boss:
  Code 87, appears at server time 00:00, Tank heroes deal
  extra damage on the Wanted Boss, complete 1 attack rewards
  shown, Go timer 11:21:52. The Go button was NOT tapped.
  Community: join-community text, 200 Diamonds visit bonus,
  500 Diamonds Discord-link bonus after Headquarters Lv.8,
  the 500 shown as Claimed. No social link was tapped.
- Resolved unknown from 0441 - the tab-strip leftmost icon tab
  identity, left unlabelled by the 0441 unit, is Arms Race:
  the drag revealed its label in place, and tapping it opened
  the Arms Race page. Every hub label now matches the roster;
  no candidate filing arises from this.
- Tab strip verified at both ends: Arms Race (left end),
  Desert Storm Battlefield, Wanted Boss, Community (right
  end). There is no fifth page and no Zombie Invasion tab -
  the chain-close rule from unit 066 stands, and no fresh
  zombie chain is seeded.
- Red dot accounting - seen 3 badge signals: Arms Race tab
  dot, Wanted Boss tab dot, base Events badge 1. Explained 3
  in the roll-up sense: the two tab dots map to the arms-race
  and events regulars, both with units already queued
  (arms-race-2026-11-02-0603, events-2026-11-02-0657); the
  base Events badge 1 is the hub-level roll-up of the two
  dots, not an additional dot. Unexplained hub dots: none.
  Base-screen dots outside this unit's group (Season II
  badge 1, 99+ badge, furnace toast) are carried by the
  current day's scout pass, not by this unit.
- Unwalked, carried - none from this unit. No successor unit
  is enqueued from this unit: the remaining groups of the
  current reset day (scout-store, scout-alliance, duel page,
  radar panel) belong to scout-midday-2026-11-02-0700,
  already in inbox for the 07:00 pass; a stale-chain
  successor would duplicate it. The Oct31 post-reset chain
  is spent.


## What the 2026-11-02 1357 unit added

- Unit scout-midday-2026-11-02-0700 by ticker-1336,
  session about 13:51 to 13:54 by unit timestamps (the
  file name 1357 reflects the estimate at writing time;
  the base capture was read about 13:53, not 13:56),
  status partial: only the scout-base group was walked
  inside this unit; the events, store and alliance
  groups are unwalked and carried to the successor unit,
  so the tracker is left untouched. Evidence in
  `_records_/2026-11-02/perception-scout/1357-queue-run.md`
  and the appended 2026-11-02 observation sections.
- Base screen and HUD, read live about 13:53: account
  power 149,311,528 (was 149,296,925 at the 04:36 read);
  HUD top row 387.7M, 577.5M, 54.0M; second row 20.1M,
  1.5M, 11.72K with a plus button; cart 2,536; stamina
  120.
- Left column: hammer 2/4, flask 2/2, chat badge 2,
  truck, question-mark icon, backpack 8, hammer icon,
  vehicle icon; weather widget 6.5C. Right column:
  Events with no red badge visible (was badge 1 at
  04:36; the 12:34 events unit found nothing claimable,
  so the badge cleared with no claim in between -
  observed, not explained), Capitol, VS timer 04:07:34,
  Season II badge 1, Alliance, Mail, Inventory. Bottom:
  HEROES, chat ticker, 99+ badge, WORLD. Timers: 13d
  04:07:34 near Season II, 2d 01:32:41 near Inventory -
  meanings not verified by opening.
- Resource bubbles on many buildings observed only, not
  collected. Furnace toast again: "Furnace total
  overdrive time (in sec) [22/60]", still unexplained -
  third sighting, observed only.
- Red dot accounting: seen 4 badges (Season II 1, chat
  2, backpack 8, 99+) plus 2 counters (hammer 2/4, flask
  2/2). Explained 0 within the base group alone; the
  badges map to owning groups this unit did not walk,
  and none was resolved by opening its surface.
  Unexplained 4, carried to their owning groups.
  unmatched_labels: none in the surfaces walked.
- Outcome: partial (base group only). Successor unit
  scout-midday-scout-mid-2026-11-02-001 enqueued under
  chain scout-mid-2026-11-02 for the remaining groups.
  Production note: the staged head unit carried no chain
  id; the chain starts with the successor unit.
- Persistence note for the open questions below:
  Season II badge 1 is still unexplained at this read,
  and the furnace toast [22/60] is now on its third
  sighting; neither is closed on silence.

## Open questions

- Season II badge 1, seen in the 0436 and 0514 units of
  2026-11-02 and still unexplained, carried with the other
  unexplained dots above.

- The unexplained red dots as restated by the 1437 unit
  (Alliance dot seen again, Inventory dot, 99+ badge,
  plus building badge 5 and NEW! chest badge 3 not
  re-seen and not cleared) and the unknown items
  (furnace overdrive toast now reading [22/60], second
  HUD row labels, 780 km home icon meaning) - carried
  to the successor scout unit, not closed on silence.
- Whether stale staged scout units execute or expire - see the
  filing question in the 2026-11-01 section; a queue-rule
  decision, not a scout-unit decision.
