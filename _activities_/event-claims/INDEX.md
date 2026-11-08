---
title: Event Claims
created: 2026-10-25T18:58:00Z
modified: 2026-11-08T15:38:02Z
level: L1
version: 1.26.0
description: Checking event pages and claiming earned event rewards, one activity folder for event claim knowledge
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-25
  - source: owner structure direction on activity folders, 2026-10-25
  - source: owner direction to page through every red dot and claim what is shown, evening of 2026-10-25
  - source: owner correction on 2026-10-26 - a bouncing chest on the Events screen is an unclaimed reward signal, and the three Arms Race point chests are not all of its rewards
  - source: in-game screens observed on the owner Mac mini, 2026-11-01 (1055 events unit)
  - source: in-game screens observed on the owner Mac mini, 2026-11-01 (1348 events unit)
  - source: ticker-2142 events execution record 2026-11-01 2200 queue run
  - source: ticker-0034 event-claims execution record 2026-11-02 0050 queue run
  - source: ticker-0334 event-claims execution record 2026-11-02 0359 queue run (partial, Escape crash)
  - source: ticker-0904 event-claims execution record 2026-11-02 0910 queue run (done, full hub sweep, nothing claimable, hub back arrow unresponsive to background clicks)
  - source: ticker-0934 truck-plunder execution record 2026-11-02 0935 queue run (hub back arrow centre re-measurement)
  - source: ticker-1234 event-claims execution record 2026-11-02 1250 queue run (done, full hub sweep, nothing claimable, relaunch restores hidden rails)
  - source: ticker-2104 event-claims execution record 2026-11-02 2113 queue run (done, full hub sweep, Wanted Boss rotated to Code 64)
  - source: ticker-2334 event-claims execution record 2026-11-02 2341 queue run (done, full hub sweep, nothing claimable, Arms Race rotated to Tech Research, Wanted Boss tab dot is a live-event marker)
  - source: ticker-0304 event-claims execution record 2026-11-03 0318 queue run (done, full hub sweep, 0 claimed, Desert Storm registered)
  - source: ticker-1204 event-claims execution record 2026-11-03 1217 queue run (done, full hub sweep, 0 claimed, Arms Race Hero Advancement 41,500, Boss Code 64 not yet out)
  - source: ticker-0234 event-claims execution record 2026-11-04 0245 queue run (done, full hub sweep, nothing claimable)
  - source: ticker-0504 event-claims execution record 2026-11-04 0519 queue run (done, full hub sweep, 0 claims, Arms Race phase ends inside the next hour, no Zombie Invasion tab)
  - source: ticker-0834 event-claims execution record 2026-11-04 0843 queue run (done, full hub sweep, 0 claims, Arms Race now Base Building phase, no Zombie tab)
  - source: ticker-1834 event-claims execution record 2026-11-04 1834 queue run (failed, Mac screen-capture failure on every attempt, no game screen read, no input dispatched, thirteenth consecutive ticker pass to fail this way, Issue 284)
  - source: ticker-0004 perception-scout execution record 2026-11-08 0011 queue run (partial, events group walked live, Frontline badge 1 is a Challenge attempt, Doomsday badge 22 is claimable Rewards, Winter Battlefield starting soon, Hero Advancement phase live; record commit e6192726d1 on records/2026-11-08)
  - source: ticker-0604 perception-scout execution record 2026-11-08 0608 queue run (partial, Winter Battlefield Rewards, Rules and Shop Honor tab read live); record commit 50389b4b4a on records/2026-11-08
  - source: ticker-0634 event-claims execution record 2026-11-08 0656 queue run (partial, Doomsday first-kill tiers Lv.100-140 claimed, Frontline rewards unclaimable); record commit 9669d391ea on records/2026-11-08
---


# Event claims

## What this activity is

Checking the Events pages for earned rewards and claiming them. This
folder accumulates event claim knowledge - which events pay passive
claims, and which ones only pay for active grinding. Grinding points in
a timed event is a decision for the owner, not part of a claim round.
Executions are recorded in `_records_/<date>/event-claims/`, one file per execution.

## How it is done

- Open Events and scan each active event for claim buttons and red dots.
- Page through everything - the Events tab bar scrolls sideways, and
  the owner standing direction (evening of 2026-10-25) is to navigate
  through the pages to finish the red dots, not stop at the first
  page. Where a Claim shows, claim it.
- The hub renders slowly - after tapping a tab, wait a couple of
  seconds before reading the screen, or the previous page content
  will mislead the tap.
- Claim milestone and completion rewards that are already earned.
- Treat an animated or bouncing chest on the Events screen, an
  event card or an event detail page as an unclaimed reward until
  it has been opened and inspected. Do not stop at the rewards
  inside the first detail page. After claiming, return to the
  Events screen and scan again - the event sweep is complete only
  when no bouncing chest or reward red dot remains, or a visible
  chest is proven locked and its unlock condition is recorded.
  For Arms Race in particular, the three point chests are only
  one reward set and do not prove that all Arms Race rewards
  have been claimed.
- Record timed stage state without grinding it, unless the owner asked.

## Standing limits

- Priced buttons are never event claims - the Battle Pass Unlock
  Advanced Rewards at 9.99 dollars and the Legendary Claim All (which
  is a 19.99 dollar purchase) stay untouched.
- The completed Battle Pass login task's yellow Claim More button is
  the same purchase in disguise - verified 2026-10-28, it opens the
  Game Season Advanced Battle Pass panel (extra rewards of all tiers
  after purchase, 9.99 dollars). A completed login task whose points
  were already taken shows Claim More, not Claim; never tap it. The
  bottom Claim All button is the safe completeness check - with
  nothing pending it answers No rewards available to claim.
- Permanent or consequential mechanics are inspected only - Level
  Swap permanently swaps two hero levels; it is never executed
  without the owner decision.

## What is known from 2026-10-25

- Frontline Breakthrough - its milestone chest was claimed, paying red
  diamonds times 50, event chests times 8, speedups and EXP chests as
  itemised in the day play record. Its challenge mini game was not played.
- The Doomsday - all five warzone first kill reward tiers, Doom Walker
  levels 100 to 140, were claimed with the bottom Claim button.
- Arms Race was in its Unit Progression stage with this account at
  0 points and rank 2110 as displayed. No grinding was done.
- Evening sweep of the Events hub (tabs Arms Race, Desert
  Battlefield, Level Swap, Wanted Boss, Community - the bar scrolls).
  Arms Race had rotated to its Base Building stage; this account at
  0 points, chest thresholds 6,250, 12,500 and 30,000; scoring was
  building power plus 1 per point, 1 minute build speedups plus 10
  (burning items, not done) and diamond pack purchases plus 30
  (paid, not done) - nothing free to claim that stage. The red
  target icon with a countdown at the right of the base screen is
  the current Arms Race stage timer.
  Wanted Boss is Code 87, a giant polar bear - appears at server
  time 00:00, tank heroes deal 50 percent extra damage, completing
  1 attack pays chest times 6, food chest times 6, coin chest
  times 6, 5 minute speedups times 5 and red diamonds times 10. It
  was not yet out at inspection time. Its Goals page shows this
  account best single attack at 899,542,636 damage, with the 1.0B
  tier claims still grey.
  Community - the Discord binding reward already read Claimed.
  Level Swap - inspected only, 6 days 22 hours left on the event.
  Desert Battlefield (Desert Storm Battlefield) - registration
  ends in about 2 days 22 hours; an alliance level registration
  event with nothing personal to claim.
- Halloween Check-In, its own base icon - Day 01 claimed on
  2026-10-25 by tapping the center of the Day 01 tile (an earlier
  tap before the panel finished loading had opened the Store
  instead). The reward was a vehicle or decoration type item times
  1 whose name was not fully read. Days 02 to 07 are date locked.
- Season Battle Pass (in the Season hub) - the Daily Tasks login
  task was claimed for plus 100, taking the pass to 16,900 points.
  Daily tasks also listed Buy any pack in the Store 0 of 1 (paid,
  skipped) and Donate Coal to the Alliance Furnace 5 times 0 of 5
  (not done - coal is a cold wave survival resource and the wave
  was approaching; left for the owner or a later round), plus Gain
  Profession EXP 1 of 3. On the Rewards track the 16,200 free tier
  was already claimed and 17,000 was not yet reached; the advanced
  column is locked behind the 9.99 dollar unlock. The Infinity
  Chest needs 35,000. Target Tasks - Kill Polar Zombie tiers all
  complete.

## What is known from 2026-10-26

- After the Arms Race Hero Advancement point chests were claimed,
  the owner could still see a bouncing reward chest connected
  with the Events or Arms Race screen and corrected the report
  that all rewards were done - more rewards remained beyond the
  three point chests. A bouncing chest is therefore a completion
  check failure until the final Events-screen sweep required
  above has been performed.
- The bouncing chest was identified in the follow-up run - it
  is the Arms Race cumulative counter chest at the top left of
  the phase page, above the point track. It stood full at 6 of
  2 after the point chests were claimed, was claimed with one
  tap (gold ticket item 1, pink puzzle-piece items 2, a red gem
  tagged 50), and rolled to the next tier at 6 of 8 in purple.
  Full mechanics live in the arms-race activity metadata; the
  standing lesson for event claims is that a detail page can
  hold several independent reward sets, and each one needs its
  own check.

## Season knowledge gathered the same evening

- Profession Hall - current profession Engineer level 61, EXP
  37,794 of 1,500,000, season cap 70. War Leader is the other open
  choice, Diplomat locked. Learned active skills each carry a Use
  button - Cooperative Research (boosts research speed by 20
  percent for you and a selected ally for 60 minutes), Double
  Exchange, Professional Insights, Rapid Production, Firebomb and
  Build Now, plus Research Now, Siege Banner and Drone Supply
  whose learned state was not confirmed. Skill use is a timing
  decision (the research queue sat idle at 0 of 2), so none was
  used in a claim round.
- Faction Duel (Season card) is a season faction event, not the
  daily VS duel - a Monica and Violet dialog explains the winning
  faction earns large amounts of Rare Soil, which feeds the
  faction ranking only; the winning alliance itself gains nothing
  extra. Rare Soil is the blue crystal resource of the season -
  the Rare Soil War and Rare Soil Showdown cards sit in the same
  hub with about 6 days 22 hours left.
- Season main page - the Assign Rewards control belongs to the
  alliance leader (the alliance leader) and is never touched. Individual
  Goals rows (High-heat Furnace Level, Titanium upgrade) all read
  Claimed.

## What is known from 2026-11-01

Measured in the 0117 events unit (ticker-0104, window mode
642x951, no different-device dialog). Outcome: done, nothing
claimed, nothing spent. Hub tabs swept in full, Community
proving the last tab (a further tab-bar drag moved nothing) -
that drag is the sweep-completeness check, not wasted motion.

- Arms Race, Hero Advancement, Contest Segment Lv.29-30,
  timer 00:44:53, cumulative chest 1/2, chest thresholds
  2,000 / 4,000 / 12,000, tasks 1 Hero Recruitment +400, Use
  at least 2,000 Hero EXP at a time +1, Buy Packs containing
  Diamonds +30. State recorded only: no Arms Race chest was
  claimed in this unit, that stage is the arms-race unit's
  work, and the ranking row figure (6,000) is not reported as
  a stage score - re-confirming the standing rule.
- Frontline Breakthrough, Saving Soldiers 81%, timer
  16:34:12: the Reward row shows green checks on all six
  tiers (100, 10, 18, 18, 3, 3) - all already claimed, no claim
  button.
- Level Swap, timer 16:43:58: inspected only. Permanent hero
  level swap, never executed without the owner decision.
- Rampage Bosses: Mutated Bear Lv.9 at 42.0%, Attacks left 3,
  No Ranking, rewards sent via mail after the event ends. No
  claim button; the Go fight button was not tapped -
  attacking is grinding, not a claim.
- Community: Discord binding reward reads 500 Diamonds
  Claimed. Nothing new.
- No bouncing chest or reward red dot remained on any swept
  tab outside the Arms Race stage left for its own unit.



## What the 2026-11-01 1055 unit added

- Unit events-2026-11-01-0657 by ticker-1034, session
  about 10:51 to 10:55, status done, checked. Full Events
  hub sweep completed, nothing claimable found, nothing
  paid, no Legendary or Battle Pass purchase touched.
  No different-device dialog.
- Arms Race, Unit Progression stage (Contest Segment
  Lv.29-30): score bar at 6,000 against thresholds
  15,000 / 30,000 / 75,000, rank #2110, stage timer
  03:08:03 at entry. No point chest claimable at this
  score; the tier push belongs to the arms-race unit,
  and no grinding was done here. This is a different
  stage from the 0117 unit's Hero Advancement stage, so
  the two reads do not conflict.
- Frontline Breakthrough: Saving Soldiers 100%, bottom
  Reward row all six items green-checked (already
  claimed). The top-right Reward icon took two
  no-change taps and was left alone under the tap-method
  rule; with the reward row fully checked there is no
  unclaimed item visible on this page.
- Level Swap: inspected only, no hero selected, Confirm
  not tapped (permanent mechanic, owner decision only).
- Community: Discord binding reward reads Claimed.
- Rampage Bosses: Mutated Bear Lv.9 at 0.0% damage,
  three Lv.9 bosses (Vulnerable, Appeared, Appeared),
  rewards sent via Mail after the event ends. No claim
  button; Go (attack) was not tapped - attacking is
  grinding, not a claim. The bear damage read 42.0% at
  0117 and 0.0% here; that reads as a new boss cycle,
  recorded as observed, not as a rewind or a
  contradiction.
- Tab bar scrolled to its end after Community; no
  further event tab exists. No bouncing chest was seen
  on any page visited.
- Control note: one transient control error ("target app
  exited") mid-unit proved false - the game process was
  still present and the page state was unchanged on
  re-select. A single such error is unverified until a
  re-select confirms it. Tracker marked done. Game left
  on the base screen.

## What the 2026-11-01 1348 unit added

- Unit events-2026-11-01-1057 by ticker-1334, session
  about 13:42 to 13:50, status done, checked only. Full
  hub sweep, all five tabs visited, nothing claimed, no
  bouncing chest and no unclaimed reward red dot left on
  any visited page. No diamonds or money spent, no paid
  button tapped. Game left on the base screen.
- Arms Race, Unit Progression, Contest Segment Lv.29-30:
  score 0, point chests at 15,000, 30,000 and 75,000 all
  unearned, cumulative chest at 1 of 2, rank 2,110, phase
  timer about 00:17 remaining at about 13:44 local, so
  the phase ends around 14:01 local. Nothing claimable
  here; no grinding was done in this claim unit. Flag
  for the arms-race unit: its 14:03 slot falls after this
  phase end, so that unit should expect a fresh phase,
  not this stage's chests.
- Level Swap: inspect only, two empty hero slots,
  Confirm not touched. Nothing to claim.
- Rampage Bosses: Mutated Bear Lv.9, 0 of
  35,000,000,000,000 HP at 0.0 percent, one Vulnerable
  and two Appeared cards. No claim button on the page;
  the Go button is a fight entry, not a claim, and no
  fight was started. Rewards go via Mail after the event
  ends. Consistent with the 1055 new-boss-cycle read
  (0.0 percent after 42.0 percent at 0117).
- Community: Discord binding reward reads Claimed.
- Frontline Breakthrough: Saving Soldiers 100 percent,
  all six Reward tiles show green checks. The Challenge
  button is active play, not a claim, and was not tapped.


## What the 2026-11-01 2200 unit added

- Unit events-2026-11-01-1857 by ticker-2142, session
  about 21:55 to 22:00, status partial. Four hub pages
  were checked and nothing was claimable on them; the
  remaining hub tabs were not reached before the pass
  budget ended, so the sweep is incomplete and the
  tracker is untouched.
- Events hub opened from the base Events icon (red 1
  badge). Arms Race, Base Building stage, Contest
  Segment Lv.29-30, timer 00:04:19 at first sight:
  account score 0, chest thresholds 6,250, 12,500 and
  30,000 all unreached. Noted only; Arms Race is its own
  unit type and nothing was ground or claimed here.
- Desert Battlefield page: registration ends in 2d
  20:03:46, Task Force A and B, Sign Up button. This is
  an alliance-level registration with nothing personal
  to claim, so Sign Up was left untouched - consistent
  with the 2026-10-25 registration-only read.
- Wanted Boss page: Code 87, appears at server time
  00:00, Go button countdown 19:03:22 at first sight, so
  the boss is not out. The 1-attack reward list is a
  future payout, not a claim. Its tab carries a red dot
  that survived the visit, so the Rewards subpage was
  opened: it holds only the Ranking Reward table (No.1,
  No.2, No.3, No.4 to 10) with no claim button. Lesson:
  a surviving Wanted Boss red dot does not by itself
  prove a claim - the Rewards subpage must be opened
  and can prove to hold only a ranking table. No claim
  exists on this page at this check.
- Community page: the Discord binding reward reads
  Claimed (500 diamonds), so nothing new is claimable
  there - unchanged across every 2026-11-01 sweep.
- Tab-bar method note: the tab bar scrolls sideways;
  two drags moved it as far as Community, and the tabs
  beyond Community (Level Swap and Winter Battlefield
  in earlier hub listings) were not opened in this unit.
  A sweep that stops at Community is incomplete by the
  standing rule, not a full sweep.
- Closing navigation lesson: the Rewards panel closed
  cleanly with its X back to Wanted Boss, but the Events
  panel back arrow then produced no observed change, so
  the game was left on the Wanted Boss page in the
  Events hub. The next executor should expect to start
  there, not on the base screen - the same start-state
  rule as the 1813 train unit's trucks-view close.
- Incidental train note, not a train action: a base
  "Boarding closes in" banner was visible behind the hub
  during this unit (00:01:44 falling to 00:00:45); the
  train unit of this same pass already confirmed the
  account aboard carriage 2, so no train action was
  taken here.
- Nothing claimed, nothing spent, no paid button tapped,
  no Sign Up tapped, no Level Swap executed.

## What the 2026-11-02 0050 unit added

- Unit events-2026-11-01-2257 by ticker-0034, session
  about 00:48 to 00:50, status done - inspected, nothing
  claimable. Events hub opened from the base right rail
  at norm 927,137. No bouncing chest was seen on the hub.
- Arms Race, Unit Progression stage, read live: account
  score 0, rank #2110 [AP3x]Bears Lair, stage countdown
  about 01:11. Point chests at 15,000, 30,000 and 75,000
  are all unearned at 0 points, and the top chest reads
  0/2, so no Arms Race chest was claimable. No grinding
  was done; Arms Race point work belongs to the
  arms-race unit, not this sweep.
- Wanted Boss, Code 87, read live: appears at server
  time 00:00, Go countdown about 16:10, so the boss is
  not out yet. Its Rewards panel shows ranking tiers
  No.1 to No.10 as prospective rewards with no Claim
  buttons. The red dots on the Wanted Boss tab and Go
  button are the event's active markers, not claims -
  no Claim button exists on the page before the boss
  appears. Go was not tapped and no attack was started.
  This strengthens the 2200 lesson: a surviving Wanted
  Boss red dot does not by itself prove a claim.
- Desert Battlefield and Community tabs were not
  reopened in this unit: the activity metadata records
  Desert Battlefield as an alliance registration event
  with nothing personal to claim, and Community's
  Discord binding reward as already Claimed. Tabs
  further right than Community were not reached, so
  like the 2200 sweep this unit's sweep stops at
  Community and is incomplete by the standing rule for
  the unreached tabs - recorded honestly, not as a full
  sweep. Events hub closed with its back arrow, leaving
  the game on the base screen.
  Evidence in `_records_/2026-11-02/event-claims/0050-queue-run.md`.

## What the 2026-11-02 0359 unit added - partial, Escape crash recurrence

- Unit events-2026-11-02-0257 by ticker-0334, session
  about 03:52 to 03:59, status partial. The hub sweep
  was cut short by an app crash at the pass budget
  end; the tracker is untouched and the next tick
  re-produces this regular.
- Events hub opened from the base right rail. It
  landed on the current Arms Race phase page, Hero
  Advancement, Contest Segment Lv.29-30, read live:
  account score 40,500, rank #2110 [AP3x]Bears Lair,
  phase countdown 02:08:44 falling. Point chest
  thresholds 2,000, 4,000 and 12,000 are all passed at
  this score. The top-left cumulative chest reads 6/2.
  Score-context note: this 40,500 is the Hero
  Advancement phase score, not the 0050 unit's Unit
  Progression stage score of 0 - different sub-pages,
  so the two reads do not contradict each other.
- The 2,000 point chest was tapped: it opened only a
  reward preview popup ("Valued: 2,360" - Skill Medal
  200, Arms Race Badge 1, Coin Chest (SR) 4, Food
  Chest (SR) 4, Iron Chest (SR) 4, 5m Speed-up 8) with
  no Claim button visible. A preview-only tap is
  consistent with that chest already having been
  claimed by an earlier arms-race unit, but the
  claimed state was not verified before the crash
  below, so no chest state is asserted here. The
  4,000 and 12,000 chests and the cumulative chest
  were not tapped. No grinding was done; Arms Race
  point work belongs to the arms-race unit. No paid
  button was tapped: no Legendary Take All, no Battle
  Pass unlock, no Level Swap.
- App crash, self-inflicted, recovered: to close the
  chest preview popup, an Escape key was sent.
  LastWar quit immediately after the key reached it.
  This re-affirms the standing rule recorded in the
  workspace notes - never use Esc (or Ctrl-Cmd-F) on
  this app, it crashes it. The Escape key must not be
  used on LastWar again. Recovery: the app was
  relaunched and came back directly to the base
  screen (power 149,196,915, no login demand, no
  "active on a different device" dialog). Nothing was
  lost beyond this unit's unfinished sweep.
- Not done in this unit: the 4,000 and 12,000 point
  chests, the cumulative chest, and the remaining hub
  tabs (Desert Battlefield, Wanted Boss, Community
  and further right tabs) were not swept. The next
  tick's events unit resumes the sweep; the arms-race
  unit owns any unclaimed Arms Race chest.
  Evidence in `_records_/2026-11-02/event-claims/0359-queue-run.md`.


## What the 2026-11-02 0910 unit added - full hub sweep, nothing claimable

- Unit events-2026-11-02-0657 by ticker-0904, session
  about 09:10, status done. Full Events hub sweep
  performed, nothing claimable anywhere in the hub,
  nothing claimed. Evidence in
  `_records_/2026-11-02/event-claims/0910-queue-run.md`.
- Entry: the game was left on a leftover HOT DEALS and
  Weekly Pass shop panel from a previous session; that
  panel was closed with its back arrow before the sweep
  started. No paid button was touched: the Legendary
  Take All $19.99 and the Coin Weekly Pass Renew $4.99
  buttons were visible on that panel and were left
  alone. No "active on a different device" dialog
  appeared.
- Arms Race (Tech Research, Contest Segment Lv.29-30,
  about 00:52 left at first read): cumulative counter
  chest at top left reads 6/8, not full, nothing to
  claim. The three point chests (thresholds 6,250 /
  12,500 / 30,000) show no claim state; one tap on the
  6,250 chest produced no change, consistent with the
  phase score still at 0 as recorded by the 0608
  arms-race unit. The bottom ranking row still shows the
  finished Hero Advancement result (#2110 [AP3x]Bears
  Lair, 40,500), whose ranking chest was already
  inspected in the 0608 unit (contents preview only, no
  Claim button). No bouncing chest, no reward red dot
  on this page.
- Cumulative-chest denominator note, kept as two
  phase-page reads, not merged: this Tech Research
  page reads 6/8, while the 0359 Hero Advancement page
  read 6/2. Until a unit reads both pages in one pass,
  do not treat either figure as the standing cumulative
  total - the counter may be per-phase, and merging the
  two would invent a total neither page showed.
- Desert Battlefield (Desert Storm Battlefield):
  registration ends in 2d 08:52, registration limited
  to top-32 power-rank alliances. Alliance-level
  registration event, nothing personal to claim.
- Wanted Boss (Code 87, giant polar bear, appears at
  server time 00:00, countdown about 07:50 at read):
  Goals page re-checked - best single attack
  899,542,636 against tiers 1.0B / 1.5B / 2.0B / 2.5B /
  3.0B, all above the best, all grey, nothing
  claimable. The red dot seen on the Wanted Boss tab in
  one hub render is the upcoming-boss marker, not a
  reward: the page itself and its Goals list were both
  opened and inspected and hold no claim. This
  strengthens the 0050 lesson - a surviving Wanted Boss
  red dot does not by itself prove a claim. Attacking
  the boss is grinding, not a claim, and the boss is not
  out yet.
- Community: Discord binding reward reads Claimed (500
  diamonds tier), unchanged from prior knowledge.
  Nothing to claim.
- Hub completeness: the tab bar was dragged to its end;
  the four tabs above are the whole hub (Arms Race,
  Desert Battlefield, Wanted Boss, Community). No
  Zombie Invasion tab - the event ended 2026-10-30,
  consistent with the 2026-10-28 unit 066 record.
- Exit failure, for the next unit: the game was left on
  the Events hub Wanted Boss page, because the hub back
  arrow did not respond to background clicks (two
  attempts; system guidance says background clicks do
  not reach that control). The exit to base was left
  for the next unit's navigation rather than forcing
  it. The next unit should bring the game window to the
  foreground before using the hub back arrow, or exit
  by another route.

## What the 2026-11-02 1250 unit added - full hub sweep, nothing claimable

- Unit events-2026-11-02-1057 by ticker-1234, session
  about 12:51, status done. Full Events hub sweep
  performed, nothing claimable anywhere in the hub,
  nothing claimed. Evidence in
  `_records_/2026-11-02/event-claims/1250-queue-run.md`.
- Camera recovery lesson, qualifying the 0047 lesson:
  the train unit had left the camera panned to the base
  edge with the side icon rails hidden; drags moved the
  camera but did not restore the rails, and taps on a
  building and on empty map produced no change. Per
  rule R2 the method was switched: the game window was
  closed and relaunched, which restored the full base
  UI with rails intact, state intact, and no login or
  verification demanded. No "active on a different
  device" dialog appeared. Drags plus an empty-map tap
  do NOT always restore hidden rails - relaunch is the
  verified fallback, and it costs nothing here.
- Arms Race (Drone Boost, Contest Segment Lv.29-30,
  about 01:10:39 left at first read): cumulative counter
  chest at top left reads 6/8, not full, nothing to
  claim. Score reads 0; the three point chests
  (thresholds 1,500 / 10,000 / 30,000) show no claim
  state. The bottom ranking row still shows the
  finished Hero Advancement result (#2110 [AP3x]Bears
  Lair, 40,500), whose ranking chest was already
  inspected in earlier units (contents preview only, no
  Claim button). No bouncing chest, no reward red dot
  on this page. Phase work itself belongs to the
  arms-race unit, not this sweep. Phase note: the phase
  has rotated from Tech Research (0910) to Drone Boost,
  so the point-chest thresholds differ (1,500 / 10,000 /
  30,000 here against 6,250 / 12,500 / 30,000 at 0910) -
  do not carry thresholds across phases.
- Wanted Boss (Code 87, giant polar bear, appears at
  server time 00:00, countdown about 04:09:55 at read):
  Goals page re-checked - best single attack
  899,542,636 against tiers 1.0B / 1.5B / 2.0B / 2.5B /
  3.0B, all above the best, all Claim buttons grey,
  nothing claimable. Attacking the boss is grinding,
  not a claim, and the boss is not out yet.
- Community: Discord binding reward reads Claimed,
  unchanged from prior knowledge. Nothing to claim.
- Desert Battlefield (Desert Storm Battlefield):
  registration ends in 2d 05:09, registration limited
  to top-32 power-rank alliances. Alliance-level
  registration event, nothing personal to claim.
- Hub completeness: the tab bar was dragged to its end;
  the four tabs above are the whole hub (Arms Race,
  Desert Battlefield, Wanted Boss, Community). No
  Zombie Invasion tab - the event ended 2026-10-30,
  consistent with unit zombie-invasion-zombie-2026-10-28-066.
- Game left on the Events hub Desert Battlefield page
  at unit close, for the next unit's navigation.

## What the 2026-11-02 1850 unit added - contested stop, failed, nothing claimed

- Unit events-2026-11-02-1457 by ticker-1834, session
  about 18:44 to 18:50, status failed (contested),
  tracker untouched. No Events screen was reached and
  nothing was claimed. Evidence in
  `_records_/2026-11-02/event-claims/1850-queue-run.md`.
- Contested counting clarified, cross-unit within one
  pass: the "active on a different device" dialog
  returned for a third time in this pass, after two
  Confirm takeovers earlier in the same pass (during
  the trucks unit, at norm 501,568 each, the app
  exiting and being reopened each time). Per the owner
  rule of 2026-10-27, after two takeovers a returning
  dialog means the owner is likely playing on his phone,
  so the pass stopped: the dialog was NOT confirmed a
  third time, the device token was released, and the
  game was left with the dialog on screen, leaving the
  owner session on the other device undisturbed.
- Contrast, same evening: the ticker-1904 radar unit
  (1913) saw the dialog once, confirmed once, and the
  dialog did not return, so that pass continued - not
  contested. The contested stop is therefore the third
  return in a pass, counting takeovers across the
  units of that pass, not per unit.

## What the 2026-11-02 2113 unit added - full hub sweep, Wanted Boss rotated to Code 64

- Unit events-2026-11-02-1857 by ticker-2104, session
  about 21:05 to 21:13, status done. Full sweep
  performed, nothing claimable anywhere in the hub,
  nothing claimed. Evidence in
  `_records_/2026-11-02/event-claims/2113-queue-run.md`.
- Arms Race, Unit Progression (Contest Segment
  Lv.29-30, about 00:49 left at first read):
  cumulative counter chest at top left reads 0/2,
  not full, nothing to claim. Score reads 9,300; the
  three point chests (thresholds 15,000 / 30,000 /
  75,000) are all above the score, no claim state.
  The bottom ranking row shows #2110 [AP3x]Bears
  Lair, 9,300. Phase work itself belongs to the
  arms-race unit, not this sweep. No bouncing chest,
  no reward red dot on this page.
- Desert Battlefield (Desert Storm Battlefield):
  Battle Day 2026-11-6, 03:00-03:30, Participants
  19/20 (including you), stamped Enlisted.
  Registration ends in 1d 20:48. Alliance
  registration event; Select Time / Select
  Participants were not tapped, nothing personal to
  claim.
- Wanted Boss rotation, measured 2026-11-02: now
  Code 64 (was Code 87), a giant gorilla; Missile
  Vehicle heroes deal 50% extra damage (was tank
  heroes for Code 87). Appears at server time 00:00,
  Go countdown about 19:48 at read - not out yet,
  attacking is grinding, not a claim. Goals page:
  best single attack 852,929,736 against tiers 1.0B
  / 1.5B / 2.0B / 2.5B / 3.0B, all Claim buttons
  grey, nothing claimable.
- Community: Discord binding reward reads 500
  Claimed, unchanged. Nothing to claim.
- Tab bar dragged to its end: the four tabs above
  are the whole hub (Arms Race, Desert Battlefield,
  Wanted Boss, Community). No Zombie Invasion tab -
  the event ended 2026-10-30, consistent with unit
  zombie-invasion-zombie-2026-10-28-066.
- No diamonds, money, speedups or other resources
  spent. Game left on the base screen.


## What the 2026-11-02 2341 unit added - full hub sweep, nothing claimable, phase rotated

- Unit events-2026-11-02-2257 by ticker-2334, session
  about 23:34 to 23:41, status done. Full hub sweep
  performed, nothing claimable anywhere in the hub,
  nothing claimed. Evidence in
  `_records_/2026-11-02/event-claims/2341-queue-run.md`.
- Arms Race phase rotated since the 2113 sweep: now
  Tech Research phase, Contest Segment Lv.29-30,
  score 0, cumulative chest 0/2 (not full, not
  bouncing), point chests 6,250 / 12,500 / 30,000
  all locked. The bottom rank row reads #2110
  [AP3x]Bears Lair with 9,300 - phase context only,
  not a claim, and not the current phase score.
  Pushing the phase is the arms-race unit's job,
  not this sweep.
- Desert Storm Battlefield: Battle Day 2026-11-6,
  03:00-03:30, Participants 19/20 (including you),
  stamped Enlisted on Task Force A. Registration
  ends in 1d 18:20:11 at read (about 2.5 hours on
  from the 2113 read, consistent). Alliance
  registration event; Select Time / Select
  Participants were not tapped, nothing personal
  to claim.
- Wanted Boss: still Code 64 (giant gorilla,
  unchanged since the 2113 sweep); Missile Vehicle
  heroes deal 50% extra damage. Appears at server
  time 00:00, Go countdown about 17:19 at read -
  not out yet, attacking is grinding, not a claim.
  Goals page: best single attack 852,929,736
  against tiers 1.0B / 1.5B / 2.0B / 2.5B / 3.0B,
  all Claim buttons grey, nothing claimable.
  Discrimination rule for sweeps: the Wanted Boss
  tab carries a small red dot, but the page itself
  holds no claimable reward - the dot marks the
  live event, not a pending claim. A tab dot alone
  is not claim proof.
- Community: Discord binding reward reads 500
  Claimed, unchanged. Nothing to claim.
- Tab bar dragged to its end: the four tabs above
  are the whole hub (Arms Race, Desert Battlefield,
  Wanted Boss, Community). No Zombie Invasion tab -
  the event ended 2026-10-30, consistent with unit
  zombie-invasion-zombie-2026-10-28-066.
- No bouncing chest, no reward red dot on any swept
  page other than the Wanted Boss tab dot explained
  above. No diamonds, money, speedups or other
  resources spent. Game left on the base screen.
- Result statistics: tabs_swept 4, claimed_count 0,
  target 1 full hub sweep performed, achieved 1,
  verified yes.



## What the 2026-11-03 0318 unit added - full hub sweep, 0 claimed, Desert Storm registered, Boss Code 64

- Ticker-0304, unit events-2026-11-03-0257, about 03:18
  local, status done. Evidence in
  `_records_/2026-11-03/event-claims/0318-queue-run.md`.
- Events hub swept tab by tab, with a sideways tab-bar
  scroll to reach the last tab.
- Arms Race (first tab): Base Building phase, contest
  segment Lv.29-30, score 9,300, countdown 02:42:45. Tier
  chests at 6,250, 12,500 and 30,000; the tier-1 chest
  was already claimed in the earlier arms-race unit and
  tiers 2 and 3 are locked by score. No phase action was
  taken here: Arms Race work belongs to its own unit,
  and no grinding was done. This read is a hub sweep
  only and is not folded into the arms-race profile.
- Desert Storm Battlefield: Registration ends in 1d
  14:42:34, Battle Day 2026-11-6 03:00-03:30,
  Participants 19 of 20 including this account: already
  registered, no claim button, nothing changed.
- Wanted Boss (Code 64): appears at server time 00:00,
  Go button with a 13:42:24 countdown. Go would start
  an attack, which is grinding, not a claim, so it was
  not tapped; the 1-attack rewards are not earned.
- Community: the link reward reads Claimed, no new
  claim.
- Final sweep: no bouncing chest and no claimable reward
  red dot remained on the hub tabs checked. 0 rewards
  claimed, no purchase tapped.

## What the 2026-11-03 0808 unit added - full hub sweep, 0 claimed, Drone Boost phase, Desert Storm registered, Boss Code 64

- Ticker-0804, unit events-2026-11-03-0657, about 08:08
  local, status done. Evidence in
  `_records_/2026-11-03/event-claims/0808-queue-run.md`.
- Events hub swept tab by tab, with sideways tab-bar
  scrolls to reach the last tab and back to the first.
- Arms Race (first tab): Drone Boost phase, contest
  segment Lv.29-30, score 9,300, rank 2110, countdown
  01:53:47 falling to 01:52:21 on the final sweep. Tier
  chests at 1,500, 10,000 and 30,000; tier 1 already
  claimed in an earlier unit and tiers 2 and 3 are locked
  by score. Cumulative chest at top left reads 0 of 2,
  not claimable. No phase action was taken here - Arms
  Race work belongs to its own unit, and no grinding was
  done. This read is a hub sweep only and is not folded
  into the arms-race profile. Note the phase and tier
  thresholds differ from the 0318 hub read (Base
  Building phase, tiers 6,250 / 12,500 / 30,000): tier
  thresholds are per-phase, so do not carry them across
  a phase rotation.
- Desert Storm Battlefield: Registration ends in 1d
  09:52:38, Battle Day 2026-11-6 03:00-03:30,
  Participants 19 of 20 including this account - already
  registered, no claim button, nothing changed. The
  registration countdown is consistent with the 0318
  read (1d 14:42:34 then, about 4h50m earlier).
- Wanted Boss (Code 64): appears at server time 00:00,
  Go button with a 08:53:34 countdown. Go would start
  an attack, which is grinding, not a claim, so it was
  not tapped; the 1-attack rewards are not earned. Its
  Rewards panel was inspected read-only: ranking reward
  tiers No.1 to No.4-10 only, no claim button.
- Community: the 500 Diamonds row reads Claimed, no new
  claim.
- Discrimination rule, confirmed again: the red dot on
  the Wanted Boss tab is the boss countdown indicator,
  not a claim - it stays lit while the boss is not yet
  out. A tab dot alone is not claim proof.
- Final sweep back to Arms Race: no bouncing chest and
  no claimable reward red dot remained on the hub tabs
  checked. 0 rewards claimed, no purchase tapped.

## What the 2026-11-03 1217 unit added - full hub sweep, 0 claimed, Hero Advancement phase, Boss Code 64 not yet out

- Ticker-1204, unit events-2026-11-03-1057, about
  12:12 to 12:17 local, status done. Evidence in
  `_records_/2026-11-03/event-claims/1217-queue-run.md`.
  Events hub opened from the base view. Four tabs
  walked in order, waiting for each page to render
  before reading it.
- Arms Race - Hero Advancement phase: personal score
  shown 41,500, phase countdown 01:45 at entry.
  Cumulative chest top left reads 6/8, not full,
  nothing to claim. Point chests at 2,000, 4,000 and
  12,000: tapping the 2,000 chest opened only its reward
  preview (Valued 2,360: Skill Medal 200, Arms Race
  Badge 1, Coin Chest SR 4, Food Chest SR 4, Iron Chest
  SR 4, 5m Speed-up 8), with no Claim button in the
  popup. The popup was closed by tapping outside it. No
  point chest was claimed in this unit; the earlier
  arms-race unit of this phase already worked the tier-3
  target, and no chest here presented a claim action.
  Lesson: a point chest that opens a preview with no
  Claim button is not a missed claim - close it and move
  on. Scoring rows below (Hero Recruitment, Hero EXP,
  diamond packs) are scoring paths, not claims, and were
  not touched. This unit does no Arms Race grinding.
  This read is a hub sweep only and is not folded into
  the arms-race profile.
- Desert Storm Battlefield: registration ends in 1d
  05:44:47, Battle Day 2026-11-6 03:00 to 03:30,
  Participants 19/20 including this account. Already
  registered. No claim button, no red dot, no bouncing
  chest. The registration countdown is consistent with
  the 0808 read (1d 09:52:38 then, about 4h08m earlier).
- Wanted Boss - Code 64: boss rotated from Code 87 to
  Code 64 (rotation already recorded in the 2113 unit).
  Appears at server time 00:00; Go countdown read
  04:44:07 at entry, so the boss is not out yet. Missile
  Vehicle heroes deal 50 percent extra damage. Rewards
  panel checked on both tabs: Ranking Reward tiers No.1
  to No.4-10 are payout tables with no Claim button;
  Individual Reward tiers pay on 1, 2 and 3 attacks,
  also with no Claim button. Nothing claimable before
  the boss appears.
- Caveat, recorded not resolved: the Wanted Boss tab
  itself carries a small red dot in the tab bar, but its
  page and both Rewards tabs show no claimable item. The
  dot is consistent with a new-boss notice rather than a
  pending claim; the next events unit re-checks it after
  the boss appears. This matches the 2341 "live-event
  marker" and 0808 "countdown indicator" readings: a tab
  dot alone is not claim proof.
- Community: Discord binding reward reads 500 diamonds,
  Claimed. Nothing further to claim on this page.
- Outcome: done. No earned reward was left unclaimed on
  any tab walked; nothing was claimed because nothing
  presented a claim action. No purchase button was
  tapped; the Battle Pass paid buttons were never shown
  in this sweep. Costs: about 5 minutes of unit time,
  0 diamonds. Game left on the base view.

## What the 2026-11-04 0245 unit added - full hub sweep, 0 claimed, General's Trial badge explained, back-arrow centre corrected

- Ticker-0234, unit events-2026-11-03-2257, about 02:43 to 02:45 local, status done. Evidence in `_records_/2026-11-04/event-claims/0245-queue-run.md`.
- Tabs seen in this sweep, in order: Arms Race, Desert Battlefield, General's Trial, Wanted Boss, Community. A further tab-bar drag to the right produced no change, so Community is the last tab. No Zombie Invasion tab is present in the hub, which re-confirms the zombie chain stays closed.
- Arms Race page: current phase Tech Research, Contest Segment Lv.29-30, 03:17:16 left at entry. Score 0, cumulative chest 3/8 (not full, not claimable), point chests at 6,250 / 12,500 / 30,000 all unreached at score 0. Scoring paths are Tech Power (+1 per point), 1-minute Research Speed-ups (+10, burning items - not done) and diamond packs (+30, paid - not done). No Arms Race grinding was done in this unit; that belongs to the arms-race unit type. Phase state is recorded here for that unit's next run.
- Desert Storm Battlefield: Registration ends in 15:17:04, Battle Day 2026-11-6 03:00-03:30, Participants 19/20 (including You) - already registered, no Claim button, nothing to claim. The Select Time and Select Participants buttons were not tapped (alliance registration choices, not claims).
- General's Trial (carries a red 1 badge on its tab): Solo Challenge page, 2d 15:16:26 left, "Defeat 3/10 instructors to obtain" rewards row. The Rewards panel reads "Get rewards for all completed challenges at the end of the event!" with milestones 3/10, 3/15, 3/20, 3/25 - none complete, no Claim button anywhere. The Challenge buttons are grinding and were not tapped. The tab badge is therefore explained as a new-event marker, not a claimable reward - the same tab-dot-alone-is-not-claim-proof lesson as the 1217 Wanted Boss caveat.
- Wanted Boss Code 39: appears at server time 00:00, aircraft heroes deal 50 percent extra damage, Go button countdown 14:15:37 at entry (boss not out yet). "Complete 1 attacks to get the following rewards" - no attack was made in this claim unit. Goals page inspected: best single attack 1,097,397,868 against tiers 1,500,000,000 / 2,000,000,000 / 2,500,000,000 / 3,000,000,000 / 4,000,000,000 - no tier reached, no Claim button. Evidence caveat: the Goals screenshot file failed to persist, so these figures are recorded from the live OCR element read, a weaker read than a persisted screenshot.
- Community: Discord binding reward reads Claimed.
- 0 claims in this unit. No priced button, no paid unlock, no Challenge or Go button was tapped.
- Leaving the hub, back-arrow centre corrected: the first back-arrow tap at norm 86,952 closed the Goals panel to the Wanted Boss page, a second tap at the same point did nothing, and a tap at the corrected arrow centre norm 132,952 returned to the base screen on the first tap. Back-arrow centre for the Events hub is 132,952, not 86,952 (the latter hits the corner avatar icon). The same correction held for the Secret Command Post exit in the same pass (see the 0248 section in the secret-missions profile).
- No bouncing chest or unexplained red dot remains except the General's Trial tab badge, explained above as a new-event marker with rewards payable only at event end. Costs: about 2 minutes of unit time, 0 diamonds.
## Open questions

- Which recurring events hold claims that expire unclaimed.
- The exact item name of the Halloween Day 01 reward.
- Whether the Battle Pass Donate Coal daily should be done on cold
  wave days, and the coal cost per donation.
- What the Wanted Boss Code 87 fight pays in practice when it is
  out at server 00:00. (2026-11-02 2113 update: the boss has rotated to Code 64, a giant gorilla, with Missile Vehicle heroes dealing 50% extra damage; best single attack read 852,929,736 against tiers 1.0B / 1.5B / 2.0B / 2.5B / 3.0B, all Claim buttons grey - the Code 87 payout question is moot until it rotates back.)
- Hub back arrow unresponsive to background clicks (0910 unit) - foreground-first exit still to be verified by a later unit. (2026-11-02 0935 update: the trucks unit's hub back arrow responded once its centre was re-measured at norm 158,947 after taps near 97,906 missed - point accuracy, not background clicks alone, may be the cause; the foreground-first exit is still to be verified by an events unit.) (2026-11-02 1250/1300 update: window close-and-relaunch is now a verified exit and recovery route - the 1250 unit restored hidden side rails by relaunch, and the 1300 passes unit exited the stalled hub by relaunch, both with state intact and no login or device dialog; the foreground-first exit itself is still unverified.) (2026-11-04 0245 update: back-arrow centre corrected - taps at norm 86,952 do nothing because that point hits the corner avatar icon; the corrected centre norm 132,952 returned to the base screen on the first tap, verified in both the Events hub exit and the Secret Command Post exit in the same pass. The foreground-first exit itself is still unverified.)

## What the 2026-11-04 0519 unit added - full hub sweep, 0 claimed, Arms Race phase ends inside the next hour

- Ticker-0504, unit events-2026-11-04-0257, about 05:12 to 05:19 local, status done. Evidence in `_records_/2026-11-04/event-claims/0519-queue-run.md`. Computer session cc-419 dropped mid-unit and was restarted as cc-420 with no game state lost.
- Tabs seen in this sweep, in order: Arms Race, Desert Battlefield, General's Trial, Wanted Boss, Community. No Zombie Invasion tab is present in the hub, which re-confirms the zombie chain stays closed (no fresh chain seeded in this pass).
- Grounding notes: the base Events button grounds at norm (935,145) - a tap at (885,150) hit the gold hexagon beside it and opened nothing; the tab bar shifts between openings, so each tab was re-read before tapping, and a drag of the tab bar from norm 800,131 to 400,131 was needed to reveal the Wanted Boss and Community tabs.
- Arms Race page: current phase Tech Research, Contest Segment Lv.29-30, 00:45:24 left at entry. Score 0, cumulative chest 3/8 (not full, not claimable), point chests at 6,250 / 12,500 / 30,000 all unreached at score 0. No Arms Race grinding was done in this unit; that belongs to the arms-race unit type. Phase state is recorded here for that unit's next run - the phase ends inside the next hour.
- Desert Storm Battlefield: Registration ends in 12:44:48, Battle Day 2026-11-6 03:00-03:30, Participants 19/20 (including You) - already registered, no Claim button, nothing to claim. The Select Time and Select Participants buttons were not tapped (alliance registration choices, not claims).
- General's Trial: Solo Challenge page, 2d 12:44:11 left, "Defeat 3/10 instructors to obtain" rewards row, next instructor Lv.4 Vanguard, Suggested Power 10,928,500. The Rewards panel (opened with a fresh-grounded tap at norm 830,280 after a tap at 875,230 did nothing) reads "Get rewards for all completed challenges at the end of the event!" with milestones 3/10, 3/15, 3/20, 3/25 - none complete, no Claim button anywhere. The Challenge buttons are grinding and were not tapped.
- Wanted Boss Code 39: Go button countdown 11:41:45 at entry (boss not out yet), aircraft heroes deal 50 percent extra damage. "Complete 1 attacks to get the following rewards" - no attack was made in this claim unit. Goals page inspected: best single attack 1,097,397,868 against tiers 1,500,000,000 / 2,000,000,000 / 2,500,000,000 / 3,000,000,000 / 4,000,000,000 - no tier reached, no Claim button.
- Community: Discord binding reward reads Claimed.
- 0 claims in this unit. No priced button, no paid unlock, no Challenge or Go button was tapped.
- Leaving the hub: the back-arrow tap at norm 132,952 closed the Goals panel to the Wanted Boss page, and a second tap at the same point from the Community page returned to the base screen on the first tap. Back-arrow centre for the Events hub is re-confirmed at norm (132,952).
- Countdown consistency check, no contradiction: the Desert registration (15:17:04 at 0245 to 12:44:48 here), General's Trial (2d 15:16:26 to 2d 12:44:11) and Wanted Boss (14:15:37 to 11:41:45) countdowns all stepped down by about the elapsed time between the units. Costs: about 7 minutes, 0 diamonds.

## What the 2026-11-04 0843 unit added - full hub sweep, 0 claimed, Arms Race now Base Building phase

- Unit events-2026-11-04-0657 by ticker-0834, about 08:42 to 08:43 local, status done as checked only. Evidence in `_records_/2026-11-04/event-claims/0843-queue-run.md`. No priced button, no paid unlock, no Challenge or Go button was tapped. No different-device dialog appeared.
- Tabs seen in this sweep, in order: Arms Race, General's Trial (tab bar shift sent the first Desert tap to General's Trial; Desert Battlefield was then opened with a freshly grounded tap), Desert Battlefield, Wanted Boss, Community. The tab-bar shift repeats the 0519 lesson: re-read each tab before tapping. No Zombie Invasion tab is present in the hub, which re-confirms the zombie chain stays closed (no fresh chain seeded in this pass).
- Arms Race page: current phase Base Building, Contest Segment Lv.29-30, 01:18:14 left at entry. Score 0, cumulative chest 3/8 (not full, not claimable), point chests at 6,250 / 12,500 / 30,000 all unreached at score 0. The phase changed since the 0519 unit's Tech Research phase (which ended inside the next hour then). No Arms Race grinding was done in this unit; that belongs to the arms-race unit type. Phase state is recorded here for that unit's next run.
- General's Trial: Solo Challenge page, 2d 09:17:58 left, "Defeat 3/10 instructors to obtain" rewards row, next instructor Lv.4 Vanguard, Suggested Power 10,928,500. The Rewards panel reads "Get rewards for all completed challenges at the end of the event!" with milestones 3/10, 3/15, 3/20, 3/25 - none complete, no Claim button anywhere. The Challenge buttons are grinding and were not tapped.
- Desert Storm Battlefield: Registration ends in 09:17:05, Battle Day 2026-11-6 03:00-03:30, Participants 19/20 (including You) - already registered, no Claim button, nothing to claim. The Select Time and Select Participants buttons were not tapped (alliance registration choices, not claims).
- Wanted Boss Code 39: Go button countdown 08:16:51 at entry (boss not out yet), aircraft heroes deal 50 percent extra damage. "Complete 1 attacks to get the following rewards" - no attack was made in this claim unit, and the Go button was not tapped. Goals page inspected: best single attack 1,097,397,868 against tiers 1,500,000,000 / 2,000,000,000 / 2,500,000,000 / 3,000,000,000 / 4,000,000,000 - no tier reached, no Claim button.
- Community: Discord binding reward reads Claimed.
- Countdown consistency check, no contradiction: the Desert registration (12:44:48 at 0519 to 09:17:05 here), General's Trial (2d 12:44:11 to 2d 09:17:58) and Wanted Boss (11:41:45 to 08:16:51) countdowns all stepped down by about the elapsed 3 hours 24 minutes between the units.
- Leaving the hub: the back-arrow tap at norm 132,952 closed the Goals panel to the Wanted Boss page, and a second tap at the same point from the Community page returned to the base screen on the first tap. Back-arrow centre for the Events hub is re-confirmed at norm (132,952). Game left on the base view.

## What the 2026-11-04 1834 unit added - screen-capture failure, thirteenth consecutive pass, nothing read

- Unit events-2026-11-04-1457 by ticker-1834, about 18:34 to 18:37 local, status failed. Evidence in `_records_/2026-11-04/event-claims/1834-queue-run.md`. No diamonds spent, no paid button tapped.
- No game screen was ever read and no game input was dispatched. The Mac screen-capture stream failed on every attempt across two computer sessions: computer.control activate (session cc-477) selected the LastWar window for background input but captured no observation with "Failed to start stream due to audio/video capture failure"; computer.observe (cc-477, compact view) failed with the same error twice and computer.observe (cc-477, image view) failed with the same error; computer.control open_app LastWar returned outcome_unknown (launch result unverifiable, not repeated); in a fresh session (cc-478, after ending cc-477) computer.observe (compact view) failed with the same error and computer.control describe for LastWar failed with the same error. Six capture attempts in total, all the same error, satisfying the at-least-3-retries rule before the unit was recorded as access-failed.
- No blind taps were dispatched: without an observation, any tap could land on the wrong control, so the unit stops here under the check-first rule. The Events hub could not be opened, no event page or red dot was read, and nothing was claimed or verified. No different-device dialog was observed (no screen was ever captured) and no device takeover was needed.
- Recurrence, not a new failure class: this is the thirteenth consecutive ticker pass to fail on this exact blocker, per GitHub Issue #284 (tooling), whose latest comment before this pass was ticker-1804 (gifts unit). This pass commented on #284 instead of filing a duplicate, and this run comments the thirteenth and fourteenth occurrences onto the knowledge Issue #282.
- Reading warning: this failed unit gives zero evidence about the event claim state. It must NOT be read as "nothing claimable" - the 0843 close (full hub sweep, Arms Race now Base Building phase, 0 claims) rests on a live read and stands as the last live read; this unit rests on no read at all.
- Tracker untouched for failed, per the queue rules; the next tick re-produces this regular. The pass stopped after this unit: with no observation channel, a second unit would fail identically and burn the pass budget, so the remaining inbox units (66 at this pass) were left queued.

## What the 2026-11-08 0011 scout read added - events group walked live, Frontline attempt and Doomsday Rewards waiting, Hero Advancement live

- Scout unit scout-scout-2026-11-03-002 by ticker-0004, about 00:06 to 00:11 local, status partial (events group). Evidence in `_records_/2026-11-08/perception-scout/0011-queue-run.md` (commit e6192726d1 on records/2026-11-08). Observe-only; nothing was claimed, fought or tapped on any event page. The Reward panels and Winter Battlefield sub-pages were not opened; they are carried to successor seq 003 of chain scout-2026-11-03.
- Tabs seen in this walk, in order: Arms Race, Frontline Breakthrough, Winter Battlefield, The Doomsday, Community (tab bar dragged both ways; left end is Arms Race, right end is Community). Desert Storm Battlefield, Level Swap and Wanted Boss - present on 2026-10-30 (unit 066) - are gone. No Zombie Invasion tab is present in the hub, which re-confirms the zombie chain stays closed (no fresh chain seeded in this pass).
- Arms Race page: current phase Hero Advancement, Contest Segment Lv.29-30, 01:49:42 left at entry. Score 0, cumulative chest 0/2 (not full, not claimable), point chests at 2,000 / 4,000 / 12,000 all unreached at score 0. No Arms Race grinding was done in this unit; that belongs to the arms-race unit type. Phase state is recorded here for that unit's next run - the phase is live with 1:49 left. Folded into arms-race 1.57.0.
- Frontline Breakthrough: badge 1, timer 17:42:00, Saving Soldiers 64% (chest ladder on the left: gold, silver, bronze, small). Reward row at the bottom: red gem x100, gold bar x10, blue crate x18, gold coins x18, blue crate x3, gold coins x3. Reward button (gift icon) and Ranking button, top right. Challenge button at the bottom carries a red dot - this is the tab badge 1: one challenge attempt available, left for the events regular. The Reward panel was not opened; carried to the successor. Unknown: the 17:42:00 timer reads about 10 minutes shorter than the Doomsday and Winter countdowns read minutes apart (about 17:51-17:52), so it is a different timer - its meaning is unread.
- Winter Battlefield 5v5: "Event is starting soon." Countdown 17:51:09 (17:51:32 on first sight, falling). Local Time. Windows: 11/08 20:00-22:00, 11/09 03:00-05:00, 11/09 13:00-15:00. "Matchmaking is available for Base level 15 and above during the specified times." Match button greyed. Buttons: Rewards, Rules, Shop, History, Achievement - none opened; carried to the successor. No red dot on this page.
- The Doomsday: badge 22, timer 17:52:15. "During the event, Doom Walkers will more easily attack commanders' bases..." Warzone Guardian: [CTR1]초리vv, Total Damage: 2.8G. Alliance Threat (1) / Warzone Threat (79) toggle. Alliance Threat shows one Lv.200 Doom Walker (420,819) with timer 02:52:34; two further slots greyed ("Zombies"). Ranking and Rewards buttons on the right; Rewards carries a red dot. The tab badge 22 maps to the Rewards signal (items waiting there), but the Rewards panel was not opened, so the composition of the 22 is unread - carried to the successor for the events regular to claim.
- Community: Discord binding reward reads Claimed (the 500 Diamonds row); 200 Diamonds visit bonus; Facebook, Discord, X and Reddit links. No red dot, nothing claimable.
- 0 claims in this unit. No priced button, no paid unlock, no Challenge or Go button was tapped. The Doomsday Rewards claim (badge 22) and the Frontline Challenge attempt (badge 1) are this regular's work, carried to the successor read and the next events unit.

## What the 2026-11-08 0608 scout read added - Winter Battlefield Rewards, Rules and Shop Honor tab read live

- Scout unit scout-scout-2026-11-03-004 by ticker-0604, about 06:08 to
  06:23 local, status partial - the 15-minute unit cap ran out after Rewards,
  Rules (all 4 tabs) and the Shop Honor tab; History, Achievement, the Shop
  Campaign/Season tabs and the Doomsday count finish carry to successor seq
  005. Evidence in `_records_/2026-11-08/perception-scout/0608-queue-run.md`
  (commit 50389b4b4a on records/2026-11-08). Observe-only; nothing claimed,
  fought, dispatched, donated, boarded or bought. The Match button was never
  tapped (greyed - event not started).
- Winter Battlefield main page: 5v5 event, "Event is starting soon",
  countdown 11:49:09 at entry falling to 11:41:57 at exit. Matching windows
  (Local Time): 11/08 20:00-22:00, 11/09 03:00-05:00, 11/09 13:00-15:00.
  Matchmaking for Base level 15 and above during the specified times. Match
  button greyed. Right-side buttons: Rules, Shop, History, Achievement.
  Left: Rewards chest icon. Info icon top right unread.
- Rewards (both pages): event currency balance 0 (blue snowflake icon).
  Cumulative Reward Points chest ladder, two pages: 45,000 (tag 4,100),
  90,000 (4,100), 135,000 (5,150), 225,000 (5,250), 337,500 (6,200),
  450,000 (6,500). The tag above each chest carries a red ticket-like icon
  whose meaning is unread - recorded as a number only, not labelled content
  or cost. Ways to earn the currency: Complete a battlefield +10.0K;
  Individual Total Points Ranking +17.5K-52.5K; Get Commendations when the
  battle settles +21.0K-45.0K; Earn Achievements in the battlefield
  +2.4K-3.5K. Achieving victory grants x1.5 for this battle.
- Rules, Rules tab: story - global warming melted the glacier, uncovering a
  hidden nuclear missile site; plan "Winter Storm" to seize the nuclear
  silo. Event Overview: 1. Hold Missile Sites or Oil Wells to earn points;
  first to 30,000 points wins. 2. If time runs out, the side with more
  points wins. 3. The central Silo opens after some time; capture it for
  lots of points. 4. Supply boxes airdrop periodically; send troops to
  capture them for points. 5. On entry, the highest-level units the
  Commander can train fill the independent Drill Ground; they do not appear
  in the Base Drill Ground and do not leave the battlefield after the
  battle. 6. In battles, units do not die; severely wounded units
  automatically recover for free. Reward Rules: unlock chests by
  accumulating Reward Points; Reward Points reset with each event. 1.
  Complete a match for guaranteed Reward Points (requires Total Individual
  Points of at least 250,000). 2. At settlement, Reward Points by total
  individual points ranking (same 250,000 gate). 3. At settlement, Reward
  Points by commendations earned (such as MVP): 3.1 at most one
  highest-value commendation per match; 3.2 players not among the 5
  displayed on the settlement screen still receive commendations normally;
  3.3 past commendations viewable in [History]. 4. Achievements earned per
  match only, progress does not carry over: 4.1 total achievements earned
  historically viewable in [History]; 4.2 progress from a previous match
  cannot be carried to the next match. Event Stages: 1. Event Start - begins
  for the first time after the server's 7th week, match battles on Saturdays;
  during off-season periods, opens each Monday. 2. Matching - Headquarters
  level 15+, several matching times on battle day. 3. Entering - once 10
  commanders confirm, all automatically enter. 4. Battle Stage -
  Preparation: safe zone, own side blue, enemy red, safe zone cannot be
  attacked. Battle: holding Oil Wells earns lots of Battlefield Points,
  Missile Sites fewer; Missile Sites attack all enemy-held buildings,
  killing stationed troops. Silo Opens: opens after some time, holding it
  earns a lot of Battlefield Points. Supply Airdrop: resource packs drop
  periodically, send troops to collect them for Battlefield Points.
- Rules, Structures tab (4 entries): Airdrop Supplies - capture to earn
  1,000 Battlefield Points. Nuclear Silo - opens sometime after the battle
  starts; capturing grants a large amount of Battlefield Points, a key
  structure for victory; gain 100 Battlefield Points per second while
  controlling it. Oil Refinery I - opens when the battle begins; capturing
  gains a large amount of Battlefield Points, the primary way to produce
  them; gain 30 Battlefield Points per second while controlling it. Missile
  Site - automatically targets all enemy-held buildings, dealing damage to
  their troops; gain 10 Battlefield Points per second while controlling it.
- Rules, Reward Points tab: Ranking sub-tab (No.1-No.10) - No.1 +52.5K,
  No.2 +45.5K, No.3 +42.0K, No.4 +38.5K, No.5 +35.0K, No.6 +31.5K, No.7
  +28.0K, No.8 +24.5K, No.9 +21.0K, No.10 +17.5K, all for Individual Total
  Points Ranking at that rank (matches the Rewards page range +17.5K-52.5K).
  Commendations sub-tab (8): War Hero - Total Points over 1,200,000,
  +33.0K. Elite Defender - Capture Points over 375,000, +30.0K. Elite
  Vanguard - Kill Points above 750,000, +30.0K. Elite Tactician - Plunder
  Points over 250,000, +30.0K. Grand General - Total Points over 600,000,
  +24.0K. Outpost Defender - Capture Points over 187,500, +21.0K. Frontline
  Hero - Kill Points above 375,000, +21.0K. Swift Tactician - Plunder Points
  over 125,000, +21.0K. Achievements sub-tab (10): +2.8K - Battlefield Will
  Medal (win battles 25 times in the battlefield); Stand Ready Medal (any
  Troop helps defend the same Building for 90s); Logistics Support Medal
  (successfully collect 4 airdrops); Fire Suppression Medal (plunder 4000
  building points). +3.5K - Thunder Assault Medal (use a total of 600%
  March Speedup); Life Guardian Medal (heal a total of 16000 units); Bloody
  Valor Medal (win battles 30 times in the battlefield); Unyielding Stand
  Medal (any Troop helps defend the same Building for 120s); Airdrop Hunter
  Medal (successfully collect 6 airdrops); War Harvest Medal (plunder 5000
  building points).
- Rules, Other tab: Participation Conditions - Commanders with bases level
  15 and above can participate; multiple matching time slots are available
  on the battle day. Special Rules: 1. In battle, commanders can relocate
  their Base 1 time every minute. 2. On entry, the highest-level units
  automatically fill the separate Drill Ground; they do not show up in the
  base Drill Ground and do not leave the battlefield after the fight. 3.
  Units do not die; severely wounded units are automatically healed for
  free. 4. All boosts from tech, VIP, base skins, titles, decorations and
  drones work in battle. 5. Rallies are disabled, no continuous marching. 6.
  Each commander can garrison multiple troops in a single building.
- Shop, STORE Honor tab (12 items, all full stock): balance 101.1K (gold
  medal currency, not the blue Winter Battlefield currency). Refreshes at
  00:00 on the 1st of every month (server time). Timer 22d 11:42:23 at read.
  Gear Blueprint (UR) 50/50 at 10,000; Skill Chip Chest (UR) 1/1 at 50,000;
  Decoration Chest 1/1 at 50,000; Universal Decor Component 150/150 at 200;
  UR Hero Universal Shard 10/10 at 3,000; Drone Parts 100/100 at 800;
  Universal Exclusive Weapon Shard 25/25 at 2,500; Resource Choice Chest
  (UR) 100/100 at 4,000; Dielectric Ceramic 100/100 at 800; Hero
  Recruitment Ticket 100/100 at 2,000; 50 Stamina 50/50 at 1,000; Emote:
  Victory Fest 1/1 at 100,000. Campaign and Season tabs unread; whether the
  Season tab is the Winter Battlefield currency shop is unverified.
- Open discrepancies (flagged, not resolved): the Commendations range on
  the Rewards page reads +21.0K-45.0K, but the highest listed commendation
  is War Hero +33.0K; 30.0K x 1.5 victory = 45.0K fits the top only if the
  30.0K tier is the max counted, while 33.0K x 1.5 = 49.5K exceeds it. The
  Achievements range on the Rewards page reads +2.4K-3.5K, but the lowest
  listed achievement is +2.8K; no 2.4K achievement was seen in the list. The
  red ticket-like icon on the Rewards chest tags (4,100 / 5,150 / 5,250 /
  6,200 / 6,500) is unread.
- 0 claims in this unit. The Winter Battlefield sub-pages carry no red dots;
  the Events hub badge 1 sits on Frontline Breakthrough (known: Challenge
  attempt, from the 0011/0325 reads). The Doomsday count finish (Lv.150 row,
  Lv.220 rewards, cumulative rows below 30 and above 70, Damage Ranking and
  Ranking Reward tabs) carries to successor seq 005 with the Winter
  Battlefield History + Achievement and Shop Campaign/Season tabs.
- Game left safe: game left on the base screen. Nothing bought. No Assemble,
  no teleport.

## What the 2026-11-08 0656 events unit added - Doomsday first-kill tiers Lv.100-140 claimed, Frontline rewards unclaimable

- Unit events-2026-11-08-0257 by ticker-0634, about 06:54 to 07:02
  local, status partial - the Doomsday first-kill claim landed and was
  verified, but the Events hub sweep is incomplete (Arms Race tab,
  Winter Battlefield Rewards and the scrolled tabs were not visited), so
  the next tick re-produces the regular and finishes the sweep. Evidence
  in `_records_/2026-11-08/event-claims/0656-queue-run.md` (commit
  9669d391ea on records/2026-11-08). Tracker untouched.
- Session: computer session cc-92 on the owner Mac mini (same session as
  the passes unit in this pass). No device-access error, no
  different-device dialog, no login demanded.
- Events hub at entry: Winter Battlefield tab (event starting soon,
  11:18:17 countdown; match windows 11/08 20:00-22:00, 11/09 03:00-05:00
  and 13:00-15:00). Tab badges: Frontline Breakthrough 1, The Doomsday
  22. No Zombie Invasion tab in the bar.
- Frontline Breakthrough: Saving Soldiers 100%, 11:08:02 left. Its
  Rewards panel lists three Play Frontline Breakthrough rows at 0/3,
  0/2 and 0/1 - all unclaimable (the mini-game was not played; grinding
  is outside a claim round). Nothing claimed there; the tab badge 1 is a
  notice, not a claim. The Challenge attempt the 0011 read attached to
  the badge is mini-game play, outside a claim round - the badge marks
  no claimable reward on this tab.
- The Doomsday: 11:17:20 left, Warzone Guardian [AP3x]Nuna Knuckles
  Total Damage 5.2G, Alliance Threat (0), Warzone Threat (28), Threat
  Neutralized. Its Rewards panel showed all five Warzone first-kill
  tiers with green Claim buttons - Lv.100, Lv.110, Lv.120, Lv.130,
  Lv.140 Doom Walker, each paying a builder helmet x1, grey chest x2 and
  brown crate x2. The bottom Claim button was tapped: CONGRATULATIONS
  shown, and after dismissing it all five rows read green checks - all
  five tiers claimed. The congratulations panel itemised gold card x20,
  red diamonds x180, lightning item 50 x11, grey chest x30, brown crate
  x30, 5m speedup x240 and builder helmets x3 visible; those panel
  totals do not equal five times the per-row icons, so no aggregate total
  is claimed here - the verified fact is the five green checks.
- The tiers re-arm per event round: the same five tiers were claimed on
  2026-10-25 and are claimable again in this round - a re-claim is
  routine, not a gap, and no new Issue was filed. Not visited in this
  unit: the Arms Race tab, the Winter Battlefield Rewards chest, and the
  tabs past the scroll (Level Swap, Wanted Boss, Community). The next
  events unit finishes the hub sweep - Arms Race tab (point chests plus
  the cumulative counter chest), Winter Battlefield Rewards, and the
  scrolled tabs - and confirms no red dot or bouncing chest remains.
- Game left safe: base screen. Nothing bought. No Assemble, no teleport.
