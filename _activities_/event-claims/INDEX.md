---
title: Event Claims
created: 2026-10-25T18:58:00Z
modified: 2026-11-03T05:40:46Z
level: L1
version: 1.15.0
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


## Open questions

- Which recurring events hold claims that expire unclaimed.
- The exact item name of the Halloween Day 01 reward.
- Whether the Battle Pass Donate Coal daily should be done on cold
  wave days, and the coal cost per donation.
- What the Wanted Boss Code 87 fight pays in practice when it is
  out at server 00:00. (2026-11-02 2113 update: the boss has rotated to Code 64, a giant gorilla, with Missile Vehicle heroes dealing 50% extra damage; best single attack read 852,929,736 against tiers 1.0B / 1.5B / 2.0B / 2.5B / 3.0B, all Claim buttons grey - the Code 87 payout question is moot until it rotates back.)
- Hub back arrow unresponsive to background clicks (0910 unit) - foreground-first exit still to be verified by a later unit. (2026-11-02 0935 update: the trucks unit's hub back arrow responded once its centre was re-measured at norm 158,947 after taps near 97,906 missed - point accuracy, not background clicks alone, may be the cause; the foreground-first exit is still to be verified by an events unit.) (2026-11-02 1250/1300 update: window close-and-relaunch is now a verified exit and recovery route - the 1250 unit restored hidden side rails by relaunch, and the 1300 passes unit exited the stalled hub by relaunch, both with state intact and no login or device dialog; the foreground-first exit itself is still unverified.)
