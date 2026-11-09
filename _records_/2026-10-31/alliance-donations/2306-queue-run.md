---
title: Alliance donations queue run 2306
created: 2026-11-01T06:06:00Z
modified: 2026-11-01T06:22:00Z
status: done
executor: ticker-2304
unit: donations-2026-10-31-2203
---

# Alliance donations - 2306 queue run

Session window: 2026-10-31 23:06 to 23:21 PDT. Unit
donations-2026-10-31-2203, executor ticker-2304. Status: done.

## What was done

- Entered Alliance Techs from the base screen. A first tap on the
  Alliance button area opened a MISSING ITEMS dialog for an Advanced
  Teleporter instead of the alliance menu; no Buy button was tapped
  and the dialog was closed with its X. A fresh measured tap on the
  Alliance shield then opened the alliance menu, and Alliance Techs
  was entered from its tile.
- Alliance Techs, War tab: Troop Movement 5/10, Rallied HP 5/10,
  Rallied Attack 7/10, Rallied Defense 7/10, next node 1/10.
  Tech Donation Today footer read 1100 at entry, above the 1000
  reward threshold. No hand claim exists for the daily donation
  reward (ranking settlement at the 19:00 reset, per the activity
  metadata), so nothing was claimed by hand.
- Rallied Attack panel, coin button only, diamond button never
  used: Donation Count read live at entry as 4/30, cost 800 coin
  per donation, Donation Reward 50 plus 50 per donation.
- Five coin donations landed, each confirmed by a live re-read:
  4/30 to 3/30 (Tech EXP 7.9K to 8.0K), to 2/30 (8.0K to 8.1K),
  to 1/30 (8.1K to 8.2K), then the fourth donation greyed the
  coin button with a 00:03:52 timer. The cooldown was waited out
  inside the unit; the panel then read Donation Count 1/30 again
  with the coin button active, so the count had replenished by
  one during the cooldown. A fifth coin donation was made and
  the coin button greyed again, this time with a 00:18:27 timer.
- No diamonds spent, no purchase made, no other task type touched.

## Closing state, stated plainly

- The unit closed on the game exhausted state, not on an
  arithmetic figure: every donation was confirmed by a live
  count step and a Tech EXP step, and the final state is the
  greyed coin button with its timer, read live. The final
  Donation Count numeral itself was hidden by that timer at
  close, as the activity hard rule anticipates; the count
  sequence 4, 3, 2, 1, greyed, 1 replenished, greyed is the
  live evidence, not a subtraction.
- Mechanism note for the knowledge job (not edited here, tier 2):
  the Donation Count replenishes in small bursts behind a
  cooldown timer (3:52 after the fourth donation, 18:27 after
  the fifth), so a later unit in this reset day may find a
  fresh allowance. The 30 count is not a single pool drained
  once per day.
- Tracker marked done for this slot. Later bursts belong to
  later donations units, not to this unit.

## Result statistics

- target: 5 available coin donations found in this unit
- achieved: 5
- resources_gained: Donation Reward 50 plus 50 times 5, Tech EXP
  7.9K to 8.2K on Rallied Attack
- costs: 4000 coin (5 times 800), about 15 minutes
- verified: yes, same-unit live reads at every step
- blocker_category: none
