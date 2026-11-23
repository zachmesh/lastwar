---
title: Audit of the run articles against the dated records
created: 2026-11-23T08:57:00Z
modified: 2026-11-23T08:57:00Z
version: 1.0.0
description: Read-only coach audit of the 1,767 run-star articles in the activities folders - duplicate of a record, unique rule or lesson, or no record - with the method, totals by class and activity, and the reconciliation with Steer B
status: done
activity: coach
run_id: coach-2026-11-23-0055
trigger: coordinator assignment A-20261123-0853-coach, Steer B finding IMP-20261123-12
started_at: 2026-11-23T08:53:00Z
finished_at: 2026-11-23T08:57:00Z
duration_seconds: 240
verified: no
grounded_in:
  - source: _activities_/<activity>/run-*.md, 1,767 files, and the primary files under _records_/<date>/
  - source: run-articles-audit-method.py in this folder, run on the checkout after PR 877
---

# Run article audit

Nothing was moved, renamed or deleted; `git status` shows no change under `_activities_`. Rows: [audit](run-articles-audit.csv); totals by activity: [totals](run-articles-audit-totals.csv); script: [method](run-articles-audit-method.py), re-runnable.

## Method

1. The article time comes from `run-YYYYMMDD-HHMM`, local Pacific, as the records use.
2. Candidate records are all primary files under `_records_/<date>/` within 45 minutes, across midnight; records that only cite others (knowledge-organization, pr-*, tool-development, integration, queue-planning, retro-review) are excluded. A record the article cites by path is also a candidate.
3. Numbers: comma-grouped, decimals, K, M, G or percent suffixes, bare 3-digit and 5-or-more-digit integers; years, clock times and small integers are ignored.
4. Share = distinct article numbers found in the best candidate. Class a: share 0.50 or more. Class b: share below 0.50, or fewer than 3 numbers. Class c: no candidate.

## Result

| Class | Files | Words |
|---|---|---|
| a duplicate of a record | 1,108 (62.7%) | 393,089 (70.8%) |
| b unique rule or lesson | 554 (31.4%) | 127,199 (22.9%) |
| c no record | 105 (5.9%) | 34,793 (6.3%) |

Total 1,767 files and 555,081 words, as Steer B counted; 31 of 38 activity folders have run files. Class a median share is 0.94. Window-only classes were 1,103, 557 and 107; citations moved 6 files.

**Against Steer B.** 1,498 articles with a number map within 45 minutes (he found 1,491); median share 0.91 over 1,244 (his 87 percent over 1,180). His 276 unmapped is the 105 class c plus 162 articles with a record nearby but no numbers to map. Of class c, 96 have a record that day outside the window, 9 have nothing that day.

**Class b is an upper bound.** 418 files (80,137 words) have fewer than 3 numbers, so the number test cannot say; their word overlap with a nearby record has median 79 percent and 285 reach 70 percent, which suggests narrative duplicates (indicative, domain words inflate it). The other 136 files (47,062 words) have a median share of 25 percent. If the 285 are duplicates, class b is about 269 files.

**Largest by duplicate words.** alliance-donations 53,306 of 72,465; perception-scout 50,318 of 71,223; radar-tasks 34,364 of 49,735.

## Limits

Classes rest on numbers, not reading. I read six rows across the classes; they showed articles citing their evidence record, which is why cited records were added. Class b holds the decision for the owner: a new local type or topic articles. Duplicates are for later marking superseded, never deletion (C2).
