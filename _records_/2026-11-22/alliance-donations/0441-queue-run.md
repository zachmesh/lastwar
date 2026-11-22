---
title: Alliance donations queue run 0441
created: 2026-11-22T12:42:00Z
modified: 2026-11-22T12:42:00Z
version: 1.0.0
description: Queue unit donations-2026-11-22-1146, ticker-0434 - re-read after the 0334 unit's refill wait, Donation Count 3/30 then 1/30 live, 4 coin donations dispatched, final 0/30 never live-read (cooldown timer hides the count), closed partial; refill-timer model refined to a roughly 20 minute clock-anchored tick
status: unverified
grounded_in:
  - source: live game screen on the Mac mini, 2026-11-22 04:35-04:41 PT
  - source: unit donations-2026-11-22-1146 in _queue_/done
  - source: _activities_/alliance-donations/INDEX.md hard closing rule (live read or unverified)
---

# Alliance donations queue run 0441 (ticker-0434)

Unit donations-2026-11-22-1146, regular donations,
activity alliance-donations, priority 2, est 7 minutes,
not_before 2026-11-22T12:15:00Z (04:15 PT). Executor
ticker-0434. Session window about 04:35 to 04:41 PT.
Computer session cc-95, LastWar window 105986, no
session drop, no other-device dialog. Token held
04:35 to about 04:41 PT.

## Outcome

Partial - this is the re-read unit the 0334 pass
enqueued for after the next refill (not_before
2026-11-22T12:15:00Z, 04:15 PT). The 0334 unit
(donations-2026-11-22-1119, 03:46-03:59 PT) found
the count at 1/30 live on both Quick Construction
and Rallied Attack, dispatched nothing, and left
it at 1/30. Donation
Count read live 3/30 at entry, a batch of 3 coin
donations dispatched, the coin button then greyed
with a green 00:00:08 timer hiding the count
label. After a 12 second wait the count re-read
live at 1/30 with the button green again. One more
coin donation dispatched and the button greyed
again with a 00:19:25 timer, the count label
hidden again. The final 0/30 was never read live
in this unit, so per the hard closing rule the
unit closes partial with verified no for the full
30, the tracker stays untouched, and a named
re-read unit is enqueued for after the new
cooldown (donations-2026-11-22-1241, not_before
2026-11-22T13:05:00Z, about 05:05 PT, just after
the next refill tick at about 05:03 PT). The unit
closed inside the 15 minute cap (about 6 minutes
of execution).

## Entry

- Base view at entry was the default framing with
  the full UI present (avatar Lv.30, total power
  149,417,850, right column Events, VS, Alliance,
  Mail, Inventory, HEROES / WORLD bottom bar).
  No network error dialog this time, unlike the
  0319 pass.
- Base view at entry: food 760.8M, iron 1.1G,
  coin 103.9M, stamina 120, badges 17.72K.
- Alliance shield tapped at the fresh measured
  centre (936,707) from the screenshot and opened
  the Alliance menu on the first try.
- Alliance menu live: [AP3x] The Apex, Leader
  Abŷss Apex, Power 14,383,191,808, Members
  99/100. Alliance Star (Event 42) banner read
  Time Left 13:13:16 at entry, 13:10:08 at close,
  not entered.

## Donations made (live reads only)

- Alliance Techs, Development tab: Auto Rally Max
  Level, Quick Construction 9/10 carrying the red
  thumbs-up recommended marker, Great Helper Max
  Level, one node below at 2/10. Tech Donation
  Today footer 5300 - alliance-wide, not
  account-attributable (Issue #558), not used as
  a count.
- Quick Construction panel live: Increased
  Building Speed for Allies, Donation Reward +20%,
  Tech EXP Required 3.6M/8.0M at entry and at
  close, Current +22.5%, Next Level +25%,
  Donation Reward EXP 50 and badge 50 per
  donation. Coin Donate 1000 per donation; diamond
  Donate 2, never used.
- Donation Count live reads: 3/30 at entry. A
  batch of 3 taps on the green coin Donate button
  (647,783) dispatched in about 1.7 seconds; the
  button then greyed with a green 00:00:08 timer
  and no count label. After a 12 second wait the
  count re-read live at 1/30 with the button green
  again. A single tap dispatched the last one;
  the button greyed with a green 00:19:25 timer
  and no count label.
- The batch of 3 landing as 3 donations is
  supported by the badge counter in the top bar
  moving 346.5K to 346.8K across the batch
  (+300, about +100 per donation, the same step
  the 2144 unit saw per batch of 3), and by the
  coin HUD moving 103.9M to 103.8M. Both are
  rounding-level moves and are recorded as
  supporting, not as the closing count: the
  closing count is the live 1/30 read and the
  greyed button after the single tap.
- Verified spend: 4,000 coin dispatched (4 x
  1000). Panel rates imply Tech EXP +200 and
  badge +200; the Tech EXP panel rounding (3.6M
  to 3.6M) cannot confirm it. The top-bar badge
  steps do not match 50 per donation, so that bar
  is not used as evidence for the donation count,
  as the 0113 record already established.

## New observation - the refill timer model

- The green timer is the countdown to the next
  +1 refill tick, and the ticks land roughly
  every 20 minutes on a clock-anchored cycle,
  not on a per-donation cooldown. Evidence in
  this unit: after the batch of 3 zeroed the
  count the timer read 00:00:08 and the count
  re-read 1/30 about 20 seconds later; after
  the single tap zeroed it again the timer read
  00:19:25, putting the next tick at about
  05:03 PT, about 21 minutes after the
  04:42 tick. The 0319 unit fits the same
  model: its 00:09:37 timer expired into a
  1/30 re-read, and its 00:18:47 timer put the
  next tick about 19 minutes after that one.
- Cross-unit arithmetic fits too. 0113 left the
  count at 24/30 at 21:58 PT and found 30/30
  at 01:14 PT (+6 in 3 hours 16 minutes,
  capped at 30, so at most about 6 ticks in
  about 2 hours). 0319 found 5/30 at 03:06 PT
  after 0113's zeroing at about 01:21 PT (+5
  in about 105 minutes, about 5 ticks). 0334
  left the count at 1/30 at about 03:59 PT
  (live on both Quick Construction and Rallied
  Attack, the same count on both nodes, so the
  remaining count is shared across tech nodes,
  not per node) and this unit found 3/30 at
  04:41 PT (+2 ticks at about 04:17 and 04:37).
- Implication: the metadata's flat "30 donations
  a day, burn them down early" model is wrong -
  the count is a regenerating pool capped at 30,
  refilling about 1 per 20 minutes. A 0/30 state
  is transient: it lasts only until the next
  tick, which can land seconds after the zeroing
  donation, so the hard closing rule's live
  0/30 read is unachievable in the general case
  and the rule needs a closing standard that
  matches the mechanism (for example, the
  greyed button plus long timer on a zeroing
  donation, bracketed by live reads). Filed as
  GitHub Issue #813 from this unit. The re-read
  unit pattern still applies: each pass drains
  whatever the count holds at its tick.

## Notes

- The "Hold down for easier continuous donations"
  tooltip appeared after the batch of 3, as in
  the 0113 and 0319 units; long-press continuous
  donation remains untested.
- An alliance announcement banner crossed the top
  during the batch ("Obtained 5000 Diamonds from
  Mystery Supply Box") - another player's rumor,
  no action taken.
- No diamonds or money spent. No red-line
  contact. The diamond Donate button was never
  tapped.
