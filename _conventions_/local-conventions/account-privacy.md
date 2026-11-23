---
title: Account Privacy
created: 2026-11-01T07:14:00Z
modified: 2026-11-23T09:06:18Z
level: L2
version: 2.1.0
description: Executors keep the owner's own in-game name and personal identifiers out of the public repository; other in-game names are allowed
status: active
grounded_in:
  - source: owner instruction 2026-11-01 to remove account identifiers holistically and prevent executors from recording them
  - source: owner decision 2026-11-22 22:2x PT (OD-20261123-04) narrowing the scope to the owner's own in-game name and personal identifiers
---

# Account Privacy

Executors keep the owner's own in-game name and personal identifiers out of the public repository; other in-game names are allowed. This register stays at this path as an entry page; its text was split verbatim into 4 articles in [account-privacy-sections](account-privacy-sections/INDEX.md), unchanged and in reading order.

## Adding an entry

Add one small article file `account-privacy-sections/<entry-id>.md`, named by an entry id that starts with letters (for example `entry-20261123-01.md`), with the frontmatter fields title, created, modified, version and description, then add one line for it at the end of this page: `- [Title](account-privacy-sections/entry-20261123-01.md) one sentence`. Never edit an existing article.

## Changelog

- 2.1.0, 2026-11-23 - Split verbatim into articles of 300 words or fewer (split_doc.py with a 300-word limit); --check EQUAL, sha256 5c299210e8c1; the 2.0.0 single file is in git history.

## Articles

- [Account privacy](account-privacy-sections/account-privacy.md) - This repository is public.
- [Narrowed scope (owner decision 2026-11-22, version 2.0.0)](account-privacy-sections/day-20261122.md) - day-20261122 - The owner's own in-game name is the one name that must never appear.
- [Information that stays out of repository content](account-privacy-sections/information-that-stays.md) - information-that-stays - The owner's own in-game name and any alias of it.
- [Exception to C1 (records immutable), recorded 2026-11-23 and](account-privacy-sections/day-20261123.md) - day-20261123, executor-writing-rules, enforcement-section - By explicit owner decision the owner's own in-game name was redacted from the current...
