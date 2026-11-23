---
title: Queue Planning T1 Second Trial Retired And Donation Logging 2500 2026-11-23
created: 2026-11-23T02:21:00-08:00
modified: 2026-11-23T02:21:00-08:00
level: L0
version: 1.0.0
description: Planner pass on the Researcher's decision that the second T1 trial is not needed - the unit retired, timer and count logging added to the two unclaimed regular donations units, and T2 narrowed now that level 5 is read
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-0221-t1-002-and-logging
trigger: Researcher message on trial 002 and the timer evidence
started_at: 2026-11-23T02:20:00-08:00
finished_at: 2026-11-23T02:21:00-08:00
verified: unit files read back after each edit; validate exit 0
grounded_in:
  - source: _records_/2026-11-22/research/donation-timer-evidence.csv
  - source: _records_/2026-11-22/alliance-donations/1012-t1-test.md
---

# T1 second trial retired and donation logging, 2500

## 1. Decision

The Researcher decided trial 002 is not needed. One landing was the pre-registered criterion and the 1012 record meets it. A count read after the timer cannot separate a landing followed by one refill from an eaten tap, and four such post-timer reads already sit in the records, all 1/30. `donations-playbook-t1-2026-11-23-002` is retired, its expiry set past so `sync` expires it. `-001` was retired earlier.

## 2. Logging instead of a unit

`donations-2026-11-23-0203` and `donations-2026-11-23-1630` now carry a logging block: at the last Donate tap write the cooldown timer value and the UTC time to the second, and at entry write the donation count and the time. That entry count is the post-timer read of the 10:12:44Z tap and the refill data. The refill of about one count per 20 minutes stays a guess until a second read. No taps are added. The units minted later by `plan` and `sync` will not carry the block, so the rule needs to sit in the donations rule digest, which is the scribe's file.

## 3. T2

Level 5 is read (Rapid Siege 5/10 at 600 coin, in the 1012 record, a fit), so `donations-playbook-t2-2026-11-23-001` now owes level 1 (predict 200) and any of levels 3, 4, 6 or 10. Its window stays 10:00Z to 14:45Z. T3 is unchanged.
