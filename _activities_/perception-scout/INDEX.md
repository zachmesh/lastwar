---
title: Perception Scout
created: 2026-11-01T05:10:00Z
modified: 2026-11-08T05:32:17Z
level: L1
version: 1.26.0
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
  - source: ticker-0934 perception-scout execution records 2026-11-03 0940 and 0949 queue runs (partial, stale alliance remainder chains, Wars dot live cause seen departing, Elite Exercise Commendation Notice, Issue #212)
  - source: ticker-1304 perception-scout execution records 2026-11-03 1309 and 1314 queue runs (partial, base group and alliance remainder, Wars dot clearing answered, store and techs re-read, Issue #212)
  - source: ticker-1334 perception-scout execution record 2026-11-03 1345 queue run (partial, LOOT box located, station preparation-only surface, Wars dot present again, Issue #212 open)
  - source: tool-development 2032 run (daily-reset UTC boundary fix, PR 249) and GitHub Issue #247 - scout post-reset anchor corrected to the 02:00 UTC boundary
  - source: ticker-0904 perception-scout execution records 2026-11-04 0906, 0911 and 0919 queue runs plus the 2026-11-04 observation file (base group x2, stale alliance remainder, Wars dot absent with no rally)
  - source: ticker-0104 perception-scout execution record 2026-11-05 0104 queue run (failed, Mac screen-capture failure on every attempt, no game screen read, no input dispatched, twenty-fifth consecutive ticker pass to fail this way, Issue 284)
  - source: ticker-0941 perception-scout execution record 2026-11-05 0941 queue run (failed, Mac device invoke channel stall, zero responses to any invoke, forty-first consecutive ticker pass with a Mac device-access blocker, confirms the worsened zero-response form first recorded by ticker-0904, Issue 284)
  - source: ticker-1234 perception-scout execution record 2026-11-05 1234 queue run (failed, Mac device offline, forty-sixth consecutive ticker pass to fail this way, seventh in the worsened zero-response form, Issue 284; last_seen 15:36:52Z stale about 5h, unchanged since the 1025 pass; four invokes, zero responses)
  - source: ticker-1304 perception-scout execution record 2026-11-05 1304 queue run (failed, Mac device offline, forty-seventh consecutive ticker pass to fail this way, eighth in the worsened zero-response form, Issue 284; last_seen 15:36:52Z stale about 5h35m, unchanged since the 1025 pass; five invokes, zero responses; records-branch pool is the authoritative pool)
  - source: ticker-1334 perception-scout execution record 2026-11-05 1334 queue run (failed, Mac device offline, forty-eighth consecutive ticker pass to fail this way, ninth in the worsened zero-response form, Issue 284; last_seen 15:36:52Z stale about 6h05m, unchanged since the 1025 pass; four invokes, zero responses; records-branch pool inbox 39, done 846)
  - source: ticker-1404 perception-scout execution record 2026-11-05 1404 queue run (failed, Mac device offline, forty-ninth consecutive ticker pass to fail this way, tenth in the worsened zero-response form, Issue 284; last_seen 15:36:52Z stale about 6h33m, identical to the 1334 reading 30 minutes earlier; four invokes, zero responses; records-branch pool inbox 42, done 850)
  - source: ticker-1834 perception-scout execution record 2026-11-05 1836 queue run (failed, Mac device offline, fifty-eighth consecutive ticker pass to fail this way, nineteenth in the worsened zero-response form, Issue 284; last_seen 15:36:52Z stale about 11h, unchanged since the 1025 pass, identical to the 1804 reading 30 minutes earlier; five invokes, zero responses; inbox 73, done 949 at sync time)
  - source: ticker-1704 perception-scout execution record 2026-11-06 1710 queue run (failed, Mac device offline, eighty-fourth consecutive ticker pass to fail this way, forty-fifth in the worsened zero-response form, Issue 284; last_seen 15:36:52Z stale about 33h33m, unchanged since the 1507, 1534, 1604 and 1634 passes; seven invokes, zero responses)
  - source: ticker-2104 perception-scout execution record 2026-11-07 2121 queue run (partial, alliance remainder walked observe-only, first live scout observation since the outage, Zombie Siege / Alliance Exercise new label filed as Issue #419, Applicants permission-gated, observation-file divergence Issue #415; record commit 31467b04cb on records/2026-11-07)
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
  anchored at the trade-day reset (02:00 UTC absolute
  boundary, about 18:00 PST now, 19:00 PDT before the
  DST end). Correction, 2026-11-03 2032: the standing
  19:00 local anchor is superseded - the 1846 live
  counters, the PR 243 duel-boundary fix and the PR 249
  daily-reset tool fix (regulars.py gated daily-reset
  regulars on a fixed 19:00 local wall time; now
  reset_utc 02:00) settle the boundary, and the tool's
  old fixed-19:00 gating is the cause of the stale
  anchor. Filed as Issue #247; this correction is the
  knowledge-page half of that issue, closure belongs
  to the daily retro.
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


## What the 2026-11-03 0940 and 0949 units added - alliance remainder chains, Wars dot cause seen live, Elite Exercise notice

- Ticker-0934, units scout-midday-scout-mid-2026-10-31-005
  (about 09:36 to 09:41 local, 0940 record) and
  scout-midday-scout-mid-2026-11-02-004 (about 09:42 to
  09:49 local, 0949 record), both status partial with
  blocker category h (by-design chain continuation),
  not misses. Note on staleness, in both units: the
  queue `next` pick returned these stale units of the
  closed 2026-10-31 and 2026-11-02 midday passes. They
  still yielded live reads, so they were executed
  rather than skipped; the planner or retro may
  expire the chains. Observe-only throughout: nothing
  claimed, fought, dispatched, donated, boarded, dug,
  joined or bought. Evidence in
  `_records_/2026-11-03/perception-scout/0940-queue-run.md`
  and
  `_records_/2026-11-03/perception-scout/0949-queue-run.md`.
- 0940 Alliance Techs detail, read live and closed
  without action: Rallied Attack 7/10, Tech EXP
  12.7K/4.5M, Current +7 percent, Next Level +8
  percent, Donation Reward 50 Tech EXP and 50 coin,
  Donation Count 1/30, Unlimited Attempts. Donate
  buttons (2 red gems and 800 coin) observed only,
  never tapped.
- 0940 Alliance panel, read live: [AP3x] The Apex,
  5.0 stars, Leader Abyss Apex, Power 13,085,838,780
  (down from 13,086,499,653 at the 0910 read),
  Members 94/100, Language English. The panel's other
  buttons were not re-walked in this unit; the 0910
  read stands for them.
- 0940 base screen, read live about 09:38 local:
  account power 149,940,141, unchanged from the 0910
  read; HUD totals food 240.3M, iron 575.0M, coin
  12.1M, second row 19.0M, 505.1K, diamonds 12.72K
  with a plus button, stamina 120, cart 2,836; March
  Queues 0/4. Right column: Events badge 1, Capitol,
  VS timer 08:22:43, Season II timer 12d 08:22:44,
  Alliance, Mail, Inventory. Target icon badge 1 with
  a recurring short countdown ticking 00:01:36,
  00:00:43, 00:00:05 and restarting at 00:01:00 and
  00:00:37 across views: a recurring short timer,
  still mapped to the world-map rally surface,
  unopened. Bottom: 99+ badge, HEROES, chat ticker
  "Breaking News: Alliance War!", BASE/WORLD toggle.
  Furnace toast again: "High-temp Furnace total
  overdrive time (in sec) [22/60]", still unexplained,
  red-line surface observed only. Resource bubbles
  visible on many own-base buildings, observed only,
  never collected: they belong to the harvest
  regular's unit. No "Boarding closes in" banner on
  any view in this unit. No device-takeover dialog,
  no Touch ID, no password used.
- 0940 station panel hunt, not located: the alliance
  panel carries no Station button, as the 0539 unit
  established; the station panel is the train station
  platform screen reached from the base, not an
  alliance panel entry. The left icon column on the
  base and territory views shows no train icon in
  this unit, consistent with the 0752 train-unit
  hypothesis that the icon appears only while a train
  is preparing. Drag pans across alliance territory
  and the own base (centre drags, and the BASE button
  at about [895,950] to centre the own base) showed
  no station building, no train, no carriage plus
  bubble, and no station countdown in any frame.
  Reading: with no boarding banner and no train icon,
  no train is preparing in this window, so the
  platform has no live train state to read; the
  platform screen itself remains unlocated. This
  stays carried, not closed.
- 0940 world map frames, loot box not located: world
  map reached with the WORLD toggle at about
  [913,975]; the frame centres on the own base
  [AP3x]Bears Lair (blue crystal base) with alliance
  members around. A further pan right showed a red
  truck vehicle near [TSSU] Dwg0534, a blue dome
  structure with badge 12, and the chat ticker
  "[BIOd]Robertinho Supineiro dug up 1 Golden Mobile
  Squad with the treasure map": a treasure-map
  digging signal on the world map, recorded as an
  observed item pointing at world-map activity, never
  worked. No loot box pin was visible in either world
  map frame. The left-edge gift icon with badge 3
  seen in the 0539 frame was not re-sighted in these
  frames. No pin was tapped: on a stack day, pin
  tapping is an execution act, not perception.
  Reading: the loot box stays unlocated and stays
  carried, not closed.
- 0940 tooling finding - grounded taps: a click
  without a fresh observation_id is rejected
  (stale_observation); an image-only observation does
  not attach its id for the next control call. Take a
  compact observation first, then click with that
  observation_id. Inner Tech detail closes at about
  [818,225], outer Alliance Techs panel at about
  [818,150], alliance panel back arrow at about
  [115,936]. The BASE/WORLD toggle sits at about
  [895,950] (BASE) and [913,975] (WORLD); it centres
  the own base and opens the world map respectively.
  Drag pans move the camera but ground taps in
  alliance territory risk opening player profile cards
  (0752 lesson); this unit used drags only, no ground
  taps, and opened no card.
- 0949 Alliance panel, read live: [AP3x] The Apex,
  5.0 stars, Leader Abyss Apex, Power 13,085,838,780
  (same as the 0940 read), Members 94/100, Language
  English, motto unchanged including the Korean line.
  Red dots on the panel: Alliance Wars, Help,
  Alliance Gifts, Alliance Techs. No dot on Alliance
  Store, Members, Assemble, Strength Ranking,
  Alliance Events or Alliance City (City button shown
  highlighted, as before). Top ticker, partially read:
  "President Abyss Apex appointed ...scott as
  Secretary of Interior!"
- 0949 Alliance Wars, walked live (both tabs) - the
  dot's live cause seen directly: Rally Intel tab,
  first sight, a LIVE rally - [AP3x]Krazy Sully,
  "Rallying... 00:00:30", target Lv.40 Doom Elite,
  24km away, Attack button, four empty join slots,
  Count/Limit (1/5). The join slots were observed
  only; joining is not scout work and no slot was
  tapped. Under a minute later the same tab read "No
  Alliance Rally currently.": the rally had departed
  while it was being watched. Individual Intel tab:
  "There are no ongoing Alliance Wars currently.", as
  in 0910. Reading: the Wars dot maps to a live rally
  when one is running. This walk caught the dot's
  live cause directly, where 0910 saw both tabs empty
  and left the dot open on Issue #212. The dot is
  still not closed here: after the rally departed,
  whether the dot clears with it was not re-read on
  the panel. Commented on Issue #212 with this
  evidence by the executor.
- 0949 Strength Ranking, walked live (Power tab
  only): 1 ItStartsWithaDream (R4) 270,322,299;
  2 Abyss Apex (R5) 248,620,590; 3 StarFall (R4)
  207,866,377; 4 Missile Apex (R3) 203,332,272;
  5 papillon707 (R3) 203,299,470; 6 Echo Apex (R3)
  196,836,790. Own row pinned at the foot: 31 Bears
  Lair (R3) 149,940,141. Kills and Donation tabs not
  opened, carried to successor.
- 0949 Members, walked live (list head only): online
  count 15. Leader R5 Abyss Apex. Officer row:
  Warlord ItStartsWithaDream, Recruiter KAGE OG, Muse
  StarFall, Butler KillerInstinct14. Search for
  Members field, observed only. Groups: R4 The
  elected 1/10 (collapsed), R3 Armed Guards 10/58
  (expanded). Visible Armed Guards rows, all Online,
  Lv.30, Manage buttons observed only: QueenSTX Apex
  109.6M, Missile Apex 203.3M, RoadHouse54 140.1M,
  ArmyLucas 115.0M. Rows below the fold not verified.
- 0949 Alliance City, walked live (Rare Soil tab
  only): Production Rate 5.88K/h, Captured Cities
  6/6. Visible Rare Soil cities: Lv.6 X:499 Y:411
  +1,000/h; Lv.5 X:336 Y:411 +900/h; Lv.5 X:587 Y:336
  +900/h; Lv.5 X:411 Y:336 +900/h; Lv.4 X:499 Y:262
  +800/h; Lv.4 X:336 Y:262 +800/h. A further row
  (Lv.6, Lv.6, Lv.5) is below the fold, yields cut
  off. Footer: Server Time 2026-11-3 15:46:52 as
  displayed; Digging Stronghold captures left today
  2/2; War declarations left today 2/2; City Buff
  button observed only, never tapped. Produces Coal
  tab not opened, carried to successor.
- 0949 Alliance Events, walked live (Exercise card):
  Alliance Exercise: Battle Stage lasts 30 minutes,
  highest total Alliance damage earns massive rewards
  for all members; the Commander dealing the most
  damage has a chance to multiply all Alliance
  members' rewards by 10x; Offline Participation
  automatically joins allies' rallies against the
  Exercise monster when offline (if open slots remain
  20 seconds before departure). Preparing countdown
  05:12:34 at first sight, ticking; War Time Zone
  2026-11-3 15:00:00. Offline Participation checkbox
  already checked, observed only, never toggled.
  View, Rewards and Build buttons observed only,
  never tapped. Top ticker again: "...dug up 1 Golden
  Mobile Squad with the treasure map-congrats!",
  matching the 0940 record's treasure-map digging
  signal.
- 0949 Commendation Notice popup, left open: the
  Events page carried a "Tap to view message"
  envelope overlay. A tap meant for the page back
  arrow was consumed by the pending message and
  opened it instead of navigating back: a
  "Commendation Notice" popup reading, in full,
  "Dear Commander, We are pleased to inform you that
  thanks to your and your allies' remarkable
  performance and tireless dedication, your Alliance
  has unlocked Elite Exercise and can now challenge
  the new Level 11 and 12 difficulties! Tougher
  challenges bring better rewards! We look forward
  to witnessing your courage and strategy as you
  unite with your allies for even more glorious
  victories!" The popup's View button was NOT tapped
  in this unit: it navigates to the Exercise, which
  is not scout work. A dimmed-area tap and a repeat
  back-arrow tap both showed no change while the
  popup is modal (the control channel notes
  background clicks do not reach some controls). The
  popup was therefore left open on the Events page
  for the next unit to handle - the 1010 radar unit
  later navigated past it via View to the Exercise
  panel and backed out untouched, folded in the
  radar 1.20.0 entry. No Esc key was used: Esc
  crashes this app.
- 0949 Mail, not walked in this unit: the mail
  category lists were not opened before the unit cap.
  The Mail icon showed no red badge on the base views
  of this pass, so no new mail signal is recorded;
  the category lists stay carried. The 0539 mail read
  (Event dot = unread train mail, System dot =
  Planned Update Notice) stands as the last full read,
  and the mail regular is queued separately.
- Red dot accounting for the 0949 unit: seen on
  surfaces walked, Wars, Help, Gifts and Techs dots
  on the alliance panel. Explained: Wars maps to the
  live rally seen departing in this walk
  (dot-clearing after departure not re-read); Help
  maps to the help regular; Gifts maps to the gifts
  regular; Techs maps to the donations regular.
  Unexplained: 0 in the surfaces walked, with the
  standing open items below carried, not closed.
  Carried unwalked, dots unknown: mail category
  lists, City Produces Coal tab, Ranking Kills and
  Donation tabs, the station panel and the loot box
  (both covered in this pass's 0940 unit, still
  unlocated), and whether the Wars dot clears after
  a rally departs (2026-11-03 1314 update: answered, the dot clears when no rally is running; see the 1309 and 1314 section).
- Tooling finding - grounded taps: Alliance panel
  button rows ground at about 80 apart from the Wars
  anchor: Wars [312,547], Members [690,627],
  Strength Ranking [690,787], Alliance Events
  [310,867], Alliance City [690,867]. A
  visual-centre estimate alone misses: [310,468] did
  not open Wars, and [690,787] opens Strength
  Ranking, not City. Sub-page back arrows ground at
  about [117,948]; [62,950] misses left of the button
  on the Strength Ranking and Member List pages. A
  modal message popup swallows back-arrow and
  dimmed-area taps; only its own button responds.
  Do not use Esc on this app.
- Carried forward: successor unit enqueued in chain
  scout-mid-2026-11-02
  (scout-midday-scout-mid-2026-11-02-005) for the
  remainder: mail category lists, City Produces Coal
  tab, Ranking Kills and Donation tabs, the station
  panel and the loot box, and the Wars-dot-after-
  departure re-read. Successor unit enqueued in chain
  scout-mid-2026-10-31
  (scout-midday-scout-mid-2026-10-31-006) for the
  remainder: the station panel and the loot box.
- Issue #212: this unit's rally evidence was
  commented on the issue by the executor (live rally
  seen departing; dot cause observed directly). No
  issue is closed here - closure belongs to the daily
  retro, with evidence.

## What the 2026-11-03 1309 and 1314 units added - base group and alliance remainder, Wars dot clearing answered, store and techs re-read

- Units by ticker-1304, session cc-352, both
  observe-only, both partial with blocker category h
  (by-design chain continuation), not misses. Evidence
  in `_records_/2026-11-03/perception-scout/1309-queue-run.md`
  and `_records_/2026-11-03/perception-scout/1314-queue-run.md`.
  Nothing claimed, fought, dispatched, donated,
  collected, dug or bought; no price tag tapped.
- 1309, scout-base head unit of the fresh midday chain
  scout-mid-2026-11-03, about 13:05 to 13:09 local. Entry
  state: the game opened on the Secret Command Post
  panel, left there by the previous session, not on the
  base screen. Three back-arrow taps failed before the
  exit worked: taps at [86,907] and [86,862] and
  [62,951] left the panel unchanged (the first produced
  an Achievements 8/16 Completed toast at the top, no
  navigation). A visual-grounding point for the blue
  arrow button at [158,946] exited the panel at once to
  the base screen. Grounded point for this panel: back
  arrow [158,946], not the earlier estimates.
- 1309 secrets surface, read live at entry, observed
  only: Secret Command Post, Secret Mobile Squad tab:
  Assist Allies 5/5, Plunder Others 0/3, unchanged from
  the 0539 read today. Your Tasks, all Lv.5: UR Disrupt
  electric grid; SSR Search for Missing Refugees
  (PERFECT badge); SSR Provide Tech Support to Refugees
  (PERFECT badge); SSR Train Refugees (PERFECT badge).
  Hidden Treasures and Ghost Ops tabs not opened,
  carried to the secrets regular, not to this chain.
  Reading: the secrets state maps to the secrets
  regular, already queued for the 14:03 slot
  (secrets-2026-11-03-1457 in inbox). No new secrets
  signal beyond the standing state.
- 1309 base screen and HUD, read live about 13:09
  local: account power 149,948,901, up from 149,940,141
  at the 09:38 read today. HUD totals as displayed: top
  row food 240.3M, iron 575.0M, coin 12.1M; second row
  19.0M, 505.1K; power row 149,948,901, diamonds 12.72K
  with a plus button; cart 2,836. Left column: avatar
  Lv.30, stamina 120, hammer 2/4, flask 1/2 (was 2/2 at
  the 00:17 read), green face, white truck, wrench,
  megaphone-style radar icon badge 11, yellow radio;
  weather widget 6.5C. Right column: Events badge 1,
  Capitol, VS timer 04:51:03, Season II timer 12d
  04:51:04, target icon badge 1 with countdown 00:00:40,
  Alliance, Mail, Inventory. Bottom: HEROES, chat
  ticker, 99+ badge, WORLD. Resource bubbles visible on
  many left and centre buildings, observed only, not
  collected. Furnace toast again at the bottom:
  "High-temp Furnace total overdrive time (in ...",
  still unexplained, red-line surface observed only. No
  "Boarding closes in" banner on this view; no train
  icon in the left column; no station building in this
  frame. The station panel stays carried, consistent
  with the 0940 read.
- 1309 red dot accounting: seen 4 - Events badge 1,
  target-icon badge 1, radar badge 11, 99+ badge - plus
  2 counters (hammer 2/4, flask 1/2). Explained 4:
  Events maps to the events surface (events regular
  queued for 14:57); the target-icon badge 1 with its
  short recurring countdown maps to the world-map rally
  surface, unopened; the radar badge 11 maps to the
  radar regular; the 99+ badge maps to chat and mail
  surfaces. Unexplained red dots: 0 in the surfaces
  walked. Unknown items: the furnace overdrive toast
  (recurring, unexplained since 00:17 today), the flask
  1/2 change (a queue slot freed since 00:17, not a red
  dot). Carried unwalked: scout-events, scout-store and
  scout-alliance groups in full; the station panel and
  the loot box pin, both still unlocated (2026-11-03 1345 update: the loot box is located, see the 1345 section; the station panel stays carried as a preparation-only surface).
  unmatched_labels: none in the surfaces actually walked.
- 1314, scout-alliance remainder unit of the stale
  post-reset chain scout-2026-11-02, about 13:11 to
  13:14 local. Note on staleness: the queue `next` pick
  returned this stale unit of the closed 2026-11-02
  post-reset pass. It still yielded live reads, notably
  the Wars-dot clearing evidence and the first
  Development-tab read of this chain, so it was executed
  rather than skipped, as the 0949 unit did for the
  midday chain. The planner or retro may expire the
  chain.
- 1314 alliance panel, read live: [AP3x] The Apex, 5.0
  stars, Leader Abŷss Apex, Power 13,091,557,850 (up
  from 13,085,838,780 at the 09:42 read), Members 94/100,
  Language English, motto unchanged including the
  Korean line. Red dots on the panel: Help and Alliance
  Gifts only. No dot on Alliance Wars, Alliance Store,
  Members, Assemble, Strength Ranking, Alliance Events
  or Alliance City (City button shown highlighted, as
  before). Entry: Alliance icon re-grounded at [903,699]
  on the base screen, as in 0910.
- 1314 Wars dot clearing - the 0949 carried question
  answered: Alliance Wars, walked live (Rally Intel tab
  only), reads "No Alliance Rally currently."
  Individual Intel tab not opened. Reading: the Wars dot
  is gone from the panel at the same time the tab is
  empty. Combined with the 0949 read (a live rally
  departing mid-walk, dot still present then), this is
  the dot-clearing re-read that unit left open: the Wars
  dot clears when no rally is running. Commented on
  Issue #212 by the executor; this fold is commented
  there by this run. The dot is therefore explained,
  not merely observed. Join slots: none present while
  no rally runs; joining is not scout work in any case.
- 1314 Alliance Techs, walked live (both tabs): War tab:
  Troop Movement 5/10, Rallied HP 6/10, Rallied Attack
  7/10, Rallied Defense 7/10, next tier 1/10 partially
  visible, unchanged from the 01:40 read. Development
  tab, first read in this chain: Auto Rally Max Level,
  Quick Construction 8/10, Great Helper Max Level, next
  tier 2/10 partially visible. Tech Donation Today:
  8000, up from 6700 at the 09:06 read and 5100 at 01:40.
  Requires at least 1000 contribution points to earn
  the reward. Maps to the donations regular, queued for
  14:03. Techs closes at the panel X [838,150], as in
  0539. Donation controls observed only.
- 1314 Alliance Store, walked live (Alliance tab,
  read-only): Honor 199.2K, up from 193.1K at the 01:36
  read. UR Hero Universal Shard SOLD, Survivor
  Recruitment Ticket SOLD, Violet Shard SOLD, Mason
  Shard 30/30 at 1,000, Drone Parts SOLD, Lv.1 Drone
  Component Chest SOLD, Skill Chip Chest (SR), Drone
  Combat Boost EXP Card, 8-Hour Shield 7/7. Refreshes
  Monday 00:00 server time, 5d 04:45:22 remaining. State
  otherwise identical to the 01:36 read. No Buy button
  tapped, per the red line.
- 1314 red dot accounting: seen on surfaces walked:
  Help and Gifts dots on the alliance panel. Explained
  2: Help maps to the help regular; Gifts maps to the
  gifts regular. The absent Wars dot is explained above
  as the cleared state. Unexplained: 0 in the surfaces
  walked. Carried unwalked: Members, Strength Ranking
  (Kills and Donation tabs), Alliance Events, Record,
  Applicants, Alliance Star, Settings, the station panel
  and the loot box pin (2026-11-03 1345 update: loot box located, see the 1345 section). Note that Members, Strength
  Ranking (Power tab) and Alliance Events were walked
  today in the midday chains (0940 and 0949 records),
  so the successor need only re-read them if it wants
  this chain's own copy. unmatched_labels: none in the
  surfaces actually walked.
- Issue #212: the executor commented the Wars-dot
  clearing evidence; this fold is commented there by
  this run. No issue is closed here - closure belongs
  to the daily retro, with evidence.


## What the 2026-11-03 1345 unit added - LOOT box located, station panel is a preparation-only surface

- Unit scout-midday-scout-mid-2026-10-31-006 by
  ticker-1334, session cc-357, about 13:36 to 13:44
  local, status partial with blocker category h
  (by-design chain continuation), not a miss: the loot
  box is now located, and only the station panel
  remainder is carried to the successor. Observe-only;
  nothing claimed, fought, dispatched, donated,
  boarded, dug or bought; no price tag tapped. The
  Alliance Techs Donate buttons and the LOOT Claim All
  button were observed only, never tapped. No carriage
  plus bubble was tapped, so no boarding action was
  taken. No world map pin was tapped. Evidence in
  `_records_/2026-11-03/perception-scout/1345-queue-run.md`.
  Appended to the 2026-11-03 observation file.
- Alliance Techs, read live on entry from the previous
  unit's end state: Rallied Attack 7/10, Tech EXP
  14.0K/4.5M (up from 12.7K at the 0940 read,
  consistent with the 1322 donations unit landing 7
  coin donations today), Current +7%, Next Level +8%.
  Donation Reward 50 Tech EXP and 50 coin. Donation
  Count 1/30, Unlimited Attempts. Donate buttons: 2 red
  gems and 800 coin, observed only. This read
  corroborates the 1322 donations close (EXP 14.0K,
  count 1/30). Techs list, read live: War tab rows
  Troop Movement 5/10, Rallied HP 6/10, Rallied Attack
  7/10, Rallied Defense 7/10, next tier 1/10 partially
  visible. Tech Donation Today: 9000, up from 8000 at
  the 1314 read (alliance-wide footer; the rise is
  recorded, not attributed to any donor). Detail closed
  at [818,225], then the panel at [818,150].
- Alliance panel, read live: [AP3x] The Apex, 5.0
  stars, Leader Abŷss Apex, Power 13,091,657,850 (up
  from 13,091,557,850 at the 1314 read), Members 94/100,
  Language English. Red dots on the panel: Alliance
  Wars, Help, Alliance Gifts, Alliance Techs. No dot
  on Members, Alliance Store, Assemble, Strength
  Ranking, Alliance Events or Alliance City (City
  button shown highlighted, as before). No Station
  button on this panel, as established in 0539 and
  0940. Note: the Wars dot is present again here after
  its absence at 13:14; no rally was opened in this
  unit, so whether a rally is running is unverified -
  the clearing rule predicts one is, but that
  prediction is not verified by this read.
- Station panel hunt, changed method versus 0940
  (which used drag pans only): this unit closed the
  panels to a clean base view, screenshot-read the
  left icon column, and checked the two
  train-preparation signals before any pan. Base
  screen, read live about 13:40 local: account power
  149,948,901, HUD food 240.3M, iron 575.0M, coin
  12.1M, second row 19.0M, 505.1K, diamonds 12.72K,
  cart 2,836, stamina 120. Left icon column: avatar
  Lv.30, hammer 2/4, flask 1/2, green face, white
  truck, wrench, radar badge 11, yellow radio. No train
  icon in this frame. No "Boarding closes in" banner
  under the resource bar on the base view. Reading:
  with neither preparation signal present, no train is
  preparing in this window, so the STATION PLATFORM
  screen has no live state to read. The platform
  screen itself remains unlocated, and it is a
  preparation-only surface, not a standing panel: it
  can only be read when a train is preparing. This
  stays carried, not closed, and the successor should
  re-check the two preparation signals first rather
  than re-panning the base edge.
- LOOT box, LOCATED. Changed method versus 0940 and
  0539 (which only far-observed the left-edge gift
  icon): on the world map, centred on the own base
  [AP3x]Bears Lair with March Queues 0/4, one east
  drag pan, then a grounded tap on the left-edge gift
  icon at [311,237] opened the panel titled LOOT. That
  icon is the loot box. Claim All was observed only,
  never tapped, so the loot stays unclaimed for its
  owning regular. Panel title: LOOT, with an info
  button and an X close at about [818,216]. Three
  rows, all Lv.60 Doom Elite, all marked Member, all
  with a 0 lightning counter: row 1 crate stack x4,
  iron 16.0K, food 16.0K, coin 11.0K; row 2 crate stack
  x4, iron 28.5K, food 28.5K, coin 19.4K; row 3 crate
  stack x4, iron 16.0K, food 16.0K, coin 11.0K. The
  world-map gift badge was 3 at entry, matching the
  three rows. Panel closed at its X, then the BASE
  toggle at [913,975] returned to the base view. Game
  left on the own base screen. Follow-up for the
  owning regular: the three Doom Elite loot rows are
  unclaimed work, not scout work. The gifts units
  queued for 14:30 should claim them, or a diff should
  raise them if the gifts regular does not cover LOOT.
  No new Issue filed: the loot box is a located
  surface, not a new gap or failure mode, and the
  station remainder is a pre-existing carried item.
- Red dot accounting: seen on surfaces walked:
  Alliance panel Wars, Help, Gifts and Techs dots;
  base Events badge 1, radar badge 11, 99+ badge;
  world-map gift badge 3. Explained: Wars, Help,
  Gifts and Techs map to their owning regulars; Events
  badge 1 maps to the events surface; radar badge 11
  maps to the radar regular; 99+ maps to chat and mail
  surfaces; the world-map gift badge 3 maps to the LOOT
  panel above, with three unclaimed rows. Unexplained:
  0 in the surfaces walked. Carried unwalked: the
  station panel only (see above), and the standing
  furnace overdrive toast.
- Tooling finding - grounded taps: a click needs a
  fresh observation_id from a compact or image
  observation taken immediately before it; the close,
  panel and toggle taps in this unit all used the
  observation just taken. LOOT entry grounded at
  [311,237] on the world map; LOOT close at about
  [818,216]; BASE/WORLD toggle at [913,975].
- Carried forward: successor unit enqueued in chain
  scout-mid-2026-10-31
  (scout-midday-scout-mid-2026-10-31-007) for the
  remainder: the station panel only, to be re-checked
  when a train is preparing.


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

## What the 2026-11-04 0906, 0911 and 0919 units added - base group twice, stale alliance remainder, Wars dot absent with no rally

- Units scout-2026-11-03-1900 (post-reset base group, 09:04-09:06), scout-midday-2026-11-04-0700 (midday base group, about 09:11) and scout-midday-scout-mid-2026-11-02-005 (stale alliance remainder, 09:12-09:19) by ticker-0904, sessions cc-441/cc-442, all partial with blocker category h (by-design chain continuation), not misses. Observe-only throughout; nothing claimed, fought, dispatched, donated, boarded, dug, joined or bought. No price tag was tapped. Evidence in `_records_/2026-11-04/perception-scout/0906-queue-run.md`, `0911-queue-run.md`, `0919-queue-run.md`, appended to `_records_/2026-11-04/perception-scout/observation.md`.
- Base screen and HUD, read live 09:06 and 09:11: account power 150,028,269, unchanged across the pass (was 149,948,901 at the 2026-11-03 13:40 read). HUD totals as displayed: top row food 415.2M, iron 745.8M, coin 15.2M; second row 21.0M, 922.2K; diamonds 12.72K with a plus button. The food/coin/power figures match the 0755 harvest and 0814 training reads exactly. Cart 3,071 at 09:06 to 3,121 at 09:11 (+50, cause not established from this screen). Chat badge 45 to 48. Left column both reads: avatar Lv.30, hammer 2/4, flask 2/2, green face, weather widget 6.5C, an icon with a red badge 2, a truck icon, a circular icon with a red badge 1, wrench icon at the bottom. Right column: Events with a red badge 1, Capitol, VS timer 08:54:15 falling to 08:48:39, Season II timer 11d 08:54:15 falling to 11d 08:48:39, Alliance with no red dot visible, Mail, Inventory. Building timer 15:05 to 15:11. A NEW badge on a centre building, observed only, not opened - recurring unknown, carried not closed.
- Furnace toast again at the bottom both reads: "...rnace total overdrive time (in sec) [22/60]", still unexplained, red-line surface observed only - recurring unknown, carried not closed.
- No train icon in the left column and no "Boarding closes in" banner in either base read, so no train is preparing in these frames; the station panel stays a preparation-only surface, carried not closed (consistent with the 1345 section and the 0839 train check-only unit).
- Red dot accounting, base groups: seen 4 (Events badge 1, left-column badges 2 and 1, chat badge). Explained 2 within the base group: Events badge 1 maps to the events regular; chat badge maps to the chat and mail surfaces. The two left-column badges belong to groups the successor walks, so unexplained within the base group alone is 2, and 0 in the pass standard since the carried badges belong to successor groups. Carried unwalked from the base passes: scout-events, scout-store and scout-alliance groups in full. unmatched_labels: none in the surfaces actually walked.
- Alliance remainder (stale chain, executed not skipped): the queue `next` pick returned this stale unit of the closed 2026-11-02 midday pass. It still yielded live reads (Kills and Donation tabs, both City List tabs, mail categories), so it was executed rather than skipped. The planner or retro may expire the chain; no new Issue filed here, since no new task, gap or repeated failure mode was discovered.
- Alliance panel, read live: [AP3x] The Apex, 5.0 stars, Leader Abŷss Apex, Power 13,077,801,685 (was 13,091,657,850 at the 2026-11-03 13:40 read), Members 94/100, Language English, motto unchanged including the Korean line. Red dots on the panel: Help, Alliance Gifts, Alliance Techs. No dot on Alliance Wars in this frame (previously the Wars dot mapped to a live rally; no rally is running now), and no dot on Alliance Store, Members, Assemble, Strength Ranking, Alliance Events or Alliance City (City button shown highlighted, as before). Wars-dot mapping refined: the dot is present while a rally runs and absent with no rally running - this frame closes the mapping question for the no-rally case (cf. Issue #212).
- Strength Ranking, walked live: Power tab own row pinned at the foot, 31 Bears Lair (R3) 150,028,269, matching the HUD power. Kills tab: 1 Teemo (R4) 71,222,940; 2 TTS Rage Apex (R4) 37,105,456; 3 Missile Apex (R3) 29,909,611; 4 Abŷss Apex (R5) 24,756,940; 5 ItStartsWithaDream (R4) 21,390,596; 6 Bamie (R3) 20,018,107; own row pinned at the foot: 92 Bears Lair (R3) 48,638 kills. Donation tab, Daily sub-tab: 1 KaBoom420 (R2) 23,150; 2 DCna8ive (R3) 13,250; 3 Texan Apex (R4) 10,300; 4 MrCallejon (R3) 8,750; 5 Kkkayyyyy (R3) 8,550; own row pinned at the foot: 32 Bears Lair (R3) 5,300 donation points. Donate and Rewards buttons observed only, never tapped.
- Alliance City (City List), walked live, both tabs: Produces Rare Soil tab: Production Rate 5.88K/h, Captured Cities 6/6 (Lv.6 X:499 Y:411 +1,000/h; Lv.5 X:336 Y:411 +900/h; Lv.5 X:587 Y:336 +900/h; Lv.5 X:411 Y:336 +900/h; Lv.4 X:499 Y:262 +800/h; Lv.4 X:336 Y:262 +800/h; a further Lv.6, Lv.6, Lv.5 row below the fold). Produces Coal tab: Production Rate 13.53K/h, Digging Strongholds captured 4/4 (Lv.6 X:587 Y:411 +3,456/h; Lv.6 X:411 Y:411 +3,456/h; Lv.5 X:662 Y:336 +3,312/h; Lv.5 X:336 Y:336 +3,312/h). Footer on both tabs: Digging Stronghold captures left today 2/2, War declarations left today 2/2. City Buff button observed only, never tapped. The Coal tab Claim All button is greyed (disabled), observed only, never tapped. No coal was donated anywhere in this unit.
- Mail, read live at category level only: Battle Report red dot, Alliance no dot, Event red dot, Season no dot, System no dot, Regular no dot, In-app Purchases no dot, one further row below the fold, unread. Footer: "Mails older than 30 days will be automatically deleted." The two dots map to the mail regular; no mail row was opened, so nothing was marked read and no mail reward was claimed here.
- Tap notes, per-screen grounding (do not inherit): the Donation tab first tap at norm 810,135 missed (no change); the re-grounded centre at 655,140 switched tabs. The Coal tab first tap at norm 625,123 missed (the tab ends at x 610); the re-grounded centre at 466,128 switched tabs. The Ranking back arrow sits at norm 160,930, not at the far left edge; the City List back arrow sits at norm 80,923. Back-arrow position varies by screen and must be grounded per screen, not inherited. The two missed taps were single misses corrected by fresh grounding inside the unit, not a repeated failure mode.
- Red dot accounting, alliance remainder: seen on surfaces walked - Alliance panel Help, Gifts and Techs dots; mail Battle Report and Event dots. Explained: all map to their owning regulars. Unexplained: 0 in the surfaces walked. Unknown items: none new in the surfaces walked.
- Carried forward: successor unit enqueued in chain scout-mid-2026-11-02 for the remainder: station panel and loot box re-check only. Both stay carried for a fresh re-check, not closed from memory (station signals checked in this pass's base reads: no train icon, no boarding banner; the loot box was located 2026-11-03 at the world-map gift icon).
- Resource bubbles visible on many left and centre buildings in the base reads, observed only, not collected - harvest belongs to the harvest unit, one unit one task type. Game left on the own base screen.

## What the 2026-11-05 0104 unit added - screen-capture failure, twenty-fifth consecutive pass, nothing read

- Unit scout-midday-scout-mid-2026-11-02-001 by ticker-0104, about 01:04 to 01:07 local, status failed. Evidence in `_records_/2026-11-05/perception-scout/0104-queue-run.md`. Observe-only throughout; nothing claimed, fought, dispatched, donated, boarded, dug, joined or bought.
- No game screen was ever read and no game input was dispatched. The Mac screen-capture stream failed on every attempt: session cc-503 `computer.observe` compact, `computer.control` activate, `computer.observe` image; fresh session cc-504 `computer.control` activate, `computer.observe` compact - five attempts across two computer sessions, all with "Failed to start stream due to audio/video capture failure". `activate` reports `window_on_screen: false` and `brought_to_front: false`. LastWar (bundle com.lastwar.ios, pid 59735) is running, fullscreen 1920x1080 at (0,0) on an inactive Space; Google Chrome is frontmost. Device connection health at the same time: both native and web transports connected and healthy (native lastResponseAgeSeconds 0, web 7) - this is not a connectivity problem; the fullscreen game window on its inactive Space is simply not capturable.
- Recurrence, not a new failure class: this is the twenty-fifth consecutive ticker pass to fail on this exact blocker (ticker-0034 at 00:34 was the twenty-fourth). The blocker is filed as Issue #284 (tooling) alongside the knowledge Issue #282; this pass commented on #284 instead of filing a duplicate, and this run comments the twenty-fourth and twenty-fifth occurrences onto #282.
- Reading warning: this failed unit gives zero evidence about any scout surface. It must NOT be read as "nothing to do" or as a red-dot state - the 2026-11-04 0906 and 0911 base-group reads (account power 150,028,269, HUD food 415.2M, iron 745.8M, coin 15.2M) rest on live reads and stand as the last live reads; this unit rests on no read at all. The carried remainder (station panel and loot box re-check in chain scout-mid-2026-11-02) stays carried for a fresh re-check, not closed from memory.
- The unit's 15 minute budget was spent on capture attempts; game time was zero. No other unit was attempted in this pass: every unit needs the same game screen, so all would fail identically.
- Tracker untouched for failed, per the queue rules; the next tick re-produces this regular.

## Correction 2026-11-05 - the game window is windowed on an inactive Space, not in native fullscreen

- Source: the 0134 survivors record (`_records_/2026-11-05/survivor-intake/0134-queue-run.md`, ticker-0134, twenty-sixth consecutive capture failure), re-confirmed by the 0204 gifts record (`_records_/2026-11-05/alliance-gifts/0204-queue-run.md`, ticker-0204, twenty-seventh). The View menu lists "Enter Full Screen" (read from the menu-action error listing in session cc-505, repeated probe in cc-508 with the menu unchanged), so the app is NOT in native fullscreen: it is a windowed 1920x1080 window on an inactive Space, and the capture failure is the pixel stream of an off-screen window, not a broken screen-recording permission (Chrome windows observe normally in the same sessions).
- Superseded in this profile: the 0104 section's "the fullscreen game window on its inactive Space is simply not capturable" wording - the window is windowed, not fullscreen.
- Follow-up corrected: the standing "screen recording permission or capture pipeline restart" unblock is replaced - the unblock is getting the window back onto the active Space, and the owner clicking the LastWar Dock icon once is the known reliable step. Background-sent Space keys do not switch Spaces, set_window_frame is gated by the stale-observation rule, Cmd+Tab is blocked by the tool, and list_windows needs the exact app name "LastWar" ("Last War" returns 0 windows). No control route available to the background channel moves the window across Spaces without a fresh observation of the window itself.
- This correction does not change the scout state: the 2026-11-04 0906 and 0911 base-group reads (account power 150,028,269, HUD food 415.2M, iron 745.8M, coin 15.2M) stand as the last live reads. The twenty-sixth and twenty-seventh occurrences are commented onto Issue #282 by this run; Issue #284 already tracks the blocker.

## What the 2026-11-05 0234 unit added - screen-capture failure, twenty-eighth consecutive pass, nothing read

- Unit scout-scout-2026-11-02-001 by ticker-0234, about 02:34 to 02:38 local, status failed. Evidence in `_records_/2026-11-05/perception-scout/0234-queue-run.md`. Observe-only throughout; nothing claimed, walked, fought, dispatched, donated, boarded, dug, joined or bought.
- No game screen was ever read and no game input was dispatched. The Mac screen-capture stream failed on every attempt: session cc-509 `computer.control` activate, `computer.observe` compact, `computer.observe` full, `screen.snap`; fresh session cc-510 `computer.control` activate, `computer.observe` image - six attempts across two computer sessions, all with "Failed to start stream due to audio/video capture failure". `activate` reports `window_on_screen: false` and `brought_to_front: false`. LastWar (bundle com.lastwar.ios, pid 59735) is running, one window 1920x1080 at (0,0), window_id 160366; Google Chrome is frontmost. Device connection health at the same time: both native and web transports connected and healthy (native lastResponseAgeSeconds 0, web 9) - this is not a connectivity problem.
- Narrowing, first-hand this pass: session cc-511 observes the Chrome window normally - `computer.control` activate on Google Chrome returned a full accessibility tree and text. The capture pipeline itself works; the fault is specific to the Last War window's capture stream, consistent with the windowed-on-inactive-Space diagnosis in the Correction 2026-11-05 section above. The full and image views fail at stream start exactly like compact, so the failure is not view-dependent - re-verified here, not inherited from the 0034 pass.
- Stale chain head, queue behaviour: this unit belongs to chain scout-2026-11-02, three days stale - its observation would have landed in the 2026-11-02 day file, whose reset day ended 2026-11-03 19:00. The stale head was picked by the queue's earliest-expiry order; the capture failure, not the staleness, is what stopped the unit. A future live unit on this chain should expect the head to be stale and re-ground from the current day, not from the chain's reset day.
- Recurrence, not a new failure class: this is the twenty-eighth consecutive ticker pass to fail on this exact blocker (ticker-0204 at 02:04 was the twenty-seventh). The blocker is filed as Issue #284 (tooling) alongside the knowledge Issue #282; this pass commented on #284 instead of filing a duplicate, and this run comments the twenty-eighth and twenty-ninth occurrences onto #282.
- Reading warning: this failed unit gives zero evidence about any scout surface. It must NOT be read as "nothing to do" or as a red-dot state - the 2026-11-04 0906 and 0911 base-group reads (account power 150,028,269, HUD food 415.2M, iron 745.8M, coin 15.2M) rest on live reads and stand as the last live reads; this unit rests on no read at all. The carried remainder (station panel and loot box re-check in chain scout-mid-2026-11-02) stays carried for a fresh re-check, not closed from memory.
- Tracker untouched for failed, per the queue rules; the next tick re-produces this regular.

## What the 2026-11-05 0941 unit added - invoke-channel stall, forty-first consecutive pass, nothing read

- Unit scout-midday-scout-mid-2026-10-31-005 by ticker-0941, about 09:44 to 09:52 local, status failed. Evidence in `_records_/2026-11-05/perception-scout/0941-queue-run.md`. Observe-only throughout; nothing claimed, fought, dispatched, donated, boarded, dug, joined or bought.
- No game screen was ever read and no game input was dispatched. Every device invoke timed out with zero responses - three attempts: `computer.session` start (node_invoke_timeout after 120000ms), `connection.health` (node_invoke_timeout after 25000ms), `computer.session` start again (node_invoke_timeout after 120000ms). Mac mini 1c817413-83e2-0545-cb90-36d5e096a6bd reported online by device.list, but last_seen 2026-11-05T15:36:52Z (07:36 local), stale about 2 hours 5 minutes at pass time; the recovery device shows the same stale timestamp. This meets the standing at-least-3-attempts retry rule.
- Worsened form, confirmed not new: this is the same zero-response invoke-channel stall the ticker-0904 harvest pass first recorded - the invoke channel itself is stalled, not just the LastWar window stream. The in-tree probe `_tools_/mac_capture_probe.py` 1.0.0 answers this evidence UNKNOWN (low confidence, exit 1): it has no invoke-timeout field and asks for the checklist (list_windows, View-menu inspect, one observe attempt), each step of which would burn another 120s timeout. The CHANNEL_STALL diagnosis that classifies exactly this evidence (invoke_timeouts with invoke_responses 0, high confidence, stop_pass yes) lived in PR #321, still open and unmerged at pass time, so this pass classifies by that design and stops rather than re-running the checklist. PR #321 has since MERGED (2026-11-05, pr-integration 0952 pass, commit 18b8b6da29), so the probe now classifies this evidence in-tree and the next pass will classify with it rather than by the design.
- Stale-chain unit: chain scout-mid-2026-10-31, seq 5, staged 2026-11-03. Per the stale-scout precedent its observation would have been filed under 2026-11-05 as a read of the current game state, but no read exists to file. The alliance remainder this unit owns (station panel, loot box) is unwalked and no observation was produced.
- Recovery, gateway level: recovery still needs the owner-side step, now at the gateway level - the Mac-side agent gateway likely needs a restart before re-probing (per the PR #321 design); the Dock-icon step addresses the window-stream fault, not a stalled invoke channel. That gateway-restart step is the record's inference, not a verified fix: no pass has yet run it and confirmed recovery. See the resource-collection 1.28.0 fold for the first recording of this form and the scoping of the Correction 2026-11-05 unblock.
- No blind taps were dispatched: without a session or an observation, any tap could land on the wrong control, so the unit stops here under the check-first rule. No different-device dialog was observed (no screen was ever captured) and no device takeover was needed.
- Recurrence: this is the forty-first consecutive ticker pass with a Mac device-access blocker (fortieth was ticker-0904, which first recorded this zero-response form; thirty-seventh was ticker-0734 on the capture failure form). The blocker is filed as Issue #284 (tooling) alongside the knowledge Issue #282; this pass commented on #284 instead of filing a duplicate, and this run comments the forty-first occurrence onto #282.
- Reading warning: this failed unit gives zero evidence about any scout surface. It must NOT be read as "nothing to do" or as a red-dot state - the 2026-11-04 0906 and 0911 base-group reads (account power 150,028,269, HUD food 415.2M, iron 745.8M, coin 15.2M) rest on live reads and stand as the last live reads; this unit rests on no read at all. The carried remainder (station panel and loot box re-check in chain scout-mid-2026-11-02) stays carried for a fresh re-check, not closed from memory. No successor unit is enqueued from this unit - the chain's remainder is unchanged by a pass that read nothing, and a successor would hit the same stalled channel. No zombie check was possible (Events hub unwalked); no zombie chain is seeded, per the standing rule that the event ended 2026-10-30 and no live return sighting exists in this pass.
- Tracker untouched for failed, per the queue rules; the next tick re-produces this regular.

## What the 2026-11-05 1234 unit added - Mac device offline, forty-sixth consecutive pass, zero-response form

- Unit scout-midday-scout-mid-2026-11-02-004 by ticker-1234, about 12:34 to 12:50 local, status failed. Evidence in `_records_/2026-11-05/perception-scout/1234-queue-run.md`. Observe-only throughout; nothing claimed, fought, dispatched, donated, boarded, dug, joined or bought. The unit owned the alliance remainder of the 2026-11-02 midday pass: Wars, City, Events, Members, Strength Ranking, station panel, mail, world map.
- No game screen was ever read and no game input was dispatched. Four device invokes, zero responses: connection.health on the Mac mini node_offline (device offline, no wake-up path), connection.health on the recovery device node_invoke_timeout after 25s, connection.repair (native) on the recovery device node_invoke_timeout after 25s, connection.health on the Mac mini again node_offline. device.list reports the Mac mini offline with last_seen 2026-11-05T15:36:52Z (07:36 local), stale about 5 hours, unchanged since the ticker-1025 pass. No probe was run: re-probing is owed only after device.list last_seen refreshes, and last_seen is unchanged, so the CHANNEL_STALL classification from the 1025 probe stands unre-tested.
- Recurrence, not a new failure class: this is the forty-sixth consecutive ticker pass with a Mac device-access blocker, seventh in the worsened zero-response form after ticker-0904 (fortieth), ticker-0941 (forty-first), ticker-1025 (forty-second), ticker-1104 (forty-third), ticker-1134 (forty-fourth) and ticker-1204 (forty-fifth). The blocker is filed as Issue #284 (tooling) alongside the knowledge Issue #282; this pass commented on #284 instead of filing a duplicate, and this run comments the forty-sixth occurrence onto #282.
- Reading warning: this failed unit gives zero evidence about any scout surface. It must NOT be read as "nothing to do" or as a red-dot state - the 2026-11-04 0906 and 0911 base-group reads (account power 150,028,269, HUD food 415.2M, iron 745.8M, coin 15.2M) rest on live reads and stand as the last live reads; this unit rests on no read at all. The carried remainder (station panel and loot box re-check in chain scout-mid-2026-11-02) stays carried for a fresh re-check, not closed from memory. No zombie check was possible (Events hub unwalked); no zombie chain is seeded, per the standing rule that the event ended 2026-10-30 and no live return sighting exists.
- Sync: reaped 0, expired 2, due 23, produced 14 units (mail, help, gifts, harvest, passes, secrets, treasures, survivors, trucks, train, training, events, star-ceremony, duel-score for the 1003/1030/1057 cycles); 8 regulars already queued. The inbox held 42 units at this pass.
- Tracker untouched for failed, per the queue rules; the next tick re-produces this regular.

## What the 2026-11-05 1304 unit added - Mac device offline, forty-seventh consecutive pass, zero-response form

- Unit scout-scout-2026-11-03-001 by ticker-1304, about 13:04 to 13:15 local, status failed. Evidence in `_records_/2026-11-05/perception-scout/1304-queue-run.md`. Observe-only throughout; nothing claimed, fought, dispatched, donated, boarded, dug, joined or bought. This was the post-reset scout chain head for reset date 2026-11-03, created 2026-11-04T17:06Z, never attempted before this pass - so the current trade day still has no live scout observation, and the 2026-11-04 0906/0911 reads stand as the last live reads.
- No game screen was ever read and no game input was dispatched. Five device invokes, zero responses: computer.session start on the Mac mini node_offline (attempt 1), connection.health on the Mac mini node_offline (attempt 2), connection.repair (web) on the Mac mini node_offline (attempt 3), computer.session start on the Mac mini again node_offline (attempt 4), connection.health on the recovery device node_invoke_timeout after 25s (attempt 5). device.list reports the Mac mini offline with last_seen 2026-11-05T15:36:52Z (07:36 local), stale about 5 hours 35 minutes, unchanged since the ticker-1025 pass. No probe was run: re-probing is owed only after device.list last_seen refreshes, and last_seen is unchanged, so the CHANNEL_STALL classification from the 1025 probe stands unre-tested.
- Recurrence, not a new failure class: this is the forty-seventh consecutive ticker pass with a Mac device-access blocker, eighth in the worsened zero-response form. The blocker is filed as Issue #284 (tooling) alongside the knowledge Issue #282; this pass commented on #284 instead of filing a duplicate, and this run comments the forty-seventh occurrence onto #282.
- Pool-authority note, measured by this pass: pool figures must be read from the records/2026-11-05 branch (inbox 41 units, done 845 at sync time). The planner-1240 pool figures (inbox 75, done 925) were measured against the main working tree, which sits on the stale work/ops-execution-records branch (queue state from 2026-11-03) and holds another job's in-flight state - so planner pool figures read from that tree are not authoritative. The records branch is the authoritative pool for ticker passes.
- Reading warning: this failed unit gives zero evidence about any scout surface. It must NOT be read as "nothing to do" or as a red-dot state. The carried remainder (station panel and loot box re-check) stays carried for a fresh re-check, not closed from memory. No zombie check was possible (Events hub unwalked); no zombie chain is seeded, per the standing rule.
- Tracker untouched for failed, per the queue rules; the next tick re-produces this regular.

## What the 2026-11-05 1334 unit added - Mac device offline, forty-eighth consecutive pass, zero-response form

- Unit scout-midday-scout-mid-2026-11-04-001 by ticker-1334, about 13:34 to 13:45 local, status failed. Evidence in `_records_/2026-11-05/perception-scout/1334-queue-run.md`. Observe-only throughout; nothing claimed, fought, dispatched, donated, boarded, dug, joined or bought. This was the midday scout chain head for 2026-11-04, created 2026-11-04T17:11:49Z, never attempted before this pass - so the current trade day still has no live scout observation, and the 2026-11-04 0906/0911 reads stand as the last live reads.
- No game screen was ever read and no game input was dispatched. Four device invokes, zero responses: connection.health on the Mac mini node_offline (attempt 1), computer.session start on the Mac mini node_offline (attempt 2), screen.snap on the Mac mini node_offline (attempt 3), connection.health on the recovery device node_invoke_timeout after 25s (attempt 4). device.list reports the Mac mini offline with last_seen 2026-11-05T15:36:52Z (07:36 local), stale about 6 hours 5 minutes, unchanged since the ticker-1025 pass. No probe was run: re-probing is owed only after device.list last_seen refreshes, and last_seen is unchanged, so the CHANNEL_STALL classification from the 1025 probe stands unre-tested.
- Recurrence, not a new failure class: this is the forty-eighth consecutive ticker pass with a Mac device-access blocker, ninth in the worsened zero-response form. The blocker is filed as Issue #284 (tooling) alongside the knowledge Issue #282; this pass commented on #284 instead of filing a duplicate, and this run comments the forty-eighth occurrence onto #282.
- Reading warning: this failed unit gives zero evidence about any scout surface. It must NOT be read as "nothing to do" or as a red-dot state - the 2026-11-04 0906 and 0911 base-group reads (account power 150,028,269, HUD food 415.2M, iron 745.8M, coin 15.2M) rest on live reads and stand as the last live reads; this unit rests on no read at all. The carried remainder (station panel and loot box re-check in chain scout-mid-2026-11-04) stays carried for a fresh re-check, not closed from memory. No zombie check was possible (Events hub unwalked); no zombie chain is seeded, per the standing rule that the event ended 2026-10-30 and no live return sighting exists.
- Sync: reaped 0, expired 0, due 23, produced 0 units - all 23 due regulars already queued. The inbox held 39 units at this pass (records-branch pool, done 846 at sync time).
- No successor unit is enqueued from this unit - the chain's remainder is unchanged by a pass that read nothing, and a successor would hit the same stalled channel.
- Tracker untouched for failed, per the queue rules; the next tick re-produces this regular.

## What the 2026-11-05 1404 unit added - Mac device offline, forty-ninth consecutive pass, zero-response form

- Unit scout-midday-scout-mid-2026-11-02-006 by ticker-1404, about 14:04 to 14:10 local, status failed. Evidence in `_records_/2026-11-05/perception-scout/1404-queue-run.md`. Observe-only throughout; nothing claimed, fought, dispatched, donated, boarded, dug, joined or bought. The unit owned the scout-alliance remainder window of chain scout-mid-2026-11-02 (seq 6, created 2026-11-04T17:18:45Z, first attempt this pass): station panel, loot box re-check - so the current trade day still has no live scout observation, and the 2026-11-04 0906/0911 reads stand as the last live reads.
- No game screen was ever read and no game input was dispatched. Four device invokes, zero responses: connection.health on the Mac mini node_offline (attempt 1), computer.session start on the Mac mini node_offline (attempt 2), screen.snap on the Mac mini node_offline (attempt 3), connection.health on the recovery device node_invoke_timeout after 25s (attempt 4). device.list reports the Mac mini offline with last_seen 2026-11-05T15:36:52Z (07:36 local), stale about 6 hours 33 minutes, unchanged since the ticker-1025 pass and identical to the ticker-1334 reading 30 minutes earlier. No probe was run: re-probing is owed only after device.list last_seen refreshes, and last_seen is unchanged, so the CHANNEL_STALL classification from the 1025 probe stands unre-tested.
- Recurrence, not a new failure class: this is the forty-ninth consecutive ticker pass with a Mac device-access blocker, tenth in the worsened zero-response form. The blocker is filed as Issue #284 (tooling) alongside the knowledge Issue #282; this pass commented on #284 instead of filing a duplicate, and this run comments the forty-ninth occurrence onto #282.
- Reading warning: this failed unit gives zero evidence about any scout surface. It must NOT be read as "nothing to do" or as a red-dot state. The carried remainder (station panel and loot box re-check) stays carried for a fresh re-check, not closed from memory. No zombie check was possible (Events hub unwalked); no zombie chain is seeded, per the standing rule.
- Sync: reaped 0, expired 3 (harvest, survivors and training 2026-11-05-1003), due 23, produced 6 units (harvest, radar, survivors, training, donations, arms-race 2026-11-05-1403); 17 due regulars already queued. The inbox held 42 units at this pass (records-branch pool, done 850 at sync time).
- No successor unit is enqueued from this unit - the chain's remainder is unchanged by a pass that read nothing, and a successor would hit the same stalled channel.
- Tracker untouched for failed, per the queue rules; the next tick re-produces this regular.

## What the 2026-11-05 1836 unit added - Mac device offline, fifty-eighth consecutive pass, zero-response form

- Unit scout-scout-2026-11-02-005 by ticker-1834, about 18:36 to 18:50 local, status failed. Evidence in `_records_/2026-11-05/perception-scout/1836-queue-run.md`. Observe-only throughout; nothing claimed, fought, dispatched, donated, boarded, dug, joined or bought. The unit owned the chain remainder window of chain scout-2026-11-02 (seq 5, created 2026-11-03T21:15:50Z, first attempt this pass), the remainder after unit 004 walked the alliance remainder - so the current trade day still has no live scout observation, and the 2026-11-04 0906/0911 reads stand as the last live reads.
- No game screen was ever read and no game input was dispatched. Five device invokes, zero responses: connection.health on the Mac mini node_offline (attempt 1), connection.repair (web) on the Mac mini node_offline (attempt 2), computer.session start on the Mac mini node_offline (attempt 3), computer.control frontmost_app on the Mac mini node_offline (attempt 4), connection.health on the recovery device node_invoke_timeout after 25s (attempt 5). device.list reports the Mac mini offline with last_seen 2026-11-05T15:36:52Z (07:36 local), stale about 11 hours, unchanged since the ticker-1025 pass and identical to the ticker-1804 reading 30 minutes earlier; a fresh device.list at about 18:44 confirms the same last_seen, still unrefreshed. No probe was run: re-probing is owed only after device.list last_seen refreshes, and last_seen is unchanged, so the CHANNEL_STALL classification from the 1025 probe stands unre-tested.
- Recurrence, not a new failure class: this is the fifty-eighth consecutive ticker pass with a Mac device-access blocker, nineteenth in the worsened zero-response form. The blocker is filed as Issue #284 (tooling) alongside the knowledge Issue #282; this pass commented on #284 instead of filing a duplicate, and this run comments the fifty-eighth occurrence onto #282.
- Reading warning: this failed unit gives zero evidence about any scout surface. It must NOT be read as "nothing to do" or as a red-dot state. The carried remainder stays carried for a fresh re-check, not closed from memory. No zombie check was possible (Events hub unwalked); no zombie chain is seeded, per the standing rule.
- Sync: reaped 0, expired 4 in the first sync (train, star-ceremony, help and gifts 2026-11-05-1430) but a concurrent job expired those same four on the shared disk pool at 18:42:34, so the redo sync expired 0 and the expiry is not this pass's change; due 23, produced 4 units (vip, daily-missions, duel-score and scout 2026-11-05-1800); 18 due regulars already queued. The inbox held 73 units at this pass (pool as synced from the main worktree disk, done 949 at sync time); the records-branch pool on its own reads smaller, so the disk copy carries units the branch lacks, including this unit itself. The four produced units are absent from the branch, so no duplicate was staged.
- Worktree loss, process lesson: the pass first ran in /tmp/lastwar-ticker-1834, which the runtime wiped mid-run (the whole /tmp was empty when the token-release step ran, about 18:44), taking the uncommitted sync output, claim, record and INDEX append with it. The GitHub comment on Issue 284 had already been posted and was not duplicated. The pass was redone in full in a workspace worktree (~/workspace/lastwar-worktrees/ticker-1834-1105): sync re-run (same 4 units produced), token re-acquired, unit re-claimed, device.list re-confirmed the same stale last_seen, record rewritten and unit completed there. Lesson for later passes: never put pass work in /tmp; worktrees live under ~/workspace/lastwar-worktrees/.
- No successor unit is enqueued from this unit - the chain's remainder is unchanged by a pass that read nothing, and a successor would hit the same stalled channel.
- Tracker untouched for failed, per the queue rules; the next tick re-produces this regular.

## What the 2026-11-06 1704 unit added - Mac device offline, eighty-fourth consecutive pass, zero-response form

- Unit scout-2026-11-05-1800 by ticker-1704, about 17:04 to 17:10 local, status failed. Evidence in `_records_/2026-11-06/perception-scout/1710-queue-run.md`. Observe-only throughout; nothing claimed, fought, dispatched, donated, boarded, dug, joined or bought. Zero surfaces walked, zero items observed, zero red dots seen or explained, no observation appended to the 2026-11-06 day observation file. This was a stale unit from the 2026-11-05 18:00 slot (planned_for 2026-11-06T02:00:00Z, expires 2026-11-07T02:00:00Z).
- No game screen was ever read and no game input was dispatched. Seven device invokes, zero responses: computer.session start on the Mac mini three times node_offline (device offline, no wake-up path), connection.health on the Mac mini node_offline, connection.repair (target web) on the Mac mini node_offline, connection.repair (target native) on the recovery device node_invoke_timeout after 25 seconds, connection.health on the recovery device node_invoke_timeout after 25 seconds. device.list reports the Mac mini offline with last_seen 2026-11-05T15:36:52Z (07:36 local), stale about 33 hours 33 minutes at pass time, unchanged since the ticker-1507, ticker-1534, ticker-1604 and ticker-1634 passes; the recovery device also reports offline with the same stale last_seen. This meets the standing at-least-3-attempts retry rule. No probe was run: re-probing is owed only after device.list last_seen refreshes, and last_seen is unchanged, so the CHANNEL_STALL classification from the 1025 probe stands unre-tested.
- Recurrence, not a new failure class: this is the eighty-fourth consecutive ticker pass with a Mac device-access blocker, forty-fifth in the worsened zero-response form after ticker-1634 (eighty-third, forty-fourth). The blocker is filed as Issue #284 (tooling) alongside the knowledge Issue #282; this pass commented on #284 instead of filing a duplicate, and this run comments the eighty-fourth occurrence onto #282.
- Reading warning: this failed unit gives zero evidence about any scout surface. It must NOT be read as "nothing to do" or as a red-dot state - no observation file exists for the 2026-11-06 reset day and none was created; the last live scout observation remains the one recorded before the outage, and no scout unit has succeeded since the Mac went offline. This unit rests on no read at all. No zombie check was possible (Events hub unwalked); no zombie chain is seeded, per the standing rule that the event ended 2026-10-30 and no live return sighting exists.
- Sync: reaped 0, expired 0, due 22, produced 0 new units; 22 regulars already queued. Queue stats at 01:07Z: inbox 70, claimed 0, done 977, upcoming 53. The pre-reset zero-sweep pair for tonight's 19:00 reset (chain pre-reset-sweep-2026-11-06) sits in the inbox (pending 2), not yet due.
- No successor unit is enqueued from this unit - the chain's remainder is unchanged by a pass that read nothing, and a successor would hit the same stalled channel.
- Tracker untouched for failed, per the queue rules; the next tick re-produces this regular.

## Channel rules, carried 2026-11-07 - Mission Control and background Ctrl+Right lessons (propagation from the 1020 help unit)

- Channel rules, now carried in this profile (propagation follow-up from the 1732 run, perception-scout done - joining alliance-help, alliance-gifts, radar-tasks, arms-race, alliance-donations and shop-claims): Mission Control was not opened as a recovery step, per the 1020 lessons folded into alliance-help 1.27.0 - open_app Mission Control wedged the channel in that pass (first launch opened the overview; every later activate and observe then failed with geometry_mismatch origin_delta 256+, agent_display false, and all key input gated on observation_required; a second launch closed it and restored observation; the overview itself cannot be observed or clicked through this channel). Background Ctrl+Right was not tried: it does not switch Spaces through this channel (in the 1020 pass the key went to the Finder column view instead). The known reliable unblock stands: the owner clicking the LastWar Dock icon once.

## What the 2026-11-07 2121 unit added - alliance remainder partial, first live scout observation since the outage, Zombie Siege found

- Unit scout-scout-2026-11-02-005 by ticker-2104, about 21:07 to 21:16 local (542 seconds; the 21:21 end in the record header is the device-token lease expiry, not the execution end), status partial. Evidence in `_records_/2026-11-07/perception-scout/2121-queue-run.md` (commit 31467b04cb on records/2026-11-07) and the observation appended to `_records_/2026-11-02/perception-scout/observation.md` (ticker-2104 section). Computer session cc-50. Observe-only throughout; nothing claimed, fought, dispatched, donated, joined or bought. This is the first live scout observation since the Mac came back online - the chain remainder from unit 004, carried through the outage as failed attempts by ticker-1834 (2026-11-05) and ticker-1704 (2026-11-06).
- Base screen and HUD, read live about 21:07 local: power 149,850,353; resources 478.8M, 802.1M, 6.9M, 25.0M, 922.2K; diamonds 13.22K; cart 4,217; stamina 120. Events badge 1, Season II badge 1, Alliance dot, skull timer 00:00:20 with badge 2, Inventory dot, 99+ badge. Furnace toast again: "h-temp Furnace total overdrive time (in sec) [22/60]", still unexplained. Resource bubbles observed only, not collected.
- Alliance panel: [AP3x] The Apex, 5.0 stars, Leader Abyss Apex, Power 13,355,288,388 at entry rising to 13,360,041,845 during the unit, Members 96/100, Language English. Dots on Alliance Wars, Help, Alliance Gifts only. Lower panel scrolled: Assemble, Strength Ranking, Alliance Events, Alliance City (gold), Season Contributions (gold), Season Milestones (gold), one more gold row below the fold, unread. Alliance Star (Event 40) banner, Time Left 20:41:09 falling to 20:36:40.
- Members: 18 online; R5 Abyss Apex; Warlord ItStartsWithaDream, Recruiter KAGE, Muse StarFall, Butler KillerInstinct14; R4 "The elected" 2/10; R3 "Armed Guards" 10/59 with four Lv.30 members read (Captain Landmine 131.3M, Dw1968 110.2M, Commander Supa 93.5M, Raze Cromwell 145.4M, all Online). Manage buttons not tapped.
- Strength Ranking, all three tabs: Power top 6 and own #34 Bears Lair 147,744,234 (HUD read 149,850,353 minutes earlier; discrepancy noted, unverified); Kills top 6 and own #94 Bears Lair 48,638; Donation Daily top 5 and own #46 Bears Lair 1150. Donate and Rewards buttons observed only, not tapped. Weekly subtab not opened.
- Alliance Events: single tab seen, Zombie Siege, mode Alliance Exercise (30-minute Battle Stage, top-damage Commander may multiply all members' rewards by 10x, Offline Participation auto-joins rallies when offline). Preparing 41:48:23; Your Time Zone 2026-11-9 15:00:00; Offline Participation already checked. Rewards, Build and View not tapped. This is a NEW label for the roster - filed as Issue #419 (idea, knowledge): explore before 2026-11-09 15:00, read-only first (entry and staging flow, participation cost if any, reward table, whether the 15:00 time is the battle start, whether any action is due from Bears Lair before then); anything touching a price, diamonds or a red line stays learn-only and is named to the owner.
- Record (Alliance Logs), War tab: six identical entries of one member attacking Jujuliano1's base #2110, victory, server times 02:36:01 to 02:36:20; next entry another member attacking Valerunomu's base #2110. Member, Message and Event tabs not opened.
- Applicants: two taps produced no page change; the second surfaced the toast "Permission needed to execute this action." R3 Bears Lair cannot open Applicants (officer-only surface). Resolved by permission, not unwalked.
- Red dot accounting: seen 8 (Alliance Wars, Help, Alliance Gifts dots; base Events 1, Season II 1, skull-timer 2, Inventory dot, 99+ badge). Explained 3: the three panel dots map to their owning regulars. Unexplained 5: the five base badges, carried to their owning groups. Unknown items 5: furnace overdrive toast [22/60]; the gold-row label below Season Milestones; the "Important: President..." scrolling banner; a Tactical Master Supply Box toast seen mid-unit; the HUD-vs-ranking power discrepancy.
- unmatched_labels: Zombie Siege, Alliance Exercise, Offline Participation, Alliance City, Season Contributions, Season Milestones.
- No Zombie Invasion tab was seen anywhere in the alliance panel or the base screen; the event ended 2026-10-30 and the chain stays closed until its tab is seen live again. No zombie chain seeded.
- Unwalked and carried to the successor unit 006 (enqueued under chain scout-2026-11-02): Alliance Star, Settings, the Record Member/Message/Event tabs, the station panel and the loot box pin. Tracker untouched (partial rule).
- Observation file divergence (known gap, Issue #415): the branch observation file lacks five disk sections (ticker-0404, ticker-0504 x2, ticker-0904, ticker-1304) and the disk file lacks the branch's 1801 section (ticker-1755); the five disk sections' run records (0410, 0508, 0510, 0910, 1314) are likewise unpushed. This pass appends only its own section to the branch file; the union is left for the retro/integrator under Issue #415.
- Branch already carries this unit: the records branch holds `_queue_/done/scout-scout-2026-11-02-005.md` as failed by ticker-1834 (2026-11-06 02:43Z, Mac offline, Issue 284). The branch file is kept; this partial is the re-attempt evidence, per the ticker-0127 precedent for the same situation. The successor 006 chains from 005 regardless.
