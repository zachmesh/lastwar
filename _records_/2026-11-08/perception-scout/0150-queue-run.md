---
title: Perception scout queue run 0150
created: 2026-11-08T09:50:00Z
executor: ticker-0137
unit: scout-midday-scout-mid-2026-11-03-004
status: partial
---

# Perception scout - stale midday chain, store-group remainder blocked by the Star Ceremony

Unit scout-midday-scout-mid-2026-11-03-004 (priority 2, chain
scout-mid-2026-11-03, chain seq 4). Session window about 01:44-01:50
PST on the Mac mini Last War window (computer sessions cc-69 and
cc-70; cc-69 ended and cc-70 started mid-unit after a clock check,
no game state lost). Observe-only: nothing claimed, fought,
dispatched, donated, signed up for, or bought. Result: partial -
the game was found on the Alliance Star Ceremony overlay and the
ceremony held the screen for the whole unit, so the store-group
remainder the unit owns (VIP panel, daily missions panel, Weekly
Deal page) was never reached and is carried to the successor in
the same chain.

## Entry state, read live

- The game was found on the [AP3X] Alliance Star Ceremony
  (Event 40) bonus-rewards slide, left there by the 0122 unit
  of the ticker-0104 pass: "Thank you all for ... to claim
  your rewards", a purple gem 4.0K, "Here are your bonus
  rewards", a "Send emotes to the winner to receive rewards"
  tooltip with a blue Go button, and a chest counter 0/1 at
  top right. The bottom row reads 10, 11, 12, 13, MVP and a
  chest icon, the chest glowing.
- No base screen, HUD, or shop state was readable in this
  unit - the ceremony overlay covers the whole window. No
  different-device dialog, no login demand. The star-ceremony
  regular owns the ceremony claim; its unit is already queued.

## Ceremony slides, read live in this unit

The ceremony advanced slide by slide under the controls below.
Each slide has 2-4 stages (title, winner, runners, host speech)
and each tap advances one stage.

- Slide 10, Doom Elite Slayer: winner JerryLogDog - "Launch a
  Rally and eliminate Doom Elite 223 time(s) this week", 42
  hearts, 7 / 1 / 3 on the other emote counts. Runners
  SKRyZeRZ 181, xChroniApex 171. Host line: "I'm still buzzing
  with excitement - your passion is inspiring!"
- Slide 11, Alliance Sponsor: winner DCna8ive - "Donated
  178,000 point(s) this week". Runners kaBoom420 166,850,
  Texan Apex 103,300. Host line: "Let's leave our
  encouragement and blessings to the winners."
- Slide 12, Good Helper: winner 5tarFall - "Helped allies
  2,807 time(s) this week". Runners DCna8ive 2,738, VOUGoApex
  2,543. Host line: "Once again, thank you all for the
  amazing Energy."
- Slide 13, Shining Star: winner Abŷss Apex - "Desert storm
  points increased by 4,362,901 compared to last week".
  Runners 2,113,189 and 1,937,365 (names garbled in OCR,
  unread). A top banner crossed the screen during this slide:
  "Important: President HawksMav appointe..." (truncated, full
  text unread - the same President banner the 0016 unit saw
  truncated on 2026-11-03).
- MVP slide: winner SKRyZeRZ - "Earned 9 Performance
  Point(s) this week". Runners Rage Apex, Abŷss Apex.
- Chest slide: the bonus-rewards slide again (4.0K gem,
  "Here are your bonus rewards", chest 0/1, Go tooltip
  still showing).

## The loop - the ceremony cycles, it does not exit on its own controls

- After the MVP slide the ceremony returned to the chest /
  bonus-rewards slide, and a back-arrow tap from the chest
  slide advanced to the "Next UP ... presenting the award
  for ..." transition and then to slide 10 (Doom Elite
  Slayer) again. The ceremony loops: chest -> 10 -> 11 ->
  12 -> 13 -> MVP -> chest.
- Advancement mechanics, measured in this unit: a centre tap
  at norm 500,500 advances one animation stage; the blue
  skip button at norm 806,938 advances one slide; the
  bottom-left back arrow at norm 170,914 advances slides
  (and loops from the chest slide back to slide 10). A skip
  tap at norm 800,914 (above the button) did nothing - the
  button's active point is low, near y 938. Two taps on the
  skip point that report no change still changed the slide
  content, so the tool's no-change report is unreliable on
  this screen; judge by the image, not by the status line.
- The only untested forward action is the Go button ("Send
  emotes to the winner to receive rewards", chest 0/1): it
  is the ceremony's claim path, so it was NOT tapped in this
  observe-only unit. Whether the ceremony exits after the
  emote is sent is the open exit question, and it belongs to
  the star-ceremony regular, not to a scout unit. The emote
  bar (heart plus five faces) appears at the bottom of the
  award slides while the ceremony runs.

## Red dot accounting

- Seen in the walked surface (the ceremony): 1 signal - the
  chest 0/1 counter with its Go tooltip.
- Explained 1: the chest maps to the star-ceremony regular
  (claim the 4.0K gem bonus), whose unit is already queued.
- Unexplained red dots: 0.
- Unknown items: 3 - (a) the ceremony exit route (Go/emote
  untested, star-ceremony regular's); (b) slide-count
  reconciliation: the 0122 unit read "6 slides" with opening
  slides "S2 Big Shot - Texan Apex" and "Little Sun / Nuna
  Knuckles", while this unit read the six bottom-row slides
  (10, 11, 12, 13, MVP, chest) plus the bonus slide - whether
  the S2 awards are opening slides before rank 10 or a
  separate presentation is unresolved; (c) the full President
  HawksMav banner text.
- Observed items: 14. Evidence: the day observation file
  `_records_/2026-11-08/perception-scout/observation.md`
  (appended section for this unit).

## Not walked, and why

- VIP panel, daily missions panel, Weekly Deal page: the
  ceremony overlay blocked the base screen for the whole
  unit; all three are carried, not forced, to the successor
  in chain scout-mid-2026-11-03. The Weekly Pass reset
  figure (18:00:00 vs the standing 19:00 note) from the 2209
  unit is still an unanswered re-read item for the successor
  or the next scout-store unit.
- No train, boarding banner, zombie sighting or other base
  signal was readable in this unit - the overlay covers
  everything, so no such signal is asserted either way.

## Follow-up

- Successor chain unit enqueued in scout-mid-2026-11-03 for
  the VIP panel, the daily missions panel and the Weekly Deal
  page, with a first step of re-checking whether the ceremony
  is still open (if the star-ceremony unit has run, it is
  gone; if it is still open, the successor re-tests the exit
  only through the star-ceremony claim path, never by
  claiming inside a scout unit).
- The ceremony-loop finding is a queue-level note: while the
  ceremony is open, every unit that needs the base screen
  blocks on it, and only the star-ceremony unit can clear it.
