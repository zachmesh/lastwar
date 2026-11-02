---
title: Alliance Donations
created: 2026-10-25T18:58:00Z
modified: 2026-11-02T04:45:00Z
level: L1
version: 1.8.0
description: Donating to alliance technology, one activity folder for donation knowledge
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-25
  - source: owner structure direction on activity folders, 2026-10-25
  - source: owner task request naming alliance tech, 2026-10-25
  - source: owner instruction on 2026-10-26 - always do alliance tech donation as part of the regular routine, each time it is available
  - source: alliance donations execution record 2026-10-31 2306 queue run
  - source: daily retro 2026-10-31 action M4 proposed not applied
  - source: alliance donations execution record 2026-11-01 1141 queue run
  - source: resource collection execution record 2026-11-01 1149 queue run (footer re-read)
  - source: alliance donations execution record 2026-11-01 1619 queue run
  - source: alliance donations execution record 2026-11-01 1944 queue run
---


# Alliance donations

## What this activity is

Donating resources to alliance technology. This folder accumulates
donation knowledge - costs, buttons, daily limits and which technology is
the current target. Executions are recorded in
`_records_/<date>/alliance-donations/`, one file per execution.

Alias - the owner named this activity alliance tech on 2026-10-25. The
in-game screen is titled ALLIANCE TECHS, and donating there is this
activity. Not a separate type.

## How to enter

- Tap Alliance at the bottom right of the base screen.
- Tap the Alliance Techs tile (the flask icon) in the alliance menu.
- The screen has Development and War tabs over a technology tree.
  Tapping a technology node opens its donation panel.

## How it is done

- Donate to the current target technology with the coin button.
- The diamond button is never used without the owner approval, under the
  recording rules on spending.
- Donate in every run, owner instruction 2026-10-26 - alliance tech
  donation is part of the regular routine, not a once a day check.
  Each run opens Alliance Techs and, whenever coin donations still
  remain today, donates them to the recommended technology until
  the daily coin count is used up. If the recommended technology
  completes mid way, follow the new recommended marker. If no coin
  donations remain, record the visit as checked only. Claim the
  daily donation reward whenever it shows as claimable.

## Cadence

- Every four hour run (owner instruction, 2026-10-26, replacing the
  earlier daily cadence). The coin button allows 30 donations a day.
- The screen footer tracks Tech Donation Today in contribution points,
  with a daily reward at 1000 points. Five coin donations earned 300
  points on 2026-10-25, so a coin donation is worth 60 points and the
  1000 point reward sits beyond the 5 donations the daily mission asks
  for.

## Scope and availability

- Always available while in an alliance, not season specific.
- War tab tree as of the 2026-10-25 check - Troop Movement 5 of 10,
  Rallied HP 5 of 10, Rallied Attack 7 of 10, Rallied Defense 6 of 10,
  and the next node below at 1 of 10. Rallied Attack carries the
  recommended marker.
- A Development tab exists beside War. Its nodes were not inspected.

## What is known from 2026-10-25

- Current target seen was Rallied Attack, at 7 of 10 with its bonus moving
  from plus 7 percent toward plus 8 percent as displayed before donating.
- The coin button cost 800 coin per donation, with a daily limit of 30.
  The count shown fell from 30 to 25 after five donations.
- Five donations completed the daily mission Donate to Alliance Tech
  5 Times. The diamond button shown cost 2 diamonds and was not used.
- Checked again at about 13:00 the same day under the task intake
  workflow - Rallied Attack still 7 of 10, Tech Donation Today 300
  points. No further donation was made in that visit. Recorded as a
  checked only execution.

## What is known from 2026-10-26

- The 01:49 run only checked Alliance Techs - Tech Donation Today
  already read 3,100 (the owner had topped it up on 2026-10-25),
  so no coin donation was made, and later runs that day treated
  donations as done for the day. The owner corrected this - the
  donation belongs in every run whenever the daily coin count
  remains, which is the Cadence rule above.

- The daily reward is resolved (10:03 run) - the trophy beside
  Tech Donation Today opens Strength Ranking, Donation tab, and
  its Rewards button opens the Donation Ranking Reward panel.
  The reward is a ranking settlement paid at the 19:00 reset
  (daily tiers by rank; the 4 to 100 tier pays a 50-count badge
  item 4 and red gem 10), gated on at least 1000 contribution
  points. There is no Claim button in the flow - nothing is
  claimed by hand, which closes the claim state left unverified
  by the 0547 and 0608 runs.
- Donation availability runs in bursts - the Rallied Defense
  panel showed Donation Count 2 of 30 at the 10:03 run, two
  coin donations landed at 50 points each (today 7,000 to
  7,100, coin cost 700 each), and the coin button then greyed
  with a 00:13:28 timer, the same end state the 0547 run hit
  after nine donations. Donate until the button greys, then
  stop for that run.

## Hard closing rule - live read or unverified (2026-10-31 fix)

The owner named the incomplete donations himself on 2026-10-31 -
the day closed without the donations completed. The audit found
the mechanism - four donation units that day closed on an
arithmetic final count that was never read live, because the
greyed coin button timer hid the count label. These rules are
hard, and they override any earlier closing habit in this file.

- The daily target is the full count - **30 of 30 coin donations
  every reset day**. The Donation Count is a remaining count (it
  fell from 30 to 25 after five donations on 2026-10-25), so the
  day is done only when it reads 0 remaining.
- A donations unit closes only on a **live Donation Count read
  inside that same unit**. An arithmetic final - donations made
  subtracted from 30 - is never a closing figure, in any record,
  summary or tracker note. This is rule R1 of the task unit queue
  design, stated here for its worst offender.
- When the button timer hides the count, the executor waits out
  the cooldown inside the unit if the budget allows, or re-reads
  the day state from another surface - the Tech Donation Today
  footer, or the Donation tab of Strength Ranking. If the count
  still cannot be read, the unit closes as **unverified**, the
  tracker stays untouched, and a named re-read unit is enqueued
  for after the cooldown.
- Scheduling - donation units run in the early cycles of the day
  (this regular is segment 1, produced from the 02:03 local slot
  onward) and burn the 30 down early, not in the evening units.
  The quota checkpoints of rule R3 apply - the remaining count is
  read live six hours and two hours before the 19:00 reset, and a
  shortfall raises the next donations unit to priority 1. A day
  may not discover an un-donated remainder at its end.

## Open questions

- Who sets the donation target, and when it changes.
- What the Development tab technologies are, and whether donations
  there share the same daily limit and points.
- Whether the queue tool records donation counts under one semantics (remaining counts read live, made counts under donations_made only) - daily retro 2026-10-31 action M4, proposed not applied, tool side pending; the profile side is settled by the 2306 live-read close above.

## What is known from 2026-10-31

- Entry failure mode, measured 2026-10-31 in the 2306 unit
  - a first tap on the Alliance button area opened a
  MISSING ITEMS dialog for an Advanced Teleporter instead
  of the alliance menu. No Buy button was tapped and the
  dialog was closed with its X. A fresh measured tap on
  the Alliance shield then opened the alliance menu, and
  Alliance Techs was entered from its tile. A MISSING
  ITEMS dialog on Alliance entry is a mis-tap surface, not
  a purchase prompt to act on.
- Donation Count replenishment, measured 2026-10-31 in the
  2306 unit - the count replenishes in small bursts behind
  a cooldown timer, so the 30 count is not a single pool
  drained once per day. The unit entered at Donation Count
  4 of 30 on Rallied Attack, cost 800 coin per donation,
  Donation Reward 50 plus 50 per donation as displayed,
  and landed five coin donations, each confirmed by a live
  re-read - 4 of 30 to 3 of 30 to 2 of 30 to 1 of 30, then
  the coin button greyed with a 00:03:52 timer. The
  cooldown was waited out inside the unit; the panel then
  read Donation Count 1 of 30 again with the coin button
  active, so the count had replenished by one during the
  cooldown. A fifth coin donation was made and the coin
  button greyed again, this time with a 00:18:27 timer.
  Tech EXP on Rallied Attack moved 7.9K to 8.2K. A later
  unit in the same reset day may therefore find a fresh
  allowance, and later bursts belong to later donations
  units, not to the unit that found the first burst.
- Correction to the hard closing rule above, in favour of
  the newest verified record - the 2306 unit closed done
  on the game exhausted state, not on an arithmetic figure
  and not on reading 0 remaining. Because the count
  regenerates behind cooldowns, 0 remaining is not a
  stable day-done state, so the two single-pool phrasings
  in the hard closing rule - the day is done only when it
  reads 0 remaining, and the daily target as 30 of 30
  drained once - are superseded. What stands, and what the
  2306 unit confirms, is the live-read core - every
  donation confirmed by a live count step and a Tech EXP
  step, and the unit closing on the greyed coin button
  with its timer read live. Day completeness is judged at
  the rule R3 checkpoints by live reads before the 19:00
  reset, never by subtraction across units.
- War tab nodes as read 2026-10-31 - Troop Movement 5 of
  10, Rallied HP 5 of 10, Rallied Attack 7 of 10, Rallied
  Defense 7 of 10, next node 1 of 10, Tech Donation Today
  1100 at entry, above the 1000 reward threshold. Rallied
  Defense moved from 6 of 10 on 2026-10-25 to 7 of 10 here.
  No hand claim exists for the daily donation reward
  (ranking settlement at the 19:00 reset), so nothing was
  claimed by hand. Cost varies by node as measured -
  Rallied Attack 800 coin per donation in this unit,
  against Rallied Defense 700 coin per donation in the
  2026-10-26 run - so no single cost is assumed across
  nodes.

## What the 2026-11-01 1141 unit added

- Recommended tech is Rallied HP 5 of 10, marked with
  the red thumbs-up badge, entered from the Alliance
  menu Alliance Techs tile (red dot), Development tab.
  Nine coin donations landed, all to Rallied HP, at 600
  coins each - 5,400 coins spent, the diamond button
  untouched. Donation Count moved 30 of 30 to 29 of 30
  after the first tap, 25 of 30 after five, and 21 of 30
  after nine, each step read live.
- Correction to the grey-out precedent: the coin button
  stayed green and active after nine donations in this
  unit - the earlier precedent of it greying after nine
  (2026-10-26, and the 0547 run) did not repeat. Grey-out
  is burst and cooldown dependent, not a fixed
  nine-donation rule, and no grey-out was reached here.
  The unit closed done on its nine confirmed donations,
  not on an exhausted state.
- Tech state at close: Rallied HP Tech EXP 1.6M of 2.0M,
  Current plus 5 percent, Next Level plus 6 percent,
  Donation Reward plus 20 percent. Weekly settlement
  timer read 06:26:54 at close.
- Footer reads and an unresolved arithmetic tension:
  Tech Donation Today read 1,450 at entry, already above
  the 1,000 point reward line, and 2,750 on the re-read
  taken during the 1149 harvest unit's opening moves -
  a rise of 1,300 that exceeds nine donations at the
  previously measured 50 to 60 points each. No new
  per-donation value is derived from this pair: the
  footer may count contributions beyond this unit's nine
  donations, or the per-donation value may vary by node.
  The two reads stand as measured; the footer is not a
  clean per-unit counter until that gap is explained.
- Daily reward timing re-confirmed: the donation ranking
  reward settles at the 19:00 reset, so no reward was
  claimable inside this unit and none was tapped; the
  trophy icon beside Tech Donation Today was left alone.
- Panel close quirk: the Rallied HP detail panel was
  still open at unit close (one X tap did not close it);
  leaving it open spends nothing and changes nothing.
  The footer re-read after the nine donations was skipped
  in the donations unit itself for the pass time budget;
  the entry read of 1,450 stands as that unit's last
  measured footer value, with the 2,750 re-read recorded
  here from the harvest unit that took it.

## What the 2026-11-01 1619 unit added

- Unit donations-2026-11-01-1403 by ticker-1604,
  session about 16:06 to 16:19, status partial and
  unverified under the 2026-10-31 hard rule. The
  tracker is untouched and a re-read unit is enqueued
  for after the cooldown (not before 16:34 local).
- Alliance entry mis-tap, same center-tap lesson as
  the harvest profile: a first tap at 927,795 on the
  base screen opened Mail instead of Alliance. No mail
  was read, claimed or changed; the back arrow returned
  to the base screen. Alliance was then grounded at
  931,705 and opened, and the Alliance Techs tile at
  686,685.
- War tab nodes read live, unchanged from the
  2026-10-31 read: Troop Movement 5 of 10, Rallied HP
  5 of 10, Rallied Attack 7 of 10, Rallied Defense 7 of
  10, next node 1 of 10. Tech Donation Today read 5600
  before the donation.
- One coin donation to Rallied Attack at 800 coin:
  the Rallied Attack panel read Current plus 7 percent,
  Next Level plus 8 percent, Tech EXP Required 8.2K of
  4.5M, Donation Reward 50 EXP and 50 alliance coin,
  Donation Count 1 of 30 with the coin Donate button
  active. A first Donate tap at 662,731 produced no
  change (count still 1 of 30, button still green); a
  second tap at the grounded button centre 657,755
  donated. Proof in the same unit: Tech EXP moved 8.2K
  to 8.3K and Tech Donation Today moved 5600 to 5700,
  a plus 100 point move for one coin donation. The
  diamond Donate button at 2 diamonds was never tapped.
- Count-read rule from this unit: read the Donation
  Count BEFORE donating. After the donation the coin
  button greyed with a 00:16:24 cooldown timer that
  hides the count label, so no live final count exists
  for this unit and no arithmetic final count is
  claimed. Cooldown expiry about 16:33 local.
- The plus 100 single-unit footer move stands as a
  measured pair only. It does not resolve the footer
  tension recorded from the 1141 unit (a 1,300 rise
  against nine donations at 50 to 60 points each), and
  no new universal per-donation value is derived from
  it: the footer may count contributions beyond one
  unit's donations, or the per-donation value may vary
  by node. The 1141 tension stands unchanged.
- Session note, confirming the standing device rule:
  the different-device dialog was showing at entry;
  Confirm was tapped once, the session was taken over,
  the app exited as expected and was relaunched, and
  no second dialog appeared in this unit.

## What the 2026-11-01 1944 unit added

Unit donations-2026-11-01-1803 by ticker-1934,
session about 19:44 to 19:54, status partial with an
unverified close under the hard closing rule above.
The tracker is untouched and a named re-read unit is
enqueued for after the cooldown (not before about
20:15 local). Evidence in
`_records_/2026-11-01/alliance-donations/1944-queue-run.md`.

- Target: Rallied HP, War tab, level 5/10, Current
  plus 5 percent, Next Level plus 6 percent, Tech EXP
  1.9M/2.0M, Donation Reward plus 20 percent. Coin
  button cost 600 coin per donation; the diamond
  button (2 diamonds) was never used.
- Donation Count, every figure read live in this
  unit: 8/30 at entry, 7/30 after the first coin tap,
  6/30 after the second (image-verified; the compact
  OCR misread 6 as 5), then a batch of 6 coin taps
  dispatched in 2.4 seconds. The coin button then
  greyed with a 00:04:56 cooldown timer, hiding the
  count label. The cooldown was waited out inside the
  unit - the panel was re-opened after the timer read
  00:02:11, waited a further 140 seconds, and the
  count reappeared as a live-read 1/30. That proves 7
  coin donations landed in this unit (8 down to 1);
  the sixth batch tap hit the already-greyed button
  and did not land. No arithmetic final is claimed
  for the batch itself: the 7 is fixed by the two live
  reads, 8/30 and 1/30.
- One last coin donation was then dispatched from the
  live-read 1/30. The button greyed again, this time
  with a 00:18:42 timer, hiding the count label once
  more. The 0/30 final is therefore NOT claimed as a
  live read: it is the expected result of 1 remaining
  minus 1 dispatched tap, but the count itself was not
  seen after that tap. The unit closes unverified on
  that point. The re-read unit confirms it: if it
  reads 0/30 the day is done and the tracker may be
  marked done; if it reads 1/30 the last tap did not
  land and one more coin donation is due.
- Footer tension, standing and grown, not resolved:
  Tech Donation Today read 0 at entry and 750 after
  the first donation phase. The footer points are
  recorded as observed only; they are not converted
  into a count, because this file carries two
  different per-donation figures (50 and 60) and 750
  does not divide by the 7 live-counted donations
  under either figure. Together with the 1619 unit's
  plus 100 single-unit footer move, no universal
  per-donation footer value is derived from any of
  these pairs: the footer may count contributions
  beyond one unit's donations, or the per-donation
  value may vary by node. The 1141 tension stands
  unchanged.
- Entry-point lessons, rule R2: the first Alliance
  tile tap at norm 902,831 and the second at norm
  903,800 both opened Mail, not the Alliance menu;
  visual grounding on the base screenshot put the
  Alliance tile at norm 930,705 and the Mail tile at
  norm 930,785, and the 930,705 tap opened the
  Alliance menu. The Alliance Techs tap at norm
  700,631 landed on Members (row boundary); the
  OCR-grounded Techs label row at norm 700,679
  opened Alliance Techs. The Alliance menu back arrow
  failed twice at norm 97,946 with no change
  (background clicks do not reach that control); the
  method was abandoned per R2 and the game was left
  on the Alliance menu, which the next session
  resumed from without loss. No Esc key was used.
  Tile centres must be re-grounded from the
  screenshot on every opening, never inherited.
- One stale-observation retry: a click refused as
  target exited or restarted dispatched nothing;
  re-selecting the same LastWar window and clicking
  with a fresh observation id succeeded, so no
  donation was lost or doubled by it. The game was
  left on the Rallied HP panel with the coin button
  greyed under its 00:18:42 timer.
