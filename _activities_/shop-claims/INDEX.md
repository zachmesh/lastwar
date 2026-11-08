---
title: Shop Claims
created: 2026-10-25T18:58:00Z
modified: 2026-11-08T06:32:17Z
level: L1
version: 1.30.0
description: Free shop packs and pass daily gifts, one activity folder for shop claim knowledge
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-25
  - source: owner structure direction on activity folders, 2026-10-25
  - source: in-game screens observed on the owner Mac mini, 2026-11-01 (1039 passes unit)
  - source: in-game screens observed on the owner Mac mini, 2026-11-01 (1340 passes unit)
  - source: in-game screens observed on the owner Mac mini, 2026-11-01 (1843 passes unit)
  - source: ticker-2212 passes execution record 2026-11-01 2220 queue run
  - source: ticker-0104 shop-claims execution record 2026-11-02 0104 queue run
  - source: ticker-0834 shop-claims execution record 2026-11-02 0846 queue run (done as checked only, monthly pass 19 of 19, coin weekly pass already claimed today)
  - source: ticker-1234 shop-claims execution record 2026-11-02 1300 queue run (done, nothing new, all owned daily claims already taken)
  - source: ticker-2104 shop-claims execution record 2026-11-02 2109 queue run (done, nothing new, S2 Drone card is an offer)
  - source: ticker-2334 shop-claims execution record 2026-11-02 2338 queue run (done, nothing new, tab-tap mapping offset)
  - source: ticker-0304 shop-claims execution record 2026-11-03 0316 queue run (done, 0 new claims, S2 Drone card an offer)
  - source: ticker-1134 shop-claims execution record 2026-11-03 1151 queue run (done, 0 new claims, cart entry re-grounded, S2 Drone/EXP/Iron cards all offers)
  - source: ticker-1804 shop-claims execution record 2026-11-03 1812 queue run (done, 3 claims, Weekly Pass reset 18:00:00 confirmed, Coin pass lapsed, monthly gift re-claimed, Issue #242)
  - source: ticker-2234 shop-claims execution record 2026-11-03 2234 queue run (done as checked only, 0 claims, Hot Deals sold out after the 1812 claim, monthly still Claimed)
  - source: ticker-0234 shop-claims execution record 2026-11-04 0237 queue run (done, checked only, nothing claimable)
  - source: ticker-0504 shop-claims execution record 2026-11-04 0511 queue run (done, checked only, 0 claims, monthly Days Left 17, tab taps need a re-read after each tap)
  - source: ticker-0834 shop-claims execution record 2026-11-04 0841 queue run (done, checked only, 0 claims, monthly 17/17 Claimed as in 0511)
  - source: ticker-1434 shop-claims execution record 2026-11-04 1434 queue run (failed, Mac screen-capture failure on every capture step, no game input dispatched, fifth consecutive ticker pass to fail this way, Issue 284)
  - source: ticker-2234 shop-claims execution record 2026-11-04 2234 queue run (failed, Mac screen-capture failure on every attempt, no game screen read, no input dispatched, next ticker pass after 2204 known to fail identically, Issue 284)
  - source: ticker-1434 shop-claims execution record 2026-11-05 1434 queue run (failed, Mac device offline, fiftieth consecutive ticker pass to fail this way, eleventh in the worsened zero-response form, Issue 284; last_seen 15:36:52Z stale about 7h07m, unchanged since the 1025 pass; six invokes, zero responses)
  - source: ticker-0234 shop-claims execution record 2026-11-06 0234 queue run (failed, Mac device offline, sixty-fifth consecutive ticker pass to fail this way, twenty-sixth in the worsened zero-response form, Issue 284; last_seen 15:36:52Z stale about 19h, unchanged since the 1025 pass; four invokes, zero responses, recovery-device native repair timed out after 25s)
  - source: ticker-0634 shop-claims execution record 2026-11-06 0634 queue run (failed, Mac device offline, seventy-second consecutive ticker pass with a Mac device-access blocker, thirty-third in the worsened zero-response form, Issue 284; last_seen 15:36:52Z stale about 23h, unchanged since the 0534 pass; four invokes, zero responses, no recovery-device attempts)
  - source: ticker-0234 shop-claims execution record 2026-11-07 0234 queue run (failed, Mac device offline, ninety-sixth consecutive ticker pass to fail this way, fifty-seventh in the worsened zero-response form, Issue 284; last_seen 15:36:52Z stale about 43h, unchanged since the ticker-0204 pass; five invokes, zero responses, recovery-device health check timed out after 25s)
  - source: ticker-0633 shop-claims execution record 2026-11-07 0633 queue run (failed, Mac device offline, one-hundred-first consecutive ticker pass with a Mac device-access blocker, sixty-second in the worsened zero-response form, Issue 284; last_seen 15:36:52Z stale about 47h, unchanged since the ticker-0526 pass; seven invokes, zero responses)
  - source: ticker-1452 shop-claims execution record 2026-11-07 1458 queue run (failed, Mac back online, window off-Space, capture failure, one-hundred-eleventh consecutive ticker pass to fail this way, fifth in the capture-failure form, Issue 282; window 160366 pid 59735 at (0,-360), 9 invokes zero game screens, 5 capture attempts failed identically, Mission Control / Ctrl+Right / open_app / set_window_frame not retried per the 1020 lessons; last_seen 22:39:40Z fresh, about 13 minutes before the pass; sync reaped 0 expired 9 due 22, produced duel-score-2026-11-07-1430, queue stats inbox 66 done 1077 at 22:54Z; last live passes read stands at the 2026-11-04 0841 checked-only unit (the record's 0633 line is a mislabel, corrected in the section); record commit 40b58874c0 on records/2026-11-07, verified against the Issue #282 comment 2026-11-07T22:59:38Z which agrees on every point)
  - source: ticker-1834 shop-claims execution record 2026-11-07 1853 queue run (done, 3 claims, first live shop read since 2026-11-04, Free Supply auto-claim and monthly gift re-confirmed)
  - source: ticker-2204 perception-scout execution record 2026-11-07 2209 queue run (partial, Mall strip walked in full, Weekly Pass reset 18:00:00 fourth live confirmation, Super Monthly Pass Days Left 14, check-in FREE GIFT claimable; record commit 0e4f2e52e2 on records/2026-11-07)
---


# Shop claims

## What this activity is

Taking only the free and already paid for items in the shop - free daily
packs and pass daily gifts. This folder accumulates shop claim knowledge
- refresh times and what each free claim pays. Paid buttons are never
tapped without the owner approval, under the recording rules.
Executions are recorded in `_records_/<date>/shop-claims/`, one file per execution.

## How it is done

- Open the shop from the cart icon.
- In Hot Deals, claim the free pack when it is showing.
- In the pass pages, claim the daily gift. Note days and rewards left.

## How to enter

- Base screen cart icon opens the shop on the HOT DEALS tab row.
- The Weekly Pass tab lists the Free Supply chest, the Legendary
  bundle row, and every weekly pass card, owned and for sale mixed.
- The Super Monthly Pass tab holds the monthly pass and its daily gift.

## Cadence

- Weekly Pass page rewards reset daily at 18:00:00 as displayed in
  game. CORRECTED 2026-11-03 1812 (Issue #242): this supersedes
  the 19:00 figure this profile carried, and resolves the
  18:00:00-versus-19:00 discrepancy first noted at 0114 and
  carried unresolved through the 1039 and 1340 sections - the
  1812 unit both re-read the line and confirmed it
  behaviourally (Coin pass lapsed about 18:03, new-cycle
  Free Supply auto-claim fired on shop open).
- Each owned pass pays one Daily Pickup per day; after claiming, the
  card reads Already claimed today and its button turns into Renew.
- The Free Supply chest on the Weekly Pass page auto claims when the
  page is opened - on the second visit of 2026-10-25 it paid out on
  its own with the note Free rewards have been automatically claimed.
- The monthly pass daily gift is once per day, and it refreshes
  at the 18:00 reset with the Weekly Pass cycle (measured
  2026-11-03: button read Claimed at 11:51, Claim Reward
  again at about 18:19 after the reset - single-day evidence,
  consistent with the 18:00:00 reset line).

## Scope and availability

- Only already owned passes pay pickups. Cards with a price button
  (4 dollars 99 seen) are offers, not claims - never tap them.
- The Legendary bundle button is a purchase under a claim label -
  it read Claim All in the morning and Take All at 19 dollars 99
  after the pass claims. Never tap it; it buys the Instant Gain on
  Purchase bundle.
- The pass list re-sorts after a claim, claimed cards move - scroll
  to find the card that is still claimable.

## What is known from 2026-10-25

- Gear Master Pack was claimed free, paying an Upgrade Ore Lucky Chest
  plus 1,500 Upgrade Ore. Its daily refresh showed about 7 hours
  20 minutes left.
- Monthly Pass daily gift was claimed, paying gold tickets times 2, red
  diamonds times 100, stamina items, iron and 5 minute speedups. The pass
  showed 27 days and 27 rewards left. Its paid extension button at
  24 dollars 99 was not touched.
- Weekly Pass showed packs sold out in the morning round. By the
  afternoon check the account held two live weekly passes - an S1
  Drone Parts Weekly Pass (Epic) paying a Daily Pickup of drone
  parts times 15, total 105 over its run, 3 days left, and a Coin
  Weekly Pass (Elite) paying a Daily Pickup of coin items times 3,
  total 21, 9 days left.
- Afternoon claims on 2026-10-25 - the Drone Parts Daily Pickup was
  claimed (drone parts times 15), and the Free Supply auto claim paid
  a ruby times 10 and iron times 4 as displayed. The Coin pickup was
  still outstanding when the session was interrupted.

## What is known from 2026-11-01

Measured in the 0114 passes unit (ticker-0104, window mode
642x951, no different-device dialog). Outcome: done, nothing
claimable - every daily pickup for today was already claimed.

- Shop opened from the base cart icon. HOT DEALS showed only
  promo banners: a FREE GIFT check-in banner and a 1000 POINTS
  banner. Tapping the FREE GIFT banner only advanced the
  carousel to the points banner, so it was not treated as a
  claim, and the Go button was not tapped (external store, not
  a claim).
- Weekly Pass page: Free Supply chest reads Claimed. Legendary
  row shows Take All $19.99 - never tapped. Coin Weekly Pass,
  Remaining 2d 16:47:31, Daily Pickup reads Already claimed
  today; Renew $4.99 not tapped. S2 Drone Components Weekly
  Pass and Iron Weekly Pass show Get Now $4.99 - offers to
  buy, not owned pickups; not tapped.
- Super Monthly Pass page: Days Left 21, Rewards Left 21,
  Daily Pickup reads Claimed. Monthly Pass Extension $24.99
  not tapped.
- Weekly Deal page: Valor Badge $99.99, Base Upgrade $19.99,
  UR Set $49.99 - all paid packs, no free pack showing today.
- Unresolved display, do not overwrite the cadence above: the
  0114 screen read "Weekly Pass rewards reset at 18:00:00",
  against this profile's standing "reset daily at 19:00 as
  displayed in game". The next passes unit must re-read that
  line and establish whether it is a clock time or a
  countdown before either figure is treated as settled.


## Season passes - in the Season hub, not the shop

Two more passes pay daily claims from the Season Two hub (base
screen Season icon). They belong to this folder's family - claim
the free and already paid for parts, never the paid unlocks.

- Season Battle Pass - a points track. Claim and Claim All take
  the unlocked free tiers; the Advanced columns are padlocked
  behind an Unlock Advanced Rewards button at 9 dollars 99 -
  never tap it. On 2026-10-25 the track stood at 16,300 points;
  claiming paid 500 pass points and moved it to 16,800. Free
  tiers at 12,200, 13,000 and 13,800 all showed green checks, and
  the next tiers sit at 17,000 and 17,800. The Infinity Chest at
  the bottom unlocks at 35,000 Battle Pass points.
- Season Weekly Pass - the Titanium Alloy Factory pass. Perks
  shown - Titanium Alloy Factory plus 1, marching speed against
  zombies plus 30 percent, Virus Resistance plus 250. It has a
  Daily Freebie chest on the left of its page (a separate free
  claim - tapping it answered Reward Claimed) and a Daily Pickup
  taken with the green Claim Reward button. On 2026-10-25 the
  pickup paid a stamina 50 item times 1, a dark rock item of
  10.0K times 2, and 5 minute speedups times 60; the pass showed
  1 day left. Lesson from that claim - the first Claim Reward tap
  only flashed the button; a second tap produced the
  congratulations and turned the button to Claimed. Verify the
  button state after claiming, do not assume one tap landed.
- The Instant Gain on Purchase row on the Weekly Pass page is
  the paid bundle - never tap it.
- The base Season icon badge fell from 4 to 2 after these two
  claims, so the badge counts claimable season items among
  other notices.


## What the 2026-11-01 1039 unit added

- Unit passes-2026-11-01-0657 by ticker-1034, session
  about 10:36 to 10:39, status done, checked. Window
  mode, no different-device dialog. Game was on the base
  screen at entry. Nothing was claimed in this unit
  because every claimable item already reads claimed
  today.
- Hot Deals: only the external-store promo ("Visit the
  Last War Store for more rewards!", 1000 points card, Go
  button). No free pack, no Free Claim button on this
  page at this check - consistent with the 0114
  promo-only read.
- Weekly Pass: Free Supply chest reads Claimed.
  Legendary bundle row reads Take All $19.99 - not
  tapped, per the red lines. Coin Weekly Pass reads
  Remaining 2d 7:21:58 and Already claimed today, with a
  Renew $4.99 button - Renew not tapped. The drop from
  the 0114 read of 2d 16:47:31 matches the roughly nine
  and a half hours elapsed, so no discrepancy stands.
  The other weekly cards below (Drone Components, EXP,
  Iron) show $4.99 Get Now purchase buttons - purchase
  offers, not claims, none tapped.
- Super Monthly Pass: Monthly Pass, Squad 4 Lv.20, Days
  Left 20, Rewards Left 20, Daily Pickup button reads
  Claimed. The $24.99 Monthly Pass Extension button was
  not tapped. Days Left 21 at 0114 to 20 here is
  consistent with the day rollover since that unit.
- Still unresolved, carried forward unchanged: the 0114
  display "Weekly Pass rewards reset at 18:00:00"
  against this profile's standing "reset daily at 19:00
  as displayed in game". This unit did not re-read that
  line, so neither figure is treated as settled. Game
  left on the shop Super Monthly Pass page.

## What the 2026-11-01 1340 unit added

- Unit passes-2026-11-01-1057 by ticker-1334, session
  about 13:37 to 13:55, status partial (checked, nothing
  claimed). No different-device dialog.
- Shop Hot Deals tab: store promo only, no free pack
  showing - consistent with the 0114 and 1039 promo-only
  reads.
- Weekly Pass tab: Free Supply chest reads Claimed; Coin
  Weekly Pass reads Already claimed today with Remaining
  2d 4:23:02 (against 2d 7:21:58 at 1039, a drop matching
  the roughly three hours elapsed, so no discrepancy
  stands); S1 Drone Parts Weekly Pass shows no Remaining
  line and no claimable pickup row, so it is not
  currently owned and pays nothing today. The Legendary
  Take All 19.99 button and the Renew 4.99 buttons were
  not tapped.
- Super Monthly Pass tab: Monthly Pass Days Left 20,
  Rewards Left 20, button reads Claimed - unchanged from
  1039. The 24.99 extension was not tapped.
- Season Battle Pass: 17,800 points, the 17,800 free tier
  shows a green check, next tiers at 18,600 and 19,400
  not reached. Claim All answered No rewards available
  to claim. The 9.99 Unlock Advanced Rewards button was
  not tapped. This supersedes the 2026-10-25 next-tier
  read (17,000 and 17,800) - the 17,800 tier is now
  reached and checked.
- Not finished: the Season Weekly Pass tile in the
  Season hub was not opened in this unit; its Daily
  Freebie and Daily Pickup state is unverified for this
  slot. It is the first action of the next passes unit.
- Still unresolved, carried forward unchanged: the 0114
  display "Weekly Pass rewards reset at 18:00:00"
  against this profile's standing "reset daily at 19:00
  as displayed in game". This unit did not re-read that
  line, so neither figure is treated as settled. Game
  left on the base screen.

## What the 2026-11-01 1843 unit added

- Unit passes-2026-11-01-1457 by ticker-1834, session
  about 18:35 to 18:43, status partial (checked and
  claimed, one item left unclaimed). No different-device
  dialog is recorded. Tracker untouched, as partial units
  do not mark the tracker.
- Claimed, read live: Hot Deals free pack - Drone Great
  Value Pack, Free Claim tapped once, Congratulations panel
  paid Drone Parts 20, Skill Chip Chest (SR) 2, Battle Data
  40.0K (4 x 10K); the panel then read "Packs sold out".
  This is the first Hot Deals free pack claim recorded
  today (1340 found promo only), and its contents are now
  observed; whether the pack rotates its contents by day
  stays open.
- Free Supply auto claim: a second Congratulations panel
  followed at once - "Free rewards have been automatically
  claimed", a chest x1 and ruby x10. Recorded as read;
  it sits against the 1340 "Free Supply chest reads
  Claimed" without a reconciling refresh rule, so no
  refresh claim is derived from the pair.
- Super Monthly Pass: Monthly Pass page, Days Left 20,
  Rewards Left 20. Claim Reward tapped once; the Daily
  Gift panel paid gold tickets 2, red diamonds 100,
  stamina 50 x2, iron 200, 5m speedups x60, and the button
  then read Claimed (grey). The $24.99 Monthly Pass
  Extension button was not touched. Tension carried
  forward, not resolved: the 1340 unit read this button
  as Claimed at 13:55, yet a claimable daily gift was
  present again at 18:35; the refresh rule is unrecorded
  and the next passes unit must read the button state on
  entry.
- Not claimed, tap-method blocker (audit class c): Weekly
  Pass page, Coin Weekly Pass (Elite), Remaining
  1d 23:20:41 at entry. Its green Claim button stayed Claim
  with its red badge after three grounded taps ([790,640],
  centre [840,652], [815,648], each re-grounded from a
  fresh screenshot) and a card-body pivot tap at [450,560],
  all with no screen change. No congratulations panel, no
  button-state change, so the pickup is recorded as
  unclaimed, not assumed claimed. Follow-up rule from the
  1849 final sweep: if the next passes unit hits the same
  blocker, it is the third consecutive unit with it and
  must change the entry route and write the change into
  this metadata (R2).
- Red lines held: the Legendary row's green Claim All
  ($19.99 purchase) was deliberately never tapped, and
  the S2 Drone Components Weekly Pass $4.99 offer was
  likewise not tapped.


## What the 2026-11-01 2220 unit added

- Unit passes-2026-11-01-1857 by ticker-2212, session about
  22:11 to 22:20, status done. Tracker marked done. Every
  claimable shop item for this slot is claimed or already
  claimed; no diamonds or money spent, no paid button
  tapped. Game left on the base screen.
- Coin Weekly Pass blocker resolved: Weekly Pass, Coin
  Weekly Pass (Elite), Remaining 1d 19:44 at entry - Daily
  Pickup claimed. The Claim button that was unresponsive
  through three grounded taps plus a card-body pivot in
  the 1843 unit answered on the first tap of this unit at
  the fresh measured centre [841,664] (R2 changed method:
  the 1843 points were [790,640], centre [840,652] and
  [815,648]; the working point sits lower, near the
  button's bottom edge). The Congratulations panel paid
  coin items x3, and the button then read Already claimed
  today. The 1843 follow-up rule is therefore discharged:
  this is not a third consecutive blocked unit, and the
  entry-route change (fresh measured centre, lower near
  the bottom edge) is recorded here. The Renew $4.99
  button was not tapped.
- Free Supply auto claim: on dismissing the Coin panel, a
  second Congratulations panel followed at once: "Free
  rewards have been automatically claimed", ruby x10 and
  iron x4. Note the contents differ from the 1843 auto
  claim (chest x1 and ruby x10) - the auto-claim contents
  vary by slot, and no refresh rule is derived from the
  pair.
- Hot Deals: only the external-store promo ("Visit the
  Last War Store for more rewards!", 1000 points card).
  No free pack showing, nothing to claim - consistent
  with the 1340 promo-only read, against the 1843 free
  pack claim; whether the pack rotates stays open.
- Super Monthly Pass: Monthly Pass, Squad 4 Lv.20, Days
  Left 20, Rewards Left 20, button reads Claimed. Nothing
  new to claim. The $24.99 Monthly Pass Extension button
  was not touched. Note: the 1843 tension (1340 read
  Claimed at 13:55 yet a claimable gift present at 18:35)
  is not re-tested here - the button reads Claimed with
  nothing new, so the refresh rule stays unrecorded.
- Season hub discovery: the Season hub no longer shows
  the Season Battle Pass or Season Weekly Pass tiles
  recorded on 2026-10-25; it holds only a "Calculating."
  card (6d 18:39 left) and a Season Photo card (6d 19:39
  left, red badge 1). The hub page does not scroll.
  Season Photo page (Alliance Photo tab, #2110 [AP3x]
  The Apex, Season S2 11/2/2026, empty frame) - Rewards
  panel: "Edit and save your group photo 1 time(s)" for
  100 red diamonds and "Post 1 message(s) in the
  alliance message board" for 100 red diamonds, both Not
  Achieved, Claim All greyed. Achieving either is an
  alliance-facing action, so under the recording rules
  it needs owner approval first and was not done in this
  unit. Filed as GitHub Issue #154 (owner-decision) for
  the owner to decide. The Season Photo red badge is
  therefore explained, not a missed shop claim. This
  supersedes any reading of the Season hub tiles from
  2026-10-25 as current - those tiles are gone.
- Red lines held: the Legendary row Take All $19.99 was
  never tapped, and the S2 Drone Components Weekly Pass
  $4.99 Get Now offer was not tapped (a purchase offer,
  not a claim).

## What the 2026-11-02 0104 unit added

- Unit passes-2026-11-01-2257 by ticker-0104, session
  01:05 to 01:09, status done (checked, nothing
  outstanding). Every claimable shop item for this game
  day was already claimed, so nothing new was claimed in
  this unit. Tracker marked done for this slot.
- Shop, Hot Deals tab: no free pack showing, only the
  "Visit the Last War Store" promo. No claim taken.
- Shop, Weekly Pass tab: Free Supply chest reads
  Claimed. Coin Weekly Pass (Remaining 1d 16:53) reads
  "Already claimed today" - consistent with the 22:20
  unit on 2026-11-01 claiming this day's pickup. The
  Legendary "Take All $19.99" bundle was not tapped.
  EXP, Iron and Drone pass cards show only the $4.99
  purchase button and no claim control - unowned offers,
  not tapped.
- Shop, Super Monthly Pass tab: Monthly Pass, Days Left
  20, Rewards Left 20, button reads Claimed - unchanged
  from the 2220 read. The $24.99 Monthly Pass Extension
  was not tapped.
- Season hub (base Season icon badge 1): the badge sits
  on the "Calculating." season card, not on a claimable
  pass. Season Photo remains the gated item already
  tracked under Issue #154; nothing was tapped there.
  The badge is therefore explained, not a missed claim.
  Evidence in `_records_/2026-11-02/shop-claims/0104-queue-run.md`.

## What the 2026-11-02 0846 unit added

- Unit passes-2026-11-02-0657 by ticker-0834, session
  about 08:45 to 08:46, status done as checked only.
  Every claimable shop item for this game day was already
  claimed, so nothing new was claimed in this unit.
  Evidence in
  `_records_/2026-11-02/shop-claims/0846-queue-run.md`.
- Shop, Hot Deals tab: no free pack showing, only the
  "Visit the Last War Store" promo and a "FREE TOMORROW"
  card. No claim taken; the Go button was not tapped.
- Shop, Super Monthly Pass tab: Monthly Pass, Days Left
  19, Rewards Left 19, button reads Claimed - down one
  day from the 20 and 20 read at 0104, as expected for a
  new day count, not a missed claim. The $24.99 Monthly
  Pass Extension was not tapped.
- Shop, Weekly Pass tab: Free Supply chest reads Claimed
  (auto-claimed on page open). Coin Weekly Pass (Elite,
  Remaining 1d 9:14) reads "Already claimed today" - the
  countdown fell from 1d 16:53 at 0104, consistent with
  the same day's pickup already taken. The Legendary
  "Take All $19.99" bundle was not tapped. The S2 Drone
  Components Weekly Pass card shows only the $4.99
  purchase button and no claim control - an unowned
  offer, not tapped. No Renew button was tapped.
- Qualification: a drag scroll of the list did not move
  it, so cards below the Drone card were not re-verified
  this unit; the visible cards match the earlier check.

## What the 2026-11-02 1300 unit added

- Unit passes-2026-11-02-1057 by ticker-1234, session
  about 12:51 to 12:56, status done. Nothing new to
  claim; all owned daily claims already taken today.
  Evidence in
  `_records_/2026-11-02/shop-claims/1300-queue-run.md`.
- Entry, second relaunch instance this pass: the Events
  hub back arrow again did not respond to background
  clicks (same stall as the 0910 events unit), so the
  game window was closed and relaunched, which restored
  the base UI with state intact and no login or
  verification demanded. Cross-reference: the
  event-claims profile's hub back-arrow open question
  now records relaunch as the verified exit route.
- Shop, Hot Deals tab: only a promo carousel (Visit
  the Last War Store, points card) with a Go button -
  no free pack showing; Go was not tapped.
- Shop, Weekly Pass tab: Free Supply chest reads
  Claimed; the Legendary Take All $19.99 bundle was
  left untouched; Coin Weekly Pass reads Already
  claimed today (Renew $4.99 left untouched). The
  remaining weekly cards (Drone Parts Epic, EXP
  Legendary, Iron Elite) show a Daily Pickup row with
  no claim button and a Get Now $4.99 purchase button
  - offers, not owned claims. Scrolled to the list end
  (Iron card); no further cards. This discharges the
  0846 qualification for this unit: the full card list
  was verified to its end, not just the visible cards.
- Shop, Super Monthly Pass tab: Monthly Pass, Days
  Left 19, Squad 4 Lv.20; the Daily Pickup button reads
  Claimed. Days Left 19 is unchanged from the 0846 read
  on the same game day, as expected - the count falls
  at the day boundary, not within the day. The Monthly
  Pass Extension $24.99 was not touched.
- No diamonds, money, speedups or other resources
  spent; no Renew, no purchase button tapped.

## What the 2026-11-02 2109 unit added - done, nothing new, S2 Drone card is an offer

- Unit passes-2026-11-02-1857 by ticker-2104, session
  about 21:05 to 21:09, status done. Nothing new to
  claim; all owned daily claims already taken today.
  Evidence in
  `_records_/2026-11-02/shop-claims/2109-queue-run.md`.
- Shop opened from the base cart icon. Hot Deals
  shows only the external-store promo ("Visit the
  Last War Store for more rewards!", 1000 points
  card) with a Go button - no free pack showing; Go
  was not tapped.
- Weekly Pass page: Free Supply chest reads Claimed;
  the Legendary Take All $19.99 bundle was left
  untouched; Coin Weekly Pass (Elite, Remaining
  about 20:52) reads Already claimed today, Renew
  $4.99 left untouched. The S2 Drone Components
  Weekly Pass card below shows a Daily Pickup row
  with no claim button and a Get Now $4.99 purchase
  button - an offer, not an owned claim, as the 1300
  unit already established for the remaining weekly
  cards; it was not tapped.
- Weekly Pass list did not respond to scroll or drag
  attempts in this unit, so the below-fold cards
  were not re-scrolled; the 1300 unit had already
  walked the list to its end (Iron card) with no
  further claimable card. The scroll failure here is
  unit-specific, not a list change - the list end
  from the 1300 read still stands.
- Super Monthly Pass page: Monthly Pass, Squad 4
  Lv.20, Days Left 19, Rewards Left 19, button reads
  Claimed. The Monthly Pass Extension $24.99 was not
  touched.
- Result statistics: claimed_count 0, target 1 shop
  claim sweep performed, achieved 1, resources
  gained none, verified yes. Game left on the base
  screen.


## What the 2026-11-02 2338 unit added - done, nothing new, tab taps land off-centre

- Unit passes-2026-11-02-2257 by ticker-2334, session
  about 23:34 to 23:38, status done. Nothing new to
  claim; all owned daily claims already taken today.
  Evidence in
  `_records_/2026-11-02/shop-claims/2338-queue-run.md`.
- Base screen reached with no "active on a different
  device" dialog; the game was already running on
  the Mac. Shop opened from the cart icon (Hot Deals
  page, no free pack showing on the visible row).
- Super Monthly Pass page: Monthly Pass, Squad 4
  Lv.20, Days Left 19, Rewards Left 19, button reads
  Claimed. The Monthly Pass Extension $24.99 was not
  touched.
- Weekly Pass page: Free Supply chest reads Claimed;
  the Coin Weekly Pass (Elite, Remaining about
  18:21) reads Already claimed today, Renew $4.99
  left untouched. The S2 Drone Components Weekly
  Pass card below shows a Daily Pickup row with no
  claim button and a Get Now $4.99 purchase button -
  an offer, not an owned claim, as the 2109 passes
  unit already established; it was not tapped. The
  Legendary Take All $19.99 button was not tapped
  (red line).
- Tab-click method note: a tap at normalized 573
  first landed on the Super Monthly Pass tab and a
  tap at 700 landed on Weekly Pass; coordinates on
  this window do not map one to one to the visible
  tab centres, so each page switch was verified by
  screenshot before reading its cards. Lesson for
  the next unit: verify the switched page by
  screenshot, never trust the tap point alone.
- Result statistics: claimed_count 0, target 1 shop
  claim sweep performed, achieved 1, resources
  gained none, verified yes. Game left on the base
  screen.



## What the 2026-11-03 0316 unit added - done, 0 new claims, S2 Drone card again an offer

- Ticker-0304, unit passes-2026-11-03-0257, about 03:16
  local, status done. Evidence in
  `_records_/2026-11-03/shop-claims/0316-queue-run.md`.
- Shop opened from the base cart icon. Hot Deals showed
  a store promo only, no free pack on display, and its Go
  button was not tapped.
- Weekly Pass page: the Free Supply chest reads Claimed;
  the Coin Weekly Pass Daily Pickup reads Already claimed
  today, with a Renew 4 dollars 99 button that was not
  tapped. The Legendary row Take All 19 dollars 99 was
  not tapped.
- S2 Drone Components Weekly Pass: its Daily Pickup row
  shows the Lv.4 chest reward icon and no claim button;
  tapping the icon opened only its tooltip (Lv.4 Drone
  Component Chest, Owned 0). The card's only action is
  Get Now 4 dollars 99, so this pass is an unowned offer,
  not an owned pass with a pickup due: the purchase was
  not tapped. This repeats the 2109 and 2338 finding;
  the card stays classified as an offer, not an owned
  pass.
- Super Monthly Pass page: Daily Pickup reads Claimed,
  Days Left 19, Rewards Left 19. The Monthly Pass
  Extension 24 dollars 99 button was not tapped.
- 0 new claims in this unit; every owned daily claim was
  already taken. No price button, Renew button, or paid
  bundle was tapped anywhere in the shop.

## What the 2026-11-03 0811 unit added - done, 0 new claims, S2 Drone card again an offer, back arrows re-grounded

- Ticker-0804, unit passes-2026-11-03-0657, about 08:11
  local, status done. Evidence in
  `_records_/2026-11-03/shop-claims/0811-queue-run.md`.
- Shop opened from the base cart icon. Hot Deals showed
  a store promo only, no free pack on display, and its
  Go button was not tapped.
- Weekly Pass page: the Free Supply chest reads Claimed;
  the Coin Weekly Pass Daily Pickup reads Already claimed
  today, with a Renew 4 dollars 99 button that was not
  tapped. The Legendary row Take All 19 dollars 99 was
  not tapped. Coin Weekly Pass Remaining 09:50:16,
  consistent with the 2338 read (about 18:21 some 8.5
  hours earlier) as a running countdown.
- S2 Drone Components Weekly Pass: its Daily Pickup row
  shows the Lv.4 chest reward icon and no claim button;
  the card's only action is Get Now 4 dollars 99, so this
  pass is an unowned offer, not an owned pass with a
  pickup due - the purchase was not tapped. This repeats
  the 2109, 2338 and 0316 finding; the card stays
  classified as an offer, not an owned pass. Rule for
  the next unit: a pass card whose only action is a
  purchase button, with no claim button on its Daily
  Pickup row, is an offer - do not tap the purchase to
  "claim" it.
- Super Monthly Pass page: Daily Pickup reads Claimed,
  Days Left 18, Rewards Left 18. The Monthly Pass
  Extension 24 dollars 99 button was not tapped. Days
  Left 18 follows 19 at the 0316 unit, a normal daily
  decrement.
- 0 new claims in this unit; every owned daily claim was
  already taken. No price button, Renew button, or paid
  bundle was tapped anywhere in the shop.
- Navigation lesson: the Events back arrow needed a
  re-grounded point (159,947) after two taps at 95,920
  showed no change; the shop back arrow was then
  grounded fresh at 47,950 and worked on the first tap.
  Back-arrow points drift between units - ground them
  fresh each unit instead of reusing a stale point, and
  treat two no-change taps as the signal to re-ground,
  not to tap a third time.

## What the 2026-11-03 1151 unit added - done, 0 new claims, cart entry re-grounded, three S2 cards all offers

- Ticker-1134, unit passes-2026-11-03-1057, about
  11:43 to 11:51 local, status done. Evidence in
  `_records_/2026-11-03/shop-claims/1151-queue-run.md`.
- Shop opened from the base cart icon. Entry
  correction: the first tap at the grounded point norm
  874,38 changed nothing; the cart icon box norm
  829,37 to 995,100, centre 912,68, opened the shop on
  the first tap. The 38 height point sat on the icon
  top edge and missed. Ground the cart icon by its box
  centre, not by a top-edge point.
- Hot Deals: store promo only, no free pack on
  display. The check-in banner shows FREE GIFT "Claim
  your gift today!" with a Go button; the Go button was
  not tapped, as in the 0811 unit - it leads out to the
  check-in event, not a direct shop claim.
- Weekly Pass page, read live and scrolled through
  all cards: the Free Supply chest reads Claimed; the
  Legendary row Take All 19 dollars 99 was not tapped;
  the Coin Weekly Pass reads Remaining 06:11:49 with
  Daily Pickup Already claimed today and a Renew
  4 dollars 99 button that was not tapped; the S2 Drone
  Components, EXP and Iron Weekly Pass cards each show
  only Get Now 4 dollars 99, so all three are unowned
  offers, not owned passes with a pickup due - none was
  tapped. The EXP and Iron cards join the Drone card as
  classified offers under the 0811 rule: a pass card
  whose only action is a purchase button, with no claim
  button on its Daily Pickup row, is an offer.
- Scroll lesson: the second drag at first did not move
  the list; a longer drag from norm 500,850 to 500,250
  moved it and exposed the Iron card button. On this
  page, a short drag that does nothing is a drag-length
  failure, not a page end - drag longer before concluding
  the list is exhausted.
- Super Monthly Pass page, read live: Daily Pickup
  reads Claimed, Days Left 18, Rewards Left 18. The
  Monthly Pass Extension 24 dollars 99 button was not
  tapped. Days Left 18 repeats the 0811 read, not a
  decrement - the monthly day boundary had not passed.
- 0 new claims in this unit; every owned daily claim
  was already taken, matching the 0811 unit. No price
  button, Renew button, or paid bundle was tapped
  anywhere in the shop. Shop left with the back arrow
  at norm 47,950, as recorded in the 0811 unit,
  returning to the base screen on the first tap.
- Costs: about 8 minutes, no stamina or items spent.

## What the 2026-11-03 1812 unit added - 18:00 reset confirmed, Coin pass lapsed, monthly gift re-claimed, 3 claims

- Ticker-1804, unit passes-2026-11-03-1457, about
  18:09 to 18:12 local, status done. Evidence in
  `_records_/2026-11-03/shop-claims/1812-queue-run.md`.
- Shop opened from the base cart icon (grounded
  centre norm 912,68, as recorded in the 11:51 unit) -
  the cart entry re-grounding from 1151 holds.
- Hot Deals: a free pack was on display, unlike the
  11:51 check. RESEARCH SPEED-UP PACK, Availability 1,
  green Free Claim button tapped once:
  congratulations popup paid Coin Chest (UR) times 5
  and 1h Research Speed-up times 25. A second popup
  followed, "Free rewards have been automatically
  claimed", showing a supply chest times 1 and ruby
  times 10; this is the new cycle Free Supply
  auto-claim firing on shop open. Hot Deals then read
  Packs sold out.
- Weekly Pass page, read live and scrolled: the page
  states on screen "Weekly Pass rewards reset at
  18:00:00". The Legendary row Take All 19 dollars 99
  was not tapped. The S2 Drone Components and S1 Drone
  Parts Weekly Pass cards each show only Get Now
  4 dollars 99, so both are unowned offers, not owned
  passes with a pickup due; neither was tapped. The
  Coin Weekly Pass card, owned at the 11:51 check
  with Remaining 06:11:49, now also shows only Get
  Now 4 dollars 99: the pass lapsed at about 18:03
  and is now an offer, not a pickup. It was not
  tapped. The list was scrolled with the long drag
  from norm 500,850 to 500,250 recorded in the 11:51
  unit - the drag lesson holds.
- Reset correction: this unit settles the discrepancy
  carried since 0114. The page line reads 18:00:00,
  the Coin pass lapsed about 18:03, and the new-cycle
  Free Supply auto-claim fired on open - three
  agreeing evidences against the 19:00 figure this
  profile carried in Cadence. Cadence is corrected to
  18:00:00 in this fold. Gap filed as Issue #242
  (labels knowledge); the ticker pass edited no
  knowledge file, the correction rides this fold.
- Super Monthly Pass page, read live: Days Left 18,
  Rewards Left 18, and the Daily Pickup button read
  Claim Reward in green, not Claimed as at 11:51.
  Tapped once: DAILY GIFT popup paid gold tickets
  times 2, red diamonds times 100, stamina 50 items
  times 2, iron 200, and 5 minute speedups times 60.
  The button then read Claimed. The Monthly Pass
  Extension 24 dollars 99 button was not tapped. The
  monthly gift being claimable again at about 18:19
  after reading Claimed at 11:51 answers the second
  ask in Issue #242: the monthly daily gift refreshes
  at the 18:00 reset with the Weekly Pass cycle,
  recorded in Cadence as single-day measured evidence.
- 3 claims in this unit: the Hot Deals free pack,
  the Free Supply auto-claim, and the monthly Daily
  Gift. No price button, Renew button, or paid bundle
  was tapped anywhere in the shop. Shop left with the
  back arrow, returning to the base screen on the
  first tap. Costs: about 3 minutes, no stamina or
  items spent.

## Open questions

- Whether the free Hot Deals pack rotates its contents by day.
- What the dark rock item in the Season Weekly Pass pickup is -
  coal or titanium alloy; the tile only showed 10.0K.


## What the 2026-11-03 2234 unit added - checked only, 0 claims, 1812 cycle state confirmed

- Ticker-2234, unit passes-2026-11-03-1857, about 22:35
  to 22:47 local, status done as checked only. Evidence
  in `_records_/2026-11-03/shop-claims/2234-queue-run.md`.
- The game was found already open on the Alliance Gifts
  Premium tab, all visible rows already Claimed - the
  2208 close state. Two back taps returned through the
  Alliance screen to the base (the first tap needed a
  repeat; the second tap landed).
- Shop opened from the base cart icon (norm about
  885,77 on this unit, a re-grounding variance against
  the profile's 912,68; entry worked).
- Hot Deals: no free pack on display. The page shows
  only the banner carousel (check-in event banner,
  points banner) and the Go button; two drags moved the
  carousel rather than revealing a pack row, and no Free
  Claim button exists on this page now. Consistent with
  the 1812 unit, which claimed the cycle free pack and
  then read Packs sold out. No Free Supply auto-claim
  popup fired on this shop open either, consistent with
  the 1812 auto-claim already firing this cycle.
- Weekly Pass page, read live and scrolled with the
  long drag from norm 500,850 to 500,250: the page
  states "Weekly Pass rewards reset at 18:00:00". The
  Legendary row Take All 19 dollars 99 was not tapped.
  The S2 Drone Components, S1 Drone Parts and Coin
  Weekly Pass cards each show only Get Now 4 dollars
  99, so all three are unowned offers, not owned passes
  with a pickup due; none was tapped. The Coin pass
  lapsed at about 18:03 per the 1812 unit and remains an
  offer.
- Super Monthly Pass page, read live: Days Left 18,
  Rewards Left 18, and the Daily Pickup button read
  Claimed, as expected after the 1812 claim in this
  cycle. The Monthly Pass Extension 24 dollars 99 button
  was not tapped.
- 0 claims in this unit: every shop pass surface was
  checked live and nothing was claimable. No price
  button, Renew button, or paid bundle was tapped
  anywhere in the shop. Shop left with the back arrow,
  returning to the base screen on the first tap. Total
  Power read on the base screen, 149,948,901, unchanged
  by this unit. Costs: about 12 minutes including the
  Alliance Gifts detour, no stamina or items spent.
- No earlier claim superseded: this unit confirms the
  1812 cycle state on every surface rather than changing
  it.

## What the 2026-11-04 0237 unit added - checked only, 0 claims, 2234 cycle state confirmed again

- Ticker-0234, unit passes-2026-11-03-2257, about 02:34 to 02:37 local, status done as checked only. Evidence in `_records_/2026-11-04/shop-claims/0237-queue-run.md`.
- Shop opened from the base cart icon (norm about 885,77 on this unit). The first click attempt was refused for a stale observation and was re-sent with the fresh observation id, no input dispatched twice.
- Hot Deals: no free pack on display and no Free Supply auto-claim popup fired on this shop open. The page shows only the Last War Store banner carousel and the Go button, which leads out to the store and was not tapped.
- Weekly Pass page, read live and scrolled with the drag from norm 500,850 to 500,250: the Free Supply chest reads Claimed. The Legendary row Take All 19 dollars 99 was not tapped. The S2 Drone Components, S1 Drone Parts and Coin Weekly Pass cards each show only Get Now 4 dollars 99, so all three are unowned offers, not owned passes with a pickup due; none was tapped. The Coin pass remains an offer, consistent with the 2026-11-03 2234 unit.
- Super Monthly Pass page, read live: Days Left 18, Rewards Left 18, and the Daily Pickup button reads Claimed, as expected after the previous cycle's claim in this reset day. The Monthly Pass Extension 24 dollars 99 button was not tapped.
- 0 claims in this unit: every shop pass surface was checked live and nothing was claimable. No price button, Renew button, or paid bundle was tapped anywhere in the shop. Shop left with the back arrow on the first tap, returning to the base screen.
- No earlier claim superseded: this unit confirms the 2234 cycle state on every surface rather than changing it. Costs: about 4 minutes, no stamina or items spent.

## What the 2026-11-04 0511 unit added - checked only, 0 claims, monthly count steps 18 to 17, tab taps need a re-read

- Ticker-0504, unit passes-2026-11-04-0257, about 05:09 to 05:11 local, status done as checked only. Evidence in `_records_/2026-11-04/shop-claims/0511-queue-run.md`.
- Shop opened from the base cart icon (norm about 885,77) onto the HOT DEALS tab. No free pack on display and no Free Supply auto-claim popup fired on this shop open. The page shows only the Last War Store banner carousel and the Go button, which leads out to the store and was not tapped.
- Super Monthly Pass page, read live: Days Left 17, Rewards Left 17, and the Daily Pickup button reads Claimed, as expected after this reset day's claim. The Monthly Pass Extension 24 dollars 99 button was not tapped. The 18 to 17 step from the 0237 unit is the normal one-day decrement, not a discrepancy.
- Weekly Pass page, read live and scrolled with the drag from norm 500,850 to 500,250: the Free Supply chest reads Claimed. The Legendary row Take All 19 dollars 99 was not tapped. The S2 Drone Components, S1 Drone Parts and Coin Weekly Pass cards each show only Get Now 4 dollars 99, so all three are unowned offers, not owned passes with a pickup due; none was tapped.
- Tab-tap lesson, new: the first tab tap at norm 570,115 landed on the Monthly page rather than the Weekly page; a second tap at norm 600,118 reached the Weekly page. Tab taps in this bar need a re-read after each tap - do not assume the first tap landed on the intended tab.
- 0 claims in this unit: every shop pass surface was checked live and nothing was claimable. No price button, Renew button, or paid bundle was tapped anywhere in the shop. Shop left with the back arrow on the first tap, returning to the base screen.
- No earlier claim superseded: this unit confirms the 1812 cycle state on every surface rather than changing it. Costs: about 2 minutes, no stamina or items spent.

## What the 2026-11-04 0841 unit added - checked only, 0 claims, monthly 17/17 Claimed unchanged since 0511

- Unit passes-2026-11-04-0657 by ticker-0834, about 08:40 to 08:41 local, status done as checked only. Evidence in `_records_/2026-11-04/shop-claims/0841-queue-run.md`. No price button, Renew button, or paid bundle was tapped anywhere in the shop. No different-device dialog appeared.
- Shop opened from the base cart icon onto the HOT DEALS tab. No free pack on display and no Free Supply auto-claim popup fired on this shop open. The page shows only the Last War Store banner carousel and the Go button, which leads out to the store and was not tapped.
- Super Monthly Pass page, read live: Days Left 17, Rewards Left 17, and the Daily Pickup button reads Claimed - identical to the 0511 read, so no within-day decrement is claimed. The Monthly Pass Extension 24 dollars 99 button was not tapped.
- Weekly Pass page, read live and scrolled with the drag from norm 500,850 to 500,250: the Free Supply chest reads Claimed. The Legendary row Take All 19 dollars 99 was not tapped. The S2 Drone Components, S1 Drone Parts and Coin Weekly Pass cards each show only Get Now 4 dollars 99, so all three are unowned offers, not owned passes with a pickup due; none was tapped.
- 0 claims in this unit: every shop pass surface was checked live and nothing was claimable. This is the third checked-only shop unit today (0237, 0511, 0841), confirming the 1812 cycle state on every surface rather than changing it. Shop left with the back arrow on the first tap, returning to the base screen.

## What the 2026-11-04 1434 unit added - screen-capture failure, fifth consecutive pass, nothing checked or claimed

- Unit passes-2026-11-04-1057 by ticker-1434, about 14:36 to 14:45 local, status failed (the record frontmatter says unverified while its Outcome section says failed - the body outcome is followed, as in the 1344 and 1404 sections). Evidence in `_records_/2026-11-04/shop-claims/1434-queue-run.md`. No different-device dialog appeared.
- No game screen was ever read and no game input was dispatched. The Mac screen-capture stream failed on every attempt: computer.control activate (session cc-462) selected the LastWar window for background input but captured no observation with "Failed to start stream due to audio/video capture failure"; computer.observe (compact) failed with the same error; a fresh computer session (cc-463, after ending cc-462) failed identically on activate and on observe (image view).
- No blind taps were dispatched: without an observation, any tap could land on the wrong control, so the unit stops here under the check-first rule. The shop, the Weekly Pass page and the Season passes were never opened, no free pack or daily pickup was checked or claimed, and no claim was verified.
- Recurrence, not a new failure class: this is the fifth consecutive ticker pass to fail on this exact blocker (ticker-1224 help 1235, ticker-1327 mail 1333, ticker-1340 star-ceremony 1344, ticker-1404 train 1404, ticker-1434 passes 1434), now across five activities. The blocker is filed as Issue #284 (tooling, filed by the ticker-1340 pass) alongside the knowledge Issue #282 filed by the 1332 organizer run; this pass commented on #284 instead of filing a duplicate, and this run comments the fifth and sixth occurrences onto #282.
- Reading warning: this failed unit gives zero evidence about the shop or pass claim state. It must NOT be read as "nothing claimable" - the 0841 checked-only state above rests on a live read; this one rests on no read at all.
- Tracker untouched, per the failed-unit rule; the next tick re-produces the passes unit. The inbox held 64 units at this pass. The unit file sits in `_queue_/done/` with result status failed - that is the unit file's lifecycle state after execution, not a tracker marking; the regular remains due.

## What the 2026-11-04 2234 unit added - screen-capture failure, next known pass after 2204, nothing checked or claimed

- Unit passes-2026-11-04-1857 by ticker-2234, about 22:34 to 22:47 local, status failed (the record frontmatter says unverified while its Outcome section says failed - the body outcome is followed, as in the 1434 section). Evidence in `_records_/2026-11-04/shop-claims/2234-queue-run.md`. No different-device dialog was observed - no screen was ever captured, so none could have been seen.
- No game screen was ever read and no game input was dispatched. The Mac screen-capture stream failed on every attempt across two computer sessions: session cc-492, open_app LastWar returned outcome_unknown and was not repeated, computer.observe (compact) failed three times with "Failed to start stream due to audio/video capture failure", screen.snap failed with the same error, computer.control list_windows succeeded and listed the LastWar window (window_id 160366) so the control channel itself was reachable while the capture stream was not, connection.repair (web) reported both transports healthy and a further computer.observe still failed, computer.control describe failed with the same error, and after a 45-second wait computer.observe failed again; session cc-493 (fresh, after ending cc-492), computer.control activate selected the window for background input but captured no observation with the same error, computer.observe (compact) failed with the same error, and after a 120-second wait a final computer.observe failed with the same error. Total capture attempts: 9 (7 observe, 1 screen.snap, 1 describe). This meets and exceeds the standing at-least-3-attempts retry rule.
- No blind taps were dispatched: without an observation, any tap could land on the wrong control, so the unit stops here under the check-first rule. The shop, the Weekly Pass page and the Season passes were never opened, no free pack or daily pickup was checked or claimed, and no claim was verified.
- Recurrence, not a new failure class: this is the next ticker pass after ticker-2204 known to fail on this exact blocker; the record does not assert an exact consecutive count beyond that. The blocker is filed as Issue #284 (tooling) alongside the knowledge Issue #282; this pass commented on #284 instead of filing a duplicate, and this run comments this occurrence onto #282. The 2234 detail that list_windows succeeds while observe, screen.snap and describe all fail with the same error, and that 45-second and 120-second waits do not clear it, is further evidence against a transient-stream reading, but it adds no new diagnosis beyond the game-window capture stream already narrowed in the 1404 section.
- Reading warning: this failed unit gives zero evidence about the shop or pass claim state. It must NOT be read as "nothing claimable" - the 0841 checked-only state above rests on a live read; this one rests on no read at all.
- Tracker untouched, per the failed-unit rule; the next tick re-produces the passes unit. The inbox held 64 units at this pass. The unit file sits in `_queue_/done/` with result status failed - that is the unit file's lifecycle state after execution, not a tracker marking; the regular remains due.

## What the 2026-11-05 1434 unit added - Mac device offline, fiftieth consecutive pass, zero-response form

- Unit passes-2026-11-05-1057 by ticker-1434, about 14:34 to 14:44 local, status failed (the record frontmatter says unverified while its Outcome section says failed - the body outcome is followed, as in the 1434 and 2234 sections of 2026-11-04). Evidence in `_records_/2026-11-05/shop-claims/1434-queue-run.md`. No different-device dialog was observed - no screen was ever captured, so none could have been seen.
- No game screen was ever read and no game input was dispatched. Six device invokes, zero responses: computer.session start on the Mac mini node_offline (attempt 1), connection.health on the Mac mini node_offline (attempt 2), connection.repair (web) on the Mac mini node_offline (attempt 3), connection.repair (native) on the recovery device node_invoke_timeout after 25s (attempt 4), connection.health on the recovery device node_invoke_timeout after 25s (attempt 5), computer.session start on the Mac mini again node_offline (attempt 6). device.list reports the Mac mini offline with last_seen 2026-11-05T15:36:52Z (07:36 local), stale about 7 hours 7 minutes at pass time, unchanged since the ticker-1025 pass. This meets the standing at-least-3-attempts retry rule. No probe was run beyond these attempts: re-probing is owed only after device.list last_seen refreshes, and last_seen is unchanged, so the CHANNEL_STALL classification from the 1025 probe stands unre-tested.
- Recurrence, not a new failure class: this is the fiftieth consecutive ticker pass with a Mac device-access blocker, eleventh in the worsened zero-response form after ticker-1404 (forty-ninth, tenth). The blocker is filed as Issue #284 (tooling) alongside the knowledge Issue #282; this pass commented on #284 instead of filing a duplicate, and this run comments the fiftieth occurrence onto #282.
- Reading warning: this failed unit gives zero evidence about the shop or pass claim state. It must NOT be read as "nothing claimable" - the 2026-11-04 0841 checked-only state rests on a live read; this one rests on no read at all. The passes unit's daily gifts stay unclaimed for this slot.
- Sync (authoritative, records-branch pool): reaped 0, expired 6 (duel-score, gifts, help, mail, star-ceremony, train 2026-11-05-1030), due 23, produced 6 units (mail, help, gifts, train, star-ceremony, duel-score 2026-11-05-1430); 17 due regulars already queued. Pool-authority note: the pass's first sync ran in the main working tree, which sits on the stale work/ops-execution-records branch (queue state from 2026-11-03) and holds another job's in-flight state - its expirations of 8 local copies were discarded; the branch-pool sync above is the one committed. The records branch is the authoritative pool for ticker passes.
- No successor unit is enqueued from this unit - a successor would hit the same stalled channel. The pass stopped after this one unit.
- Tracker untouched, per the failed-unit rule; the next tick re-produces the passes unit. The unit file sits in `_queue_/done/` with result status failed - that is the unit file's lifecycle state after execution, not a tracker marking; the regular remains due.

## What the 2026-11-06 0234 unit added - Mac device offline, sixty-fifth consecutive pass, zero-response form

- Unit passes-2026-11-05-2257 by ticker-0234, about 02:34 to 02:43 local, status failed. Evidence in `_records_/2026-11-06/shop-claims/0234-queue-run.md`. No different-device dialog was observed - no screen was ever captured, so none could have been seen. On a working screen it would have opened the shop, claimed the free pack and the pass daily gifts. The loss is the unexecuted passes check for this slot (planned 22:57 local 2026-11-05, expires 02:57 local 2026-11-06).
- No game screen was ever read and no game input was dispatched. Four device invokes, zero responses: connection.health (attempt 1) node_offline with "device is offline and does not advertise a wake-up path", connection.repair (web) (attempt 2) node_offline, connection.repair (native) on the recovery device (attempt 3) node_invoke_timeout after 25 seconds, computer.session start (attempt 4) node_offline. device.list reports the Mac mini offline with last_seen 2026-11-05T15:36:52Z (07:36 local), stale about 19 hours at the 02:36 re-check, unchanged since the ticker-0104 pass. New against ticker-0104: this pass did attempt the recovery device, and its native repair timed out after 25 seconds, matching the ticker-2041 timeouts - the recovery channel is unresponsive too, not just untested. This meets the standing at-least-3-attempts retry rule.
- Recurrence, not a new failure class: this is the sixty-fifth recorded consecutive ticker pass with a Mac device-access blocker, twenty-sixth in the worsened zero-response form after ticker-0104 (sixty-fourth, twenty-fifth). Passes between 0104 and 0234 left no record on the branch, so the true consecutive count may be higher; this pass counts recorded passes only. The blocker is filed as Issue #284 (tooling) alongside the knowledge Issue #282; this pass commented on #284 instead of filing a duplicate, and this run comments the sixty-fifth occurrence onto #282.
- Reading warning: this failed unit gives zero evidence about the shop or pass claim state. It must NOT be read as "nothing claimable" - the 2026-11-04 0841 checked-only state rests on a live read; this one rests on no read at all. The passes unit's daily gifts stay unclaimed for this slot.
- Tracker untouched, per the failed-unit rule; the next tick re-produces the passes unit. The pass stopped after this one unit: with the device fully offline, further units would fail identically. Sync reaped 0, expired 9, due 20, produced nothing new, all 20 regulars already queued. The inbox held 75 units before this pass's sync reaped the 9 expired ones.

## What the 2026-11-06 0634 unit added - Mac device offline, seventy-second consecutive pass, zero-response form

- Unit passes-2026-11-06-0257 by ticker-0634, about 06:34 to 06:37 local, status failed. Evidence in `_records_/2026-11-06/shop-claims/0634-queue-run.md`. On a working screen it would have opened the shop, claimed the free pack and the pass daily gifts. The loss is the unexecuted passes check for this slot (planned 02:57 local 2026-11-06, expires 06:57 local 2026-11-06).
- No game screen was ever read and no game input was dispatched. Four device invokes, zero responses, all node_offline with "device is offline and does not advertise a wake-up path": connection.health (attempts 1 and 4), connection.repair (web) (attempt 2), computer.session start (attempt 3). device.list reports the Mac mini offline with last_seen 2026-11-05T15:36:52Z (07:36 local), stale about 23 hours at the 06:36 re-check, unchanged since the ticker-0534 pass and re-verified unchanged by the ticker-0604 pass. No recovery-device attempts were made: the recovery device is offline with the same frozen last_seen 15:36:52Z, and the ticker-0234 pass attempted its recovery channel and timed out after 25 seconds, so nothing new would be learned by repeating it. This meets the standing at-least-3-attempts retry rule.
- Recurrence, not a new failure class: this is the seventy-second recorded consecutive ticker pass with a Mac device-access blocker, thirty-third in the worsened zero-response form after ticker-0604 (seventy-first, thirty-second). No executed pass is recorded between 0604 and this one. The blocker is filed as Issue #284 (tooling) alongside the knowledge Issue #282; this pass commented on #284 instead of filing a duplicate, and this run comments the seventy-second occurrence onto #282.
- Reading warning: this failed unit gives zero evidence about the shop or pass claim state. It must NOT be read as "nothing claimable" - the 2026-11-04 0841 checked-only state rests on a live read; this one rests on no read at all. The passes unit's daily gifts stay unclaimed for this slot.
- Tracker untouched, per the failed-unit rule; the next tick re-produces the passes unit. The pass stopped after this one unit: with the device fully offline, further units would fail identically. Sync reaped 0, expired 15, due 22, produced one new unit (duel-score-2026-11-06-0630), 20 regulars already queued. The inbox held 50 units at this pass close (50 at sync, after 15 expired units were reaped and the duel-score unit was produced).

## What the 2026-11-07 0234 unit added - Mac device offline, ninety-sixth consecutive pass, zero-response form

- Unit passes-2026-11-06-2257 by ticker-0234, about 02:34 to 02:47 local, status failed. Evidence in `_records_/2026-11-07/shop-claims/0234-queue-run.md`. No different-device dialog was observed - no screen was ever captured, so none could have been seen. On a working screen it would have opened the shop, claimed the free pack and the pass daily gifts. The loss is the unexecuted passes check for this slot (planned 22:57 local 2026-11-06, expires 02:57 local 2026-11-07).
- No game screen was ever read and no game input was dispatched. Five device invokes, zero responses: connection.health on the Mac mini node_offline (attempt 1), connection.repair (web) on the Mac mini node_offline (attempt 2), computer.session start on the Mac mini node_offline (attempts 3 and 4, retry), connection.health on the recovery device node_invoke_timeout after 25 seconds (attempt 5). device.list reports the Mac mini offline with last_seen 2026-11-05T15:36:52Z (07:36 local), stale about 43 hours at the 02:46 re-check, unchanged since the ticker-0204 pass 30 minutes earlier. The recovery device's last_seen is frozen at the same 2026-11-05T15:36:52Z as the Mac mini. This meets the standing at-least-3-attempts retry rule. No probe is recorded in this pass: re-probing is owed only after device.list last_seen refreshes, and last_seen is unchanged, so the CHANNEL_STALL classification from the 1025 probe stands unre-tested.
- Recurrence, not a new failure class: this is the ninety-sixth recorded consecutive ticker pass with a Mac device-access blocker, fifty-seventh in the worsened zero-response form after ticker-0204 (ninety-fifth, fifty-sixth). No executed pass is recorded between 0204 and this one. The blocker is filed as Issue #284 (tooling) alongside the knowledge Issue #282; this pass commented on #284 instead of filing a duplicate, and this run comments the ninety-sixth occurrence onto #282.
- Reading warning: this failed unit gives zero evidence about the shop or pass claim state. It must NOT be read as "nothing claimable" - the 2026-11-04 0841 checked-only state rests on a live read; this one rests on no read at all. The passes unit's daily gifts stay unclaimed for this slot.
- Tracker untouched, per the failed-unit rule; the next tick re-produces the passes unit. The pass stopped after this one unit: with the device fully offline, further units would fail identically. Sync reaped 0, expired 4 (help, mail, star-ceremony, train, all 2026-11-06-2230 slot), due 20, produced nothing new, all 20 regulars already queued. Queue stats at 10:34Z: inbox 66, claimed 0, done 1089. The pre-reset zero-sweep pair for tonight's 19:00 reset (chain pre-reset-sweep-2026-11-07) sits in the inbox (pending 2), not yet due, untouched by this pass. No zombie seeding: the chain closed with unit 066 on 2026-10-30 and the seeding rule forbids a fresh chain until a Zombie Invasion tab is seen live again.

## What the 2026-11-07 0633 unit added - Mac device offline, one-hundred-first consecutive pass, zero-response form

- Unit passes-2026-11-07-0257 by ticker-0633, about 06:33 to 06:39 local, status failed. Evidence in `_records_/2026-11-07/shop-claims/0633-queue-run.md`. No different-device dialog was observed - no screen was ever captured, so none could have been seen. On a working screen it would have opened the shop, claimed the free pack and the pass daily gifts. The loss is the unexecuted passes check for this slot (planned 02:57 local 2026-11-07, expires 06:57 local 2026-11-07).
- No game screen was ever read and no game input was dispatched. Seven device invokes, zero responses: computer.session start on the Mac mini node_offline (attempt 1), connection.health on the Mac mini node_offline (attempt 2), connection.repair (native) on the recovery device node_invoke_timeout after 25 seconds (attempt 3), connection.health on the recovery device node_invoke_timeout after 25 seconds (attempt 4), computer.session start on the Mac mini node_offline (attempt 5), connection.repair (web) on the Mac mini node_offline (attempt 6), computer.session start on the Mac mini node_offline (attempt 7). device.list reports the Mac mini offline with last_seen 2026-11-05T15:36:52Z (07:36 local), stale about 47 hours at the 06:38 re-check, unchanged since the ticker-0526 pass about 70 minutes earlier. The recovery device's last_seen is frozen at the same 2026-11-05T15:36:52Z as the Mac mini. This meets the standing at-least-3-attempts retry rule. No probe is recorded in this pass: re-probing is owed only after device.list last_seen refreshes, and last_seen is unchanged, so the CHANNEL_STALL classification from the 1025 probe stands unre-tested.
- Recurrence, not a new failure class: this is the one-hundred-first recorded consecutive ticker pass with a Mac device-access blocker, sixty-second in the worsened zero-response form after ticker-0526 (one-hundredth, sixty-first). No executed pass is recorded between 0526 and this one. The blocker is filed as Issue #284 (tooling) alongside the knowledge Issue #282; this pass commented on #284 instead of filing a duplicate, and this run comments the one-hundred-first occurrence onto #282.
- Reading warning: this failed unit gives zero evidence about the shop or pass claim state. It must NOT be read as "nothing claimable" - the 2026-11-04 0841 checked-only state rests on a live read; this one rests on no read at all. The passes unit's daily gifts stay unclaimed for this slot.
- Tracker untouched, per the failed-unit rule; the next tick re-produces the passes unit. The pass stopped after this one unit: with the device fully offline, further units would fail identically. Sync reaped 0, expired 7 (gifts, help, mail, star-ceremony and train 2026-11-07-0230; survivors and training 2026-11-07-0203), due 20, produced nothing new, all 20 regulars already queued. Queue stats at 14:35Z: inbox 66, claimed 0, done 1105. The pre-reset zero-sweep pair for tonight's 19:00 reset (chain pre-reset-sweep-2026-11-07) sits in the inbox (pending 2), not yet due, untouched by this pass. No zombie seeding: the chain closed with unit 066 on 2026-10-30 and the seeding rule forbids a fresh chain until a Zombie Invasion tab is seen live again.

## What the 2026-11-07 1458 unit added - screen-capture failure, one-hundred-eleventh consecutive pass, capture-failure form

- Unit passes-2026-11-07-1057 by ticker-1452, about 14:52 to 14:58 local, status failed. Evidence in `_records_/2026-11-07/shop-claims/1458-queue-run.md` (commit 40b58874c0 on records/2026-11-07; the pass's own Issue #282 comment 2026-11-07T22:59:38Z agrees with it on every point). No different-device dialog was observed - no screen was ever captured, so none could have been seen. On a working screen it would have opened the shop, claimed the free pack and the pass daily gifts. The loss is the unexecuted passes check for this slot (planned 10:57 local 2026-11-07, expires 14:57 local 2026-11-07 - the unit was already past its expiry when claimed, so it also counts as late in the stats).
- No game screen was ever read and no game input was dispatched. Nine device invokes, zero game screens: computer.session start (cc-7) on the Mac mini; computer.control activate LastWar selected the window for background input but captured no observation, with the error "Failed to start stream due to audio/video capture failure", window_on_screen false, brought_to_front false; computer.observe failed with the same error twice; computer.session end (cc-7); computer.session start (cc-8); computer.control list_windows LastWar listed 1 window at (0, -360), 1920x1080, pid 59735 - the control channel itself is reachable while the capture stream is not; computer.control activate failed with the same error again; computer.observe failed a third time; connection.health on the Mac mini reported both transports connected and healthy (native lastResponseAgeSeconds 0, web 3). Five capture attempts failed identically (two activate evidences plus three observes). This meets the standing at-least-3-attempts retry rule. The Mac mini is back online: device.list last_seen 2026-11-07T22:39:40Z (14:39 local), fresh, about 13 minutes before this pass started - the offline form (Issue 284) is over and this pass is the capture failure in its new form (Issue 282). The window is unchanged since the 1020, 1104, 1204 and 1334 passes: same window, same pid, same position.
- Channel rules, now carried in this profile (propagation follow-up from the 1032 run, shop-claims done - joining alliance-help, alliance-gifts, radar-tasks, arms-race and alliance-donations): Mission Control, background Ctrl+Right and open_app were NOT retried, per the 1020 lessons folded into alliance-help 1.27.0 and confirmed by ticker-1104, ticker-1204 and ticker-1334 - the pass applied the folded lessons instead of re-learning them. set_window_frame was NOT retried: the 1204 pass tried it before any open_app and was still refused with observation_required, so the ordering does not bypass the gate - the gate is on a fresh observation, which cannot be produced while capture is down. The known reliable unblock stands: the owner clicking the LastWar Dock icon once.
- Recurrence, not a new failure class: this is the one-hundred-eleventh consecutive ticker pass with a Mac device-access blocker, fifth in the capture-failure form after ticker-1020 (one-hundred-seventh), ticker-1104 (one-hundred-eighth), ticker-1204 (one-hundred-ninth) and ticker-1334 (one-hundred-tenth). No executed pass is recorded between 1334 and this one: no ticker-1426 record is on the branch, and the 1452 account names no intermediate pass. The blocker is filed as Issue #282 (knowledge); this pass commented on #282 itself, and this run comments the one-hundred-eleventh occurrence onto #282. No duplicate issue is filed.
- Reading warning: this failed unit gives zero evidence about the shop or pass claim state. It must NOT be read as "nothing claimable" - the 2026-11-04 0841 checked-only state rests on a live read; this one rests on no read at all. Correction to the 1452 record's own line (kept verbatim in the record, which is append-only): the record says the last live passes read "stands at the 0633 checked-only unit", but the 0633 record itself (shop-claims/0633-queue-run.md) is a failed unit with no game screen ever read - it is not a live read. The last live passes read stands at the 2026-11-04 0841 checked-only unit, and this unit neither confirms nor supersedes it. The passes unit's daily gifts stay unclaimed for this slot.
- Tracker untouched, per the failed-unit rule; the next tick re-produces the passes unit. The pass stopped after this one unit: with the capture channel down, further units would fail identically. Sync reaped 0, expired 9, due 22, produced duel-score-2026-11-07-1430, all 20 other regulars already queued. Queue stats at 22:54Z: inbox 66, claimed 0, done 1077. The pre-reset zero-sweep pair for tonight's 19:00 reset (chain pre-reset-sweep-2026-11-07) sits in the inbox (pending 2), not yet due, untouched by this pass - if the capture channel recovers before 19:00, the 17:30 and 18:30 sweeps are the backstop for the day's unmeasured shop claim state. No zombie seeding: the chain closed with unit 066 on 2026-10-30 and the seeding rule forbids a fresh chain until a Zombie Invasion tab is seen live again.

## What the 2026-11-07 1853 unit added - first live shop read since 2026-11-04, 3 claims, Free Supply auto-claim and monthly gift re-confirmed

- Unit passes-2026-11-07-1457 by ticker-1834, about 18:41 to 18:53 local, status done, 3 claims. Evidence in `_records_/2026-11-07/shop-claims/1853-queue-run.md` (commit ea01f4aef on records/2026-11-07). Computer session cc-34. Mac mini online and the game screen readable on the first capture - the first live shop read since the 0841 checked-only unit of 2026-11-04. Last War window 372131, 788x1083 at (114,236), pid 98156, on-screen this time (contrast the 1452 unit's off-Space window 160366 at (0,-360), Issue 282). No "active on a different device" dialog appeared, so no takeover was needed or made.
- Capture recovery, second independent live read: this pass read the shop live on first capture, after the ticker-1904 radar unit (1912) read live at 19:07. The pid changed (59735 in the 1020-1608 passes to 98156 here), so the app relaunched at some point after the Mac came back online about 10:20 PT - the relaunch itself is inferred from the pid change, not observed. The recovery is commented on Issue #282 by the 1912 pass; this unit's read corroborates it. The game was on the MY PROFILE panel at entry (leftover state, Lv.30 [AP3x]Bears Lair, 149.8M power, VIP13, #2110). Closed with the X at [838,43]; base screen read Total Power 149,850,353.
- Hot Deals: GEAR MASTER PACK on display, Availability 1, timer 23:17:59. Free Claim tapped once at [500,754]: CONGRATULATIONS paid Upgrade Ore Lucky Chest x1 and Upgrade Ore 1.5K. Page then read "Packs sold out". The same payout as the 2026-10-25 Gear Master Pack claim.
- Free Supply auto-claim, re-confirmed: a second panel followed at once - "Free rewards have been automatically claimed": supply chest x1 and ruby x10 (the new-cycle Free Supply auto-claim, firing on shop open after the 18:00 reset). This matches the 2026-10-25 auto-claim pattern (ruby x10) and the Cadence rule above.
- Weekly Pass page, read live and scrolled to the list end: the page line reads "Weekly Pass rewards reset at 18:00:00" (re-confirmed, third live confirmation after 0114 and 1812). Free Supply already auto-claimed. The Legendary row reads Take All $19.99 - not tapped, per the red lines. S2 Drone Components Weekly Pass, S1 Drone Parts Weekly Pass and Coin Weekly Pass each show only Get Now $4.99 - all three are unowned offers, none tapped. The list ends at the Coin card (three cards total today; no EXP or Iron card in the list). No owned weekly pass has a claimable pickup this cycle.
- Super Monthly Pass page, read live: Monthly Pass, Squad 4 Lv.20, Days Left 14, Rewards Left 14. Claim Reward tapped once at [370,859]: DAILY GIFT paid gold tickets x2, red diamonds 100, stamina 50 x2, iron 200, 5m speedups x60; the button then read Claimed. The Monthly Pass Extension $24.99 was not tapped. Days Left 14 follows 17 at the 0841 read on 2026-11-04 - three daily decrements across the offline days, no discrepancy. The payout matches the 2026-10-25 daily gift exactly.
- Queue-health note for the retro (no profile change): the chain units zero-sweep-pre-reset-sweep-2026-11-07-001 (not_before 17:30) and -002 (not_before 18:30) were never claimed (attempts 0) and expire at the 19:00 reset; the sweep work itself ran as the separate units zero-sweep-2026-11-07-1630 (expired unexecuted) and -1730 (ticker-1734, partial, 23 lines walked, 2 fix-ups enqueued). The chain pair is a duplicate production path, not a missed sweep - the 1730 unit is the live sweep of record. No Issue filed; the stalled-P1 pair is visible in the stats report for the retro's queue-health read. The tooling side (stale-geometry pair) is Issue #410, already filed and fixed by PR 412.
- The pass stopped after this one unit: the device token lease ran to 02:55:34Z, leaving about 2 minutes after the unit closed, too short for a second unit. The next tick (19:04) picks up the remaining inbox. Sync: reaped 0, expired 2, due 21, produced none - all 20 due regulars already queued. Queue stats at 02:40Z: inbox 68, claimed 0, done 1101 - the done-count anomaly from the 1732/1832 runs persists (done 1143 at the 1608 read, 1101 here with 0 expired in between); carried as an observation for the retro, not a profile claim.
- Tooling note, recorded not filed: the unit file's first completion call omitted the resources_gained and costs keys, so it records stats_missing [resources_gained, costs]; the tool refuses a second complete on a done unit, so the keys stand in the record instead. No diamonds, money, speedups or other spending. No alliance diplomacy, no assembly, no teleport.

## What the 2026-11-07 2209 scout read added - Mall strip walked in full, Weekly Pass 18:00 reset confirmed a fourth time, check-in gift waiting

- Scout unit scout-midday-scout-mid-2026-11-03-003 by ticker-2204, session cc-55 about 22:05 to 22:09 local, status partial (store group). Evidence in `_records_/2026-11-07/perception-scout/2209-queue-run.md` (commit 0e4f2e52e2 on records/2026-11-07) and the observation appended to `_records_/2026-11-03/perception-scout/observation.md`. Observe-only; nothing claimed or bought - the check-in gift below is this regular's work, already queued for the 22:57 passes window.
- Mall strip, all 7 tabs walked: Official Event, Weekly Deal, Super Monthly Pass, Weekly Pass, Diamond, Gold Brick Mall, Hot Sale Packs (entry: base cart icon grounded 902,52 opens the shop on the HOT DEALS / MALL header).
- Check-in banner, page 1 of 2: "Participate in the check-in event and claim great rewards!" - FREE GIFT "Claim your gift today!" (chest icon); FREE TOMORROW x5/x5/x5 "Randomly obtain one". Page 2 of 2: "Claim points and redeem great rewards" - 1000 POINTS card. The FREE GIFT is claimable now and maps to this regular; it was already queued for the 22:57 passes window by the scout pass.
- Weekly Pass tab: the page line reads "Weekly Pass rewards reset at 18:00:00" - the FOURTH live confirmation of the line (after 0114, 1812 and 1853), and the first to rule out the countdown reading: at 22:12 local a countdown to the 19:00 reset would read about 20:48:00, so the figure is a wall-clock 18:00, not a countdown. Commented on Issue #242 by this run. Free Supply chest present with no claim badge visible. Legendary bundle Take All $19.99 - the Legendary Claim All, red line, untouched. $2 Drone Components Weekly Pass (Legendary tag), Validity 7 Days, Daily Pickup 1x, Total 7x, Get Now, $4.99. $1 Drone Parts Weekly Pass (Epic tag), Validity 7 Days, Daily Pickup 15x, Total 105x, Get Now, $4.99. All three weekly pass cards are unowned offers, none tapped.
- Super Monthly Pass tab: Monthly Pass, Days Left 14; Squad 4 Lv.20 "Unlock an extra squad!"; Daily Pickup (100 red gems x1, 50 blue x2, gold ticket x2, 5m speedup 60, blue item 200); Get Now +2500 red gems plus 5 items; Rewards Left: 14; button reads "Claimed" (greyed - today's Daily Pickup already claimed, matching the 1853 claim). Monthly Pass Extension $24.99, paid, untouched. Days Left 14 follows 14 at the 1853 read the same evening - no discrepancy.
- Diamond tab: paid diamond packs only (10000, 5000, 2000, 1000, 500; "Double Diamonds"); nothing free or claimable visible. Gold Brick Mall tab: paid gold packs only (x1000 $4.99, x50000 $9.99, x100000 $999.99 shown in OCR; 5% Bonus banner); nothing free visible. Hot Sale Packs tab: "Packs sold out" - nothing available.
- Not walked: Weekly Deal page (named in the strip, page not opened) and the VIP panel and daily missions panel - all carried to the successor in chain scout-mid-2026-11-03. Unknown item: small chest icon overlaid on the Weekly Pass and Super Monthly Pass tabs (possibly an owned-pass marker; meaning unread).
- Red dots in the surfaces walked: Official Event tab dot and the check-in FREE GIFT claimable - both explained, mapping to this regular. No other claimable surface was seen in the Mall strip.
