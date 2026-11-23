---
title: 4. Crystal and the zero sweeps, as queued
created: 2026-11-23T09:01:51Z
modified: 2026-11-23T09:01:51Z
version: 0.1.0
sequence: 7
description: Crystal is modelled as its own activity type in _activities_/crystal-shop/, registered in the activities index, and
---
## 4. Crystal and the zero sweeps, as queued

- Crystal is modelled as its own activity type in
  `_activities_/crystal-shop/`, registered in the activities
  index, and one priority 1 unit is in the inbox -
  crystal-shop-2026-11-01-0500. Its body carries the whole job -
  Store, then the Building section, then the Crystal Shop tab;
  read the tab live, record the mechanism, claim what is
  claimable under the red lines, and backfill the mechanism into
  the metadata. Under R5 it stays named in every round summary
  until it closes.
- The zero sweep pair for the 2026-11-01 reset is enqueued as the
  chain pre-reset-sweep-2026-11-01 - unit 001 actionable from
  17:30 local and unit 002 from 18:30 local, both expiring at the
  19:00 reset (2026-11-02T03:00:00Z). Each walks the ledger item
  by item; a line not at zero gets a priority 1 unit of its own
  type enqueued before the sweep closes, named in the sweep
  record.

