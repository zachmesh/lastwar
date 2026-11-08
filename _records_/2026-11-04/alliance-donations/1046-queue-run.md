---
title: Alliance donations queue run 1046
created: 2026-11-04T10:46:00-08:00
modified: 2026-11-04T10:46:00-08:00
version: 1.0.0
description: Ticker unit donations-2026-11-04-1003, partial, 10 coin donations Rallied Attack 10 of 30 to exhausted live, test tap at 1 of 30 landed
status: partial
grounded_in:
  - source: live game screens on the owner Mac mini, 2026-11-04 10:36 to 10:46 PST
---

# Alliance donations queue run 1046

Unit: donations-2026-11-04-1003, executor ticker-1034.
Session window: 2026-11-04 10:36 to 10:46 PST, device session cc-446.
No different-device dialog appeared. Coin button only, no diamonds,
no money, no paid button tapped. The diamond Donate button (2 diamonds)
was never tapped.

## Entry route

- Game was on the Events page at entry (an Arms Race Unit Progression
  page left open by the previous unit). The back arrow (108,940)
  returned to the base screen on the first tap.
- Alliance shield: a first tap at (930,670) showed no change on the
  follow-up screenshot; a second tap at the freshly grounded point
  (933,686) opened the Alliance menu (menu verified in the tap
  observation: [AP3x] The Apex, leader Abyss Apex, power
  13,222,993,818, members 95/100). The two points are 16 units apart;
  whether the first tap was a slow render or a miss is not
  distinguished by the evidence, so the entry note records both.
- Alliance Techs tile opened on the first tap at its fresh centre
  (685,689). War tab tree at entry: Troop Movement 5/10,
  Rallied HP 6/10, Rallied Attack 7/10, Rallied Defense 7/10,
  next node below 1/10. Tech Donation Today read 5300 on the
  tree footer.
- Rallied Attack node tap (500,487, freshly grounded) opened its
  panel on the first tap.

## State, read live in this unit

- Rallied Attack panel at entry: 7/10, Current +7 percent,
  Next Level +8 percent, Tech EXP Required 18.7K/4.5M,
  Donation Reward 50/50, Donation Count 10/30, coin Donate 800
  green and active.
- The 10/30 entry count is regeneration since the 2026-11-04 0741
  unit's 1/30 close at 07:41, about 9 counts in about 2 hours 55
  minutes, consistent with the roughly 3 counts per hour rate.

## Donations made - per-burst evidence

Coin Donate taps at (660,770), 800 coin each, the proven point from
the 2340, 0309 and 0741 units. The hold-down tooltip appeared during
the bursts, as in prior units.

- Burst 1, 4 taps: 10/30 down to 6/30, verified by closing image
  (Tech EXP 18.7K to 19.0K).
- Burst 2, 4 taps: 6/30 down to 2/30, verified by closing image
  (Tech EXP 19.0K to 19.6K).
- Single tap: 2/30 down to 1/30, verified by closing image
  (Tech EXP 19.6K to 19.7K).
- Test tap at 1/30: the coin button greyed with a 00:16:35 timer
  and Tech EXP moved 19.7K to 19.9K on the closing image. The EXP
  move proves this tap LANDED: it donated the last available
  count, and the greyed timer is the count-exhausted state (0
  available, next count regenerating in about 16.5 minutes),
  not a failed tap. This corrects the avoidance note carried by
  the 0309 and 0741 units, which declined the 1/30 tap on the
  belief that it greys without landing; the EXP evidence here
  shows the opposite.
- Total landed in this unit: 10 coin donations, 8,000 coin spent.
  Coin HUD is too coarse to show an 8,000 move; the count ladder
  and Tech EXP moves are the donation evidence, not the HUD.
- Donation Reward still 50/50; no claim button was presented, so
  nothing was claimed, consistent with the ranking reward settling
  at the reset rather than by hand.

## Closing state - partial, day not closed by a numeric read

- At close the coin button is greyed with a regen timer
  (00:16:35 at the test-tap read), so the numeric Donation Count
  is hidden and a live 0/30 label cannot be read in this unit.
  Under the hard closing rule (rule R1) the unit closes partial,
  the tracker stays untouched, and a named re-read unit is
  enqueued for after the cooldown (not-before about 11:02 local,
  after the 16.5 minute timer clears).
- The implied regen rate from the timer, about 16.5 minutes per
  count (about 3.6 per hour), matches the roughly 3 per hour
  rate observed across the day.
- Panel left open on the Rallied Attack panel, button greyed
  with timer. Next: the re-read unit re-reads the count after
  the cooldown and donates whatever has regenerated.

## Red lines

No diamonds spent, no paid button tapped, no speedup items used,
no alliance diplomacy, no assembly, no teleport.
