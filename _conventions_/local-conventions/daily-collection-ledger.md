---
title: Daily Collection Ledger
created: 2026-11-01T05:00:00Z
modified: 2026-11-23T09:02:16Z
level: L2
version: 1.4.0
description: The master list of everything collectible or due in one reset day, each line with the live read that closes it
status: active
grounded_in:
  - source: miss audit of 2026-10-31, section 4 umbrella rule
  - source: owner expanded collection checklist of 2026-10-31
  - source: owner direction of 2026-10-31 to reflect and fix
  - source: "organizer 0432 run 2026-11-07 (Refs #147) - the reset-day definition rewritten to the absolute reset instant 02:00 UTC"
---

# Daily Collection Ledger

The master list of everything collectible or due in one reset day, each line with the live read that closes it. This register stays at this path as an entry page; its text was split verbatim into 8 articles in [daily-ledger-sections](daily-ledger-sections/INDEX.md), unchanged and in reading order.

## Adding an entry

Add one small article file `daily-ledger-sections/<entry-id>.md`, named by an entry id that starts with letters (for example `entry-20261123-01.md`), with the frontmatter fields title, created, modified, version and description, then add one line for it at the end of this page: `- [Title](daily-ledger-sections/entry-20261123-01.md) one sentence`. Never edit an existing article.

## Changelog

- 1.3.0, 2026-11-23 - Split verbatim by split_doc.py into 7 articles; --check EQUAL, sha256 7edd451b87d4; the unsplit 1.2.0 file is commit 6d019ade
- 1.4.0, 2026-11-23 - Re-split verbatim into articles of 300 words or fewer (split_doc.py with a 300-word limit); --check EQUAL, sha256 7edd451b87d4; the 1.3.0 split is in git history.

## Articles

- [Daily collection ledger](daily-ledger-sections/daily-collection-ledger.md) - The master collection list for one reset day - the day runs from the...
- [The closing standard](daily-ledger-sections/the-closing-standard.md) - the-closing-standard - Every line closes on a live read from that day - a counter, a...
- [The lines](daily-ledger-sections/the-lines.md) - the-lines
- [Base and harvest](daily-ledger-sections/base-and-harvest.md) - base-and-harvest - Food bubbles - producing unit, harvest.
- [Shop, passes and VIP](daily-ledger-sections/shop-passes-and.md) - shop-passes-and - Drone components - passes and shop checks.
- [Missions, mail and alliance](daily-ledger-sections/missions-mail-and.md) - missions-mail-and - Daily activity chests - daily-missions.
- [Trucks, train, radar, duel part 1](daily-ledger-sections/trucks-train-radar-p1.md) - trucks-train-radar - Trucks - dispatch 5 of 5, plunder 4 of 4 - trucks.
- [Trucks, train, radar, duel part 2](daily-ledger-sections/trucks-train-radar-p2.md) - trucks-train-radar - Crystal - crystal-shop.
