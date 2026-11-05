---
title: Alliance donations unit interrupted by device takeover dialog
created: 2026-11-02T18:10:00Z
modified: 2026-11-02T18:10:00Z
version: 1.0.0
description: Ticker-1755 donations unit, partial, zero donations landed, device dialog takeover applied once
status: unverified
grounded_in:
  - source: live game screen reads 2026-11-02 about 18:04 to 18:09 local
---

# Alliance donations - partial, takeover dialog (ticker-1755)

- Unit: donations-2026-11-02-1344, regular donations,
  priority 2, no chain. Status: partial. Zero coin
  donations landed, zero diamond donations (the
  diamond button was never tapped).
- Tracker untouched (partial units never mark the
  tracker; the next tick re-produces the regular).

## Entry - worked, grounding corrected

- The game was left on the Alliance panel by the
  previous unit of this pass, so entry started there.
  A first Techs-tile tap at norm 686,735 opened
  Strength Ranking instead - that tap lands on the
  row below the intended tile. The tile centres were
  then measured with the visual grounding tool on the
  panel capture: Help centre 687,500, Wars centre
  313,500, Techs centre 687,672, Strength centre
  687,758. A tap at the measured Techs centre
  687,672 opened Alliance Techs at once.
- Lesson carried from this unit, superseding the
  plus-90 correction written in the same pass's scout
  record (perception-scout/1801-queue-run.md): tap
  coordinates must come from measured grounding
  boxes or OCR element positions in tap space, never
  from image-pixel conversion of a screenshot. The
  image-pixel conversions used earlier in this pass
  underestimated y by roughly 40 to 90 norm units;
  every measured-centre tap in this unit landed
  exactly. A correction appendix is added to the
  scout record rather than rewriting it.
- This working entry (base Alliance icon, then the
  measured Techs centre) bears on the donations
  entry blocker recorded by the ticker-1412 unit
  (three straight entry failures) and commented on
  issue 171: the route itself works, and the earlier
  failures are consistent with grounding error, not
  with a broken route. The next donations unit
  should enter by the measured centres above.

## Alliance Techs read, about 18:07

- Development tab: Expert Nurse 1/10 at the top;
  Garrison HP 7/10, Garrison Attack 7/10, Garrison
  Defense 7/10 carrying the recommended thumbs-up
  marker; a further 7/10 node below the fold, not
  identified. The War tab was not opened.
- Footer: Tech Donation Today 0, with the trophy
  icon and the line "Requires at least 1000
  contribution points to earn the reward".
- Garrison Defense donation panel (recommended
  node, measured centre 730,530 on the Techs
  capture): "Increased Hero Defense in Defense
  Support for Alliance members", Current +7%,
  Next Level +8%. Donate buttons: diamond 2
  ("Unlimited Attempts", never tapped) and coin
  800 (active, not greyed). Donation Count read
  live as 30/30.

## Donation Count ambiguity - flagged for the next unit

- The 30/30 read conflicts with the ticker-1729
  zero-sweep note ("donations, last live count 1
  remaining"). Under the activity's hard rule the
  Donation Count is a remaining count (it fell
  30 to 25 after five donations on 2026-10-25),
  which would read 30/30 as 30 remaining and the
  Tech Donation Today 0 as corroboration that
  nothing has been donated today - but that
  reading is NOT asserted here, because the
  1729 note says otherwise and this unit landed
  no donation to test the counter's direction.
- Direction to the next donations unit: re-read
  the Donation Count live on the Garrison Defense
  panel first. If it still reads 30 remaining (or
  any positive remaining count), donate with the
  coin button only until the count reads 0 live or
  the button greys, then stop for that run. If it
  reads 0 remaining, record checked-only. Never
  close on arithmetic; only on a live read in
  that same unit.

## Device takeover dialog - owner rule applied once

- While the Garrison Defense panel was open, the
  dialog "Your account is currently active on a
  different device!" appeared. Per the owner rule
  of 2026-10-27, Confirm was tapped (first at a
  mis-grounded point from image-pixel conversion,
  which missed; then at the measured Confirm
  centre 501,568, which landed). Takeover count
  this pass: 1. The app exited as the rule states;
  it was relaunched and returned straight to the
  base screen with no login or verification demand.
- The dialog did not recur after the relaunch in
  this pass. No second takeover was needed, so the
  contested stop condition (two takeovers then a
  third dialog) was not reached.
- The unit's game window ended at the token lease
  boundary: after the relaunch the game sat on the
  base screen and no further game input was made,
  so the donation panel was not re-entered and no
  donation was attempted in this unit. The game
  was left safe on the base screen.

## Side reads in this unit

- Strength Ranking, Power tab, read on the
  mis-tap: rank 1 ItStartsWithaDream 270,322,299;
  rank 2 Abuss Apex 216,125,369; rank 3 StarFall
  207,761,433; rank 4 papillon707 203,535,837;
  rank 5 Missile Apex 198,709,407; rank 6 Echo Apex
  196,836,790; own account rank 31, R3, Bears Lair,
  power 149,311,528 - unchanged from the 13:53
  scout read. This confirms the 146,610,448
  mid-HUD figure seen in this pass is NOT account
  power; its identity remains unknown.
- Base HUD after relaunch: top row first value
  405.8M (was 387.7M at the 17:58 read), furnace
  toast [22/60] still showing, 99+ badge still
  showing, chat ticker lines seen only.

## Result statistics

- donations_landed: 0
- coin_spent: 0
- donation_count_read: 30/30
- tech_donation_today_points: 0
- recommended_tech: Garrison Defense
- device_takeovers: 1
- verified: false
