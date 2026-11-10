---
title: Alliance donations queue run 0324
created: 2026-11-09T11:31:00Z
modified: 2026-11-09T11:31:00Z
version: 1.0.0
description: Rallied Attack Donation Count re-read live at 9 of 30, one coin donation made, count 8 of 30, unit closed partial at the pass budget
status: partial
grounded_in:
  - source: live game screen on the owner Mac mini, 2026-11-09 03:24-03:31 PT
---

# Alliance donations queue run 0324 (ticker-0304)

Unit: donations-2026-11-09-0203. Status: partial.
Activity: alliance-donations. Target: Rallied Attack.

## Live reads

- Alliance menu opened on the first tap at the fresh measured
  Alliance shield centre (931,717 on this framing); the 2026-11-02
  entry-route blocker did not recur.
- ALLIANCE TECHS, War tab: Unit Load Capacity 2/10, Quick Training
  1/10, Expert Trainer 2/10, World Interception 5/10, Rapid Siege
  5/10, Quick Garrison 5/10, Troop Movement 5/10, Rallied HP 7/10,
  Rallied Attack 7/10, Rallied Defense 7/10, Expert Nurse 1/10.
  Tech Donation Today footer: 2200 points, reward needs 1000.
- Rallied Attack panel (read live about 03:29 PT): 7/10, Increased
  Hero Attack in Rallies for Allies, Tech EXP Required 24.5K/4.5M,
  Current +7%, Next Level +8%, Donation Reward EXP 50 and badge
  50, Donation Count 9/30, coin Donate button 800 (active), diamond
  Donate button 2 (never used).
- One coin donation tapped: Donation Count re-read live 8/30
  immediately after. The count falls by one per coin donation, so
  it is a remaining count, not a made count.

## What was done

- One coin donation to Rallied Attack (800 coin): Donation Count
  9/30 to 8/30, read live on both sides of the tap.
- No diamond donation. No other unit's work touched (Help and
  Alliance Gifts red dots in the Alliance menu left for their
  own units).

## Open question - the count replenished (needs a knowledge check)

- The previous donations unit (ticker-2334, 2026-11-08 23:50 PT,
  same reset day) left the count at 1/30 read live, with the
  button greyed on a timer. This unit entered about 03:29 PT
  and read 9/30. A remaining count cannot rise without a refill,
  and no 19:00 reset fell between the two reads.
- Working hypothesis, unverified: the Donation Count refills over
  time (or per burst cooldown) rather than being a strict daily
  30 that only falls. The 2026-10-26 burst evidence (button
  greyed with a 00:13:28 timer after the burst) points the same
  way. If the count refills, the hard closing rule (day done
  only when the count reads 0 remaining) needs re-examination:
  a 0 read may be a burst floor, not the day total, and Tech
  Donation Today (2200 here) may be the better day total.
- This unit closed partial at the pass budget with the count at
  8/30, so no closing claim is made either way. The tracker is
  left untouched; the next tick re-produces donations and the
  successor should donate until the button greys and re-read
  the count and the footer after the cooldown.
- Filed as GitHub Issue #500 (knowledge) from this unit.

## What was not done

- The remaining 8 donations were not made inside this unit: the
  pass budget ended about 03:31 PT, one donation into the burst.
  The burst was not run to the greyed button.

## Red lines

- No diamonds or money spent. No speedup item used. No building
  or research started. No stage swap. No login or verification
  was demanded, and no different-device dialog appeared.

## Stats

- target: 30
- achieved: 1
- points: 50
- resources_gained: Tech EXP 50, contribution 50 points
- costs: 800 coin, about 7 minutes of unit time
- verified: yes
- blocker_category: h
