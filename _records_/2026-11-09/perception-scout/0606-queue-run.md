---
title: Scout pass 0606
created: 2026-11-09T14:06:00Z
modified: 2026-11-09T14:18:00Z
version: 1.0.0
description: Partial perception-scout pass by ticker-0604 - base, HUD, Events hub, Mail
---

# Scout pass 0606 - perception-scout (partial)

- Unit: scout-midday-2026-11-08-0700, executor ticker-0604
- Session: 06:06 to 06:18 local, Mac mini, LastWar window 642x951
- Status: partial - pass incomplete, unwalked surfaces named below
- Slot note: this unit's slot was the 2026-11-08 midday pass
  (07:00 local 2026-11-08); that reset day had already ended at
  the 19:00 reset. The pass was executed against the live game
  instead of being left to expire, and its observations were
  recorded in the current reset day file
  _records_/2026-11-09/perception-scout/observation.md, the first
  perception of reset day 2026-11-09. Nothing was attributed to
  2026-11-08.

## What was walked

- Base screen and HUD, read live from screenshots at 06:05 -
  food 540.1M, iron 864.9M, coin 42.9M, diamonds 6077, stamina
  113, total power 149217331, building queue 1 of 4, research
  1 of 2, many resource bubbles standing, Builders Hut Lv.26
  banner quest 0 of 1, truck icon with a question marker.
- Events hub, full tab-bar scroll - seven tabs: The Age of Oil,
  Arms Race, Winter Battlefield, Desert Battlefield, Wanted
  Boss, Survey Center, Community. No Zombie Invasion tab
  anywhere on the bar - the event is still ended, no chain
  seeded. Level Swap, present 2026-10-30, is gone.
- Arms Race page - Tech Research phase, Contest Segment
  Lv.29-30, phase score 0, chest 6 of 8, timer 03:47:52 left
  at last read, tiers 6250 12500 30000, diamond buy prices
  2360 4800 11800, paths Tech Power plus 1, 1-min Research
  Speed-up plus 10, Buy Packs containing Diamonds plus 30.
  Player rank 8, row value 82500 (meaning unverified).
- Mail - seven categories (Battle Report, Alliance, Event,
  System, Regular, In-app Purchases, Favorite); Event carries
  the one unread mail (top, [AP3x] Abyss Apex train notice,
  4m ago) and a Claim All button; the other five visible Event
  mails are alliance train notices 2h to 8h old. Delete All
  present and untouched.

## Red dots - 6 seen, 5 explained, 1 unexplained

- Events badge 1 - Wanted Boss red dot.
- Mail badge 1 - one unread Event mail.
- Alliance red dot - contents unread, alliance units already
  queued for this window.
- Inventory red dot - contents unread, no owning regular.
- VIP red dot - vip unit already queued for this window.
- 99+ chat badge - visible in the 06:05 base screenshot but
  first classified after the pass closed; carried unexplained
  to the staged 07:00 midday unit. The pass first reported 5
  seen and 0 unexplained; the corrected accounting is 6 seen,
  5 explained, 1 unexplained, and the unit stats were
  corrected to match before delivery.

## Unmatched labels (discovery)

- The Age of Oil - new Events tab against the 2026-10-30 roster.
- Survey Center - new Events tab against the 2026-10-30 roster.
- Both enter discovery as candidates; the diff output below
  names their filings.

## Not walked in this pass

Store by section, VIP page, passes pages, daily missions panel,
alliance panel and station, duel page, radar panel, world map
pins and loot box, Inventory contents, and the Age of Oil,
Survey Center, Wanted Boss and Community event pages. The
staged scout-midday-2026-11-09-0700 unit (07:00 local) covers
them; no duplicate successor was enqueued.

## Scout discipline

Observe only - no claim, fight, dispatch, donation or purchase
was made. The diamond Buy Packs path and the chest diamond
buy prices were read, never tapped. Delete All in mail was
never tapped.

## Diff and follow-up

- tools/scout_diff.py dry run over the observation file -
  29 observed, 8 actionable, 12 to enqueue, 3 already queued,
  9 candidates, 0 unexplained red dots. Outputs in
  /tmp/scout-diff-0604 (not committed - scratch).
- The plan was NOT applied: its three execution enqueues
  (events, help, mail) duplicate units already staged for the
  10:30 and 10:57 PT slots - the diff wrote the local slot
  time as UTC. Filed as Issue #505 (tooling).
- The diff also drafted exploration candidates for info-only
  reads (Total Power total, building queue counts, the absent
  Zombie tab note) - misclassified, not filed. Only the two
  genuine unmatched labels (The Age of Oil, Survey Center)
  stand as candidates, recorded in the observation file; their
  filings are drafted in the diff output for the knowledge
  organiser.
- Unwalked surfaces pass to the staged
  scout-midday-2026-11-09-0700 unit (07:00 local).
