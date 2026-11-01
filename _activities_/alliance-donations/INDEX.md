---
title: Alliance Donations
created: 2026-10-25T18:58:00Z
modified: 2026-11-01T06:36:48Z
level: L1
version: 1.5.0
description: Donating to alliance technology, one activity folder for donation knowledge
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-25
  - source: owner structure direction on activity folders, 2026-10-25
  - source: owner task request naming alliance tech, 2026-10-25
  - source: owner instruction on 2026-10-26 - always do alliance tech donation as part of the regular routine, each time it is available
  - source: alliance donations execution record 2026-10-31 2306 queue run
  - source: daily retro 2026-10-31 action M4 proposed not applied
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
