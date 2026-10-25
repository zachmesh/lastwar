---
title: Records
created: 2026-10-25T17:56:00Z
modified: 2026-10-25T19:07:00Z
version: 1.2.0
description: Append-only records of play on the game account, organised by date, then activity type, then one file per execution
grounded_in:
  - source: human-authored
---

# `_records_`

Type folder, from reflection's vocabulary — append-only audit records
of play on the game account, organised **by date first**.

- One instance folder per date, named by its date, for example
  `2026-10-25/`. Its `INDEX.md` is the day record — sessions, snapshots,
  disclosures, and the index of that date's activity records.
- Inside a date, one subfolder per activity type, named as in
  `_activities_`. A subfolder exists for every activity evaluated that
  date, so absence also reads as not evaluated.
- Inside an activity subfolder, **one file per execution**, added one at
  a time. Each file states performed, performed in part, checked only,
  or not performed, with its session window and outcome.

Records are trajectories under constitution C1 and are never edited or
deleted once committed. A correction is a new appended record. The one
exception so far is layout, not content — on 2026-10-25 the owner
directed this date-first layout and the earlier records were moved into
it unchanged, as noted in the 2026-10-25 day record.

## Contents

- [`2026-10-25/`](2026-10-25/INDEX.md) — install, login, first snapshot,
  and the first daily round, split per activity.
