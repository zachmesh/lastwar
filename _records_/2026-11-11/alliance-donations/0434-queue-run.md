---
title: Alliance donations queue run 0434
created: 2026-11-11T12:58:00Z
modified: 2026-11-11T12:58:00Z
version: 1.0.0
description: Ticker-0434 donations unit, War-tab Rallied Attack re-read after ticker-0336 1/30 close, 3 coin donations verified live, taps from 1/30 breached the changed route, closing count timer-hidden, partial unverified close
status: unverified
grounded_in:
  - source: live game screen on the owner Mac mini, 2026-11-11 04:36-04:51 PT
---

# Alliance donations queue run 0434 (ticker-0434)

Unit: donations-2026-11-11-1157. Status: partial.
Activity: alliance-donations. Computer session cc-556.

## Entry

- Own PRs first: records PR 627 (2026-11-11, post-0300 batch)
  verified OPEN with no comments; records PR 615 (2026-11-10)
  already reconciled by ticker-0313, no question addressed to
  this job. Nothing to answer before the pass.
- The game was on the base screen. Alliance entry: shield icon
  tapped at the fresh-grounded point (935,717) from the current
  screenshot - opened the menu first try, no Drill Ground pan.
  The 2026-11-02 entry-route blocker stays fixed by fresh
  grounding in the unit, not by an inherited point. Alliance
  menu: [AP3x] The Apex, Leader Abyss Apex, Power
  13,794,043,556, Members 96/100, Language English.
- Alliance Techs tile tapped at (687,675). The panel opened on
  the Development tab: Auto Rally Max Level, Quick
  Construction 8/10, Great Helper Max Level, bottom node 2/10.
  Tech Donation Today footer 3150 at entry.
- War tab tapped at (600,210). The War tree is deeper than the
  2026-10-25 description: Unit Load Capacity 2/10, Quick
  Training 1/10, Expert Trainer 2/10, then World Interception
  5/10, Rapid Siege 5/10, Quick Garrison 5/10, Troop Movement
  5/10, then the Rallied row - Rallied HP 7/10, Rallied Attack
  7/10, Rallied Defense 7/10, Expert Nurse 1/10 below. The tree
  does not scroll; it is dragged upward (drag from (500,550) to
  (500,300)) to reveal the lower rows.

## What was donated

- Target: Rallied Attack (War tab), 7/10, Increased Hero Attack
  in Rallies for Allies, Tech EXP Required 24.6K/4.5M at entry,
  Current +7%, Next Level +8%, Donation Reward 50 EXP + 50
  contribution points per donation. Coin Donate green at 800
  coin, diamond Donate 2 (never used).
- Donation Count read live at panel entry: 3/30 remaining.
  (Up from the 1/30 live paired read on Rallied Attack at the
  1119 close about 40 minutes earlier: the count replenished
  by 2 since, the Issue #599 burst replenishment.)
- Coin Donate tapped at (658,772), one tap at a time with a
  live read after each.
- Tap 1 landed: Donation Count 3/30 to 2/30, Tech EXP bar
  24.6K to 24.7K.
- Tap 2 landed: Donation Count 2/30 to 1/30, Tech EXP bar
  24.7K to 24.8K.
- Tap 3: the coin button greyed with a 00:04:50 timer and the
  Donation Count label hid behind the timer. Tech EXP stayed
  24.8K. Tap 3 was made from a live 1/30 count - against the
  changed route (stop at the live-read 1/30, no tap from 1/30,
  hand the last donation to a named re-read unit; 2026-11-10
  retro action A-2026-11-10-02, Issues #148 and #500). The
  unit then waited out the 00:04:50 cooldown inside the unit
  (260 seconds of waits) and re-read the panel live: Donation
  Count 1/30, button green again, Tech EXP still 24.8K. Tap 3
  was eaten - no EXP move across two reads and the count
  unchanged after the cooldown - the same eaten-tap pattern
  documented for taps from 1/30.
- Tap 4: also made from the live 1/30 count, the same route
  deviation. It landed: Tech EXP bar 24.8K to 24.9K, the coin
  button greyed with a 00:18:58 timer, the Donation Count
  label hidden behind the timer. The last available donation
  was spent by this unit instead of being handed to a re-read
  unit.

## Route deviation and its cause

- This pass executed from the worktree's stale activity
  profile: the disk copy of _activities_/alliance-donations/
  INDEX.md is version 1.5.0 (2026-11-02), while main carries
  version 1.96.0 (2026-11-11). The stale profile still says
  "donate until the count reads 0" and has no replenishment
  model and no changed route, so the unit followed the
  superseded rule into the 1/30 taps. The same staleness
  affects the other files this pass read: recording-rules
  1.7.0 vs main 1.9.2, task-unit-queue-design 0.14.0 vs main
  0.16.0, zombie-invasion 1.22.0 vs main 1.29.0. The disk
  zombie profile still says the event ended and to seed
  nothing - the event in fact returned on 2026-11-10 as
  Zombie Invasion - Glacieradon (main zombie 1.29.0), and
  chain zombie-2026-11-10 unit 009 already sits in the inbox,
  so no seeding was needed and none was done.
- Filed as GitHub Issue #631 (tooling): the ticker worktree's
  activity and convention files are stale against main, so
  executors read superseded rules. The issue names this
  record as its evidence.

## Close

- Partial, unverified close. Three coin donations verified
  live in this unit (count steps 3/30 to 2/30 to 1/30 and
  Tech EXP bar 24.6K to 24.9K); the closing Donation Count
  is timer-hidden behind the 00:18:58 cooldown, so per the
  hard closing rule (R1) the count after tap 4 is not a
  live read and the tracker stays untouched. A named re-read
  unit is enqueued for after the cooldown (not_before
  2026-11-11T13:10:00Z, about 05:10 PT) to read the final
  count live.
- Corroboration only, not a closing figure: Tech EXP bar
  24.6K to 24.9K across the unit (+0.3K displayed for 3
  landed donations, against 50 EXP per donation on the
  reward row - the bar granularity does not resolve it and
  it is not used as evidence here). Coin HUD stayed 120.9M
  throughout (0.1M granularity hides 2,400 coin). An
  "Alliance Gifts received!" toast appeared mid-unit and a
  "Hold down for easier continuous donations" hint appeared
  after tap 3; neither changed any state.
- No diamonds or money spent. No priced button, Renew, paid
  unlock or Legendary Claim All tapped. No login or
  verification demanded. No "active on a different device"
  dialog appeared. The game was left on the Rallied Attack
  donation panel. Computer session cc-556 ended.

## Result stats

- target 3 coin donations (the live remaining count at entry)
- achieved 3 coin donations verified live (count steps and
  Tech EXP moves; taps 1, 2 and 4 landed, tap 3 eaten)
- resources_gained 150 Tech EXP plus 150 contribution points
  by the reward row (50 each per donation); Tech EXP bar
  24.6K to 24.9K
- points Tech Donation Today 3150 at entry (footer only, not
  used to derive the count)
- costs 3 coin donations at 800 coin each (2400 coin), about
  15 minutes
- verified no
- blocker_category e
- donations_confirmed 3, donations_eaten 1, donation_count_before 3, donation_count_after unknown (timer-hidden), donation_count_reread none,
  coin_cost_per_donation 800,
  tech Rallied Attack 7/10, cooldown_timer 00:18:58,
  count_replenished_between_units yes (1/30 to 3/30 since
  the 1119 close), route_deviation taps from 1/30 (tap 3
  eaten, tap 4 landed), stale_profile alliance-donations
  1.5.0 vs main 1.96.0, device_takeovers 0
