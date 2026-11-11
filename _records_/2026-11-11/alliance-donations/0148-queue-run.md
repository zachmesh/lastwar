---
title: Alliance donations queue run 0148
created: 2026-11-11T09:48:00Z
modified: 2026-11-11T09:48:00Z
version: 1.0.0
description: Ticker-0135 donations unit, re-read after 0107 cooldown, 1 coin donation confirmed 2/30 to 1/30, second tap timer-hidden behind 00:17:30 cooldown, partial unverified close
status: unverified
grounded_in:
  - source: live game screen on the owner Mac mini, 2026-11-11 01:46-01:48 PT
---

# Alliance donations queue run 0148 (ticker-0135)

Unit: donations-2026-11-10-2203. Status: partial.
Activity: alliance-donations. Computer session cc-535.

## Entry - camera reset needed first

- The game was left on the base screen by this pass's
  survivors unit, but the camera was still panned down-left
  from the gate check, so the right-side icon column
  (Alliance, Mail, Inventory) was off-screen.
- A tap on the blue house button at the bottom left, norm
  (156,757), did NOT reset the camera: it opened the SET
  DEFENSE LINEUP panel for the Wall. Nothing was changed
  there (no squad order touched, no Join Defense toggled)
  and the panel was exited at once via its back arrow.
  Side read, unverified as a claim about the account: Wall
  status In Good Condition 10,000/10,000, In-Base Unit
  Count 39,996, all four squads with Join Defense checked.
  The blue house button is the Wall's defense control, not
  a camera reset - do not tap it for view resets again.
- The camera was reset by dragging the map (start norm
  (350,450) to (150,650)); the default base view returned
  with the Alliance shield visible.
- Alliance entry: shield icon tapped at the fresh measured
  centre (927,726) from the current screenshot - opened the
  menu first try. Alliance menu: [AP3x] The Apex, Leader
  Abyss Apex, Power 13,798,558,789, Members 96/100,
  Language English.
- Alliance Techs tile tapped at (685,683). The panel opened
  on the Development tab: Auto Rally Max Level, Quick
  Construction 8/10 (red recommended marker), Great Helper
  Max Level, bottom node 2/10. Tech Donation Today footer
  2500 at entry - unchanged from the 0107 close, consistent
  with no donations since.

## What was donated

- Target: Quick Construction (recommended), 8/10,
  Increased Building Speed for Allies, Donation Reward
  +20%, Tech EXP Required 3.1M/6.0M, Current +20%,
  Next Level +22.5%, Donation Reward 50 EXP + 50 badge
  per donation. Coin Donate green at 900 coin, diamond
  Donate 2 (never used).
- Donation Count read live at panel entry: 2/30 remaining.
  (Up from the 1/30 live re-read at the 0107 close: the
  count replenished by 1 during the ~40 minutes since,
  the Issue #599 burst replenishment. The 0107 tap 3's
  effect is unknowable from this read - the replenishment
  dominates any arithmetic.)
- Coin Donate tapped at (659,764), one tap at a time
  with a live read after each.
- Tap 1 landed: Donation Count 2/30 to 1/30 on the
  screenshot after the tap, button stayed green with the
  count visible - no cooldown hid it this time.
- Tap 2: the coin button greyed with a 00:17:30 timer
  and the Donation Count label hid behind the timer,
  the same end state as 1913, 2015, 2133, 2319 and 0107.
  The button was green with count 1/30 visible
  immediately before tap 2 and greyed with the timer
  immediately after - a missed tap produces no change,
  so tap 2 registered; but the count label itself is
  timer-hidden, so per the hard closing rule (R1) the
  count after tap 2 is not a live read.
- Timer 00:17:30 is too long to wait inside the unit
  cap, so the unit closes here.

## Close

- Partial, unverified close - the same close as 1913,
  2015, 2133, 2319 and 0107. Two coin taps made (tap 1
  confirmed by live count read 2/30 to 1/30; tap 2
  evidenced by the green-to-greyed button state change);
  the final count label is timer-hidden, so the count
  after tap 2 is not a live read. The tracker stays
  untouched. A named re-read unit is enqueued for after
  the cooldown (not_before 2026-11-11T10:11:00Z, about
  02:11 PT) to read the final count live.
- Corroboration only, not a closing figure: badge item
  top bar read 406.7K at entry and 407.0K at close
  (+300 over 2 taps, against +100 per tap in 0107 - the
  badge meaning is not pinned down and it is not used
  as evidence here). Tech EXP bar still reads 3.1M/6.0M
  (granularity hides the +100 EXP).
- No diamonds or money spent. No priced button, Renew,
  paid unlock or Legendary Claim All tapped. No login or
  verification demanded. No "active on a different
  device" dialog appeared. The game was left on the
  Alliance Techs list screen.

## Result stats

- target 30 of 30 coin donations for the reset day
- achieved 1 confirmed this unit by live count read
  (2/30 to 1/30); 1 further tap evidenced by the
  button greying, count after it timer-hidden
- resources_gained 50 Tech EXP plus 50 badge items per
  confirmed donation (100 Tech EXP plus 100 badge for
  the 2 taps as displayed)
- points Tech Donation Today 2500 at entry (footer only,
  not used to derive the count)
- costs 2 coin donations at 900 coin each (1800 coin),
  about 3 minutes
- verified no
- blocker_category e
- donations_confirmed 1, donations_button_greyed 1,
  donation_count_before 2, donation_count_after
  unknown (timer-hidden), donation_count_reread none,
  coin_cost_per_donation 900,
  tech Quick Construction 8/10, cooldown_timer 00:17:30,
  count_replenished_between_units yes (1/30 to 2/30
  since 0107), device_takeovers 0
