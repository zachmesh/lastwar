---
title: Item 5. Alliance Duel daily total against the 3.6M target
created: 2026-11-23T08:37:03Z
modified: 2026-11-23T08:37:03Z
version: 0.1.0
sequence: 20
description: Verdict - cannot be confirmed from the records for either day.
---
### Item 5. Alliance Duel daily total against the 3.6M target

Verdict - cannot be confirmed from the records for either day. No
gap figure can be computed, and none is estimated here.

- No record on 2026-10-30 or 2026-10-31 reads a personal Alliance
  Duel daily total. The folders named alliance-duel contain only
  Star Ceremony checks, because the star-ceremony regular maps to
  the alliance-duel activity - so the duel score has no record
  home of its own.
- Mail records prove a Duel Progress and Alliance Duel Individual
  Reward mail existed and was listed, but no score was read from
  it - `_records_/2026-10-30/mail-rewards/1937-queue-run.md`,
  `_records_/2026-10-30/mail-rewards/2313-queue-run.md`,
  `_records_/2026-10-31/mail-rewards/0317-queue-run.md` and
  `_records_/2026-10-31/mail-rewards/1947-queue-run.md`.
- Fragment scores do exist (Arms Race phase scores, radar points),
  but none of them is a duel daily total and this audit does not
  substitute them. The record dates also straddle duel days - the
  2026-10-30 folder spans duel Day 5 and the start of Day 6 at the
  19:00 reset - so a per-duel-day total cannot be reconstructed
  after the fact from these files.
- Result - 2026-10-30 gap against 3.6M, not readable in the
  records. 2026-10-31 gap against 3.6M, not readable in the
  records.

Prevention rule 5 - one unit per duel day opens the duel panel
before the 19:00 reset and reads the personal daily total live,
recording total and gap against the 3.6M target the owner set.
The Duel Progress mail is a cross-check only. A day with no total
read is reported as total unread, never as total assumed.

