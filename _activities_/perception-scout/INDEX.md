---
title: Perception Scout
created: 2026-11-01T05:10:00Z
modified: 2026-11-03T17:40:00Z
level: L1
version: 1.11.0
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
  - source: ticker-1755 perception-scout execution record 2026-11-02 1801 queue run (alliance group partial, stale chain spent)
  - source: ticker-0004 perception-scout execution record 2026-11-03 0016 queue run (base group partial, power 149,940,141)
  - source: ticker-0134 perception-scout execution record 2026-11-03 0136 queue run (alliance group remainder partial, Wars dot filed as Issue #212)
  - source: ticker-0434 perception-scout execution record 2026-11-03 0446 queue run (partial, alliance remainder walked, grounded taps, Wars tabs empty, Issue #212 open)
  - source: ticker-0504 perception-scout execution records 2026-11-03 0508 and 0510 queue runs (partial, observe-only, store-group re-walk, Mall 7-tab strip identical, MALL label static, no Crystal Shop or Glittering Market tab)
  - source: ticker-0834 perception-scout execution record 2026-11-03 0839 queue run (partial, base and events groups, Drone Boost 9300, Wanted Boss Code 64, no Zombie entry)
  - source: ticker-0904 perception-scout execution record 2026-11-03 0910 queue run (partial, alliance group, stale 11-02 post-reset unit executed, Wars dot still open on Issue #212, OCR-row grounding lesson)
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

## What the 2026-11-02 1801 unit added

- Unit scout-midday-scout-mid-2026-10-31-002 by ticker-1755,
  session about 17:58 to 18:01, status partial, observe-only:
  the alliance group only (base, Alliance panel, Alliance
  Wars, Alliance Gifts). Evidence in
  `_records_/2026-11-02/perception-scout/1801-queue-run.md`
  and the appended 2026-11-02 observation sections. This is
  a stale-chain unit executed late in the current reset day,
  following the ticker-0434 and ticker-0534 precedent:
  observations are filed under 2026-11-02 as reads of the
  current game state, not of the old midday window.
- Base screen and HUD, read live about 17:58: HUD top row
  387.7M, 577.5M, 54.0M; second row 20.1M, 1.5M, 11.72K;
  stamina 120; shield-icon figure 146,610,448 displayed,
  identity not verified (see the exclusion below). Left
  column: hammer 2/4, flask 2/2, radio badge 4 (was 3 at
  13:53), truck, question-mark icon, backpack 8. Weather
  widget 6.5C. Right column: Events with no red badge
  visible, Capitol, VS timer 00:02:58, Season II badge 1,
  Alliance with no red dot visible in this capture, Mail
  with no dot visible, Inventory with a 1d 21:28:04 timer.
  Bottom: HEROES, chat ticker, 99+ badge, WORLD. A 13d
  00:02:58 timer shown near Season II - meaning not
  verified by opening.
- Resource bubbles standing on many buildings, observed
  only, not collected; the harvest regular owns collection
  and its 1803 unit was already queued.
- Furnace toast again: "High-temp Furnace total overdrive
  time (in sec) [22/60]" - fourth sighting in this record
  series, still unexplained, furnace observed only, never
  switched on or off, a red-line surface.
- Alliance panel read about 17:59 to 18:01: [AP3x] The
  Apex, Overall Rating 5.0, Leader Abuss Apex, Members
  94/100, Language English. Alliance Power read
  12,873,290,481 on the first panel capture and
  12,900,451,256 on the second capture about two minutes
  later - both recorded as displayed; the change is
  unexplained (live member power movement is possible,
  read variance is possible) and is not asserted either
  way. Panel red dots, six: Help, Alliance Gifts,
  Alliance Store, Alliance Techs, Alliance Events,
  Alliance City. No dot on Alliance Wars, Members,
  Assemble or Strength Ranking. Bottom row: Record,
  Applicants, Alliance Star, Settings - none opened this
  unit. Transient toast on panel entry: "Achievements
  8/16 Completed" - recorded as seen only; no achievement
  surface was opened. Base Alliance icon showed no red
  dot in the entry capture while the panel carries six
  dots - recorded as a visibility difference in this
  capture, not as the dots being cleared.
- Tap grounding, corrected and then superseded in the
  same pass: a tap aimed at Alliance Gifts at norm
  327,542 opened Alliance Wars instead, and a tap at norm
  327,633 opened Alliance Gifts, which first suggested a
  plus-90-in-y correction (buttons sit lower in tap terms
  than screenshots suggest). That correction is
  SUPERSEDED by the same pass's donations unit: measured
  grounding boxes on the panel capture give Help centre
  687,500, Wars centre 313,500, Techs centre 687,672,
  Strength centre 687,758, and taps at measured centres
  land exactly. Rule going forward: tap coordinates come
  from measured grounding boxes or OCR element positions
  in tap space, never from image-pixel conversion of a
  screenshot, which underestimates y by roughly 40 to 90
  norm units. The Help centre 686,531 recorded by the
  1741 help unit is consistent with the measured 687,500
  (inside the Help box 508-866, 465-536). Re-ground fresh
  every unit all the same.
- Alliance Wars page read (not the intended target):
  "There are no ongoing Alliance Wars currently."
  Individual Intel tab selected, one march intel row:
  [AP3x]Janet^A at X:478 Y:436 marching 00:01:15 toward
  [CHIA] TripleCs69 at X:468 Y:551. Rally Intel tab not
  selected. No rally joined.
- Alliance Gifts page read: Gift Level 28, progress
  181,429,280 of 206,300,000. Regular tab selected;
  Premium tab also carries a red dot. Banner: "Defeat the
  Doom Elite for a Regular Alliance Gift" with a Go
  button, not tapped. Gift rows, each +10 with a Claim
  button, none claimed (observe-only; the gifts regular
  owns claims): PrincessEsra10xoxo Defeated Doom Elite
  23:51:32; Niermeat 23:40:52; Niermeat 23:4x (third row
  partially obscured); Niermeat 23:28:11; further rows
  below the fold, not read. Claim All button badge 201,
  not tapped. (The counter rise since the 1215 gifts
  close is folded in alliance-gifts, Issue #183.)
- Red dot accounting: seen 10 badge signals (base radio
  4, Season II 1, backpack 8, 99+ badge; panel Help,
  Gifts, Store, Techs, Events, City dots). Explained 5,
  mapped to owning regulars with units already queued or
  in inbox: radio 4 and the panel Help dot to the help
  regular, Gifts dot to the gifts regular, Techs dot to
  the donations regular, Events dot to the events
  regular. Unexplained 5, carried: Season II badge 1,
  backpack 8, 99+ badge, panel Store dot (alliance shop
  surface; Buy never opened per the red line), panel City
  dot (owning regular not identified). Unknown items 3:
  furnace overdrive toast [22/60], the alliance Power
  figure change between two captures, the 146,610,448
  HUD figure identity - the last now partly resolved:
  the same pass's donations unit read own power
  149,311,528 (rank 31, unchanged from the 13:53 read),
  so the 146,610,448 figure is NOT account power; what it
  is remains unknown.
- unmatched_labels: none in the surfaces walked. No
  zombie sighting: this unit did not open the Events hub,
  so no Zombie Invasion return check was made; no zombie
  chain seeded, per the standing rule that the event ended
  2026-10-30 and no live return sighting exists in this
  pass.
- Outcome: partial (alliance group only). No successor
  unit is enqueued from this unit: the remaining groups of
  the current reset day belong to
  scout-midday-scout-mid-2026-11-02-001, already in inbox
  under chain scout-mid-2026-11-02; a stale-chain
  successor would duplicate it. The
  scout-mid-2026-10-31 chain is spent with this unit.
- Persistence note for the open questions below:
  Season II badge 1 is still unexplained at this read,
  the furnace toast [22/60] is now on its fourth sighting,
  and the Store and City panel dots are still unexplained;
  none is closed on silence.

## What the 2026-11-03 0016 unit added - base group partial, power up, successor chain

- Unit scout-2026-11-02-1900 by ticker-0004, session
  about 00:16 to 00:19 local, status partial: only the
  scout-base group was walked inside this unit; the
  events, store and alliance groups are unwalked and
  carried to the successor unit in chain
  scout-2026-11-02, so the tracker is left untouched.
  Observe-only throughout: nothing claimed, fought,
  dispatched, donated, dug or bought. Evidence in
  `_records_/2026-11-03/perception-scout/0016-queue-run.md`
  and the day observation file
  `_records_/2026-11-03/perception-scout/observation.md`.
- Base screen and HUD, read live about 00:17 local:
  power 149,940,141 (was 149,311,528 at the
  2026-11-02 13:56 read); HUD top row food 230.7M,
  iron 565.3M, coin 5.9M; second row 18.7M, 505.1K;
  12.72K with a plus button; cart 2,831.
- Left column: avatar Lv.30, hammer 2/4, flask 2/2,
  green face, robot head, white truck, wrench,
  megaphone badge 11, yellow radio; weather 6.5C.
- Right column: Events with no red badge visible,
  Capitol, VS timer 17:43:17, a second timer
  12d 17:43:17, Alliance with a red dot, Mail,
  Inventory.
- Bottom: HEROES, chat ticker, 99+ badge, WORLD.
  Timers as read, not interpreted: the two 17:43:17
  readings are reported as displayed.
- Resource bubbles on many buildings observed only,
  not collected. Furnace toast again: "High-temp
  Furnace total overdrive time (in ...", still
  unexplained, observed only - a further sighting
  past the fourth counted at 1801, carried, not
  closed on silence. Top banner partially visible
  ("Important: President Ab..."), not opened, not
  read in full.
- Red dot accounting: seen 3 badges (megaphone 11,
  Alliance dot, 99+ badge) plus 2 counters (hammer
  2/4, flask 2/2). Explained 0 within the base group
  alone; the badges map to owning groups this unit
  did not walk. Unexplained 3: megaphone 11,
  Alliance dot, 99+ badge. Unknown items: furnace
  overdrive toast, truncated President banner.
- unmatched_labels: none in the surfaces actually
  walked. No zombie sighting check was made in this
  unit (Events hub unwalked); no zombie chain seeded,
  per the standing rule that the event ended
  2026-10-30 and no live return sighting exists.
- Carried forward: successor unit enqueued in chain
  scout-2026-11-02 for the scout-events, scout-store
  and scout-alliance groups. Game left on the base
  screen.


## What the 2026-11-03 0136 unit added - alliance group remainder partial, Wars dot filed as Issue #212

- Ticker-0134, unit scout-midday-scout-mid-2026-10-31-002
  (record title run 0147), about 01:36 to 01:44 local, partial.
  Observe-only throughout: nothing claimed, fought, dispatched,
  donated, dug or bought; the Gifts Claim All button (badge 48)
  and every Claim button were observed only.
- Alliance panel, read live: [AP3x] The Apex, 5.0 stars,
  Leader Abŷss Apex, Power 13,009,089,868, Members 94/100,
  Language English. Motto: "We are The Apex. An alliance of
  veteran players. All are welcomed - messages sent in
  multiple languages." Top ticker partially read: "...talia
  as Secretary of Science!"
- Alliance Techs, War tab: Troop Movement 5/10, Rallied HP
  6/10, Rallied Attack 7/10, Rallied Defense 7/10, next tier
  1/10 (partially visible). Tech Donation Today 5100, with
  the note that at least 1000 contribution points earn the
  reward. Rallied Attack detail: 7/10, Tech EXP 10.2K/4.5M,
  Current +7%, Next Level +8%, Donation Reward 50/50,
  Donate buttons 0/0.
- Alliance Gifts, Regular tab: Level 28, progress
  183,423,470/206,300,000, Claim All badge 48, claimable
  gifts each +10 from "TheGoldenEclipse Defeated Doom
  Elite" with timers about 23:53 to 23:58. Premium tab: SSR
  and R purchase gifts - "Someone purchased Take All"
  (timers about 22:41 and 21:50), "Someone purchased
  Premium Training Pass", "Someone purchased Advanced
  Training...". Observed only.
- Alliance Store, Alliance tab, read-only (Buy never
  pressed): UR Hero Universal Shard SOLD, Survivor
  Recruitment Ticket SOLD, Violet Shard SOLD, Mason Shard
  30/30 at 1,000, Drone Parts SOLD, Lv.1 Drone Component
  Chest SOLD, Skill Chip Chest (SR), Drone Combat Boost
  EXP Card, 8-Hour Shield 7/7. Refreshes at 00:00 every
  Monday (server time), 5d 16:19 remaining at read time.
  Honor balance shown 193.1K.
- Base HUD totals during this session: food 230.7M, iron
  565.3M, coin 5.9M, 12.72K with a plus button, 193.1K,
  cart 2,831.
- Red dot accounting, resolving the 0016 unit's unexplained
  Alliance dot: seen 5 on the Alliance panel (Alliance Wars,
  Help, Alliance Gifts, Alliance Store, Alliance Techs);
  explained 4 (Help maps to help-2026-11-03-0230, already
  queued; Gifts maps to gifts-2026-11-03-0230, already
  queued; Techs maps to donations done today, 5100; Store
  maps to the read-only store state above). The Alliance
  dot seen on the base screen at 00:17 is therefore the
  aggregate of these five panel dots, not a sixth signal.
  Unexplained 1: the Alliance Wars dot. No regular owns
  the Alliance Wars entry - the duel-score regular reads
  the VS panel, a different surface - so it is filed as
  Issue #212 (label play) by the executor and carried
  here as an open question: route the entry to an
  existing regular or open it as a new candidate. The
  issue stays open; closure belongs to the daily retro,
  with evidence.
- Unknown item clarified, not closed: the cycling
  member-avatar badge that appears on dotted buttons
  (seen on Help, then on Alliance Wars) is a live
  member-activity indicator, not a separate signal.
- Tooling finding, session-specific: the Gifts, Store and
  panel X buttons responded to background taps, but the
  Help button (5 taps at 4 points), the Alliance Wars
  button (1 tap), the Alliance City button (1 tap) and
  the Alliance main panel back arrow (3 taps, including
  the recorded back point 82,930) did not change the
  screen in this session. This is NOT a standing block:
  ticker-1755 read Wars in its own pass, so the
  successor unit re-grounds these entry points fresh
  and, if they still do not respond, tries the
  foreground route before recording them unwalked again.
- Carried forward: successor unit
  scout-midday-scout-mid-2026-10-31-003 in chain
  scout-mid-2026-10-31 owns the remainder - Help,
  Alliance Wars and Alliance City sub-pages, the station
  panel train by train, mail (six categories), world map
  pins and the loot box. Game left on the Alliance main
  panel.
- Queue state note (process, not scout knowledge): this
  unit had already been completed in the delivered
  branch by ticker-1755 (evidence
  _records_/2026-11-02/perception-scout/1801-queue-run.md),
  so the delivered branch unit file was NOT overwritten
  and this pass stands as additional observation only.
  The pool divergence is filed as Issue #213 (label
  tooling, owned by lastwar-tool-developer, not
  duplicated here).


## What the 2026-11-03 0446 unit added

- Ticker-0434, unit scout-midday-scout-mid-2026-10-31-003,
  about 04:42 to 04:46 local, status partial, observe-only
  throughout: nothing claimed, fought, dispatched, donated,
  dug or bought. Evidence in
  `_records_/2026-11-03/perception-scout/0446-queue-run.md`.
  Walked: Help, Alliance Wars (both tabs), Alliance City
  (both tabs), the mail category list and one world map
  frame. Carried to successor unit 004: the station panel,
  the loot box and the individual mail category lists, so
  the tracker is left untouched.
- Tooling finding, mechanism established: the 0136 unit's
  Help, Wars and City buttons did not respond to
  background taps; in this session all three opened on
  the first tap at a freshly grounded point (Help
  (687,497), Wars (313,497), City (687,835)). The
  difference is grounding on the current screenshot, not
  a game-side block. The Alliance menu back arrow
  grounded at (162,935) and the Mail and sub-page back
  arrows at (62,951) all worked. This corroborates the
  donations re-ground-per-session rule: fresh grounding
  first, never a carried point.
- Alliance panel, read live: [AP3x] The Apex, 5.0 stars,
  Leader Abyss Apex, Power 13,016,623,359, Members 94/100,
  Language English. Top ticker partly read: "...pointed
  DR.POO as Secretary of Development!"
- Alliance Techs tree (already open from the previous unit
  in this pass): War tab Troop Movement 5/10, Rallied HP
  6/10, Rallied Attack 7/10, Rallied Defense 7/10, next
  node below 1/10. Tech Donation Today 6200 at close of
  the previous unit.
- Help panel: Today's points gained from Alliance Help
  1,240/1,000, already over the 1,000 gate. Four Bears
  Lair requests, all 30/30: building Lv.27 Drill Ground,
  building Lv.30 Aircraft Center, Morale research,
  Precision Targeting II research (fourth row partly cut
  off). Help All button present, observed only, not
  tapped. The Help dot maps to the help regular (already
  queued) with nothing new to claim in this walk.
- Alliance Wars: Rally Intel tab reads "No Alliance Rally
  currently." Individual Intel tab reads "There are no
  ongoing Alliance Wars currently." No rally, no war, no
  action available on either tab, so the Wars dot
  (Issue #212) is not explained by a live Wars action; it
  reads as the cycling member-activity indicator noted in
  the 0136 unit, or a stale badge. Left open on Issue
  #212, not closed by this unit.
- Alliance City: City List, Produces Rare Soil tab:
  Production Rate 5.88K/h, Captured Cities 6/6. Fully
  visible cities: Lv.6 X:499 Y:411 +1,000/h, Lv.5 X:336
  Y:411 +900/h, Lv.5 X:587 Y:336 +900/h, Lv.5 X:411 Y:336
  +900/h, Lv.4 X:499 Y:262 +800/h, Lv.4 X:336 Y:262
  +800/h, with a third row (Lv.6, Lv.6, Lv.5) cut off at
  the bottom of the frame. Produces Coal tab: Production
  Rate 13.53K/h, Digging Strongholds captured 4/4. Cities:
  Lv.6 X:587 Y:411 +3,456/h, Lv.6 X:411 Y:411 +3,456/h,
  Lv.5 X:662 Y:336 +3,312/h, Lv.5 X:336 Y:336 +3,312/h.
  Footer on both tabs: Server Time 2026-11-3 10:44 (as
  displayed), Digging Stronghold captures left today 2/2,
  War declarations left today 2/2. City Buff button and
  the Coal tab Claim All button observed only, never
  tapped.
- Mail list, opened from the base screen on a grounded tap
  at (931,777): categories Battle Report, Alliance, Event
  (red dot), Season, System (red dot), Regular, In-app
  Purchases. Footer: "Mails older than 30 days will be
  automatically deleted." No category list was opened and
  nothing was claimed or deleted; Delete All was never
  tapped. The (931,777) Mail grounding corroborates the
  0441 donations entry correction and Issue #220. Event
  and System dots map to the mail regular (already
  queued); no claim state is recorded for them.
- World map, one frame centred on alliance territory:
  Glacial Area -10C, [AP3x] The Apex member bases
  clustered, March Queues 0/4, no squad out. No zombie pin
  and no loot box pin visible in this frame. The furnace
  toast ("High-temp Furnace total overdrive time") recurs
  at the bottom, observed only.
- Base HUD totals as displayed during this session: food
  230.7M, iron 565.3M, coin 5.9M, 12.72K with a plus
  button, 193.9K to 194.5K honor, cart 2,836, account
  power 149,940,141.
- Unexplained in this walk: the station panel and the loot
  box were not located, so any signal they carry is still
  unknown. unmatched_labels: none in the surfaces actually
  walked. Game left on the base screen.


## What the 2026-11-03 0508 and 0510 units added

- Ticker-0504, units scout-midday-scout-mid-2026-11-02-002
  (about 05:05 to 05:08 local) and
  scout-scout-2026-11-02-002 (about 05:09 to 05:10
  local), both status partial, observe-only throughout:
  nothing claimed, fought, dispatched, donated, signed
  up for, or bought, and no price tag was tapped.
  Evidence in
  `_records_/2026-11-03/perception-scout/0508-queue-run.md`
  and `_records_/2026-11-03/perception-scout/0510-queue-run.md`.
  The 0508 unit is the stale chain remainder of the
  2026-11-02 midday pass and the 0510 unit the
  post-reset pass for the reset day started 2026-11-02
  19:00; the store group is now walked for both passes
  and the alliance group is carried to the successor
  units 003. Both units close partial with blocker
  category h (by-design chain continuation), not as a
  miss, and the observations were appended to the
  2026-11-02 observation file.
- Base screen, read live in both units: account power
  149,940,141, unchanged from the 0410 read and
  unchanged between the two units minutes apart. HUD
  totals as displayed: top row 230.7M, 565.3M, 5.9M;
  second row 19.0M, 505.1K, diamonds 12.72K; cart 2,836.
  Left column: hammer 2/4, flask 2/2, backpack 11,
  weather widget 6.5C. Right column: Events badge 1,
  Capitol, VS timer 12:54:01 falling to 12:50:25, Season
  II timer 12d 12:54:01 falling to 12d 12:50:25, Alliance,
  Mail, Inventory. Bottom: 99+ badge, HEROES, WORLD.
  Furnace toast again, value unchanged: "High-temp
  Furnace total overdrive time (in sec) [22/60]", still
  unexplained, red-line surface observed only. No
  "active on a different device" dialog appeared.
- Store (Mall), walked live in both units: the cart icon
  at the top right of the base screen, re-grounded fresh
  in each unit, opened the Mall on its HOT DEALS section
  on the first tap, centre [910, 68] in 0508 and [872,
  48] in 0510. The cart grounding varies per session;
  every unit re-grounds on its own capture. Tab strip
  verified at both ends in both units; full strip, 7
  tabs: Official Event, Weekly Deal, Super Monthly
  Pass, Weekly Pass, Diamond, Gold Brick Mall, Hot Sale
  Packs. Identical in both walks minutes apart and
  identical to the 2026-11-02 store walk. No Glittering
  Market tab and no Crystal Shop tab. No red dot on any
  tab. Observation only for Issue #128: the tabs behind
  its unclaimed priority-1 units are absent from the
  Mall strip as walked; the issue stays open for the
  daily retro and is not resolved by this observation.
- Check-in banner (Official Event page): "Participate
  in the check-in event and claim great rewards!" with
  FREE GIFT "Claim your gift today!" and a FREE
  TOMORROW row (x5, x5, x5, "Randomly obtain one").
  Observed only, not claimed; belongs to the
  shop-claims regular to verify.
- Gold Brick Mall, opened by tab tap only: banner "Gold
  Brick Mall Extra 5% Bonus". Packs shown, no price
  tapped: x500 $4.99, x1000 $9.99, x50000 $499.9,
  x100000 $999.9, each with an Initial Buy Reward free
  gift (x500, x1000, x2500, x5000 respectively as
  displayed). No red dot on the tab.
- Hot Sale Packs, opened by tab tap only: empty state,
  a gift-box graphic with "Packs sold out". No offers
  listed, nothing tappable as a purchase.
- MALL top label: tapped twice, first at an estimated
  point [630, 68] and then at the visually grounded
  label centre [574, 60]; neither tap changed the page
  (rule R2: method ended after two no-change taps). The
  MALL label is recorded as a static screen title, not
  a separate section switch; no red dot or signal hides
  behind it.
- Tabs strip-verified only, not opened: Weekly Deal,
  Super Monthly Pass, Weekly Pass and Diamond were
  verified on the strip but not opened, the same scope
  as the 2026-11-02 store walk. All are paid pass or
  diamond sections with no red dot; opening them would
  add nothing to the observation beyond their labels.
- Red dot accounting for these units: seen in the store
  group 0, explained 0, unexplained 0. Not resolved by
  these units, carried by their owning groups: Season II
  badge 1, backpack 11, 99+ badge, the furnace toast
  (base group, already carried by unit 001).
  unmatched_labels: none in the surfaces walked.
- Tap-method notes (rule R2): strip drag from [550,
  120] to [200, 120] revealed the right end of the tab
  strip. Gold Brick Mall tab tap at [707, 128] and Hot
  Sale Packs tab tap at [909, 128] each opened its page
  on the first tap. These grounded points are for this
  base and Mall layout only; every unit re-grounds on
  its own capture.

## What the 2026-11-03 0839 and 0910 units added - base and events walk, alliance group with OCR-row grounding

- Ticker-0834, unit scout-midday-2026-11-03-0700 (chain
  head of the midday pass), about 08:39 local, status
  partial: the base screen and the Events hub (Arms Race
  and Wanted Boss tabs) were walked live; the Desert
  Battlefield and fourth Events tabs, the Alliance panel
  group, the store group, mail category lists and the
  world map frame for this pass are unwalked and carried
  to the successor unit in chain scout-mid-2026-11-03, so
  the tracker is left untouched. Evidence in
  `_records_/2026-11-03/perception-scout/0839-queue-run.md`.
  Observe-only throughout: nothing claimed, fought,
  dispatched, donated, dug or bought. The Wanted Boss Go
  button was observed only, never tapped; no Buy button
  was tapped.
- 0839 base screen, read live: account power 149,940,141,
  unchanged from the 0710 help read; food 240.3M, iron
  575.0M, coin 12.1M, second row 19.0M, 505.1K, 12.72K
  with a plus button, diamonds 2,836, stamina 120, March
  Queues 0/4. Left column badges: green face with a red
  badge 1 nearby, radar dish badge 11. Right column:
  Events red badge 1, Capitol, VS timer 09:21:09, second
  timer 12d 09:21:09, Season II icon, Alliance, Mail,
  Inventory. Bottom 99+ badge, target icon with red badge
  1 and a 00:00:52 countdown, furnace toast "High-temp
  Furnace total overdrive time (in sec)" again,
  unexplained red-line surface observed only.
- 0839 Events hub, read live: Arms Race phase Drone
  Boost, Contest Segment Lv.29-30, chest progress 0/2,
  star counter 0, time left 01:20:50, tier thresholds
  1,500, 10,000, 30,000, player row #2110 [AP3x]Bears
  Lair with 9,300 shown below the row - consistent with
  the 0808 events read folded in the 0832 run, not a new
  score. Wanted Boss tab: Code 64, appears at server
  time 00:00, Go timer 08:20:35, Missile Vehicle heroes
  deal 50 percent extra damage on the Wanted Boss,
  rewards for completing 1 attack listed (stamina 50 and
  four other items). No Zombie Invasion entry seen in
  the Events hub tabs walked, consistent with the event
  having ended 2026-10-30. Red dot accounting for the
  surfaces walked: 0 unexplained (Events badge 1 maps to
  the Wanted Boss dot and the Arms Race phase, radar 11
  to the radar surface, 99+ to chat/mail surfaces, the
  target-icon badge to the world-map rally surface).
- Ticker-0904, unit scout-scout-2026-11-02-003, about
  09:05 to 09:12 local, status partial (alliance group
  walked in part; the remainder is carried to the
  successor). Note on staleness: the 0834 pass left this
  unit unexecuted as a stale unit of the closed 2026-11-02
  post-reset pass. This pass executed it because the
  queue `next` pick returned it and it still yielded live
  reads (notably the 238 claimable Regular gifts); the
  remainder is carried to the successor per design
  section 13, and the planner or retro may expire the
  chain. Evidence in
  `_records_/2026-11-03/perception-scout/0910-queue-run.md`.
  Observe-only: nothing claimed, fought, dispatched,
  donated, signed up for, or bought. No price tag was
  tapped. The Help All button, the Gifts Claim and Claim
  All buttons, the Gifts Go buttons and the Techs
  donation controls were observed only, never tapped.
  Appended to the 2026-11-02 observation file.
- 0910 base screen, read live about 09:06 local: account
  power 149,940,141, unchanged from the 0839 read; HUD
  totals as displayed food 240.3M, iron 575.0M, coin
  12.1M, second row 19.0M, 505.1K, diamonds 12.72K with a
  plus button, stamina 120, cart 2,836. March Queues 0/4.
  Right column: Events badge 1, Capitol, VS timer
  08:53:52, Season II timer 12d 08:53:52, Alliance, Mail,
  Inventory. Bottom: 99+ badge, HEROES, chat ticker
  "Breaking News: Alliance War!", BASE, target icon with
  red badge 3 and a 00:00:31 countdown, radar badge 11
  on the left column. Furnace toast again: "High-temp
  Furnace total overdrive time (in sec) [22/60]", still
  unexplained, red-line surface observed only.
- 0910 Alliance panel, read live: entry by the Alliance
  icon on the base right column, re-grounded fresh on
  the screenshot (centre about [903,699]); the recorded
  (903,787) centre is Mail, not Alliance, as the
  donations unit already noted. Panel header: [AP3x] The
  Apex, 5.0 stars, Leader Abyss Apex, Power
  13,086,499,653 (up from 13,016,623,359 at the 0446
  read), Members 94/100, Language English. Motto
  unchanged, including the Korean line. Red dots on the
  panel: Alliance Wars, Help, Alliance Gifts, Alliance
  Techs. No dot on Alliance Store, Members, Assemble,
  Strength Ranking, Alliance Events or Alliance City
  (City button shown highlighted, as before). Footer:
  Record, Applicants, Alliance Star, Settings, all
  unwalked in this unit.
- 0910 Help, walked live: today's points gained from
  Alliance Help 1,240/1,000, over the gate, unchanged
  from 0446. Four Bears Lair requests, all 30/30: Morale
  research, Precision Targeting II research, building
  Lv.27 Drill Ground, building Lv.30 Aircraft Center.
  Help All button present, observed only, not tapped.
  The Help dot maps to the help regular (already queued);
  the owner's own requests are full and the daily points
  are over the gate, so nothing new to claim is recorded
  for this walk.
- 0910 Alliance Wars, walked live (both tabs): Rally
  Intel tab "No Alliance Rally currently."; Individual
  Intel tab "There are no ongoing Alliance Wars
  currently." Both tabs empty, as in 0446. The Wars dot
  is not explained by a live Wars action; it stays open
  on Issue #212 (cycling member-activity indicator or
  stale badge), not closed by this unit.
- 0910 Alliance Gifts and Techs, walked live: see the
  gifts profile for the 238 claimable Regular gifts and
  the 186,155,650 progress read, and the donations
  profile for the 6700 Tech Donation Today read. War
  tab levels identical to the 0446 read (Troop Movement
  5/10, Rallied HP 6/10, Rallied Attack 7/10, Rallied
  Defense 7/10, next node below 1/10 with its name cut
  off at the frame edge). Tech Donation Today 6700, up
  from 6200 at 0446; "Requires at least 1000
  contribution points to earn the reward". No separate
  claim button was visible on this tab. Top ticker,
  partially read: "President Abyss Apex appointed
  Mav6776 as Secretary of Development!" Development tab
  not opened, carried to successor.
- 0910 red dot accounting for this unit: seen on surfaces
  walked 5 (Help, Wars, Gifts panel, Premium tab,
  Techs); explained 3 (Help, Gifts Regular with 238
  claimable, Techs mapped to the donations regular);
  unexplained 2 (Wars dot, open on Issue #212; Premium
  tab dot, visible rows all Claimed and below-fold rows
  unverified). Carried unwalked, dots unknown:
  Development tab, Alliance Store, Members, Strength
  Ranking, Alliance Events, Record, Applicants, Alliance
  Star, Settings, the station panel and the loot box
  (both still unlocated since 0446). unmatched_labels:
  none in the surfaces walked.
- Tooling finding, ground alliance panel taps on the
  current OCR label rows, never on a screenshot estimate
  alone: the first Help tap at [730,455] produced no
  change, while the 0446 grounding [687,497] opened Help
  on the first tap. The Alliance panel button rows sit
  lower than a fresh screenshot estimate suggests: OCR
  label rows are 509, 595, 679, 766, 849, so a tap at
  [312,547] falls on the Wars button's lower area and
  opened Wars, while [303,595] opened Gifts. The Premium
  tab tap at [725,231] produced no change; the
  OCR-grounded [694,269] opened it. This repeats the
  0650 gifts lesson that eyeballed y estimates run low
  on this panel.


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
  decision, not a scout-unit decision. (2026-11-03 0910 update: a stale 11-02 post-reset scout unit DID execute when the queue `next` pick returned it and still yielded live reads, so execution of stale units is observed, not merely hypothesised; whether the planner or retro expires the chain is still open.)

- The 146,610,448 mid-HUD figure is NOT account power (donations 1810 unit: own power 149,311,528, rank 31, unchanged from the 13:53 read); what the figure is remains unknown.
