---
title: Review of the 100 cross-activity class-a rows
created: 2026-11-23T09:46:00Z
modified: 2026-11-23T09:46:00Z
version: 1.0.0
description: Read-only coach review of the 100 duplicate run articles whose mapped record sits in another activity's folder - target exists, numbers held, same unit - with the 14 rows not to mark superseded, and the donation 1/30 evidence
status: done
activity: coach
run_id: coach-2026-11-23-0145
trigger: coordinator review request after the scribe's block 1
started_at: 2026-11-23T09:42:00Z
finished_at: 2026-11-23T09:46:00Z
duration_seconds: 240
verified: no
grounded_in:
  - source: run-articles-audit.csv and the primary records, tested by run-articles-cross-review-method.py in this folder
  - source: the alliance-donations records of 2026-11-04, 11-11 and 11-22 named below
---

# Cross-activity review

My audit has the same 100 rows as the scribe (9.0 percent of 1,108 class a; 14 in alliance-donations, shop-claims and troop-training). All 100 targets exist; the shared-number share is 0.50 to 1.00, median 0.78 (the scribe's 57 to 100 percent counts differently). Nothing was moved or edited in `_activities_`.

## Tests

1. Same unit: a unit id named in the article (regular-date-slot) also appears in the record, or the article cites the record.
2. Different unit: both name unit ids and none is shared, with no citation, is a wrong match.
3. Distinctive numbers: shared numbers found in at most 30 primary records, so a repeated HUD value is not evidence.
4. The record names the article's activity.

## Result ([all 100](run-articles-cross-activity-review.csv))

| Verdict | Rows |
|---|---|
| confirm: same unit id 53, cites the record 15 | 68 |
| plausible: 3 or more distinctive numbers shared, or 2 of 2 with the activity named | 18 |
| weak: thin evidence | 6 |
| wrong: different unit | 8 |

So 86 of 100 are sound cross-activity maps: a scout sweep or ticker pass writes one record that covers several activities.

## Do not mark superseded: 14 ([list](run-articles-not-superseded.csv))

Eight wrong, six weak. In block 1: troop-training `run-20261101-1651` names unit training-2026-11-01-1403, but its matched record is survivors-2026-11-01-1403; it has no record, so class c, and a mark already made should be reverted. Three rows have a better target, their own cited record, which holds too little: daily-activities `run-20261111-1940-p1` to queue-planning `1940-run.md` shares 60 percent of 10 numbers (class a if remapped); perception-scout `run-20261109-0606-p1` to its `0606` record 38 percent; radar-tasks `run-20261104-2334-p1` to its `2334` record 33 percent (both class b).

## Donation 1/30 premise

Open. A tap from a live 1/30 landed on all three dates, but the cooldown timer hid the count each time, so no live 0/30 was read: 2026-11-04 `1046-queue-run.md:62` (test tap, button greyed 00:16:35); 11-11 `0434-queue-run.md:145` (taps from 1/30, tap 3 eaten, tap 4 landed); 11-22 `0319-queue-run.md` (one more dispatched at live 1/30). The 11-22 `0359` unit made no tap from 1/30. The researcher's test: tap at live 1/30, wait out the timer, read the count.

## Limits

Queue-planning records are excluded from the candidate set, so articles about planner units map poorly. Counts only; no article was read in full except the flagged ones.
