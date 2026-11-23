---
title: 4. Unit schema part 1
created: 2026-11-23T09:03:48Z
modified: 2026-11-23T09:03:48Z
version: 0.1.0
sequence: 8
description: The unit frontmatter is the single structured source for the unit - what the task is,
---
## 4. Unit schema

The unit frontmatter is the single structured source for the unit -
what the task is, where it is (the state subfolder plus the claim
fields below), and what it produced (the result section in section
5). Status, statistics and reports are gathered from these fields by
`_tools_/queue.py stats`, never by scraping prose. Values are kept
colon-free except timestamps, as elsewhere in this repository.

| Field | Meaning |
|---|---|
| `unit` | unit id, matches the file name |
| `regular` | regular id from _tools_/regulars.json |
| `activity` | activity type folder name for the run record |
| `segment` | owning segment under the current routine, kept for reporting |
| `priority` | 1 expiry-critical, 2 windowed, 3 standard, 4 background |
| `created_at` | when the producer wrote the unit |
| `expires_at` | after this the unit is worthless or degraded (reset, phase end); empty when none |
| `planned_for` | the cadence window (time slot) this unit serves; with `regular` it is the unit's identity |
| `not_before` | the unit may not be claimed before this time; set to the window start for future windows |
| `window` | execution window constraint, for example an Arms Race phase or a duel posture; empty when none |
| `est_minutes` | typical minutes for this task type, learned per section 5; enqueue rejects anything above the 15 minute cap |
| `chain_id` | continuation chain this unit belongs to; empty for one-off units |
| `chain_seq` | position inside the chain, 1 based |
| `attempts` | how many times the unit has been claimed |
| `max_attempts` | claims allowed before the unit dead-letters as failed (default 3) |
| `claimed_by` | executor name once claimed |
| `claimed_at` | claim time |
| `lease_until` | claim expiry; past it the unit returns to inbox |

Priority classes from the current regulars.

