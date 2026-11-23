---
title: Queue Planning Ledger Troop Columns And Secrets Claim Unit 2345 2026-11-22
created: 2026-11-22T23:45:00-08:00
modified: 2026-11-22T23:45:00-08:00
level: L0
version: 1.0.0
description: Planner pass after the coordinator accepted the candidate ledger - schema v1.1 adds tier, count and capacity_used for troop rows without a new category, and a Secrets claim unit is minted for the 4-hour UR task at 08:50Z to 09:25Z
status: done
activity: queue-planning
run_id: queue-planning-2026-11-22-2345-ledger-v1-1-and-secrets-claim
trigger: coordinator decisions after A-20261123-0741-planner
started_at: 2026-11-22T23:42:00-08:00
finished_at: 2026-11-22T23:46:00-08:00
verified: the new unit read back and validate exit 0; the v1.1 CSV parsed with 13 columns and 6 rows; the troop arithmetic recomputed
grounded_in:
  - source: _records_/2026-11-22/queue-planning/2345-candidate-ledger-template.csv
  - source: _records_/2026-11-22/queue-planning/2340-candidate-ledger.md, the accepted v1.0
  - source: _activities_/troop-training/changelog-section-p11.md, entries 1.38.0 and 1.41.0
---

# Ledger v1.1 and the Secrets claim unit, 2345

## 1. Schema v1.1

[The template](2345-candidate-ledger-template.csv) keeps the 10 accepted columns and adds three, filled only on `train` and `promote` rows and left empty elsewhere:

- `tier`: the troop tier as the panel shows it, for example T8, T9, or `T8 to T9` for a promotion.
- `count`: troops in the batch or promotion.
- `capacity_used`: units this batch occupies, with the Drill Ground figure read live, or `unread`.

Power per troop and power per capacity unit are derived at ranking time, not stored. No new category is needed. The v1.0 file is superseded and left untouched. Rows now: the Hut, a T8 batch of 666 (1,063 per troop), a T9 batch of 313 (1,352 per troop), a research item, a promotion row and a hero row. The promotion and hero rows are `unread` and cannot be ranked. One caution: the 289 power per troop between T8 and T9 is arithmetic on two batch figures, unverified until the promotion panel is read.

## 2. Secrets claim unit

`secrets-2026-11-23-0742`, priority 2, 6 minutes, `not_before` 2026-11-23T08:50:00Z, `expires_at` 2026-11-23T09:25:00Z, for the 4-hour UR task due about 08:51Z. The coordinator still sends the claim; this makes the queue cover a missed reminder. The brief claims every finished task in one tap before it can be plundered, takes assists, and if nothing has finished records the earliest finish and stops. Snapshot windows stay clear of 08:45Z to 09:05Z.

## 3. Held

No troop-training change is staged; the existing training units stay as they are. The ranking waits for the charter and the snapshot. Interim `serves:` first-body-line is accepted; the real field is the toolsmith's. The snapshot units are staged when the scout's protocol lands in `_records_/2026-11-22/perception-scout/`, expected about 08:15Z.
